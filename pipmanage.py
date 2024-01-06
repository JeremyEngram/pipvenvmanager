import subprocess
import os

# Function to create and activate a virtual environment
def create_venv(venv_name):
    subprocess.run([f'python3 -m venv {venv_name}'], shell=True)

# Function to install package in the virtual environment
def install_package(venv_name, package):
    subprocess.run([f'{venv_name}/bin/pip install {package}'], shell=True)

# Check if requirements.txt exists
if not os.path.exists('requirements.txt'):
    print('requirements.txt not found')
    exit(1)

# Read each line in requirements.txt and process
with open('requirements.txt', 'r') as file:
    for line in file:
        package = line.strip()
        if package:
            venv_name = f'venv_{package}'
            print(f'Creating virtual environment in {venv_name} for package {package}...')
            create_venv(venv_name)
            install_package(venv_name, package)
            print(f'Package {package} installed in {venv_name}')
