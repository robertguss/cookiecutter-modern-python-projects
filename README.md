# Modern Python Project Cookiecutter Template

A streamlined cookiecutter template for modern Python projects with opinionated defaults and best practices built-in.

## 🚀 Features

### 🏗️ Six Project Types
Choose from **full**, **api**, **cli**, **data_science**, **scripts**, or **minimal** - each with tailored dependencies and structure.

### 🛠️ Modern Development Stack
- **Python 3.13** - Latest Python version
- **[uv](https://docs.astral.sh/uv/)** - Ultra-fast package management
- **[Ruff](https://docs.astral.sh/ruff/)** - Lightning-fast linting and formatting  
- **[pytest](https://pytest.org/)** - Testing with 80% coverage requirement
- **[just](https://github.com/casey/just)** - Modern task runner
- **[pre-commit](https://pre-commit.com/)** - Quality assurance hooks

### 📚 Documentation Ready
- **[MkDocs](https://www.mkdocs.org/)** with Material theme
- **src/ layout** for clean package structure
- **Type hints** with mypy support


## 📋 Quick Start

### Prerequisites
- Python 3.13+
- [cookiecutter](https://cookiecutter.readthedocs.io/)

### Generate a Project
```bash
# Install cookiecutter
pip install cookiecutter

# Generate your project
cookiecutter https://github.com/yourusername/cookiecutter-modern-python-projects
```

### Simple Configuration
You'll be prompted for just the essentials:
- **Project name** and description  
- **Author** information
- **Project type** (full, api, cli, data_science, scripts, minimal)

That's it! No complex configuration choices - sensible defaults are built-in.

## 📖 Documentation

- **[Project Types Guide](docs/project_types.md)** - Detailed breakdown of each project type
- **[Features Guide](docs/features.md)** - What each feature adds to your project

## 🏗️ Generated Project Structure

```
your_project/
├── src/your_project/           # Source code (src layout)
│   ├── __init__.py
│   ├── cli/                    # CLI commands (if project type includes)
│   ├── api/                    # FastAPI routes (if project type includes)  
│   └── data/                   # Data science utilities (if project type includes)
├── scripts/                    # Scripts and utilities (if project type includes)
│   └── automation/
├── tests/                      # Test files
├── docs/                       # MkDocs documentation
├── pyproject.toml              # Project configuration
├── justfile                    # Task definitions
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .gitignore
└── README.md
```

## 🎯 Project Types Overview

| Type | FastAPI | Typer CLI | Data Science | Scripts |
|------|:-------:|:---------:|:------------:|:-------:|
| `full` | ✅ | ✅ | ✅ | ✅ |
| `api` | ✅ | ❌ | ❌ | ❌ |
| `cli` | ❌ | ✅ | ❌ | ❌ |
| `data_science` | ❌ | ❌ | ✅ | ❌ |
| `scripts` | ❌ | ✅ | ❌ | ✅ |
| `minimal` | ❌ | ❌ | ❌ | ❌ |

See the **[Project Types Guide](docs/project_types.md)** for detailed explanations.

## 🛠️ Development Workflow

After generating your project:

```bash
cd your_project

# Install dependencies
just install

# Run tests
just test

# Check code quality  
just check

# Format code
just format

# Start API server (if API project)
just serve

# Serve documentation
just docs
```

## 🔧 What's Always Included

Every generated project includes:
- **Python 3.13** support
- **Pre-commit hooks** (ruff, mypy, pytest)
- **MkDocs documentation** with Material theme
- **80% test coverage** requirement
- **src/ layout** for clean imports
- **uv** for fast dependency management
- **justfile** for task automation

## 🎨 Customization

This template is designed with opinionated defaults, but you can:
- Modify `cookiecutter.json` to add new project types
- Edit template files in `{{cookiecutter.project_slug}}/`
- Update `hooks/post_gen_project.py` for custom logic

See the **[Features Guide](docs/features.md)** for implementation details.

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
