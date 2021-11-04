#! /usr/bin/env python3
#SHEBANG
#copyright (c) Dinesh_Kumar_Palanivelu #Save file as <title>.py in your preferred location. Then start typing
import socket
from loguru import logger
from time import sleep
#import modules with methods in this space


def nslook():    
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
        print("No Changes in facebook ip");
    else:
        print("IP is changed. Changing the ACL in firewall")


   
      
def main():
#write your main function here 
       try:
           global web
           web = input("Please enter the website:")
           while True:
               nslook()
               logger.info("Press 'ctrl+c' to exit");sleep(3);
                     
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       main() 
