from tkinter.messagebox import showinfo

def instructionsDialogBox():
    showinfo("Help", "Open the files you want to merge. \n\nThen drag the files in the desired order such that the " \
    "top will be the first document and the bottom will be the last document.")

def noFileRemoveDialogBox():
    showinfo("Warning", "Please add files first.")

def noSelectedRowDialogBox():
    showinfo("Warning", "Please select a row first.")

def noFileMergeDialogBox():
    showinfo("Warning", "Please add files before merging.")

def singleFileDialogBox():
    showinfo("Warning", "Please add more than one file before merging.")

def mergeSuccessDialogBox():
    showinfo("Success", "Merged successfully! Merged file stored in Downloads folder.")