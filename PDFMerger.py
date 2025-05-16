import os
import sys
import tkinter as tk
from tkinter import filedialog, Frame, Scrollbar, Menu, PhotoImage
from tkinter import ttk
from src.checks import instructionsDialogBox, noFileRemoveDialogBox, noSelectedRowDialogBox, noFileMergeDialogBox, singleFileDialogBox, mergeSuccessDialogBox
from src.move import move
from src.merge import mergeFiles
from idlelib.tooltip import Hovertip

#def resource_path(relative_path):
#    try:
#        base_path = sys._MEIPASS
#        print(base_path)
#    except Exception:
#        base_path = os.path.abspath(".")
#    return os.path.join(base_path, relative_path)

def uploadAction(event=None):
    file_path = list(filedialog.askopenfilenames(title="Select files", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]))
    for i in range(len(file_path)):
        file_name = extractFileName(file_path[i])
        addFile(file_name, file_path[i], i)

def addFile(file, file_path, ind):
    tree.insert("", tk.END, text=ind, values=(file,file_path,))

def removeFile():
    files = readTreeData()
    if not files:
        noFileRemoveDialogBox()
        return
    if tree.selection():
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
    else:
        noSelectedRowDialogBox()

def removeAllFiles():
    files = readTreeData()
    if not files:
        noFileRemoveDialogBox()
        return
    for row in tree.get_children():
        tree.delete(row)

def extractFileName(file_path):
    filename = file_path.split("/")[-1]
    return filename

def readTreeData():
    file_data = []
    for line in tree.get_children():
        for value in tree.item(line)['values']:
            file_data.append(value)
    return file_data

def mergeAllFiles():
    files = readTreeData()
    if not files:
        noFileMergeDialogBox()
        return
    if len(files) == 2:
        singleFileDialogBox()
        return

    paths = []
    for i in range(len(files)):
        if i % 2 == 1:
            paths.append(files[i])

    mergeFiles(paths)
    mergeSuccessDialogBox()
    return

root = tk.Tk()
root.title("PDF-Merge")
root.geometry("520x420")
root.iconbitmap(("./assets/pdf.ico"))

menubar = Menu(root)
primmenu = Menu(menubar, tearoff=0)
primmenu.add_command(label="Remove All", command=removeAllFiles)
menubar.add_cascade(label="File", menu=primmenu)
menubar.add_command(label="Help", command=instructionsDialogBox)
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

style = ttk.Style()
style.configure("Treeview.Heading", font=('MS Sans Serif', 16, 'bold'))
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12))

tree_frame = Frame(root)
tree_frame.pack(pady=10, fill='both', expand=True, anchor="center")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=("col1","col2"), show="tree")
tree.pack(expand=True, fill='y')

tree_scroll.config(command=tree.yview)
tree.heading('col1', text='File Name')
tree.heading('col2', text='Path')

tree.column('#0', minwidth=0, width=0, anchor=tk.CENTER)
tree.column('#1', minwidth=500, width=500, anchor=tk.CENTER)
tree.column('#2', minwidth=0, width=0, anchor=tk.CENTER)

# tv.move(s, tv.identify_row(event.y), moveto)
moveRow = move()

tree.bind("<B1-Motion>", moveRow.moveR, add='+')
tree.bind("<ButtonRelease-1>", moveRow.up, add='+')
tree.bind("<ButtonPress-1>", moveRow.down)
tree.bind("<Shift-ButtonRelease-1>", moveRow.shiftUp, add='+')
tree.bind("<Shift-ButtonPress-1>", moveRow.shiftDown, add='+')

mergePhoto = PhotoImage(file = ("./assets/merge.png")).subsample(12,12)
mergeButton = tk.Button(root, text='Merge', command=mergeAllFiles, image=mergePhoto, highlightthickness=4, bd = 2)
mergeButton.pack(padx=10, pady=10, side="left")
mergeButton.config(font=("Arial", 10, "bold"))
myTip = Hovertip(mergeButton,'Merge Files')

folderPhoto = PhotoImage(file = ("./assets/openFolder.png")).subsample(12,12)
uploadButton = tk.Button(root, command=uploadAction, image=folderPhoto, highlightthickness=4, bd = 2)
uploadButton.pack(padx=10, pady=10, side="left")
uploadButton.config(font=("Arial", 10, "bold"))
myTip = Hovertip(uploadButton,'Open Files')

removeFilePhoto = PhotoImage(file = ("./assets/delete_file.png")).subsample(12,12)
removeFileButton = tk.Button(root, text="Remove File", command=removeFile, image=removeFilePhoto, highlightthickness=4, bd = 2)
removeFileButton.pack(padx=10, pady=10, side="right")
removeFileButton.config(font=("Arial", 10, "bold"))
myTip = Hovertip(removeFileButton,'Remove Selected File')

#990000, #ebe834
#exitButton = tk.Button(root, text="Exit", command=root.destroy, height = 1, width = 10, fg='#FFFFFF', bg='#990000',highlightthickness=4, bd = 4)
#exiButton.pack(padx=10, pady=10, side="right")
#exitButton.config(font=("Arial", 10, "bold"))

root.mainloop()