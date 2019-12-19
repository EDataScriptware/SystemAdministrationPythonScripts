# Necessary for this program to run
import socket
import time
import os


# Printing the beginning of the test
print("*** Beginning Test ***");

# Count down to the test with a 1.25 seconds delay
# Gives the user more than enough time to stop the process.
for x in range(5):
    print("\t" + str(5 - x));
    time.sleep(1.25);

# Grabbing the hostname
hostname = socket.gethostname();

#Grabbing and Testing the IP address of this machine (localhost)
try:   
    ipAddress = socket.gethostbyname(hostname);
    print("\nYour default gateway is " + ipAddress)
    result = os.system("ping " + ipAddress);
    print("\n\n")
    print("Connection to Default Gateway is SUCCESSFUL");
    defaultGateWayBool = True;
except:
    print("Connection to Default Gateway has FAILED");
    defaultGateWayBool = False;
print("\n");

# This is TRUSTED address we want to ping to
targetAddress = "Google.com";
result = os.system("ping " + targetAddress);
print("\n\n")
if result == 0:
    print("Remote Connection SUCCEEDED!");
    targetAddressBool = True;
else:
    print("Remote Connection FAILED!");
    targetAddressBool = False;

print("\n");
try:
    IP = socket.gethostbyname(targetAddress);
    print("DNS Resolution SUCEEDED!");
    dnsResolutionBool = True;
except:    
    print("DNS Resolution FAILED!");
    dnsResolutionBool = False;

# Dividing the descriptive from simplified
print("\n\nSummarized Results:\n")





# Summarizing the results
print("Your default gateway is " + ipAddress + ".");

if defaultGateWayBool == True:
    print("Connection to Default Gateway is SUCCESSFUL!");
else:
    print("Connection to Default Gateway has FAILED!");

if targetAddressBool == True:
    print("Remote Connection SUCCEEDED!");
else:
    print("Remote Connection FAILED!");
if dnsResolutionBool == True:
    print("DNS Resolution SUCCEEDED!");
else: 
    print("DNS Resolution FAILED!");

print("*** Test Complete ***")
