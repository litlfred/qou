#!/usr/bin/env python3
"""
27c: Does α (per-transition ladder coefficient) correlate with the
chirality knot Vol at the optimal rank?

Hypothesis: α_X · Vol(K_χ_X) = universal constant, OR
            α_X / Vol(K_χ_X) = universal constant, OR
            α_X = f(K_χ_X, q_0) for some closed function f.

Data points:
  n → p:    α_np = 0.827  with K_χ = 6_1 (Vol = 3.164) at r = 3, tail at r = 4
  ³H → ³He: α_T = 0.446 (at r=6 best, but candidate at r=4 too) with what K_χ?

Strategy:
  1. For tritium, sweep candidate K_χ knots.  At each (K, r_chir) pair,
     compute residual after subtracting the chirality piece:
       residual_T = Q_T_codata - Q_T_closed - m_e·Vol(K)·|(q;q)_{r_chir}|
     and the implied tail coefficient α at r = r_chir+1.
  2. Look for a (K, r) choice where α matches α_np = 0.827 within 1%.
  3. If found: candidate universal coefficient ✓.
  4. If not: report the best (K, r) and the α value.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from q_parameter import Q as Q0_FLOAT, vol_4_1_at, Q_MP, Q_INV_MP
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qpoch(n):
    out = mp.mpf(1)
    for k in range(1, n+1): out *= (1 - Q0**k)
    return out


# n→p reference
alpha_np = mp.mpf("0.8272227623")  # at r=4 tail
Vol_61 = mp.mpf("3.16396322888314")  # K_χ for n→p, at r=3

# Tritium closed form residual
q2 = Q0**2; q4 = Q0**4; q7 = Q0**7
Q_T_closed = 3*(q2-1)**3 * (q2+1)**2 * (3*q4 + 4*q2 + 3) / (32*q7) * m_e
Q_T_codata = mp.mpf("0.018592")
residual_T = Q_T_codata - Q_T_closed

# Knot DB (Vol, std/sym/alt channel from curvature_rank_mass.py)
KNOTS = [
    ("4_1",  mp.nstr(vol_4_1_at(50), 50), 0),  # exact via 2·Cl_2(π/3)  (was 20-dps string)
    ("5_2",  "2.82812208833078",       0),
    ("6_1",  "3.16396322888314",       1),  # std
    ("6_2",  "4.40083251397820",       0),
    ("6_3",  "5.69270",                0),
    ("7_2",  "3.33174",                0),
    ("7_3",  "4.59213",                1),
    ("7_4",  "5.01376",                2),  # alt
    ("7_5",  "6.44390",                0),
    ("7_6",  "7.08458",                0),
    ("7_7",  "7.64340",                0),
    ("8_11", "8.28631808635811",       1),  # std (T binding chirality)
    ("8_19", "8.92395",                0),  # T_{3,4}
    ("L6a4", "7.32772475300860",       0),  # Borromean
]


print("=" * 110)
print("27c: α-Vol(K_chirality) correlation across (n→p, T→³He) and beyond")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f},  m_e = {float(m_e):.6f} MeV")
print(f"  α_np (rank-4 tail) = {float(alpha_np):.10f}, K_χ_np = 6_1 (Vol={float(Vol_61):.4f}, r_chir=3)")
print(f"  Q_T_codata        = {float(Q_T_codata):.10f} MeV")
print(f"  Q_T_closed_form   = {float(Q_T_closed):.10f} MeV")
print(f"  residual_T to close = {float(residual_T):+.10f} MeV")
print()

# Sweep (K_χ, r_chir) for tritium
# Implied α_T at r_chir+1 tail position:
#   residual_T = m_e·Vol(K)·|(q;q)_{r_chir}| + α_T·m_e·|(q;q)_{r_chir+1}|
# Solve: α_T = (residual_T - m_e·Vol(K)·|(q;q)_{r_chir}|) / (m_e·|(q;q)_{r_chir+1}|)
print("─" * 110)
print(f"  {'K_χ':<6} {'Vol(K)':>10} {'r_chir':>7} {'chir_MeV':>14} {'tail_α_T':>14} {'α_T match α_np?':>20}")
print("─" * 110)

best_matches = []
for K, Vol_str, channel in KNOTS:
    Vol_K = mp.mpf(Vol_str)
    for r_chir in range(2, 8):
        chir_contrib = m_e * Vol_K * abs(qpoch(r_chir))
        # Allow negative α_T (chirality overshoots, tail compensates)
        tail_contrib = residual_T - chir_contrib
        tail_basis = m_e * abs(qpoch(r_chir + 1))
        alpha_T = tail_contrib / tail_basis
        delta = abs(alpha_T - alpha_np)
        match_pct = float(delta / alpha_np * 100)
        match_marker = "★ MATCH" if match_pct < 5 else f"({match_pct:+.1f}%)"
        # show all
        print(f"  {K:<6} {float(Vol_K):>10.4f} {r_chir:>7} {float(chir_contrib):>14.10f} {float(alpha_T):>+14.6f} {match_marker:>20}")
        best_matches.append((K, float(Vol_K), r_chir, float(chir_contrib), float(alpha_T), match_pct))

print()
# Best match
if best_matches:
    best = min(best_matches, key=lambda b: b[5])
    print(f"  Best candidate (closest α_T to α_np):")
    print(f"    K_χ = {best[0]}, Vol = {best[1]:.4f}, r_chir = {best[2]}")
    print(f"    chirality_MeV = {best[3]:.10f}")
    print(f"    α_T = {best[4]:.6f}  vs  α_np = {float(alpha_np):.6f}  ({best[5]:.1f}% gap)")

# Also try: α_T·Vol(K_chir) = α_np·Vol(K_np) ?
print()
print("─" * 110)
print("Test: does α · Vol(K_chir) at chirality rank give a universal constant?")
print("─" * 110)
print(f"  n→p:  α_np · Vol(6_1) = {float(alpha_np * Vol_61):.6f}  (= α_np at rank-4 tail × K_χ=6_1 at rank-3 chirality)")

# Search for K_χ such that α_T · Vol(K) = α_np · Vol(6_1)
target_product = alpha_np * Vol_61
print(f"  Looking for K_χ_T such that α_T_implied · Vol(K) ≈ {float(target_product):.4f}")
for K, Vol_str, channel in KNOTS[:10]:
    Vol_K = mp.mpf(Vol_str)
    # If chirality only at this K and rank, residual_T - chir = α_T·tail
    for r in range(2, 8):
        chir = m_e * Vol_K * abs(qpoch(r))
        if chir > 2*abs(residual_T): continue
        alpha_T = (residual_T - chir) / (m_e * abs(qpoch(r+1)))
        product = alpha_T * Vol_K
        ratio = product / target_product
        if abs(float(ratio) - 1) < 0.05:
            print(f"  ★ K={K:<5} r={r}  α·Vol = {float(product):.4f}  ratio to n→p = {float(ratio):.4f}")

# Also test: α·Vol_q where Vol_q is q-deformed Vol?
print()
print("─" * 110)
print("Verdict")
print("─" * 110)
print(f"""
Hypothesis (27c): α_X · Vol(K_χ_X) is universal across transitions.

n→p baseline:  α_np · Vol(6_1) = {float(alpha_np * Vol_61):.6f}

For tritium, scanning all (K, r) candidates: see table above.
If a (K, r) match within 5% to α_np was found, the hypothesis holds
with that knot identification.  Otherwise, α is genuinely transition-
specific without simple Vol-correlation.
""")

# Save
out = {
    "computation": "alpha-vol-chirality-correlation",
    "description": ("27c: Test whether α (per-transition ladder coefficient) "
                    "correlates with the chirality knot Vol at the optimal "
                    "rank.  Sweep all (K, r) pairs for tritium, looking for "
                    "(i) α_T = α_np = 0.827 at some choice, (ii) α·Vol(K) "
                    "universal across n→p and T."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "alpha_np": float(alpha_np),
    "Vol_K_np": float(Vol_61),
    "alpha_np_times_Vol": float(alpha_np * Vol_61),
    "Q_T_residual_MeV": float(residual_T),
    "tritium_sweep": [
        {"K": K, "Vol_K": float(Vol_str), "r_chir": r,
         "alpha_T_implied": (lambda Vol, rc: float((residual_T - m_e*mp.mpf(Vol)*abs(qpoch(rc))) / (m_e*abs(qpoch(rc+1)))))(Vol_str, r)}
        for K, Vol_str, _ in KNOTS for r in range(2, 8)
    ]
}
out_path = Path(__file__).parent / "alpha-vol-chirality-correlation.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
