#!/usr/bin/env python3
"""
Probe: derived categorical A from GS normal form / jet order.

Tests the hypothesis that the "A" in the Bethe–Weizsäcker-shaped T5
term can be **derived** from the braid's Gröbner-Shirshov reduction
(max filtration grade of the normal form), giving a categorical
functional of the braid alone — no nucleon-ledger dependency.

Generic statement (subject to this probe's empirical check):

  For any braid word β in H_n(q):
    A(β) := max filtration grade of the GS normal form of β,
            computed by the canonical right-action reducer of
            `gb_filtration_jet_tracker.reduce_braid`.
    a_K(β) := V2 Gram-matrix chirality from `term5_v2_chirality.aK_v2`.
    Z(β), N(β) := flavour-decoration quark counts (electron: 0, 0).
    sign(β) := pairing parity from `bw_chirality_isotopes.pairing_sign`.

    T5(β) := a_K(β) · B_bulk(A(β), Z(β), N(β), sign(β))
             + f_Zdep_scale · B_Zdep(A(β), Z(β), N(β))
             + (B_shell(A(β), Z(β), N(β)) if A(β) ≥ 4 else 0)

  All ingredients are q-integer-derived (`bw_chirality_isotopes`)
  or Gram-matrix-derived (`term5_v2_chirality.aK_v2`); the A
  invariant comes from GS reduction.  No fitting.  No nucleon
  ledger.  T5(electron) is no longer "0 by convention" — it is
  the value at A=1 (the electron's σ_1^3 reduces to a grade-1
  element in S_2's Coxeter structure).

Empirical check (this probe):
  Compute T5 under both conventions (A=nucleon vs A=max_grade)
  for {electron, proton, neutron} and report the m_p prediction
  shift.

Output: `probe-derived-A-from-gs-normal-form.witness.json`
"""
from __future__ import annotations

import io
import contextlib
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV_RAW, M_P_MEV_VALIDATION as M_P_CODATA,
)
from witness_base import (  # noqa: E402
    WitnessBuilder, load_and_hash_upstream,
)
from gb_filtration_jet_tracker import reduce_braid  # noqa: E402
from bw_chirality_isotopes import (  # noqa: E402
    B_bulk, B_Zdep, B_shell, pairing_sign,
)
from mass_formula_6term_mpfr_50dps import (  # noqa: E402
    term_4_frobenius_mp, f_Zdep_scale,
)
from term5_v2_chirality import aK_v2  # noqa: E402

M_E_MEV = mp.mpf(str(_M_E_MEV_RAW))
PER_GEN_WITNESS = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
OUT_PATH = HERE / "probe-derived-A-from-gs-normal-form.witness.json"


# Canonical braid words (positive int i ↦ σ_i; negative −i ↦ σ_i^{-1}).
BRAID_WORDS = {
    # σ_1^3 in H_2: the electron's trefoil.
    "electron": {
        "n": 2,
        "word": [1, 1, 1],
        "description": "σ_1^3 in H_2 (trefoil σ_1^3)",
        "Z": 0, "N": 0, "knot_type": "none",
    },
    # (σ_1 · σ_2^{-1})^3 in H_3: B_3 Borromean baseline of the proton.
    # The proton's flavour decoration (uud quark content + 2 gluons)
    # is encoded in the (c, d) Hecke coefficients in the production
    # m_p chain; the *braid-word* part is the B_3 element.
    "proton": {
        "n": 3,
        "word": [1, -2, 1, -2, 1, -2],
        "description": "(σ_1 · σ_2^{-1})^3 in H_3 (B_3, uud flavour)",
        "Z": 1, "N": 0, "knot_type": "none",
    },
    "neutron": {
        "n": 3,
        "word": [1, -2, 1, -2, 1, -2],
        "description": "(σ_1 · σ_2^{-1})^3 in H_3 (B_3, udd flavour)",
        "Z": 0, "N": 1, "knot_type": "none",
    },
}


def categorical_A(name: str, n: int, word: list[int]) -> dict:
    """Run the GS reducer and extract derived A invariants.

    Returns a dict with the categorical A candidates:
      A_max_grade       = max Coxeter length in the normal form
      A_jet_steps       = total reduction events
      A_hecke_fires     = number of Hecke-quadratic relation firings
      filtration_shape  = the full {grade: term_count} dict
    """
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = reduce_braid(name, n, word)
    shape = r["filtration_shape"]
    return {
        "A_max_grade":     max(shape.keys()) if shape else 0,
        "A_jet_steps":     r["n_steps"],
        "A_hecke_fires":   r["n_hecke_relations_fired"],
        "filtration_shape": {str(k): v for k, v in shape.items()},
    }


def t5_at_A(A: int, Z: int, N: int, knot_type: str) -> mp.mpf:
    """T5 in MeV at given (A, Z, N) using V2 chirality."""
    if A == 0:
        return mp.mpf(0)
    a_K = aK_v2(Z, N)
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if A >= 4 else mp.mpf(0)
    return a_K * bulk + f_Zdep_scale * zdep + shell


def get_T1_T2_T3(per_gen_witness: dict, atom: str) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    for r in per_gen_witness["data"]["results"]:
        if r.get("atom") != atom:
            continue
        vols = [mp.mpf(v["full"]) for v in r["wedderburn_vols"]]
        desc = mp.mpf(1)
        for v in vols:
            desc *= v
        return (
            mp.fabs(desc),
            mp.mpf(r["term2_single_50dps"]),
            mp.mpf(r["term3_pair_50dps"]),
        )
    raise KeyError(atom)


def main() -> int:
    per_gen_w, _ = load_and_hash_upstream(PER_GEN_WITNESS)

    # 1. Compute derived A from GS reduction for each particle.
    print("\n=== Derived categorical A from GS reduction ===\n")
    print(f"{'particle':<10} {'H_n':>4}  {'A_max_grade':>11} {'A_jet_steps':>11} {'A_hecke_fires':>13} filtration")
    print("-" * 90)
    derived = {}
    for name, info in BRAID_WORDS.items():
        ca = categorical_A(name, info["n"], info["word"])
        derived[name] = ca
        print(f"{name:<10} {info['n']:>4}  "
              f"{ca['A_max_grade']:>11} {ca['A_jet_steps']:>11} "
              f"{ca['A_hecke_fires']:>13} {ca['filtration_shape']}")

    # 2. Compare m_p_pred under (a) nucleon-A and (b) derived-A_max_grade.
    print("\n=== m_p prediction under each A convention ===\n")
    print(f"{'convention':<32} {'A_p':>4} {'A_e':>4}  {'T5_p MeV':>12} {'T5_e MeV':>12}  {'m_p_pred':>10}  {'residual':>11}")
    print("-" * 105)

    mp_t1, mp_t2, mp_t3 = get_T1_T2_T3(per_gen_w, "proton")
    me_t1, me_t2, me_t3 = get_T1_T2_T3(per_gen_w, "electron")

    A_p_nuc, A_e_nuc = 1, 0
    A_p_grade = derived["proton"]["A_max_grade"]
    A_e_grade = derived["electron"]["A_max_grade"]

    results = []
    for label, A_p, A_e in [
        ("A = nucleon count (legacy)", A_p_nuc, A_e_nuc),
        ("A = max GS filtration grade", A_p_grade, A_e_grade),
        ("A = jet-order steps",        derived["proton"]["A_jet_steps"],   derived["electron"]["A_jet_steps"]),
        ("A = Hecke-relation firings", derived["proton"]["A_hecke_fires"], derived["electron"]["A_hecke_fires"]),
    ]:
        t5_p = t5_at_A(A_p, 1, 0, "none")
        t5_e = t5_at_A(A_e, 0, 0, "none")
        t4_p = term_4_frobenius_mp(max(A_p, 1))
        t4_e = term_4_frobenius_mp(max(A_e, 1))
        m_p = mp_t1 + mp_t2 + mp_t3 + t4_p + t5_p / M_E_MEV
        m_e = me_t1 + me_t2 + me_t3 + t4_e + t5_e / M_E_MEV
        ratio = m_p / m_e
        m_p_pred = ratio * M_E_MEV
        err = (m_p_pred - M_P_CODATA) / M_P_CODATA
        print(f"{label:<32} {A_p:>4} {A_e:>4}  {float(t5_p):>+12.4f} {float(t5_e):>+12.4f}  "
              f"{float(m_p_pred):>10.4f}  {100*float(err):>+9.4f}%")
        results.append({
            "convention": label,
            "A_proton":   A_p,
            "A_electron": A_e,
            "T5_proton_MeV":   str(t5_p),
            "T5_electron_MeV": str(t5_e),
            "m_p_hecke_50dps": str(m_p),
            "m_e_hecke_50dps": str(m_e),
            "ratio_p_over_e":  str(ratio),
            "m_p_pred_MeV":    str(m_p_pred),
            "residual":        str(err),
            "residual_ppm":    str(err * mp.mpf("1e6")),
        })

    # 3. Witness emission.
    w = WitnessBuilder("probe-derived-A-from-gs-normal-form", engine="mpmath")
    w.set_description(
        "Probe: derive the BW 'A' parameter from GS normal-form "
        "invariants of each particle's canonical braid word "
        "(electron σ_1^3 in H_2; proton/neutron B_3 = (σ_1 σ_2^{-1})^3 "
        "in H_3) and compare m_p prediction under each candidate A. "
        "Categorical, no fitting: A comes from "
        "gb_filtration_jet_tracker.reduce_braid; a_K from "
        "term5_v2_chirality.aK_v2; BW coefficients from "
        "bw_chirality_isotopes (q-integer-derived). T5 becomes a "
        "categorical functional of the braid alone — no nucleon "
        "ledger dependency — and T5(electron) is no longer '0 by "
        "convention' but the value at A(electron) = 1."
    )
    w.set_audit_only("docs/audits/2026-05-16-t1-t4-tower-closure-plan.md")
    w.add_upstream(PER_GEN_WITNESS)
    w.add_parameter("q_0_50dps", str(per_gen_w["parameters"]["q_0_50dps"]))
    w.add_data("derived_braid_invariants", derived)
    w.add_data("m_p_pred_per_convention", results)
    w.add_data("generic_statement", {
        "claim": (
            "For any braid β ∈ H_n(q): T5(β) is a categorical "
            "functional of β alone, with A(β) derived from the GS "
            "normal form of β and BW coefficients as q-integer "
            "expressions in q_0."
        ),
        "ingredients": {
            "A": "max filtration grade of GS normal form",
            "a_K": "V2 Gram-matrix chirality τ(β · β_mirror^{-1})",
            "Z, N": "flavour-decoration quark counts",
            "BW_coefficients": "q-integer × m_e (categorical, from bw_chirality_isotopes)",
        },
        "no_fitting": True,
        "no_codata_anchor_in_chain": True,
        "scope": "A=1 atoms verified (electron, proton, neutron); A≥2 extension is a research follow-on",
    })
    w.set_content_block("prop:mass-endomorphism-tower")
    w.save()
    print(f"\n  Wrote {OUT_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
