#! /usr/bin/env python3
#SHEBANG
try:
    import socket
except:
    print("Please install a socket module - you can do this by running 'pip install socket' in the command prompt then run the code again")
try:    
    from loguru import logger
except:
    print("Please install a loguru module - you can do this by running 'pip install loguru' in the command prompt then run the code again")
try:
    from time import sleep
except:
    print("Please install a time module - you can do this by running 'pip install time' in the command prompt then run the code again")    
#import modules with methods in this space

#define a function(method) here
def nslook():
    global web
    #declare a web as a variable to get user input
    web = input("Please enter the website:")
    #from module socket using a method gethostbyname_ex
    addr1 = socket.gethostbyname_ex(web)
    print(f"IP for {web}:")
    print(addr1[2])
    f = str(addr1[2])
    with open('ns.txt','r') as o:
        d = o.readlines() 
    with open('ns.txt','w') as n:
        n.write(f)
    with open('ns.txt','r') as o:
        l = o.readlines()     
    if d == l:
        print("No Changes in website ip");
    else:
        print("IP is changed. Changing the ACL in firewall")


   
      
def main():
#write your main function here 
       try:
           nslook()
           while True:               
               logger.info("Press 'ctrl+c' to exit");sleep(3);
                     
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       main() 
#coded by Dinesh_Kumar_Palanivelu #Save file as lookupacl.py in your preferred location.
