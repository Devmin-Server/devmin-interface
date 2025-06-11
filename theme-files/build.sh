
#!/bin/bash

# UltraFast Theme Build Script
# This script packages the theme for distribution

set -e

THEME_NAME="ultrafast-theme"
VERSION="2.0.0"
BUILD_DIR="build"
PACKAGE_NAME="${THEME_NAME}-${VERSION}.wbt.gz"

echo "Building UltraFast Theme v${VERSION}..."

# Create build directory
mkdir -p $BUILD_DIR
rm -rf $BUILD_DIR/*

# Copy theme files
echo "Copying theme files..."
cp -r authentic-theme $BUILD_DIR/
cp theme.info $BUILD_DIR/
cp config.info $BUILD_DIR/

# Create the package structure
cd $BUILD_DIR

# Create theme package
echo "Creating theme package..."
tar -czf ../$PACKAGE_NAME .

cd ..

# Cleanup
rm -rf $BUILD_DIR

echo "Theme package created: $PACKAGE_NAME"
echo "Package size: $(du -h $PACKAGE_NAME | cut -f1)"

# Verify package
echo "Verifying package contents..."
tar -tzf $PACKAGE_NAME | head -10

echo "Build completed successfully!"
echo ""
echo "Installation instructions:"
echo "1. Upload $PACKAGE_NAME to Devmin/Usermin"
echo "2. Go to Webmin Configuration → Themes"
echo "3. Click 'Install Theme' and select the uploaded file"
echo "4. Apply the theme from the dropdown menu"
