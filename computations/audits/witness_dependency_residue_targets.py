#!/usr/bin/env python3
"""qou-wlaf residue: re-run producers whose import cone reaches the mpf-ified
word builder, and report which committed witnesses actually MOVE.

Discipline (all of it bought by earlier failures, see qou-wlaf/qou-9ohz):
  * pinned to ONE main SHA, recorded in the output
  * detector self-tests against a known positive before any count is trusted
  * baseline read from GIT, never from the tree this script is mutating
  * whole computations/ tree restored between runs (producers write siblings)
  * stdout captured as well as stderr; traceback checked, not exit code
  * volatile keys masked or we measure the clock, not the corpus
"""
import ast, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/user/qou")
COMP = ROOT / "computations"
SHA = subprocess.check_output(["git","rev-parse","origin/main"],cwd=ROOT,text=True).strip()
TARGET = {"atom_braid_word_3A", "per_generator_V_hat_3A"}
VOLATILE = {"timestamp","elapsed_seconds","measured_at","start_time_monotonic",
            "computedAt","durationMs","elapsed_sec","invocation","environment",
            "scriptCommitSha","commitSha"}

def importers():
    out=set()
    for p in ROOT.rglob("*.py"):
        if "_deprecated" in p.parts: continue
        try: tree=ast.parse(p.read_text(errors="ignore"))
        except Exception: continue
        for n in ast.walk(tree):
            if isinstance(n,ast.ImportFrom) and n.module and "mass_at_3A_proper" in n.module:
                if any(a.name in TARGET for a in n.names): out.add(p.stem)
            if isinstance(n,ast.Import):
                for a in n.names:
                    if "mass_at_3A_proper" in a.name: out.add(p.stem)
    return out

def witnesses(imp):
    hits=[]
    for w in ROOT.rglob("*.witness.json"):
        try: d=json.loads(w.read_text())
        except Exception: continue
        sf=d.get("scriptFile") or (d.get("witness") or {}).get("scriptFile") or ""
        if sf and Path(sf).stem in imp: hits.append((w, Path(sf).stem))
    return hits

def strip(o):
    if isinstance(o,dict): return {k:strip(v) for k,v in o.items() if k not in VOLATILE}
    if isinstance(o,list): return [strip(v) for v in o]
    return o

imp = importers()
hits = witnesses(imp)
known = [h for h in hits if h[0].name == "gram-norm-binding-probe.witness.json"]
print(f"PINNED main SHA : {SHA}")
print(f"importers       : {len(imp)}")
print(f"witnesses       : {len(hits)}")
print(f"SELFTEST known positive detected: {bool(known)}")
if not known:
    print("ABORT: detector missed the known positive; count is not trustworthy")
    sys.exit(2)
json.dump({"sha":SHA,"witnesses":[[str(w),s] for w,s in hits]},
          open("/tmp/residue_targets.json","w"))
print(f"targets written: /tmp/residue_targets.json")
