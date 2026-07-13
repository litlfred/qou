import re
import os

with open('/Users/litlfred/space_cats/qou/lean-qa-report.md', 'r') as f:
    lines = f.readlines()

blocks = set()
for line in lines:
    if "proof-statement-integrity" in line or "proof-no-self-assuming-projection" in line:
        match = re.search(r'`(prop|lem|thm|cor|def|rem|prf|ex|conj|fig):([^`]+)`', line)
        if match:
            blocks.add(match.group(2))

print(f"Found {len(blocks)} blocks")
for block in blocks:
    # convert kebab-case to snake_case for lean files
    snake_case = block.replace('-', '_')
    res = os.popen(f"find /Users/litlfred/space_cats/qou -name '{block}.lean' -o -name '{snake_case}.lean'").read().strip()
    if res:
        for f in res.split('\n'):
            print(f)
    else:
        # maybe search inside files
        pass

