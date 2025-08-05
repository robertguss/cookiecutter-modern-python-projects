{% if cookiecutter.include_fastapi == 'y' -%}
from fastapi import FastAPI
from {{ cookiecutter.project_slug }} import __version__

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version=__version__,
)


@app.get("/")
async def root():
    return {"message": "Hello from {{ cookiecutter.project_name }}!", "version": __version__}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": __version__}
{% endif %}
