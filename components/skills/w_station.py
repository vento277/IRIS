# Function Def'n
# Create a working station on various coding & CAD applications

# Header
import os
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

# Define path for the folder
def user_path(text):
    parent_path = r'H:\Personal Project'
    path = os.path.join(parent_path, text)
    return path

