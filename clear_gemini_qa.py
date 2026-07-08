import json
import glob
import os

target_models = ['gemini-3.1-pro']

cleared_count = 0
for f in glob.glob("content/**/*.qa.json", recursive=True):
    try:
        with open(f) as fp:
            data = json.load(fp)
    except:
        continue
        
    modified = False
    
    for crit_name, entries in data.get("criteria", {}).items():
        new_entries = []
        for entry in entries:
            rev = entry.get("reviewer", {})
            if rev.get("kind") == "agent" and rev.get("agent_model") in target_models:
                modified = True
            else:
                new_entries.append(entry)
        data["criteria"][crit_name] = new_entries
                
    if modified:
        with open(f, "w") as fp:
            json.dump(data, fp, indent=2)
        cleared_count += 1

print(f"Cleared gemini-3.1-pro reviews from {cleared_count} files.")
