from geoip import geolite2 as ip;
import sys;
import csv;

# Intialzied Variables
ipAddressArrayUnique = [];
ipAddressArrayCount = [];
count = 1;
countryName = "";

# Getting the file_name from user argument
file_name = sys.argv[1];


try:
	# Opens up a file name and reads each file name
	with open(file_name) as fp:
		for line in fp:
			try:

				# Cleaning off anything before from
				preline = line[line.index("from") + len("from "):];
				
				# Remove white space
				preline = preline.strip();
				
				# Place each together text into an array
				preline = preline.split();
 
				# Replace that pesky ":" with nothing
				ipAddress = preline[0].replace(":", "");
				
				# adds unique ip address
				if ipAddress not in ipAddressArrayUnique:
					ipAddressArrayUnique.append(ipAddress);
					
				ipAddressArrayCount.append(ipAddress);
				
				
				

				
				
			except:
				counter = 0; # - end of the file - nothing happens
		# Begin writing the csv 
		c = csv.writer(open("status_report.csv", "wb"))
		
		# Writes the header of the csv
		c.writerow(["Count", "IP", "Location"]);
		print "\nCount,IP,Location";
		try:
			while True: 
				# Counting up
				count = count + 1;
				
				# Current IP address to use to count
				ipAddress = str(ipAddressArrayUnique[count])
				
				# Checking the geolite database for the specific ip address
				match = ip.lookup(ipAddress)
				
				# Uses the unique ip array to count the overall ip array in a count number, then the name of the IP address, then the country
				print str(ipAddressArrayCount.count(ipAddressArrayUnique[count])) + "," + str(ipAddressArrayUnique[count]) + "," + match.country;
				
				# Export to csv
				c.writerow([str(ipAddressArrayCount.count(ipAddressArrayUnique[count])), str(ipAddressArrayUnique[count]), match.country]);
		except: 
			counter = 0; # - Do nothing - finished with unique count

		
	
				
# end file not found main try-catch except - exits the program
except Exception as e: 
	print "\nError: File not found. Exitting the program.\n"
	sys.exit(1);
	



