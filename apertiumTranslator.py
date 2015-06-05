"""
Offline translation for srt using Apertium
"""
from __future__ import print_function
from sys import platform as _platform
from subprocess import Popen,PIPE,STDOUT
import sys

def translate(sentence,langPair):
    try:
        translated = Popen('echo "'+sentence+'" | '+'apertium '+'en-ca',shell=True,stdout=PIPE,stderr=STDOUT).communicate()[0].decode('utf-8')
    except:
        raise RuntimeError("Apertium or its module for the given language pair is not installed properly.\n Try running 'echo <sentence> | apertium langPair.\n If this doesn't give any Error, then try running the program again.\n Else install Apertium and the required language pair.'")
    print("sentence:",sentence,'\n',translated)
    return translated

def translateSRT(filePath,langPair):
    fileContent = open(filePath,"r").read()
    fileLines = fileContent.splitlines()
    outputFile=open(filePath[:-4]+"_"+langPair+'.srt',"w")
    for i in fileLines:
        if not(i.startswith("<") or (len(i)>0 and i[0].isdigit())):
            print((translate(i,langPair).encode('utf-8')),file=outputFile)
        else:
            print(i,file=outputFile)
    return 1



if __name__ == "__main__": 
    if _platform in ["linux","linux2","darwin","cygwin"]:
        print("Running Platform: " + ( _platform if _platform != "darwin" else "Mac OS X").capitalize())
        print("For offline translation, you will have to install Apertium.\nInstall it according to your OS from this link http://wiki.apertium.org/wiki/Installation.")
        if (len(sys.argv)) == 1:
            print("Give the srt file for translation.")
        elif (len(sys.argv)) == 2:
            if sys.argv[1] == "all":
                print("'eo-es', 'eu-es', 'pt-ca', 'es-ca', 'fr-ca', 'pt-gl', 'en-ca', 'es-gl', 'fr-es', 'en-es', 'es-pt', 'oc-ca', 'eo-ca', 'es-ro', 'oc-es'")
            else:
                print("Give the language pair for translation. Argument 'all' to get all language pairs.")
        elif (len(sys.argv)) > 2:    
            translateSRT(sys.argv[1],sys.argv[2])
       
  
    elif _platform == "win32":
        print("Sorry this feature is only for UNIX environment. If you are running\nwindows, then use Cygwin terminal for running this.")
    exit()



