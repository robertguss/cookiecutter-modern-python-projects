import pytest
from pathlib import Path
import tempfile
import shutil
{% if cookiecutter.include_data_science == 'y' -%}
import pandas as pd
{% endif %}


@pytest.fixture
def temp_dir():
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_text_file(temp_dir):
    file_path = temp_dir / "sample.txt"
    file_path.write_text("Hello, World!\nThis is a test file.")
    return file_path


{% if cookiecutter.include_data_science == 'y' -%}
@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age": [25, 30, 35, None, 45],
        "city": ["New York", "London", "Paris", "Tokyo", "Sydney"]
    })


@pytest.fixture
def sample_csv_file(temp_dir, sample_dataframe):
    file_path = temp_dir / "sample.csv"
    sample_dataframe.to_csv(file_path, index=False)
    return file_path
{% endif %}


{% if cookiecutter.include_fastapi == 'y' -%}
@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from {{ cookiecutter.project_slug }}.api import app
    
    return TestClient(app)
{% endif %}
