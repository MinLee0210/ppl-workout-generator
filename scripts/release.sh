#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

# Define terminal colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=======================================${NC}"
echo -e "${BLUE}🚀  PPL Workout Generator Release Script${NC}"
echo -e "${BLUE}=======================================${NC}\n"

# 1. Clean previous build artifacts
echo -e "${YELLOW}[1/5] Cleaning up old build artifacts...${NC}"
rm -rf build/ dist/ src/*.egg-info *.egg-info
echo -e "${GREEN}Clean completed.${NC}\n"

# 2. Run unit tests
echo -e "${YELLOW}[2/5] Running pytest suite...${NC}"
if python3 -m pytest; then
    echo -e "${GREEN}All tests passed successfully!${NC}\n"
else
    echo -e "${RED}Tests failed. Aborting release process.${NC}"
    exit 1
fi

# 3. Build package distributions
echo -e "${YELLOW}[3/5] Building source distribution and wheel...${NC}"
if python3 -m build; then
    echo -e "${GREEN}Build succeeded.${NC}\n"
else
    echo -e "${RED}Build failed. Aborting release process.${NC}"
    exit 1
fi

# 4. Check package integrity
echo -e "${YELLOW}[4/5] Checking package integrity with twine...${NC}"
if python3 -m twine check dist/*; then
    echo -e "${GREEN}Integrity check passed.${NC}\n"
else
    echo -e "${RED}Twine validation failed. Aborting release.${NC}"
    exit 1
fi

# Show built files
echo -e "${BLUE}Generated Assets:${NC}"
ls -lh dist/
echo ""

# 5. Prompt for Upload
echo -e "${YELLOW}[5/5] Uploading to PyPI${NC}"
read -p "Upload to TestPyPI first? (y/N): " testpypi_choice

if [[ "$testpypi_choice" =~ ^[Yy]$ ]]; then
    echo -e "${BLUE}Uploading to TestPyPI...${NC}"
    python3 -m twine upload --repository testpypi dist/*
    echo -e "${GREEN}Upload to TestPyPI completed!${NC}\n"
fi

read -p "Upload to production PyPI? (y/N): " prod_choice

if [[ "$prod_choice" =~ ^[Yy]$ ]]; then
    echo -e "${BLUE}Uploading to production PyPI...${NC}"
    python3 -m twine upload dist/*
    echo -e "${GREEN}Upload to production PyPI completed!${NC}"
else
    echo -e "${YELLOW}Production upload skipped.${NC}"
fi

echo -e "\n${GREEN}Release script execution finished.${NC}"
