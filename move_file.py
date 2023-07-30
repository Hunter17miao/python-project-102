import os 
import shutil
from_dir = "/Users/huntermiao/Downloads"
to_dir = " /Users/huntermiao/Desktop/Project 102"
list_of_files= os. listdir(from_dir)
print (list_of_files)
for file_name in list_of_files:
    name, ext= os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext=='':
        continue
if ext in ['.txt','.doc','.docx','.pdf']:
    path1= from_dir+ "/"+ file_name 
    path2= to_dir+ "/"+ "img"
    path3= to_dir+ "/"+ "img"+ "/"+ file_name 
    if os.path.exists (path2):
        shutil.move (path1, path3) 
    else:
        os.makedirs (path2)
        shutil. move (path1, path3)