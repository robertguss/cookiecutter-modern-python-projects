{% if cookiecutter.project_type in ['full', 'automation'] -%}
from .automation import *
{% endif %}
