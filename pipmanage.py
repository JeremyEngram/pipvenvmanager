#!/bin/bash

# Ensure requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found"
    exit 1
fi

# Loop through each line in requirements.txt
while IFS= read -r package; do
    # Create a directory for the virtual environment
    venv_dir="venv_$package"
    echo "Creating virtual environment in $venv_dir for package $package..."
    python3 -m venv "$venv_dir"

    # Activate the virtual environment
    source "$venv_dir/bin/activate"

    # Install the package
    pip install $package

    # Deactivate the virtual environment
    deactivate

    echo "Package $package installed in $venv_dir"
done < requirements.txt
