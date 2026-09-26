import os
import re
import json

directory = 'content/quantum-observable-universe/mass-theory'
pattern = re.compile(r'\b(float64|probe|dps|mpmath|numerical(?:ly)?|curve\s*fit(?:ting)?|script|\.py)\b', re.IGNORECASE)

results = {}

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        matches = []
        for i, line in enumerate(lines):
            if pattern.search(line):
                matches.append({"line_number": i + 1, "content": line.strip()})
        
        if matches:
            results[filename] = matches

with open('.gemini/scratch_matches.json', 'w') as f:
    json.dump(results, f, indent=2)
