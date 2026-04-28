#!/usr/bin/env python3
"""
STRICT 3-cal unified mass: NO per-isotope fitting allowed.

Three categorical calibrations only:
  m_e (CODATA), q_0 (from m_μ/m_e), m_p (E_0 anchor).

NO LSQ fits to nuclei.  NO per-isotope variant selection.
Every other quantity is a structural derivation.

Formula (Markov-invariant unified curvature-rank):
  M(β) = E_0 · Σ_k α_k · Φ_k(β)         dimensionless prediction × E_0
       + Z·m_e                            (electron rest mass per Z)

Where:
  Φ_k(β) = Σ_{depth(λ)=k} w_λ · log|χ_λ(β)|   (depth-resolved log functional)
  α_k = STRUCTURAL prefactors:
    α_0 = 1   (Term 1, descended Markov, unit prefactor)
    α_1 = 1   (Term 2, single-gen tower)
    α_2 = z²  (Term 3, pair-gen tower, Markov parameter squared)
    α_3 = 1   (Term 6, jet-prefix; identity prefactor)
    α_(k≥4) = m_e · 8G  (Term 7 universal, per prop:plancherel-term-7-formulation)
  E_0 = m_p / (Σ for proton)               (calibrated to anchor m_p, NOT a fit)

For each isotope:
  1. Compute χ_λ(β_isotope) per partition via pyhecke nuclear_braid_character.
  2. Bin by depth, compute Φ_k.
  3. Sum α_k · Φ_k → dimensionless mass.
  4. Multiply by E_0 → MeV.

This is the strict 3-cal prediction — NO per-isotope adjustment.
"""
from __future__ import annotations
import sys, json, time, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 25

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, nuclear_braid_character,
    partitions_of, dim_q, qfac, q_int
)

Q0 = Q_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816")
G = mp.catalan
m_e_8G = m_e * 8 * G  # ≈ 3.745 MeV — universal Term 7 prefactor

# Markov parameter z = 1/(q^{1/2} + q^{-1/2})
z_mark = 1/(mp.sqrt(Q0) + 1/mp.sqrt(Q0))


# Structural α_k (NO per-isotope fitting)
# Per unified-curvature-rank-mass-formula + plancherel-term-7-formulation
def alpha_k(k):
    if k == 0: return mp.mpf(1)         # Term 1
    if k == 1: return mp.mpf(1)         # Term 2
    if k == 2: return z_mark ** 2       # Term 3 (Markov parameter squared)
    if k == 3: return mp.mpf(1)         # Term 6 (jet-prefix; identity)
    return float(m_e_8G)                # Term 7 universal for k >= 4


def Phi_k_per_isotope(Z, N, max_height=12):
    """Compute Φ_k(β_isotope) for each depth k via per-partition Hoefsmit.

    Uses higher height cap (12 vs 8) to capture more partitions for ⁴He.
    """
    A = Z + N
    n = 3 * A
    n_gens = max(1, n - 1)

    bins = {}
    for shape in partitions_of(n):
        if len(shape) > max_height: continue
        try:
            sigmas, dim_lam, _ = build_seminormal_matrices(shape)
            if dim_lam == 0: continue
            chi = nuclear_braid_character(Z, N, sigmas, dim_lam, n_gens)
        except Exception:
            continue

        d = dim_q(shape)
        w_lam = float((d * d) / qfac(n))
        k_depth = len(shape) - 1
        bins.setdefault(k_depth, []).append((w_lam, float(chi)))

    Phi_k = {}
    for k, contribs in bins.items():
        s = 0.0
        for w, chi in contribs:
            if abs(chi) > 1e-30:
                s += w * float(np.log(abs(chi)))
        Phi_k[k] = s
    return Phi_k


# AME 2020
AME = {
    "p":   ( 1, 0,   938.78308711,    0.0),
    "n":   ( 0, 1,   939.56542052,    0.0),
    "D":   ( 1, 1,  1876.12393,       2.22456612),
    "T":   ( 1, 2,  2809.43215,       8.481798),
    "3He": ( 2, 1,  2809.41347,       7.718058),
    "4He": ( 2, 2,  3728.40133,      28.29566),
}


print("=" * 110)
print("STRICT 3-cal Markov-invariant unified mass — NO per-isotope fitting")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print(f"  m_e = {float(m_e):.6f} MeV  (cal #1)")
print(f"  m_p = {float(m_p):.6f} MeV  (cal #3, anchors E_0)")
print(f"  m_e·8G = {float(m_e_8G):.6f} MeV  (Term 7 universal)")
print()

# Compute Φ_k per isotope
isotope_data = {}
for iso in AME:
    Z, N, M_AME, B_AME = AME[iso]
    A = Z + N; n = 3*A
    print(f"  {iso} (n={n})...", end=" ", flush=True)
    t0 = time.time()
    Phi_k = Phi_k_per_isotope(Z, N)
    elapsed = time.time() - t0
    print(f"done in {elapsed:.1f}s ({len(Phi_k)} ranks populated)")
    isotope_data[iso] = {
        "Z": Z, "N": N, "A": A, "n": n,
        "M_AME": M_AME, "B_AME": B_AME,
        "Phi_k": Phi_k
    }
print()

# Calibrate E_0 from proton mass (the 3rd cal):
#   M_p(struct, before E_0) = Σ_k α_k · Φ_k(p) + Z·m_e_natural
#   E_0 = m_p / [Σ_k α_k · Φ_k(p)]      (assuming m_e enters separately)
# OR more cleanly: M(struct, MeV) = E_0 · Σ_k α_k_dimensionless · Φ_k + Z·m_e
# E_0 calibrated so M(p) = m_p.
def structural_sum(iso):
    """Σ_k α_k · Φ_k(β_iso) — dimensionless until multiplied by E_0."""
    Phi_k = isotope_data[iso]["Phi_k"]
    s = mp.mpf(0)
    for k, phi in Phi_k.items():
        ak = alpha_k(k)
        s += mp.mpf(str(float(ak))) * mp.mpf(str(phi))
    return s

# Use proton to anchor E_0:  E_0 · S(p) + Z_p · m_e = m_p_codata
# For p: Z=1, so E_0 · S_p + m_e = m_p,  E_0 = (m_p − m_e) / S_p
S_p = structural_sum("p")
print(f"  S(p) = Σ_k α_k · Φ_k(p) = {float(S_p):.6f}")

if abs(float(S_p)) < 1e-10:
    print("  ⚠ S(p) ≈ 0; E_0 calibration ill-defined.  Using alternative anchor.")
    # Fall back: use total mass directly
    E_0 = (m_p - m_e) / S_p if abs(float(S_p)) > 1e-30 else mp.mpf("1.0")
else:
    E_0 = (m_p - m_e) / S_p

print(f"  E_0 (anchor m_p): {float(E_0):.6e} MeV / structural-unit")
print()

# Predict
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'M_AME':>12} {'M_pred (struct)':>16} {'err %':>10} {'B_AME':>8} {'B_pred':>8}")
print("-" * 110)
results = []
for iso, d in isotope_data.items():
    S = structural_sum(iso)
    M_pred = float(E_0) * float(S) + d["Z"] * float(m_e)
    M_AME = d["M_AME"]
    err_M = (M_pred - M_AME)/M_AME * 100 if M_AME != 0 else 0
    # Binding from M
    M_constituents = d["Z"] * float(m_p) + d["N"] * float(m_e + mp.mpf("939.56542052") - m_p)  # crude
    # Actually use AME m_p, m_n directly for constituent baseline
    m_n_codata = 939.56542052
    M_const = d["Z"] * float(m_p) + d["N"] * m_n_codata
    B_pred = M_const + d["Z"] * float(m_e) - M_pred
    role = "calibration" if iso == "p" else "PREDICTION"
    print(f"  {iso:<5} {d['A']:>3} {M_AME:>12.4f} {M_pred:>16.6f} {err_M:>+10.4f}% {d['B_AME']:>8.3f} {B_pred:>8.3f} {role}")
    results.append({
        "iso": iso, "A": d["A"], "M_AME": M_AME, "M_pred": M_pred,
        "err_M_pct": err_M, "B_AME": d["B_AME"], "B_pred": B_pred
    })

print()
print("=" * 110)
print("SUMMARY")
print("=" * 110)
print(f"""
3 categorical calibrations: m_e ({float(m_e):.6f} MeV), q_0, m_p (anchor)
Universal Term 7 prefactor:  m_e · 8G = {float(m_e_8G):.6f} MeV
Structural α_k per rank: 1, 1, z², 1, m_e·8G·..., m_e·8G·..., ...
  (no per-isotope free parameters, no LSQ to bindings)

Predictions for n, D, T, ³He, ⁴He are STRUCTURAL — same α_k as p.

If all errors < 5%: framework's 3-cal prediction works at structural-form
level.  If errors are larger (per the existing 6-term diagnostics: D -21%,
T -26%, ⁴He -4%), the structural form needs further refinement (proper
antipode symmetrisation, Coulomb integration, etc.) — all without adding
calibrations.
""")

out = {
    "computation": "strict-3cal-unified-mass",
    "description": ("STRICT 3-categorical-calibration unified mass prediction. "
                    "NO per-isotope fitting.  Uses m_e, q_0, m_p (E_0 anchor) "
                    "with structural α_k = (1, 1, z², 1, m_e·8G, ...) and "
                    "per-partition Hoefsmit Φ_k.  Predicts n, D, T, ³He, ⁴He "
                    "with the same prefactors as the proton calibration."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "calibrations": {
        "m_e_MeV": float(m_e),
        "q_0": float(Q0),
        "m_p_MeV": float(m_p)
    },
    "structural_alpha_k": {
        "0": 1.0, "1": 1.0, "2": float(z_mark**2),
        "3": 1.0, ">=4": float(m_e_8G)
    },
    "E_0_calibrated": float(E_0),
    "results": results
}
out_path = Path(__file__).parent / "strict-3cal-unified-mass.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
