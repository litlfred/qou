#!/usr/bin/env python3
"""
26a: Apply spectral-ladder extension to tritium Q via parent-daughter
NF-difference baseline.

Per `prop:branching-qvalue-factorization` (already in repo):
  Σ over 4^A configs Δm_e = a^Z · b^{N-1} · (a − b)
  where a = Σ_c G_P(c), b = Σ_c G_N(c).

For tritium ³H → ³He (Z=1, N=2 → Z=2, N=1):
  Q(³H → ³He) = a · b · (a − b) · m_e   (closed form)
              = 3(q²-1)³(q²+1)²(3q⁴+4q²+3) / (32 q⁷) · m_e
              ≈ 0.01793 MeV  (-3.55% off CODATA 0.01859)

Apply spectral-ladder extension (analog of Δm_{n-p} fix):
  Q(T) = Q_closed_form + chir · m_e · Vol(K_χ_T) · |(q;q)_r|
       + α · m_e · |(q;q)_{r+1}|

where:
  - K_χ_T = chirality knot for tritium decay (candidate: 8_11 or another)
  - r = curvature-rank of K_χ_T
  - α = test as universal (= 0.8272 from n→p) OR fit to tritium

Goal: does α₄ = 0.8272 from n→p close tritium when applied to the right
(branching-factorization) baseline?
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


# ── Tritium closed form (branching factorization) ────────────────
q2 = Q0**2; q4 = Q0**4; q7 = Q0**7
Q_T_closed = 3*(q2-1)**3 * (q2+1)**2 * (3*q4 + 4*q2 + 3) / (32*q7) * m_e
Q_T_codata = mp.mpf("0.018592")
err_closed = (Q_T_closed - Q_T_codata)/Q_T_codata

print("=" * 100)
print("26a: Tritium Q via branching-factorization baseline + spectral ladder")
print("=" * 100)
print(f"  Q(T→³He) closed form (branching factorization) = {float(Q_T_closed):.10f} MeV")
print(f"  Q(T→³He) CODATA                                = {float(Q_T_codata):.10f} MeV")
print(f"  err (closed form alone)                          = {float(err_closed)*100:+.4f}%")
print(f"  residual to close                                = {float(Q_T_codata - Q_T_closed):+.6e} MeV")
print()

residual = Q_T_codata - Q_T_closed  # ≈ +0.00066 MeV

# n→p reference
Sigma_3 = 2 + 1/qint(2)
alpha_4_np = mp.mpf("0.8272227623")
print(f"  FROZEN α₄ from n→p fit = {float(alpha_4_np):.10f}")
print()

# ── Test 1: Add α₄·m_e·|(q;q)_r| with FROZEN α₄ at various ranks ──
print("─" * 100)
print("Test 1: Q(T) = closed form + α₄·m_e·|(q;q)_r|  (FROZEN α₄ from n→p)")
print("─" * 100)
print(f"  {'rank r':>8} {'m_e·|(q;q)_r|':>18} {'α₄·m_e·|(q;q)_r|':>20} {'Q_pred':>12} {'err %':>10}")
for r in range(3, 10):
    qpr = abs(qpoch(r))
    contrib = alpha_4_np * m_e * qpr
    Q_pred = Q_T_closed + contrib
    err = (Q_pred - Q_T_codata)/Q_T_codata
    print(f"  {r:>8} {float(m_e*qpr):>18.10f} {float(contrib):>20.10f} {float(Q_pred):>12.6f} {float(err)*100:>+10.4f}%")

# ── Test 2: Same with α=1 (no fit) ─────────────────────────────────
print()
print("─" * 100)
print("Test 2: Q(T) = closed form + m_e·|(q;q)_r|  (no fit, raw Pochhammer)")
print("─" * 100)
print(f"  {'rank r':>8} {'m_e·|(q;q)_r|':>18} {'Q_pred':>12} {'err %':>10}")
for r in range(3, 10):
    qpr = abs(qpoch(r))
    Q_pred = Q_T_closed + m_e * qpr
    err = (Q_pred - Q_T_codata)/Q_T_codata
    print(f"  {r:>8} {float(m_e*qpr):>18.10f} {float(Q_pred):>12.6f} {float(err)*100:>+10.4f}%")

# ── Test 3: Add chirality knot + universal tail (full extension) ──
print()
print("─" * 100)
print("Test 3: Q(T) = closed form + m_e·Vol(K)·|(q;q)_r| + α₄·m_e·|(q;q)_{r+1}|")
print("─" * 100)
KNOTS = [
    ("6_1", "3.16396322888314", 3, 4),
    ("8_11", "8.28631808635811", 4, 5),
    ("4_1", mp.nstr(vol_4_1_at(50), 50), 3, 4),  # figure-eight, exact via 2·Cl_2(π/3)
    ("5_2", "2.82812208833078", 3, 4),
]
print(f"  {'K':<6} {'r_chir':>7} {'chir_MeV':>14} {'tail_MeV':>14} {'Q_pred':>12} {'err %':>10}")
for K, vol_str, r_chir, r_tail in KNOTS:
    Vol_K = mp.mpf(vol_str)
    chir = m_e * Vol_K * abs(qpoch(r_chir))
    tail = alpha_4_np * m_e * abs(qpoch(r_tail))
    Q_pred = Q_T_closed + chir + tail
    err = (Q_pred - Q_T_codata)/Q_T_codata
    print(f"  {K:<6} {r_chir:>7} {float(chir):>14.10f} {float(tail):>14.10f} {float(Q_pred):>12.6f} {float(err)*100:>+10.4f}%")

# ── Test 4: Solve for α at each rank that closes Q exactly ─────────
print()
print("─" * 100)
print("Test 4: Fit α at each rank to close Q exactly — does any rank give α ≈ 0.8272?")
print("─" * 100)
print(f"  {'rank r':>8} {'fitted α':>16} {'matches α₄_np?':>18}")
for r in range(3, 10):
    qpr = abs(qpoch(r))
    alpha_r = float(residual) / float(m_e * qpr)
    delta = abs(alpha_r - float(alpha_4_np))
    match = "★ MATCH" if delta < 0.05 else f"({delta:+.4f})"
    print(f"  {r:>8} {alpha_r:>16.6f} {match:>18}")

print()
print("=" * 100)
print("BEST FORMULA")
print("=" * 100)
# Find the cleanest match
best_r, best_alpha, best_qpred = None, None, None
for r in range(3, 12):
    qpr = abs(qpoch(r))
    alpha_r = float(residual) / float(m_e * qpr)
    delta = abs(alpha_r - float(alpha_4_np))
    if best_r is None or delta < abs(best_alpha - float(alpha_4_np)):
        best_r, best_alpha = r, alpha_r
        best_qpred = float(Q_T_closed) + alpha_r * float(m_e * qpr)
print(f"  Rank closest to α₄_np = 0.8272: r = {best_r}")
print(f"  Fitted α at that rank = {best_alpha:.6f}  (vs n→p α₄ = {float(alpha_4_np):.6f})")
if abs(best_alpha - float(alpha_4_np)) / float(alpha_4_np) < 0.05:
    print(f"  → α₄ from n→p ALSO works for tritium at rank {best_r}!")
else:
    print(f"  → α at tritium-correct rank differs from n→p α₄ by {abs(best_alpha - float(alpha_4_np))/float(alpha_4_np)*100:.1f}%")

out = {
    "computation": "tritium-q-spectral-extension",
    "description": ("26a: Test whether α₄ = 0.8272 (from n→p single-nucleon fit) "
                    "ALSO closes tritium Q via parent-daughter NF-difference "
                    "baseline (branching factorization).  Tests four ansätze: "
                    "(1) frozen α₄ at various ranks, (2) raw Pochhammer no fit, "
                    "(3) chirality knot + tail, (4) per-rank fitted α to find "
                    "which rank gives α ≈ 0.8272 universal."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "Q_T_closed_form_MeV": float(Q_T_closed),
    "Q_T_codata_MeV": float(Q_T_codata),
    "err_closed_form_pct": float(err_closed * 100),
    "residual_to_close_MeV": float(residual),
    "alpha_4_from_np_fit": float(alpha_4_np),
    "best_rank_for_universal_alpha": best_r,
    "best_fitted_alpha_at_that_rank": best_alpha,
    "alpha_match_pct": float(abs(best_alpha - float(alpha_4_np))/float(alpha_4_np)*100)
}
out_path = Path(__file__).parent / "tritium-q-spectral-extension.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
