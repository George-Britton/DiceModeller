#D6
import bpy
from math import radians

def pathify(path, name):
    splitFilepath = path.split("\\")
    newFilepath = ""
    if len(splitFilepath) > 1:
        for i in splitFilepath:
            newFilepath += i + "/"
    else:
        newFilepath = splitFilepath[0] + "/"
    if newFilepath[-1] == "/" and newFilepath[-2] == "/":
        newFilepath = newFilepath[0:-1]
    newFilepath += name
    return newFilepath
    
def stamp():
    obj = bpy.context.scene.objects["die"]
    bpy.data.objects['Text'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
    bpy.ops.object.modifier_apply(modifier="Boolean")

def deleteNum():
    obj = bpy.context.scene.objects["Text"]
    bpy.data.objects['die'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()

def makeNum(number, font):
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=str(number))
    bpy.ops.object.editmode_toggle()
    bpy.data.objects["Text"].data.font = bpy.data.fonts.load(font)
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [12, 12, 0.05]
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    return num

def make(digit, font):
    num = makeNum(digit, font)
    num.location = [0, 0, 8.6]
    bpy.data.objects["die"].select_set(True)
    stamp()
    deleteNum()

def makeD6(fontFolder, fontName, outputFolder):
    bpy.ops.mesh.primitive_cube_add()
    die = bpy.context.active_object
    die.name = "die"
    #scale
    die.dimensions[2] = 16
    die.scale[0] = die.scale[2]
    die.scale[1] = die.scale[2]
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    font = pathify(fontFolder, fontName)
    make(6, font)
    die.rotation_euler[2] = radians(90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    die.rotation_euler[1] = radians(-90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make(2, font)
    die.select_set(True)
    die.rotation_euler[2] = radians(90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    die.rotation_euler[1] = radians(-90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make(4, font)
    die.select_set(True)
    die.rotation_euler[0] = radians(180)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make(3, font)
    die.select_set(True)
    die.rotation_euler[2] = radians(-90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    die.rotation_euler[1] = radians(90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make(1, font)
    die.select_set(True)
    die.rotation_euler[2] = radians(-90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    die.rotation_euler[1] = radians(90)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    make(5, font)
    bpy.ops.export_mesh.stl(filepath=pathify(outputFolder, "D6_" + fontName.split(".")[0] + ".stl"))

if __name__ == "__main__":
    # Edit these to change font and destination
    systemFontFolderPath = "C:/Windows/Fonts"
    chosenFontNameAndExtension = "arial.ttf"
    outputDestinationFolder = "G:/George/Documents/3D Prints/STL/DICE/Auto-Generated"
    makeD6(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder)