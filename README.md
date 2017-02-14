# Maxlength Folder Eraser
It's a script used to take care of issues regarding folders and files with too many characters

> Tested on Windows10 and Ubuntu16. Because of the function **os.scandir()** it only works on Python 3.6+

# Warning

## Precautions
* Already tested on nested and simple folders with files but be aware that there are **No Guarantees**
* This script will rename all files and folders into the ``-dir`` parameter, use it very, very, carefully!!!

## Warranty
There is no warranty of this script. For more information, read the MIT Licence

# How to Use it
1. Clone or download the ``__init__.py`` file

2. Be sure to be using Python 3.6+ by running ``python --version`` on your command prompt

3. Run the following command:
 
 1. **Windows:** ``python __init__.py -dir "C:\path\to\folder" -silent``
 
 2. **Linux:** ``.\__init__.py -dir "C:\path\to\folder" -silent``

* The script is **verbose name** by default

* Use ```-silent```parameter to use it in quiet mode or just use the ```-dir``` parameter to inform the folder

# Log system
By default, the filename is **maxlength-folder-eraser.log** and you can check the entire process there! 
