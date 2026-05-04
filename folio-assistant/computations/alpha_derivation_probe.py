#!/usr/bin/env python3
"""
α* derivation probe: structural forms close to Catalan/3.

Upstream finding: α* = 0.30580743 closes neutron tower to zero.
Approximation α = G/3 = 0.30532186 gives 100 ppm.
Δ = α* - G/3 = +0.0004856 (~0.16% multiplicative correction).

Test candidate structural forms for the small correction:
  α* / (G/3) = 1.001590

Candidates:
  1. 1 + ℏ_q² · k  for various k
  2. 1 + h² · k
  3. 1 + small q-rational corrections
  4. Ratios involving [n]_q for small n
  5. Vol corrections (Vol(B_3) · refinement)

Witness: alpha-derivation-probe.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath as mp
mp.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT
from witness_polynomial import expose_polynomial_dict  # P2.5 Tier B


q = sp.Symbol('q', positive=True, real=True)
q0 = sp.Rational(int(Q0_FLOAT * 10 ** 16), 10 ** 16)
h = q - 1 / q

# Empirical / known constants
G_CATALAN = mp.mpf("0.9159655941772190150546035149323841107741493742816721342664981196")
ALPHA_STAR = mp.mpf("0.305807430741241")  # numerical root-find from upstream
G_OVER_3 = G_CATALAN / 3
DELTA = ALPHA_STAR - G_OVER_3
RATIO = ALPHA_STAR / G_OVER_3


def q_int(n, q_val=q0):
    return (q_val ** n - q_val ** (-n)) / (q_val - 1 / q_val)


def evaluate_at_q0(expr):
    return float(expr.subs(q, q0).evalf(30))


if __name__ == "__main__":
    print("α* DERIVATION PROBE — structural forms for the G/3 correction")
    print("=" * 80)
    print(f"q_0  = {float(q0)}")
    print(f"G    = {G_CATALAN}")
    print(f"G/3  = {G_OVER_3}")
    print(f"α*   = {ALPHA_STAR}")
    print(f"Δ    = α* - G/3 = {float(DELTA)}")
    print(f"ratio= α*/(G/3) = {float(RATIO)}")
    print(f"Δ/(G/3) = {float(DELTA/G_OVER_3) * 100:.4f}%")
    print()

    h_val = mp.mpf(str(float(h.subs(q, q0).evalf(30))))
    hbar_q = (q0 - 1) / q0
    hbar_q_val = mp.mpf(str(float(hbar_q.evalf(30))))
    hbar_sq = hbar_q_val ** 2
    print(f"h     = q - q⁻¹       = {float(h_val):.6f}")
    print(f"h²                     = {float(h_val ** 2):.6f}")
    print(f"ℏ_q   = (q-1)/q       = {float(hbar_q_val):.6f}")
    print(f"ℏ_q²                   = {float(hbar_sq):.6f}")
    print()

    target = float(DELTA / G_OVER_3)
    print(f"Target multiplicative correction: 1 + δ where δ = "
          f"{target:.8f}")
    print(f"  (Δ/(G/3) = {target * 100:.4f}%)")
    print()

    # Candidate forms for δ
    candidates = []

    # Powers of h, ℏ_q
    for name, val in [
        ("h²/27",        float(h_val) ** 2 / 27),
        ("h²/28",        float(h_val) ** 2 / 28),
        ("ℏ_q²/6",       float(hbar_sq) / 6),
        ("ℏ_q²/6.18",    float(hbar_sq) / 6.18),
        ("h⁴",           float(h_val) ** 4),
        ("h³/13",        float(h_val) ** 3 / 13),
        ("h·ℏ_q²",       float(h_val) * float(hbar_sq)),
        ("(q-1)³",       float((q0 - 1).evalf(30)) ** 3),
        ("ℏ_q³",         float(hbar_q_val) ** 3),
        ("ℏ_q⁴",         float(hbar_q_val) ** 4),
        ("ℏ_q · h",      float(hbar_q_val) * float(h_val)),
        ("ℏ_q²/[3]_q",   float(hbar_sq) / float(q_int(3))),
        ("h²/[3]_q²",    float(h_val ** 2) / float(q_int(3) ** 2),),
        ("ℏ_q²/[2]_q²",  float(hbar_sq) / float(q_int(2) ** 2)),
        ("(q²-1)²/100",  float(((q0**2 - 1)**2).evalf(30)) / 100),
        ("h/130",        float(h_val) / 130),
        ("(q-1)/130",    float(q0 - 1) / 130),
    ]:
        err_pct = abs(val - target) / target * 100 if target else 0
        candidates.append((name, val, err_pct))

    candidates.sort(key=lambda x: x[2])
    print(f"{'candidate':<25}  {'value':>14}  {'err vs target':>15}")
    print('-' * 60)
    for name, val, err in candidates[:15]:
        mark = "★" if err < 5 else "·" if err < 30 else " "
        print(f"  {name:<25}  {val:>14.8f}  {err:>13.4f}% {mark}")

    print()
    print("Best matches (under 5% err):")
    best = [c for c in candidates if c[2] < 5]
    if not best:
        print("  none under 5% — δ is small but not obviously a simple")
        print("  q-rational; may require multi-term expression or")
        print("  involve substrate-specific constants beyond q.")
    else:
        for name, val, err in best:
            print(f"  α* candidate: G/3 · (1 + {name}) = "
                  f"{float(G_OVER_3) * (1 + val):.10f}  err = "
                  f"{abs(float(G_OVER_3) * (1 + val) - float(ALPHA_STAR)) / float(ALPHA_STAR) * 100:.4f}%")

    # Also test additive corrections (α* = G/3 + δ)
    print()
    print("Additive correction Δ = α* - G/3:")
    print(f"  Δ    = {float(DELTA):.10e}")
    print(f"  Δ/m_e (m_e in Hecke units) for context:")

    additive_candidates = [
        ("h⁴/100",        float(h_val) ** 4 / 100),
        ("ℏ_q²·G/2000",   float(hbar_sq) * float(G_CATALAN) / 2000),
        ("h⁵",            float(h_val) ** 5),
        ("ℏ_q⁴",          float(hbar_q_val) ** 4),
        ("h²·ℏ_q²/100",   float(h_val ** 2) * float(hbar_sq) / 100),
        ("(q-1)⁴",        float(q0 - 1) ** 4),
    ]
    target_add = float(DELTA)
    print(f"  target Δ = {target_add:.10e}")
    for name, val in additive_candidates:
        err = abs(val - target_add) / target_add * 100 if target_add else 0
        print(f"    {name:<22} = {val:>14.6e}  err = {err:>8.2f}%")

    witness = {
        "computation": "alpha-derivation-probe",
        "description": (
            "Probes structural forms for the multiplicative correction "
            "α*/(G/3) - 1 ≈ 0.0016 (where α* = 0.30581 closes neutron "
            "tower to 0 and G/3 = 0.30532 closes to 100 ppm).  Tests "
            "h, ℏ_q, q-integer combinations."
        ),
        "reference_blocks": [
            "thm:frobenius-antipode-unifies-chirality-and-tower",
            "rem:kashaev-volume-density",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        # P2.5 Tier B — expose symbolic forms of the basic q-quantities.
        "polynomial_forms": expose_polynomial_dict(
            {
                "h_q_minus_inverse": h,
                "hbar_q": (q - 1) / q,
                "h_squared": h ** 2,
            },
            q,
            q0=q0,
        ),
        "parameters": {
            "q_0": float(Q0_FLOAT),
            "G_catalan": float(G_CATALAN),
            "G_over_3": float(G_OVER_3),
            "alpha_star": float(ALPHA_STAR),
            "delta": float(DELTA),
            "ratio": float(RATIO),
            "h_val": float(h_val),
            "hbar_q_val": float(hbar_q_val),
        },
        "candidates_multiplicative": [
            {"name": n, "value": v, "err_pct": e}
            for n, v, e in candidates
        ],
    }
    out = Path(__file__).parent / "alpha-derivation-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
