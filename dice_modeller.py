# Generate and export STL files for a full set of roleplaying dice
# Import basic system modules
import bpy
import os

# Import dice modules
import D4
import D6
import D8
import D10
import D12
import D20
import D100
from math import radians

# Enable new shapes for dice
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
    "tracker_url": "",
    "support": "TESTING",
    "category": "Add Mesh",
}

# Deletes the die in the scene
def deleteDie():
    obj = bpy.context.scene.objects["die"]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()

# Create the GUI for the dice creation
class DiceModellerPanel(bpy.types.Panel):
    # Creates a Panel in the 3D Viewport
    bl_label = "Dice Modeller"
    bl_idname = "OBJECT_PT_dice_modeller"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Dice"

    def draw(self, context):
        layout = self.layout
        # Create the D4 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D4")
        row.prop(context.scene, "D4Scale", text="Scale")
        # Create the D6 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D6")
        row.prop(context.scene, "D6Scale", text="Scale")
        # Create the D8 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D8")
        row.prop(context.scene, "D8Scale", text="Scale")
        # Create the D10 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D10")
        row.prop(context.scene, "D10Scale", text="Scale")
        # Create the D12 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D12")
        row.prop(context.scene, "D12Scale", text="Scale")
        # Create the D20 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D20")
        row.prop(context.scene, "D20Scale", text="Scale")
        # Create the D100 checkbox and scale float
        row = layout.row()
        row.prop(context.scene, "D100")
        row.prop(context.scene, "D100Scale", text="Scale")
        # Create the font selection field
        row = layout.row()
        row.prop(context.scene, "font_select_path", text="Font")
        # Create the export folder selection field
        row = layout.row()
        row.prop(context.scene, "folder_select_path", text="Output Folder")
        # Create the activation button
        row = layout.row()
        row.operator("mesh.dice_modeller")

# Identifies and activates the GUI elements
class DiceModellerOperator(bpy.types.Operator):
    # Runs the dice modeller function
    bl_idname = "mesh.dice_modeller"
    bl_label = "Run Dice Modeller"

    def execute(self, context):
        # Identify the checkboxes
        D4 = context.scene.D4
        D6 = context.scene.D6
        D8 = context.scene.D8
        D10 = context.scene.D10
        D12 = context.scene.D12
        D20 = context.scene.D20
        D100 = context.scene.D100
        # Identify the scale floats
        D4Scale = context.scene.D4Scale
        D6Scale = context.scene.D6Scale
        D8Scale = context.scene.D8Scale
        D10Scale = context.scene.D10Scale
        D12Scale = context.scene.D12Scale
        D20Scale = context.scene.D20Scale
        D100Scale = context.scene.D100Scale
        # Identify the font and export fields
        folder = context.scene.folder_select_path
        font = context.scene.font_select_path
        # Pass the GUI values to the generation logic
        dice_modeller(D4, D6, D8, D10, D12, D20, D100, D4Scale, D6Scale, D8Scale, D10Scale, D12Scale, D20Scale, D100Scale, folder, font)
        return {'FINISHED'}

# Field for selecting a font for the numbers on the dice
class FontSelectBrowseFontOperator(bpy.types.Operator):
    # Opens a file browser to select a font
    bl_idname = "mesh.font_select_browse_font"
    bl_label = "Font"

    def execute(self, context):
        context.scene.font_select_path = bpy.path.abspath(bpy.context.scene.font_select_path)
        return {'FINISHED'}

# Field for selecting a folder to export the dice to
class FolderSelectBrowseFolderOperator(bpy.types.Operator):
    # Opens a file browser to select a folder
    bl_idname = "mesh.folder_select_browse_folder"
    bl_label = "Browse..."

    def execute(self, context):
        context.scene.folder_select_path = bpy.path.abspath(bpy.context.scene.folder_select_path)
        return {'FINISHED'}

# Create the dice with the specified parameters
def dice_modeller(D4, D6, D8, D10, D12, D20, D100, D4Scale, D6Scale, D8Scale, D10Scale, D12Scale, D20Scale, D100Scale, folder, font):
    # Derive the font folder and name from the input font path
    fontName = font.split(".")[-2].split("\\")[-1].split("/")[-1] + font[-4:]
    fontFolder = font[0: -(len(fontName) + 1)]
    # Create the D4
    if D4:
        D4.makeD4(fontFolder, fontName, outputFolder, D4Scale)
        deleteDie()
    # Create the D6
    if D6:
        D6.makeD6(fontFolder, fontName, outputFolder, D6Scale)
        deleteDie()
    # Create the D8
    if D8:
        D8.makeD8(fontFolder, fontName, outputFolder, D8Scale)
        deleteDie()
    # Create the D10
    if D10:
        D10.makeD10(fontFolder, fontName, outputFolder, D10Scale)
        deleteDie()
    # Create the D12
    if D12:
        D12.makeD12(fontFolder, fontName, outputFolder, D12Scale)
        deleteDie()
    # Create the D20
    if D20:
        D20.makeD20(fontFolder, fontName, outputFolder, D20Scale)
        deleteDie()
    # Create the D100
    if D100:
        D100.makeD100(fontFolder, fontName, outputFolder, D100Scale)
        deleteDie()

# Registers the classes and UI properties
def register():
    # Register classes
    bpy.utils.register_class(DiceModellerPanel)
    bpy.utils.register_class(DiceModellerOperator)
    bpy.utils.register_class(FontSelectBrowseFontOperator)
    bpy.utils.register_class(FolderSelectBrowseFolderOperator)
    # Register checkboxes
    bpy.types.Scene.D4 = bpy.props.BoolProperty(name = "D4", default = True)
    bpy.types.Scene.D6 = bpy.props.BoolProperty(name = "D6", default = True)
    bpy.types.Scene.D8 = bpy.props.BoolProperty(name = "D8", default = True)
    bpy.types.Scene.D10 = bpy.props.BoolProperty(name = "D10", default = True)
    bpy.types.Scene.D12 = bpy.props.BoolProperty(name = "D12", default = True)
    bpy.types.Scene.D20 = bpy.props.BoolProperty(name = "D20", default = True)
    bpy.types.Scene.D100 = bpy.props.BoolProperty(name = "D100", default = True)
    # Register scale floats
    bpy.types.Scene.D4Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D6Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D8Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D10Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D12Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D20Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    bpy.types.Scene.D100Scale = bpy.props.FloatProperty(name = "Scale", default = 1.0, min = 0.01)
    # Register font and export fields
    bpy.types.Scene.folder_select_path = bpy.props.StringProperty(name = "Folder", default = s.path.expanduser('~\\'), subtype = 'DIR_PATH')
    bpy.types.Scene.font_select_path = bpy.props.StringProperty(name = "Font", default = "C:\\Windows\\Fonts\\arial.ttf", subtype = 'FILE_PATH')
    
def unregister():
    # Unregister classes
    bpy.utils.unregister_class(DiceModellerPanel)
    bpy.utils.unregister_class(DiceModellerOperator)
    bpy.utils.unregister_class(FolderSelectBrowseFolderOperator)
    bpy.utils.unregister_class(FontSelectBrowseFontOperator)
    # Unregister checkboxes
    del bpy.types.Scene.D4
    del bpy.types.Scene.D6
    del bpy.types.Scene.D8
    del bpy.types.Scene.D10
    del bpy.types.Scene.D12
    del bpy.types.Scene.D20
    del bpy.types.Scene.D100
    # Unregister scale floats
    del bpy.types.Scene.D4Scale
    del bpy.types.Scene.D6Scale
    del bpy.types.Scene.D8Scale
    del bpy.types.Scene.D10Scale
    del bpy.types.Scene.D12Scale
    del bpy.types.Scene.D20Scale
    del bpy.types.Scene.D100Scale
    # Unregister font and export fields
    del bpy.types.Scene.folder_select_path
    del bpy.types.Scene.font_select_path

if __name__ == "__main__":
    register()
