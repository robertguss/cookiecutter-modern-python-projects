# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

{% if cookiecutter.include_fastapi == 'y' -%}

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
  {% endif -%}
  {% if cookiecutter.include_typer == 'y' -%}
- 🖥️ **Typer** - Modern CLI framework with rich output
  {% endif -%}
  {% if cookiecutter.include_data_science == 'y' -%}
- 📊 **Data Science** - Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
  {% endif -%}

- 🧪 **Testing** - Pytest with 80%+ coverage requirement
- 🔧 **Code Quality** - Ruff for linting and formatting
- 📦 **Dependency Management** - UV for fast package management
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
- Install all dependencies
- Set up pre-commit hooks

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

{% if cookiecutter.include_fastapi == 'y' -%}
# Start development server
just serve
{% endif -%}

# Serve documentation
just docs-serve

# Clean up generated files
just clean
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/    # Main package
{% if cookiecutter.include_typer == 'y' -%}
│   ├── cli/                    # Command-line interface
{% endif -%}
{% if cookiecutter.include_fastapi == 'y' -%}
│   ├── api/                    # API routes and models
{% endif -%}
{% if cookiecutter.project_type in ['full', 'scripts'] -%}
│   ├── automation/             # Scripts and utilities
{% endif -%}
{% if cookiecutter.include_data_science == 'y' -%}
│   └── data/                   # Data processing utilities
{% endif -%}
├── tests/                      # Test files
├── docs/                       # Documentation
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
├── .pre-commit-config.yaml     # Pre-commit hooks
└── README.md                   # This file
```

## Usage

{% if cookiecutter.include_typer == 'y' -%}

### Command Line Interface

```bash
# Run the CLI
{{ cookiecutter.project_slug }} --help
```

{% endif %}

{% if cookiecutter.include_fastapi == 'y' -%}

### API Server

```bash
# Start the development server
just serve

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

{% endif %}

{% if cookiecutter.include_data_science == 'y' -%}

### Data Science

```python
from {{ cookiecutter.project_slug }}.data import load_data, process_data

# Your data science code here
data = load_data("path/to/data.csv")
processed = process_data(data)
```

{% endif %}

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
