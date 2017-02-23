#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Maxlength_folder_eraser as eraser

# Get the arguments
_args = eraser.Argumentos()
SILENT  = _args.params["SILENT"]
DIR     = [_args.params["DIR"]]


# Print arguments
if not SILENT:
    _args.PrintArgs()


# Start the process log
log.info("Target folder is: %s" % os.path.abspath(DIR[0]))
Time = eraser.Timer()

# Call the main function to rename files and folders 
_analyzer = eraser.Analise(DIR)

# Finish process
Time.stop()
