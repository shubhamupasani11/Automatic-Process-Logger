#displays the infromation of running proceses..
from sys import *
import psutil

def ProcessDisplay():
    print("List of running processes:")
    
    Data=[]
    for proc in psutil.process_iter():
        value=proc.as_dict(attrs=['pid','name','username'])
        Data.append(value)
        
    return Data
def main():
   
    print("Script Title:"+argv[0])
    
    arr=ProcessDisplay()
    for element in arr:
        print(element)
    
if __name__=="__main__":
    main()