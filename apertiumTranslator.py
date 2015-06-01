"""
Offline translation for srt using Apertium
"""
from __future__ import print_function
from sys import platform as _platform
import sys

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
        exit()
  
    elif _platform == "win32":
        print("Sorry this feature is only for UNIX environment. If you are running\nwindows, then use Cygwin terminal for running this.")
        exit()
