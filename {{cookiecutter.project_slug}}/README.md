# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- 🖥️ **Typer** - Modern CLI framework with rich output
- 📁 **Scripts Framework** - Organized automation and utility scripts
- 🧪 **Testing** - Pytest with 80%+ coverage requirement
- 🔧 **Code Quality** - Ruff for linting and formatting
- 📦 **Dependency Management** - UV for fast package management (always installs latest versions, with reproducible builds via uv.lock)
- 🏗️ **Task Runner** - Just for common development tasks
- 🪝 **Pre-commit Hooks** - Automated code quality checks
- 📚 **Documentation** - MkDocs with Material theme

## Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- [just](https://github.com/casey/just) task runner

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd {{ cookiecutter.project_slug }}

# Set up development environment
just dev-setup
```

This will:

- Create a virtual environment
- Install all dependencies (latest versions)
- Generate a `uv.lock` file for reproducible builds
- Set up pre-commit hooks

> **Note**: This project is configured to always install the latest versions of all dependencies. The `uv.lock` file ensures reproducible builds across environments while still allowing you to stay current with the latest package releases.

## Development

### Available Commands

```bash
# Show all available commands
just

# Run tests
just test

# Run tests with coverage report
just test-cov

# Lint and format code
just lint
just format

# Check code quality
just check

# Serve documentation
just docs-serve

# Clean up generated files
just clean
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/    # Main package
│   ├── cli/                    # Command-line interface
│   └── __init__.py
├── scripts/                    # Automation and utility scripts
│   └── automation/             # Script framework
├── tests/                      # Test files
├── docs/                       # Documentation
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
├── .pre-commit-config.yaml     # Pre-commit hooks
└── README.md                   # This file
```

## Usage

### Command Line Interface

```bash
# Run the CLI
python -m {{ cookiecutter.project_slug }}.cli --help

# Example commands
python -m {{ cookiecutter.project_slug }}.cli hello
python -m {{ cookiecutter.project_slug }}.cli hello --name "Developer"
python -m {{ cookiecutter.project_slug }}.cli version
```

### Scripts Framework

The `scripts/` directory contains organized automation and utility scripts:

```python
from scripts.automation import BaseAutomation, AutomationConfig

# Create custom automation
config = AutomationConfig(
    name="my_script",
    description="My custom script",
    enabled=True
)

# Your automation logic here
```

## Testing

```bash
# Run all tests
just test

# Run with coverage report
just test-cov

# Run specific test file
uv run pytest tests/test_specific.py
```

## Documentation

Documentation is built with MkDocs and the Material theme.

```bash
# Serve docs locally
just docs-serve

# Build docs
just docs-build
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure they pass
5. Submit a pull request

Pre-commit hooks will automatically run code quality checks.
