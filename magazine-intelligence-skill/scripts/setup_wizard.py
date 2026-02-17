#!/usr/bin/env python3
"""
Interactive setup wizard for magazine intelligence assistant
Run this to configure your personalized reading preferences
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tools.setup_wizard import SetupWizard

if __name__ == "__main__":
    wizard = SetupWizard()
    wizard.run()
