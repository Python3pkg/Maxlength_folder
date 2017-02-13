#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import uuid
import timeit
import logging as log
from time import gmtime, strftime

def Analise(folders):
    
    # Dirs receives subfolders
    Dirs    = []
     
    # walk trough the folders on the "folders" param
    for folder in folders:
        
        # walk truogh the subfolders into the iterated  "folder" var
        for d in os.listdir(folder):
            
            # Create the Unique ID
            
            UID = uuid.uuid4()
            UID = UID.hex [:10]
            
            # Rename files
            
            # Log the entire process to a file
            
            # Do not rename folders/files with 10 chars (seems to be faster)
            
            if len(d) > 10:
            
                try:
                    print(os.path.join(folder,d), os.path.join(folder, UID))

                except:
                    
                    e = sys.exc_info()[0]

            
        # Read again the dirs - now it's already renamed
        for d in os.listdir(folder):
                
            # add the folders into a list
            path = os.path.join(folder,d)
            
            if os.path.isdir(path):
                
                Dirs.append(os.path.join(folder,d))
            
            
        # Recursively calls the function passing the list "Dirs" as a new parameter
        Analise(Dirs)
        
root_dir = "C:\\Users\\frreinert\\Desktop\\QUALIDADE"
Analise(root_dir)