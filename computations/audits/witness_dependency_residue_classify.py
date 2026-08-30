#!/usr/bin/env python3
"""Three-way classification of the qou-wlaf residue sweep.

A bare MOVED count is the wrong granularity and must never be reported:
`atomic_tr_m_mpfr_50dps` moves in `.scriptHash` ALONE, which is provenance
drift, not a number changing. Computable from the recorded per-witness
`fields` without re-running anything — which is why the runner records them.
"""
import json, sys
from collections import Counter

PROVENANCE = {"scriptHash", "scriptCommitSha", "commitSha", "engine",
              "engineVersion", "schema", "schemaVersion", "auditOnly"}

def leaf_key(path):
    return path.rsplit(".", 1)[-1].split("[")[0]

TIMING = lambda k: ("elapsed" in k or k.endswith("_seconds")
                    or k.endswith("_runtime") or k.endswith("_wall_sec"))

def classify(r):
    v = r.get("verdict")
    if v != "MOVED":
        return v
    keys = {leaf_key(f) for fl in r.get("fields", {}).values() for f in fl}
    # drop timing keys the runner's mask missed at the time it ran; recorded
    # field names make this reclassifiable without re-running anything
    keys = {k for k in keys if not TIMING(k)}
    if not keys:
        return "IDENTICAL"
    if keys and keys <= PROVENANCE:
        return "MOVED_PROVENANCE_ONLY"
    return "MOVED_SUBSTANTIVE"

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/residue_results3.json"
d = json.load(open(path))
res = d["results"]
cls = [(r["producer"], classify(r), r) for r in res]
c = Counter(k for _, k, _ in cls)

print(f"pinned SHA : {d['sha']}")
print(f"processed  : {len(res)} of 95\n")
for k in ("MOVED_SUBSTANTIVE","MOVED_PROVENANCE_ONLY","IDENTICAL",
          "TIMEOUT","CRASH","GUARD_REFUSAL","NO_SOURCE"):
    if c.get(k): print(f"  {k:<24s} {c[k]}")

scoreable = c.get("MOVED_SUBSTANTIVE",0)+c.get("MOVED_PROVENANCE_ONLY",0)+c.get("IDENTICAL",0)
print(f"\n  scoreable (excludes timeouts/crashes): {scoreable}")
print("  NB a TIMEOUT is NOT evidence either way — it is a budget artifact.")

print("\nMOVED_SUBSTANTIVE — a real number changed:")
for p,k,r in cls:
    if k=="MOVED_SUBSTANTIVE":
        ks=sorted({leaf_key(f) for fl in r.get('fields',{}).values() for f in fl})
        print(f"  {p:<44s} {', '.join(ks[:5])}")
print("\nMOVED_PROVENANCE_ONLY — no number changed:")
for p,k,r in cls:
    if k=="MOVED_PROVENANCE_ONLY":
        ks=sorted({leaf_key(f) for fl in r.get('fields',{}).values() for f in fl})
        print(f"  {p:<44s} {', '.join(ks)}")
