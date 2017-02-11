#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import uuid
import timeit
import logging as log
from time import gmtime, strftime

# Log file setup
log.basicConfig(filename='maxlength-folder-eraser.log', level=log.INFO)

class output():
    
    Silent = False
    
    def __init__(self, silent):
        self.Silent = silent
        
    def out(self, string):
        if self.Silent == False:  
            print(string)

class version():
    """
    Version information
    """
    VERS        = 0.1
    DAT         = "11/02/2017"
    COPYRIGHT   = "Developed by Fabricio Roberto Reinert"
    
    def __init__(self, silent):
        o = output(silent)
        o.out("-------------------------------------")
        o.out("Version:         %f" % self.VERS)
        o.out("Last Revision:   %s" % self.DAT)
        o.out(self.COPYRIGHT)
        o.out("-------------------------------------")
        

class Argumentos():
    """
    Handle initial arguments
    """
    params  = dict()
    
    # handle the arguments and insert them into the dictionary "params"
    def __init__(self):
        if len(sys.argv) == 1:
            sys.exit("\n\n        Folder Name Shortener Tool\n\n    -dir : Specify a folder\n    -silent : Silent mode\n\n")
        
        for p in sys.argv:
            
            if p == "-dir":
                dir_index = sys.argv.index("-dir",)
                if dir_index+1 > len(sys.argv)-1:
                    sys.exit("\n>> ERROR: Folder not specified")
                else:
                    dir_index = dir_index+1
                    self.params["DIR"] = sys.argv[dir_index]
                    if not os.path.isdir(self.params["DIR"]):
                        sys.exit("\n>> ERROR: Folder  '%s' do not exist" % self.params["DIR"])
            
            if p == "-silent":
                self.params["SILENT"] = True
                
        if not "SILENT" in self.params:
            self.params["SILENT"] = False
    
    # Print Arguments
    def PrintArgs(self): 
        print("\n\n-----------\nArguments:\n-----------")
        for k, v in self.params.items():
            print("+ %s: %s" % (k,v))
            
def Analise(folders):
    
    # Dirs receives subfolders
    Dirs    = []
     
    # walk trough the folders on the "folders" param
    for folder in folders:
        
        # walk truogh the subfolders into the iterated  "folder" var
        for d in os.listdir(folder):
            
            # rename them
            
            UID = uuid.uuid4()
            UID = UID.hex [:8]
            
            # Log the entire process to a file
            try:
                os.rename(os.path.join(folder,d), os.path.join(folder, UID))
                log.info('Processing: ' + os.path.join(folder,d) + ' updated to: ' + os.path.join(folder, UID))
            except:
                
                e = sys.exc_info()[0]
                
                log.warning(os.path.join(folder,d) + ' could not be renamed to: ' + os.path.join(folder, UID))
                log.error(e)
            
            
        # Read again the dirs - now it's already renamed
        for d in os.listdir(folder):
                
            # add the folders into a list
            path = os.path.join(folder,d)
            
            if os.path.isdir(path):
                
                Dirs.append(os.path.join(folder,d))
            
            
        # Recursively calls the function passing the list "Dirs" as a new parameter
        Analise(Dirs)   
        
        
class Timer:
    """
    Used to calculate time spent
    and others time stuff 
    """
    
    time_start  = 0
    time_end    = 0
    
    def __init__(self):
        self.time_start = timeit.default_timer()
        log.info("Process started at %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                     
    def stop(self):
        self.time_end = timeit.default_timer()
        log.info("Process finished at %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        log.info("Time elapsed in this process is %s seconds" % str(self.time_end - self.time_start))

# Get the arguments
_args = Argumentos()

SILENT  = _args.params["SILENT"]
DIR     = [_args.params["DIR"]]


# Print Version
_ver = version(SILENT)

# Print arguments
if not SILENT:
    _args.PrintArgs()


# Start the process log
log.info("Target folder is: %s" % os.path.abspath(DIR[0]))
Time = Timer()

# Call the main function to rename files and folders 
_analyzer = Analise(DIR)

# Finish process
Time.stop()




