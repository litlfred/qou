#!/usr/bin/env python3
"""Per-module dirty closure for the QOU library: a module is DIRTY if its source's
last commit is newer than its olean, or the olean is missing, or any import is
dirty. Prints the dirty modules in topological order (deps first).

Run from content/quantum-observable-universe/lean after
  git log --since=<date well before the cache seed> --format=%ct --name-only origin/main \
      -- content/quantum-observable-universe/lean/QOU > /tmp/src_times.txt
and with /tmp/full_topo_all.txt holding the full topological order of QOU/**.
Measured 2026-09-04: 158 of 2,597 (63 source-newer, 52 missing, 43 dependents),
against 1,494 for a single seed-commit criterion — the difference is the 25
Pauli-witness modules at 10+ min each, whose sources predate their oleans."""
import os, sys
last = {}; t = None
for l in open('/tmp/src_times.txt'):
    l = l.rstrip('\n')
    if not l: continue
    if l.isdigit(): t = int(l); continue
    if l.endswith('.lean') and l.startswith('content/quantum-observable-universe/lean/QOU/'):
        m = l[len('content/quantum-observable-universe/lean/'):-5].replace('/', '.')
        last[m] = max(last.get(m, 0), t)
order = [l.strip() for l in open('/tmp/full_topo_all.txt') if l.strip()]
mods = {}
for m in order:
    p = m.replace('.', '/') + '.lean'
    mods[m] = [l.split()[1] for l in open(p, errors='ignore') if l.startswith('import QOU')] if os.path.exists(p) else []
dirty = set(); reasons = {'src-newer': 0, 'missing': 0, 'dep': 0}
for m in order:
    o = '.lake/build/lib/lean/' + m.replace('.', '/') + '.olean'
    if not os.path.exists(o): dirty.add(m); reasons['missing'] += 1; continue
    if last.get(m, 0) > os.path.getmtime(o): dirty.add(m); reasons['src-newer'] += 1; continue
    if any(d in dirty for d in mods[m]): dirty.add(m); reasons['dep'] += 1
sys.stderr.write(f"dirty {len(dirty)} of {len(order)}: {reasons}\n")
print('\n'.join(m for m in order if m in dirty))
