# Modern Python Project Cookiecutter Template

A comprehensive cookiecutter template for modern Python projects with best practices, quality tools, and flexible configuration options.

## 🚀 Features

### 🏗️ Project Types

- **Full Stack**: Everything included (API + CLI + Data Science)
- **API**: FastAPI-based web APIs
- **CLI**: Command-line tools with Typer
- **Data Science**: Pandas, NumPy, Matplotlib, Seaborn
- **Automation**: Scripts and automation tools
- **Minimal**: Basic Python package

### 🛠️ Modern Development Tools

- **[uv](https://docs.astral.sh/uv/)** - Ultra-fast Python package manager
- **[Ruff](https://docs.astral.sh/ruff/)** - Lightning-fast linting and formatting
- **[pytest](https://pytest.org/)** - Comprehensive testing framework
- **[just](https://github.com/casey/just)** - Modern task runner
- **[deptry](https://github.com/fpgmaas/deptry)** - Dependency analysis
- **[pre-commit](https://pre-commit.com/)** - Git hooks for quality assurance

### 📚 Documentation & Quality

- **[MkDocs](https://www.mkdocs.org/)** with Material theme
- **Test coverage** requirements (configurable 80-95%)
- **Type hints** with mypy support
- **EditorConfig** for consistent coding styles

### 🎯 Smart Configuration

- **Conditional dependencies** based on project type
- **Flexible project structure** (src layout or flat)


## 📋 Quick Start

### Prerequisites

- Python 3.11+
- [cookiecutter](https://cookiecutter.readthedocs.io/)
- [uv](https://docs.astral.sh/uv/) (recommended)
- [just](https://github.com/casey/just) (recommended)

### Installation

```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Generate a new project
cookiecutter https://github.com/yourusername/python-project-cookiecutter

# Or use this local template
cookiecutter /path/to/this/template
```

### Configuration Options

The template will prompt you for:

- **Project name** and description
- **Author** information

- **Python version** (3.11, 3.12, 3.13)
- **Project type** (full, api, cli, data_science, automation, minimal)
- **Optional features** (pre-commit, MkDocs, etc.)
- **Test coverage threshold** (80%, 85%, 90%, 95%)

## 🏗️ Generated Project Structure

```
your_project/
├── src/your_project/           # Source code (if src layout chosen)
│   ├── __init__.py
│   ├── cli/                    # CLI commands (if enabled)
│   ├── api/                    # FastAPI routes (if enabled)
│   ├── automation/             # Automation scripts (if enabled)
│   └── data/                   # Data science utilities (if enabled)
├── tests/                      # Test files
│   ├── conftest.py
│   └── test_*.py
├── docs/                       # Documentation (if enabled)
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
├── .pre-commit-config.yaml     # Pre-commit hooks (if enabled)
├── .gitignore
├── .editorconfig

└── README.md
```

## 🎯 Project Types Explained

### Full Stack (`full`)

Perfect for comprehensive projects that need everything:

- FastAPI for APIs
- Typer for CLI
- Data science tools
- Complete documentation setup

### API (`api`)

Focused on building web APIs:

- FastAPI with uvicorn
- API documentation
- Health check endpoints
- Minimal dependencies

### CLI (`cli`)

Command-line applications:

- Typer for beautiful CLIs
- Rich for enhanced output
- Argument parsing and validation

### Data Science (`data_science`)

Data analysis and ML projects:

- Pandas, NumPy, Matplotlib, Seaborn
- Data processing utilities
- Visualization tools

### Automation (`automation`)

Scripts and automation tools:

- File processing utilities
- Configuration management
- Logging and error handling

### Minimal (`minimal`)

Basic Python package:

- Core dependencies only
- Simple structure
- Easy to extend

## 🛠️ Development Workflow

After generating your project:

```bash
cd your_project

# Set up development environment
just dev-setup

# Run tests
just test

# Check code quality
just check

# Format code
just format

# Start development (if API project)
just serve

# Serve documentation (if enabled)
just docs-serve
```

## 📦 Dependencies

### Core Dependencies (Always Included)

- `pydantic` - Data validation
- `requests` - HTTP client
- `python-dotenv` - Environment variables
- `tqdm` - Progress bars

### Conditional Dependencies

- **API**: `fastapi`, `uvicorn`
- **CLI**: `typer`, `rich`
- **Data Science**: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`


### Development Dependencies

- `pytest`, `pytest-cov` - Testing
- `ruff` - Linting and formatting
- `deptry` - Dependency analysis
- `mkdocs`, `mkdocs-material` - Documentation (if enabled)
- `pre-commit` - Git hooks (if enabled)

## 🔧 Customization

### Adding New Project Types

1. Update `cookiecutter.json` with new project type
2. Add conditional logic in templates
3. Update documentation

### Modifying Dependencies

Edit the `pyproject.toml` template to add/remove dependencies for different project types.

### Custom Hooks

Modify `hooks/post_gen_project.py` to add custom post-generation logic.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different configurations
5. Submit a pull request

## 📄 License

This template is licensed under the MIT License.

## 🙏 Acknowledgments

This template incorporates best practices from:

- [Python Packaging Authority](https://packaging.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Typer](https://typer.tiangolo.com/)
- [Ruff](https://docs.astral.sh/ruff/)
- [uv](https://docs.astral.sh/uv/)

---

**Happy coding!** 🐍✨
