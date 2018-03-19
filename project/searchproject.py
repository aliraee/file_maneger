#search files
import os
def findFile(path,fileName):
    for root,dirs,filenames in os.walk(path):
        if fileName in filenames:
            return os.path.join(root,fileName)
output=findFile(os.environ['HOME'],'ali.txt')        
