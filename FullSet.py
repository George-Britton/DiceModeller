#Full Set
import bpy
from math import radians
bpy.ops.preferences.addon_enable(module="add_mesh_extra_objects")

def deleteDie():
    obj = bpy.context.scene.objects["die"]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()

class D4:
    def __init__(self):
        self.scale = 1
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

    def makeD4(self, fontFolder, fontName, outputFolder):
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
        font = self.pathify(fontFolder, fontName)
        self.make4(font)
        self.make3(font)
        self.make2(font)
        self.make1(font)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D4_" + fontName.split(".")[0] + ".stl"))
    
class D6:
    def __init__(self):
        self.scale = 1
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

    def makeD6(self, fontFolder, fontName, outputFolder):
        bpy.ops.mesh.primitive_cube_add()
        die = bpy.context.active_object
        die.name = "die"
        #scale
        die.dimensions[2] = 16
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        font = self.pathify(fontFolder, fontName)
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
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D6_" + fontName.split(".")[0] + ".stl"))
    
class D8:
    def __init__(self):
        self.scale = 1
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

    def makeD8(self, fontFolder, fontName, outputFolder):
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
        font = self.pathify(fontFolder, fontName)
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
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D8_" + fontName.split(".")[0] + ".stl"))
    
class D10:
    def __init__(self):
        self.scale = 1
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
        if digit == "_":
            num.location[1] -= 3
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

    def makeD10(self, fontFolder, fontName, outputFolder):
        die = self.makeShape()
        die.rotation_euler[0] = radians(-54.3)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 17
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        font = self.pathify(fontFolder, fontName)
        self.make(6, font)
        self.make("_", font)
        die.select_set(True)
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
        self.make(8, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(2, font)
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
        self.make(1, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(9, font)
        self.make("_", font)
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
        self.make(7, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(5, font)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D10_" + fontName.split(".")[0] + ".stl"))
    
class D12:
    def __init__(self):
        self.scale = 1
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
        if digit == "_":
            num.location[1] -= 3
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD12(self, fontFolder, fontName, outputFolder):
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
        font = self.pathify(fontFolder, fontName)
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
        self.make("_", font)
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
        self.make("_", font)
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
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D12_" + fontName.split(".")[0] + ".stl"))
    
class D20:
    def __init__(self):
        self.scale = 1
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
        if digit == "_":
            if pos:
                num.location[1] -= 3
            else:
                num.location[1] += 3
        if not pos:
            num.rotation_euler[2] = radians(180)
        bpy.data.objects["die"].select_set(True)
        self.stamp()
        self.deleteNum()

    def makeD20(self, fontFolder, fontName, outputFolder):
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
        font = self.pathify(fontFolder, fontName)
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
        self.make("_", font, True)
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
        die.select_set(True)
        die.rotation_euler[0] = radians(0)
        die.rotation_euler[2] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(-41.8)
        self.make(3, font, False)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D20_" + fontName.split(".")[0] + ".stl"))
    
class D100:
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
        if digit == "_":
            num.location[1] -= 3
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

    def makeD100(self, fontFolder, fontName, outputFolder):
        die = self.makeShape()
        die.rotation_euler[0] = radians(-54.3)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        #scale
        die.dimensions[2] = 17
        die.scale[0] = die.scale[2]
        die.scale[1] = die.scale[2]
        font = self.pathify(fontFolder, fontName)
        self.make(60, font)
        die.select_set(True)
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
        self.make(80, font)
        die.select_set(True)
        die.rotation_euler[0] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[1] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        die.rotation_euler[0] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.make(20, font)
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
        self.make(10, font)
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
        self.make(30, font)
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
        self.make(50, font)
        die.select_set(True)
        bpy.ops.export_mesh.stl(filepath=self.pathify(outputFolder, "D100_" + fontName.split(".")[0] + ".stl"))

def makeDSet(fontFolder, fontName, outputFolder, in4Scale, in6Scale, in8Scale, in10Scale, in12Scale, in20Scale, in100Scale):
    d4 = D4()
    if in4Scale != 1:
        d4.scale = in4Scale
    d4.makeD4(fontFolder, fontName, outputFolder)
    deleteDie()
    del d4
    d6 = D6()
    if in6Scale != 1:
        d6.scale = in6Scale
    d6.makeD6(fontFolder, fontName, outputFolder)
    deleteDie()
    del d6
    d8 = D8()
    if in8Scale != 1:
        d8.scale = in8Scale
    d8.makeD8(fontFolder, fontName, outputFolder)
    deleteDie()
    del d8
    d10 = D10()
    if in10Scale != 1:
        d10.scale = in10Scale
    d10.makeD10(fontFolder, fontName, outputFolder)
    deleteDie()
    del d10
    d12 = D12()
    if in12Scale != 1:
        d12.scale = in12Scale
    d12.makeD12(fontFolder, fontName, outputFolder)
    deleteDie()
    del d12
    d20 = D20()
    if in20Scale != 1:
        d20.scale = in20Scale
    d20.makeD20(fontFolder, fontName, outputFolder)
    deleteDie()
    del d20
    d100 = D100()
    if in100Scale != 1:
        d100.scale = in100Scale
    d100.makeD100(fontFolder, fontName, outputFolder)
    deleteDie()
    del d100

if __name__ == "__main__":
    # Edit these to change font and destination
    systemFontFolderPath = "C:/Windows/Fonts"
    chosenFontNameAndExtension = "arial.ttf"
    outputDestinationFolder = "C:/Users/geo-g/Documents/TTRPG/Dice"
    # These are used to change the size of the numbers on the dice, not the dice themselves
    d4Scale = 1
    d6Scale = 1
    d8Scale = 1
    d10Scale = 1
    d12Scale = 1
    d20Scale = 1
    d100Scale = 1
    # Leave this following line alone, it's what calls for the generation
    makeDSet(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder, d4Scale, d6Scale, d8Scale, d10Scale, d12Scale, d20Scale, d100Scale)