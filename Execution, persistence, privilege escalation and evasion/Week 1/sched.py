import os, random
from datetime import datetime , timedelta 

if os.system("schtasks / query / tn securityScan"):
    os.system("schtasks / delete /f /tn securityScan")

print("I am doing Things")

filedir = os.path.join(os.getcwd(), "sched.py")

maxInterval = 1
interval = 1+(random.random() * (maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s" % (str(dt.hour).zfill(2), str(dt.minute).zfill(2))
d = "%s/%s/%s" % (dt.month, str(dt.day).zfill(2),dt.year)
os.system('schtasks / create / tn securityScan /tr' + filedir + ' /sconce /st ' + t + ' /sn ' + d)
input()