import PyInstaller.__main__
import os

# Get the absolute path to the icon file
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'src/main.py',  # Your main script
    '--onefile',    # Create single executable
    '--name=JSFNC', # Name of the executable
    '--add-data=README.md;.',  # Include README
    '--clean',      # Clean cache
    '--console',    # Console based application
])