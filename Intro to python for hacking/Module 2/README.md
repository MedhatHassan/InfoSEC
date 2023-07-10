# Subdomain Enumeration Tool

This is a Python script that performs subdomain enumeration by brute-forcing subdomains using a <a href="https://github.com/MedhatHassan/InfoSEC/blob/main/Intro%20to%20python%20for%20hacking/Module%202/sub">wordlist</a> and performing DNS requests on each subdomain. The script uses the "dns" and "socket" libraries to perform DNS requests and reverse DNS lookups, respectively.

## Requirements

- Python 3.x
- dns library
- socket library

## Usage

To use this tool, simply run the script and provide the target domain name and wordlist as input. The script will perform DNS requests on each subdomain and print the results to the console.

```
python subdomain_enumeration.py <domain> <wordlist>
```

You can also specify whether to include numbers in the subdomain names by setting the "nums" parameter to True or False.

## Credits

Feel free to use and modify this script for your own projects.
