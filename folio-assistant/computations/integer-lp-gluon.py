#!/usr/bin/env python3
"""
Integer LP for gluon placement: minimum gluon crossings for LP stability.

For each nucleon (proton uud, neutron udd), the 9-crossing element
B₃ × Δ₃(quarks) is LP UNSTABLE (Frobenius positivity Gx[γ] < 0).
The integer LP enumerates all feasible gluon combinations from
{σ₀, σ₁, L₊, L₋} and selects the one with minimum |tr_M|
that is stable at every intermediate step.

Results:
  Proton:  σ₀ → σ₀ (2 crossings, 11 total), |tr_M| = 0.027
  Neutron: L₊ → L₋ (4 crossings, 13 total), |tr_M| = 0.112

Usage:
    cd folio-assistant/computations && python3 integer-lp-gluon.py
"""

import json
import sys
import numpy as np
from itertools import product as cartprod
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h

z = 1.0 / (q0**0.5 + qi0**0.5)
NAMES = ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']

# Corrected Gram matrix (tr_M(e⁻) = z³)
G = np.array([
    [1, z, z, z**2, z**2, z**3],
    [z, h*z+1, z**2, h*z**2+z, z**3, h*z**3+z**2],
    [z, z**2, h*z+1, z**3, h*z**2+z, h*z**3+z**2],
    [z**2, z**3, h*z**2+z, h*z**3+z**2, h*(h*z**2+z)+z**2, h*(h*z**3+z**2)+h*z**2+z],
    [z**2, h*z**2+z, z**3, h*(h*z**2+z)+z**2, h*z**3+z**2, h*(h*z**3+z**2)+h*z**2+z],
    [z**3, h*z**3+z**2, h*z**3+z**2, h*(h*z**3+z**2)+h*z**2+z, h*(h*z**3+z**2)+h*z**2+z, h*(h*(h*z**3+z**2)+h*z**2+z)+h*z**3+z**2],
])


def mul(nf, c, d, gen):
    r = [0.0] * 6
    if gen == 0:
        rules = [(0,[(1,c),(0,d)]), (1,[(1,c*h),(0,c),(1,d)]), (2,[(3,c),(2,d)]),
                 (3,[(3,c*h),(2,c),(3,d)]), (4,[(5,c),(4,d)]), (5,[(5,c*h),(4,c),(5,d)])]
    else:
        rules = [(0,[(2,c),(0,d)]), (1,[(4,c),(1,d)]), (2,[(2,c*h),(0,c),(2,d)]),
                 (3,[(5,c),(3,d)]), (4,[(4,c*h),(1,c),(4,d)]), (5,[(5,c*h),(3,c),(5,d)])]
    for src, targets in rules:
        if abs(nf[src]) < 1e-15:
            continue
        for tgt, coeff in targets:
            r[tgt] += nf[src] * coeff
    return r


def trM(nf):
    w = [1, z, z, z**2, z**2, z**3]
    return sum(nf[i] * w[i] for i in range(6))


def is_stable(nf):
    return all(G @ np.array(nf) >= -1e-10)


# B₃ = (σ₀σ₁⁻¹)³
nf_b3 = [1, 0, 0, 0, 0, 0]
for _ in range(3):
    nf_b3 = mul(nf_b3, 1, 0, 0)
    nf_b3 = mul(nf_b3, 1, -h, 1)

# Available gluon operations
ops = [
    ("σ₀", lambda nf: mul(nf, 1, 0, 0)),
    ("σ₁", lambda nf: mul(nf, 1, 0, 1)),
    ("L₊", lambda nf: mul(mul(nf, 1, 0, 0), 1, 0, 1)),
    ("L₋", lambda nf: mul(mul(nf, 1, 0, 1), 1, 0, 0)),
]


def solve_integer_lp(base_nf, quark_label, max_depth=3):
    """Enumerate all integer gluon combinations up to max_depth operations.
    Require LP stability at EVERY intermediate step.
    Return sorted by |tr_M| (minimum action)."""
    results = []

    # 0 gluons
    if is_stable(base_nf):
        results.append((0, [], base_nf[:], trM(base_nf)))

    # 1 to max_depth gluon operations
    for depth in range(1, max_depth + 1):
        for combo in cartprod(range(4), repeat=depth):
            nf = base_nf[:]
            valid = True
            names = []
            ncross = 0
            for oi in combo:
                nf = ops[oi][1](nf)
                names.append(ops[oi][0])
                ncross += 2 if ops[oi][0] in ("L₊", "L₋") else 1
                if not is_stable(nf):
                    valid = False
                    break
            if valid:
                results.append((ncross, names, nf[:], trM(nf)))

    # Deduplicate by NF
    seen = set()
    unique = []
    for r in results:
        key = tuple(f"{v:.6f}" for v in r[2])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    unique.sort(key=lambda r: abs(r[3]))
    return unique


# ══════════════════════════════════════════════════════════════
# PROTON (uud)
# ══════════════════════════════════════════════════════════════

print("INTEGER LP FOR GLUON PLACEMENT")
print("=" * 70)
print(f"q₀ = {q0:.15f}")
print(f"Gram matrix: corrected (tr_M(e⁻) = z³ = {z**3:.6f})")
print()

# Proton 9-crossing: B₃ × uu(σ₀) × ud(σ₁ mixed) × ud(σ₀ mixed)
p9 = nf_b3[:]
p9 = mul(p9, 1, 0, 0)        # uu
p9 = mul(p9, 1, -h/2, 1)     # ud gen 1
p9 = mul(p9, 1, -h/2, 0)     # ud gen 0

print("━━━ PROTON (uud) ━━━")
print(f"  9-crossing NF: [{' '.join(f'{v:+.4f}' for v in p9)}]")
print(f"  tr_M = {trM(p9):.6f}, LP stable = {is_stable(p9)}")
print()

p_results = solve_integer_lp(p9, "proton")

print(f"  {len(p_results)} feasible integer solutions:")
print(f"  {'#':>3} {'cross':>5} {'ops':>20} {'|tr_M|':>10} {'tr_M':>12}")
print("  " + "-" * 55)
for i, (nc, ns, nf, tm) in enumerate(p_results[:10]):
    ops_str = "→".join(ns) if ns else "(none)"
    print(f"  {i:>3} {nc:>5} {ops_str:>20} {abs(tm):>10.6f} {tm:>+12.6f}")

p_best = p_results[0]
print(f"\n  INTEGER LP OPTIMAL: {' → '.join(p_best[1]) if p_best[1] else 'none'}")
print(f"  Total crossings: {9 + p_best[0]}")
print(f"  NF = [{' '.join(f'{v:+.4f}' for v in p_best[2])}]")
print(f"  net = {sum(p_best[2]):.6f}, |tr_M| = {abs(p_best[3]):.6f}")


# ══════════════════════════════════════════════════════════════
# NEUTRON (udd)
# ══════════════════════════════════════════════════════════════

# Neutron 9-crossing: B₃ × ud(σ₀ mixed) × dd(σ₁⁻¹) × ud(σ₀ mixed)
n9 = nf_b3[:]
n9 = mul(n9, 1, -h/2, 0)     # ud gen 0
n9 = mul(n9, 1, -h, 1)       # dd gen 1
n9 = mul(n9, 1, -h/2, 0)     # ud gen 0

print()
print("━━━ NEUTRON (udd) ━━━")
print(f"  9-crossing NF: [{' '.join(f'{v:+.4f}' for v in n9)}]")
print(f"  tr_M = {trM(n9):.6f}, LP stable = {is_stable(n9)}")
print()

n_results = solve_integer_lp(n9, "neutron")

print(f"  {len(n_results)} feasible integer solutions:")
print(f"  {'#':>3} {'cross':>5} {'ops':>20} {'|tr_M|':>10} {'tr_M':>12}")
print("  " + "-" * 55)
for i, (nc, ns, nf, tm) in enumerate(n_results[:10]):
    ops_str = "→".join(ns) if ns else "(none)"
    print(f"  {i:>3} {nc:>5} {ops_str:>20} {abs(tm):>10.6f} {tm:>+12.6f}")

n_best = n_results[0]
print(f"\n  INTEGER LP OPTIMAL: {' → '.join(n_best[1]) if n_best[1] else 'none'}")
print(f"  Total crossings: {9 + n_best[0]}")
print(f"  NF = [{' '.join(f'{v:+.4f}' for v in n_best[2])}]")
print(f"  net = {sum(n_best[2]):.6f}, |tr_M| = {abs(n_best[3]):.6f}")


# ══════════════════════════════════════════════════════════════
# STABILITY BOUNDARY (symbolic in q)
# ══════════════════════════════════════════════════════════════

print()
print("━━━ STABILITY BOUNDARY ━━━")
print("  The 9-crossing proton is LP stable iff tr_M ≥ 0.")
print("  tr_M sign is determined by P(q²) where")
print("  P(u) = u⁶ − 3u⁵ + 5u⁴ − 8u³ + 5u² − 3u + 1")

# Find critical q by scanning
for qv in [1.10, 1.102, 1.104, 1.105, 1.106, 1.108, 1.110]:
    zv = 1.0 / (qv**0.5 + qv**(-0.5))
    hv = qv - 1.0/qv
    nf = [1, 0, 0, 0, 0, 0]
    for _ in range(3):
        nf = mul(nf, 1, 0, 0)
        nf = mul(nf, 1, -hv, 1)
    nf = mul(nf, 1, 0, 0)
    nf = mul(nf, 1, -hv/2, 1)
    nf = mul(nf, 1, -hv/2, 0)
    trm = sum(nf[i] * [1, zv, zv, zv**2, zv**2, zv**3][i] for i in range(6))
    print(f"  q = {qv:.3f}: tr_M(9-cross proton) = {trm:+.6f} {'✓ stable' if trm >= 0 else '✗ unstable'}")

print(f"\n  Critical q ≈ 1.104 (our q₀ = {q0:.4f} is just above)")
print(f"  The gluon is needed because q₀ > q_critical.")


# ══════════════════════════════════════════════════════════════
# WITNESS
# ══════════════════════════════════════════════════════════════

witness = {
    "computation": "integer-lp-gluon",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": q0,
    "proton": {
        "base_crossings": 9,
        "base_stable": is_stable(p9),
        "base_trM": trM(p9),
        "gluon_optimal": " → ".join(p_best[1]),
        "gluon_crossings": p_best[0],
        "total_crossings": 9 + p_best[0],
        "optimal_trM": p_best[3],
        "n_feasible": len(p_results),
        "NF": p_best[2],
    },
    "neutron": {
        "base_crossings": 9,
        "base_stable": is_stable(n9),
        "base_trM": trM(n9),
        "gluon_optimal": " → ".join(n_best[1]),
        "gluon_crossings": n_best[0],
        "total_crossings": 9 + n_best[0],
        "optimal_trM": n_best[3],
        "n_feasible": len(n_results),
        "NF": n_best[2],
    },
    "stability_boundary": {
        "polynomial": "u⁶ − 3u⁵ + 5u⁴ − 8u³ + 5u² − 3u + 1",
        "critical_q": 1.104,
        "our_q0": q0,
    },
}

# ══════════════════════════════════════════════════════════════
#  SDP LIFT VALIDATION  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
# integer-lp-gluon enumerates gluon combinations + checks G·x ≥ 0
# componentwise.  That's strictly weaker than xᵀGx ≥ 0 at q₀
# (G has a negative eigenvalue).  The per-nucleon H_3 SDP lift
# below adds tr(G·X) ≥ 0.  NB: the full-atom H_{3A} SDP for gluon
# selection (P2.1b) is a separate problem — see
# docs/mass-1ppm-workplan.md.
print(f"\n━━━ SDP LIFT VALIDATION (per-nucleon H_3) ━━━")
_sdp_reports = []
try:
    from sdp_moment_lift import lp_vs_sdp_report
    _tr_m = np.array([1.0, z, z, z**2, z**2, z**3])
    for _lbl, _nf in [("proton-9x", p9), ("neutron-9x", n9),
                         ("proton-best", p_best[2]),
                         ("neutron-best", n_best[2])]:
        _net = float(sum(_nf))
        _rep = lp_vs_sdp_report(
            c=_tr_m, G=G, A_eq=np.ones((1, 6)),
            b_eq=np.array([_net]),
            label=f"integer-lp-gluon/{_lbl}")
        for _l in _rep.summary_lines():
            print(_l)
        print()
        _sdp_reports.append(_rep.__dict__)
except ImportError as _e:
    print(f"  (cvxpy not available: {_e})")
witness["sdp_lift"] = _sdp_reports

witness_path = Path(__file__).parent / "integer-lp-gluon.witness.json"
witness_path.write_text(json.dumps(witness, indent=2))
print(f"\nWitness: {witness_path.name}")
