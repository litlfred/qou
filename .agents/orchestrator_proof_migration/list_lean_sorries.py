import os
import re

lean_dir = "/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU"

# Regex to find sorry statements (not inside comments)
sorry_re = re.compile(r'\bsorry\b')

results = []

for root, dirs, files in os.walk(lean_dir):
    for file in files:
        if file.endswith('.lean'):
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, lean_dir)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            in_block_comment = False
            for idx, line in enumerate(lines):
                # Simple comment tracking
                stripped = line.strip()
                
                # Check block comment start/end
                if '/-' in line:
                    in_block_comment = True
                if '-/' in line:
                    in_block_comment = False
                    continue
                if in_block_comment:
                    continue
                
                if stripped.startswith('--'):
                    continue
                
                # Split at '--' if it's a line comment, but be careful not to split inside strings (approximation)
                if '--' in line:
                    parts = line.split('--')
                    code_part = parts[0]
                else:
                    code_part = line
                
                if sorry_re.search(code_part):
                    # Check if it's a conditional class sorry
                    # Look back to see if we are in a class definition
                    is_class_body = False
                    for prev_idx in range(max(0, idx - 15), idx):
                        prev_line = lines[prev_idx].strip()
                        if prev_line.startswith('class ') or prev_line.startswith('class\n'):
                            is_class_body = True
                            break
                    
                    results.append({
                        'file': rel_path,
                        'line': idx + 1,
                        'content': stripped,
                        'is_class_body': is_class_body
                    })

print(f"Total occurrences found: {len(results)}")
print("First 30 occurrences:")
for r in results[:30]:
    print(f"{r['file']}:{r['line']} -> {r['content']} (ClassBody: {r['is_class_body']})")

import json
with open("/Users/litlfred/space_cats/qou/.agents/orchestrator_proof_migration/sorry_audit.json", "w") as f:
    json.dump(results, f, indent=2)
