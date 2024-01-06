import subprocess
import os
import sys

def create_and_activate_venv(venv_name):
    # Create a virtual environment
    subprocess.run([sys.executable, "-m", "venv", venv_name])

    # Activate the virtual environment
    # On Windows
    if os.name == "nt":
        activate_script = os.path.join(venv_name, "Scripts", "activate")
    # On Unix or MacOS
    else:
        activate_script = os.path.join(venv_name, "bin", "activate")
    
    return activate_script

def install_packages_from_file(file_name, venv_name):
    # Activate the virtual environment
    activate_script = create_and_activate_venv(venv_name)

    # Install packages from the file
    with open(file_name, "r") as file:
        for line in file:
            package = line.strip()
            if package:
                subprocess.run(f"{activate_script} && pip install {package}", shell=True)

venv_name = "omnicenv"  # Name of the virtual environment
file_name = "requirements.txt"  # File containing the list of packages

install_packages_from_file(file_name, venv_name)
