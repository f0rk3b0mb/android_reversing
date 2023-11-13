### code created by f0rk3b0mb
### 9 aug 2023
### rewitten 13 nov 2023
### https://github.com/f0rk3b0mb
### to automate apk reverse engineering for ctfs




#!/bin/bash


usage() {
    echo "Usage: $0 <APK_FILE> <DEX2JAR_PATH>"
    echo "Decompile Android APK for CTF"
    echo "Arguments:"
    echo "  <APK_FILE>     Path to the APK file you want to decompile."
    echo "  <DEX2JAR_PATH> Path to the dex2jar tool."
    exit 1
}


decomp() {
    apk_file=$1
    dex2jar_path=$2

    apk_file_path="$(pwd)/$apk_file"
    echo $apk_file_path
    extracted_dir="/tmp/_extracted"

    # Decompile using apktool
    apktool_cmd="apktool -f -r -s d $apk_file -o $extracted_dir"
    $apktool_cmd || { echo "Check apktool path or if it's installed"; exit 1; }

    file_list=()

    # Iterate through files in the extracted directory
    find "$extracted_dir" -type f -name "*.dex" | while read -r file_path; do
        dex2jar_cmd="$dex2jar_path --force $file_path"
        $dex2jar_cmd || { echo "Check dex2jar path or file path"; exit 1; }
        file_list+=("$file_path")
    done

    # Clean up and attempt full decompile
    apktool -f d "$apk_file" -o _extracted || { echo "Attempting full decomp failed"; exit 1; }

    # Print the decompiled files
    echo "Decompiled files: ${file_list[@]}"
}

# Example usage:
#decomp "../test.apk"  "dex-tools-2.1/d2j-dex2jar.sh "

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for correct number of arguments
    if [ "$#" -ne 2 ]; then
        usage
    fi

    decomp "$1" "$2"
fi
