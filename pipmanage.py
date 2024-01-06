import subprocess
import os

# Function to create a virtual environment
def create_venv(venv_name):
    subprocess.run(['python3', '-m', 'venv', venv_name])

# Function to install package in the virtual environment
def install_package(venv_name, package):
    pip_path = os.path.join(venv_name, 'bin', 'pip')
    subprocess.run([pip_path, 'install', package])

# Check if requirements.txt exists
if not os.path.exists('requirements.txt'):
    print('requirements.txt not found')
    exit(1)

# Read each line in requirements.txt and process
with open('requirements.txt', 'r') as file:
    for line in file:
        package = line.strip()
        if package:
            # Format the virtual environment directory name
            package_name = package.split('==')[0]
            venv_name = f'venv_{package_name}'
            print(f'Creating virtual environment in {venv_name} for package {package}...')
            create_venv(venv_name)
            install_package(venv_name, package)
            print(f'Package {package} installed in {venv_name}')
