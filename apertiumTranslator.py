from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
    #linux
elif _platform == "darwin":
    #Mac OS X
elif _platform == "cygwin":
    #Windows/cygwin
elif _platform == "win32":
    #windows
