import json

path = 'content/quantum-observable-universe/particle-interactions/shell-closure-stability.qa.json'
with open(path) as f:
    data = json.load(f)

# Fix the missing lean path
data['paths']['lean'] = '../qou/content/quantum-observable-universe/lean/QOU/BraidKnot/ShellClosureStability.lean'

# Filter out old fails, keep only the entries for the latest hash
latest_md_hash = data['source_hashes']['md']
for crit, entries in data.get('criteria', {}).items():
    new_entries = []
    for e in entries:
        if e.get('field_hash', {}).get('md') == latest_md_hash:
            if e.get('result') == 'n/a' and 'lean sibling' in e.get('notes', ''):
                # We fixed the lean sibling issue, so drop the n/a or set to pass
                # actually, we can just delete this entry so the qa-checker will re-evaluate it on the next run
                continue
            new_entries.append(e)
    data['criteria'][crit] = new_entries

# Clean up empty criteria
data['criteria'] = {k: v for k, v in data['criteria'].items() if v}

with open(path, 'w') as f:
    json.dump(data, f, indent=2)

