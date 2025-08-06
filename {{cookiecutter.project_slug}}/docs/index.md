# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

This project provides a modern Python scripts development environment with:

- **Typer** for creating beautiful command-line interfaces
- **Scripts Framework** for organized automation and utility scripts
- **Modern Development Tools** with Ruff, Pytest, and UV
- **Quality Assurance** with 80%+ test coverage
- **Pre-commit Hooks** for automated code quality checks

## Quick Start

1. **Install dependencies:**

    ```bash
    just dev-setup
    ```

2. **Run tests:**
    ```bash
    just test
    ```

3. **Try the CLI:**
    ```bash
    python -m {{ cookiecutter.project_slug }}.cli hello
    python -m {{ cookiecutter.project_slug }}.cli hello --name "Developer"
    ```

4. **Serve documentation:**
    ```bash
    just docs-serve
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
└── README.md
```

## Features

### Command Line Interface

Built with [Typer](https://typer.tiangolo.com/) for rich, interactive command-line experiences.

### Scripts Framework

Organized structure for automation scripts with base classes and configuration management.

### Development Tools

- **UV** - Ultra-fast package management
- **Ruff** - Lightning-fast linting and formatting
- **Pytest** - Comprehensive testing with coverage
- **Just** - Modern task runner
- **Pre-commit** - Automated quality checks

## Development

See the [Development Guide](development.md) for detailed information about:

- Setting up the development environment
- Running tests and quality checks
- Contributing guidelines
- Code style and standards

## CLI Documentation

For command-line usage, see the [CLI Documentation](cli.md).

## Next Steps

- Check out the [CLI Reference](cli.md) for available commands
- Read the [Development Guide](development.md) for contribution guidelines
- Explore the [API Reference](reference.md) for code documentation
