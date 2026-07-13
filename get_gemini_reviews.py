import json
import glob
import os

target_models = ['gemini-3.1-pro']
target_kinds = ['milnor', 'milnor-section', 'milnor-sub-section']

gemini_count = 0
milnor_count = 0
total = 0

for f in glob.glob("content/**/*.qa.json", recursive=True):
    try:
        with open(f) as fp:
            data = json.load(fp)
    except:
        continue
        
    kind = data.get("kind", "")
    
    is_milnor = kind in target_kinds
    is_gemini = False
    
    for crit_name, entries in data.get("criteria", {}).items():
        for entry in entries:
            rev = entry.get("reviewer", {})
            if rev.get("kind") == "agent" and rev.get("agent_model") in target_models:
                is_gemini = True
                
    if is_milnor:
        milnor_count += 1
    if is_gemini:
        gemini_count += 1
    if is_milnor or is_gemini:
        total += 1

print(f"Total files: {total}")
print(f"Gemini files: {gemini_count}")
print(f"Milnor files: {milnor_count}")
