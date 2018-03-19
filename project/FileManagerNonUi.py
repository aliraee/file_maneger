"""
    The functions that defined in class folders is just for folders
    The functions that define in class files is just for files not folders
    and the functions that define publicly is for both files and folders
"""

import os
import win32api
import shutil


def show(path):
    """
    :return: a list that contains sub file and sub folder names !
             if return None it means that directory is fake !
    """
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return None
    # Test result: :)


def back(path):
    dirs = path.split("\\")
    path = ""
    dirs = dirs[:-1]
    for i in dirs:
        path += i + "\\"
    if os.path.exists(path):
        return path
    else:
        return None
    # Test result: :)

class files:
    def __init__(self, dir):
        self.dir = dir
    def open(self):
        os.startfile(self.dir)
    def copy(self, to):
        try:
            shutil.copy2(self.dir, to)
        except PermissionError:
            print(" Can not access to %s" %to)
    def cut(self, to):
        shutil.move(self.dir, to)
    def rename(self, newName):
        dirs = self.dir.split("\\")
        newDir = ""
        dirs = dirs[:-1]
        for i in dirs:
            newDir += i + "\\"
        newDir += newName
        if os.path.exists(newDir):
            return None
        else:
            os.rename(self.dir, newDir)
    # Test result: :)

class folders:
    def __init__(self, dir):
        self.dir = dir
    def rename(self, newName):
        dirs = self.dir.split("\\")
        newPath = ""
        dirs = dirs[:-1]
        for i in dirs:
            newPath += i + "\\"
        newPath += newName
        if os.path.exists(newPath):
            return None
        else:
            os.rename(self.dir, newPath)
    def new(self, name):
        self.dir += "\\"+name
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        else:
            return None
    # Test result: :)
        
#____________________________________________________________________________________
# Test:


#Dir = "M:\\My University\\Advanced Programming 2"
#backDir = back(Dir)
#print(Dir, show(Dir), backDir, show(backDir), sep = "\n")
#folder = folders(Dir)
#folder.rename("test")
#folder.new("new")

#file = files("M:\\My University\\Math 2\\Nadjafikhah - Calculus II - Persian.pdf")
#file.open()
#file.copy("C:\\Users\\Ali Ayati\\Documents")
#file.cut("M:\\My Downloads")
#file.rename("test.pdf")

