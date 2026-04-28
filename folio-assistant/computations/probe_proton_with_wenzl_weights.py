#!/usr/bin/env python3
"""Probe — recompute proton mass-endomorphism using Wenzl y_λ weights.

Per the Wedderburn weight-scheme audit (probe_wedderburn_weight_scheme.py):
mass_endomorphism uses Plancherel-A (dim_q²/[n]_q!), but the canonical
Markov trace per Wenzl bridge uses different weights. Plancherel-A
doesn't sum to 1 at q_0 (off by 1.3%) — strong hint of mis-normalization.

This probe substitutes the Wenzl y_λ values from the canonical witness
into the mass-endomorphism V̂_full computation and re-runs the proton
+ neutron + electron masses. Compare to the Plancherel-A result
(1869.85·m_e for proton, +1.84% off CODATA).

The Plancherel-Wenzl difference in the V̂_full formula:

  V̂_full = w_sym · sp + w_std · Vs + w_alt · ap

Plancherel-A: w_sym = qdim((3,))²/[3]_q! = 1/6.121 = 0.1634
              w_std = qdim((2,1))²/[3]_q! = (2.011)²/6.121 = 0.661
              w_alt = qdim((1,1,1))²/[3]_q! = 1/6.121 = 0.1634
              (sums to 0.987, not 1)
Wenzl-B:      w_sym = y_(3)        = 0.4154
              w_std = y_(2,1)      = 0.2809
              w_alt = y_(1,1,1)    = 0.0228
              (sums to 0.719 BUT sums to 1 with classical dims)

The mass_endomorphism formula uses w_λ in V̂_full as:
  V̂_full = w_sym · sp + w_std · Vs + w_alt · ap

If V̂_full is meant to be the per-generator Markov trace at λ, this is:
  (Plancherel-A) Vf_A = Σ (dim_q²/[n]_q!) · per-irrep-weight
  (Wenzl-B)      Vf_B = Σ y_λ · per-irrep-weight

NO Vol_hyp.  NO census.  Pure mpmath at 50 dps.

Output: probe-proton-with-wenzl-weights.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

mp.mp.dps = 50

VOL_FIGURE_EIGHT = mp.mpf("2.029883212819307")
MASS_RATIO_MU_E  = mp.mpf("206.7682830")
HBAR_Q_SQ        = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q           = mp.sqrt(HBAR_Q_SQ)
Q0               = mp.mpf(1) / (mp.mpf(1) - HBAR_Q)
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0
Z_MARK           = mp.mpf(1) / (mp.sqrt(Q0) + mp.sqrt(QI0))


def qint(k):
    if k == 0:
        return mp.mpf(0)
    return (Q0**k - QI0**k) / HA


def q_factorial_mp(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return r


# Plancherel-A weights for n=3
QDIM_SYM = mp.mpf(1)
QDIM_STD = qint(2)
QDIM_ALT = mp.mpf(1)
NF3      = q_factorial_mp(3)
W_SYM_A = QDIM_SYM**2 / NF3
W_STD_A = QDIM_STD**2 / NF3
W_ALT_A = QDIM_ALT**2 / NF3

# Wenzl-B weights for n=3 (loaded from canonical witness)
def load_wenzl_n(n):
    path = Path(__file__).parent / "y-lambda-wenzl-witness.json"
    with open(path) as f:
        d = json.load(f)
    table = d["tables_by_n"].get(str(n))
    return {tuple(w["partition"]): mp.mpf(w["y_lambda_numeric"])
            for w in table["weights"]}

wenzl3 = load_wenzl_n(3)
W_SYM_B = wenzl3[(3,)]
W_STD_B = wenzl3[(2, 1)]
W_ALT_B = wenzl3[(1, 1, 1)]

# Wenzl for n=2 (electron)
wenzl2 = load_wenzl_n(2)
W_SYM_e_B = wenzl2[(2,)]
W_ALT_e_B = wenzl2[(1, 1)]


def Phi_q_mpfr(z, max_k=2000):
    if abs(z) >= Q0:
        return mp.inf
    product = mp.mpf(1)
    qi_pow = QI0
    eps = mp.mpf(10) ** (-(mp.mp.dps + 5))
    for _ in range(max_k):
        term = qi_pow * z
        factor = mp.mpf(1) - term
        if mp.fabs(factor) < eps:
            return mp.inf
        product /= factor
        if mp.fabs(term) < eps:
            break
        qi_pow *= QI0
    return product


def additive_wedderburn_volumes(crossings_per_gen, n_strands, weights):
    """Compute V̂_full per generator with given (w_sym, w_std, w_alt)."""
    w_sym, w_std, w_alt = weights
    vols = []
    for gen in range(n_strands - 1):
        a, b = mp.mpf(0), mp.mpf(1)
        sp_val = mp.mpf(1)
        ap_val = mp.mpf(1)
        for c, d in crossings_per_gen.get(gen, []):
            c_mp = mp.mpf(c)
            d_mp = mp.mpf(d)
            a, b = (a * c_mp * HA + a * d_mp + b * c_mp,
                    a * c_mp + b * d_mp)
            sp_val *= c_mp * Q0 + d_mp
            ap_val *= -c_mp * QI0 + d_mp
        Vs = Z_MARK * a + b
        Vf = w_sym * sp_val + w_std * Vs + w_alt * ap_val
        vols.append({"std": Vs, "sym": sp_val, "alt": ap_val, "full": Vf})
    return vols


def mass_from_tower(vols):
    n = len(vols)
    desc = mp.mpf(1)
    for v in vols:
        desc *= v["full"]
    desc = mp.fabs(desc)
    single = mp.mpf(0)
    for v in vols:
        single += Phi_q_mpfr(mp.fabs(v["full"]))
    cross = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            cross += Z_MARK**2 * Phi_q_mpfr(
                mp.fabs(vols[i]["full"] * vols[j]["full"])
            )
    return desc, single, cross, desc + single + cross


HA_FLOAT = float(HA)
electron_cross = {0: [(1, 0)] * 3}
proton_cross = {
    0: [(1, 0)] * 3 + [(1, 0)] + [(1, -HA_FLOAT/2)] + [(1, 0)] * 2,
    1: [(1, -HA_FLOAT)] * 3 + [(1, -HA_FLOAT/2)],
}
neutron_cross = {
    0: [(1, 0)] * 3 + [(1, -HA_FLOAT/2)] + [(1, -HA_FLOAT/2)] + [(1, 0)] * 2,
    1: [(1, -HA_FLOAT)] * 3 + [(1, -HA_FLOAT)],
}


def main():
    print("=" * 78)
    print("Probe — proton mass with Wenzl y_λ weights vs Plancherel")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(Q0, 30)}")
    print(f"  m_e = {M_E_MEV} MeV")
    print()
    print("  Plancherel-A weights @ n=3:")
    print(f"    w_sym = dim_q((3,))²/[3]_q!     = {float(W_SYM_A):.6f}")
    print(f"    w_std = dim_q((2,1))²/[3]_q!    = {float(W_STD_A):.6f}")
    print(f"    w_alt = dim_q((1,1,1))²/[3]_q!  = {float(W_ALT_A):.6f}")
    print(f"    Σ                                = {float(W_SYM_A + W_STD_A + W_ALT_A):.6f}")
    print()
    print("  Wenzl-B weights @ n=3 (from y-lambda-wenzl-witness.json):")
    print(f"    y_(3)     = {float(W_SYM_B):.6f}")
    print(f"    y_(2,1)   = {float(W_STD_B):.6f}")
    print(f"    y_(1,1,1) = {float(W_ALT_B):.6f}")
    print(f"    Σ          = {float(W_SYM_B + W_STD_B + W_ALT_B):.6f}")
    print()

    plancherel = (W_SYM_A, W_STD_A, W_ALT_A)
    wenzl = (W_SYM_B, W_STD_B, W_ALT_B)

    # Electron uses n=2 weights, but electron's V̂ formula has only sym/alt
    # (no std at H_2). For consistency just compute with both schemes.
    # mass_endomorphism uses n=3 weights even for electron (per code).

    print("━━ ELECTRON (uses n=3 weights per mass_endomorphism convention)")
    e_vols_A = additive_wedderburn_volumes(electron_cross, 2, plancherel)
    _, _, _, e_total_A = mass_from_tower(e_vols_A)
    e_vols_B = additive_wedderburn_volumes(electron_cross, 2, wenzl)
    _, _, _, e_total_B = mass_from_tower(e_vols_B)
    print(f"   V̂(plancherel) = {mp.nstr(e_vols_A[0]['full'], 8)}")
    print(f"   V̂(wenzl)      = {mp.nstr(e_vols_B[0]['full'], 8)}")
    print(f"   total(plancherel) = {mp.nstr(e_total_A, 10)}")
    print(f"   total(wenzl)      = {mp.nstr(e_total_B, 10)}")
    print()

    print("━━ PROTON")
    p_vols_A = additive_wedderburn_volumes(proton_cross, 3, plancherel)
    _, _, _, p_total_A = mass_from_tower(p_vols_A)
    p_vols_B = additive_wedderburn_volumes(proton_cross, 3, wenzl)
    _, _, _, p_total_B = mass_from_tower(p_vols_B)
    print(f"   V̂_0 V̂_1  (plancherel) = {mp.nstr(p_vols_A[0]['full'], 6)}, {mp.nstr(p_vols_A[1]['full'], 6)}")
    print(f"   V̂_0 V̂_1  (wenzl)      = {mp.nstr(p_vols_B[0]['full'], 6)}, {mp.nstr(p_vols_B[1]['full'], 6)}")
    print(f"   total(plancherel) = {mp.nstr(p_total_A, 10)}")
    print(f"   total(wenzl)      = {mp.nstr(p_total_B, 10)}")
    print()

    print("━━ NEUTRON")
    n_vols_A = additive_wedderburn_volumes(neutron_cross, 3, plancherel)
    _, _, _, n_total_A = mass_from_tower(n_vols_A)
    n_vols_B = additive_wedderburn_volumes(neutron_cross, 3, wenzl)
    _, _, _, n_total_B = mass_from_tower(n_vols_B)
    print(f"   total(plancherel) = {mp.nstr(n_total_A, 10)}")
    print(f"   total(wenzl)      = {mp.nstr(n_total_B, 10)}")
    print()

    # Mass ratios under both schemes
    print("=" * 78)
    print(f"{'scheme':<14} {'m_p/m_e':>14} {'err vs CODATA':>14} {'m_n/m_e':>12} {'err':>10}")
    print("-" * 78)
    target_p = mp.mpf(M_P_MEV) / mp.mpf(M_E_MEV)
    target_n = mp.mpf(M_N_MEV) / mp.mpf(M_E_MEV)

    for label, e_t, p_t, n_t in (
        ("Plancherel-A", e_total_A, p_total_A, n_total_A),
        ("Wenzl-B",      e_total_B, p_total_B, n_total_B),
    ):
        rp = p_t / e_t
        rn = n_t / e_t
        ep = float((rp - target_p) / target_p * 100)
        en = float((rn - target_n) / target_n * 100)
        print(f"{label:<14} {float(rp):>14.4f} {ep:>+13.4f}% {float(rn):>12.4f} {en:>+9.4f}%")
    print(f"{'CODATA':<14} {float(target_p):>14.4f} {'(target)':>14} {float(target_n):>12.4f}")

    # Witness
    w = (
        WitnessBuilder("probe-proton-with-wenzl-weights", engine="python+mpmath")
        .set_description(
            "Test if switching mass_endomorphism's Plancherel weights "
            "(dim_q²/[n]_q!) to Wenzl y_λ from y-lambda-wenzl-witness "
            "closes the +1.84% m_p/m_e residual. Both at 50 dps."
        )
        .set_content_block("prop:y-lambda-recipe-from-partition")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("m_p_AME_MeV", M_P_MEV)
        .add_parameter("m_n_AME_MeV", M_N_MEV)
        .add_parameter("mpmath_dps", mp.mp.dps)
        .add_data("plancherel_results", {
            "e_total_50dps": mp.nstr(e_total_A, 30),
            "p_total_50dps": mp.nstr(p_total_A, 30),
            "n_total_50dps": mp.nstr(n_total_A, 30),
            "m_p_over_m_e_50dps": mp.nstr(p_total_A / e_total_A, 30),
            "m_n_over_m_e_50dps": mp.nstr(n_total_A / e_total_A, 30),
            "m_p_over_m_e_err_pct": float(((p_total_A/e_total_A) - target_p) / target_p * 100),
            "m_n_over_m_e_err_pct": float(((n_total_A/e_total_A) - target_n) / target_n * 100),
        })
        .add_data("wenzl_results", {
            "e_total_50dps": mp.nstr(e_total_B, 30),
            "p_total_50dps": mp.nstr(p_total_B, 30),
            "n_total_50dps": mp.nstr(n_total_B, 30),
            "m_p_over_m_e_50dps": mp.nstr(p_total_B / e_total_B, 30),
            "m_n_over_m_e_50dps": mp.nstr(n_total_B / e_total_B, 30),
            "m_p_over_m_e_err_pct": float(((p_total_B/e_total_B) - target_p) / target_p * 100),
            "m_n_over_m_e_err_pct": float(((n_total_B/e_total_B) - target_n) / target_n * 100),
        })
        .add_data("plancherel_minus_wenzl_in_me_units", {
            "e_total_diff": mp.nstr(e_total_A - e_total_B, 10),
            "p_total_diff": mp.nstr(p_total_A - p_total_B, 10),
            "n_total_diff": mp.nstr(n_total_A - n_total_B, 10),
        })
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
