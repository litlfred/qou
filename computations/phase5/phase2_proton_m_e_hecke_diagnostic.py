#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical-only diagnostic.
"""
Phase 2 of the 1 ppb workplan
([`docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 2`](../../docs/audits/2026-05-10-1ppb-workplan-update.md))
— **derive m_p_Hecke and m_e_Hecke from first principles** to replace
the placeholder literals `M_HECKE_PIPELINE_AT_Q0['p']=1.4283` /
`['e']=0.0007783` in `derivation_chain.py:73-76`.

Status: **diagnostic-only**.  Full closure requires either a
reformulation of the 6-term mass tower (currently non-converging at
the 1.83 % floor admitted in `mass_endomorphism.py`) OR an alternative
Path A ratio-based construction.  This script makes the gap visible
and exposes the empirical numbers.

Three approaches surveyed:

A. **Direct 6-term sum at q_0** (`mass-formula-6term-mpfr-50dps.witness.json`)
   sum_K(p) = T1 + T2 + T3 + T4 + T5 + T6 = -4.77 (sign-indefinite)
   sum_K(D) = +9.68e5 (T2+T3 millions of MeV — scale-broken)

B. **Categorical-formula ratio**
   m_p_Hecke / m_e_Hecke ≈ ρ_p · |tr_M(β_p)| / (ρ_e · |tr_M(β_e)|)
                        = 1 · 1.0653 / (1 · 0.499) = 2.135
   CODATA m_p / m_e = 1836 — off by factor 860.

C. **Placeholder ratio (current state)**
   M_HECKE_PIPELINE_AT_Q0['p']/['e'] = 1.4283 / 0.0007783 ≈ 1835.4
   matches CODATA m_p/m_e to ~470 ppb, BUT (per
   `2026-05-09-proton-m_e-anomaly.md`) the placeholder ratio lands at
   `(m_p - m_e)/m_e + 470 ppb`, NOT `m_p/m_e`.  Hidden algebraic +1.

Finding: none of A, B, C is the right derivation.  A is incomplete
(missing terms, sign issues), B oversimplified (ignores higher T_k),
C numerologically calibrated.  The honest Phase 2 deliverable is to
construct a Path A chain that aggregates only the components currently
on solid footing — T1 (Markov trace; canonical Wenzl-bridge anchor)
and T4 (Frobenius per-vortex; closed-form at H_3·A) — and quarantine
T2/T3/T5/T6 as known-broken-or-empirical.

Output: `phase2-m-e-hecke-diagnostic.witness.json`.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION as M_P_MEV  # validation-only
from derivation_chain import M_HECKE_PIPELINE_AT_Q0, TR_M_AT_Q0
from witness_base import WitnessBuilder

ASSEMBLY_DIR = Path(__file__).parent
SIX_TERM_WITNESS = ASSEMBLY_DIR / "mass-formula-6term-mpfr-50dps.witness.json"


def six_term_sum(atom_record: dict) -> tuple[mp.mpf, dict[str, mp.mpf]]:
    """Sum the 6 terms for a given atom record from the mpfr witness."""
    keys = (
        "term1_descended", "term2_single", "term3_pair",
        "term4_frob_per_vortex", "term5_chirality_bw", "term6_habiro_residue",
    )
    terms: dict[str, mp.mpf] = {}
    total = mp.mpf(0)
    for k in keys:
        v = atom_record.get(k, 0)
        try:
            mv = mp.mpf(str(v)) if not (isinstance(v, str) and "Error" in v) else mp.mpf(0)
        except (ValueError, TypeError):
            mv = mp.mpf(0)
        terms[k] = mv
        total += mv
    return total, terms


def t1_t4_only_sum(terms: dict[str, mp.mpf]) -> mp.mpf:
    """Restricted Path A: only T1 + T4 (the two cleanly-derived terms).

    Quarantines T2/T3 (out of scale on nuclei), T5 (sign-indefinite),
    T6 (Habiro residue — separately derived, currently small).
    """
    return terms["term1_descended"] + terms["term4_frob_per_vortex"]


def categorical_ratio_for_atom(atom_label: str, tr_M_q0: mp.mpf) -> mp.mpf | None:
    """Approach B: ratio via the categorical formula M = ρ · m_e · |tr_M|.

    Returns m_K_Hecke / m_e_Hecke under the simple categorical
    formula — equivalent to ρ_K · |tr_M(β_K)| / (ρ_e · |tr_M(β_e)|).

    Electron's |tr_M(β_e)| at H_2 (zero-crossings) = z = 1/(√q + 1/√q).
    """
    from q_parameter import Q as Q0
    q = mp.mpf(str(Q0))
    z_electron = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    rho_atom = {"proton": 1, "neutron": 1, "deuteron": 1}.get(atom_label, 1)
    rho_e = 1
    return (rho_atom * tr_M_q0) / (rho_e * z_electron)


def main() -> int:
    w = WitnessBuilder("phase2-m-e-hecke-diagnostic", engine="mpmath")
    w.set_audit_only("docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.set_description(
        "Phase 2 diagnostic — surveys three approaches for deriving "
        "m_p_Hecke / m_e_Hecke to replace the DEPRECATED placeholder "
        "literals in derivation_chain.M_HECKE_PIPELINE_AT_Q0.  Finds "
        "all three approaches incomplete: 6-term sum is sign-indefinite "
        "for the proton and out-of-scale for nuclei; categorical-formula "
        "ratio reproduces only ~2.135 (vs CODATA 1836); placeholder "
        "ratio matches numerologically but at (m_p - m_e)/m_e, not "
        "m_p/m_e.  Quarantines T2/T3/T5/T6 as known-broken-or-empirical "
        "and exposes a T1+T4 Path A residual for downstream chains."
    )
    w.set_content_block("prop:atom-knot-mass-derivation")

    if not SIX_TERM_WITNESS.exists():
        print(f"missing input: {SIX_TERM_WITNESS}")
        return 1

    six_term = json.loads(SIX_TERM_WITNESS.read_text())
    atoms = six_term["data"]["results"]

    print("=" * 90)
    print("PHASE 2 — m_e_Hecke / m_p_Hecke DIAGNOSTIC (Path A construction survey)")
    print("=" * 90)
    print()
    # M_HECKE_PIPELINE_AT_Q0 returns mp.mpf (PR #637); use mp.nstr
    # for display, preserve precision per the no-float64 directive.
    _p_over_e = M_HECKE_PIPELINE_AT_Q0['p'] / M_HECKE_PIPELINE_AT_Q0['e']
    print(f"  CODATA m_p / m_e  = {float(M_P_MEV/M_E_MEV):.4f}")
    print(f"  Path A ratio      = {mp.nstr(M_HECKE_PIPELINE_AT_Q0['p'], 6)}/"
          f"{mp.nstr(M_HECKE_PIPELINE_AT_Q0['e'], 6)} = "
          f"{mp.nstr(_p_over_e, 6)}")
    print()

    # ─── Approach A: full 6-term sum ────────────────────────────────────
    print("A. Full 6-term sum (mass-formula-6term-mpfr-50dps):")
    print(f"  {'atom':>10}  {'sum_6term':>14}  {'T1':>10}  {'T4':>10}  {'T1+T4':>10}")
    a_results = {}
    for atom_rec in atoms:
        atom_label = atom_rec["atom"]
        total, terms = six_term_sum(atom_rec)
        t1_t4 = t1_t4_only_sum(terms)
        a_results[atom_label] = {
            "sum_6term": str(total),
            "terms": {k: str(v) for k, v in terms.items()},
            "t1_t4_only": str(t1_t4),
        }
        print(f"  {atom_label:>10}  {float(total):>+14.4e}  "
              f"{float(terms['term1_descended']):>+10.4f}  "
              f"{float(terms['term4_frob_per_vortex']):>+10.4f}  "
              f"{float(t1_t4):>+10.4f}")
    print()

    # ─── Approach B: categorical-formula ratio ──────────────────────────
    print("B. Categorical-formula ratio M_K_Hecke / m_e_Hecke (= ρ · |tr_M|):")
    b_results = {}
    for atom_short, label in [("p", "proton"), ("n", "neutron"), ("D", "deuteron")]:
        if atom_short not in TR_M_AT_Q0:
            continue
        tr = mp.mpf(str(TR_M_AT_Q0[atom_short]))
        ratio = categorical_ratio_for_atom(label, tr)
        b_results[label] = {
            "tr_M_q0": str(tr),
            "categorical_ratio_to_m_e_Hecke": str(ratio),
        }
        print(f"  {label:>10}  |tr_M| = {float(tr):.6f}   "
              f"ratio_to_m_e_Hecke = {float(ratio):.4f}")
    print()
    if "proton" in b_results:
        ratio_pe = mp.mpf(b_results["proton"]["categorical_ratio_to_m_e_Hecke"])
        print(f"  m_p/m_e (categorical-ratio prediction) = {float(ratio_pe):.4f}")
        print(f"  m_p/m_e (CODATA)                       = {float(M_P_MEV/M_E_MEV):.4f}")
        print(f"  Categorical ratio is OFF by factor "
              f"{float(M_P_MEV/M_E_MEV / ratio_pe):.1f}")
    print()

    # ─── Approach C: Path A ratio (post-PR #637 derived values) ─────────
    # M_HECKE_PIPELINE_AT_Q0 now returns substrate-derived mp.mpf
    # (Path A T1+T4); preserve as mp.mpf, display via mp.nstr.
    print("C. Path A ratio (substrate-derived state, post-PR #637):")
    p_derived = M_HECKE_PIPELINE_AT_Q0["p"]
    e_derived = M_HECKE_PIPELINE_AT_Q0["e"]
    path_a_ratio = p_derived / e_derived
    codata_pe = M_P_MEV / M_E_MEV
    codata_pe_minus_one = (M_P_MEV - M_E_MEV) / M_E_MEV
    c_results = {
        "M_p_Hecke_path_a": mp.nstr(p_derived, 12),
        "M_e_Hecke_path_a": mp.nstr(e_derived, 12),
        "path_a_ratio": mp.nstr(path_a_ratio, 12),
        "codata_m_p_over_m_e": mp.nstr(codata_pe, 12),
        "codata_m_p_minus_m_e_over_m_e": mp.nstr(codata_pe_minus_one, 12),
        "diff_to_codata_p_over_e_ppb":
            mp.nstr((path_a_ratio - codata_pe) / codata_pe * mp.mpf("1e9"), 6),
        "diff_to_codata_minus_one_ppb":
            mp.nstr((path_a_ratio - codata_pe_minus_one) / codata_pe_minus_one * mp.mpf("1e9"), 6),
    }
    print(f"  Path A ratio     = {mp.nstr(path_a_ratio, 6)}")
    print(f"  CODATA m_p/m_e   = {mp.nstr(codata_pe, 6)}  "
          f"diff = {c_results['diff_to_codata_p_over_e_ppb']} ppb")
    print(f"  CODATA (m_p-m_e)/m_e = {mp.nstr(codata_pe_minus_one, 6)}  "
          f"diff = {c_results['diff_to_codata_minus_one_ppb']} ppb")
    print()

    # ─── Finding ────────────────────────────────────────────────────────
    finding = (
        "Phase 2 deliverable status: NONE OF THE THREE APPROACHES CLOSES.\n"
        "  A. 6-term sum: proton sum is sign-indefinite (-4.77); D/T/³He "
        "T2+T3 are 10^5..10^6 (out of scale).\n"
        "  B. Categorical ratio: predicts m_p/m_e ≈ 2.135 vs CODATA 1836 "
        "(factor 860 off — missing the higher T_k structure).\n"
        "  C. Placeholder ratio: hits CODATA-(m_p - m_e)/m_e to ~470 ppb, "
        "NOT m_p/m_e — hidden algebraic +1 (audit doc 2026-05-09-proton-m_e-anomaly.md).\n"
        "\n"
        "Recommended forward path: a Path A *partial* chain — T1 (canonical "
        "Wenzl-bridge anchor) + T4 (Frobenius per-vortex) only — quarantining "
        "T2 (single-pole), T3 (pair-pole), T5 (chirality-BW), T6 (Habiro "
        "residue) until each closes individually.  Currently T1+T4 yields:\n"
        f"    proton:   {float(a_results['p (proton)']['t1_t4_only']):>+10.4f}\n"
        f"    neutron:  {float(a_results['n (neutron)']['t1_t4_only']):>+10.4f}\n"
        f"    deuteron: {float(a_results['D (deuteron)']['t1_t4_only']):>+10.4f}\n"
        "Note: T1+T4 ratio (proton/neutron) ~ 1.022 vs CODATA m_p/m_n ~ 0.999 "
        "(off by 2.3%) — confirming T1+T4 alone is not the right closure either, "
        "but is the cleanest currently-trustable subset.\n"
        "\n"
        "NEXT STEPS:\n"
        "  1. Rederive T2 (single-pole brane tower) at q_0 using canonical "
        "Wenzl-bridge weight; compare to the current 6-term mpfr witness "
        "values which use the legacy weight (factor-of-2 issue same root "
        "cause as habiro_interpolate_cross_validator).\n"
        "  2. Audit T5 (chirality-BW) for sign convention — current value "
        "-7.79 dominates but with the wrong sign would give the right scale.\n"
        "  3. Once T2..T6 are individually closed, replace the placeholders "
        "with sum-derived values and re-run applied_uniqueness_mass_table.py."
    )
    print(finding)

    w.add_parameter("M_E_MEV_CODATA", str(M_E_MEV))
    w.add_parameter("M_P_MEV_CODATA", str(M_P_MEV))
    w.add_data("approach_A_6term_sum", a_results)
    w.add_data("approach_B_categorical_ratio", b_results)
    w.add_data("approach_C_placeholder_anomaly", c_results)
    w.add_data("finding", finding)
    w.add_data("phase", "Phase 2 of 1ppb workplan (2026-05-10)")
    w.add_data("workplan_doc", "docs/audits/2026-05-10-1ppb-workplan-update.md")

    w.add_assertion(
        "approach_A_proton_sum_is_negative",
        computed=mp.mpf(a_results["p (proton)"]["sum_6term"]) < 0,
        expected=True,
    )
    w.add_assertion(
        "approach_B_far_from_codata",
        computed=abs(mp.mpf(b_results["proton"]["categorical_ratio_to_m_e_Hecke"]) - codata_pe) > 100,
        expected=True,
    )
    w.add_assertion(
        "approach_C_path_a_lands_at_minus_m_e",
        computed=abs(mp.mpf(c_results["diff_to_codata_minus_one_ppb"])) < 1000,
        expected=True,
    )
    w.add_assertion(
        "approach_C_path_a_diverges_from_codata",
        computed=abs(mp.mpf(c_results["diff_to_codata_p_over_e_ppb"])) > 100_000,
        expected=True,
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
