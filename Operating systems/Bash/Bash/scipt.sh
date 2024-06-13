#!/bin/bash

# to get the contents of the /etc/passwd file 
cat /etc/passwd > report.txt

# to get paths to all world writable files 
find / -perm -0002 -type f -print >> report.txt




