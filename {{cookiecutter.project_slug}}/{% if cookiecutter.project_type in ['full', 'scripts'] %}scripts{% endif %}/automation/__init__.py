{% if cookiecutter.project_type in ['full', 'scripts'] -%}
import logging
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
from python_dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class AutomationConfig(BaseModel):
    name: str
    description: str
    enabled: bool = True
    schedule: str | None = None
    config: Dict[str, Any] = {}


class BaseAutomation:
    def __init__(self, config: AutomationConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{config.name}")
    
    def run(self) -> bool:
        if not self.config.enabled:
            self.logger.info(f"Automation {self.config.name} is disabled")
            return False
        
        try:
            self.logger.info(f"Starting automation: {self.config.name}")
            result = self.execute()
            self.logger.info(f"Automation {self.config.name} completed successfully")
            return result
        except Exception as e:
            self.logger.error(f"Automation {self.config.name} failed: {e}")
            return False
    
    def execute(self) -> bool:
        raise NotImplementedError("Subclasses must implement execute method")


class FileProcessorAutomation(BaseAutomation):
    def execute(self) -> bool:
        input_dir = Path(self.config.config.get("input_dir", "data/input"))
        output_dir = Path(self.config.config.get("output_dir", "data/output"))
        
        if not input_dir.exists():
            self.logger.warning(f"Input directory {input_dir} does not exist")
            return False
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        processed_count = 0
        for file_path in input_dir.glob("*.txt"):
            self.process_file(file_path, output_dir)
            processed_count += 1
        
        self.logger.info(f"Processed {processed_count} files")
        return processed_count > 0
    
    def process_file(self, input_path: Path, output_dir: Path) -> None:
        output_path = output_dir / f"processed_{input_path.name}"
        content = input_path.read_text()
        processed_content = content.upper()  # Example processing
        output_path.write_text(processed_content)
{% endif %}
