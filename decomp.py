### code created by f0rk3b0mb
### 9 aug 2023
### https://github.com/f0rk3b0mb
### to automate apk reverse engineering for ctf

import os
#import zipfile
import subprocess

def decomp(apk_file,extracted_dirname,dex2jar_path):
    apk_file_path = os.getcwd()+"/"+apk_file
    extracted_dir = os.getcwd()+"/"+extracted_dirname
    # Open the zip file
    #with zipfile.ZipFile(apk_file_path, 'r') as zip_ref:
    # Extract all contents to the specified directory
    #    zip_ref.extractall(extracted_dir)

    # decompile using apktool

    cmd=f"apktool -r -s d {apk_file} -o {extracted_dirname} 1>/dev/null"
    try:
        p=subprocess.run(cmd,shell=True)
    except :
        return "check apktool path or if its installed"


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
    
    cmd=f"rm -r {extracted_dirname} && apktool d {apk_file} -o {extracted_dirname}"
    try:
        p=subprocess.run(cmd,shell=True)
    except :
        return "attempting full decomp failed"
    

    return f'decompiled file {" | ".join(file_list)}'
    



    


