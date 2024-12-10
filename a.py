import os
import datetime

logwriter = open("log.txt",'a+')
logreader = open("log.txt",'r+')

if not os.stat("log.txt").st_size:
    os.system("git init")
    repo = input("Enter the link of repo you wish to commit changes to..... ")
    with open("log.txt",'a+') as temp:
        temp.write(f"initialized script on {datetime.datetime.now()}\n")
        temp.write(f"{repo}\n")
    with open("changes.txt",'w') as changelogwriter:
        changelogwriter.write("0")
    os.system(f"git remote add origin {repo}")

changelogreader = open("changes.txt",'r+')
no_to_be_done = int(input("Enter no of commits: "))
dest_repo = logreader.readlines()[1]
no_of_changes_done_yet = int(changelogreader.readline())+1

for i in range(0,no_to_be_done):
    os.system(f"git remote add origin {dest_repo}")
    with open("log.txt","a+") as lgwriter:
        lgwriter.write(f"change no:{no_of_changes_done_yet} done on {datetime.datetime.now()}\n")
    no_of_changes_done_yet = no_of_changes_done_yet+1
    os.system("git add .")
    os.system(f"git commit -m \"change no {no_of_changes_done_yet}\"")
    os.system("git push origin master")

with open("changes.txt","w") as temp:
    temp.write(f"{no_of_changes_done_yet-1}")
    
logreader.close()
logwriter.close()
changelogreader.close()