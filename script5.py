import os
import time
import psutil
from sys import *

def ProcessDisplay():
    
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    else:
        print("Destination directory is already present")
        exit()
        
    File_Path = os.path.join(FolderName,"Marvellous.txt")
    print("File path is:",File_Path)
    fd = open(File_Path,"w")
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n"%element)

def main():
   
    print("Script Title:"+argv[0])
    if (len(argv)!=2):
        print("Insufficient argumets to the Srcipt")
        exit()
        
    if (argv[1]=="-u") or (argv[1]=="U"):
        print("Use the Script as Name.py Parameters")
        exit()
    
    if(argv[1]=="-h") or (argv[1]=="H"):
        print("This is demo automation script")
        exit()

    ProcessDisplay(argv[1])

       
if __name__=="__main__":
    main()