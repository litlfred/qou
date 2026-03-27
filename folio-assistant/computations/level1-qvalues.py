#!/usr/bin/env python3
"""
Level 1 (quark-level) Q-value computation for all 6 verification nuclei.

Level 0: A strands (1 per nucleon), binom(A,2) crossings
Level 1: 3A strands (3 quarks per nucleon), binom(3A,2) crossings

The hecke_engine works at Level 1 WITHOUT code changes — we just
expand the ordering from nucleon-level to quark-level:
  proton (1) → [1, 1, 0]  (u, u, d)
  neutron (0) → [1, 0, 0]  (u, d, d)

The crossing types are:
  u-u (1,1) → positive crossing (weight q)    [= p-p at Level 0]
  d-d (0,0) → negative crossing (weight q⁻¹)  [= n-n at Level 0]
  u-d (1,0) → mixed crossing                   [= p-n at Level 0]

Run from repo root:
    python3 folio-assistant/computations/level1-qvalues.py

Output:
    folio-assistant/computations/level1-qvalues.witness.json
"""

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from computations.hecke_engine import QRat

# ── Quark-level ordering expansion ───────────────────────────────

def expand_to_quarks(nucleon_ordering):
    """Expand nucleon ordering to quark ordering.

    proton (1) → [1, 1, 0]  (u, u, d)
    neutron (0) → [1, 0, 0]  (u, d, d)
    """
    quark_ordering = []
    for nucleon in nucleon_ordering:
        if nucleon == 1:  # proton = uud
            quark_ordering.extend([1, 1, 0])
        else:             # neutron = udd
            quark_ordering.extend([1, 0, 0])
    return quark_ordering


def find_converting_quarks(ord_par_quarks, ord_dau_quarks):
    """Find the 3 quark positions where d→u conversion occurs."""
    converting = []
    for i in range(len(ord_par_quarks)):
        if ord_par_quarks[i] != ord_dau_quarks[i]:
            converting.append(i)
    return converting


# ── Nuclei ───────────────────────────────────────────────────────

nuclei = [
    {"name": "³H",    "p": 1,  "n": 2,  "Q_exp_MeV": 0.0186},
    {"name": "¹⁴C",   "p": 6,  "n": 8,  "Q_exp_MeV": 0.156},
    {"name": "⁶⁰Co",  "p": 27, "n": 33, "Q_exp_MeV": 0.318},
    {"name": "⁹⁰Sr",  "p": 38, "n": 52, "Q_exp_MeV": 0.546},
    {"name": "¹³⁷Cs", "p": 55, "n": 82, "Q_exp_MeV": 0.514},
    {"name": "²¹⁰Bi", "p": 83, "n": 127,"Q_exp_MeV": 1.163},
]

# ── Engine ───────────────────────────────────────────────────────

qr = QRat(11100, 10000)  # q = 1.1100
hbar_q_sq = float((qr.q - 1) / qr.q) ** 2  # ℏ_q²

print("=" * 60)
print("Level 1 (quark-level) Q-value computation")
print("=" * 60)
print(f"q = {float(qr.q)}")
print(f"ℏ_q² = {hbar_q_sq:.6f}")
print()

results = []

for nuc in nuclei:
    p, n = nuc["p"], nuc["n"]
    A = p + n
    strands_L1 = 3 * A
    crossings_L1 = strands_L1 * (strands_L1 - 1) // 2

    print(f"{'─' * 50}")
    print(f"{nuc['name']}: N({p},{n}), A={A}")
    print(f"  Level 0: {A} strands, {A*(A-1)//2} crossings")
    print(f"  Level 1: {strands_L1} strands, {crossings_L1} crossings")

    # Skip very heavy nuclei (> 60 strands at L1 is too slow for exact)
    if strands_L1 > 60:
        print(f"  SKIPPED — {strands_L1} strands too large for exact computation")
        print(f"  (need heuristic ordering for Level 1 with A > 20)")
        results.append({
            "name": nuc["name"], "A": A, "p": p, "n": n,
            "strands_L1": strands_L1, "crossings_L1": crossings_L1,
            "status": "skipped — too large",
        })
        print()
        continue

    t0 = time.time()

    # Parent ordering (nucleon level): block ordering [1]*p + [0]*n
    nucleon_par = [1] * p + [0] * n
    nucleon_dau = [1] * (p + 1) + [0] * (n - 1)

    # Expand to quark level
    quark_par = expand_to_quarks(nucleon_par)
    quark_dau = expand_to_quarks(nucleon_dau)

    print(f"  Parent quarks:   {''.join('u' if x else 'd' for x in quark_par)}")
    print(f"  Daughter quarks: {''.join('u' if x else 'd' for x in quark_dau)}")

    # Find converting positions
    converting = find_converting_quarks(quark_par, quark_dau)
    print(f"  Converting positions: {converting}")

    # Compute traced volumes at each generator
    n_gens = strands_L1 - 1
    log_ratio_sum = 0.0
    affected_count = 0

    for i in range(n_gens):
        vp = float(qr.traced_volume(i, quark_par))
        vd = float(qr.traced_volume(i, quark_dau))
        if vp != 0 and vd != 0 and abs(vp - vd) > 1e-15:
            log_ratio = math.log(abs(vp)) - math.log(abs(vd))
            log_ratio_sum += log_ratio
            affected_count += 1

    # Q-value from log-ratio of traced volumes
    Q_q = log_ratio_sum / hbar_q_sq if hbar_q_sq != 0 else 0

    elapsed = time.time() - t0

    result = {
        "name": nuc["name"], "A": A, "p": p, "n": n,
        "strands_L1": strands_L1, "crossings_L1": crossings_L1,
        "converting_positions": converting,
        "affected_generators": affected_count,
        "log_ratio_sum": log_ratio_sum,
        "Q_q_skein_units": Q_q,
        "Q_exp_MeV": nuc["Q_exp_MeV"],
        "elapsed_s": elapsed,
        "status": "computed",
    }
    results.append(result)

    print(f"  Affected generators: {affected_count} / {n_gens}")
    print(f"  Σ log|V_par/V_dau| = {log_ratio_sum:.6f}")
    print(f"  Q_q (Skein units) = {Q_q:.4f}")
    print(f"  Q_exp (MeV) = {nuc['Q_exp_MeV']}")
    print(f"  Time: {elapsed:.2f}s")
    print()

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "level1-qvalues",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Level 1 (quark-level) Q-value computation. "
        "Each nucleon expanded to 3 quark strands (u,u,d or u,d,d). "
        "Uses block ordering — ground-state search not performed."
    ),
    "q": float(qr.q),
    "hbar_q_sq": hbar_q_sq,
    "nuclei": results,
    "notes": [
        "Block ordering [protons first] is NOT the ground state for Level 1.",
        "Ground-state search at Level 1 has binom(3A, total_u) orderings.",
        "For A=3: binom(9,5) = 126 orderings — feasible.",
        "For A=14: binom(42,20) ~ 10^11 — needs heuristic.",
        "The Q_q values here are UPPER BOUNDS (block ordering overestimates).",
    ],
}

out_path = Path(__file__).parent / "level1-qvalues.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
