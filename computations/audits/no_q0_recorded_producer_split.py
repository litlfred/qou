#!/usr/bin/env python3
"""Split the no-q0-recorded witnesses: does the PRODUCER read q0 at all?

Pure static inspection; no arithmetic, so NO-FLOAT64 is satisfied vacuously.
Reports file-local AND one-hop-import-cone, because a file-local grep
undercounts (a producer can read q0 through a helper).
"""
import json, re, subprocess, pathlib, collections, sys

ROOT = pathlib.Path("/home/user/qou")
MU, PR = "1.109978595", "1.1099785827"
Q0F = ("q_0_50dps", "q0", "q_0", "q0_50dps")

tracked = subprocess.run(["git","ls-files","computations","tools"],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
wits = [f for f in tracked if f.endswith(".witness.json") and "_deprecated" not in f]
pys  = [f for f in tracked if f.endswith(".py")]

# stem -> paths, preferring NON-deprecated (the trap that bit terms_2_3 earlier)
by_stem = collections.defaultdict(list)
for f in pys:
    by_stem[pathlib.Path(f).stem].append(f)
for k in by_stem:
    by_stem[k].sort(key=lambda p: ("_deprecated" in p, len(p)))

def has_q0_value(o, depth=0):
    if depth > 8: return False
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, (str, int, float)):
                s = str(v)
                if s.startswith(MU) or s.startswith(PR): return True
            elif has_q0_value(v, depth+1): return True
    elif isinstance(o, list):
        for v in o:
            if has_q0_value(v, depth+1): return True
    return False

# signals that a module reads q0
READ = re.compile(r"""(
    from\s+q_parameter\s+import | import\s+q_parameter |
    qou_substrate\.constants | from\s+\.constants\s+import |
    \bq_at\s*\( | \bq_muon_at\s*\( | \bQ_50_DIGIT_STR\b | \bQ_MUON\b | \bQ_MP\b |
    load_q_50dps | q-pinning-50-digit | _q0_value_for_anchor |
    1\.109978595
)""", re.X)
IMPORT = re.compile(r"^\s*(?:from\s+([A-Za-z_][\w.]*)\s+import|import\s+([A-Za-z_][\w.]*))", re.M)

import ast
src_cache = {}
def src(p):
    """CODE ONLY: comments and docstrings stripped.

    A raw read matched `from q_parameter import Q` inside _path_bridge.py's
    USAGE DOCSTRING and reported 536 producers as reading q0 through it. It is
    a path resolver (`witness_path`); it reads no q0. Measure the code.
    """
    if p not in src_cache:
        try:
            raw = (ROOT/p).read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(raw)
            for node in ast.walk(tree):
                if isinstance(node, (ast.Module, ast.FunctionDef,
                                     ast.AsyncFunctionDef, ast.ClassDef)):
                    b = getattr(node, "body", None)
                    if b and isinstance(b[0], ast.Expr) and \
                       isinstance(b[0].value, ast.Constant) and \
                       isinstance(b[0].value.value, str):
                        b.pop(0)          # drop the docstring
            src_cache[p] = ast.unparse(tree)
        except Exception:
            src_cache[p] = ""             # unparseable -> no claim
    return src_cache[p]

def reads_local(p): return bool(READ.search(src(p)))

def one_hop(p):
    """Any locally-resolvable import of p that itself reads q0."""
    hits = []
    for m in IMPORT.finditer(src(p)):
        mod = (m.group(1) or m.group(2) or "").split(".")[0]
        if not mod or mod in ("os","sys","json","re","math","pathlib","typing",
                              "collections","itertools","functools","argparse",
                              "subprocess","dataclasses","decimal","fractions",
                              "numpy","scipy","sympy","mpmath","time","datetime"):
            continue
        for cand in by_stem.get(mod, []):
            if reads_local(cand): hits.append(mod); break
    return sorted(set(hits))

rows = []
for w in wits:
    try: d = json.loads((ROOT/w).read_text(encoding="utf-8"))
    except Exception: continue
    if "q0Anchor" in d: continue
    if has_q0_value(d): continue                 # records a q0 -> not this population
    sf = d.get("scriptFile") or ""
    stem = pathlib.Path(sf).stem if sf else pathlib.Path(w).name[:-len(".witness.json")].replace("-","_")
    paths = by_stem.get(stem) or by_stem.get(stem.replace("-","_"))
    if not paths:
        rows.append(("UNRESOLVED-PRODUCER", w, stem, [])); continue
    p = paths[0]
    if reads_local(p): rows.append(("READS q0 (file-local)", w, p, []))
    else:
        hop = one_hop(p)
        rows.append((("READS q0 (via import cone)" if hop else "NO q0 READ anywhere"), w, p, hop))

c = collections.Counter(r[0] for r in rows)
print(f"population (unstamped AND recording no q0): {len(rows)}\n")
for k, v in c.most_common(): print(f"  {v:5d}  {k}")

print("\n--- sample: READS q0 via import cone (file-local grep would miss these) ---")
for _, w, p, hop in [r for r in rows if r[0].startswith("READS q0 (via")][:10]:
    print(f"   {p}  <- via {','.join(hop)}")
print("\n--- sample: NO q0 READ anywhere (candidates for q0Anchor: independent) ---")
for _, w, p, _ in [r for r in rows if r[0] == "NO q0 READ anywhere"][:10]:
    print(f"   {p}")
print("\n--- sample: UNRESOLVED PRODUCER ---")
for _, w, s, _ in [r for r in rows if r[0] == "UNRESOLVED-PRODUCER"][:8]:
    print(f"   stem={s}  {w}")
