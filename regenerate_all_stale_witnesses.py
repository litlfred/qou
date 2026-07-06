import re
import subprocess
from pathlib import Path
import sys

def main():
    log_file = "/Users/litlfred/.gemini/antigravity-cli/brain/c54c2f03-e279-4f0f-8324-fb96d717d7ce/.system_generated/tasks/task-6640.log"
    content = Path(log_file).read_text()
    
    # Regex to find: (producer script_name.py):
    pattern = re.compile(r"\(producer ([a-zA-Z0-9_\-\.]+)\):")
    
    scripts = set(pattern.findall(content))
    print(f"Found {len(scripts)} unique producer scripts to run.")
    
    # Find the actual paths of these scripts in computations/
    # Some might be in subdirectories of computations/
    script_paths = {}
    computations_dir = Path("computations")
    for py_file in computations_dir.rglob("*.py"):
        script_paths[py_file.name] = str(py_file)
        
    failed = []
    success = []
    
    for script_name in scripts:
        if script_name in script_paths:
            path = script_paths[script_name]
            print(f"Running {path}...")
            # We don't want to use tee, we just want to run it. 
            # We'll use subprocess.run and capture output in case of failure.
            res = subprocess.run(["python3", path], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"FAILED: {path}")
                failed.append(path)
            else:
                print(f"SUCCESS: {path}")
                success.append(path)
        else:
            print(f"WARNING: Script {script_name} not found in computations/")
            failed.append(script_name)
            
    print(f"\nSummary: {len(success)} succeeded, {len(failed)} failed.")
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
