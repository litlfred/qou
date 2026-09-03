#!/usr/bin/env python3
"""
bwsc_level7_wrt_targets.py — the concrete bwsc targets for closing bwS0_eq_hecke.

The W_λ keystone conjecture bwS0_eq_hecke reduces (PR #4365/#4402, beans bws0/bwsc)
to: the gauge row bwS0 (the colored WRT invariant of Σ(2,3,q)) equals the value map
d_q(λ) = [mark λ]_q at the fibre roots.  #4365 proved the Σ(2,3,5) slice (2 flat
connections → 2 distinct fold values), which `two_roots_insufficient` shows cannot
pin the degree-≤4 value map alone.  `eq_of_habiro_root_agreement` shows the full
(infinite) root family DOES pin it.

The cheapest sufficient finite slice is **level 7**: the 6 fold values
t_k = 2cos(kπ/7), k=1..6, are 6 distinct points > the max block-polynomial degree
(4), so agreement there already forces bwS0 = value map (KeystoneN5ValueMapRigidity
generalises to N=7 via eq_of_root_family_agreement).

This probe COMPUTES those 6 targets exactly (the value-map polynomial evaluated at
the level-7 roots) — the explicit numbers a WRT(Σ(2,3,7)) / colored-Jones-at-ζ₇
computation must reproduce to close bwsc via level 7.  It does NOT perform that WRT
computation (that is the open research compute).  Scope-(a); no fit; nothing wired.
"""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def qi_poly(n):
    """[n] as integer-coeff polynomial in t (dict power->coeff)."""
    a, b = {0: 0}, {0: 1}
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(n - 1):
        tb = {p + 1: c for p, c in b.items()}
        nxt = dict(tb)
        for p, c in a.items():
            nxt[p] = nxt.get(p, 0) - c
        a, b = b, {p: c for p, c in nxt.items() if c != 0}
    return b


def evalp(poly, t):
    return sum(c * t ** p for p, c in poly.items())


import math

# n=5 block value-map polynomials d_q(λ)=[mark]_q (+1 split for the electron block)
blocks = {
    "(5)   [1]": qi_poly(1),
    "(4,1) [4]": qi_poly(4),
    "(3,2) [5] (muon)": qi_poly(5),
    "(3,1,1) [5]+1 (electron)": {**qi_poly(5), 0: qi_poly(5).get(0, 0) + 1},
}
maxdeg = max(max(p.keys()) for p in blocks.values())  # 4

# level-7 fold points t_k = 2cos(kπ/7), k=1..6 — six distinct real values
level = 7
tpoints = [(k, 2 * math.cos(k * math.pi / level)) for k in range(1, level)]
distinct = len({round(t, 12) for _, t in tpoints})

assertions = []
assertions.append({
    "name": "level7_gives_six_distinct_points_exceeding_degree",
    "computed": f"{distinct} distinct points, max block degree {maxdeg}",
    "expected": f"{level - 1} distinct > {maxdeg}",
    "passed": distinct == level - 1 and distinct > maxdeg,
    "tolerance": 0,
    "source": "2cos(kπ/7), k=1..6 are 6 distinct fold values > deg 4 ⇒ agreement pins the value map (eq_of_root_family_agreement, N=7).",
})

# the explicit targets: value-map polynomial values at the 6 level-7 roots
targets = {}
for name, poly in blocks.items():
    targets[name] = {f"t_{k}=2cos({k}pi/7)": round(evalp(poly, t), 10) for k, t in tpoints}

# cross-level consistency: the value map at level-5 roots (the #4365 slice) uses the
# SAME polynomials — corroborating one-polynomial (infinite-rigidity) picture.
t5 = [(k, 2 * math.cos(k * math.pi / 5)) for k in (1, 2)]
sigma235_slice = {name: {f"t_{k}=2cos({k}pi/5)": round(evalp(poly, t), 10) for k, t in t5}
                  for name, poly in blocks.items()}

all_passed = all(a["passed"] for a in assertions)

script_path = Path(__file__)
script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]


def git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=script_path.parent,
                                       stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


witness = {
    "engine": "python",
    "engineVersion": "python 3.11",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "commitSha": git("rev-parse", "HEAD"),
    "assertions": assertions,
    "allPassed": all_passed,
    "durationMs": 0,
    "computation": "bwsc-level7-wrt-targets",
    "scriptFile": "computations/probes/bwsc_level7_wrt_targets.py",
    "scriptHash": script_hash,
    "scriptCommitSha": git("log", "-1", "--format=%H", "--",
                           "computations/probes/bwsc_level7_wrt_targets.py"),
    "precisionMetadata": {"note": "float64 sampling of the value-map polynomials at 2cos(kπ/N)"},
    "environment": {"python": "3.11"},
    "description": (
        "The concrete bwsc targets for closing bwS0_eq_hecke via level 7: the value map "
        "d_q(λ)=[mark]_q evaluated at the six level-7 fibre roots 2cos(kπ/7). These are the numbers a "
        "colored WRT(Σ(2,3,7)) / Jones-at-ζ₇ computation must reproduce; 6 distinct points > degree 4 "
        "⇒ agreement there pins the value map (eq_of_root_family_agreement, N=7). The #4365 Σ(2,3,5) "
        "slice (2 points) is bracketed as insufficient by two_roots_insufficient. Scope-(a); this probe "
        "does NOT perform the WRT computation; no fit; nothing wired."
    ),
    "data": {
        "level": level,
        "max_block_degree": maxdeg,
        "level7_targets": targets,
        "sigma235_slice_for_reference": sigma235_slice,
    },
}

out = script_path.parent / "bwsc-level7-wrt-targets.witness.json"
# Provenance stamp (bean qou-4un2): this producer writes its
# witness directly, so nothing else records which script made
# it -- and a re-run of an unstamped producer DELETES the
# scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
from qou_substrate.witness import WitnessBuilder as _WB
import os as _os  # noqa: E402 -- provenance stamp
witness.setdefault("scriptFile", _os.path.basename(__file__))
_WB.stamp_staleness_metadata(
    witness, script_path=__file__, engine=None, q0_anchor=False)
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out}  (allPassed={all_passed})")
print(f"level-7 needs 6 targets/block (deg {maxdeg} < 6). Sample (electron block):")
for kt, v in targets["(3,1,1) [5]+1 (electron)"].items():
    print(f"  {kt:22} -> {v}")
