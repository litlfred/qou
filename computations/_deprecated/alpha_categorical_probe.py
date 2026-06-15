#!/usr/bin/env python3
"""
Categorical probe for α ≈ 342.5 MeV.

The Term6/A³ binding fit (gs_term6_normalization.py) yields:
    B/A ≈ α · (Term6/A³) + β,    α = 342.5 MeV,  β = 1.20 MeV.

The framework's calibrations are:
    m_e (CAL-0, H^0)        = 0.51100 MeV
    q_0 (CAL-1, H^1)        = 1.10998
    E_0 (CAL-2, H^2)        = Q_β / |Δ(net)| ≈ 4.18 MeV
    m_μ / m_e               = 206.77 (= Vol(4_1) / ℏ_q²)

This probe enumerates candidate categorical expressions for α
and ranks by relative error vs the fit. Goal: identify a clean
(< 1% error) expression in q-integers + m_e + E_0 + m_μ/m_e
that gives α structurally.

Note on epistemics: the fitted α = 342.5 MeV has uncertainty
~5-10% from the 7-atom LSQ fit (residual σ = 1.09 MeV). Any
candidate within ~10% is a viable structural match; below ~1%
is strong evidence.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath
import sys

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0


def q_int(k: int) -> float:
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return 0.0
    return float((q0 ** k - q0 ** (-k)) / (q0 - q0 ** (-1)))


def q_fact(k: int) -> float:
    return float(np.prod([q_int(i) for i in range(1, k + 1)])) if k > 0 else 1.0


# Constants
M_E_MEV = 0.51099895
M_MU_OVER_M_E = 206.7682830
E_0_MEV = 4.18  # rough; from Q_β / |Δ_net|
ALPHA_FIT = 342.5

print(f"  q_0 = {float(q0):.6f}")
print(f"  m_e = {M_E_MEV} MeV")
print(f"  m_μ/m_e = {M_MU_OVER_M_E}")
print(f"  E_0 = {E_0_MEV} MeV")
print()
print(f"  q-integers:")
for k in range(2, 11):
    print(f"    [{k}]_q = {q_int(k):.4f}")
print()
print(f"  Target: α = {ALPHA_FIT} MeV")
print()


# ─── Candidate expressions ──────────────────────────────────────────
candidates = []


def cand(name: str, value: float):
    err = (value - ALPHA_FIT) / ALPHA_FIT * 100
    candidates.append({"name": name, "value": value, "err_pct": err})


# m_e × q-integer combos
cand("m_e · [3]_q · [4]_q · [5]_q · [5]_q",
     M_E_MEV * q_int(3) * q_int(4) * q_int(5) ** 2)
cand("2 · m_e · [3]_q · [4]_q · [5]_q²",
     2 * M_E_MEV * q_int(3) * q_int(4) * q_int(5) ** 2)
cand("m_e · [3]_q · [4]_q · [5]_q · [6]_q",
     M_E_MEV * q_int(3) * q_int(4) * q_int(5) * q_int(6))
cand("m_e · [4]_q · [5]_q · [6]_q · [7]_q",
     M_E_MEV * q_int(4) * q_int(5) * q_int(6) * q_int(7))
cand("m_e · [3]_q² · [4]_q² · [5]_q",
     M_E_MEV * q_int(3) ** 2 * q_int(4) ** 2 * q_int(5))
cand("m_e · [3]_q · [4]_q · [5]_q · [6]_q · [7]_q / [2]_q",
     M_E_MEV * q_int(3) * q_int(4) * q_int(5) * q_int(6) * q_int(7) / q_int(2))

# E_0 × magic numbers
cand("E_0 · 82 (Pb shell)", E_0_MEV * 82)
cand("E_0 · 80",            E_0_MEV * 80)
cand("E_0 · [82]_q^(1/2)",  E_0_MEV * float(mpmath.sqrt(q_int(82))))
cand("E_0 · 4 · 20 (Z·N at 4×20)", E_0_MEV * 80)

# m_e · m_μ/m_e × q
cand("m_e · m_μ/m_e · [3]_q",
     M_E_MEV * M_MU_OVER_M_E * q_int(3))
cand("m_e · m_μ/m_e",
     M_E_MEV * M_MU_OVER_M_E)
cand("m_e · m_μ/m_e · [3]_q / 2",
     M_E_MEV * M_MU_OVER_M_E * q_int(3) / 2)

# Bring volume + Borromean
V_BORROMEAN = 7.32772
cand("V_Bor · m_e · m_μ/m_e / [3]_q",
     V_BORROMEAN * M_E_MEV * M_MU_OVER_M_E / q_int(3))
cand("V_Bor² · m_e · 2",
     V_BORROMEAN ** 2 * M_E_MEV * 2)

# m_e · q-factorial fragments
cand("m_e · [5]_q!",         M_E_MEV * q_fact(5))
cand("m_e · [4]_q! · [3]_q", M_E_MEV * q_fact(4) * q_int(3))
cand("m_e · [4]_q! · [4]_q", M_E_MEV * q_fact(4) * q_int(4))

# Pure q-integers (no m_e prefactor — checking dimensional analysis)
cand("[7]_q · [8]_q · [9]_q (·1 MeV implicit)",
     q_int(7) * q_int(8) * q_int(9))
cand("[10]_q · [9]_q · [4]_q",
     q_int(10) * q_int(9) * q_int(4))


# ─── Rank by absolute error ─────────────────────────────────────────
candidates.sort(key=lambda c: abs(c["err_pct"]))

print(f"  {'expression':<55} {'value (MeV)':>12} {'% err':>10}")
print("  " + "-" * 80)
for c in candidates[:15]:
    marker = "★" if abs(c["err_pct"]) < 1 else (
        "✓" if abs(c["err_pct"]) < 5 else " ")
    print(f"  {marker} {c['name']:<53} {c['value']:>12.4f} "
          f"{c['err_pct']:>+10.4f}")

# Best candidate
best = candidates[0]
print()
print(f"  Best match: {best['name']}")
print(f"             value = {best['value']:.4f} MeV")
print(f"             error = {best['err_pct']:+.4f}%")
print()
print(f"  Note: fit uncertainty on α is ~5-10% (residual σ = 1.09 MeV / 7 atoms);")
print(f"        candidates < 5% error are viable; < 1% is strong evidence.")

out = {
    "computation": "alpha-categorical-probe",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "alpha_fit_MeV": ALPHA_FIT,
    "fit_uncertainty_pct": "~5-10",
    "constants": {
        "q_0": float(q0),
        "m_e_MeV": M_E_MEV,
        "m_mu_over_m_e": M_MU_OVER_M_E,
        "E_0_MeV": E_0_MEV,
    },
    "q_integers": {f"[{k}]_q": q_int(k) for k in range(2, 11)},
    "candidates": candidates,
    "interpretation": (
        "Probe enumerates candidate categorical expressions for the "
        "fitted slope α ≈ 342.5 MeV in the Term6/A³ binding-energy "
        "formula. Ranks by % error. None below 1% is strong evidence "
        "that α has not yet been derived from first principles; "
        "candidates within ~5-10% are within fit uncertainty."
    ),
}
p_out = (Path(__file__).parent.parent.parent
         / "docs/audits/2026-05-02-alpha-categorical-probe.witness.json")
p_out.write_text(json.dumps(out, indent=2, default=str))
print()
print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")
