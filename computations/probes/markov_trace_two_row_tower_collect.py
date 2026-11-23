#!/usr/bin/env python3
"""Collect markov_trace_two_row_tower_probe.py chain outputs into one witness.

Usage: markov_trace_two_row_tower_collect.py OUT.witness.json CHAIN.json ...
Each row is cross-checked against the v9 certificate's tr_markov_d where v9
computed one (A <= 8); the witness records the agreement.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70
CERT = Path(__file__).resolve().parents[2] / "tools/hecke-engine"

out, chains = sys.argv[1], sys.argv[2:]
rows, checks = [], []
meta = None
for c in chains:
    d = json.load(open(c))
    meta = meta or {k: d[k] for k in ("q0", "z", "dps", "self_check_worst_residual")}
    # carry the chain's q0 anchor into the witness (q0-anchor refill ratchet)
    for k in ("q0Anchor", "q0Value"):
        if k in d:
            meta.setdefault(k, d[k])
    for r in d["rows"]:
        rows.append(r)
        f = CERT / f"certificate-{r['isotope']}.json"
        if f.exists():
            v = json.load(open(f)).get("tr_markov_d", {}).get("value")
            if v:
                diff = abs(mp.mpf(v) - mp.mpf(r["tr_markov_d"]))
                checks.append({"isotope": r["isotope"], "v9": v,
                               "abs_diff": mp.nstr(diff, 5)})
rows.sort(key=lambda r: (r["z"], r["n"]))
w = {
    "description": "Convention-D Markov trace of the v9 nuclear element, computed as "
                   "sum over two-row shapes of [n-2k+1]_q/[2]_q^n times the seminormal "
                   "character, built up the Hecke tower; divided by 2^pn like the v9 "
                   "certificate field tr_markov_d.",
    "producer": "computations/probes/markov_trace_two_row_tower_probe.py",
    **meta,
    "cross_check_v9": checks,
    "rows": rows,
}
json.dump(w, open(out, "w"), indent=1)
print(len(rows), "rows,", len(checks), "cross-checked against v9; max diff",
      max((mp.mpf(c["abs_diff"]) for c in checks), default=0))
