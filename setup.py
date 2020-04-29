application_title = "Sudoku" 
main_python_file = "GUI.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = application_title,
    version = "1.0",
    description = "test",
    executables = [Executable("GUI.py", base = base)]
)

#use 'python setup.py bdist_msi'
#OR
#use 'python setup.py build'