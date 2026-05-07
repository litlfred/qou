#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Test the paper's UNIFIED mass formula (knot-mass-formula-unified.md)
on light isotopes D, T, ³He, ⁴He with all three Frobenius
interpretations:

  (A) per-vortex: A · m_e · (2 + 1/[2]_q)      = A · 1.276 MeV
  (B) per-atom:   m_e · Σ_{λ⊢3A} 1/dim_q(λ)    = n-specific
  (C) universal:  m_e · (2 + 1/[2]_q)          = 1.276 MeV constant

Full formula (from knot-mass-formula-unified.md):
  𝔪(ρ) = |tr_M(T_w)| + Σ Φ_q(V̂_i) + z² Σ Φ_q(V̂_i V̂_j) + m_e · Σ 1/dim_q(λ)

Goal: see which Frobenius interpretation reproduces CODATA binding B.

Uses pure categorical-action pieces — no BW template.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50
import sympy as sp

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV
from hecke_characters import partitions_of, young_hooks
from hecke_core import (atom_per_generator_volumes, _ensure_ysn_attached,
                           _partition_table, atom_character_raw,
                           z as Z_MARKOV)
from mass_endomorphism import w_sym, w_std, w_alt

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
Z_MP = mp.mpf(str(float(Z_MARKOV)))
Z_SQ = Z_MP * Z_MP

_ensure_ysn_attached()
_PT = _partition_table()


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= q_int(k)
    return out


def dim_q_mp(shape):
    n = sum(shape); hooks = young_hooks(shape)
    num = q_fact(n)
    den = mp.mpf(1)
    for h in hooks:
        den *= q_int(h)
    return num / den


def sum_inv_dim_q(n):
    total = mp.mpf(0)
    for shape in partitions_of(n):
        d = dim_q_mp(shape)
        if d > 0:
            total += 1 / d
    return total


# Precompute universal n=3 Frobenius
FROB_N3_MeV = float((2 + 1 / (Q0 + QI)) * me)   # 1.276 MeV


def Phi_q(v, max_iter=3000):
    if not isinstance(v, mp.mpf):
        v = mp.mpf(str(float(v)))
    prod = mp.mpf(1)
    coef = mp.mpf(1) / Q0
    for k in range(1, max_iter + 1):
        term = mp.mpf(1) - coef * v
        if abs(term) < mp.mpf("1e-40"):
            return mp.mpc("inf")
        prod /= term
        if abs(coef * v) < mp.mpf("1e-60"):
            break
        coef /= Q0
    return prod


def brane_tower(V_arr):
    """|Π V̂_i| + Σ Φ_q(|V̂_i|) + z² Σ_{i<j adj} Φ_q(|V̂_i V̂_j|)"""
    if not V_arr:
        return mp.mpf(0)
    abs_V = [mp.fabs(mp.mpf(str(float(v)))) for v in V_arr]
    prod = mp.mpf(1)
    for v in abs_V:
        prod *= v
    phi_sum = mp.mpf(0)
    for v in abs_V:
        if v < mp.mpf(1):
            phi_sum += Phi_q(v)
        else:
            return mp.mpc("nan")
    pair_sum = mp.mpf(0)
    for i in range(len(abs_V) - 1):
        prod_ij = abs_V[i] * abs_V[i + 1]
        if prod_ij < mp.mpf(1):
            pair_sum += Phi_q(prod_ij)
        else:
            return mp.mpc("nan")
    return prod + phi_sum + Z_SQ * pair_sum


def descended_markov_trace(Z, N, include_inter=True):
    """|tr_M(T_w)| via Plancherel-weighted sum with quantum dim norm."""
    n = 3 * (Z + N)
    if n < 2: return mp.mpf(0)
    if n > 11:    # partition table limit
        return None
    entries = [e for e in _PT if e['k'] == n]
    nfac = q_fact(n)
    total = mp.mpc(0)
    for entry in entries:
        shape = entry['partition']
        dq = dim_q_mp(shape)
        if dq == 0: continue
        w = dq * dq / nfac
        try:
            chi_q, ln, _ = atom_character_raw(Z, N, entry, include_inter=include_inter)
        except Exception:
            continue
        chi_actual = mp.mpc(str(float(chi_q))) * mp.exp(mp.mpf(str(float(ln))))
        total += w * chi_actual / dq
    return mp.fabs(total)


def unified_predict_M(Z, N, frob_kind='per_vortex'):
    """Full unified formula for atomic mass M(Z,N)."""
    A = Z + N
    n = 3 * A

    # 1. Descended
    tr_abs = descended_markov_trace(Z, N, include_inter=True)
    if tr_abs is None or mp.isnan(mp.re(tr_abs)):
        return None, None, None, None

    # 2. Brane tower
    V_full = [d["full"] for d in atom_per_generator_volumes(Z, N)]
    bt = brane_tower(V_full)
    if mp.isnan(mp.re(mp.mpf(str(float(bt.real)))) if hasattr(bt, 'real') else mp.mpf(str(float(bt)))):
        bt = mp.mpf(0)

    # 3. Frobenius
    if frob_kind == 'per_vortex':
        frob = A * FROB_N3_MeV
    elif frob_kind == 'universal':
        frob = FROB_N3_MeV
    elif frob_kind == 'per_atom':
        if 3 * A <= 11:
            s = sum_inv_dim_q(3 * A)
            frob = float(s * me)
        else:
            return None, float(tr_abs), float(mp.re(mp.mpf(str(float(bt))))), None
    else:
        frob = 0.0

    m_predicted = float(tr_abs) + float(mp.re(mp.mpf(str(float(bt))))) + frob
    return m_predicted, float(tr_abs), float(mp.re(mp.mpf(str(float(bt))))), frob


def main() -> int:
    print("=" * 100)
    print("UNIFIED FORMULA TEST: knot-mass-formula-unified.md")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}, m_e = {M_E_MEV}")
    print(f"  n=3 Frobenius (2 + 1/[2]_q) · m_e = {FROB_N3_MeV:.6f} MeV")
    print()
    # Expected categorical mass = m_e · Σ tr_M but also calibrated
    # via E_0 = 938/|tr_M(proton)| or similar.  Here we directly test
    # the unified formula's output against CODATA.

    # For our purposes, the unified formula output is a PROXY of mass;
    # the calibration E_0 (MeV per cat.unit) converts to MeV.  Set it
    # such that proton mass is exact: E_0 = 938.272 / 𝔪_p(unified).

    # First compute 𝔪(proton) under each Frobenius kind:
    print(f"  {'iso':<6} {'frob_kind':<14} {'|tr_M|':>10} {'brane':>12} {'Frob':>8} "
          f"{'total':>14} {'CODATA_M':>12} {'err%':>8}")
    CODATA_ATOMIC = {
        "p":    (1, 0, 938.272),
        "n":    (0, 1, 939.565),
        "D":    (1, 1, 1876.124),
        "T":    (1, 2, 2809.432),
        "3He":  (2, 1, 2809.414),
    }
    # Calibrate E_0 per-vortex from proton
    m_p_predict_pv = unified_predict_M(1, 0, 'per_vortex')
    if m_p_predict_pv[0] is None or m_p_predict_pv[0] == 0:
        print("  !! proton unified output unusable")
        return 1
    E_0 = 938.272 / m_p_predict_pv[0]
    print(f"  (calibration: E_0 = 938.272 / 𝔪_p[per_vortex] = {E_0:.6f} MeV/cat.unit)")
    print()

    rows = []
    for iso, (Z, N, M_cod) in CODATA_ATOMIC.items():
        for kind in ['per_vortex', 'per_atom', 'universal']:
            M_pred, tr_v, bt_v, fr_v = unified_predict_M(Z, N, kind)
            if M_pred is None:
                print(f"  {iso:<6} {kind:<14} {'—':>10} {'—':>12} {'—':>8} "
                      f"{'nan':>14} {M_cod:>12} {'nan':>8}")
                continue
            M_MeV = M_pred * E_0
            err = (M_MeV - M_cod) / M_cod * 100
            print(f"  {iso:<6} {kind:<14} {tr_v:>10.4f} {bt_v:>12.4f} "
                  f"{fr_v:>8.4f} {M_pred:>14.4f} {M_cod:>12.3f} "
                  f"{err:>+7.3f}%")
            rows.append({
                "iso": iso, "Z": Z, "N": N, "kind": kind,
                "tr_M_abs": tr_v, "brane": bt_v, "frobenius": fr_v,
                "M_unified_cat": M_pred, "M_MeV": M_MeV,
                "M_CODATA": M_cod, "err_pct": err,
            })

    # Binding implied
    print()
    print("  Implied bindings B = Z·m_p + N·m_n + Z·m_e − M(Z,N):")
    print(f"  {'iso':<6} {'kind':<14} {'M_pred':>10} {'M_CODATA':>10} {'B_pred':>10} {'B_AME':>10} {'err%':>7}")
    AME_B = {"D": 2.224, "T": 8.482, "3He": 7.718}
    for iso in ["D", "T", "3He"]:
        Z, N, _ = CODATA_ATOMIC[iso]
        A = Z + N
        for kind in ['per_vortex', 'per_atom', 'universal']:
            row = [r for r in rows if r['iso']==iso and r['kind']==kind]
            if not row:
                continue
            M_MeV = row[0]['M_MeV']
            B_implied = Z * 938.272 + N * 939.565 + Z * 0.511 - M_MeV
            B_ame = AME_B.get(iso, 0)
            err_b = (B_implied - B_ame) / B_ame * 100 if B_ame > 0 else 0
            print(f"  {iso:<6} {kind:<14} {M_MeV:>10.4f} {row[0]['M_CODATA']:>10.3f} "
                  f"{B_implied:>10.4f} {B_ame:>10.3f} {err_b:>+7.2f}%")

    witness = {
        "computation": "unified-formula-test",
        "description": (
            "Test of paper's unified mass formula on light isotopes "
            "with three Frobenius interpretations."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "E_0_calibration_MeV_per_cat_unit": E_0,
        "rows": rows,
    }
    out = Path(__file__).parent / "unified-formula-test.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
