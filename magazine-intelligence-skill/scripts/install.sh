#!/bin/bash
# Installation script for Magazine Intelligence Assistant Claude Code Skill
# This script installs the skill to your Claude Code skills directory

set -e

SKILL_NAME="magazine-intelligence-assistant"
INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(dirname "$SCRIPT_DIR")"

echo "📚 Installing Magazine Intelligence Assistant..."
echo ""

# Check if Claude Code is installed
if [ ! -d "$HOME/.claude" ]; then
    echo "❌ Error: Claude Code not found"
    echo "Please install Claude Code first: https://claude.com/claude-code"
    exit 1
fi

# Create skill directory
echo "📁 Installing to: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# Copy skill files
echo "📄 Copying skill files..."
cp -r "$SOURCE_DIR"/* "$INSTALL_DIR/"

# Make scripts executable
chmod +x "$INSTALL_DIR"/scripts/*.py 2>/dev/null || true

# Check Python dependencies
echo ""
echo "🔍 Checking dependencies..."
python3 -c "import PyPDF2" 2>/dev/null || {
    echo "⚠️  PyPDF2 not found. Installing..."
    pip3 install PyPDF2
}

# Create config directory
CONFIG_DIR="$HOME/Desktop/杂志精读"
mkdir -p "$CONFIG_DIR"

if [ ! -f "$CONFIG_DIR/config.json" ]; then
    echo ""
    echo "🎯 First-time setup detected!"
    echo "Run the configuration wizard to personalize your skill:"
    echo ""
    echo "  python3 $INSTALL_DIR/scripts/setup_wizard.py"
    echo ""
else
    echo "✅ Configuration found at: $CONFIG_DIR/config.json"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "Quick start:"
echo "  > I have a new magazine: ~/Downloads/Wired_March_2026.pdf"
echo "  > Please split it into articles and categorize them"
echo ""
echo "Documentation: $INSTALL_DIR/reference.md"
echo "GitHub: https://github.com/reneexiaoxiao/magazine-intelligence-assistant"
