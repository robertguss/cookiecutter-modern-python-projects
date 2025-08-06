import typer
from rich.console import Console

app = typer.Typer(help="{{ cookiecutter.project_name }} CLI")
console = Console()


@app.command()
def hello(name: str = typer.Option("World", help="Name to greet")):
    console.print(f"Hello {name}! 👋", style="bold green")


@app.command()
def version():
    from {{ cookiecutter.project_slug }} import __version__
    console.print(f"{{ cookiecutter.project_name }} v{__version__}", style="bold blue")


def main():
    app()


if __name__ == "__main__":
    main()
