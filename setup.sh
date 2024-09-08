#!/bin/bash

# Ensure the script is run from the project root directory
if [ ! -f "requirements.txt" ]; then
    echo "Error: 'requirements.txt' not found. Please run this script from the project root directory."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Notify user of successful setup
echo "Setup complete. You can now run the simulation using 'python main.py' and visualize data using 'streamlit run visualization.py'."
gi