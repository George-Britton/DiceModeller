#D4
#d4.transform_apply(location=False, rotation=True, scale=False)
import bpy
from math import radians

def stamp():
    obj = bpy.context.scene.objects["d4"]
    bpy.data.objects['Text'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
    bpy.ops.object.modifier_apply(modifier="Boolean")

def deleteNum():
    obj = bpy.context.scene.objects["Text"]
    bpy.data.objects['d4'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()

def make4():
    #4.1
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text="4")
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [8, 8, 0.05]
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    num.location = [0, 7, 5]
    stamp()
    #4.2
    d4 = bpy.context.scene.objects["d4"]
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    #4.3
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    d4.rotation_euler[2] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    deleteNum()

def make3():
    #3.1
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text="3")
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [8, 8, 0.05]
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    num.location = [0, 7, 5]
    stamp()
    #3.2
    d4 = bpy.context.scene.objects["d4"]
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    #3.3
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    d4.rotation_euler[2] = radians(-120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    deleteNum()

def make2():
    #2.1
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text="2")
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [8, 8, 0.05]
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    num.location = [0, 7, 5]
    stamp()
    #2.2
    d4 = bpy.context.scene.objects["d4"]
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    #2.3
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[2] = radians(-120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    deleteNum()

def make1():
    #1.1
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text="1")
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [8, 8, 0.05]
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    num.location = [0, 7, 5]
    bpy.data.objects["d4"].select_set(True)
    stamp()
    #1.2
    d4 = bpy.context.scene.objects["d4"]
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    #1.3
    d4.rotation_euler[0] = radians(-19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(120)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[0] = radians(19.47)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    stamp()
    deleteNum()

def makeD4():
    bpy.ops.mesh.primitive_solid_add()
    d4 = bpy.context.active_object
    d4.name = "d4"
    #scale
    d4.dimensions[2] = 20
    d4.scale[0] = d4.scale[2]
    d4.scale[1] = d4.scale[2]
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    #rotate for initial numbering
    d4.rotation_euler[2] = radians(-30)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    d4.rotation_euler[1] = radians(180)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make4()
    make3()
    make2()
    make1()

if __name__ == "__main__":
    makeD4();
