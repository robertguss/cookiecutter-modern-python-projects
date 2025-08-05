{% if cookiecutter.include_mkdocs == 'y' -%}
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
- **Quality Assurance** with {{ cookiecutter.test_coverage_threshold }}%+ test coverage
{% if cookiecutter.include_pre_commit == 'y' -%}
- **Pre-commit Hooks** for automated code quality checks
{% endif %}

## Quick Start

1. **Install dependencies:**
   ```bash
   just dev-setup
   ```

2. **Run tests:**
   ```bash
   just test
   ```

{% if cookiecutter.include_fastapi == 'y' -%}
3. **Start the API server:**
   ```bash
   just serve
   ```
{% endif %}

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── {% if cookiecutter.use_src_layout == 'y' %}src/{{ cookiecutter.project_slug }}/{% else %}{{ cookiecutter.project_slug }}/{% endif %}
{% if cookiecutter.include_typer == 'y' -%}
│   ├── cli/           # Command-line interface
{% endif -%}
{% if cookiecutter.include_fastapi == 'y' -%}
│   ├── api/           # API routes and models
{% endif -%}
{% if cookiecutter.project_type in ['full', 'automation'] -%}
│   ├── automation/    # Automation scripts
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
{% endif %}
