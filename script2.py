
from sys import *

def Function(value):
    print("Inside the function paramter: "+value)
def main():

   if (len(argv)!=2):
        print("Insufficient argumets to the Srcipt")
        exit()
        
    if (argv[1]=="-u") or (argv[1]=="U"):
        print("Use the Script as Name.py Parameters")
        exit()
    
    if(argv[1]=="-h") or (argv[1]=="H"):
        print("This is demo automation script")
        exit()

    Function(argv[1])
    
if __name__=="__main__":
    main()