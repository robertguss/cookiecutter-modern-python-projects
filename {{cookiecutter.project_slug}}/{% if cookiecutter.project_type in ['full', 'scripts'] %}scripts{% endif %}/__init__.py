{% if cookiecutter.project_type in ['full', 'scripts'] -%}
from .automation import *
{% endif %}
