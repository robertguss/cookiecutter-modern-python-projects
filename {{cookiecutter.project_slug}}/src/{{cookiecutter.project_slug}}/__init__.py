from importlib.metadata import version

__version__ = version("{{ cookiecutter.project_slug }}")
__all__ = ["__version__"]
