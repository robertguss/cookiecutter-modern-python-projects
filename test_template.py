#!/usr/bin/env python3

import subprocess
import tempfile
import shutil
from pathlib import Path
import json

def test_cookiecutter_template():
    """Test the cookiecutter template with different configurations."""
    
    template_dir = Path(__file__).parent
    
    test_configs = [
        {
            "project_name": "Test Scripts Project",
        }
    ]
    
    for i, config in enumerate(test_configs):
        print(f"\n🧪 Testing configuration {i+1}: {config['project_name']}")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Create a temporary cookiecutter config
            config_file = temp_path / "cookiecutter.json"
            
            # Load the default config and update with test values
            default_config = json.loads((template_dir / "cookiecutter.json").read_text())
            default_config.update(config)
            
            config_file.write_text(json.dumps(default_config, indent=2))
            
            try:
                # Run cookiecutter with no input (use defaults)
                result = subprocess.run([
                    "cookiecutter", 
                    str(template_dir),
                    "--output-dir", str(temp_path),
                    "--no-input",
                    "--config-file", str(config_file)
                ], capture_output=True, text=True, check=True)
                
                project_slug = config["project_name"].lower().replace(" ", "_")
                project_path = temp_path / project_slug
                
                if project_path.exists():
                    print(f"✅ Project generated successfully at {project_path}")
                    
                    # Check key files exist
                    key_files = ["pyproject.toml", "justfile", "README.md"]
                    for file in key_files:
                        if (project_path / file).exists():
                            print(f"  ✅ {file} exists")
                        else:
                            print(f"  ❌ {file} missing")
                    
                    # Check scripts-specific files
                    cli_file = project_path / "src" / project_slug / "cli" / "__init__.py"
                    if cli_file.exists():
                        print("  ✅ CLI module exists")
                    else:
                        print("  ❌ CLI module missing")
                    
                    scripts_dir = project_path / "scripts"
                    if scripts_dir.exists():
                        print("  ✅ Scripts directory exists")
                    else:
                        print("  ❌ Scripts directory missing")
                
                else:
                    print(f"❌ Project not generated")
                    
            except subprocess.CalledProcessError as e:
                print(f"❌ Cookiecutter failed: {e}")
                print(f"   stdout: {e.stdout}")
                print(f"   stderr: {e.stderr}")

if __name__ == "__main__":
    print("🧪 Testing cookiecutter template...")
    test_cookiecutter_template()
    print("\n✅ Template testing complete!")
