import os
import zipfile
import subprocess

def decomp(zip_file,extracted_dirname,dex2jar_path):
    zip_file_path = os.getcwd()+"/"+zip_file
    extracted_dir = os.getcwd()+"/"+extracted_dirname
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all contents to the specified directory
        zip_ref.extractall(extracted_dir)
    file_list = []
    
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            if file.endswith('.dex'):
                file_path = os.path.join(root, file)
                cmd=f"{dex2jar_path} {file_path}"
                try:
                    p=subprocess.run(cmd,shell=True,stderr=subprocess.PIPE)
                except :
                    return "check dex2jar path or file path"
                file_list.append(file_path)
    return f'decompiled file {" | ".join(file_list)}'
    



    


