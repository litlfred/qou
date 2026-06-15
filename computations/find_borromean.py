#!/usr/bin/env python3
import os
import re

root_dir = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'
for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith('.md'):
            path = os.path.join(dirpath, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                if 'id: conj:borromean-quark' in content or 'conj:borromean-quark}' in content:
                    print(f"Found in {path}")
