# Development Guide

This guide covers the development workflow for {{ cookiecutter.project_name }}.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- [just](https://github.com/casey/just) task runner

## Setup

### Initial Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd {{ cookiecutter.project_slug }}

# Set up development environment
just dev-setup
```

This command will:
- Create a virtual environment with Python 3.13
- Install all dependencies including dev dependencies
- Set up pre-commit hooks

### Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
uv venv .venv --python=3.13

# Install dependencies
uv pip install -e ".[dev{% if cookiecutter.include_fastapi == 'y' %},api{% endif %}{% if cookiecutter.include_typer == 'y' %},cli{% endif %}{% if cookiecutter.include_data_science == 'y' %},ds{% endif %}]"

# Set up pre-commit hooks
uv run pre-commit install
```

## Development Workflow

### Available Commands

```bash
# Show all available commands
just

# Code quality
just lint          # Run linting with ruff
just format        # Format code with ruff
just check         # Run all quality checks

# Testing
just test          # Run tests
just test-cov      # Run tests with coverage report

{% if cookiecutter.include_fastapi == 'y' -%}
# Development server
just serve         # Start FastAPI development server
{% endif %}

# Documentation
just docs-serve    # Serve documentation locally
just docs-build    # Build documentation

# Cleanup
just clean         # Remove generated files and caches
```

### Code Quality Standards

This project uses several tools to maintain code quality:

#### Ruff
- **Linting**: Checks for code issues and style violations
- **Formatting**: Automatically formats code to consistent style
- **Import sorting**: Organizes imports consistently

Configuration is in `pyproject.toml` under `[tool.ruff]`.

#### Pytest
- **Unit tests**: All code should have corresponding tests
- **Coverage**: Minimum 80% test coverage required
- **Fixtures**: Use pytest fixtures for test setup

#### Deptry
- **Dependency analysis**: Checks for unused and missing dependencies
- **Clean dependencies**: Keeps `pyproject.toml` dependencies clean

#### Pre-commit Hooks
Automatically run before each commit:
- Ruff linting and formatting
- Deptry dependency checks
- Pytest test suite
- Basic file checks (trailing whitespace, etc.)

To run manually:
```bash
just pre-commit-run
```

## Testing

### Running Tests

```bash
# Run all tests
just test

# Run with coverage report
just test-cov

# Run specific test file
uv run pytest tests/test_specific.py

# Run tests matching pattern
uv run pytest -k "test_pattern"

# Run tests with verbose output
uv run pytest -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Mirror the source structure: `src/package/module.py` → `tests/test_module.py`
- Use descriptive test names: `test_function_name_expected_behavior`
- Use fixtures for common test setup (see `tests/conftest.py`)

Example test:
```python
def test_my_function_returns_expected_value():
    result = my_function("input")
    assert result == "expected_output"
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/    # Main package
│   ├── __init__.py             # Package initialization
{% if cookiecutter.include_typer == 'y' -%}
│   ├── cli/                    # Command-line interface
│   │   └── __init__.py
{% endif -%}
{% if cookiecutter.include_fastapi == 'y' -%}
│   ├── api/                    # API routes and models
│   │   └── __init__.py
{% endif -%}
{% if cookiecutter.project_type in ['full', 'automation'] -%}
│   ├── automation/             # Automation scripts
│   │   └── __init__.py
{% endif -%}
{% if cookiecutter.include_data_science == 'y' -%}
│   └── data/                   # Data processing utilities
│       └── __init__.py
{% endif -%}
├── tests/                      # Test files
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration and fixtures
│   └── test_*.py               # Test modules
├── docs/                       # Documentation
│   ├── index.md
│   └── *.md
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .gitignore                  # Git ignore rules
└── README.md                   # Project overview
```

## Adding Dependencies

### Production Dependencies
```bash
# Add to pyproject.toml [project] dependencies
uv add package-name

# Or edit pyproject.toml manually and run:
uv pip install -e .
```

### Development Dependencies
```bash
# Add to pyproject.toml [project.optional-dependencies] dev
# Edit pyproject.toml manually and run:
uv pip install -e ".[dev]"
```

### Optional Dependencies
Add to appropriate optional dependency groups in `pyproject.toml`:
- `api`: FastAPI and related packages
- `cli`: Typer and CLI-related packages
- `ds`: Data science packages

## Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run quality checks**: `just check`
5. **Run tests**: `just test`
6. **Commit your changes**: `git commit -m "Add amazing feature"`
7. **Push to the branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

Pre-commit hooks will automatically run quality checks before each commit.

## Troubleshooting

### Common Issues

**Import errors when running tests:**
- Make sure you're in the project root directory
- Ensure the virtual environment is activated
- Check that the package is installed in development mode: `uv pip install -e .`

**Pre-commit hooks failing:**
- Run `just lint` and `just format` to fix code style issues
- Run `just test` to ensure all tests pass
- Check `just check` for any remaining issues

**UV command not found:**
- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Or follow the [official installation guide](https://docs.astral.sh/uv/)

**Just command not found:**
- Install just: Follow the [installation guide](https://github.com/casey/just#installation)
- On macOS: `brew install just`
- On Ubuntu: `sudo snap install --edge --classic just`
