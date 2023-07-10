# Table of Contents
<ui>
  <li>
     <a href="https://github.com/MedhatHassan/InfoSEC/tree/main/Intro%20to%20python%20for%20hacking/Module%203#malicious-usb-autorun">Malicious USB AutoRun</a>
  </li>
  <li>
  </li>
  <li>
  </li>
</ui>


# Malicious USB AutoRun

This is a Python script that creates a malicious executable and sets up an autorun file on a USB drive to automatically run the executable when the drive is inserted into a computer. The script uses the "PyInstaller" library to create the executable and the "shutil" and "os" libraries to move files and set file attributes.

## Requirements

- Python 3.x
- PyInstaller library
- shutil library
- os library

## Usage

To use this tool, simply run the script and provide the name of the Python script, the name of the executable, and the name of the icon file as input. The script will use PyInstaller to create the executable, move the files to a USB drive, and set up an autorun file.

```
python malicious_usb_autorun.py <python_script> <executable_name> <icon_file>
```

You can customize the autorun file by modifying the script. By default, the autorun file will run the executable and set the label of the USB drive to "My USB".

## Credits

This script was created by [Your Name] for the [Course Name] course at [University Name]. Feel free to use and modify this script for your own projects.

Here's a professional GitHub description for the Python script:

# SSH and Telnet Brute-Force Tool

This is a Python script that performs brute-force attacks on SSH and Telnet services by trying different username and password combinations. The script uses the "paramiko" and "telnetlib" libraries to establish a connection with the target host and attempt to login with the provided credentials.

## Requirements

- Python 3.x
- paramiko library
- telnetlib library

## Usage

To use this tool, simply run the script and provide the target host IP address, the path to the <a href=""></a> containing the username and password combinations, and the port number for SSH and Telnet services.

```
python ssh_telnet_bruteforce.py <host> <path_to_file> <ssh_port> <telnet_port>
```

The script will read the username and password combinations from the file and attempt to login to the SSH and Telnet services using each combination. If a successful login is found, the script will print a message indicating the successful login.

## Credits

This script was created by [Your Name] for the [Course Name] course at [University Name]. Feel free to use and modify this script for your own projects.
