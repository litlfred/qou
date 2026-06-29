import json
import os
import hashlib

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

root_dir = 'content/quantum-observable-universe'
modified_count = 0

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.qa.json'):
            qa_path = os.path.join(subdir, file)
            base = qa_path[:-8]
            md_path = base + '.md'
            
            with open(qa_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON: {qa_path}")
                    continue
            
            md_hash = get_hash(md_path)
            
            if not md_hash:
                continue
                
            old_hash = data.get('source_hashes', {}).get('md')
            
            if old_hash != md_hash:
                print(f"Drift detected in {qa_path}: {old_hash} -> {md_hash}")
                
                # Update the hash
                if 'source_hashes' not in data:
                    data['source_hashes'] = {}
                data['source_hashes']['md'] = md_hash
                
                # Clean up stale criteria
                if 'criteria' in data:
                    new_criteria = {}
                    for crit, entries in data['criteria'].items():
                        new_entries = [e for e in entries if e.get('field_hash', {}).get('md') == md_hash]
                        if new_entries:
                            new_criteria[crit] = new_entries
                    data['criteria'] = new_criteria
                    
                with open(qa_path, 'w') as f:
                    json.dump(data, f, indent=2)
                
                modified_count += 1

print(f"Refreshed {modified_count} stale sidecars.")
