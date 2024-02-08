# for baking fluid simulation
# works ok on blender 4.0.2

import bpy

import bpy

for scene in bpy.data.scenes:
    print('scene', scene)
    for object in scene.objects:
        print('object', object)
        for modifier in object.modifiers:
            print('modifier', modifier, 'modifier_type', modifier.type)
            if modifier.type == 'FLUID':
                print('modifier.fluid_type', modifier.fluid_type)
                if modifier.fluid_type == 'DOMAIN':
                    print('baking...')
                    object.select_set(True)
                    bpy.context.view_layer.objects.active = object
                    bpy.ops.fluid.bake_all()

bpy.ops.wm.save_mainfile()
