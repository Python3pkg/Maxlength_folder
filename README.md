# Maxlength Folder Eraser
It's a script used to take care of issues regarding folders and files with too many characters

## Tests
Tested on Windows10 and Ubuntu16. Works only on Python 3.6+

## Performance
The script took about 13 minutes to finish a 250GB repository, with very nested folders (dozens of folder levels) and also files that exceeded the maximum length allowed by the NTFS system.

Unfortunately, we cannot use multiple threads because the recursive process needs to be synchronous, but we can merge from the old **listdir** function to **scandir** function (Contained in the OS module - Python 3.6) and make it faster (Part of the code is already using the new function).

# Warning

## Precautions
* Already tested on nested folders with files but be aware that there are **No Guarantees**
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
