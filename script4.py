#take file name from user and write that data in that file..
from sys import *
import psutil
import os


def ProcessDisplay(FolderName="Marvellous"):
    
    Data=[]
   
   #jar given folder nasel tr navin foldeer tayar hoill(os madhe path sub module exists function->mkdir->to create folder)
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    else:
        print("Destination directory is already present")
        exit()
    return
def main():
   #script title
    print("Script Title:"+argv[0])
    
    if(len(argv)!=2):
        print("Insufficient arguments")
        exit()
        
    if(argv[1]=="-u")or(argv[1]=="U"):
        print("Usage:Application_name Directory_name")
        exit()
        
    if(argv[1]=="-h")or(argv[1]=="H"):
        print("Help:It is use to create log file of running processes")
        exit()
        
    ProcessDisplay(argv[1])
    
    
if __name__=="__main__":
    main()