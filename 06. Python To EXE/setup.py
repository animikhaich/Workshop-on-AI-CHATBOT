from cx_Freeze import Executable, setup
import os

os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

exe = Executable(script="Hello_World.py")

setup(name="Hello World",
      version="1.0",
      description="Just a program to print Hello World",
      executables=[exe])
