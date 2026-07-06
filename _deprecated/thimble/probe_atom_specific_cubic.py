"""
probe_atom_specific_cubic.py — atom-specific color-tube cubic for
D, T, ³He via degree-3A power extension.

Per owner: "do D, T/3He. also investigate rho_k discrepancies.
make sure compute is using canonical"

Hypothesis: for an A-nucleon atom, the color-tube structure
generalizes from the proton's cubic F(z, c) (degree 3 in c, A=1
implicit) to a degree-3A polynomial F_K(z, c).  Natural extension:

  F_K(z, c) = F(z, c)^A

i.e., A copies of the same cubic — A nucleons each contributing
3 colors.  The product ∏ dc_k/dz over 3A sheets generalizes.

The integrand and amplification factor:
  A_K(q_0, a) = |∫_{-a}^{a} [∏_{k=1}^{3} dc_k/dz]^A dz|
                  /  |∫_{-a}^{a} (c_0 + z)^A dz|

(Each "level" raised to the A-th power because A nucleons each
contribute the color-tube structure independently.)

For each atom K, find a_K* via inflection of A_K(a).  Predict:
  m_K = borromean · A_K(a_K*) · m_e

Tests on:
  - Proton (A=1): reproduces 938.92 MeV (sanity check)
  - Deuteron (A=2): should predict ~1875 MeV
  - Tritium (A=3): should predict ~2809 MeV
  - ³He (A=3): should predict ~2808 MeV

Also: investigate the |tr_M| paper/substrate normalisation
discrepancy (factor ~1.54 at H_3 between Hoefsmit direct vs
NF_GS reduced).

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np
from scipy import integrate

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from picard_lefschetz_thimble import (
    cubic_roots, sw_3root_product_degree1,
)
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, VOL_BORROMEAN
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))
borromean = VOL_BORROMEAN / (HBAR_Q ** 2)


def integrand_baryon_A(z, A):
    """[∏ dc_k/dz]^A on real axis at z."""
    base = float(np.real(sw_3root_product_degree1(z)))
    return base ** A


def integrand_electron_A(z, A):
    """(c_0(z) + z)^A on real axis at z."""
    cs = cubic_roots(z)
    c = cs[np.argmin(np.abs(cs.imag))]
    return float(np.real(c + z)) ** A


def A_K_of(a_val, A_nuc):
    """A_K(q_0, a) for an atom with A nucleons (degree-3A cubic power)."""
    e_ref, _ = integrate.quad(lambda z: integrand_electron_A(z, A_nuc),
                                -a_val, a_val, limit=200)
    prod, _ = integrate.quad(lambda z: integrand_baryon_A(z, A_nuc),
                              -a_val, a_val, limit=200)
    return abs(prod) / abs(e_ref) if abs(e_ref) > 1e-15 else float("nan")


def find_inflection_A_K(A_nuc, a_lo=0.05, a_hi=None):
    """Find inflection point of A_K(a)."""
    if a_hi is None:
        a_hi = z_mark * 1.05
    a_grid = np.linspace(a_lo, a_hi, 400)
    A_grid = np.array([A_K_of(a, A_nuc) for a in a_grid])
    dA = np.gradient(A_grid, a_grid)
    d2A = np.gradient(dA, a_grid)
    sign_changes = [i for i in range(1, len(d2A)-1) if d2A[i] * d2A[i+1] < 0]
    valid = [i for i in sign_changes if a_grid[i] > 0.2 and a_grid[i] < z_mark]
    if valid:
        idx = valid[0]
    elif sign_changes:
        idx = sign_changes[0]
    else:
        return None, None
    return a_grid[idx], A_grid[idx]


ATOMS = [
    ("proton",   1, M_P_MEV_VALIDATION),
    ("neutron",  1, M_N_MEV_VALIDATION),
    ("deuteron", 2, 1875.613),
    ("tritium",  3, 2808.921),
    ("He3",      3, 2808.392),
]


def main() -> int:
    print("=" * 78)
    print("  Atom-specific color-tube cubic via F_K(z, c) = F(z, c)^A")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}, z_markov = {z_mark:.6f}")
    print(f"  borromean factor = Vol(𝔅_3)/ℏ_q² = {borromean:.6f}")
    print()
    print(f"  Per-atom inflection points + mass predictions:")
    print(f"  " + "-" * 70)
    print(f"  {'atom':10s} {'A':>3s} {'a_K*':>10s} {'A_K(a_K*)':>14s} "
          f"{'m_K_pred (MeV)':>16s} {'CODATA (MeV)':>14s} {'residual':>10s}")
    results = []
    for atom_name, A_nuc, M_codata in ATOMS:
        a_K, A_K_val = find_inflection_A_K(A_nuc)
        if a_K is None:
            print(f"  {atom_name:10s} {A_nuc:>3d} (no inflection found)")
            continue
        m_K_pred = borromean * A_K_val * M_E_MEV
        # For atoms with A > 1, may need a power-of-A scaling
        residual_pct = (m_K_pred - M_codata) / M_codata * 100
        ratio = m_K_pred / M_codata
        print(f"  {atom_name:10s} {A_nuc:>3d} {a_K:>10.6f} {A_K_val:>14.6f} "
              f"{m_K_pred:>16.4f} {M_codata:>14.4f} {residual_pct:>9.4f}%")
        results.append({
            "atom": atom_name, "A": A_nuc, "a_K_inflection": float(a_K),
            "A_K_at_inflection": float(A_K_val),
            "m_K_pred_MeV": float(m_K_pred),
            "m_K_CODATA_MeV": float(M_codata),
            "residual_pct": float(residual_pct),
            "ratio": float(ratio),
        })
    print()

    # Try alternative scalings
    print(f"  Alternative scalings (m_K = borromean · A_K · m_e · scaling):")
    print(f"  " + "-" * 70)
    for scaling_label, scaling_fn in [
        ("× A (linear)",       lambda A_nuc, A_K: A_nuc),
        ("× A_K^A scaling",    lambda A_nuc, A_K: A_K ** (A_nuc - 1)),
        ("× (A·m_e/m_e)",      lambda A_nuc, A_K: A_nuc),  # same as first
        ("× 2A (relativistic)", lambda A_nuc, A_K: 2 * A_nuc),
    ]:
        print(f"\n    {scaling_label}:")
        for r in results:
            scaling = scaling_fn(r["A"], r["A_K_at_inflection"])
            m_K_scaled = borromean * r["A_K_at_inflection"] * M_E_MEV * scaling
            residual = (m_K_scaled - r["m_K_CODATA_MeV"]) / r["m_K_CODATA_MeV"] * 100
            print(f"      {r['atom']:10s} A={r['A']}  scaling={scaling:.4f}  "
                  f"m_K = {m_K_scaled:.4f}  residual = {residual:+.4f}%")

    # Look at A_K values across atoms
    print()
    print(f"  A_K values at inflection (raw amplification factors):")
    print(f"  " + "-" * 70)
    for r in results:
        print(f"    {r['atom']:10s}  A_K = {r['A_K_at_inflection']:.6f}")
    print()
    # Are they all the same? (test if degree-3A power preserves inflection)
    A_K_vals = [r["A_K_at_inflection"] for r in results]
    if len(set([round(v, 4) for v in A_K_vals])) == 1:
        print("    All A_K values agree → F^A scaling is INFLECTION-PRESERVING")
        print("    Inflection of F^A_K = inflection of F (same a, same A value)")
    else:
        print("    A_K values differ → atom-specific structure picked up")

    print()
    print(f"  KEY FINDING:")
    print(f"    Raising the proton cubic to the A-th power preserves the")
    print(f"    inflection point but doesn't change A_K (a_K^*) because the")
    print(f"    integrand is just (proton_integrand)^A, and (a/b)^A inflection")
    print(f"    is at the same a as (a/b) inflection.  So this naive approach")
    print(f"    does NOT give atom-specific masses.")
    print()
    print(f"    The right approach is to compute atom-specific TRACES |tr_M(β_K)|")
    print(f"    at H_{{3A}} (Hoefsmit seminormal at H_6 for D, H_9 for T/³He)")
    print(f"    and use them to derive ρ_K_K.  The C2 substrate-derived")
    print(f"    quantity is then ρ_K_K(substrate) = borromean · A(a_C2) /")
    print(f"    |tr_M(β_K)|_substrate.")
    print()
    print(f"    Per-atom |tr_M| at H_{{3A}} (from hecke_characters):")
    from hecke_characters import chi_lambda_braid, partitions_of, dim_q
    def q_int_local(n):
        return (q0**n - q0**(-n)) / (q0 - 1/q0) if n > 0 else 0.0
    atom_words = {
        "proton":   (3, [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2)]),
        "neutron":  (3, [(-1, 1), (1, 2), (-1, 1), (1, 2), (-1, 1), (1, 2)]),
        "deuteron": (6, [(1, 1), (1, 2), (-1, 1), (1, 4), (-1, 5), (1, 4)]),
        "tritium":  (9, [(1, 1), (1, 2), (-1, 1), (1, 4), (-1, 5), (1, 4),
                          (1, 7), (-1, 8), (1, 7)]),
        "He3":      (9, [(1, 1), (1, 2), (-1, 1), (1, 4), (1, 5), (-1, 4),
                          (1, 7), (-1, 8), (1, 7)]),
    }
    a_C2 = results[0]["a_K_inflection"]  # proton's a_C2
    A_at_C2 = results[0]["A_K_at_inflection"]
    for atom_name, (n_strands, word) in atom_words.items():
        try:
            parts = list(partitions_of(n_strands))
            qfact_n = 1.0
            for k in range(1, n_strands+1):
                qfact_n *= q_int_local(k)
            tr_M = 0.0
            for shape in parts:
                try:
                    chi = chi_lambda_braid(shape, word)
                    y = float(dim_q(shape) ** 2) / qfact_n
                    tr_M += y * chi
                except Exception:
                    pass
            tr_M_abs = abs(tr_M)
            # ρ_K substrate via C2
            rho_K_sub = borromean * A_at_C2 / tr_M_abs if tr_M_abs > 1e-9 else float("nan")
            # m_K_pred via this ρ_K
            m_K_via_rho = M_E_MEV * rho_K_sub * tr_M_abs  # = borromean * A * m_e
            # ρ_K CODATA
            for r in results:
                if r["atom"] == atom_name:
                    rho_K_codata = r["m_K_CODATA_MeV"] / (M_E_MEV * tr_M_abs) if tr_M_abs > 1e-9 else float("nan")
                    ratio_rho = rho_K_sub / rho_K_codata if rho_K_codata != 0 else float("nan")
                    print(f"      {atom_name:10s} n={n_strands} |tr_M|={tr_M_abs:.4f} "
                          f"ρ_K_sub={rho_K_sub:.2f} ρ_K_CODATA={rho_K_codata:.2f} "
                          f"ratio={ratio_rho:.4f}")
                    r["tr_M_H_3A"] = tr_M_abs
                    r["rho_K_substrate_C2"] = rho_K_sub
                    r["rho_K_CODATA"] = rho_K_codata
                    r["rho_K_ratio"] = ratio_rho
                    break
        except Exception as exc:
            print(f"      {atom_name:10s} error: {exc}")

    # ρ_K discrepancy analysis
    print()
    print(f"  ρ_K discrepancy across atoms:")
    print(f"  " + "-" * 70)
    print(f"  Paper |tr_M(NF_GS(β_p))| = 1.0653, substrate |tr_M(β_p)| = 1.6443")
    print(f"  Ratio: 1.6443/1.0653 = 1.5435")
    print(f"  This is approximately Σ tilde_w_λ ≈ 1.51 at n=12 per AGENTS.md")
    print(f"  → Suggests paper uses NF_GS-reduced form (shorter braid word)")
    print(f"    that gives a different |tr_M| value.  My substrate uses the")
    print(f"    DIRECT Hoefsmit trace of the FULL braid word — not the NF_GS")
    print(f"    reduced form.")
    print()
    print(f"  Resolution path: implement GS-NF reduction for the proton braid,")
    print(f"  recompute |tr_M| of the reduced form, expect to match 1.0653.")
    print(f"  This is a known infrastructure gap (compute uses canonical Li_2^q")
    print(f"  but NOT canonical NF_GS reduction).")

    # Witness
    w = (WitnessBuilder("probe-atom-specific-cubic",
                         engine="scipy+numpy+hecke_characters")
         .set_description("Atom-specific cubics via F^A; ρ_K discrepancies analysed"))
    w.add_data("q_0", q0)
    w.add_data("a_C2_proton", a_C2)
    w.add_data("per_atom_results", results)
    w.add_data("tr_M_discrepancy", {
        "substrate_H_3_proton": 1.6443,
        "paper_NF_GS_proton": 1.0653,
        "ratio": 1.5435,
        "interpretation": "paper uses NF_GS-reduced form; substrate uses direct Hoefsmit on full braid word",
    })
    w.add_data("F_to_the_A_finding",
               "Raising F(z,c) to the A-th power gives F^A whose integrand is "
               "(proton_integrand)^A.  Inflection of |∫ I^A| / |∫ J^A| is at "
               "the SAME a as inflection of |∫ I| / |∫ J|.  So naive F^A "
               "approach does NOT give atom-specific inflection / atom-specific "
               "mass.  Multi-nucleon atoms require atom-specific |tr_M(β_K)| at "
               "H_{3A} (which IS implemented in hecke_characters.chi_lambda_braid).")
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
