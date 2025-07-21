#!/usr/bin/env python3
"""Simple test runner"""
import subprocess
import sys
import os

def main():
    """Run tests"""
    # Check pytest
    try:
        import pytest
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    
    # Find test files
    test_files = []
    for f in ["test_component.py", "test_image_upload.py", "test_integration.py"]:
        if os.path.exists(f):
            test_files.append(f)
    
    if not test_files:
        print("No test files found")
        return False
    
    # Run tests
    cmd = [sys.executable, "-m", "pytest", "-v"] + test_files
    result = subprocess.run(cmd)
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)