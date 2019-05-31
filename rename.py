#Build command: "C:\Program Files (x86)\Python36-32\Scripts\pyinstaller" "D:\Dokumente\_Git\WowsRename\rename.py" --onefile --icon=wows.ico
import os
import sys
import polib
import glob
import time
cur_path = os.path.dirname(os.path.realpath(__file__))+"/"
#print("Working in:", cur_path)

path = ""

# check if file is where application is:
mo_files = glob.glob(cur_path+"*.mo")
for mo in mo_files:
    if("global.mo" in mo):
        path = mo #found the language file

input("WARNING - Make a copy of your .mo file first. Press Enter to continue.")

# the file is not located where the file is run from, ask user for location:
if(path == ""):
    print()
    print("You need to locate your language file in your install folder.")
    print("The path looks something like this:")
    print("C:/Program Files/WOWS/res/texts/en/LC_MESSAGES/global.mo")
    path = input("Enter the path of you .mo file: ")
    #check if entered path is valid:
    if(os.path.isfile(path)==False or "global.mo" not in path):
        print("ERROR: Unable to find global.mo")
        time.sleep(5)
        sys.exit()

# ask user: what should be replaced:
print()    
replaceA = input("Enter the name / string that should be replaced (e.g 'Yamato'): ")
replaceB = input("Enter the name / string that it should be replaced with (e.g 'Tomato'): ")

# load the language file
print("Working...")
if(path==""):
    mo_file = polib.mofile(mo_files[0])
else:
    mo_file = polib.mofile(path)

# check line by line and replace text if present:
replaced = 0
#print("-------------------------------------------------------------")
for line in mo_file:
    line.msgid_with_context = line.msgid #somehow needed to save the file (not sure what it does)
    if(replaceA in line.msgstr):
        replaced +=1
        line.msgstr = line.msgstr.replace(replaceA, replaceB)
        #print(line.msgstr)
        #print("-------------------------------------------------------------")

# Save the file, and diplay how often the text was replaced
print("Replaced "+str(replaced)+" entries")
if(replaced>0): #save only if something was replaced.
    print("Saving file...")
    mo_file.save(path)
print("Done!")