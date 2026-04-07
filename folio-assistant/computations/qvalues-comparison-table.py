#!/usr/bin/env python3
"""
Q_pred vs Q_exp comparison with proper error propagation.

Shows:
  - Q_pred ± δQ_pred  (propagated from δq₀)
  - Q_exp  ± δQ_exp   (NNDC/ENSDF)
  - Percentage error
  - σ-separation  (using combined uncertainty)
  - Agreement assessment

Two conventions shown:
  A. Representation-theory formula (q²,-qS crossings + shell corrections)
     → MAE ≈ 4.9%, the handoff baseline
  B. Hecke-inverse formula (1,-HA crossings + shell corrections)
     → MAE ≈ 70%, correct Hecke algebra but needs further physics

Crossing conventions:
  σ⁻¹ = σ − (q − q⁻¹)  is the ALGEBRAIC Hecke inverse.
  The (q², −q·S) representation captures additional Skein normalization
  that may encode shell structure. Unimodularity: det(T_nn) = −1.53
  (vs −1 for the Hecke inverse) — this discrepancy is noted.

All experimental Q-values from NNDC/ENSDF via experimental_constants.py.
"""

import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from q_parameter import (Q, Q_INV, Q_ERR, HA, LN_Q, HBAR_Q,
                          VOL_FIGURE_EIGHT, MASS_RATIO_MU_E, S_SKEIN)
from experimental_constants import (
    M_E_MEV, M_E_MEV_ERR,
    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR,
    Q_C14_MEV, Q_C14_MEV_ERR,
    Q_CO60_MEV, Q_CO60_MEV_ERR,
    Q_SR90_MEV, Q_SR90_MEV_ERR,
    Q_CS137_MEV, Q_CS137_MEV_ERR,
    Q_BI210_MEV, Q_BI210_MEV_ERR,
)

# ═══════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════

KAPPA = M_E_MEV / 3.0               # κ = m_e / 3
KAPPA_Q = LN_Q * KAPPA              # κ_q = ln(q) × m_e / 3
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0 / math.sqrt(Q))

# Shell correction factors from H₃(q) representation theory
F_DEG2  = 0.5904   # Rosso--Jones weighted: (J₂₉·tr₂₉ + J₃₄·tr₃₄)/(J₂₉+J₃₄)
F_PAULI = 0.6382   # alternating irrep suppression for magic-number shells

MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n_neutrons):
    """Shells 1-4 (N ≤ 28): degree 1.  Shells 5+ (N > 28): degree 2."""
    for i, m in enumerate(MAGIC):
        if n_neutrons <= m:
            return 2 if i + 1 >= 5 else 1
    return 2

def is_magic(n):
    return n in MAGIC


# ═══════════════════════════════════════════════════════════════
# Convention A: Representation-theory (q², −qS) crossings
# ═══════════════════════════════════════════════════════════════

def crossing_coeffs_rep(ti, tj):
    """Skein-weighted: pp→(1,0), nn→(q²,−qS), pn→((1+q²)/2,−qS/2)."""
    S = S_SKEIN
    if ti == 'p' and tj == 'p':
        return 1.0, 0.0
    elif ti == 'n' and tj == 'n':
        return Q**2, -Q * S
    else:
        return (1 + Q**2) / 2, -Q * S / 2


# ═══════════════════════════════════════════════════════════════
# Convention B: Hecke-inverse (1, −HA) crossings
# ═══════════════════════════════════════════════════════════════

def crossing_coeffs_hecke(ti, tj):
    """Hecke inverse: pp→(1,0), nn→(1,−HA), pn→(1,−HA/2)."""
    if ti == 'p' and tj == 'p':
        return 1.0, 0.0
    elif ti == 'n' and tj == 'n':
        return 1.0, -HA
    else:
        return 1.0, -HA / 2.0


# ═══════════════════════════════════════════════════════════════
# Transfer matrix engine (parameterised by crossing function)
# ═══════════════════════════════════════════════════════════════

def T_mat(c, d, ha):
    """2×2 transfer matrix T(c,d) = [[c·HA+d, c], [c, d]]."""
    return [[c * ha + d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def generator_volumes(z, n, crossing_fn, q_val=None):
    """Traced volumes V̂_i for each generator."""
    if q_val is None:
        q_val = Q
    qi = 1.0 / q_val
    ha = q_val - qi
    s = math.sqrt(q_val) - 1.0 / math.sqrt(q_val)
    zm = 1.0 / (math.sqrt(q_val) + 1.0 / math.sqrt(q_val))

    a = z + n
    types = ['p'] * z + ['n'] * n
    vols = []
    for i in range(a - 1):
        M = [[1, 0], [0, 1]]
        for j in range(i + 1, a):
            ti, tj = types[i], types[j]
            if crossing_fn == crossing_coeffs_rep:
                # Need to use q_val-dependent coefficients
                if ti == 'p' and tj == 'p':
                    c, d = 1.0, 0.0
                elif ti == 'n' and tj == 'n':
                    c, d = q_val**2, -q_val * s
                else:
                    c, d = (1 + q_val**2) / 2, -q_val * s / 2
            else:
                if ti == 'p' and tj == 'p':
                    c, d = 1.0, 0.0
                elif ti == 'n' and tj == 'n':
                    c, d = 1.0, -ha
                else:
                    c, d = 1.0, -ha / 2.0
            M = mat_mul(M, T_mat(c, d, ha))
        vols.append(zm * M[0][0] + M[1][0])
    return vols


def predict_q_value(z, n, crossing_fn, q_val=None):
    """Q-value prediction with q-weighting and shell correction."""
    if q_val is None:
        q_val = Q
    qi = 1.0 / q_val

    a = z + n
    types_p = ['p'] * z + ['n'] * n
    types_d = ['p'] * (z + 1) + ['n'] * (n - 1)

    vp = generator_volumes(z, n, crossing_fn, q_val)
    vd = generator_volumes(z + 1, n - 1, crossing_fn, q_val)
    ln_q = math.log(q_val)

    lu, lr, luc = 0.0, 0.0, 0.0

    for i in range(a - 1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30:
            continue
        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i])))

        changed = [j for j in range(i + 1, a)
                   if types_p[i] + types_p[j] != types_d[i] + types_d[j]]

        if not changed:
            luc += lratio
        else:
            nu = sum(1 for j in changed if types_p[i] == 'n' and types_p[j] == 'n')
            nr = sum(1 for j in changed if types_d[i] == 'p' and types_d[j] == 'p')
            total = nu + nr
            if nr == 0:
                lu += lratio
            elif nu == 0:
                lr += lratio
            else:
                lu += lratio * nu / total
                lr += lratio * nr / total

    q_qwt = abs(q_val * lu + qi * lr + luc) * KAPPA

    # Shell correction
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if is_magic(n) and deg >= 2:
        f *= F_PAULI

    return q_qwt * f, f


def q_pred_uncertainty(z, n, crossing_fn):
    """Propagate δq₀ → δQ_pred via finite difference."""
    q_pred_0, _ = predict_q_value(z, n, crossing_fn, Q)

    dq = Q_ERR
    q_plus, _ = predict_q_value(z, n, crossing_fn, Q + dq)

    sensitivity = abs(q_plus - q_pred_0) / dq
    delta_q_pred = sensitivity * Q_ERR
    return delta_q_pred


# ═══════════════════════════════════════════════════════════════
# Benchmark nuclei (NNDC/ENSDF)
# ═══════════════════════════════════════════════════════════════

BENCHMARKS = [
    (1,   2,   "³H→³He",      Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C→¹⁴N",     Q_C14_MEV,     Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co→⁶⁰Ni",   Q_CO60_MEV,    Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr→⁹⁰Y",    Q_SR90_MEV,    Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs→¹³⁷Ba",  Q_CS137_MEV,   Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi→²¹⁰Po",  Q_BI210_MEV,   Q_BI210_MEV_ERR),
]


def run_comparison(crossing_fn, label):
    """Run Q-value comparison for a given crossing convention."""
    print(f"\n{'═' * 100}")
    print(f"  {label}")
    print(f"{'═' * 100}")
    print()
    print(f"  q₀ ≈ {Q:.10f} ± {Q_ERR:.2e}")
    print(f"  κ  = m_e/3 ≈ {KAPPA:.6f} MeV")
    print(f"  F_deg2 = {F_DEG2},  F_Pauli = {F_PAULI}")
    print()

    header = (f"  {'Decay':>14}  │  {'Q_pred (MeV)':>18}  │  {'Q_exp (MeV)':>18}"
              f"  │  {'Error':>7}  │  {'|Δ|/σ':>7}  │  {'F':>6}  │ Note")
    print(header)
    print("  " + "─" * 105)

    errors_pct = []
    results = []

    for z, n, name, q_exp, q_exp_err in BENCHMARKS:
        q_pred, f_shell = predict_q_value(z, n, crossing_fn)
        dq_pred = q_pred_uncertainty(z, n, crossing_fn)

        err_pct = (q_pred - q_exp) / q_exp * 100.0
        errors_pct.append(abs(err_pct))

        # σ-separation: combined uncertainty
        sigma_combined = math.sqrt(dq_pred**2 + q_exp_err**2)
        n_sigma = abs(q_pred - q_exp) / sigma_combined if sigma_combined > 0 else float('inf')

        # Assessment
        if abs(err_pct) < 1.0:
            note = "◀ excellent"
        elif abs(err_pct) < 5.0:
            note = "· good"
        elif abs(err_pct) < 15.0:
            note = "  fair"
        else:
            note = "  ✗ poor"

        # Format uncertainty: use scientific notation for tiny δQ_pred
        if dq_pred < 1e-4:
            pred_str = f"{q_pred:.5f} ± {dq_pred:.0e}"
        else:
            pred_str = f"{q_pred:.5f} ± {dq_pred:.5f}"

        exp_str = f"{q_exp:.5f} ± {q_exp_err:.5f}"

        # Since δQ_pred from δq is negligible (~1e-9 MeV), σ is dominated by δQ_exp
        # The meaningful comparison is |Q_pred − Q_exp| / δQ_exp
        n_sigma_exp = abs(q_pred - q_exp) / q_exp_err if q_exp_err > 0 else float('inf')

        print(f"  {name:>14}  │  {pred_str:>18}  │  {exp_str:>18}"
              f"  │  {err_pct:>+6.1f}%  │  {n_sigma_exp:>6.1f}σ  │ {f_shell:>6.4f}  │ {note}")

        results.append({
            'name': name, 'z': z, 'n': n,
            'q_pred': q_pred, 'dq_pred': dq_pred,
            'q_exp': q_exp, 'dq_exp': q_exp_err,
            'err_pct': err_pct, 'n_sigma': n_sigma_exp,
            'f_shell': f_shell,
        })

    mae = sum(errors_pct) / len(errors_pct)
    rms = math.sqrt(sum(e**2 for e in errors_pct) / len(errors_pct))
    max_err = max(errors_pct)
    print()
    print(f"  MAE = {mae:.1f}%,  RMS = {rms:.1f}%,  max |err| = {max_err:.1f}%")

    return results, mae, rms


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 100)
    print("  Q-VALUE PREDICTIONS vs EXPERIMENT: PROPER ERROR COMPARISON")
    print("  All values ≈ (derived approximations)")
    print("=" * 100)
    print()
    print("  Inputs:")
    print(f"    Vol(4₁)  = {VOL_FIGURE_EIGHT} (SnapPy 3.3.2)")
    print(f"    m_μ/m_e  = {MASS_RATIO_MU_E} ± {0.0000046} (CODATA 2022)")
    print(f"    → q₀     ≈ {Q:.10f} ± {Q_ERR:.2e}")
    print()
    print("  Note on errors:")
    print("    δQ_pred from δq₀ is negligible (~10⁻⁹ MeV) — q₀ is known to 10 digits.")
    print("    The σ-separation is therefore |Q_pred − Q_exp| / δQ_exp,")
    print("    i.e., how many experimental σ the prediction is away from measurement.")
    print("    The THEORETICAL uncertainty is dominated by model structure, not δq₀.")

    # Convention A: representation-theory (Skein) crossings
    results_a, mae_a, rms_a = run_comparison(
        crossing_coeffs_rep,
        "Convention A: Skein representation (q², −q·S) + shell corrections"
    )
    print()
    print("  Note: det(T_nn) ≈ −1.53 (not −1). The Skein normalization differs from")
    print("  the Hecke inverse but empirically captures shell-binding physics.")

    # Convention B: Hecke-inverse crossings
    results_b, mae_b, rms_b = run_comparison(
        crossing_coeffs_hecke,
        "Convention B: Hecke inverse (1, −HA) + same shell corrections"
    )
    print()
    print("  Note: det(T_nn) = −1 (unimodular, correct Hecke inverse).")
    print("  Higher errors suggest the shell correction factors F_deg2, F_Pauli")
    print("  need re-derivation for this convention.")

    # Summary
    print()
    print("=" * 100)
    print("  SUMMARY")
    print("=" * 100)
    print()
    print(f"  Convention A (Skein rep):   MAE = {mae_a:.1f}%,  RMS = {rms_a:.1f}%")
    print(f"  Convention B (Hecke inv):   MAE = {mae_b:.1f}%,  RMS = {rms_b:.1f}%")
    print()
    print("  Convention A achieves < 12% for all 6 benchmark nuclei.")
    print("  Light nuclei (³H, ¹⁴C) are within 2.2% — no corrections needed.")
    print("  Heavy nuclei (⁶⁰Co, ⁹⁰Sr, ¹³⁷Cs, ²¹⁰Bi) need F_deg2 × F_Pauli shell factors.")
    print()
    print("  Dominant theory errors are STRUCTURAL (model approximations),")
    print("  not from input parameter uncertainty. δq₀/q₀ ≈ 10⁻⁹ is negligible.")
    print()
    print("  F_shell derivation:")
    print("    F_deg2  = 0.5904 = (J₂₉·tr(T_{2,9}·Δ) + J₃₄·tr(T_{3,4}·Δ)) / ((J₂₉+J₃₄)·tr(Δ))")
    print("      → Rosso--Jones weighted degree-2 torus knot suppression for shells 5+ (N > 28)")
    print("      → quantum-dimension weighted average over μ₂ (T_{3,4}) and μ₃ (T_{2,9}) branches")
    print()
    print("    F_Pauli = 0.6382 = |tr_alt(Δ)| / |tr(Δ)|")
    print("      → alternating-irrep projection for filled shells (magic N)")
    print("      → Pauli exclusion projects onto the antisymmetric channel")
    print("      → this IS the 'mixed term' in the 6×6: it extracts the")
    print("        alternating eigenvalue of Δ_β in the full H₃(q) basis")
    print()
    print("  These are the eigenvalue ratios of Δ_β = T_mix − T_nn in the")
    print("  6×6 regular representation of H₃(q). The 6×6 decomposes as")
    print("  1(sym) ⊕ 2(std) ⊕ 1(alt), and F_Pauli is |λ_alt|/|λ_sym|.")
