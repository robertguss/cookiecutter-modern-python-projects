# CLI Reference

{{ cookiecutter.project_name }} includes a command-line interface built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).

## Available Commands

### Hello Command

Greet someone with a friendly message.

```bash
python -m {{ cookiecutter.project_slug }}.cli hello
python -m {{ cookiecutter.project_slug }}.cli hello --name "Alice"
```

### Version Command

Display the current version of {{ cookiecutter.project_name }}.

```bash
python -m {{ cookiecutter.project_slug }}.cli version
```

## Usage Examples

```bash
# Basic greeting
python -m {{ cookiecutter.project_slug }}.cli hello
# Output: Hello World! 👋

# Custom greeting
python -m {{ cookiecutter.project_slug }}.cli hello --name "Developer"
# Output: Hello Developer! 👋

# Check version
python -m {{ cookiecutter.project_slug }}.cli version
# Output: {{ cookiecutter.project_name }} v0.1.0
```

## Adding New Commands

To add new CLI commands, edit `src/{{ cookiecutter.project_slug }}/cli/__init__.py`:

```python
@app.command()
def my_command(arg: str = typer.Option(..., help="Description")):
    """My custom command."""
    console.print(f"Running command with: {arg}", style="bold green")
```

## Help

Get help for any command:

```bash
python -m {{ cookiecutter.project_slug }}.cli --help
python -m {{ cookiecutter.project_slug }}.cli hello --help
```
