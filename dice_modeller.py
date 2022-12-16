import bpy
import os
from math import radians
bpy.ops.preferences.addon_enable(module="add_mesh_extra_objects")

bl_info = {
    "name": "Dice Modeller",
    "description":
        "Generate and export STL files for a full set of roleplaying dice.",
    "author": "George Britton",
    "version": (1, 0),
    "blender": (2, 93, 1),
    "location": "View3D > UI > Dice",
    "warning": "",
    "doc_url": "https://github.com/George-Britton/DiceModeller"
                "Scripts/My_Script",
    "tracker_url": "",
    "support": "TESTING",
    "category": "Mesh",
}

T = True
F = False


def deleteDie():
    obj = bpy.context.scene.objects["die"]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()


class Die4:
    def __init__(self, inScale=1):
        self.scale = inScale

    def pathify(self, path, name):
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

    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        text = bpy.data.objects["Text"]
        bpy.context.object.modifiers["Boolean"].object = text
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
        bpy.ops.object.text_add(enter_editmode=False,
                                align='WORLD',
                                location=(0, 0, 0),
                                scale=(1, 1, 1))
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
        msh = bpy.ops.mesh
        msh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip": F,
                                                        "use_dissolve_ortho_edges": F,
                                                        "mirror": F},
                                                        TRANSFORM_OT_translate={"value": ( 0, 0, 49.5538),
                                                        "orient_type": 'NORMAL',
                                                        "orient_matrix": ((0, -1, 0), (1, 0, -0), (0, 0, 1)),
                                                        "orient_matrix_type": 'NORMAL',
                                                        "constraint_axis": (F, F, T),
                                                        "mirror": F,
                                                        "use_proportional_edit": F,
                                                        "proportional_edit_falloff": 'SMOOTH',
                                                        "proportional_size": 1,
                                                        "use_proportional_connected": F,
                                                        "use_proportional_projected": F,
                                                        "snap": F,
                                                        "snap_target": 'CLOSEST',
                                                        "snap_point": (0, 0, 0),
                                                        "snap_align": F,
                                                        "snap_normal": (0, 0, 0),
                                                        "gpencil_strokes": F,
                                                        "cursor_transform": F,
                                                        "texture_space": F,
                                                        "remove_on_cancel": F,
                                                        "release_confirm": F,
                                                        "use_accurate": F,
                                                        "use_automerge_and_split": F})
        bpy.ops.object.editmode_toggle()
        num.scale = [8 * self.scale, 8 * self.scale, 0.035]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME',
                                  center='MEDIAN')
        num.location = [0, 7, 5]
        return num

    def make4(self, font):
        #4.1
        num = self.makeNum(4, font)
        self.stamp()
        #4.2
        die = bpy.context.scene.objects["die"]
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        #4.3
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.deleteNum()

    def make3(self, font):
        #3.1
        num = self.makeNum(3, font)
        self.stamp()
        #3.2
        die = bpy.context.scene.objects["die"]
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        #3.3
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.deleteNum()

    def make2(self, font):
        #2.1
        num = self.makeNum(2, font)
        self.stamp()
        #2.2
        die = bpy.context.scene.objects["die"]
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        #2.3
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.deleteNum()

    def make1(self, font):
        #1.1
        num = self.makeNum(1, font)
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        #1.2
        die = bpy.context.scene.objects["die"]
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        #1.3
        die.rotation_euler[0] = radians(-19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(19.47)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp()
        self.deleteNum()

    def makeD4(self, font, outputFolder):
        bpy.ops.mesh.primitive_solid_add()
        die = bpy.context.active_object
        die.name = "die"
        #scale
        die.dimensions[2] = 20
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        #rotate for initial numbering
        die.rotation_euler[2] = radians(-30)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make4(font)
        self.make3(font)
        self.make2(font)
        self.make1(font)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D4_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die6:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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
        
    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [12 * self.scale, 12 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        return num

    def make(self, digit, font):
        num = self.makeNum(digit, font)
        num.location = [0, 0, 8.6]
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD6(self, font, outputFolder):
        bpy.ops.mesh.primitive_cube_add()
        die = bpy.context.active_object
        die.name = "die"
        #scale
        die.dimensions[2] = 16
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        self.make(6, font)
        die.rotation_euler[2] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(2, font)
        die.select_set(True)
        die.rotation_euler[2] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(4, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(3, font)
        die.select_set(True)
        die.rotation_euler[2] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(1, font)
        die.select_set(True)
        die.rotation_euler[2] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(5, font)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D6_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die8:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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

    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [12 * self.scale, 12 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        num.location = [0, 0, 8.6]
        return num

    def make(self, digit, font):
        num = self.makeNum(digit, font)
        num.location = [0, 0, 8.6]
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD8(self, font, outputFolder):
        bpy.ops.mesh.primitive_solid_add(source='8')
        die = bpy.context.active_object
        die.name = "die"
        #rotate
        die.rotation_euler[1] = radians(45)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 16.4
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        self.make(8, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(2, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(6, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(4, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(5, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(3, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(7, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(1, font)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D8_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die10:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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
        
    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [8 * self.scale, 8 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        num.location = [0, -1.5, 9]
        return num

    def make(self, digit, font):
        num = self.makeNum(digit, font)
        if digit == "~":
            num.location[1] -= self.scale * 3.7
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeShape(self):
        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        die1 = bpy.context.active_object
        die1.name = "intersect"
        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        die2 = bpy.context.active_object
        die2.name = "die"
        die1.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[die1.name]
        bpy.ops.object.modifier_apply(modifier="Boolean")
        obj = bpy.context.scene.objects["intersect"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()
        bpy.data.objects['die'].select_set(True)
        return die2

    def makeD10(self, font, outputFolder):
        die = self.makeShape()
        die.rotation_euler[0] = radians(-54.3)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 17
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        self.make(2, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(5, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(8, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(7, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(0, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(4, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(3, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(6, font)
        self.make("~", font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(9, font)
        self.make("~", font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(1, font)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D10_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die12:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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
        
    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [8 * self.scale, 8 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        num.location = [0, 0, 9.75]
        return num

    def make(self, digit, font):
        num = self.makeNum(digit, font)
        if digit == "~":
            num.location[1] -= self.scale * 3.7
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD12(self, font, outputFolder):
        bpy.ops.mesh.primitive_solid_add(source='12')
        die = bpy.context.active_object
        die.name = "die"
        #rotate
        die.rotation_euler[0] = radians(-58.285)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 18.5
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        self.make(12, font)
        die.select_set(True)
        die.rotation_euler[2] = radians(36)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(8, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(6, font)
        self.make("~", font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(4, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(2, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(10, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(36)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(1, font)
        die.select_set(True)
        die.rotation_euler[2] = radians(36)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(3, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(11, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(9, font)
        self.make("~", font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(7, font)
        die.select_set(True)
        die.rotation_euler[0] = 0
        die.rotation_euler[2] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(63.43)
        self.make(5, font)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D12_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die20:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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
        
    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [8 * self.scale, 8 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        num.location = [0, 0, 11]
        return num

    def make(self, digit, font, pos):
        num = self.makeNum(digit, font)
        if digit == "~":
            if pos:
                num.location[1] -= self.scale * 3
            else:
                num.location[1] += self.scale * 3
        if not pos:
            num.rotation_euler[2] = radians(180)
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD20(self, font, outputFolder):
        bpy.ops.mesh.primitive_solid_add(source='20')
        die = bpy.context.active_object
        die.name = "die"
        #rotate
        die.rotation_euler[0] = radians(20.905)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 20.7
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        self.make(20, font, True)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(14, font, True)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(6, font, True)
        self.make("~", font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(4, font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(8, font, True)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(10, font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(16, font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(2, font, True)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(18, font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        self.make(12, font, True)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(1, font, False)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(13, font, False)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(5, font, False)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(11, font, False)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(7, font, False)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(17, font, False)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(15, font, False)
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[2] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(19, font, False)
        die.select_set(True)
        die.rotation_euler[2] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(9, font, False)
        self.make("~", font, False) 
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(3, font, False)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D20_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))
    
class Die100:
    def __init__(self, inScale = 1):
        self.scale = inScale
    def pathify(self, path, name):
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
        
    def stamp(self):
        obj = bpy.context.scene.objects["die"]
        bpy.data.objects['Text'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
        bpy.ops.object.modifier_apply(modifier="Boolean")

    def deleteNum(self):
        obj = bpy.context.scene.objects["Text"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()

    def makeNum(self, number, font):
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
        num.scale = [8 * self.scale, 8 * self.scale, 0.05]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        num.location = [0, -1.5, 9]
        return num

    def make(self, digit, font):
        num = self.makeNum(digit, font)
        if digit == "~":
            num.location[1] -= self.scale * 3.7
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeShape(self):
        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        die1 = bpy.context.active_object
        die1.name = "intersect"
        bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=2, radius2=0, depth=2.25, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        die2 = bpy.context.active_object
        die2.name = "die"
        die1.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[die1.name]
        bpy.ops.object.modifier_apply(modifier="Boolean")
        obj = bpy.context.scene.objects["intersect"]
        bpy.data.objects['die'].select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()
        bpy.data.objects['die'].select_set(True)
        return die2

    def makeD100(self, font, outputFolder):
        die = self.makeShape()
        die.rotation_euler[0] = radians(-54.3)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 17
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        self.make(20, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(50, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(80, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(70, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make("00", font)
        die.select_set(True)
        die.rotation_euler[0] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(40, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(30, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(60, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(90, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(10, font)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D100_" + font.split(".")[-2].split("\\")[-1].split("/")[-1] + ".stl"))

class DiceModellerPanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport"""
    bl_label = "Dice Modeller"
    bl_idname = "OBJECT_PT_dice_modeller"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Dice"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene, "D4")
        row.prop(context.scene, "D4Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D6")
        row.prop(context.scene, "D6Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D8")
        row.prop(context.scene, "D8Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D10")
        row.prop(context.scene, "D10Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D12")
        row.prop(context.scene, "D12Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D20")
        row.prop(context.scene, "D20Scale", text="Scale")
        row = layout.row()
        row.prop(context.scene, "D100")
        row.prop(context.scene, "D100Scale", text="Scale")
        
        row = layout.row()
        row.prop(context.scene, "font_select_path", text="Font")
        
        row = layout.row()
        row.prop(context.scene, "folder_select_path", text="Output Folder")
        
        row = layout.row()
        row.operator("mesh.dice_modeller")

class DiceModellerOperator(bpy.types.Operator):
    """Runs the dice modeller function"""
    bl_idname = "mesh.dice_modeller"
    bl_label = "Run Dice Modeller"

    def execute(self, context):
        D4 = context.scene.D4
        D4Scale = context.scene.D4Scale
        D6 = context.scene.D6
        D6Scale = context.scene.D6Scale
        D8 = context.scene.D8
        D8Scale = context.scene.D8Scale
        D10 = context.scene.D10
        D10Scale = context.scene.D10Scale
        D12 = context.scene.D12
        D12Scale = context.scene.D12Scale
        D20 = context.scene.D20
        D20Scale = context.scene.D20Scale
        D100 = context.scene.D100
        D100Scale = context.scene.D100Scale
        folder = context.scene.folder_select_path
        font = context.scene.font_select_path
        dice_modeller(D4, D4Scale, D6, D6Scale, D8, D8Scale, D10, D10Scale, D12, D12Scale, D20, D20Scale, D100, D100Scale, folder, font)
        return {'FINISHED'}

class FontSelectBrowseFontOperator(bpy.types.Operator):
    """Opens a file browser to select a font"""
    bl_idname = "mesh.font_select_browse_font"
    bl_label = "Font"

    def execute(self, context):
        context.scene.font_select_path = bpy.path.abspath(bpy.context.scene.font_select_path)
        return {'FINISHED'}

class FolderSelectBrowseFolderOperator(bpy.types.Operator):
    """Opens a file browser to select a folder"""
    bl_idname = "mesh.folder_select_browse_folder"
    bl_label = "Browse..."

    def execute(self, context):
        context.scene.folder_select_path = bpy.path.abspath(bpy.context.scene.folder_select_path)
        return {'FINISHED'}

def dice_modeller(D4, D4Scale, D6, D6Scale, D8, D8Scale, D10, D10Scale, D12, D12Scale, D20, D20Scale, D100, D100Scale, output_folder, font):
    if D4:
        d4 = Die4(D4Scale)
        d4.makeD4(font, output_folder)
        deleteDie()
        del d4
    if D6:
        d6 = Die6(D6Scale)
        d6.makeD6(font, output_folder)
        deleteDie()
        del d6
    if D8:
        d8 = Die8(D8Scale)
        d8.makeD8(font, output_folder)
        deleteDie()
        del d8
    if D10:
        d10 = Die10(D10Scale)
        d10.makeD10(font, output_folder)
        deleteDie()
        del d10
    if D12:
        d12 = Die12(D12Scale)
        d12.makeD12(font, output_folder)
        deleteDie()
        del d12
    if D20:
        d20 = Die20(D20Scale)
        d20.makeD20(font, output_folder)
        deleteDie()
        del d20
    if D100:
        d100 = Die100(D100Scale)
        d100.makeD100(font, output_folder)
        deleteDie()
        del d100

def register():
    bpy.utils.register_class(DiceModellerPanel)
    bpy.utils.register_class(DiceModellerOperator)
    bpy.utils.register_class(FontSelectBrowseFontOperator)
    bpy.utils.register_class(FolderSelectBrowseFolderOperator)
    bpy.types.Scene.D4 = bpy.props.BoolProperty(name="D4", default=True)
    bpy.types.Scene.D4Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D6 = bpy.props.BoolProperty(name="D6", default=True)
    bpy.types.Scene.D6Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D8 = bpy.props.BoolProperty(name="D8", default=True)
    bpy.types.Scene.D8Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D10 = bpy.props.BoolProperty(name="D10", default=True)
    bpy.types.Scene.D10Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D12 = bpy.props.BoolProperty(name="D12", default=True)
    bpy.types.Scene.D12Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D20 = bpy.props.BoolProperty(name="D20", default=True)
    bpy.types.Scene.D20Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.D100 = bpy.props.BoolProperty(name="D100", default=True)
    bpy.types.Scene.D100Scale = bpy.props.FloatProperty(name="Scale", default=1.0, min=0.01)
    bpy.types.Scene.folder_select_path = bpy.props.StringProperty(name="Folder", default=os.path.expanduser('~\\'), subtype='DIR_PATH')
    bpy.types.Scene.font_select_path = bpy.props.StringProperty(name="Font", default="C:\\Windows\\Fonts\\arial.ttf", subtype='FILE_PATH')
    
def unregister():
    bpy.utils.unregister_class(DiceModellerPanel)
    bpy.utils.unregister_class(DiceModellerOperator)
    bpy.utils.unregister_class(FolderSelectBrowseFolderOperator)
    bpy.utils.unregister_class(FontSelectBrowseFontOperator)
    del bpy.types.Scene.D4
    del bpy.types.Scene.D4Scale
    del bpy.types.Scene.D6
    del bpy.types.Scene.D6Scale
    del bpy.types.Scene.D8
    del bpy.types.Scene.D8Scale
    del bpy.types.Scene.D10
    del bpy.types.Scene.D10Scale
    del bpy.types.Scene.D12
    del bpy.types.Scene.D12Scale
    del bpy.types.Scene.D20
    del bpy.types.Scene.D20Scale
    del bpy.types.Scene.D100
    del bpy.types.Scene.D100Scale
    del bpy.types.Scene.folder_select_path
    del bpy.types.Scene.font_select_path


if __name__ == "__main__":
    register()
