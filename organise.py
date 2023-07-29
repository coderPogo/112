import os
import shutil

fromdir = "/Users/pogo/Downloads"

listdir = os.listdir(fromdir)

todir = "/Users/pogo/Downloads"
print(listdir)

for i in listdir:
    name,extension = os.path.splitext(i)
    #print(name)
    #print(extension)

    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx",".pdf"]:
        path1 = fromdir + "/" + i
        path2 = todir + "/" + "documents"
        path3 = todir + "/" + "documents" + "/" + i

        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("Moving "+ i + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving "+ i + "...")
            shutil.move(path1,path3)