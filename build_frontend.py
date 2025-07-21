#!/usr/bin/env python3
"""
Script for building the frontend part of the component
"""
import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd, cwd=None, quiet=False):
    """Execute command and return result"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd, 
            check=True,
            capture_output=True,
            text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        if not quiet:
            print(f"✗ Error executing: {cmd}")
            print(f"Error: {e.stderr}")
        return None


def main():
    """Main build function"""
    # Define paths
    script_dir = Path(__file__).parent
    frontend_dir = script_dir / "streamlit_crepe" / "frontend"
    
    if not frontend_dir.exists():
        print("✗ Frontend directory not found")
        sys.exit(1)
    
    print("🔨 Building frontend...")
    
    # Check Node.js and npm
    if not run_command("node --version", quiet=True):
        print("✗ Node.js not found. Please install Node.js")
        sys.exit(1)
    
    if not run_command("npm --version", quiet=True):
        print("✗ npm not found")
        sys.exit(1)
    
    # Change to frontend directory
    os.chdir(frontend_dir)
    
    # Install dependencies
    print("📦 Installing dependencies...")
    if not run_command("npm install", quiet=True):
        print("✗ Failed to install dependencies")
        sys.exit(1)
    
    # Build project
    print("⚡ Building...")
    if not run_command("npx vite build", quiet=True):
        print("✗ Build failed")
        sys.exit(1)
    
    # Clean up source maps
    build_dir = frontend_dir / "build"
    if build_dir.exists():
        # Remove source map references from CSS files
        css_files = list(build_dir.glob("*.css"))
        if css_files:
            import re
            for css_file in css_files:
                try:
                    with open(css_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    content = re.sub(r'/\*# sourceMappingURL=.*?\*/', '', content)
                    content = re.sub(r'//# sourceMappingURL=.*', '', content)
                    content = content.strip()
                    
                    with open(css_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                except:
                    pass
        
        print("✅ Build completed successfully!")
    else:
        print("✗ Build failed - no output directory")
        sys.exit(1)


if __name__ == "__main__":
    main()