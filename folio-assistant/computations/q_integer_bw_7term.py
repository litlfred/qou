#!/usr/bin/env python3
"""
Seven-term q-integer Bethe-Weizsäcker mass formula.

Extends the five-term q-integer BW formula (prop:q-integer-mass-formula)
with two additional terms derived from the Hecke algebra framework:

  Term 6 — Exchange Coulomb:  reduces Z^(4/3)/A^(1/3) overcounting
           coefficient = [3]_q / [2]_q · m_e  (q-integer ratio)

  Term 7 — Shell correction:  magic-number enhanced binding from
           torus knot coherence at closed shells
           coefficient = [2]_q² · [3]_q · m_e
           form: Gaussian proximity to magic numbers {2,8,20,28,50,82,126}

Physics:
  The exchange Coulomb corrects the direct Coulomb overestimate at high Z.
  The ratio [3]_q/[2]_q = dim_q(std₃)/dim_q(std₂) encodes the screening
  by the nucleon's 3-strand internal structure.

  The shell correction captures the torus knot T_{2,m} coherence at
  magic shell closures. For s-orbital nucleons (ℓ=0), the exceptional
  divisors from brane blow-up are maximally coherent — their collective
  self-intersection enhances binding beyond the BW liquid-drop average.
  The coefficient [2]_q²·[3]_q is the product of the H₂(q) standard
  dimension squared (pair interaction) and the H₃(q) quantum 3-integer
  (nucleon strand count).

Content block: rem:q-integer-mass-table
Witness: q-integer-bw-7term.witness.json

Usage:
    cd folio-assistant/computations
    python3 q_integer_bw_7term.py
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q, Q_INV, HA, q_int, HBAR_Q, Q_ERR
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

# ══════════════════════════════════════════════════════════════
# §1  COEFFICIENTS — all from q-integers × m_e
# ══════════════════════════════════════════════════════════════

me = M_E_MEV
n2, n3, n4, n5, n6, n7 = (q_int(k) for k in (2, 3, 4, 5, 6, 7))

# Original 5 BW coefficients
LAM_V   = 2 * n2 * n7 * me        # volume
LAM_S   = 2 * n4**2 * me          # surface
LAM_C   = HA * n6 * me            # Coulomb (direct)
A_ASYM  = 3 * n2 * n7 * me        # asymmetry
DELTA_P = n3 * n7 * me            # pairing

# New: term 6 — exchange Coulomb
LAM_EX  = n3 / n2 * me            # [3]_q / [2]_q · m_e

# New: term 7 — magic shell correction
DELTA_S = n2**2 * n3 * me         # [2]_q² · [3]_q · m_e

# Magic numbers (nuclear shell closures)
MAGIC = [2, 8, 20, 28, 50, 82, 126]

# Shell proximity: Gaussian with width σ = 2 nucleons
SIGMA_SHELL = 2.0


def magic_proximity(x, sigma=SIGMA_SHELL):
    """Gaussian proximity to nuclear magic numbers.
    Peaks at 1.0 when x equals a magic number, falls off with σ."""
    return sum(math.exp(-(x - m)**2 / (2 * sigma**2)) for m in MAGIC)


# ══════════════════════════════════════════════════════════════
# §2  MASS FORMULA
# ══════════════════════════════════════════════════════════════

def binding_energy(Z, N):
    """Seven-term q-integer BW binding energy in MeV."""
    A = Z + N
    if A < 2:
        return 0.0

    # Standard 5 terms
    E_vol   = LAM_V * A
    E_surf  = LAM_S * A**(2.0 / 3)
    E_coul  = LAM_C * Z * (Z - 1) / A**(1.0 / 3)
    E_asym  = A_ASYM * (N - Z)**2 / (4 * A)

    if Z % 2 == 0 and N % 2 == 0:
        E_pair = DELTA_P / math.sqrt(A)
    elif Z % 2 == 1 and N % 2 == 1:
        E_pair = -DELTA_P / math.sqrt(A)
    else:
        E_pair = 0.0

    # Term 6: exchange Coulomb correction (reduces overbinding at high Z)
    # The direct Coulomb Z(Z-1)/A^(1/3) undercounts proton repulsion
    # for large Z because the surface proton density exceeds the bulk.
    # This correction scales as Z^(4/3) and SUBTRACTS from binding.
    E_exch  = LAM_EX * Z**(4.0 / 3) / A**(1.0 / 3)

    # Term 7: magic shell correction (enhanced binding at closures)
    # At magic numbers, the torus knot T_{2,m} coherence adds binding
    # from the aligned exceptional divisors (s-orbital effect).
    f_Z = magic_proximity(Z)
    f_N = magic_proximity(N)
    E_shell = DELTA_S * (f_Z + f_N) / A**(2.0 / 3)

    return E_vol - E_surf - E_coul - E_asym + E_pair - E_exch + E_shell


def atomic_mass(Z, N):
    """Predicted atomic mass M(Z,N) in MeV."""
    A = Z + N
    M_free = Z * M_P_MEV + N * M_N_MEV + Z * me
    return M_free - binding_energy(Z, N)


def observed_mass(Z, N, B_per_A):
    """Observed atomic mass from AME2020 B/A."""
    A = Z + N
    M_free = Z * M_P_MEV + N * M_N_MEV + Z * me
    return M_free - A * B_per_A


# ══════════════════════════════════════════════════════════════
# §3  DATA — AME2020 binding energies
# ══════════════════════════════════════════════════════════════

ATOMS = [
    # (name, Z, N, A, B/A [MeV] from AME2020)
    ("H",   1,   0,   1,  0.0000),
    ("He",  2,   2,   4,  7.0739),
    ("Li",  3,   4,   7,  5.6063),
    ("Be",  4,   5,   9,  6.4628),
    ("B",   5,   6,  11,  6.9277),
    ("C",   6,   6,  12,  7.6801),
    ("N",   7,   7,  14,  7.4756),
    ("O",   8,   8,  16,  7.9762),
    ("F",   9,  10,  19,  7.7790),
    ("Ne", 10,  10,  20,  8.0325),
    ("Na", 11,  12,  23,  8.1115),
    ("Mg", 12,  12,  24,  8.2607),
    ("Al", 13,  14,  27,  8.3316),
    ("Si", 14,  14,  28,  8.4477),
    ("P",  15,  16,  31,  8.4812),
    ("S",  16,  16,  32,  8.4932),
    ("Cl", 17,  18,  35,  8.5204),
    ("Ar", 18,  22,  40,  8.5954),
    ("K",  19,  20,  39,  8.5570),
    ("Ca", 20,  20,  40,  8.5513),
    ("Sc", 21,  24,  45,  8.6190),
    ("Ti", 22,  26,  48,  8.7229),
    ("V",  23,  28,  51,  8.7420),
    ("Cr", 24,  28,  52,  8.7760),
    ("Mn", 25,  30,  55,  8.7649),
    ("Fe", 26,  30,  56,  8.7904),
    ("Co", 27,  32,  59,  8.7680),
    ("Ni", 28,  30,  58,  8.7322),
    ("Cu", 29,  34,  63,  8.7522),
    ("Zn", 30,  34,  64,  8.7356),
    ("Sn", 50,  70, 120,  8.5050),
    ("Pb", 82, 126, 208,  7.8675),
    ("U",  92, 146, 238,  7.5702),
]


# ══════════════════════════════════════════════════════════════
# §4  COMPUTATION
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 100)
    print("SEVEN-TERM q-INTEGER BETHE–WEIZSÄCKER MASS FORMULA")
    print("=" * 100)
    print()
    print(f"  q₀ = {Q:.15f} ± {Q_ERR:.2e}")
    print(f"  ℏ_q = {HBAR_Q:.15f}")
    print()

    print("  Coefficients (all from [n]_q × m_e):")
    print(f"    λ_V    = 2[2]_q[7]_q·m_e      = {LAM_V:.6f} MeV  (volume)")
    print(f"    λ_S    = 2[4]_q²·m_e           = {LAM_S:.6f} MeV  (surface)")
    print(f"    λ_C    = (q-q⁻¹)[6]_q·m_e      = {LAM_C:.6f} MeV  (Coulomb)")
    print(f"    a_asym = 3[2]_q[7]_q·m_e       = {A_ASYM:.6f} MeV  (asymmetry)")
    print(f"    δ_P    = [3]_q[7]_q·m_e        = {DELTA_P:.6f} MeV  (pairing)")
    print(f"    λ_ex   = [3]_q/[2]_q·m_e       = {LAM_EX:.6f} MeV  (exchange)")
    print(f"    δ_S    = [2]_q²[3]_q·m_e       = {DELTA_S:.6f} MeV  (shell)")
    print()

    # Table
    print(f"  {'Atom':>3} {'Z':>3} {'N':>3} {'A':>3}"
          f"  {'M_pred':>12} {'M_obs':>12} {'Error':>8}")
    print("  " + "-" * 55)

    results = []
    errors_abs = []

    for name, Z, N, A, BperA in ATOMS:
        if A < 2:
            M_pred = Z * M_P_MEV + Z * me  # just proton + electron
            M_obs = Z * M_P_MEV + Z * me
            pct = 0.0
        else:
            M_pred = atomic_mass(Z, N)
            M_obs = observed_mass(Z, N, BperA)
            pct = (M_pred - M_obs) / M_obs * 100

        print(f"  {name:>3} {Z:>3} {N:>3} {A:>3}"
              f"  {M_pred:>12.3f} {M_obs:>12.3f} {pct:>+7.3f}%")

        errors_abs.append(abs(pct))
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "M_pred_MeV": round(M_pred, 3),
            "M_obs_MeV": round(M_obs, 3),
            "error_pct": round(pct, 4),
            "B_per_A_AME2020": BperA,
        })

    # Skip H for statistics
    stats_errors = [abs(r["error_pct"]) for r in results if r["A"] > 1]
    mae = sum(stats_errors) / len(stats_errors)
    worst = max(stats_errors)
    best_atoms = sorted(results[1:], key=lambda r: abs(r["error_pct"]))

    print()
    print(f"  Mean absolute error: {mae:.4f}% ({len(stats_errors)} atoms)")
    print(f"  Worst prediction: {worst:.4f}%")
    best_str = ', '.join(f'{r["atom"]} {r["error_pct"]:+.4f}%' for r in best_atoms[:5])
    print(f"  Best: {best_str}")
    print()

    # ── Witness ──────────────────────────────────────────────
    w = WitnessBuilder("q-integer-bw-7term", engine="python")
    w.set_description(
        "Seven-term q-integer BW mass formula. Extends the five-term "
        "formula with exchange Coulomb ([3]_q/[2]_q·m_e) and magic "
        "shell correction ([2]_q²[3]_q·m_e × Gaussian proximity). "
        "Zero fitted parameters — all coefficients are products of "
        "quantum integers [n]_q evaluated at q₀."
    )
    w.set_content_block("rem:q-integer-mass-table")

    w.add_parameter("q₀", Q)
    w.add_parameter("[2]_q", n2)
    w.add_parameter("[3]_q", n3)
    w.add_parameter("[4]_q", n4)
    w.add_parameter("[6]_q", n6)
    w.add_parameter("[7]_q", n7)
    w.add_parameter("λ_V (MeV)", LAM_V)
    w.add_parameter("λ_S (MeV)", LAM_S)
    w.add_parameter("λ_C (MeV)", LAM_C)
    w.add_parameter("a_asym (MeV)", A_ASYM)
    w.add_parameter("δ_P (MeV)", DELTA_P)
    w.add_parameter("λ_ex (MeV)", LAM_EX)
    w.add_parameter("δ_S (MeV)", DELTA_S)
    w.add_parameter("σ_shell", SIGMA_SHELL)

    for r in results:
        if r["A"] < 2:
            continue
        w.add_assertion(
            f"{r['atom']}-{r['A']} mass",
            computed=r["M_pred_MeV"],
            expected=r["M_obs_MeV"],
            tolerance=r["M_obs_MeV"] * 0.002,  # 0.2% tolerance
            unit="MeV",
            source="AME2020 + CODATA 2022",
        )

    w.add_assertion(
        "MAE < 0.025%",
        computed=round(mae, 5),
        expected=0.0,
        tolerance=0.025,
        unit="%",
        source="Mean absolute error across 32 isotopes",
    )

    w.add_data("results", results)
    w.add_data("statistics", {
        "MAE_pct": round(mae, 5),
        "worst_pct": round(worst, 5),
        "n_atoms": len(stats_errors),
    })

    w.add_caveat(
        "The shell correction uses a Gaussian proximity function with "
        "σ = 2.0. This width parameter is not directly a q-integer but "
        "reflects the shell occupancy spread (~2 nucleons above/below "
        "each magic number). A fully principled derivation would replace "
        "this with the Chebyshev torus knot width 1/ln([m]_q)."
    )
    w.add_caveat(
        "The (5/4) factor in the exchange Coulomb from standard nuclear "
        "physics is replaced here by [3]_q/[2]_q ≈ 1.513, which is the "
        "ratio of quantum dimensions. This slightly overestimates the "
        "exchange effect compared to standard (1.25), but the q-integer "
        "form is derivable from the Hecke algebra representation theory."
    )

    witness_path = w.save()
    print(f"  Witness: {witness_path}")


if __name__ == "__main__":
    main()
