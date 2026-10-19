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
NPCs export as segmented mesh parts with a simple humanoid-compatible armature for later code-driven animation. Robot hard-surface forms remain angular; organic species use sculptural low-poly volumes.
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
NPC_PROFILE = {}
NPC_MATERIAL_PROFILES = {
 "human":{"skin":["skin_a","skin_b","skin_c"],"shell":["steel"],"eye":["eye"],"claw":["ink"],"marking":["rust","cream","teal"]},
 "crystal_head":{"skin":["alien_blue","alien_purple"],"shell":["blue","plum"],"eye":["eye","cyan"],"claw":["steel"],"marking":["cyan","pink"]},
 "wide_cranium":{"skin":["alien_green","alien_blue"],"shell":["teal","blue"],"eye":["eye","cyan"],"claw":["ink"],"marking":["lime","cyan"]},
 "horned":{"skin":["alien_orange","alien_purple"],"shell":["rust","plum"],"eye":["eye","pink"],"claw":["cream","ink"],"marking":["yellow","pink"]},
 "fin_head":{"skin":["alien_blue","teal"],"shell":["blue","teal"],"eye":["eye","cyan"],"claw":["ink"],"marking":["cyan","lime"]},
 "long_neck":{"skin":["alien_green","alien_orange"],"shell":["teal","rust"],"eye":["eye","lime"],"claw":["ink"],"marking":["lime","yellow"]},
 "stocky":{"skin":["alien_green","alien_orange"],"shell":["rust","teal"],"eye":["eye"],"claw":["ink"],"marking":["yellow","cream"]},
 "tall_thin":{"skin":["alien_purple","alien_blue"],"shell":["plum","blue"],"eye":["eye","pink"],"claw":["ink"],"marking":["pink","cyan"]},
 "cyclops":{"skin":["alien_green","alien_orange"],"shell":["teal","rust"],"eye":["eye","cyan"],"claw":["ink"],"marking":["lime","pink"]},
 "four_eyed":{"skin":["alien_blue","alien_purple"],"shell":["blue","plum"],"eye":["eye","cyan"],"claw":["ink"],"marking":["cyan","pink"]},
 "slug_traveler":{"skin":["alien_green","alien_orange"],"shell":["teal","rust"],"eye":["eye","lime"],"claw":["ink"],"marking":["lime","yellow"]},
 "mantis":{"skin":["alien_green","lime"],"shell":["teal","lime"],"eye":["eye","yellow"],"claw":["ink","steel"],"marking":["lime","yellow"]},
 "robot":{"skin":["metal","steel"],"shell":["metal","steel"],"eye":["eye","cyan"],"claw":["steel"],"marking":["cyan","pink","lime"]},
 "service_droid":{"skin":["steel","metal"],"shell":["steel","ink"],"eye":["eye","cyan"],"claw":["steel"],"marking":["cyan","yellow"]},
 "shellback":{"skin":["alien_green","alien_orange"],"shell":["rust","teal","cream"],"eye":["eye","yellow"],"claw":["ink","cream"],"marking":["yellow","lime"]},
 "hopper":{"skin":["alien_green","alien_orange"],"shell":["teal","rust"],"eye":["eye","cyan"],"claw":["ink"],"marking":["lime","yellow"]},
 "sporehead":{"skin":["alien_purple","alien_green"],"shell":["plum","teal"],"eye":["eye","pink"],"claw":["ink"],"marking":["pink","lime"]},
 "tube_neck":{"skin":["alien_blue","alien_green"],"shell":["blue","teal"],"eye":["eye","cyan"],"claw":["ink"],"marking":["cyan","lime"]},
 "orbital":{"skin":["steel","metal"],"shell":["ink","steel"],"eye":["eye","cyan"],"claw":["steel"],"marking":["cyan","pink"]},
 "avian":{"skin":["cream","alien_orange","alien_blue"],"shell":["rust","blue","cream"],"eye":["eye"],"claw":["ink","cream"],"marking":["yellow","cyan"]},
 "brute":{"skin":["alien_orange","alien_green"],"shell":["rust","teal"],"eye":["eye","pink"],"claw":["ink","cream"],"marking":["yellow","pink"]},
}
def npc_material(role, fallback):
    return random.choice(NPC_PROFILE.get(role, [fallback]))

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
    """Tapered low-poly limb/connector, with a subtly smaller far end."""
    vec=Vector(b)-Vector(a)
    o=cyl(name,(Vector(a)+Vector(b))*0.5,radius,vec.length,material,7,
          radius2=radius*.72)
    o.rotation_mode="QUATERNION"; o.rotation_quaternion=vec.to_track_quat("Z","Y")
    return o

def organic_body(name, loc, scale, material):
    """Rounded faceted volume for flesh, cloth, and creature anatomy."""
    o=ico(name,loc,scale,material)
    # A couple of subdivisions keep the silhouette smooth-ish but still low-poly.
    return o

def rig_npc(mesh_objects, name):
    """Create a compact rigid-weighted skeleton. Each generated part follows one bone,
    which is ideal for stylized segmented characters and straightforward code animation."""
    if not mesh_objects:
        return None
    # Infer scale and proportions from the generated character bounds.
    min_z = min(o.bound_box[0][2] + o.location.z for o in mesh_objects)
    max_z = max(o.bound_box[6][2] + o.location.z for o in mesh_objects)
    height = max(1.0, max_z - min_z)
    min_x = min(o.location.x for o in mesh_objects)
    max_x = max(o.location.x for o in mesh_objects)
    half_width = max(.22, (max_x-min_x)*.5)
    z = lambda n: min_z + height*n
    arm_x = max(.22, half_width*.82)
    hand_x = max(.30, half_width*1.12)
    bones = [
        ("root", (0,0,z(0.04)), (0,0,z(.20)), None),
        ("pelvis", (0,0,z(.38)), (0,0,z(.55)), "root"),
        ("spine", (0,0,z(.50)), (0,0,z(.68)), "pelvis"),
        ("chest", (0,0,z(.63)), (0,0,z(.79)), "spine"),
        ("neck", (0,0,z(.76)), (0,0,z(.87)), "chest"),
        ("head", (0,0,z(.83)), (0,0,z(.99)), "neck"),
    ]
    for side, suffix in ((-1,"L"),(1,"R")):
        sx = lambda n: side*half_width*n
        bones.extend([
            ("upper_arm."+suffix, (sx(.48),0,z(.76)), (sx(.77),0,z(.59)), "chest"),
            ("forearm."+suffix, (sx(.77),0,z(.59)), (sx(1.0),0,z(.51)), "upper_arm."+suffix),
            ("hand."+suffix, (sx(1.0),0,z(.51)), (sx(1.10),0,z(.48)), "forearm."+suffix),
            ("thigh."+suffix, (sx(.30),0,z(.43)), (sx(.32),0,z(.27)), "pelvis"),
            ("shin."+suffix, (sx(.32),0,z(.27)), (sx(.32),0,z(.10)), "thigh."+suffix),
            ("foot."+suffix, (sx(.32),0,z(.10)), (sx(.32),-.13*height,z(.06)), "shin."+suffix),
        ])
    bpy.ops.object.select_all(action="DESELECT")
    arm_data = bpy.data.armatures.new(name+"_Rig")
    arm = bpy.data.objects.new(name+"_Rig", arm_data)
    bpy.context.collection.objects.link(arm)
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    created = {}
    for bone_name, head, tail, parent_name in bones:
        b=arm_data.edit_bones.new(bone_name)
        b.head=head; b.tail=tail
        if parent_name: b.parent=created[parent_name]
        created[bone_name]=b
    bpy.ops.object.mode_set(mode="OBJECT")
    # Map generated pieces to body regions. L/R follows each piece's x position.
    for obj in mesh_objects:
        low=obj.name.lower()
        x=obj.matrix_world.translation.x
        side = "L" if x < 0 else "R"
        if any(k in low for k in ("head","eye","horn","fin","antenna","beak","jaw","crown","spore","feeler","visor","face","ear","tusk","stalk")):
            bone="head"
        elif any(k in low for k in ("neck","collar","throat")):
            bone="neck"
        elif any(k in low for k in ("toe","foot","boot","claw","metal_foot","bird_foot")):
            bone="foot."+side
        elif any(k in low for k in ("shin","lower_leg","long_shin","bird_shin","stumpy_leg","tendon")):
            bone="shin."+side
        elif any(k in low for k in ("thigh","power_thigh","feathered_thigh","upper_leg","leg")):
            bone="thigh."+side
        elif any(k in low for k in ("hand","finger","knuckle","hooked")):
            bone="hand."+side
        elif any(k in low for k in ("forearm","blade_forearm","wing_forearm")):
            bone="forearm."+side
        elif any(k in low for k in ("arm","wing","scythe")):
            bone="upper_arm."+side
        elif any(k in low for k in ("shoulder","elbow","knee","joint","pad")):
            bone=("upper_arm." if "shoulder" in low else "forearm.")+side
        elif any(k in low for k in ("torso","chest","abdomen","mantle","shell","vest","garment","bib","belt","core","pack","pouch","plate","feather","ridge","mark","patch","buck")):
            bone="chest" if obj.location.z > z(.58) else "pelvis"
        else:
            bone="chest" if obj.location.z > z(.58) else "pelvis"
        group=obj.vertex_groups.new(name=bone)
        group.add(list(range(len(obj.data.vertices))),1.0,"REPLACE")
        mod=obj.modifiers.new("NPC Armature","ARMATURE")
        mod.object=arm
        obj.parent=arm
    return arm

def export(name, category):
    bpy.ops.object.select_all(action="SELECT")
    selected=list(bpy.context.selected_objects)
    if not selected: return
    bpy.context.view_layer.objects.active=selected[0]
    bpy.ops.object.convert(target="MESH")
    selected=list(bpy.context.selected_objects)
    if category == "npcs":
        rig_npc(selected, name)
        bpy.ops.object.select_all(action="DESELECT")
        for obj in selected:
            obj.select_set(True)
        arm=bpy.data.objects.get(name+"_Rig")
        if arm: arm.select_set(True)
    else:
        if len(selected)>1: bpy.ops.object.join()
        obj=bpy.context.object; obj.name=name
        for poly in obj.data.polygons: poly.use_smooth=False
    folder=os.path.join(OUT_ROOT,category); os.makedirs(folder,exist_ok=True)
    path=os.path.join(folder,name+".glb")
    bpy.ops.export_scene.gltf(filepath=path,export_format="GLB",use_selection=True,export_apply=(category != "npcs"))
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
    """Chunky low-poly NPCs with deliberately different anatomy and readable silhouettes."""
    species = random.choice([
        "human", "human", "crystal_head", "wide_cranium", "horned", "fin_head",
        "long_neck", "stocky", "tall_thin", "cyclops", "four_eyed", "slug_traveler",
        "mantis", "robot", "service_droid", "shellback", "hopper", "sporehead",
        "tube_neck", "orbital", "avian", "brute"
    ])
    height = random.uniform(1.55, 2.08)
    s = height / 1.8
    profile = NPC_MATERIAL_PROFILES.get(species, NPC_MATERIAL_PROFILES["human"])
    NPC_PROFILE.clear()
    NPC_PROFILE.update(profile)
    outfit, trim = random.choice(PAINTS), npc_material("marking", random.choice(GLOWS))
    human = species == "human"
    robot = species in ("robot", "service_droid")
    alien = not human and not robot
    skin = npc_material("skin", "skin_a" if human else ("metal" if robot else "alien_green"))
    eye_mat = npc_material("eye", "eye")
    claw_mat = npc_material("claw", "ink")
    shell_mat = npc_material("shell", outfit)
    garment = random.choice(["jacket", "coat", "armor", "tunic", "overalls", "merchant_apron", "patched_suit"])

    # Proportion presets alter the entire figure, not merely its head or paint.
    body_w, torso_h, head_w, head_h = .55, .68, .42, .38
    leg_w, stance, arm_w = .105, .17, .085
    hip_z, shoulder_z, head_z = .76, 1.31, 1.61
    leg_style, arm_style, torso_style = "human", "human", "jacket"
    if species == "wide_cranium":
        head_w, head_h, body_w = .72, .48, .52
    elif species == "horned":
        head_w, head_h, arm_w = .44, .37, .095
    elif species == "fin_head":
        head_w, head_h = .48, .36
    elif species == "long_neck":
        head_w, head_h, head_z = .34, .31, 1.78
    elif species == "stocky":
        body_w, torso_h, head_w, head_h, leg_w, stance = .76, .61, .45, .34, .15, .25
    elif species == "tall_thin":
        body_w, torso_h, head_w, head_h, leg_w, stance = .39, .82, .34, .34, .07, .12
        hip_z, shoulder_z = .79, 1.38
    elif species == "slug_traveler":
        body_w, torso_h, head_w, head_h, leg_w, stance = .73, .49, .52, .30, .14, .25
        torso_style, leg_style = "slug", "stump"
    elif species == "mantis":
        body_w, torso_h, head_w, head_h, leg_w, stance = .43, .72, .32, .40, .065, .15
        leg_style, arm_style, torso_style = "digitigrade", "scythe", "carapace"
    elif species == "robot":
        head_w, head_h, body_w, torso_h = .46, .38, .54, .66
        torso_style, leg_style, arm_style = "robot", "robot", "robot"
    elif species == "service_droid":
        head_w, head_h, body_w, torso_h = .38, .46, .48, .60
        torso_style, leg_style, arm_style = "robot", "robot", "robot"
    elif species == "shellback":
        body_w, torso_h, head_w, head_h, leg_w, stance = .68, .58, .34, .31, .12, .23
        torso_style, leg_style = "shell", "digitigrade"
    elif species == "hopper":
        body_w, torso_h, head_w, head_h, leg_w, stance = .43, .58, .40, .37, .11, .18
        leg_style, torso_style = "spring", "pear"
    elif species == "sporehead":
        body_w, torso_h, head_w, head_h = .48, .60, .57, .47
        torso_style = "pear"
    elif species == "tube_neck":
        body_w, torso_h, head_w, head_h, head_z = .50, .62, .31, .32, 1.88
    elif species == "orbital":
        body_w, torso_h, head_w, head_h, leg_w = .57, .70, .39, .37, .10
        torso_style, leg_style = "robot", "robot"
    elif species == "avian":
        body_w, torso_h, head_w, head_h, leg_w, stance = .48, .62, .38, .34, .065, .16
        leg_style, arm_style, torso_style = "bird", "wing", "feather"
    elif species == "brute":
        body_w, torso_h, head_w, head_h, leg_w, stance, arm_w = .82, .72, .43, .35, .16, .27, .14
        torso_style = "barrel"

    # Legs are built as upper/lower segments with visible knee joints, ankle and shaped feet.
    for side in (-1, 1):
        x = side * stance * s
        hip = (x, 0, hip_z*s)
        if leg_style == "digitigrade":
            knee = (x + side*.07*s, .015, .43*s)
            ankle = (x - side*.015*s, -.015, .22*s)
            beam("Thigh", hip, knee, leg_w*s*1.12, skin if species in ("mantis","shellback") else outfit)
            ico("Knee_Joint", knee, (.105*s,.11*s,.10*s), skin)
            beam("Shin", knee, ankle, leg_w*s*.68, outfit)
            foot = (ankle[0]+side*.04*s, -.13*s, .10*s)
        elif leg_style == "spring":
            knee = (x + side*.08*s, .01, .39*s)
            ankle = (x - side*.015*s, -.02, .19*s)
            beam("Power_Thigh", hip, knee, leg_w*s*1.3, outfit)
            ico("Spring_Knee", knee, (.13*s,.12*s,.12*s), skin)
            beam("Long_Shin", knee, ankle, leg_w*s*.72, skin)
            foot = (ankle[0], -.15*s, .08*s)
        elif leg_style == "bird":
            knee = (x + side*.015*s, 0, .48*s)
            ankle = (x + side*.045*s, -.04, .19*s)
            beam("Feathered_Thigh", hip, knee, leg_w*s*1.15, outfit)
            ico("Knee", knee, (.09*s,.09*s,.09*s), skin)
            beam("Bird_Shin", knee, ankle, leg_w*s*.55, skin)
            foot = (ankle[0]+side*.03*s, -.19*s, .075*s)
        elif leg_style == "stump":
            knee = (x, 0, .39*s)
            beam("Stumpy_Leg", hip, knee, leg_w*s*1.45, skin)
            foot = (x, -.10*s, .12*s)
        else:
            knee = (x + side*.015*s, 0, .43*s)
            ankle = (x + side*random.uniform(-.015,.035)*s, -.02, .17*s)
            beam("Thigh", hip, knee, leg_w*s*1.18, outfit if not robot else "metal")
            ico("Knee", knee, (.095*s,.10*s,.095*s), "steel" if robot else skin)
            beam("Shin", knee, ankle, leg_w*s*.78, outfit if not robot else "metal")
            foot = (ankle[0]+side*.025*s, -.12*s, .08*s)

        if species == "avian":
            # Three obvious toes make the feet read as bird-like, not boots.
            ico("Bird_Foot", foot, (.105*s,.15*s,.055*s), skin)
            for toe in (-1, 0, 1):
                beam("Toe", (foot[0],foot[1]-.04*s,foot[2]),
                     (foot[0]+toe*.075*s,foot[1]-.19*s,foot[2]-.015*s), .022*s, skin)
        elif species in ("mantis","shellback"):
            ico("Clawed_Foot", foot, (.13*s,.19*s,.065*s), skin)
            beam("Toe_Claw", foot, (foot[0]+side*.04*s,foot[1]-.20*s,foot[2]-.015*s), .025*s, "ink")
        else:
            foot_dims = (.24,.35,.14) if species not in ("hopper","slug_traveler") else (.28,.38,.13)
            cube("Boot" if not robot else "Metal_Foot",
                 (foot[0],foot[1]-.025*s,max(.055*s,foot[2])),
                 tuple(v*s for v in foot_dims), "ink" if not robot else "steel", .035*s)
            if robot:
                cube("Foot_Light", (foot[0],foot[1]-.20*s,foot[2]),
                     (.10*s,.025*s,.035*s), trim, .008*s)

    # Torso volume: different silhouettes and layered masses prevent the same-box-body look.
    torso_z = 1.10*s
    torso_dims = (body_w*s, .34*s, torso_h*s)
    if torso_style == "slug":
        ico("Soft_Mantle_Body", (0,.015*s,.94*s), (.43*s,.29*s,.38*s), skin)
        cube("Traveler_Vest", (0,-.19*s,1.02*s), (.55*s,.08*s,.38*s), outfit, .06*s)
    elif torso_style == "pear":
        ico("Tapered_Abdomen", (0,0,.99*s), (body_w*.52*s,.25*s,.43*s), skin)
        cube("Chest_Garment", (0,-.16*s,1.20*s), (body_w*.80*s,.10*s,.30*s), outfit, .045*s)
    elif torso_style == "barrel":
        ico("Barrel_Torso", (0,0,1.08*s), (.44*s,.27*s,.40*s), outfit)
        cube("Shoulder_Mantle", (0,0,1.35*s), (.88*s,.40*s,.20*s), outfit, .07*s)
    elif torso_style == "shell":
        cube("Torso", (0,0,torso_z), torso_dims, outfit, .08*s)
        ico("Domed_Shell", (0,.13*s,1.25*s), (.40*s,.20*s,.36*s), random.choice(["rust","teal","alien_green"]))
        for side in (-1,1):
            beam("Shell_Ridge", (side*.12*s,.01*s,1.48*s), (side*.24*s,.02*s,1.25*s), .025*s, "cream")
    elif torso_style == "robot":
        cube("Torso", (0,0,torso_z), torso_dims, "metal", .055*s)
        cube("Abdominal_Block", (0,-.18*s,.91*s), (body_w*.62*s,.09*s,.24*s), "ink", .025*s)
        cube("Core", (0,-.235*s,1.13*s), (.17*s,.035*s,.17*s), trim, .02*s)
        cube("Collar", (0,0,1.43*s), (body_w*.76*s,.38*s,.10*s), "steel", .025*s)
    else:
        if torso_style in ("carapace","feather"):
            organic_body("Torso", (0,0,torso_z), (body_w*.49*s,.23*s,torso_h*.53*s), outfit)
        else:
            # Non-robot characters use a faceted, tapered body instead of a plain cube.
            organic_body("Torso", (0,.015*s,torso_z), (body_w*.50*s,.245*s,torso_h*.54*s), outfit)
        if torso_style == "carapace":
            ico("Thorax_Plate", (0,-.17*s,1.18*s), (.24*s,.10*s,.30*s), skin)
            cube("Abdomen_Plate", (0,.015*s,.91*s), (.33*s,.30*s,.30*s), skin, .06*s)
        elif torso_style == "feather":
            for row in range(3):
                for side in (-1,1):
                    ico("Feather_Plate", (side*(.10+row*.07)*s,-.19*s,(1.32-row*.13)*s),
                        (.12*s,.035*s,.10*s), skin)
        if garment in ("coat","tunic","merchant_apron"):
            cube("Lower_Garment", (0,.015*s,.76*s),
                 (body_w*1.12*s,.38*s,.32*s), outfit, .055*s)
        if garment == "armor":
            cube("Chest_Plate", (0,-.19*s,1.18*s), (.44*s,.075*s,.34*s), "steel", .035*s)
            cube("Chest_Light", (0,-.235*s,1.18*s), (.16*s,.025*s,.06*s), trim, .01*s)
        elif garment in ("overalls","merchant_apron"):
            cube("Bib", (0,-.19*s,1.16*s), (.34*s,.06*s,.34*s),
                 "cream" if garment=="overalls" else random.choice(["rust","yellow","teal"]), .02*s)
        elif garment == "patched_suit":
            cube("Suit_Patch", (random.choice([-.13,.13])*s,-.19*s,1.16*s),
                 (.12*s,.025*s,.14*s), random.choice(["cream","rust","yellow"]), .01*s)

    # Necks are visibly different, with collars or stacked segments where appropriate.
    if species == "long_neck":
        cyl("Long_Neck", (0,0,1.48*s), .105*s, .54*s, skin, 7)
        cube("Neck_Collar", (0,-.01*s,1.26*s), (.28*s,.28*s,.09*s), "steel", .025*s)
    elif species == "tube_neck":
        for j in range(3):
            cyl("Segmented_Neck", (0,0,(1.40+j*.13)*s), .075*s, .15*s, skin, 7)
        ico("Neck_Gland", (0,-.065*s,1.47*s), (.09*s,.045*s,.07*s), trim)
    else:
        cyl("Neck", (0,0,1.43*s), .105*s, .16*s, skin if not robot else "steel", 7)

    # Arms have shoulders, elbows, forearms and hands/claws; anatomy differs by species.
    for side in (-1,1):
        shoulder = (side*(body_w*.52)*s, 0, shoulder_z*s)
        if arm_style == "scythe":
            elbow = (side*.46*s,-.015*s,1.17*s)
            wrist = (side*.58*s,-.09*s,1.29*s)
            ico("Shoulder_Joint", shoulder, (.12*s,.12*s,.13*s), skin)
            beam("Upper_Arm", shoulder, elbow, arm_w*s*.8, skin)
            ico("Elbow_Joint", elbow, (.075*s,.075*s,.075*s), skin)
            beam("Blade_Forearm", elbow, wrist, arm_w*s*.55, outfit)
            beam("Hooked_Claw", wrist, (wrist[0]+side*.15*s,-.10*s,1.43*s), .035*s, skin)
        elif arm_style == "wing":
            elbow = (side*.49*s,-.015*s,1.18*s)
            wrist = (side*.62*s,-.05*s,1.02*s)
            beam("Wing_Upper", shoulder, elbow, arm_w*s*1.2, outfit)
            ico("Wing_Joint", elbow, (.09*s,.10*s,.09*s), skin)
            beam("Wing_Forearm", elbow, wrist, arm_w*s*.75, skin)
            ico("Wing_Tip", wrist, (.07*s,.07*s,.08*s), skin)
            for j in range(2):
                beam("Wing_Feather", (wrist[0],wrist[1],wrist[2]+j*.04*s),
                     (wrist[0]+side*.13*s,wrist[1]-.03*s,wrist[2]-.12*s+j*.03*s), .022*s, outfit)
        else:
            elbow_z = random.uniform(.94,1.12)*s
            elbow = (side*random.uniform(.37,.48)*s,-.025*s,elbow_z)
            wrist = (elbow[0]+side*.025*s,-.055*s,elbow[2]-.19*s)
            shoulder_mat = "steel" if robot else (skin if species in ("shellback","brute") else outfit)
            ico("Shoulder", shoulder, (.12*s,.13*s,.13*s), shoulder_mat)
            beam("Upper_Arm", shoulder, elbow, arm_w*s*(1.25 if species=="brute" else 1), outfit if not robot else "steel")
            ico("Elbow", elbow, (.075*s,.08*s,.075*s), "steel" if robot else skin)
            beam("Forearm", elbow, wrist, arm_w*s*.82, outfit if not robot else "metal")
            ico("Hand", wrist, (.085*s,.075*s,.09*s), "steel" if robot else skin)
            if robot:
                cube("Knuckle", (wrist[0],wrist[1]-.045*s,wrist[2]), (.11*s,.035*s,.07*s), trim, .01*s)
            elif species == "brute":
                for finger in (-1,0,1):
                    beam("Finger", (wrist[0]+finger*.035*s,wrist[1]-.03*s,wrist[2]),
                         (wrist[0]+finger*.045*s,wrist[1]-.11*s,wrist[2]-.035*s), .022*s, skin)
        if species in ("stocky","brute"):
            ico("Shoulder_Pad", (side*(body_w*.50)*s,-.01*s,shoulder_z*s),
                (.17*s,.20*s,.17*s), "steel" if species=="stocky" else outfit)

    # Head and face: all species have a different outline and/or eye arrangement.
    if robot:
        cube("Robot_Head", (0,-.015*s,head_z*s), (head_w*s,.36*s,head_h*s), "steel", .055*s)
        if species == "service_droid":
            cube("Droid_Faceplate", (0,-.215*s,head_z*s), (.23*s,.035*s,.26*s), "ink", .02*s)
            for zoff in (-.06,.04,.12):
                ico("Status_Light", (0,-.24*s,(head_z+zoff)*s), (.035*s,.018*s,.025*s), trim)
            cyl("Droid_Antenna", (.13*s,0,(head_z+.25)*s), .025*s,.32*s,trim,6)
            cube("Droid_Ear", (.24*s,0,head_z*s), (.07*s,.24*s,.16*s), "ink", .015*s)
        else:
            cube("Robot_Visor", (0,-.205*s,head_z*s), (.34*s,.035*s,.12*s), trim, .02*s)
            cyl("Antenna", (0,0,(head_z+.27)*s), .025*s,.25*s,trim,6)
            for side in (-1,1):
                cube("Jaw_Hinge", (side*.20*s,-.18*s,(head_z-.10)*s), (.07*s,.05*s,.09*s), "ink", .01*s)
    elif species == "slug_traveler":
        ico("Slug_Mantle", (0,.015*s,(head_z-.10)*s), (.36*s,.29*s,.24*s), skin)
        ico("Slug_Head", (0,-.02*s,(head_z+.09)*s), (.24*s,.22*s,.22*s), skin)
        for side in (-1,1):
            beam("Eye_Stalk", (side*.12*s,0,(head_z+.18)*s),
                 (side*.19*s,-.01*s,(head_z+.38)*s), .035*s, skin)
            ico("Stalk_Eye", (side*.19*s,-.04*s,(head_z+.39)*s), (.06*s,.045*s,.06*s), "eye")
    else:
        if species == "sporehead":
            ico("Spore_Cap", (0,.015*s,(head_z+.10)*s), (.36*s,.26*s,.20*s), skin)
            ico("Face", (0,-.02*s,head_z*s), (.21*s,.20*s,.20*s), skin)
            for side in (-1,1):
                ico("Spore", (side*.29*s,.02*s,(head_z+.16)*s), (.10*s,.10*s,.10*s), trim)
        elif species == "orbital":
            ico("Orb_Helmet", (0,0,head_z*s), (.25*s,.24*s,.25*s), "steel")
            cube("Helmet_Visor", (0,-.22*s,head_z*s), (.30*s,.035*s,.12*s), trim, .025*s)
            for side in (-1,1):
                cyl("Helmet_Port", (side*.26*s,0,head_z*s), .055*s,.08*s, "ink", 8)
        elif species == "avian":
            ico("Bird_Head", (0,0,head_z*s), (.20*s,.20*s,.20*s), skin)
            beam("Beak_Upper", (0,-.17*s,head_z*s), (0,-.34*s,(head_z-.03)*s), .06*s, "yellow")
            beam("Beak_Lower", (0,-.17*s,(head_z-.04)*s), (0,-.30*s,(head_z-.09)*s), .035*s, "yellow")
            for side in (-1,1):
                ico("Eye", (side*.10*s,-.16*s,(head_z+.03)*s), (.035*s,.025*s,.04*s), "eye")
                ico("Brow_Feather", (side*.14*s,.01*s,(head_z+.14)*s), (.12*s,.10*s,.07*s), skin)
        else:
            if species == "wide_cranium":
                ico("Head", (0,0,head_z*s), (.36*s,.23*s,.24*s), skin)
                ico("Jaw", (0,-.015*s,(head_z-.12)*s), (.20*s,.20*s,.13*s), skin)
            elif species == "tall_thin":
                ico("Head", (0,0,head_z*s), (.17*s,.18*s,.28*s), skin)
            elif species == "crystal_head":
                ico("Head", (0,0,head_z*s), (.23*s,.21*s,.22*s), skin)
                ico("Crystal_Crown", (0,.015*s,(head_z+.20)*s), (.14*s,.13*s,.22*s), trim)
                for side in (-1,1):
                    ico("Temple_Crystal", (side*.21*s,0,head_z*s), (.08*s,.09*s,.14*s), trim)
            elif species == "cyclops":
                ico("Head", (0,0,head_z*s), (head_w*.5*s,.22*s,head_h*.5*s), skin)
            else:
                ico("Head", (0,0,head_z*s), (head_w*.5*s,.22*s,head_h*.5*s), skin)
            if human:
                ico("Hair", (0,.035*s,(head_z+.12)*s), (.23*s,.21*s,.12*s), random.choice(["ink","rust","cream"]))
                # Ears, nose and chin give humans a less featureless toy-head read.
                for side in (-1,1):
                    ico("Ear", (side*.205*s,-.005*s,(head_z-.015)*s), (.045*s,.055*s,.07*s), skin)
                ico("Nose", (0,-.218*s,(head_z-.015)*s), (.035*s,.035*s,.055*s), skin)
            if species == "cyclops":
                ico("Single_Eye", (0,-.218*s,head_z*s), (.095*s,.035*s,.095*s), random.choice(["eye","cyan"]))
            else:
                eye_count = 4 if species == "four_eyed" else 2
                for n in range(eye_count):
                    x = (n-(eye_count-1)/2)*(.09 if eye_count==4 else .14)*s
                    z = (head_z+.07)*s if eye_count==4 and n<2 else (head_z-.025)*s if eye_count==4 else (head_z+.015)*s
                    ico("Eye", (x,-.205*s,z), (.035*s,.025*s,.04*s), "eye" if human else random.choice(["eye","cyan"]))
            if species == "horned":
                for side in (-1,1):
                    beam("Horn", (side*.14*s,0,(head_z+.10)*s),
                         (side*.27*s,.01*s,(head_z+.37)*s), .055*s, skin)
                    ico("Horn_Tip", (side*.27*s,.01*s,(head_z+.37)*s), (.035*s,.035*s,.04*s), "cream")
            elif species == "fin_head":
                for side in (-1,1):
                    ico("Head_Fin", (side*.28*s,.015*s,head_z*s), (.15*s,.075*s,.22*s), skin)
                    beam("Fin_Ridge", (side*.27*s,0,(head_z-.12)*s),
                         (side*.31*s,0,(head_z+.13)*s), .018*s, trim)
            elif species == "tall_thin":
                for side in (-1,1):
                    beam("Crown_Antenna", (side*.08*s,0,(head_z+.18)*s),
                         (side*.13*s,0,(head_z+.43)*s), .022*s, skin)
            elif species == "mantis":
                for side in (-1,1):
                    beam("Mantis_Feeler", (side*.08*s,0,(head_z+.12)*s),
                         (side*.18*s,0,(head_z+.39)*s), .025*s, skin)
            elif species == "tube_neck":
                ico("Sensory_Dome", (0,0,(head_z+.16)*s), (.14*s,.15*s,.13*s), trim)

    # Silhouette-breaking details are chosen with archetype awareness.
    if random.random() < .62:
        cube("Utility_Belt", (0,-.19*s,.91*s), (.50*s,.06*s,.09*s), "ink", .015*s)
        cube("Belt_Buckle", (0,-.23*s,.91*s), (.09*s,.025*s,.07*s), trim, .008*s)
    if random.random() < .32 and species not in ("slug_traveler","hopper"):
        cube("Travel_Pack", (0,.23*s,1.13*s), (.31*s,.22*s,.39*s),
             random.choice(["rust","blue","ink"]), .035*s)
    if alien and random.random() < .72:
        ico("Bioluminescent_Mark", (0,-.235*s,1.22*s), (.045*s,.025*s,.12*s), trim)
    if species == "shellback":
        for side in (-1,1):
            ico("Shell_Spike", (side*.28*s,.10*s,1.45*s), (.08*s,.10*s,.12*s), "cream")
    elif species == "hopper":
        ico("Throat_Pouch", (0,-.20*s,1.08*s), (.15*s,.08*s,.17*s), trim)
        for side in (-1,1):
            beam("Long_Hind_Tendon", (side*.18*s,.08*s,.67*s), (side*.24*s,.08*s,.38*s), .025*s, skin)
    elif species == "brute":
        for side in (-1,1):
            ico("Tusks", (side*.12*s,-.18*s,(head_z-.10)*s), (.045*s,.06*s,.09*s), "cream")

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
