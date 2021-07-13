#Project Name:Automatic Process Logger

#modules
import os
import time
import psutil
from sys import *
import schedule
i=0


#FunctionName:ProcessDisplay
#Author: ShubhamUpasani
#Parameters: FolderName
#ReturnValue:none

def ProcessDisplay(FolderName = "Shubham"):
    global i
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    file_Path = os.path.join(FolderName,"Shubham%s.log"%i)
    i=i+1
    file_Path = (file_Path.replace(" ","").replace(":",""))
 

    fd = open(file_Path,"w")
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n"% element)


#FunctionName:main
#Author: ShubhamUpasani
#Parameters: none
#ReturnValue:none

def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Scheule_Time Directory_Name")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : It is used to create log file of running processess")
        exit()
            
    schedule.every(int(argv[1])).minutes.do(ProcessDisplay)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
#As a starter
if __name__ == "__main__":
    main()
