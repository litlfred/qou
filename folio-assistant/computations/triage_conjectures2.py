#!/usr/bin/env python3
import os
import re
from collections import defaultdict

def main():
    root_dir = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'
    conjectures = set()
    dependencies = defaultdict(list)
    
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith('.md'):
                path = os.path.join(dirpath, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                # Look for conditionals like conditional on [`conj:...`](#conj:...)
                for match in re.finditer(r'conditional on \[`(conj:[^`]+)`\]', content):
                    conj = match.group(1)
                    conjectures.add(conj)
                    dependencies[conj].append(f)
                    
                # Also check uses: ["conj:..."]
                for match in re.finditer(r'uses:\s*\[([^\]]+)\]', content):
                    items = match.group(1).split(',')
                    for item in items:
                        item = item.strip().strip('"').strip("'")
                        if item.startswith('conj:'):
                            conjectures.add(item)
                            dependencies[item].append(f)

    print(f"Found {len(conjectures)} conjectures.")
    print("Conjecture Triage (Sorted by # of direct dependents):")
    
    sorted_conjs = sorted(dependencies.items(), key=lambda x: len(x[1]), reverse=True)
    for conj, dependents in sorted_conjs:
        print(f"{conj}: {len(dependents)} dependents")
        for dep in set(dependents):
            print(f"  -> {dep}")
            
if __name__ == '__main__':
    main()
