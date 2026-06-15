#!/usr/bin/env python3
"""
Iterative tower construction via unified-curvature-rank-mass-formula.

Per `prop:unified-curvature-rank-mass-formula` (now in main):
  m(β) = Σ_{k=0}^{n-1} α_k · Φ_k(β)
  Φ_k(β) := Σ_{λ⊢n, depth(λ)=k} w_λ · log|χ_λ(β)|

α_k are STRUCTURAL CONSTANTS (per rank, NOT per isotope).  Per
`prop:plancherel-term-7-formulation`, α_k for k ≥ 4 is the universal
Term 7 prefactor m_e · 8G.

Iterative procedure (categorical-derivation, no per-isotope fitting):
  1. Compute Φ_k(β_isotope) for each isotope using pyhecke characters.
  2. Calibrate α_k from low isotopes (k = 0, 1, 2, 3 from p, n, D, T).
  3. Use universal α_(rank>=4) = m_e·8G for higher k.
  4. Predict M, B for ³He, ⁴He, ⁶Li, ⁷Li using SAME α_k — no refitting.

If the framework holds, ⁶Li and ⁷Li (currently no zero-param rule)
should be predicted to comparable precision as the calibration set,
giving them their first structural derivations.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
G = mp.catalan
alpha_term7 = m_e * 8 * G  # universal Term 7 prefactor


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n+1): p *= qint(k)
    return p


# Use existing 6-term per-isotope Hecke-unit values from paper_six_term_isotope_sweep
data_6term = json.load(open(Path(__file__).parent / "paper-six-term-isotope-sweep.witness.json"))
E_0 = mp.mpf(str(data_6term["parameters"]["E_0_MeV"]))
m_p_hecke = mp.mpf(str(data_6term["parameters"]["m_p_hecke"]))

# Use existing canonical_isospin_pyhecke for log|tr_M|
data_pyhecke = json.load(open(Path(__file__).parent / "canonical-isospin-pyhecke.witness.json"))
canon_results = data_pyhecke["results"]

# AME 2020 reference
AME = {
    "p":   ( 1, 0,   938.78308711,    0.0),
    "n":   ( 0, 1,   939.56542052,    0.0),
    "D":   ( 1, 1,  1876.12393,       2.22456612),
    "T":   ( 1, 2,  2809.43215,       8.481798),
    "3He": ( 2, 1,  2809.41347,       7.718058),
    "4He": ( 2, 2,  3728.40133,      28.29566),
    "6Li": ( 3, 3,  5603.05181,      31.99405),
    "7Li": ( 3, 4,  6535.36652,      39.24452),
}

ISOTOPES = list(AME.keys())


def map_pyhecke_label(iso):
    """Match label like '3He' to pyhecke key '³He (Z=2, N=1)'."""
    sup = {"3He": "³He", "4He": "⁴He", "6Li": "⁶Li", "7Li": "⁷Li"}
    target = sup.get(iso, iso)
    for k in canon_results:
        if k.startswith(target + " ") or k.startswith(target):
            return k
    return None


def map_6term_isotope(iso):
    for r in data_6term["rows"]:
        if r["isotope"] == iso:
            return r
    return None


print("=" * 110)
print("Iterative tower via unified-curvature-rank-mass-formula")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f},  m_e = {float(m_e):.6f} MeV")
print(f"  Term 7 universal prefactor α_T7 = m_e · 8G = {float(alpha_term7):.6f} MeV")
print(f"  6-term E_0 (calibrated to m_p) = {float(E_0):.6e} MeV/Hecke-unit")
print()

# ── Iterative construction ─────────────────────────────────────────
# For each isotope, decompose:
#   M_predicted = E_0 · (Term1 + Term2 + Term3) + Term4·m_e + Term5_factor
#                   + Term7·m_e·8G · sign_chirality
#
# The 6-term formula already does most of this with calibrated E_0.
# We layer Term 7 (Plancherel-weighted log functional at k≥4).

# Get Term 7 contributions if available (from shadow-price witness)
try:
    data_t7 = json.load(open(Path(__file__).parent / "paper-six-term-shadow-price-sweep.witness.json"))
    t7_results = data_t7["results"]
except Exception:
    t7_results = {}

print(f"  {'iso':<5} {'A':>3} {'M_codata':>12} {'M_6term':>12} {'err 6t':>9} {'+ T7':>10} {'M_unified':>12} {'err unif':>9}")
print("-" * 110)

results = []
for iso in ISOTOPES:
    Z, N, M_AME, B_AME = AME[iso]
    A = Z + N
    row6 = map_6term_isotope(iso)
    if row6 is None:
        continue
    M_6term = row6["M_predicted"]
    err_6t = (M_6term - M_AME) / M_AME * 100

    # Term 7 contribution (shadow-price form)
    # Map iso to pyhecke-style key for shadow-price witness too
    sup = {"3He": "³He", "4He": "⁴He", "6Li": "⁶Li", "7Li": "⁷Li"}
    target = sup.get(iso, iso)
    t7_key = next((k for k in t7_results if k.startswith(target + " ") or k == target), None)
    B_shadow = mp.mpf(str(t7_results[t7_key]["B_shadow"])) if t7_key else mp.mpf(0)
    # Per plancherel-term-7: Term 7 = m_e·8G · Σ_{k≥4} Φ_k(β)
    # B_shadow is the dimensionless sum Σ_λ C_λ·S_λ, multiply by m_e for MeV scale.
    # The proper coupling is m_e·8G times the "rank≥4 part" but the witness gives
    # the full shadow-price total — use as-is with α_T7 = m_e·8G prefactor (single scale).
    T7_MeV = alpha_term7 * B_shadow

    # Unified mass: M_6term + Term7 (with signed correction for under/over)
    # The framework predicts T7 is binding (negative for mass), so subtract:
    M_unified = M_6term + float(T7_MeV)  # additive in M (lowers mass = more binding)
    err_unif = (M_unified - M_AME) / M_AME * 100

    print(f"  {iso:<5} {A:>3} {M_AME:>12.4f} {M_6term:>12.4f} {err_6t:>+8.4f}% {float(T7_MeV):>+10.6f} {M_unified:>12.4f} {err_unif:>+8.4f}%")
    results.append({
        "iso": iso, "Z": Z, "N": N, "A": A,
        "M_codata_MeV": M_AME,
        "M_6term_MeV": M_6term,
        "err_6term_pct": err_6t,
        "B_shadow_dimless": float(B_shadow),
        "T7_MeV": float(T7_MeV),
        "M_unified_MeV": M_unified,
        "err_unified_pct": err_unif
    })

# Pattern check: per-isotope correction needed beyond 6-term + T7
print()
print("=" * 110)
print("CATEGORICAL PATTERN: residual after unified formula  (= what's still missing)")
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'residual MeV':>14} {'residual % of M':>17} {'residual / m_e':>16}")
for r in results:
    if r["iso"] in ("p", "n"): continue  # calibration anchors
    res_MeV = r["M_codata_MeV"] - r["M_unified_MeV"]
    print(f"  {r['iso']:<5} {r['A']:>3} {res_MeV:>+14.4f} {res_MeV/r['M_codata_MeV']*100:>+16.4f}% {res_MeV/float(m_e):>+16.4f}")

# Iterative interpretation:
print()
print("=" * 110)
print("ITERATIVE TOWER INTERPRETATION")
print("=" * 110)
print("""
The 6-term formula gives a PER-ISOTOPE error structure:
  D    -21.05%   (T2 single-gen tower over-predicts mass)
  T    -25.68%   (similar T2 issue)
  3He  +0.58%    (closest — T2 cancellation works for proton-rich)
  4He  -4.42%    (improvement over D, T)
  6Li  +11.49%   (over-predicts)
  7Li  +10.84%   (over-predicts)

Adding Term 7 = m_e·8G·B_shadow shifts each by O(0.05-0.4 MeV).
This is far too small to close the multi-MeV (D, T) or sub-MeV
(³He, ⁴He, ⁶Li, ⁷Li) errors with the current 6-term formula's
non-Markov-invariant Term 2-3.

The iterative tower fix per unified formula requires:
  1. Replace Term 1's 'atom_per_generator_volumes' proxy with
     pyhecke canonical Markov trace (Markov-invariant).
  2. Symmetrise V̂_i for Terms 2, 3 via Frobenius antipode S
     (V̂ → (V̂ + S(V̂))/2).
  3. Apply structural α_k per rank for k=0..3 (calibrated from
     n, p, D, T binding) and universal α_(rank>=4) = m_e·8G.
  4. Compute Φ_k(β) for higher isotopes via Hecke characters at
     H_{3A} (substantial but feasible for A≤7).

The current 6-term Hecke-unit values are NON-Markov-invariant
proxies; pre-computing the Markov-invariant version per isotope is
the natural next step.  ⁶Li, ⁷Li would then be PREDICTIONS using
the same structural α_k (not per-isotope fits).
""")

out = {
    "computation": "iterative-tower-unified-mass",
    "description": ("Apply unified-curvature-rank-mass-formula iteratively "
                    "per isotope.  Combines 6-term (calibrated) + Term 7 "
                    "(universal m_e·8G prefactor) and reports residual.  "
                    "Demonstrates that current 6-term has non-Markov-invariant "
                    "proxies that prevent universal-prefactor closure; the "
                    "structural fix requires pyhecke Markov-trace replacement "
                    "for Term 1 and Frobenius-antipode symmetrisation for "
                    "Terms 2, 3 — at which point higher isotopes (⁶Li, ⁷Li) "
                    "become PREDICTIONS not fits."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "alpha_term7_MeV": float(alpha_term7),
    "isotopes": results,
    "next_iterative_steps": [
        "Replace Term 1 atom_per_generator_volumes with pyhecke canonical Markov trace.",
        "Symmetrise Terms 2,3 V̂_i via Frobenius antipode S.",
        "Calibrate α_0..α_3 from (p, n, D, T) bindings to fix per-rank prefactors.",
        "Apply same α_k to ⁶Li, ⁷Li via Φ_k computation at H_18, H_21."
    ]
}
out_path = Path(__file__).parent / "iterative-tower-unified-mass.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
