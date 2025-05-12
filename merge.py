from pypdf import PdfWriter
from direc import checkDirec
import os

"""

Script is intended to merge documents together.

Refer to https://pypdf.readthedocs.io/en/latest/user/migration-1-to-2.html for more information.

"""

# Enter PDFs to merge
pdfs = ['.pdf','.pdf']

# Directory setup
direc = "PDFs"
direc_merge = "Merged"
output_file = "merged"

checkDirec("./" + direc)
checkDirec("./" + direc_merge)

files = []
for file in os.listdir("./" + direc):
    files.append(file)

if not all(e in files for e in pdfs):
    raise Exception("Listed PDFs are not in directory: /" + direc)

merger = PdfWriter()

for pdf in pdfs:
    merger.append("./" + direc + "/" + pdf)
    
ver_id = 1
while os.path.isfile(f"{direc_merge}/{output_file}.pdf"):
    if "_" in output_file[-2:]:
        old_ver_id = int(output_file[-1:]) + 1
        output_file = f"{output_file[:len(output_file)-2]}_{old_ver_id}"
    else:
        output_file = f"{output_file}_{ver_id}"
    ver_id += 1
    

merger.write("./" + direc_merge + "/" + output_file + ".pdf")
merger.close()