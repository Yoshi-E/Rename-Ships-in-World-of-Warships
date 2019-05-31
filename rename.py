#Build command: "C:\Program Files (x86)\Python36-32\Scripts\pyinstaller" "D:\Dokumente\_Git\WowsRename\rename.py" --onefile --icon=wows.ico
import os
import sys
import polib
import glob

cur_path = os.path.dirname(os.path.realpath(__file__))+"/"
#print("Working in:", cur_path)

path = ""
mo_files = glob.glob(cur_path+"*.mo")
for mo in mo_files:
    if("global.mo" in mo):
        path = mo

input("WARNING - Make a copy of your .mo file first. Press Enter to continue.")

if(path == ""):
    print()
    print("You need to locate your language file in your install folder.")
    print("The path looks something like this:")
    print("C:/Program Files/WOWS/res/texts/en/LC_MESSAGES/global.mo")
    path = input("Enter the path of you .mo file: ")

print()    
replaceA = input("Enter the name / string that should be replaced (e.g 'Yamato'): ")
replaceB = input("Enter the name / string that it should be replaced with (e.g 'Tomato'): ")

print("Working...")
if(path==""):
    mo_file = polib.mofile(mo_files[0])
else:
    mo_file = polib.mofile(path)
    
replaced = 0
print("-------------------------------------------------------------")
for line in mo_file:
    line.msgid_with_context = line.msgid #somehow needed to save the file (not sure what it does)
    if(replaceA in line.msgstr):
        replaced +=1
        line.msgstr = line.msgstr.replace(replaceA, replaceB)
        print(line.msgstr)
        print("-------------------------------------------------------------")
    
print("Replaced "+str(replaced)+" entries")
if(replaced>0):
    print("Saving file...")
    mo_file.save(path)
print("Done!")