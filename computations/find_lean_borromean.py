#!/usr/bin/env python3
import os

root_dir = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'
for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith('.lean'):
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if 'BorromeanQuark' in content or 'borromean' in content.lower():
                        print(f"Found in {path}")
            except Exception:
                pass
