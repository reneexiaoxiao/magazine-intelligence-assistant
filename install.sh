#!/bin/bash
# Magazine Intelligence Assistant - Installation Script

set -e

echo "=========================================="
echo "  Magazine Intelligence Assistant"
echo "  Installation Script"
echo "=========================================="
echo ""

# Check Python version
echo "🔍 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "✅ Python $PYTHON_VERSION found"

# Create virtual environment (optional)
echo ""
echo "📦 Would you like to create a virtual environment? (recommended)"
read -p "[y/N]: " create_venv

if [ "$create_venv" = "y" ] || [ "$create_venv" = "Y" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment created"
fi

# Install dependencies
echo ""
echo "📚 Installing dependencies..."
pip3 install PyPDF2 --quiet

echo "✅ Dependencies installed"

# Run setup wizard
echo ""
echo "=========================================="
echo "  Running Setup Wizard"
echo "=========================================="
echo ""

python3 tools/setup_wizard.py

# Create example config if not exists
if [ ! -f config.json ]; then
    echo ""
    echo "📝 Creating example config..."
    cp config.example.json config.json
    echo "✅ Example config created. Edit config.json to customize."
fi

# Make scripts executable
chmod +x tools/*.py

echo ""
echo "=========================================="
echo "  Installation Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Review your config.json"
echo "  2. Edit config.json to customize tags and preferences"
echo "  3. Use template/magazine_recommender_skill.md with Claude/GPT"
echo ""
echo "For help, see README.md"
echo ""
