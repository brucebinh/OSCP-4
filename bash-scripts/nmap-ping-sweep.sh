#!/bin/bash

# PING SWEEP TARGET RANGE AND PUT IN .TXT
nmap -v -sn 10.11.1.1-254 -oG ping-sweep.txt

# GREP OUT ALL THE DOWN HOSTS & ADD UP HOSTS TO NEW FILE
grep Up ping-sweep.txt | cut -d " " -f 2 > up-hosts.txt

