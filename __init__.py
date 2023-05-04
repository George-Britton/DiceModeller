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

if "bpy" in locals():
    import importlib
    importlib.reload(D4)
    importlib.reload(D6)
    importlib.reload(D8)
    importlib.reload(D10)
    importlib.reload(D12)
    importlib.reload(D20)
    importlib.reload(D100)
    importlib.reload(os)
    importlib.reload(dice_modeller)
else:
    from . import D4
    from . import D6
    from . import D8
    from . import D10
    from . import D12
    from . import D20
    from . import D100
    from . import os
    from . import dice_modeller

import bpy

def register():
    dice_modeller.register()



def unregister():
    dice_modeller.unregister()


if __name__ == "__main__":
    register()
