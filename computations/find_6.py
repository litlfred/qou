#!/usr/bin/env python3
import os

content_root = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'

targets = [
    'shell-transition-knot',
    'knot-factor-frobenius-pairing',
    'weak-spectral-completeness',
    'magic-numbers-bring',
    'mass-endomorphism',
    'quantum-langlands-dual'
]

found = {t: [] for t in targets}

for dirpath, _, filenames in os.walk(content_root):
    for f in filenames:
        if f.endswith('.lean') or f.endswith('.md'):
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    for t in targets:
                        if t in content:
                            found[t].append(path)
            except Exception:
                pass

for t, paths in found.items():
    print(f"Target: {t}")
    for p in paths:
        print(f"  - {p}")
