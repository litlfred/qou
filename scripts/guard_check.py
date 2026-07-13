import subprocess
import sys
import re

def check_file(filepath):
    if not filepath.endswith('.md'):
        print(f"Reverting {filepath} (not .md)")
        return False
    
    # Check >200-line delta
    try:
        diff_out = subprocess.check_output(['git', 'diff', '--numstat', filepath], text=True).strip()
        if diff_out:
            added, deleted, _ = diff_out.split('\t')
            if int(added) > 200 or int(deleted) > 200:
                print(f"Reverting {filepath} (>200 line delta)")
                return False
    except:
        pass
        
    # Check diagram/eqn/anchor deletion
    try:
        diff_text = subprocess.check_output(['git', 'diff', '-U0', filepath], text=True)
        for line in diff_text.splitlines():
            if line.startswith('-') and not line.startswith('---'):
                if '$$' in line or '\\begin' in line or '```mermaid' in line or '{#' in line:
                    print(f"Reverting {filepath} (math/diagram/anchor deletion)")
                    return False
    except:
        pass
        
    return True

modified = subprocess.check_output(['git', 'status', '--porcelain'], text=True).splitlines()
to_commit = []
for line in modified:
    if line.startswith(' M ') or line.startswith('M '):
        filepath = line[3:].strip()
        if filepath.startswith('"') and filepath.endswith('"'):
            filepath = filepath[1:-1]
        
        if filepath.startswith('content/'):
            if check_file(filepath):
                to_commit.append(filepath)
            else:
                subprocess.call(['git', 'checkout', '--', filepath])

# Output the valid files
for f in to_commit:
    print(f)
