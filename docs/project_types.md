# Project Types Guide

This cookiecutter template offers 6 different project types, each tailored for specific use cases. Each project type automatically enables certain features and creates the appropriate directory structure.

## Project Type Matrix

| Project Type | FastAPI | Typer | Data Science | Scripts |
|--------------|:-------:|:-----:|:------------:|:-------:|
| `full`       |    ✅    |   ✅   |      ✅       |    ✅    |
| `api`        |    ✅    |   ❌   |      ❌       |    ❌    |
| `cli`        |    ❌    |   ✅   |      ❌       |    ❌    |
| `data_science`|   ❌    |   ❌   |      ✅       |    ❌    |
| `scripts`    |    ❌    |   ✅   |      ❌       |    ✅    |
| `minimal`    |    ❌    |   ❌   |      ❌       |    ❌    |

## Project Type Details

### Full (`full`)
**Best for:** Complete applications that need web APIs, CLI tools, data processing, and custom scripts.

**What you get:**
- FastAPI web framework for REST APIs
- Typer for command-line interfaces
- Data science tools (pandas, matplotlib, etc.)
- Scripts framework for experimentation
- All optional dependency groups: `[api]`, `[cli]`, `[ds]`

**Directory structure:**
```
src/your_project/
├── api/          # FastAPI routes and models
├── cli/          # Typer CLI commands
├── data/         # Data processing modules
└── __init__.py
scripts/
└── automation/   # Scripts and utilities
```

### API (`api`)
**Best for:** Web APIs, REST services, microservices.

**What you get:**
- FastAPI web framework
- Uvicorn ASGI server
- Optional dependency group: `[api]`

**Directory structure:**
```
src/your_project/
├── api/          # FastAPI routes and models
└── __init__.py
```

### CLI (`cli`)
**Best for:** Command-line tools, utilities, scripts with user interaction.

**What you get:**
- Typer CLI framework
- Rich for beautiful terminal output
- Console script entry point: `your-project-name`
- Optional dependency group: `[cli]`

**Directory structure:**
```
src/your_project/
├── cli/          # Typer CLI commands
└── __init__.py
```

### Data Science (`data_science`)
**Best for:** Data analysis, machine learning, research projects.

**What you get:**
- Pandas (always included as core dependency)
- Optional data science stack: matplotlib, seaborn, polars, scikit-learn, numpy
- Optional dependency group: `[ds]`

**Directory structure:**
```
src/your_project/
├── data/         # Data processing and analysis modules
└── __init__.py
```

### Scripts (`scripts`)
**Best for:** Python experimentation, utility scripts, prototyping.

**What you get:**
- Typer for CLI interfaces
- Rich for terminal output
- Scripts framework for experimentation
- Console script entry point: `your-project-name`
- Optional dependency groups: `[cli]`

**Directory structure:**
```
src/your_project/
├── cli/          # Typer CLI commands
└── __init__.py
scripts/
└── automation/   # Scripts and utilities framework
```

### Minimal (`minimal`)
**Best for:** Simple Python packages, libraries, learning projects.

**What you get:**
- Basic Python package structure
- No additional frameworks or dependencies
- Clean starting point for any Python project

**Directory structure:**
```
src/your_project/
└── __init__.py
```

## Always Included Features

Regardless of project type, every generated project includes:

- **Python 3.13** support
- **Pre-commit hooks** with ruff, mypy, and other quality tools
- **MkDocs documentation** with material theme
- **80% test coverage** requirement
- **src/ layout** for clean package structure
- **pytest** testing framework with coverage reporting
- **Ruff** for linting and formatting
- **uv** for dependency management
- **justfile** for task automation
- **pyproject.toml** configuration (PEP 621)

## Console Scripts

Projects with CLI support (full, cli, scripts) automatically get a console script entry point:

```bash
# If your project is named "my-awesome-project"
my-awesome-project --help
```

The script name follows the pattern: `project_slug` (underscores converted to hyphens).
