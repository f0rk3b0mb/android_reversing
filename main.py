### code created by f0rk3b0mb
### 9 aug 2023
### https://github.com/f0rk3b0mb/amatuerCTF_Censorship
### to automate apk reverse engineering for ctfs

import sys
from decomp import decomp


def main():
    print("Welcome to apk decomp")
    zip_file_path=sys.argv[1]
    extracted_dir=sys.argv[2]
    dex2jar_path=sys.argv[3]
    print("Working...")
    x=decomp(zip_file_path,extracted_dir,dex2jar_path)
    print(x)




if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()
        print("""view the files using jd-gui
              
              dex2jar https://github.com/pxb1988/dex2jar/releases/tag/v2.1
              
              jd-gui http://java-decompiler.github.io/""")
    else:
        print("""wrong syntax , use [python3 main.py zip_file_path extraction_dir dex2jar_path]
              
              You can then view the files using jd-gui
              
              dex2jar https://github.com/pxb1988/dex2jar/releases/tag/v2.1
              
              jd-gui http://java-decompiler.github.io/""")