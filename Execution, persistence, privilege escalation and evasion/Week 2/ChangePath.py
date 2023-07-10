import os, winreg
def readPathVa1ue (reghive , regpath) :
    reg = winreg.ConnectRegistry(None , reghive)
    key = winreg.OpenKey (reg , winreg.KEY_READ)
    index = 0
    while True:
        val  = winreg.EnumVa1ue (key, index)
        if val[0] == "Path":
            return val[1]
        index +=1

def editPathVa1ue (reghive , regpath, targetdir) :
    path = readPathVa1ue(reghive, regpath)
    newpath = targetdir + ";" + path
    reg = winreg.ConnectRegistry(None, regpath)
    key = winreg.OpenKey(reg , regpath , access = winreg.KEY_SET_VALUE)
    winreg.setValueEx(key, "path", 0 , winreg.REG_EXPAND_SZ, newpath)

# Modify user path
reghive = winreg.HKEY_CURRENT_USER
regpath = "Environment"
targetdir = os.getcwd()

editPathVa1ue(reghive,regpath,targetdir)

# Modify system path NEED Admin level on windows
# reghive = winreg.HKEY_LOCAL_MACHINE
# regpath = "SYSTEM\CurrentContrlSet\Control\Session Manger\Environment"
# targetdir = os.getcwd()
# editPathVa1ue(reghive,regpath,targetdir)