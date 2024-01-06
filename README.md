Here's a script that accomplishes this:



bash

pip freeze > requirements.txt
cat requirements.txt | grep -v "^\-e" | cut -d '=' -f 1 | xargs -n1 pip uninstall -y



python

import subprocess
import os

def freeze_and_uninstall():
    # Step 1: Freeze the installed packages to a file
    with open("frozen_packages.txt", "w") as file:
        subprocess.run(["pip", "freeze"], stdout=file)

    # Step 2: Uninstall the packages
    with open("frozen_packages.txt", "r") as file:
        packages = [line.strip().split('==')[0] for line in file if '==' in line]

    for package in packages:
        subprocess.run(["pip", "uninstall", "-y", package])

    # Optional: Delete the file after uninstallation
    os.remove("frozen_packages.txt")

freeze_and_uninstall()

This script does the following:

    First, it runs pip freeze and writes the output to a file named frozen_packages.txt.
    It then reads this file, extracts the package names (ignoring version numbers and lines without '=='), and uninstalls each package using pip uninstall. The -y flag is used to automatically confirm the uninstallation for each package.
    Finally, it deletes the frozen_packages.txt file.

Important Notes:

    This script will uninstall all packages listed by pip freeze, which might include packages critical to your Python environment. Be sure to review the list and understand the consequences before running the script.
    The script should be run with the appropriate permissions for installing and uninstalling packages in your Python environment.
    If you have multiple Python environments (like virtual environments), make sure you run this script in the correct environment where you want the changes to apply.
    It's a good practice to back up your environment before performing such operations. You can do this by copying the frozen_packages.txt file to a safe location.







To create a script that installs packages from a previously saved list within a virtual environment, you can follow these steps:

    Create a Virtual Environment: First, you need to create a new virtual environment using venv or a similar tool.

    Activate the Virtual Environment: Before installing packages, the virtual environment must be activated.

    Install Packages from the List: Read the list of packages from the file and install them using pip.

Here is a sample script to accomplish this:

python

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

venv_name = "myenv"  # Name of the virtual environment
file_name = "frozen_packages.txt"  # File containing the list of packages

install_packages_from_file(file_name, venv_name)

In this script:

    create_and_activate_venv function creates a virtual environment and returns the path to the activation script.
    install_packages_from_file reads the list of packages from frozen_packages.txt and installs each package within the virtual environment.

Important Notes:

    The activation of the virtual environment in the script is a bit tricky. This script assumes you will run it in a shell that can execute the activation script (like Bash on Unix or Command Prompt on Windows).
    The approach to activate the virtual environment within the Python script might not work in some environments. In such cases, you may need to activate the virtual environment manually before running the script.
    This script assumes that frozen_packages.txt contains a list of packages in the format output by pip freeze.
    Always ensure that you're running this script in the correct context, especially if you're working with multiple Python environments.
