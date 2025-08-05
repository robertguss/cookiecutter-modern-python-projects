#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath):
    """Remove a file if it exists."""
    file_path = PROJECT_DIRECTORY / filepath
    if file_path.exists():
        if file_path.is_dir():
            shutil.rmtree(file_path)
        else:
            file_path.unlink()


def run_command(command, check=True):
    """Run a shell command."""
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Post-generation project setup."""
    
    # Remove files based on configuration
    if "{{ cookiecutter.include_pre_commit }}" != "y":
        remove_file(".pre-commit-config.yaml")
    
    if "{{ cookiecutter.include_mkdocs }}" != "y":
        remove_file("mkdocs.yml")
        remove_file("docs")
    
    # Remove conditional source directories
    src_base = "{% if cookiecutter.use_src_layout == 'y' %}src/{% endif %}{{ cookiecutter.project_slug }}"
    
    if "{{ cookiecutter.include_typer }}" != "y":
        remove_file(f"{src_base}/cli")
    
    if "{{ cookiecutter.include_fastapi }}" != "y":
        remove_file(f"{src_base}/api")
    
    if "{{ cookiecutter.project_type }}" not in ["full", "automation"]:
        remove_file(f"{src_base}/automation")
    
    if "{{ cookiecutter.include_data_science }}" != "y":
        remove_file(f"{src_base}/data")
    
    # Remove conditional test files
    if "{{ cookiecutter.include_typer }}" != "y":
        remove_file("tests/test_cli.py")
    
    if "{{ cookiecutter.include_fastapi }}" != "y":
        remove_file("tests/test_api.py")
    
    if "{{ cookiecutter.include_data_science }}" != "y":
        remove_file("tests/test_data.py")
    
    # Initialize git repository
    print("🔧 Initializing git repository...")
    if run_command("git init"):
        print("✅ Git repository initialized")
    
    # Create initial commit
    print("📝 Creating initial commit...")
    run_command("git add .")
    if run_command('git commit -m "Initial commit from cookiecutter template"'):
        print("✅ Initial commit created")
    
    # Set up development environment if uv is available
    print("🔍 Checking for uv...")
    if run_command("uv --version", check=False):
        print("📦 Setting up development environment with uv...")
        if run_command("just dev-setup", check=False):
            print("✅ Development environment set up successfully")
        else:
            print("⚠️  Development setup failed. Run 'just dev-setup' manually.")
    else:
        print("⚠️  uv not found. Please install uv and run 'just dev-setup'")
    
    # Final instructions
    print("\n🎉 Project created successfully!")
    print(f"📁 Project location: {PROJECT_DIRECTORY}")
    print("\n📋 Next steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    
    if not run_command("uv --version", check=False):
        print("2. Install uv: https://docs.astral.sh/uv/")
        print("3. Install just: https://github.com/casey/just")
        print("4. Run: just dev-setup")
    else:
        print("2. Run: just dev-setup (if not already done)")
    
    print("3. Run: just test")
    
    if "{{ cookiecutter.include_fastapi }}" == "y":
        print("4. Run: just serve (to start API server)")
    
    if "{{ cookiecutter.include_mkdocs }}" == "y":
        print("5. Run: just docs-serve (to view documentation)")
    
    print("\n🚀 Happy coding!")


if __name__ == "__main__":
    main()
