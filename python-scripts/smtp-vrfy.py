#!/usr/bin/python
import socket
import sys

#file = open ('username-list.txt')
#usernames = file.read()
#file.close()

#print usernames
#if len(sys.argv) != 2:
#	print "Usage: vrfy.py <username>"
#	sys.exit(0)

# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect=s.connect(('10.11.1.22',25))

# Receive the banner
banner=s.recv(1024)
print banner

# VRFY a user
#s.send('VRFY ' + sys.argv[1] + '\r\n')
#result=s.recv(1024)
#print result

with open('usernames.txt') as file:
	for username in file:
		s.send('VRFY ' + username)
		result=s.recv(1024)
		print result

# Close the socket & FILE
s.close()
file.close()
