import sys
import os
import uuid

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
    DAT         = "20/01/2017"
    COPYRIGHT   = "Desenvolvido por Fabricio Roberto Reinert"
    
    def __init__(self, silent):
        o = output(silent)
        o.out("-----------------------------------------")
        o.out("Versão:         %f" % self.VERS)
        o.out("Ultima revisão: %s" % self.DAT)
        o.out(self.COPYRIGHT)
        o.out("-----------------------------------------")
        

class Argumentos():
    """
    Manipulação dos argumentos iniciais
    """
    params  = dict()
    
    # handle the arguments and insert them into the dictionary "params"
    def __init__(self):
        if len(sys.argv) == 1:
            sys.exit("\n\n        Limpeza de Backups\n\n    -dir : Especifíca um diretório\n    -silent : Modo silencioso\n\n")
        
        for p in sys.argv:
            
            if p == "-dir":
                dir_index = sys.argv.index("-dir",)
                if dir_index+1 > len(sys.argv)-1:
                    sys.exit("\n>> ERRO: Diretório não especificado")
                else:
                    dir_index = dir_index+1
                    self.params["DIR"] = sys.argv[dir_index]
                    if not os.path.isdir(self.params["DIR"]):
                        sys.exit("\n>> ERRO: Diretório '%s' não existe" % self.params["DIR"])
            
            if p == "-silent":
                self.params["SILENT"] = True
                
        if not "SILENT" in self.params:
            self.params["SILENT"] = False
    
    # Print Arguments
    def PrintArgs(self): 
        print("\n\n-----------\nArgumentos:\n-----------")
        for k, v in self.params.items():
            print("+ %s: %s" % (k,v))
            
def Analise(folders, silent=True):
    
    # Dirs receives subfolders
    Dirs    = []
    o       = output(silent)    
    
    # walk trough the folders on the "folders" param
    for folder in folders:
        
        # walk truogh the subfolders into the iterated  "folder" var
        for d in os.listdir(folder):
            
            # rename them
            
            UID = uuid.uuid4()
            UID = UID.hex [:8]
            
            os.rename(os.path.join(folder,d), os.path.join(folder, UID))
            
            o.out('alterado: ' + os.path.join(folder,d) + ' para ' + os.path.join(folder, UID))
            
            
        # Read again the dirs - now it's already renamed
        for d in os.listdir(folder):
                
            # add the folders into a list
            path = os.path.join(folder,d)
            
            if os.path.isdir(path):
                
                Dirs.append(os.path.join(folder,d))
            
            
        # Recursively calls the function passing the list "Dirs" as a new parameter
        Analise(Dirs, silent)   
        
        
        

# Get the arguments
_args = Argumentos()

SILENT  = _args.params["SILENT"]
DIR     = [_args.params["DIR"]]


# Print Version
_ver = version(SILENT)

# Print arguments
if not SILENT:
    _args.PrintArgs()

# Call the main function to rename files and folders 
_analyzer = Analise(DIR, SILENT)




