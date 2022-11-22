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
    scale = 1
    makeDX(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder)
```

Depending on your operating system, you may want to change the value of `systemFontFolderPath` to your system's font folder. The one there already is the default path for most modern Windows computers.

The font you want to use for the numbers should be the value of `chosenFontNameAndExtension`. Make sure you use the correct file extension - they're not all .TTF files.

Wherever you want to output your models, set the filepath as the value of `outputDestinationFolder`. It's important that the folder exists before you run the script, as you'll get an error saying the filepath doesn't exist otherwise.

----- 
 ## Common Issues
 
 - **Invalid Path**: Make sure whatever paths you put in the `systemFontFolderPath` and `outputDestinationFolder` are correct. If you use a backslash ('\\'), make sure to use two in order to escape the string escape character. Or just use a forward slash, like in the example paths.
 - **Font Doesn't Exist**: The chosen font set in `chosenFontNameAndExtension` must have the exact same value, i.e. the exact same capitalisation and file extension.
 - **Generated Die is Just Floating Numbers / Has Embossed Numbers**: This error is usually caused by the chosen font generating numbers that are too large for the die's face. To remedy this, you can edit the value of the `scale` to change the font size. Play around with the value to see what works for you.
 - **I've installed a new font but the script can't find it in the Fonts folder**: This can sometimes be an issue with the font path. When you install new fonts, they sometimes install to a different folder, try replacing the `systemFontFolderPath` to something along the lines of "C:/Users/<NAME>/AppData/Local/Microsoft/Windows/Fonts". You can find the right folder by opening the font folder in the File Explorer, and right clicking on your chosen font, then select "Properties". The file path you want will be marked as "Location" in the "General" tab.

----- 
 ## F.A.Q.
 
 - **Q**: Can I make my own handwriting into dice?
 - **A**: Yep, go to [Calligraphr](https://www.calligraphr.com/) and turn your handwriting into a font, then save that font to your system font folder.
 
 - **Q**: What if I want dice with symbols instead of numbers?
 - **A**: If you want to make symbols to print onto numbers, you can either:
    * Go into the file and change the value of the `make` function calls.
    * If the symbols you want aren't standard unicode symbols, you can do similarly to the previous answer and go to [Calligraphr](https://www.calligraphr.com/), and put your chosen symbols in the number value slots of the faces you want printed. Then follow the previous question's instructions as normal.
