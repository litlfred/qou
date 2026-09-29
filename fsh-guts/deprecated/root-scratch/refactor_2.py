import os
import re

directory = 'content/quantum-observable-universe/mass-theory'

for filename in os.listdir(directory):
    if not filename.endswith('.md'):
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace markdown links to python scripts
    # e.g., [`some_script.py`](../../some_script.py) -> the canonical formalism
    # or [the formal derivation](../../some_script.py) -> the canonical formalism
    content = re.sub(r'\[([^\]]+)\]\([^)]+\.py#?[^)]*\)', 'the canonical formalism', content)
    
    # Also catch plain `something.py`
    content = re.sub(r'`[^`]+\.py`', 'the formal derivation', content)
    
    # Catch bare words ending in .py
    content = re.sub(r'\b[\w-]+\.py\b', 'the formal derivation', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Second refactoring complete.")
