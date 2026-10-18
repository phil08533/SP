"""Generate the first portable Space Hippie low-poly prop pack.

Run with Blender 4.x:
  blender --background --python tools/asset_generation/generate_dusty_junction_props.py

Writes one glTF binary per prop to assets/3d/dusty_junction/.
These are real, editable mesh assets, deliberately modular and untextured beyond
cohesive material assignments. Review in Blender and in-engine before production.
No external Python packages required.
"""
import bpy
import math
import os
from mathutils import Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "assets", "3d", "dusty_junction")
os.makedirs(OUT, exist_ok=True)

PALETTE = {
    "paint_teal": (0.075, 0.28, 0.31, 1),
    "paint_faded": (0.68, 0.34, 0.16, 1),
    "metal_dark": (0.075, 0.09, 0.105, 1),
    "metal": (0.31, 0.34, 0.33, 1),
    "concrete": (0.43, 0.39, 0.32, 1),
    "wood": (0.30, 0.18, 0.105, 1),
    "glass": (0.035, 0.25, 0.32, 1),
    "glow_cyan": (0.03, 0.8, 0.92, 1),
    "glow_pink": (1.0, 0.055, 0.35, 1),
    "glow_lime": (0.45, 1.0, 0.12, 1),
}

def material(name, color, metallic=0.0, roughness=0.72, emission=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission:
        bsdf.inputs["Emission Color"].default_value = color
        bsdf.inputs["Emission Strength"].default_value = emission
    return mat

MATS = {k: material(k, v, 0.55 if "metal" in k else 0.05,
                    0.32 if "glass" in k else 0.7,
                    3.0 if "glow" in k else 0.0) for k, v in PALETTE.items()}

def reset():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)

def cube(name, loc, scale, mat, bevel=0.035):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(MATS[mat])
    if bevel:
        mod = obj.modifiers.new("Small worn edges", "BEVEL")
        mod.width = bevel
        mod.segments = 1
        obj.modifiers.new("Weighted corner normals", "WEIGHTED_NORMAL")
    return obj

def cylinder(name, loc, radius, depth, mat, vertices=8, radius2=None):
    if radius2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=radius2, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(MATS[mat])
    return obj

def text_obj(body, loc, size, mat, rotation=(math.pi/2, 0, 0)):
    curve = bpy.data.curves.new("Sign lettering", "FONT")
    curve.body = body
    curve.size = size
    curve.extrude = 0.004
    obj = bpy.data.objects.new("Lettering_" + body.replace(" ", "_"), curve)
    bpy.context.collection.objects.link(obj)
    obj.location = loc
    obj.rotation_euler = rotation
    obj.data.materials.append(MATS[mat])
    return obj

def export_asset(name, builder):
    reset()
    builder()
    # Apply transforms and bevels to keep exports predictable for game engines.
    bpy.ops.object.select_all(action="SELECT")
    bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
    bpy.ops.object.convert(target="MESH")
    for obj in bpy.context.selected_objects:
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    path = os.path.join(OUT, name + ".glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB",
                              use_selection=True, export_apply=True)
    print("Wrote", path)

def motel_sign():
    cube("Sign_Backplate", (0, 0, 2.2), (3.4, 0.22, 1.15), "paint_teal")
    cube("Sign_Rim", (0, -0.13, 2.2), (3.2, 0.06, 0.96), "metal_dark")
    cube("Sign_Face", (0, -0.17, 2.2), (3.05, 0.04, 0.82), "paint_faded")
    for x in (-1.45, 1.45):
        cylinder("Support", (x, 0.05, 1.15), 0.075, 2.3, "metal_dark", 8)
    text_obj("MOTEL", (-1.05, -0.205, 2.05), 0.48, "glow_cyan")

def fuel_pump():
    cube("Pump_Base", (0, 0, 0.16), (0.8, 0.62, 0.3), "metal_dark")
    cube("Pump_Body", (0, 0, 0.88), (0.64, 0.48, 1.2), "paint_faded")
    cube("Display_Bezel", (0, -0.25, 1.12), (0.42, 0.035, 0.28), "metal_dark")
    cube("Display_Glow", (0, -0.274, 1.12), (0.34, 0.02, 0.17), "glow_lime", 0.005)
    cube("Lower_Panel", (0, -0.25, 0.63), (0.3, 0.025, 0.2), "metal")
    # Hose and nozzle are separate, readable silhouettes.
    hose = cylinder("Hose", (0.37, 0.02, 0.79), 0.035, 0.56, "metal_dark", 6)
    hose.rotation_euler[1] = -0.55
    cube("Nozzle", (0.55, -0.03, 0.56), (0.12, 0.09, 0.25), "metal_dark")

def street_lamp():
    cylinder("Pole", (0, 0, 1.8), 0.055, 3.6, "metal_dark", 8)
    cube("Arm", (0.28, 0, 3.5), (0.62, 0.07, 0.07), "metal_dark")
    cube("Lamp_Housing", (0.56, 0, 3.42), (0.42, 0.3, 0.16), "paint_teal")
    cube("Lamp_Lens", (0.56, -0.16, 3.35), (0.31, 0.025, 0.045), "glow_cyan", 0.01)
    cube("Foot", (0, 0, 0.12), (0.3, 0.3, 0.24), "concrete")

def supply_crate():
    cube("Crate_Core", (0, 0, 0.45), (1.0, 0.82, 0.9), "wood")
    for z in (0.1, 0.8):
        cube("Front_Strapping", (0, -0.42, z), (0.92, 0.045, 0.075), "metal")
    for x in (-0.42, 0.42):
        cube("Corner_Guard", (x, -0.435, 0.45), (0.07, 0.04, 0.82), "paint_faded")
    cube("Latch", (0, -0.47, 0.46), (0.15, 0.04, 0.12), "metal")

def lumen_pod():
    # Faceted seed-like resource silhouette with a restrained luminous core.
    cylinder("Pod_Lower_Stem", (0, 0, 0.25), 0.19, 0.5, "paint_teal", 6, 0.11)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=0.42, location=(0, 0, 0.67))
    pod = bpy.context.object
    pod.name = "Lumen_Pod_Faceted_Shell"
    pod.scale = (0.72, 0.72, 1.35)
    pod.data.materials.append(MATS["glow_cyan"])
    # Three small crystal fins create an unmistakable silhouette.
    for angle in (0, 2.094, 4.188):
        fin = cube("Pod_Fin", (0.25*math.cos(angle), 0.25*math.sin(angle), 0.72),
                   (0.14, 0.12, 0.48), "glow_lime", 0.015)
        fin.rotation_euler[1] = -0.35
        fin.rotation_euler[2] = angle

def portal_relay():
    # Portable industrial relay frame; the production portal architecture can reuse this kit.
    for x in (-0.85, 0.85):
        cube("Frame_Pillar", (x, 0, 1.25), (0.22, 0.32, 2.5), "metal_dark")
        cube("Pillar_Inlay", (x, -0.18, 1.3), (0.07, 0.035, 1.8), "glow_cyan", 0.01)
    cube("Frame_Header", (0, 0, 2.42), (1.92, 0.34, 0.25), "paint_teal")
    cube("Header_Light", (0, -0.19, 2.42), (1.35, 0.035, 0.055), "glow_pink", 0.01)
    cube("Base_Left", (-0.55, 0, 0.12), (0.7, 0.65, 0.24), "metal")
    cube("Base_Right", (0.55, 0, 0.12), (0.7, 0.65, 0.24), "metal")

ASSETS = [
    ("dj_motel_sign", motel_sign),
    ("dj_fuel_pump", fuel_pump),
    ("dj_street_lamp", street_lamp),
    ("dj_supply_crate", supply_crate),
    ("bloom_lumen_pod", lumen_pod),
    ("dj_portal_relay_frame", portal_relay),
]

for asset_name, build in ASSETS:
    export_asset(asset_name, build)

print("Finished Space Hippie starter props:", len(ASSETS))
