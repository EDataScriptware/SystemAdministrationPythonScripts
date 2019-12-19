# Edward Riley

# import
import os
import getpass
import subprocess
import sys
import os.path
from os import path

shortcut = "";
origin = "";

# Getting username
user_name = os.path.expanduser('~')
os.system("clear");

# Current directory
print ("Current directory: ") + os.getcwd()

# Checking directory
if os.getcwd() != user_name + "/Desktop":

	print str(user_name + "/Desktop")
	sys.exit("Warning: Incorrect Directory!");
else:
	print("Notification: Correct Directory!")


print ("\n('EXIT' to exit the program)");
print ("(Enter a relative file or absolute file)\n");
shortcut = raw_input("Shortcut File Name: ");

if shortcut == 'EXIT':
	sys.exit("Exiting the program")

# Create a Symbolic Link
origin = raw_input("Origin File Name: ");

# This checks to see if the file exists or not. 

# IF FALSE | create a file at that path
if path.exists(origin) == False:
	print("File or Directory does not exist!");
	os.system("touch " + str(origin));
	print("Creating a file at " + str(origin));
else:
	print("File or Directory exists!");

# Created Symbolic Link
os.system("ln -s " + str(origin) + " " + str(shortcut));

# Finding number of symbolic link
number = subprocess.Popen(["find . -type l -ls | wc -l"], stdout=subprocess.PIPE, shell=True)
(result, errorMessage) = number.communicate()
number = result;

# Summary Report
report = subprocess.Popen(["find . -type l -ls"], stdout=subprocess.PIPE, shell=True)
(result, errorMessage) = report.communicate()
report = result;

# Printing number
print ("Quantity of Symbolic Link" + str(number)) 

# Printing summary report
print ("Symbolic Links Summary Report: " + "\n" + str(report)) 
