# Importing packages
import csv;
import os;
from subprocess import call
import grp;
import time;
import re;

# Initializing Functions
def reverse(s): 
	if len(s) == 0: 
        	return s 
    	else: 
        	return reverse(s[1:]) + s[0] 




# Initializing Variables
ID = [];
LAST_NAME = [];
FIRST_NAME = [];
USER_NAME = [];
OFFICE = [];
PHONE = [];
DEPARTMENT = [];
GROUP = [];
i = 0;
count = -1;
idcount = 1005;
user_name = "";
firstname = "";
lastname = "";
rownumber = 1; # Start at row 1 because header is row 1 and first increment is row 2
department = "";
group = "";
shell = "";
Skip = False;

# Open the .csv file in binary mode
with open("Lab02_Users.csv", "rb") as file_name:
	# ignore the header and read below	
	reader = csv.DictReader(file_name)
        
        # Go through header, validate, and other actions
	for row in reader:
		Skip = False;
		rownumber += 1;
		ID.append(row['EmployeeID'])
		# LAST NAME 
			# IF EMPTY
		if (row['LastName'] == ''):
			# bad record last name
			print 'BAD RECORD: Bad LastName at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID'])
			Skip = True;
		else:
			LAST_NAME.append(row['LastName'])
		lastname = row['LastName'];

		# FIRST NAME 
			# IF EMPTY
		if (row['FirstName'] == ''):
			print 'BAD RECORD: Bad FirstName Record at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID']) 
			Skip = True;
		else:
			FIRST_NAME.append(row['FirstName'])
		firstname = row['FirstName']
		
		# USER NAME
			# NO UPPER CASE FOR USERNAME
		user_name = row['FirstName'][0:1].lower() + row['LastName'].lower();
			# SWAP THE SPECIAL CHARACTER
		user_name = user_name.replace("'", '')
		if user_name not in USER_NAME:
			USER_NAME.append(user_name);
		elif user_name in USER_NAME: 
			print "DUPLICATE USERNAME: " + user_name + " | EmployeeID: " + str(row['EmployeeID']) 
			USER_NAME.append(user_name + str(1));
			user_name = user_name + str(1);
		print user_name


		# OFFICE

		if (row['Office'].find('-') == -1):
			print 'BAD RECORD: Bad Office Record at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID'])
			Skip = True;
		else:
			OFFICE.append(row['Office'])	
		# PHONE
		PHONE.append(row['Phone']) 
		if (row['Phone'] == "unlisted"):
			PHONE.append(row['Phone'])
		elif (row['Phone'] == ""):
			Skip = True;
		elif (row['Phone'].find('-') == -1):
			print 'BAD RECORD: Bad Phone Record at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID'])
			Skip = True;
		else:
			PHONE.append(row['Phone'])  


# GROUP & CREATE GROUPS
		if (row['Group'] == ''):
			print 'BAD RECORD: Bad Group Record at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID'])
			Skip = True;
			group = "null";
			try:
				grp.getgrnam(group)
	 			# print(row['Group'] + " already exists");
			except KeyError:
				idcount += 1;
				# print(row['Group'] + " has been created");
				
				print "trying to add group"  

		else:
			GROUP.append(row['Group'])
			group = row['Group']
			try:
				group = row['Group']
				grp.getgrnam(group)
	 			# print(row['Group']+ " already exists - group");
			except KeyError:
				idcount += 1;
				# print(row['Group'] + " has been created - group");
				
				print "trying to add group"  




    		
#DEPARTMENT
	
		if (row['Department'] == ''):
			print 'BAD RECORD: Bad Department Record at row ' + str(rownumber) + " | EmployeeID: " + str(row['EmployeeID'])
			Skip = True;
			department = "null";
			try:
				grp.getgrnam(department)
	 			# print(row['Department'] + " already exists");
			except KeyError:
				idcount += 1;
				# print(row['Department'] + " has been created");

		else:
			DEPARTMENT.append(row['Department'])
			department = row['Department']
			try:
				department = row['Department']
				grp.getgrnam(department)
	 			# print(row['Department']+ " already exists - group");
			except KeyError:
				idcount += 1;
				# print(row['Department'] + " has been created - group");
				
				# print "trying to add group" 
		


# PASSWORD CHANGES AFTER LOGINS
		# password = 'test'
		password = (reverse(user_name))
		
		group = group.replace("-", "");
		if (group.isdigit()):
			group = "null"

		department = department.replace("-", "");
		if (department.isdigit()):
			department = "null"
		
		if Skip == False:
			os.system("mkdir /home/" + department);
			
			os.system("groupadd " + group);
		
			if department == "ceo":
				shell = "csh"
			else: 
				shell = "bash"
			os.system("useradd -m -d /home/" + department + "/" + user_name + " -g " + group + " -s /bin/" + shell + " -c \"" + firstname + " " + lastname + "\" " + user_name)
			os.system("usermod --password " + password + " " + user_name) 
		 	os.system("passwd --expire " + user_name);
			# os.system("echo " + password + " | passwd --stdin " + user_name + " -e");
		else: 
			print("BAD RECORD: " + row['EmployeeID']);

# Close the file so it doesn't "leak".		
file_name.close()
