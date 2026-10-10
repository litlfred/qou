import re
import os
import subprocess

with open('/Users/litlfred/space_cats/qou/lean-qa-report.md', 'r') as f:
    lines = f.readlines()

blocks = []
for line in lines:
    if "proof-statement-integrity" in line or "proof-no-self-assuming-projection" in line:
        match = re.search(r'`(prop|lem|thm|cor|def|rem|prf|ex|conj|fig):([^`]+)`', line)
        if match:
            blocks.append(match.group(2))

print(f"Found {len(blocks)} blocks")
for block in blocks:
    # convert kebab-case to snake_case and camelCase
    snake_case = block.replace('-', '_')
    camel_case = ''.join(word.capitalize() for word in block.split('-'))
    
    # search using rg to find lean files containing the theorem/lemma definition
    cmd = f"rg -l 'theorem {snake_case}|lemma {snake_case}|def {snake_case}|theorem {camel_case}|lemma {camel_case}|def {camel_case}' /Users/litlfred/space_cats/qou/content/quantum-observable-universe/**/*.lean"
    try:
        res = subprocess.check_output(cmd, shell=True, text=True).strip()
        if res:
            for f in res.split('\n'):
                print(f"{block}: {f}")
    except subprocess.CalledProcessError:
        pass

