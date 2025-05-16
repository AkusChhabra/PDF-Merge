from pypdf import PdfWriter
from .direc import checkDirec
import os
from pathlib import Path

"""

Script is intended to merge documents together.

Refer to https://pypdf.readthedocs.io/en/latest/user/migration-1-to-2.html for more information.

"""

def mergeFiles(pdfs):
    
    output_file = "merged"
    direc_merge = str(Path.home() / "Downloads")

    print("\n\ndirec_merge: ", direc_merge)

    direcExist = checkDirec(direc_merge)


    if not direcExist:
        raise Exception("Could not find Downloads folder.")

    merger = PdfWriter()

    for pdf in pdfs:
        merger.append(pdf)
        
    ver_id = 1
    while os.path.isfile(f"{direc_merge}/{output_file}.pdf"):
        if "_" in output_file[-2:]:
            old_ver_id = int(output_file[-1:]) + 1
            output_file = f"{output_file[:len(output_file)-2]}_{old_ver_id}"
        else:
            output_file = f"{output_file}_{ver_id}"
        ver_id += 1  

    merger.write(direc_merge + "/" + output_file + ".pdf")
    merger.close()
    