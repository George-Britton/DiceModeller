#Full Set
import bpy
from math import radians
bpy.ops.preferences.addon_enable(module="add_mesh_extra_objects")

# Deletes the die in the scene
def deleteDie():
    obj = bpy.context.scene.objects["die"]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()

# Create the dice with the specified parameters
def makeDSet(fontFolder, fontName, outputFolder, in4Scale, in6Scale, in8Scale, in10Scale, in12Scale, in20Scale, in100Scale):
    # Create the D4
    if in4Scale > 0:
        import D4
        D4.makeD4(fontFolder, fontName, outputFolder, in4Scale)
        deleteDie()
    # Create the D6
    if in6Scale > 0:
        import D6
        D6.makeD6(fontFolder, fontName, outputFolder, in6Scale)
        deleteDie()
    # Create the D8
    if in8Scale > 0:
        import D8
        D8.makeD8(fontFolder, fontName, outputFolder, in8Scale)
        deleteDie()
    # Create the D10
    if in10Scale > 0:
        import D10
        D10.makeD10(fontFolder, fontName, outputFolder, in10Scale)
        deleteDie()
    # Create the D12
    if in12Scale > 0:
        import D12
        D12.makeD12(fontFolder, fontName, outputFolder, in12Scale)
        deleteDie()
    # Create the D20
    if in20Scale > 0:
        import D20
        D20.makeD20(fontFolder, fontName, outputFolder, in20Scale)
        deleteDie()
    # Create the D100
    if in100Scale > 0:
        import D100
        D100.makeD100(fontFolder, fontName, outputFolder, in100Scale)
        deleteDie()

if __name__ == "__main__":
    # Edit these to change font and destination
    systemFontFolderPath = "C:/Users/geo-g/AppData/Local/Microsoft/Windows/Fonts"
    chosenFontNameAndExtension = "ethnocentric rg.otf"
    outputDestinationFolder = "C:/Users/geo-g/Documents/TTRPG/Dice"
    # These are used to change the size of the numbers on the dice, not the dice themselves
    # If you don't want a type of die, set the scale to 0, and it will not be generated
    d4Scale = 1
    d6Scale = 1
    d8Scale = 1
    d10Scale = 1
    d12Scale = 1
    d20Scale = 1
    d100Scale = 1
    # Leave this following line alone, it's what calls for the generation
    makeDSet(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder, d4Scale, d6Scale, d8Scale, d10Scale, d12Scale, d20Scale, d100Scale)
