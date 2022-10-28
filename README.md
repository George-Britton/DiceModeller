<!-- markdownlint-disable MD033 --> 
 # 
  
 <p align="center"><h1>Dice Modeller</h1></p> 
  
 <!-- markdownlint-enable MD033 --> 
  
 Dice Modeller is a collection of python scripts that can be run in Blender to generate and export an .STL file for each die in a standard roleplaying set. 
  
 - **Font Customisation**: Choose which font to print the numbers in on the dice.
 - **Automatically Generated STL**: Set your own output folder to have the 3D model exported to.
  
 ----- 
  
 ## How to Use 
  
 Each die has its own separate generation script. Running one in the 'Text Editor' tab of Blender will generate and export an .STL file for that die.

At the bottom of each file, you'll see the following lines:

```python
if __name__ == "__main__": 
    # Edit these to change font and destination
    systemFontFolderPath = "C:/Windows/Fonts" 
    chosenFontNameAndExtension = "arial.ttf" 
    outputDestinationFolder = "G:/George/Documents/3D Prints/STL/DICE/Auto-Generated" 
    makeDX(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder)
```

Depending on your operating system, you may want to change the value of `systemFontFolderPath` to your system's font folder. The one there already is the default path for most modern Windows computers.

The font you want to use for the numbers should be the value of `chosenFontNameAndExtension`. Make sure you use the correct file extension - they're not all .TTF files.

Wherever you want to output your models, set the filepath as the value of `outputDestinationFolder`. It's important that the folder exists before you run the script, as you'll get an error saying the filepath doesn't exist otherwise.
