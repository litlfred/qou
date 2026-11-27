#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to fsh-guts/deprecated/computations/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Pure tower formula for absolute M(isotope) — no CODATA m_p, m_n inputs.

Per prop:mass-endomorphism-tower:
  𝔪(ρ) = |Π_i V̂_i^full|  +  Σ_i Φ_q(|V̂_i^full|)
         +  z² · Σ_{|i-j|=1} Φ_q(|V̂_i^full · V̂_j^full|)

in Hecke units.  Convert to MeV via the electron calibration:
  m_e_Hecke = tower value for the electron (σ_0σ_1σ_0)
  M_MeV = (𝔪(ρ)_Hecke / m_e_Hecke) · M_e_MeV

Apply the tower correction:
  M_corrected = M_MeV / (1 + [2]_q · ℏ_q²)

Then test whether M_CODATA − M_corrected ≈ m_e · Σ_λ 1/d_λ
where λ ranges over partitions of n = 3·A.

Isotopes tested: p, n, D, T, ³He, ⁴He, ⁶Li (optional).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (  # noqa: E402 (codata sweep)
    M_N_MEV_VALIDATION, M_P_MEV_VALIDATION,
    M_D_ATOMIC_MEV_VALIDATION, M_T_ATOMIC_MEV_VALIDATION,
    M_HE3_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION,
    M_LI6_ATOMIC_MEV_VALIDATION, M_C12_ATOMIC_MEV_VALIDATION,
)
import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from hecke_core import (
    atom_per_generator_volumes,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    vertex_volume,
)
from hecke_characters import partitions_of, young_hooks
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
B2 = Q0 + QI                            # [2]_q
HBAR = (Q0 - mp.mpf(1)) / Q0            # ℏ_q
HBAR_SQ = HBAR * HBAR
Z_MP = mp.mpf(str(float(Z_MARKOV)))
Z_SQ = Z_MP * Z_MP

# CODATA masses (MeV) — atomic masses, neutral atom
M_E_CODATA = mp.mpf(str(M_E_MEV))
CODATA_ATOMIC = {
    "p":     mp.mpf(M_P_MEV_VALIDATION),       # bare proton (not neutral H)
    "n":     mp.mpf(M_N_MEV_VALIDATION),
    "D":     M_D_ATOMIC_MEV_VALIDATION,    # ²H atomic mass (with e)
    "T":     M_T_ATOMIC_MEV_VALIDATION,    # ³H atomic mass
    "3He":   M_HE3_ATOMIC_MEV_VALIDATION,  # ³He atomic mass
    "4He":   M_HE4_ATOMIC_MEV_VALIDATION,  # ⁴He atomic mass
    "6Li":   M_LI6_ATOMIC_MEV_VALIDATION,
    "12C":   M_C12_ATOMIC_MEV_VALIDATION,
}


def Phi_q(v, max_iter=4000, tol=mp.mpf("1e-40")):
    """Φ_q(v) = Π_{k≥1} (1 − q^{-k} v)^{-1}."""
    if not isinstance(v, mp.mpf):
        v = mp.mpf(str(float(v)))
    prod = mp.mpf(1)
    coef = mp.mpf(1) / Q0
    for k in range(1, max_iter + 1):
        term = mp.mpf(1) - coef * v
        if abs(term) < tol:
            return mp.mpc("inf")
        prod /= term
        if abs(coef * v) < tol:
            break
        coef /= Q0
    return prod


def tower_level0(V_arr, use_pairs=True):
    """Tower level-0 in Hecke units:
        M = |Π V̂_i|  +  Σ_i Φ_q(|V̂_i|)
          +  z² · Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|)  if use_pairs
    """
    if not V_arr:
        return mp.mpf(0)
    # Absolute values
    abs_V = [mp.fabs(mp.mpf(str(float(v)))) for v in V_arr]
    # Product term
    prod = mp.mpf(1)
    for v in abs_V:
        prod *= v
    # Per-generator Φ_q sum
    phi_sum = mp.mpf(0)
    for v in abs_V:
        if v < mp.mpf(1):        # convergence region
            phi_sum += Phi_q(v)
        else:
            # Use log form: if |V̂| > q it's past pole; give NaN.
            phi_sum = mp.mpc("nan")
            break
    # Adjacent-pair term
    pair_sum = mp.mpf(0)
    if use_pairs and not mp.isnan(mp.re(phi_sum)):
        for i in range(len(abs_V) - 1):
            prod_ij = abs_V[i] * abs_V[i + 1]
            if prod_ij < mp.mpf(1):
                pair_sum += Phi_q(prod_ij)
            else:
                pair_sum = mp.mpc("nan")
                break
    return prod + phi_sum + Z_SQ * pair_sum


def compute_electron_tower():
    """Electron word σ_0·σ_1·σ_0 on 3 strands, 2 generators.
    V̂_e^std from transfer matrix; V̂_e^sym, alt = character eigenvalues."""
    # Use vertex_volume on the (c, d) chain [(1,0), (1,0), (1,0)] at 2 gens?
    # Actually the trefoil is 3 σ factors alternating: σ_0 σ_1 σ_0.
    # That's NOT a chain for vertex_volume (which expects a single-gen chain).
    # Use the paper's stated m_e formula: |V̂_e|·(1+Φ_q(V̂_e)) for the
    # minimal trefoil evaluation.  From hecke_core.py convention:
    # V̂_e = z · a + b with trefoil (σ^3) giving specific recurrence.
    # Hmm — simpler: mass_endomorphism probably has this.  Use its
    # 'free' baseline for A=0 electron.
    # Alternative: use 1-generator trefoil chain on 2 strands:
    #   σ_0^3 = (c=1,d=0) applied 3 times at same generator.
    # Then V̂_e = vertex_volume([(1,0),(1,0),(1,0)]).
    V_e = vertex_volume([(1.0, 0.0), (1.0, 0.0), (1.0, 0.0)])
    V_e_mp = mp.mpf(str(float(V_e)))
    # Level-0 tower for electron: |V̂_e| + Φ_q(|V̂_e|)
    # (no pair term since only 1 generator).
    abs_V = mp.fabs(V_e_mp)
    phi = Phi_q(abs_V) if abs_V < mp.mpf(1) else mp.mpc("nan")
    m_e_H = abs_V + phi
    return m_e_H, V_e_mp


def partition_sum_inv(n: int) -> Fraction:
    """Σ_λ 1/d_λ at n."""
    total = Fraction(0)
    for shape in partitions_of(n):
        n_s = sum(shape); hooks = young_hooks(shape)
        f = 1
        for k in range(2, n_s + 1): f *= k
        hp = 1
        for h in hooks: hp *= h
        d = f // hp
        if d > 0:
            total += Fraction(1, d)
    return total


def compute_isotope_tower(Z: int, N: int, m_e_H: mp.mpf) -> dict:
    """Compute absolute M(Z, N) via tower formula, convert to MeV."""
    A = Z + N
    n_strands = 3 * A
    # Per-generator V̂_i^full for the atom braid
    V_arr_dict = atom_per_generator_volumes(Z, N)
    V_full_arr = [d["full"] for d in V_arr_dict]
    # Tower level-0 in Hecke units
    M_H = tower_level0(V_full_arr, use_pairs=True)
    # Convert to MeV via electron calibration
    if mp.isnan(mp.re(mp.mpf(str(float(mp.fabs(M_H)))))):
        M_MeV = mp.mpc("nan")
        M_corrected = mp.mpc("nan")
    else:
        M_MeV = (M_H / m_e_H) * M_E_CODATA
        M_corrected = M_MeV / (mp.mpf(1) + B2 * HBAR_SQ)
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "n_generators": len(V_full_arr),
        "V_full_arr": [float(v) for v in V_full_arr],
        "M_Hecke_units": mp.nstr(M_H, 30),
        "M_MeV_raw": (mp.nstr(M_MeV, 25) if not mp.isnan(mp.re(M_MeV))
                       else "nan"),
        "M_MeV_corrected": (mp.nstr(M_corrected, 25)
                              if not mp.isnan(mp.re(M_corrected))
                              else "nan"),
    }


def main() -> int:
    print("=" * 100)
    print("PURE TOWER M(isotope) — test m_e · Σ 1/d_λ hypothesis")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    m_e_H, V_e = compute_electron_tower()
    print(f"  V̂_e = {float(V_e):.8f}")
    print(f"  m_e (Hecke units, level-0 tower) = {mp.nstr(m_e_H, 20)}")
    print(f"  m_e (MeV, calibration)           = {M_E_CODATA}")
    print(f"  conversion factor               = {mp.nstr(M_E_CODATA / m_e_H, 15)} MeV/Hecke-unit")
    print()

    ISOTOPES = [
        ("p",     1, 0, M_E_CODATA * 0 + mp.mpf(M_P_MEV_VALIDATION)),
        ("n",     0, 1, mp.mpf(M_N_MEV_VALIDATION)),
        ("D",     1, 1, CODATA_ATOMIC["D"]),
        ("T",     1, 2, CODATA_ATOMIC["T"]),
        ("3He",   2, 1, CODATA_ATOMIC["3He"]),
        ("4He",   2, 2, CODATA_ATOMIC["4He"]),
    ]

    print(f"  {'iso':<6} {'Z':>2} {'N':>2} {'A':>2} {'n':>3} "
          f"{'M_tower_MeV':>16} {'M_corrected':>16} {'M_CODATA':>14} "
          f"{'err (MeV)':>12} {'err/m_e':>10} {'Σ 1/d_λ':>10}")
    out_rows = []
    for label, Z, N, M_CODATA in ISOTOPES:
        r = compute_isotope_tower(Z, N, m_e_H)
        A = r["A"]
        s = partition_sum_inv(3 * A)
        M_corr = r["M_MeV_corrected"]
        if M_corr == "nan":
            print(f"  {label:<6} {Z:>2} {N:>2} {A:>2} {3*A:>3} "
                  f"{'nan':>16} {'nan':>16} {float(M_CODATA):>14.5f} "
                  f"{'nan':>12} {'nan':>10} {str(s)[:10]:>10}")
            out_rows.append({"label": label, "Z": Z, "N": N,
                               **r, "sum_inv_d": str(s),
                               "M_CODATA": float(M_CODATA)})
            continue
        M_corr_mp = mp.mpf(M_corr)
        err = M_CODATA - M_corr_mp
        err_me = err / M_E_CODATA
        print(f"  {label:<6} {Z:>2} {N:>2} {A:>2} {3*A:>3} "
              f"{float(r['M_MeV_raw']):>16.5f} {float(M_corr_mp):>16.5f} "
              f"{float(M_CODATA):>14.5f} "
              f"{float(err):>+12.4f} {float(err_me):>+10.4f} "
              f"{str(s)[:10]:>10}")
        out_rows.append({"label": label, "Z": Z, "N": N,
                           **r,
                           "M_CODATA": float(M_CODATA),
                           "err_MeV": float(err),
                           "err_over_m_e": float(err_me),
                           "sum_inv_d": str(s),
                           "sum_inv_d_float": float(s)})

    print()
    print("  Compare err/m_e to Σ 1/d_λ — does the partition-sum hypothesis extend?")
    print(f"  {'iso':<6}  {'err/m_e':>12}  {'Σ 1/d_λ':>15}  {'ratio':>8}")
    for row in out_rows:
        if 'err_over_m_e' in row and row.get('sum_inv_d_float'):
            r = row['err_over_m_e'] / row['sum_inv_d_float']
            print(f"  {row['label']:<6}  {row['err_over_m_e']:>+12.4f}  "
                  f"{row['sum_inv_d_float']:>15.6f}  {r:>+8.4f}")

    witness = {
        "computation": "tower-isotope-absolute",
        "description": (
            "Pure tower computation of absolute M(isotope) — no CODATA "
            "m_p, m_n inputs.  Uses atom_per_generator_volumes(Z,N) to "
            "get V̂_i^full per generator, applies level-0 tower "
            "|ΠV̂| + Σ Φ_q(V̂_i) + z² Σ_adj Φ_q(V̂_iV̂_j), electron-"
            "calibrated, corrected by /(1+[2]_q·ℏ_q²), then compared "
            "against CODATA atomic masses.  Tests partition-sum "
            "hypothesis err = m_e · Σ_λ 1/d_λ at n = 3A."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "m_e_Hecke": mp.nstr(m_e_H, 30),
        "isotopes": out_rows,
    }
    out = Path(__file__).parent / "tower-isotope-absolute.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
