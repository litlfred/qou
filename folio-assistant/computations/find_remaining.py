#!/usr/bin/env python3
import os

content_root = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'

targets = ['palindromicity-orbital-type', 'shell-closure-nf-term-count', 'PalindromicityOrbitalType', 'ShellClosureNfTermCount']

for dirpath, _, filenames in os.walk(content_root):
    for f in filenames:
        if f.endswith('.lean'):
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    for t in targets:
                        if t in content:
                            print(f"Found {t} in {path}")
                            break
            except Exception:
                pass
