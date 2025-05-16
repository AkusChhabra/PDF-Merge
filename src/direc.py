import os

"""

Helper to check if directories exist.

"""

def checkDirec(direc):
    if os.path.exists(direc):
        return True
    return False