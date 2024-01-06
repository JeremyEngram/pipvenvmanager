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
