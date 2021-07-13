#project...
from sys import *


def main():
   
    print("Srcipt Title:"+argv[0])
    
    #kamit kami 1. argument otherwise error
    if ((len(argv)!=2) or(len(argv)>2)):
        print("Insufficient argumets to the Srcipt")
        exit()
    if (argv[1]=="-u") or (argv[1]=="U"):  #u and H are just flag to indicate for the first time user how to use script..(usage/help->kay karnar aahe scrit)
        print("Use the Script as Name.py Parameters")
        exit()
    
    if(argv[1]=="-h") or (argv[1]=="H"):
        print("This is demo automation script")
        exit()
    
if __name__=="__main__":
    main()