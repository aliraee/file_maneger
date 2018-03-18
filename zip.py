import zipfile



def zipping_file(file_path,zip_path):

    
    zip_file = zipfile.ZipFile(r'zip_path','w')
    zip_file.write(r'file_path')
    zip_file.close()

#has denied permission yet
    
