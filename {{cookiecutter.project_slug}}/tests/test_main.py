import pytest
from {{ cookiecutter.project_slug }} import __version__


def test_version():
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_version_format():
    parts = __version__.split(".")
    assert len(parts) >= 2
    for part in parts:
        assert part.isdigit() or any(c.isdigit() for c in part)
