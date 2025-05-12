import os

"""

Helper to check if directories exist.

"""

def checkDirec(direc):
    if not os.path.exists(direc):
        os.makedirs(direc)
    return 