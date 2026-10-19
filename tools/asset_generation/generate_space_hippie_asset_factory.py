"""Space Hippie Asset Factory — Blender 4.x, no external packages.

Run from repository root:
  blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category all --count 10 --seed 100
  blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category buildings --count 25 --seed 2026
  blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category vehicles --count 15 --seed 42
  blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category street --count 40 --seed 77
  blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category npcs --count 30 --seed 11

Each run writes separate GLBs under assets/3d/generated/<category>/.
Seeds make a batch reproducible. Different seeds generate different batches.
These are stylized low-poly first-pass models; inspect and curate before production.
NPCs are static pose models (not rigged or animated yet).
"""
import bpy, math, os, random, argparse
from mathutils import Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_ROOT = os.path.join(ROOT, "assets", "3d", "generated")
PALETTE = {
    "ink": (0.035, 0.045, 0.065, 1), "metal": (0.20, 0.25, 0.28, 1),
    "steel": (0.40, 0.44, 0.43, 1), "cream": (0.78, 0.66, 0.46, 1),
    "rust": (0.52, 0.20, 0.10, 1), "teal": (0.035, 0.32, 0.34, 1),
    "blue": (0.08, 0.22, 0.52, 1), "plum": (0.32, 0.10, 0.29, 1),
    "yellow": (0.95, 0.55, 0.08, 1), "glass": (0.025, 0.20, 0.27, 1),
    "cyan": (0.02, 0.75, 0.95, 1), "pink": (1.0, 0.035, 0.28, 1),
    "lime": (0.45, 0.95, 0.12, 1), "white": (0.85, 0.88, 0.80, 1),
    "wood": (0.25, 0.14, 0.08, 1), "concrete": (0.34, 0.33, 0.30, 1),
    "skin_a": (0.72, 0.43, 0.29, 1), "skin_b": (0.35, 0.19, 0.13, 1),
    "skin_c": (0.88, 0.66, 0.48, 1), "alien_green": (0.22, 0.56, 0.34, 1),
    "alien_blue": (0.20, 0.48, 0.72, 1), "alien_purple": (0.48, 0.26, 0.62, 1),
    "alien_orange": (0.86, 0.38, 0.16, 1), "eye": (0.008, 0.012, 0.02, 1),
}
EMISSIVE = {"cyan", "pink", "lime"}
MATS = {}

def mat(key):
    if key in MATS: return MATS[key]
    color = PALETTE[key]
    m = bpy.data.materials.new("SH_" + key)
    m.diffuse_color = color; m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Metallic"].default_value = 0.62 if key in ("ink","metal","steel") else 0.08
    bsdf.inputs["Roughness"].default_value = 0.42 if key == "glass" else 0.72
    if key in EMISSIVE:
        bsdf.inputs["Emission Color"].default_value = color
        bsdf.inputs["Emission Strength"].default_value = 2.4
    MATS[key] = m
    return m

def reset():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

def cube(name, loc, dims, material, bevel=0.025):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(mat(material))
    if bevel:
        mod=o.modifiers.new("Hard-surface bevel","BEVEL")
        mod.width=min(bevel,min(dims)*0.18); mod.segments=1
        o.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
    return o

def cyl(name, loc, radius, depth, material, verts=8, radius2=None):
    if radius2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=radius, depth=depth, location=loc)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=radius, radius2=radius2, depth=depth, location=loc)
    o=bpy.context.object; o.name=name; o.data.materials.append(mat(material)); return o

def ico(name, loc, scale, material):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1, location=loc)
    o=bpy.context.object; o.name=name; o.scale=scale; o.data.materials.append(mat(material)); return o

def beam(name, a, b, radius, material):
    vec=Vector(b)-Vector(a); o=cyl(name,(Vector(a)+Vector(b))*0.5,radius,vec.length,material,6)
    o.rotation_mode="QUATERNION"; o.rotation_quaternion=vec.to_track_quat("Z","Y"); return o

def export(name, category):
    bpy.ops.object.select_all(action="SELECT")
    selected=list(bpy.context.selected_objects)
    if not selected: return
    bpy.context.view_layer.objects.active=selected[0]
    bpy.ops.object.convert(target="MESH")
    selected=list(bpy.context.selected_objects)
    if len(selected)>1: bpy.ops.object.join()
    obj=bpy.context.object; obj.name=name
    for poly in obj.data.polygons: poly.use_smooth=False
    folder=os.path.join(OUT_ROOT,category); os.makedirs(folder,exist_ok=True)
    path=os.path.join(folder,name+".glb")
    bpy.ops.export_scene.gltf(filepath=path,export_format="GLB",use_selection=True,export_apply=True)
    print("Wrote",path)

PAINTS=["teal","rust","blue","plum","yellow","cream"]
GLOWS=["cyan","pink","lime"]

def building(i):
    w=random.uniform(5,11); d=random.uniform(4,9); floors=random.randint(1,9); fh=random.uniform(2.3,3.1); h=floors*fh
    base=random.choice(PAINTS); trim=random.choice(["ink","metal","cream"]); glow=random.choice(GLOWS)
    style=random.choice(["stacked","offset","tower","wide","industrial","arcade"])
    cube("Building_Main",(0,0,h/2),(w,d,h),base,0.08)
    if style=="offset" and floors>2:
        cube("Upper_Mass",(w*.12,0,h+fh),(w*.68,d*.82,fh*2),random.choice(PAINTS),0.06)
    elif style=="tower":
        cube("Roof_Tower",(w*.2,0,h+1.1),(w*.38,d*.48,2.2),trim,0.04)
        cyl("Antenna",(w*.2,0,h+2.6),.07,1.2,glow,6)
    elif style=="wide":
        cube("Shop_Awning",(0,-d*.55,1.8),(w*.92,.7,.22),glow,.025)
    elif style=="industrial":
        for x in (-w*.28,0,w*.28): cyl("Roof_Vent",(x,0,h+.45,.5)[0:3],.28,.9,trim,8)
    elif style=="arcade":
        for x in (-w*.25,w*.25):
            cube("Facade_Pillar",(x,-d*.52,1.5),(.22,.28,3),trim,.02)
        cube("Sign_Band",(0,-d*.55,2.9),(w*.7,.15,.42),glow,.015)
    # Windows and facade divisions on street-facing side (-Y)
    rows=max(1,min(floors,8))
    cols=max(2,min(7,int(w/1.35)))
    for row in range(rows):
        z=1.0+row*fh
        if z>h-.25: break
        for col in range(cols):
            x=(col-(cols-1)/2)*(w/(cols+0.5))
            if random.random()<.12: continue
            ww=random.uniform(.38,.72); wh=random.uniform(.48,.92)
            cube("Window",(x,-d/2-.035,z),(ww,.07,wh),random.choice(["glass","glass",glow]),.012)
    # Exterior pipes, aircon boxes, signage and rooftop equipment
    for _ in range(random.randint(1,4)):
        x=random.uniform(-w*.42,w*.42)
        cube("Facade_Equipment",(x,-d/2-.12,random.uniform(1.1,max(1.2,h-.5))),(.35,.18,.42),trim,.025)
    for x in (-w*.34,w*.34):
        beam("External_Pipe",(x,-d/2-.08,.2),(x,-d/2-.08,min(h,random.uniform(2.5,5))),.045,trim)
    cube("Roof_Machinery",(random.uniform(-w*.25,w*.25),0,h+.25),(random.uniform(.7,1.6),random.uniform(.6,1.5),.5),trim,.04)

def vehicle(i):
    length=random.uniform(3.4,5.8); width=random.uniform(1.7,2.5); height=random.uniform(.65,1.25)
    body=random.choice(PAINTS); glass="glass"; glow=random.choice(GLOWS)
    kind=random.choice(["coupe","taxi","cargo","patrol","scrap","shuttle"])
    cube("Vehicle_Body",(0,0,.72),(width,length,height),body,.16)
    cab_y=random.uniform(-.2,.45)*length
    cube("Cockpit",(0,cab_y,1.35),(width*.72,length*.35,.58),glass,.15)
    cube("Roof_Panel",(0,cab_y,1.67),(width*.38,length*.18,.08),random.choice(PAINTS),.03)
    # Hover pods and glowing repulsors
    for x in (-width*.42,width*.42):
        for y in (-length*.32,length*.32):
            cyl("Hover_Pod",(x,y,.36),.24,.22,"ink",8)
            cyl("Repulsor_Glow",(x,y,.235),.15,.035,glow,8)
    for side in (-1,1):
        cube("Running_Light",(side*width*.505,-length*.36,.75),(.045,.42,.11),glow,.01)
    if kind=="taxi":
        cube("Taxi_Roof_Sign",(0,cab_y,1.76),(.55,.24,.12),"yellow",.025)
    elif kind=="cargo":
        cube("Cargo_Module",(0,length*.25,1.2),(width*.88,length*.38,.8),random.choice(["cream","rust","teal"]),.07)
        for y in (length*.12,length*.3,length*.45): cube("Cargo_Rib",(0,y,1.62),(width*.9,.06,.06),"metal",.01)
    elif kind=="patrol":
        cube("Lightbar",(0,cab_y,1.72),(width*.55,.16,.1),"pink",.015)
    elif kind=="scrap":
        for _ in range(4):
            cube("Scrap_Panel",(random.choice([-1,1])*width*.52,random.uniform(-length*.3,length*.3),random.uniform(.65,1.1)),(.18,random.uniform(.3,.8),.18),random.choice(PAINTS),.025)
    elif kind=="shuttle":
        for x in (-width*.58,width*.58):
            cube("Side_Fin",(x,0,.75),(.35,length*.55,.16),body,.035)
    # rear engine cluster
    for x in (-width*.24,width*.24):
        cyl("Engine_Nozzle",(x,length*.49,.77),.18,.25,"metal",8)
        cyl("Engine_Core",(x,length*.49+.14,.77),.11,.035,glow,8)

def street_prop(i):
    kind=random.choice(["kiosk","vending","stall","bench","lamp","sign","barrier","vent","generator","antenna","trash","charging","bollard","crate","drone_dock"])
    base=random.choice(PAINTS); glow=random.choice(GLOWS)
    if kind=="kiosk":
        cube("Kiosk_Body",(0,0,1.1),(1.5,1.1,2.2),base,.08)
        cube("Display",(0,-.57,1.25),(.9,.04,.85),"glass",.015)
        cube("Top_Sign",(0,-.58,2.05),(1.2,.08,.22),glow,.015)
    elif kind=="vending":
        cube("Vending_Machine",(0,0,1.0),(.9,.65,2),base,.06)
        for j in range(3): cube("Product_Window",(-.22+j*.22,-.34,1.2),(.16,.035,.65),random.choice(GLOWS),.01)
        cube("Control_Panel",(.29,-.35,.85),(.12,.035,.45),"ink",.01)
    elif kind=="stall":
        cube("Market_Counter",(0,0,.65),(2,1,1.3),base,.04)
        for x in (-.85,.85): beam("Canopy_Pole",(x,0,1.25),(x,0,2.3),.045,"metal")
        cube("Canopy",(0,0,2.3),(2.2,1.35,.16),glow,.04)
    elif kind=="bench":
        cube("Bench_Seat",(0,0,.55),(1.5,.45,.12),"wood",.025)
        for x in (-.58,.58): cube("Bench_Leg",(x,0,.28),(.12,.35,.55),"metal",.02)
        for z in (.82,1.02): cube("Bench_Back",(0,.18,z),(1.5,.1,.12),"wood",.02)
    elif kind=="lamp":
        cyl("Lamp_Pole",(0,0,1.8),.055,3.6,"ink",8)
        beam("Lamp_Arm",(0,0,3.45),(.55,0,3.45),.045,"metal")
        cube("Lamp_Head",(.65,0,3.35),(.5,.35,.18),base,.04)
        cube("Lamp_Lens",(.65,-.19,3.29),(.35,.025,.06),glow,.01)
    elif kind=="sign":
        cube("Sign_Post",(0,0,1.4),(.12,.12,2.8),"metal",.015)
        cube("Sign_Face",(0,-.04,2.45),(1.6,.12,.65),base,.04)
        cube("Sign_Glow",(0,-.11,2.45),(1.25,.025,.12),glow,.01)
    elif kind=="barrier":
        cube("Traffic_Barrier",(0,0,.5),(2,.5,1),random.choice(["yellow","rust","cream"]),.06)
        for x in (-.6,0,.6): cube("Reflector",(x,-.26,.55),(.2,.025,.55),"ink",.01)
    elif kind=="vent":
        cube("Vent_Base",(0,0,.6),(1.2,.9,1.2),"metal",.05)
        for z in (.3,.5,.7,.9): cube("Vent_Slat",(0,-.48,z),(1,.05,.07),"ink",.01)
    elif kind=="generator":
        cube("Generator",(0,0,.75),(1.5,.8,1.5),base,.06)
        for x in (-.4,0,.4): cube("Cooling_Slot",(x,-.42,.85),(.15,.025,.65),"ink",.01)
        cyl("Warning_Light",(.5,0,1.58),.12,.16,glow,8)
    elif kind=="antenna":
        cube("Antenna_Base",(0,0,.3),(.8,.8,.6),"metal",.04)
        cyl("Antenna_Mast",(0,0,1.5),.045,2.4,"ink",6)
        for z in (1.1,1.7,2.2): beam("Antenna_Dish",(0,0,z),(.5,0,z+.18),.07,glow)
    elif kind=="trash":
        for _ in range(7):
            ico("Junk",(random.uniform(-.5,.5),random.uniform(-.4,.4),random.uniform(.12,.5)),(random.uniform(.12,.35),random.uniform(.12,.3),random.uniform(.1,.25)),random.choice(["metal","rust","cream","teal"]))
    elif kind=="charging":
        cube("Charge_Pillar",(0,0,1.0),(.55,.5,2),base,.05)
        cube("Charge_Screen",(0,-.27,1.3),(.32,.025,.5),glow,.01)
        beam("Cable",(.28,0,1.2),(.55,-.15,.55),.035,"ink")
    elif kind=="bollard":
        cyl("Bollard",(0,0,.45),.18,.9,base,8)
        cyl("Bollard_Light",(0,0,.88),.19,.08,glow,8)
    elif kind=="crate":
        cube("Crate",(0,0,.55),(1.05,.9,1.1),random.choice(["wood","rust","teal"]),.035)
        for z in (.15,.95): cube("Strap",(0,-.47,z),(1,.04,.07),"metal",.01)
    elif kind=="drone_dock":
        cube("Dock_Base",(0,0,.2),(1.8,1.4,.4),"ink",.05)
        for x in (-.55,.55): cyl("Dock_Light",(x,0,.43),.12,.08,glow,8)

def npc(i):
    # Static, game-ready low-poly character silhouettes. Forward faces -Y.
    species=random.choice(["human","human","alien","alien","robot"])
    height=random.uniform(1.55,2.05); scale=height/1.8
    outfit=random.choice(PAINTS); trim=random.choice(GLOWS)
    if species=="human": skin=random.choice(["skin_a","skin_b","skin_c"])
    elif species=="alien": skin=random.choice(["alien_green","alien_blue","alien_purple","alien_orange"])
    else: skin="metal"
    torso_z=1.12*scale; head_z=1.62*scale
    # legs and footwear, slight stance variation
    for side in (-1,1):
        x=side*.16*scale; spread=random.uniform(.0,.11)
        hip=(x,random.uniform(-.025,.025),.78*scale)
        foot=(x+side*spread,-.035,.12*scale)
        beam("Leg",hip,foot,.095*scale,outfit)
        cube("Boot",(foot[0],foot[1]-.04,.07*scale),(.22*scale,.34*scale,.13*scale),"ink",.025)
    # torso silhouette: coats, uniforms, tunics, armor
    torso_kind=random.choice(["jacket","coat","armor","tunic","overalls"])
    cube("Torso",(0,0,torso_z),(.55*scale,.34*scale,.68*scale),outfit,.09*scale)
    if torso_kind in ("coat","tunic"):
        cube("Lower_Garment",(0,.015,.76*scale),(.62*scale,.38*scale,.32*scale),outfit,.06*scale)
    if torso_kind=="armor":
        cube("Chest_Plate",(0,-.19*scale,1.18*scale),(.42*scale,.07*scale,.32*scale),"steel",.035)
        cube("Chest_Light",(0,-.235*scale,1.18*scale),(.16*scale,.025*scale,.06*scale),trim,.01)
    elif torso_kind=="overalls":
        cube("Bib",(0,-.19*scale,1.16*scale),(.32*scale,.06*scale,.32*scale),"cream",.02)
    # arms with randomized sleeve angle
    for side in (-1,1):
        shoulder=(side*.31*scale,0,1.32*scale)
        elbow=(side*random.uniform(.36,.48)*scale,-.015,random.uniform(.92,1.13)*scale)
        hand=(elbow[0]+side*.025, -.04, elbow[2]-.20*scale)
        beam("Upper_Arm",shoulder,elbow,.09*scale,outfit)
        beam("Forearm",elbow,hand,.075*scale,outfit)
        ico("Hand",hand,(.075*scale,.07*scale,.08*scale),skin)
    # head shape differs by species
    if species=="robot":
        cube("Robot_Head",(0,-.015,head_z),(.42*scale,.36*scale,.38*scale),"steel",.06)
        cube("Robot_Visor",(0,-.205*scale,head_z),(.31*scale,.035*scale,.12*scale),trim,.02)
        cyl("Antenna",(0,0,head_z+.27*scale),.025*scale,.25*scale,trim,6)
    else:
        head_scale=(.23*scale,.22*scale,.28*scale)
        if species=="alien" and random.random()<.45: head_scale=(.29*scale,.23*scale,.22*scale)
        ico("Head",(0,0,head_z),head_scale,skin)
        if species=="human":
            ico("Hair",(0,.035*scale,head_z+.12*scale),(.23*scale,.21*scale,.12*scale),random.choice(["ink","rust","cream"]))
            for x in (-.085,.085): ico("Eye",(x,-.205*scale,head_z+.015*scale),(.028*scale,.018*scale,.035*scale),"eye")
        else:
            for x in (-.085,.085):
                ico("Alien_Eye",(x,-.205*scale,head_z+.02*scale),(.05*scale,.025*scale,.06*scale),random.choice(["eye","cyan"]))
            # Antennae, horns, side fins, or ear stalks
            feature=random.choice(["antennae","horns","fins","none"])
            if feature=="antennae":
                for x in (-.12,.12):
                    beam("Antenna",(x,0,head_z+.15*scale),(x*1.6,0,head_z+.42*scale),.025*scale,skin)
                    ico("Antenna_Tip",(x*1.6,0,head_z+.42*scale),(.05*scale,.05*scale,.05*scale),trim)
            elif feature=="horns":
                for x in (-.13,.13): beam("Horn",(x,0,head_z+.12*scale),(x*1.5,0,head_z+.34*scale),.055*scale,skin)
            elif feature=="fins":
                for x in (-1,1): ico("Head_Fin",(x*.25*scale,0,head_z),(.13*scale,.07*scale,.19*scale),skin)
    # wearable bag, belt, shoulder pads, and a species-specific detail
    if random.random()<.6:
        cube("Utility_Belt",(0,-.19*scale,.91*scale),(.48*scale,.055*scale,.09*scale),"ink",.015)
    if random.random()<.45:
        cube("Shoulder_Pad",(random.choice([-1,1])*.34*scale,-.01,1.31*scale),(.2*scale,.26*scale,.16*scale),random.choice(["steel","cream",trim]),.03)
    if species=="alien" and random.random()<.5:
        ico("Bioluminescent_Mark",(0,-.235*scale,1.22*scale),(.045*scale,.025*scale,.12*scale),trim)

BUILDERS={"buildings":building,"vehicles":vehicle,"street":street_prop,"npcs":npc}
def main():
    argv=[]
    if "--" in __import__("sys").argv: argv=__import__("sys").argv[__import__("sys").argv.index("--")+1:]
    parser=argparse.ArgumentParser()
    parser.add_argument("--category",choices=["all"]+list(BUILDERS),default="all")
    parser.add_argument("--count",type=int,default=10,help="number per category")
    parser.add_argument("--seed",type=int,default=2026)
    args=parser.parse_args(argv)
    random.seed(args.seed)
    categories=list(BUILDERS) if args.category=="all" else [args.category]
    for category in categories:
        for i in range(args.count):
            reset()
            name="%s_%03d_seed%d"%(category[:-1] if category=="buildings" else category, i+1, args.seed)
            BUILDERS[category](i)
            export(name,category)
    print("Asset factory finished. Output:",OUT_ROOT)
if __name__=="__main__": main()
