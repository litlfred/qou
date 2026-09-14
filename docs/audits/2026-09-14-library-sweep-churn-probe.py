#!/usr/bin/env python3
"""Does the library sweep's mtime term inflate its dirty closure?

MEASURED FALSE, 2026-09-14: 7 of 2563. See bean qou-8jjo.
Run from the repo root; reads only, writes nothing."""
import subprocess, pathlib
ROOT = pathlib.Path(subprocess.run(["git","rev-parse","--show-toplevel"],
                                   capture_output=True, text=True, check=True).stdout.strip())
PKG  = ROOT/"content/quantum-observable-universe/lean"
OLE  = PKG/".lake/build/lib/lean"
srcs = sorted(PKG.glob("QOU/**/*.lean")) + sorted(PKG.glob("QOU.lean"))
mod2path = {}
for p in srcs:
    rel = p.relative_to(PKG)
    mod2path[str(rel)[:-5].replace("/", ".")] = p

# last-commit date per file, one git call
out = subprocess.run(["git","log","--format=%H %ct","--name-only","--","content/quantum-observable-universe/lean/QOU"],
                     cwd=ROOT, capture_output=True, text=True).stdout
last = {}
ct = None
for line in out.splitlines():
    if not line.strip():
        continue
    if " " in line and len(line.split()[0]) == 40:
        ct = int(line.split()[1]); continue
    if line.endswith(".lean") and line not in last:
        last[line] = ct

# which files are clean vs HEAD
dirty_wt = set(subprocess.run(["git","status","--porcelain","--","content/quantum-observable-universe/lean/QOU"],
               cwd=ROOT, capture_output=True, text=True).stdout.split())

changed_now = changed_strict = never = 0
churn = []
for m, p in mod2path.items():
    o = OLE/(m.replace(".","/")+".olean")
    if not o.exists():
        never += 1; continue
    rel = str(p.relative_to(ROOT))
    c = last.get(rel)
    mt = p.stat().st_mtime
    om = o.stat().st_mtime
    src_now = max(c, mt) if c is not None else None
    is_clean_wt = rel not in dirty_wt
    src_strict = c if (is_clean_wt and c is not None) else src_now
    if src_now is None or src_now > om: changed_now += 1
    if src_strict is None or src_strict > om:
        changed_strict += 1
    elif src_now is None or src_now > om:
        churn.append((m, c, mt, om))
print(f"modules with olean      : {len(mod2path)-never}")
print(f"never built             : {never}")
print(f"changed (CURRENT rule)  : {changed_now}")
print(f"changed (mtime-only-when-worktree-dirty): {changed_strict}")
print(f"=> pure mtime churn     : {len(churn)}")
