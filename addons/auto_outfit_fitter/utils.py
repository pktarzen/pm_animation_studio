import bpy
from mathutils import Vector


# --------------------------------------------------
# BODY ANALYSIS
# --------------------------------------------------

def analyze_body(obj):

    bbox = [obj.matrix_world @ Vector(v) for v in obj.bound_box]

    xs = [v[0] for v in bbox]
    ys = [v[1] for v in bbox]
    zs = [v[2] for v in bbox]

    width = max(xs) - min(xs)
    depth = max(ys) - min(ys)
    height = max(zs) - min(zs)

    return width, depth, height


# --------------------------------------------------
# ARMATURE COPY
# --------------------------------------------------

def copy_armature(body, cloth):

    armature_mod = None

    for mod in body.modifiers:
        if mod.type == 'ARMATURE':
            armature_mod = mod
            break

    if armature_mod:

        already_exists = False

        for mod in cloth.modifiers:
            if mod.type == 'ARMATURE':
                already_exists = True

        if not already_exists:

            new_mod = cloth.modifiers.new(
                name="PM_Armature",
                type='ARMATURE'
            )

            new_mod.object = armature_mod.object


# --------------------------------------------------
# FIT CLOTHES
# --------------------------------------------------

def fit_clothes(body):

    selected = bpy.context.selected_objects

    for obj in selected:

        if obj == body:
            continue

        if obj.type != 'MESH':
            continue

        try:
            bpy.context.view_layer.objects.active = obj

            bpy.ops.object.transform_apply(
                location=False,
                rotation=True,
                scale=True
            )

        except:
            pass

        shrink = obj.modifiers.new(
            name="PM_Shrinkwrap",
            type='SHRINKWRAP'
        )

        shrink.target = body
        shrink.offset = 0.003

        dt = obj.modifiers.new(
            name="PM_DataTransfer",
            type='DATA_TRANSFER'
        )

        dt.object = body

        copy_armature(body, obj)
