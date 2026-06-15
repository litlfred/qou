#!/usr/bin/env python3
import os

repo_root = '/home/litlfred/space_cats/qou'
content_root = os.path.join(repo_root, 'content/quantum-observable-universe')
lean_root = os.path.join(content_root, 'lean')

orphaned = []
for dirpath, _, filenames in os.walk(content_root):
    # skip lean_root entirely
    if dirpath.startswith(lean_root):
        continue
    for f in filenames:
        if f.endswith('.lean'):
            path = os.path.join(dirpath, f)
            orphaned.append(path)

for path in orphaned:
    print(path)
