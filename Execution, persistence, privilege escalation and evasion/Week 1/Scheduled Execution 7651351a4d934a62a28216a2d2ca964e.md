# Scheduled Execution

All operating systems enable task scheduling 
•      Allow system to perform routine tasks
•      Makes system administration easier

An attacker can also take advantage of task
scheduling

• Scheduled task can download or drop
malware
• Fileless malware can be written into a
scheduled task

![Untitled](Scheduled%20Execution%207651351a4d934a62a28216a2d2ca964e/Untitled.png)

# schtasks command

The `schtasks` command is a command-line tool in **Windows** that is used to manage scheduled tasks. It allows you to create, modify, delete, run, and query scheduled tasks on the local or remote computer.

The basic syntax of the `schtasks` command is:

```
schtasks /<operation> [options]

```

Where `<operation>` is the desired operation to perform (e.g., `create`, `delete`, `query`, `run`) and `[options]` are the command-line options specific to the operation.

Here are some common command-line options for the `schtasks` command:

- `/tn` - Specifies the name of the task.
- `/tr` - Specifies the path to the program or script to run.
- `/st` - Specifies the start time of the task in HH:mm format.
- `/sn` - Specifies the start date of the task in MM/DD/YYYY format.
- `/sc` - Specifies the schedule type (e.g., `once`, `daily`, `weekly`, `monthly`).
- `/mo` - Specifies the modifier for the schedule type (e.g., `1` for every day, `2` for every other day).
- `/s` - Specifies the name or IP address of the remote computer to manage.
- `/u` - Specifies the user account to use for the task.
- `/p` - Specifies the password for the user account.

For example, to create a scheduled task named "MyTask" that runs the program "C:\Program Files\MyProgram\run.bat" every day at 9:00 AM, you would use the following command:

```
schtasks /create /tn MyTask /tr "C:\\Program Files\\MyProgram\\run.bat" /sc daily /st 09:00

```

Note that some options may require additional parameters, and the syntax may vary depending on your version of Windows. You can use the `schtasks /?` command to display the help documentation for the `schtasks` command.

```python
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
```