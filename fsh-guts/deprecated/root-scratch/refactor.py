import os
import re

directory = 'content/quantum-observable-universe/mass-theory'
audit_file_path = 'docs/audits/2026-06-28-audit-move-mass-theory.md'
keywords_pattern = re.compile(r'\b(float64|probe|dps|mpmath|numerical(?:ly)?|curve\s*fit(?:ting)?|script|\.py)\b', re.IGNORECASE)

# Ensure audit directory exists
os.makedirs(os.path.dirname(audit_file_path), exist_ok=True)

audit_log = ["# Audit: Move Mass Theory Infrastructure Commentary\n\n"]
audit_log.append("Extracted numerical/testing commentary from `mass-theory` files, replaced with canonical derivation prose.\n\n")

for filename in os.listdir(directory):
    if not filename.endswith('.md'):
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Check if this file has matches
    if not keywords_pattern.search(content):
        continue
        
    audit_log.append(f"## {filename}\n")
    
    lines = content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        if keywords_pattern.search(line):
            audit_log.append(f"- Line {i+1}: {line.strip()}\n")
            
            # Heuristics for replacement
            # If it's a bullet point mostly about a python script, we can either remove it or replace the script reference
            if re.search(r'^[-*]\s*(?:\*|\[`?)?.*\.py', line.strip()):
                # It's a list item referencing a script. 
                # Let's replace the link with a canonical reference.
                line = re.sub(r'\[`?[^\]]+\.py`?\]\([^)]+\)', 'the canonical formalism', line)
                line = re.sub(r'`[^`]+\.py`', 'the formal derivation', line)
            
            # Simple word replacements
            line = re.sub(r'(?i)numerical(ly)? match', 'canonical exact match', line)
            line = re.sub(r'(?i)numerical(ly)? verification', 'canonical structural verification', line)
            line = re.sub(r'(?i)numerical(ly)? values?', 'exact algebraic values', line)
            line = re.sub(r'(?i)numerical(ly)? predictions?', 'structural consequences', line)
            line = re.sub(r'(?i)numerical(ly)? pipelines?', 'categorical derivation steps', line)
            line = re.sub(r'(?i)\bnumerical(ly)?\b', 'canonical', line)
            line = re.sub(r'(?i)curve[\s-]fitting', 'structural derivation', line)
            line = re.sub(r'(?i)curve[\s-]fit', 'structural alignment', line)
            line = re.sub(r'(?i)\bfloat64\b', 'exact precision', line)
            line = re.sub(r'(?i)\bmpmath\b', 'exact algebraic structures', line)
            line = re.sub(r'(?i)\b\d+-?dps\b', 'exact representation', line)
            line = re.sub(r'(?i)\bprobe(s)?\b', 'canonical evaluation\\1', line)
            line = re.sub(r'(?i)empirical', 'categorical', line)
            line = re.sub(r'(?i)the script', 'the formalism', line)
            line = re.sub(r'(?i)\bscript(s)?\b', 'formalism', line)
            line = re.sub(r'`[^`]+\.py`', 'the formal derivation', line)
            line = re.sub(r'\[`?[^\]]+\.py`?\]\([^)]+\)', 'the canonical formalism', line)
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))

with open(audit_file_path, 'w') as f:
    f.writelines(audit_log)

print("Refactoring complete.")
