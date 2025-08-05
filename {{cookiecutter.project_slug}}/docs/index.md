# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

This project provides a modern Python development environment with:

{% if cookiecutter.include_fastapi == 'y' -%}

- **FastAPI** for building high-performance APIs
  {% endif -%}
  {% if cookiecutter.include_typer == 'y' -%}
- **Typer** for creating beautiful command-line interfaces
  {% endif -%}
  {% if cookiecutter.include_data_science == 'y' -%}
- **Data Science Tools** including Pandas, NumPy, and Matplotlib
  {% endif -%}
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

{% if cookiecutter.include_fastapi == 'y' -%} 3. **Start the API server:**

```bash
just serve
```

{% endif %}

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/
{% if cookiecutter.include_typer == 'y' -%}
│   ├── cli/           # Command-line interface
{% endif -%}
{% if cookiecutter.include_fastapi == 'y' -%}
│   ├── api/           # API routes and models
{% endif -%}
{% if cookiecutter.project_type in ['full', 'scripts'] -%}
│   ├── automation/    # Scripts and utilities
{% endif -%}
{% if cookiecutter.include_data_science == 'y' -%}
│   └── data/          # Data processing utilities
{% endif -%}
├── tests/             # Test files
├── docs/              # Documentation
└── pyproject.toml     # Project configuration
```

## Development

See the [Development Guide](development.md) for detailed information about:

- Setting up the development environment
- Running tests and quality checks
- Contributing guidelines
- Code style and standards

{% if cookiecutter.include_fastapi == 'y' -%}

## API Documentation

For API usage and endpoints, see the [API Documentation](api.md).
{% endif %}

{% if cookiecutter.include_typer == 'y' -%}

## CLI Documentation

For command-line usage, see the [CLI Documentation](cli.md).
{% endif %}

{% if cookiecutter.include_data_science == 'y' -%}

## Data Science

For data processing and analysis tools, see the [Data Science Documentation](data.md).
{% endif %}
