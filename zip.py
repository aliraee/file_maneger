import zipfile
import os
def zipping_file(path,file_name,zip_name):
    #os.system('cd ~')
    os.system('cd ~%s'%path)
    os.system('zip %s'%zip_name +' %s'%file_name)


#has denied permission yet
    
#zipping_file('/Desktop','Cryptography\ and\ Network\ Security\ 5th\ ed\ -\ William\ Stallings.pdf','aliraee')