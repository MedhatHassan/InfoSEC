# InfoSEC Course Notes: Execution, Persistence, Privilege Escalation and Evasion - Week 1
This repository contains my notes for Week 1 of the InfoSEC course on Coursera. The course covers python topics related to cybersecurity, including execution, persistence, privilege escalation, and evasion.
### Contents

The `Execution, persistence, privilege escalation and evasion/Week 2` directory contains the following files:
- `README.md`: this file, providing an overview of the contents of the directory
- `notes.md`: my personal notes on the topics covered in Week 2

### Code Examples

In addition to the lecture slides and my notes, the course also includes several code examples. The following is a brief description of each code file:
- `MaliciousLinks.py`: a Python script creates a simple HTTP server that redirects users to Google <i>(Or other website)</i> after logging their username and password from the query string.
- `sched.py`: a Python script creates a scheduled task to run a security scan at a random interval.

## Malicious Links

This Python script demonstrates a phishing attack by creating a malicious link that looks like a legitimate website, but actually sends the user's credentials to the attacker's server. 

### Requirements
- Python 3.x

## Installation

```
git clone https://github.com/MedhatHassan/InfoSEC 
cd InfoSEC/Execution\%2C\ persistence\%2C\ privilege\ escalation\ and\ evasion/Week\ 1
```

### Usage
1. Open the `MaliciousLinks.py` file in a code editor or IDE.
2. Change the `ip_address` and `port` variables to match the IP address and port of the attacker's server.
3. Run the script by executing `python MaliciousLinks.py`.
4. Copy the generated link and send it to the victim.
5. When the victim clicks on the link and enters their credentials, the script will print their username and password to the console.

Note: This script is for educational purposes only and should not be used for malicious purposes.

Here's a possible README.md file for that GitHub repo:

# Process Scheduler 

This script provides a simple process scheduler functionality.

## Requirements

- Python 3

## Installation

```
git clone https://github.com/MedhatHassan/InfoSEC 
cd InfoSEC/Execution\%2C\ persistence\%2C\ privilege\ escalation\ and\ evasion/Week\ 1
```

## Usage

```
python sched.py 
```

This will launch the script and prompt you for commands. You can schedule processes to run at a specific time or interval using:

```
 schedule <process> <time>
```

For example:

```
schedule uptime every 5m
```

Will run the `uptime` command every 5 minutes.

You can list currently scheduled processes using:

```
list 
```

And remove a scheduled process using:

``` 
remove <process name>
```

Enjoy! Let me know if you have any other questions.
