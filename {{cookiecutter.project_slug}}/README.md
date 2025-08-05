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
  {% if cookiecutter.include_jupyter == 'y' -%}
- 📓 **Jupyter** - Interactive notebooks for data exploration
  {% endif -%}
- 🧪 **Testing** - Pytest with {{ cookiecutter.test_coverage_threshold }}%+ coverage requirement
- 🔧 **Code Quality** - Ruff for linting and formatting
- 📦 **Dependency Management** - UV for fast package management
- 🏗️ **Task Runner** - Just for common development tasks
  {% if cookiecutter.include_pre_commit == 'y' -%}
- 🪝 **Pre-commit Hooks** - Automated code quality checks
  {% endif -%}
  {% if cookiecutter.include_mkdocs == 'y' -%}
- 📚 **Documentation** - MkDocs with Material theme
  {% endif %}

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
  {% if cookiecutter.include_pre_commit == 'y' -%}
- Set up pre-commit hooks
  {% endif %}

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

{% if cookiecutter.include_mkdocs == 'y' -%}
# Serve documentation
just docs-serve
{% endif %}

# Clean up generated files
just clean
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── {% if cookiecutter.use_src_layout == 'y' %}src/{{ cookiecutter.project_slug }}/{% else %}{{ cookiecutter.project_slug }}/{% endif %}    # Main package
{% if cookiecutter.include_typer == 'y' -%}
│   ├── cli/                    # Command-line interface
{% endif -%}
{% if cookiecutter.include_fastapi == 'y' -%}
│   ├── api/                    # API routes and models
{% endif -%}
{% if cookiecutter.project_type in ['full', 'automation'] -%}
│   ├── automation/             # Automation scripts
{% endif -%}
{% if cookiecutter.include_data_science == 'y' -%}
│   └── data/                   # Data processing utilities
{% endif -%}
├── tests/                      # Test files
{% if cookiecutter.include_mkdocs == 'y' -%}
├── docs/                       # Documentation
{% endif -%}
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
{% if cookiecutter.include_pre_commit == 'y' -%}
├── .pre-commit-config.yaml     # Pre-commit hooks
{% endif -%}
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

{% if cookiecutter.include_mkdocs == 'y' -%}

## Documentation

Documentation is built with MkDocs and the Material theme.

```bash
# Serve docs locally
just docs-serve

# Build docs
just docs-build
```

{% endif %}

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure they pass
5. Submit a pull request

{% if cookiecutter.include_pre_commit == 'y' -%}
Pre-commit hooks will automatically run code quality checks.
{% endif %}

## License

{% if cookiecutter.license == "MIT" -%}
This project is licensed under the MIT License - see the LICENSE file for details.
{% elif cookiecutter.license == "Apache-2.0" -%}
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
{% elif cookiecutter.license == "BSD-3-Clause" -%}
This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.
{% elif cookiecutter.license == "GPL-3.0" -%}
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
{% else -%}
This project is not licensed for public use.
{% endif %}
