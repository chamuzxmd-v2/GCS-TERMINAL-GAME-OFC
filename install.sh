#!/bin/bash

# Install.sh for GCS Repo
# Developed by Chamuz zZ

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Installation...${NC}"

# Update & upgrade system
echo -e "${GREEN}Updating system packages...${NC}"
pkg update -y && pkg upgrade -y

# Install dependencies
echo -e "${GREEN}Installing dependencies...${NC}"
pkg install python -y
pkg install git -y
pkg install clang -y
pkg install nano -y
pkg install wget -y
pkg install curl -y

# Clone repo (optional if script is outside repo)
# echo -e "${GREEN}Cloning repository...${NC}"
# git clone https://github.com/username/repo.git

# Give execution permission to all python scripts
echo -e "${GREEN}Setting permissions for scripts...${NC}"
chmod +x *.py
chmod +x *.sh

# Optional: Install Python packages
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}Installing Python dependencies...${NC}"
    pip install -r requirements.txt
fi

echo -e "${GREEN}Installation Completed Successfully!${NC}"
