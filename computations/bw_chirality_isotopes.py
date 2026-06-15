#!/usr/bin/env python3
"""
Implement the paper's BW formula with chirality factors derived in
six-term-mass-formula-complete.md and q-integer-mass-formula.md.

Formula (q-integer-mass-formula.md lines 26-35):
  M(Z,N) = Z·m_p + N·m_n + Z·m_e
          − λ_V·A + λ_S·A^(2/3) + λ_C·Z(Z-1)/A^(1/3)
          + a_asym·(N-Z)²/(4A) ∓ δ_P/√A
          + λ_ex·Z^(4/3)/A^(1/3) − δ_S·(f(Z)+f(N))/A^(2/3)

Coefficients (all in MeV, derived from q_0 alone):
  λ_V     = 2·[2]_q·[7]_q · m_e
  λ_S     = 2·[4]_q² · m_e
  λ_C     = (q-q⁻¹)·[6]_q · m_e
  a_asym  = 3·[2]_q·[7]_q · m_e
  δ_P     = [3]_q·[7]_q · m_e
  λ_ex    = [3]_q/[2]_q · m_e
  δ_S     = [2]_q²·[3]_q · m_e

Then apply chirality factor per six-term-mass-formula-complete.md:
  B_K(Z,N) = (chirality factor) · B_bulk(Z,N) + h·[2]_q·B_Z(Z,N)

where chirality factor is:
  D (A=2, satellite, chiral+):    (1 + h)
  T, ³He (A=3, fig-8, amphi):     (1 − h²)
  ⁴He (A=4, Borromean, 2 amphi):  (1 − h²)²
  ≥5: limit toward 1

B_bulk = volume - surface - asymmetry ± pairing (Z-independent)
B_Z = Coulomb + exchange (Z-dependent)

B(Z,N) = M(Z,N)_{no-BW} − M(Z,N) = [sum of BW corrections]

Verify against mass_table_best and paper's quoted errors:
  T: 0.5%, ³He: 0.9%
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
m_e = mp.mpf(str(M_E_MEV))
m_p = mp.mpf(str(M_P_MEV))
m_n = mp.mpf(str(M_N_MEV))


def q_int(n):
    if n == 0: return mp.mpf(0)
    return (Q0**n - QI**n) / (Q0 - QI)

# Q-integers at q_0
B2 = q_int(2); B3 = q_int(3); B4 = q_int(4); B5 = q_int(5); B6 = q_int(6); B7 = q_int(7)
h = Q0 - QI                 # H_A = q − q⁻¹ (Hecke deformation)

# BW coefficients (paper derives)
lambda_V  = 2 * B2 * B7 * m_e
lambda_S  = 2 * B4 * B4 * m_e
lambda_C  = h * B6 * m_e
a_asym    = 3 * B2 * B7 * m_e
delta_P   = B3 * B7 * m_e
lambda_ex = (B3 / B2) * m_e
delta_S   = B2 * B2 * B3 * m_e

# Chirality factors (paper)
f_chiral_plus  = 1 + h       # +h for chiral+ knot
f_chiral_minus = 1 - h       # -h for chiral-
f_amphi        = 1 - h*h     # (1-h²) for amphicheiral
f_borromean    = (1 - h*h)**2
f_Zdep_scale   = h * B2      # h[2]_q factor for Z-dep part


def magic_proximity(x):
    """f(x) = Σ_m exp(-(x-m)²/(2·[2]_q²)) over magic numbers."""
    magics = [2, 8, 20, 28, 50, 82, 126]
    sigma = B2
    s = mp.mpf(0)
    for m in magics:
        s += mp.exp(-mp.mpf(x - m)**2 / (2 * sigma * sigma))
    return s


def B_bulk(A: int, Z: int, N: int, pairing_sign: int) -> mp.mpf:
    """Z-independent bulk binding:
        B_bulk = λ_V·A - λ_S·A^(2/3) - a_asym·(N-Z)²/(4A) ± δ_P/√A
    """
    A_mp = mp.mpf(A)
    term_V  = lambda_V * A_mp
    term_S  = lambda_S * mp.power(A_mp, mp.mpf('2/3'))
    term_asym = a_asym * (N - Z)**2 / (4 * A_mp)
    term_P = pairing_sign * delta_P / mp.sqrt(A_mp)
    return term_V - term_S - term_asym + term_P


def B_Zdep(A: int, Z: int, N: int) -> mp.mpf:
    """Z-dependent Coulomb + exchange:
        B_Z = -λ_C · Z(Z-1)/A^(1/3) - λ_ex · Z^(4/3)/A^(1/3)
    (negative: reduces binding)"""
    A_mp = mp.mpf(A)
    cA13 = mp.power(A_mp, mp.mpf('1/3'))
    return -lambda_C * mp.mpf(Z * (Z - 1)) / cA13 - lambda_ex * mp.power(mp.mpf(Z), mp.mpf('4/3')) / cA13


def B_shell(A: int, Z: int, N: int) -> mp.mpf:
    """Shell correction -δ_S·(f(Z)+f(N))/A^(2/3)."""
    A_mp = mp.mpf(A)
    f_tot = magic_proximity(Z) + magic_proximity(N)
    return -delta_S * f_tot / mp.power(A_mp, mp.mpf('2/3'))


def pairing_sign(Z: int, N: int) -> int:
    """δ_P sign: + for even-even, - for odd-odd, 0 otherwise."""
    ze = Z % 2 == 0; ne = N % 2 == 0
    if ze and ne: return +1
    if (not ze) and (not ne): return -1
    return 0


def predict_binding(A: int, Z: int, N: int,
                      chirality_factor: mp.mpf,
                      zdep_factor: mp.mpf = None,
                      include_shell: bool = False) -> dict:
    """Paper-formula prediction of B(Z,N).

    six-term-mass-formula-complete.md formula (light isotopes, NO shell):
        B_K = (chirality_factor) · B_bulk + (h·[2]_q) · B_Z
    where B_bulk = volume − surface − asymmetry ± pairing
    and   B_Z   = -Coulomb − exchange

    include_shell=True adds the δ_S·(f(Z)+f(N))/A^(2/3) shell term
    for heavier isotopes near magic closures (per q-integer-mass-formula.md).
    """
    if zdep_factor is None:
        zdep_factor = f_Zdep_scale
    sign = pairing_sign(Z, N)
    B_b = B_bulk(A, Z, N, sign)
    B_Z = B_Zdep(A, Z, N)
    B_sh = B_shell(A, Z, N) if include_shell else mp.mpf(0)
    # Chirality only multiplies the bulk; Z-dep has its own factor; shell
    # (if included) is added uncorrected (per q-integer-mass-formula.md).
    # NOTE: B_shell returns NEGATIVE contribution in my sign convention,
    # but the paper's full BW has +δ_S·(magic)/A^(2/3) for binding.  Sign
    # flip here:
    B_sh_corrected = -B_sh  # flip to positive-binding contribution
    B_total = chirality_factor * B_b + zdep_factor * B_Z + B_sh_corrected
    return {
        "B_bulk": float(B_b),
        "B_Zdep": float(B_Z),
        "B_shell": float(B_sh_corrected) if include_shell else 0.0,
        "B_with_chirality": float(B_total),
        "chirality_factor": float(chirality_factor),
    }


def predict_binding_vanilla(A: int, Z: int, N: int) -> float:
    """Classic BW formula with paper's coefficients, NO chirality factor."""
    sign = pairing_sign(Z, N)
    A_mp = mp.mpf(A)
    B = (lambda_V * A_mp
         - lambda_S * mp.power(A_mp, mp.mpf('2/3'))
         + lambda_C * mp.mpf(Z*(Z-1)) / mp.power(A_mp, mp.mpf('1/3')) * (-1)
         - a_asym * (N-Z)**2 / (4*A_mp)
         + sign * delta_P / mp.sqrt(A_mp)
         - lambda_ex * mp.power(mp.mpf(Z), mp.mpf('4/3')) / mp.power(A_mp, mp.mpf('1/3'))
         - delta_S * (magic_proximity(Z) + magic_proximity(N)) / mp.power(A_mp, mp.mpf('2/3')))
    return float(B)


def main() -> int:
    print("=" * 100)
    print("Paper's BW + chirality formula for light isotopes")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  [2]_q={float(B2):.6f}  [3]_q={float(B3):.6f}  "
          f"[4]_q={float(B4):.6f}  [6]_q={float(B6):.6f}  [7]_q={float(B7):.6f}")
    print(f"  h = q - q⁻¹ = {float(h):.6f}")
    print()
    print("  BW coefficients (MeV):")
    print(f"    λ_V     = 2·[2]_q·[7]_q · m_e = {float(lambda_V):.6f}")
    print(f"    λ_S     = 2·[4]_q² · m_e      = {float(lambda_S):.6f}")
    print(f"    λ_C     = h·[6]_q · m_e       = {float(lambda_C):.6f}")
    print(f"    a_asym  = 3·[2]_q·[7]_q · m_e = {float(a_asym):.6f}")
    print(f"    δ_P     = [3]_q·[7]_q · m_e   = {float(delta_P):.6f}")
    print(f"    λ_ex    = [3]_q/[2]_q · m_e   = {float(lambda_ex):.6f}")
    print(f"    δ_S     = [2]_q²·[3]_q · m_e  = {float(delta_S):.6f}")
    print()
    print(f"  Chirality factors:")
    print(f"    D (chiral+)   : 1+h   = {float(f_chiral_plus):.6f}")
    print(f"    T/³He (amphi) : 1-h²  = {float(f_amphi):.6f}")
    print(f"    ⁴He (Borro 2) : (1-h²)² = {float(f_borromean):.6f}")
    print()

    # Observed binding energies (AME2020)
    CODATA = {
        "D":    (1, 1, 2, 2.22456612),
        "T":    (1, 2, 3, 8.481798),
        "3He":  (2, 1, 3, 7.718058),
        "4He":  (2, 2, 4, 28.29566),
        "6Li":  (3, 3, 6, 31.99405),
        "7Li":  (3, 4, 7, 39.24452),
        "9Be":  (4, 5, 9, 58.16505),
        "11B":  (5, 6, 11, 76.20546),
        "12C":  (6, 6, 12, 92.16175),
        "16O":  (8, 8, 16, 127.61931),
    }

    chirality_map = {
        "D":    f_chiral_plus,
        "T":    f_amphi,
        "3He":  f_amphi,
        "4He":  f_borromean,
        "6Li":  mp.mpf(1),       # A≥5 → limit factor = 1
        "7Li":  mp.mpf(1),
        "9Be":  mp.mpf(1),
        "11B":  mp.mpf(1),
        "12C":  mp.mpf(1),
        "16O":  mp.mpf(1),
    }
    include_shell_map = {
        "D": False, "T": False, "3He": False,
        "4He": True,           # Z=N=2 is magic → shell matters
        "6Li": True, "7Li": True, "9Be": True, "11B": True,
        "12C": True, "16O": True,
    }

    print(f"  {'iso':<5} {'Z':>2} {'N':>2} {'A':>3} {'B_bulk':>9} "
          f"{'B_Zdep':>9} {'B_shell':>10} {'chir':>8} "
          f"{'B_pred':>10} {'B_AME':>10} {'err%':>7}")
    rows = []
    for iso, (Z, N, A, B_ame) in CODATA.items():
        f_chir = chirality_map[iso]
        r = predict_binding(A, Z, N, f_chir,
                             include_shell=include_shell_map[iso])
        B_pred = r["B_with_chirality"]
        err = (B_pred - B_ame) / B_ame * 100
        print(f"  {iso:<5} {Z:>2} {N:>2} {A:>3} {r['B_bulk']:>9.4f} "
              f"{r['B_Zdep']:>9.4f} {r['B_shell']:>10.4f} "
              f"{float(f_chir):>8.4f} {B_pred:>10.4f} {B_ame:>10.4f} "
              f"{err:>+6.3f}%")
        rows.append({
            "isotope": iso, "Z": Z, "N": N, "A": A,
            "B_bulk": r["B_bulk"], "B_Zdep": r["B_Zdep"],
            "B_shell": r["B_shell"],
            "chirality_factor": float(f_chir),
            "B_pred_MeV": B_pred, "B_AME_MeV": B_ame,
            "err_pct": err,
        })

    # Paper's quoted errors for reference
    print()
    print("  Paper's quoted errors from terminal-resolution-proof.md:")
    print(f"    T:   claimed ~0.5%    (paper's formula)")
    print(f"    ³He: claimed ~0.9%")
    print()

    witness = {
        "computation": "bw-chirality-isotopes",
        "description": (
            "Paper's full BW formula with chirality factors (derived in "
            "six-term-mass-formula-complete.md) applied to light isotopes. "
            "Coefficients from q-integer-mass-formula.md.  Verifies "
            "quoted errors for T (~0.5%), ³He (~0.9%), and extends to "
            "A≥5 where chirality limit → 1."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "coefficients_MeV": {
            "lambda_V": float(lambda_V),
            "lambda_S": float(lambda_S),
            "lambda_C": float(lambda_C),
            "a_asym":   float(a_asym),
            "delta_P":  float(delta_P),
            "lambda_ex": float(lambda_ex),
            "delta_S":  float(delta_S),
        },
        "chirality_factors": {
            "D_chiral_plus":   float(f_chiral_plus),
            "T_3He_amphi":     float(f_amphi),
            "4He_Borromean":   float(f_borromean),
        },
        "rows": rows,
    }
    out = Path(__file__).parent / "bw-chirality-isotopes.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
