#!/usr/bin/env python3
import os
import re

def parse_md_file(filepath):
    metadata = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract id: Usually first line or first heading
    id_match = re.search(r'^\s*id:\s*([^\s]+)', content, re.MULTILINE)
    if not id_match:
        # Try to find {#...}
        id_match = re.search(r'\{#([^\}]+)\}', content)
        if not id_match:
            # Fallback to filename without extension
            base = os.path.basename(filepath)
            metadata['id'] = os.path.splitext(base)[0]
        else:
            metadata['id'] = id_match.group(1)
    else:
        metadata['id'] = id_match.group(1)
        
    # Extract tier
    tier_match = re.search(r'^\s*tier:\s*([^\s]+)', content, re.MULTILINE)
    if tier_match:
        metadata['tier'] = tier_match.group(1).strip()
    else:
        metadata['tier'] = 'none'
        
    # Extract dependencies
    deps = set()
    for m in re.finditer(r'\[([^\]]+)\]\([^\)]+\)', content):
        # basic link heuristic, maybe dependencies are formatted as links to other markdown files
        pass
    
    # Actually dependencies are usually marked like `ref:prop:something` or in a specific list.
    # Let's just find all references `def:.*`, `prop:.*`, `thm:.*`, `conj:.*`, `lem:.*`
    refs = re.findall(r'(def:[^\s\)\}]+|prop:[^\s\)\}]+|thm:[^\s\)\}]+|conj:[^\s\)\}]+|lem:[^\s\)\}]+)', content)
    metadata['refs'] = set(refs)
    
    # Also check if the id itself is a conjecture
    if 'conj:' in metadata['id']:
        pass
        
    return metadata

def main():
    root_dir = '/home/litlfred/space_cats/qou/content/quantum-observable-universe'
    all_blocks = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith('.md'):
                path = os.path.join(dirpath, f)
                try:
                    meta = parse_md_file(path)
                    all_blocks[meta['id']] = meta
                except Exception as e:
                    pass

    # Find the 13 conj blocks
    conjs = [b for b, meta in all_blocks.items() if b.startswith('conj:')]
    print(f"Found {len(conjs)} conjectures.")
    
    # We want to see how many "provable" blocks (tier:E, tier:S, tier:keystone) depend on each conjecture.
    # We will build a reverse dependency graph.
    rev_deps = {c: set() for c in conjs}
    for bid, meta in all_blocks.items():
        if bid.startswith('conj:'):
            continue
        
        # Consider a block 'provable' if it has a tier or is a prop/thm/lem
        is_provable = (meta['tier'] in ['E', 'S', 'keystone']) or bid.startswith(('prop:', 'thm:', 'lem:'))
        
        for ref in meta['refs']:
            if ref in rev_deps:
                rev_deps[ref].add(bid)

    print("\nConjecture Triage (Sorted by # of direct dependents):")
    sorted_conjs = sorted(rev_deps.items(), key=lambda x: len(x[1]), reverse=True)
    for c, deps in sorted_conjs:
        print(f"{c}: {len(deps)} dependents")
        if len(deps) > 0:
            # Just print a few dependents
            print(f"  -> {', '.join(list(deps)[:5])}")
            
if __name__ == '__main__':
    main()
