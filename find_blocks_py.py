import re
import os

with open('/Users/litlfred/space_cats/qou/lean-qa-report.md', 'r') as f:
    lines = f.readlines()

blocks = []
for line in lines:
    if "proof-statement-integrity" in line or "proof-no-self-assuming-projection" in line:
        match = re.search(r'`(prop|lem|thm|cor|def|rem|prf|ex|conj|fig):([^`]+)`', line)
        if match:
            blocks.append(match.group(2))

print(f"Found {len(blocks)} blocks")

lean_files = []
for root, dirs, files in os.walk('/Users/litlfred/space_cats/qou'):
    for file in files:
        if file.endswith('.lean'):
            lean_files.append(os.path.join(root, file))

results = {}
for block in blocks:
    snake_case = block.replace('-', '_')
    camel_case = ''.join(word.capitalize() for word in block.split('-'))
    patterns = [
        f"theorem {snake_case}", f"lemma {snake_case}", f"def {snake_case}",
        f"theorem {camel_case}", f"lemma {camel_case}", f"def {camel_case}"
    ]
    
    found = False
    for fpath in lean_files:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                for pat in patterns:
                    if pat in content:
                        results[block] = fpath
                        found = True
                        break
        except Exception:
            pass
        if found:
            break
            
for b, f in results.items():
    print(f"{b}: {f}")

