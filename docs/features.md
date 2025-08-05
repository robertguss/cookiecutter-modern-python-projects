# Features Guide

This document details what each feature adds to your generated project, including files, dependencies, and functionality.

## FastAPI Support

**Enabled for:** `full`, `api` project types

### What Gets Added

**Directory Structure:**
```
src/your_project/
└── api/
    └── __init__.py    # FastAPI app and basic routes
```

**Dependencies:**
- `fastapi>=0.111` - Modern web framework
- `uvicorn[standard]>=0.29` - ASGI server

**Optional Dependency Group:**
```toml
[project.optional-dependencies]
api = ["fastapi>=0.111", "uvicorn[standard]>=0.29"]
```

**Installation:**
```bash
# Install with API dependencies
uv pip install -e ".[api]"

# Or install everything
just install
```

### Usage Example

The generated `api/__init__.py` provides a basic FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI(title="Your Project API")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

**Run the API:**
```bash
# Development server
uvicorn your_project.api:app --reload

# Or using justfile
just serve
```

## Typer Support

**Enabled for:** `full`, `cli`, `automation` project types

### What Gets Added

**Directory Structure:**
```
src/your_project/
└── cli/
    └── __init__.py    # Typer app and commands
```

**Dependencies:**
- `typer>=0.12` - CLI framework
- `rich>=13.0` - Beautiful terminal output

**Console Script:**
```toml
[project.scripts]
your-project-name = "your_project.cli:main"
```

**Optional Dependency Group:**
```toml
[project.optional-dependencies]
cli = ["typer>=0.12", "rich>=13.0"]
```

### Usage Example

The generated `cli/__init__.py` provides a basic CLI application:

```python
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def hello(name: str = "World"):
    console.print(f"Hello {name}!", style="bold green")

def main():
    app()
```

**Use the CLI:**
```bash
# After installation, use your project name
your-project-name hello --name "Alice"

# Or run directly
python -m your_project.cli hello
```

## Data Science Support

**Enabled for:** `full`, `data_science` project types

### What Gets Added

**Directory Structure:**
```
src/your_project/
└── data/
    └── __init__.py    # Data processing utilities
```

**Core Dependencies:**
- `pandas>=2.2` - Always included as main dependency

**Optional Dependencies:**
- `matplotlib>=3.8` - Plotting and visualization
- `seaborn>=0.13` - Statistical visualization
- `polars>=0.20` - Fast DataFrame library
- `scikit-learn>=1.4` - Machine learning
- `numpy>=1.26` - Numerical computing

**Optional Dependency Group:**
```toml
[project.optional-dependencies]
ds = [
    "matplotlib>=3.8",
    "seaborn>=0.13", 
    "polars>=0.20",
    "scikit-learn>=1.4",
    "numpy>=1.26"
]
```

### Usage Example

The generated `data/__init__.py` provides data processing utilities:

```python
import pandas as pd
from pathlib import Path

def load_csv(file_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

def save_csv(df: pd.DataFrame, file_path: str | Path) -> None:
    df.to_csv(file_path, index=False)

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def clean(self) -> pd.DataFrame:
        return self.data.dropna()
    
    def summary(self) -> pd.DataFrame:
        return self.data.describe()
```

**Install with data science tools:**
```bash
uv pip install -e ".[ds]"
```

## Scripts/Automation Support

**Enabled for:** `full`, `automation` project types

### What Gets Added

**Directory Structure:**
```
scripts/
└── automation/
    └── __init__.py    # Automation framework and base classes
```

**Additional Dependencies:**
- `pydantic>=2.0` - Data validation
- `python-dotenv>=1.0` - Environment variable management

### Usage Example

The automation framework provides base classes for building automation scripts:

```python
from scripts.automation import BaseAutomation, AutomationConfig

# Create a custom automation
class MyAutomation(BaseAutomation):
    def execute(self) -> bool:
        self.logger.info("Running my automation...")
        # Your automation logic here
        return True

# Configure and run
config = AutomationConfig(
    name="my_automation",
    description="Does something useful",
    enabled=True
)

automation = MyAutomation(config)
success = automation.run()
```

**Built-in Example:**
The template includes a `FileProcessorAutomation` class that demonstrates:
- File processing workflows
- Logging and error handling
- Configuration management
- Directory operations

## Development Tools (Always Included)

Every project type includes these development tools:

### Pre-commit Hooks
- **ruff** - Linting and formatting
- **mypy** - Type checking  
- **pytest** - Test runner

### Documentation
- **MkDocs** with Material theme
- Auto-generated API docs
- Development guide

### Testing
- **pytest** with coverage reporting
- **80% coverage requirement**
- Test structure in `tests/` directory

### Task Automation
- **justfile** with common tasks:
  - `just install` - Install dependencies
  - `just test` - Run tests
  - `just lint` - Lint code
  - `just format` - Format code
  - `just docs` - Serve documentation
  - `just clean` - Clean build artifacts

### Package Management
- **uv** for fast dependency resolution
- **pyproject.toml** configuration (PEP 621)
- **src/ layout** for clean imports
