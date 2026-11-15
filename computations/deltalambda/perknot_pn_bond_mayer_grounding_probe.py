#!/usr/bin/env python3
"""Categorical grounding of the per-knot p!=n inverse-product bond weight
(bean qou-r1sr — verification step of the T/3He-split LEAD, PR #3841).

The LEAD (perknot_pn_bond_resolved_extensivity_probe.py): the parameter-free
inverse-product per-bond weight w(a,b) = 1/(tr_M(a)*tr_M(b)) on the p!=n-distinct
Markov traces reproduces the T/3He extensivity-multiplier split
mu_ext(T)/mu_ext(3He) to a few percent (-1.38% against the stale targets
4.444/3.292; -2.61% against the live 6.706/4.905, 2026-10-13), a split every
symmetric/equal-weight bond model gives as exactly 1.000.

**2026-11-15: that "few percent" was an artefact of RETIRED traces.** Both
figures above used typed convention-C nucleon traces (bean qou-am5t). On the
canonical traces (borromean word, convention D, proton pin; read below from
atomic-tr-m-mpfr-50dps-proton.witness.json) the split is
(tr_p/tr_n)^2 = 1.7544 against the target 1.3671: **+28.3 %, and the 5 % gate
FAILS.** Scope-(a) negative: this construction alone, on canonical traces,
does not reproduce the T/3He split. The structural reduction (point 1) and
the sign (point 3) are unaffected; only the magnitude claim falls.

This probe answers the open "why inverse?" question three ways, honestly:

1. STRUCTURAL REDUCTION.  T=(p,n,n) has bonds {pn,pn,nn}; 3He=(p,p,n) has
   {pp,pn,pn}.  The ONLY difference is one pp<->nn swap (both carry 2 pn).
   Under the product aggregate the split ratio reduces cleanly to
   w(nn)/w(pp) = (tr_p/tr_n)^2 — no tuning; the exponent 2 is the two
   endpoints of a same-type bond.

2. CATEGORICAL HOME.  1/(tr_M(a)*tr_M(b)) is the ideal-gas / Mayer
   normalization of a two-point (pair) correlation: in the Mayer-Ursell
   cluster expansion B/m_e = Sum_k b_k that main already uses
   (docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md),
   the normalized pair correlation is g2(a,b) = tr(ab)/(tr(a)tr(b)) - 1;
   the 1/(Z_a Z_b) factor is its ideal-gas normalization, with tr_M a
   Plancherel-weighted partition sum Sum_lambda y_lambda chi_lambda.
   So the inverse-product weight is the b2-level (pairwise) Ursell
   normalization, NOT a free ansatz.

3. PHYSICS DIRECTION.  tr_n < tr_p => w(nn) > w(pp) => nn binds more than pp
   => 3He (two protons) LESS bound than T (two neutrons).  This is the
   correct sign of the real Coulomb/isospin asymmetry (AME: B(T)=8.482 >
   B(3He)=7.718 MeV).

HONEST BOUNDS (keeps this a scope-(a) grounded LEAD, not a closure):
- b2/pairwise object.  Main's Ursell frame identifies the pairwise b2 content
  as the SATURATED ceiling; the OPEN magnitude gap is the CONNECTED b4.  This
  grounds the p!=n isospin discriminator but is ORTHOGONAL to the extensivity
  magnitude closure (it does not reproduce the full non-monotone mu_ext; 4He
  is not the maximum).
- true exponent is not 2: 1.112 on the canonical traces (it read 2.184 on
  the retired convention-C traces at the live mu targets, and 2.097 against
  the stale targets). Never fit it (Ursell-doc anti-numerology guardrail,
  Rule-14 hidden DOF).

EXPLORATORY; production_wired: false; no fit, no BW, scope-(a).
"""
import json
import os
import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION

set_compute_dps()

# Per-knot nucleon Markov traces, READ from their owning witness
# (atomic-tr-m-mpfr-50dps-proton.witness.json): borromean word
# (owner ruling qou-hu1f, 2026-09-05), convention D (ruling 2026-08-15 R1),
# proton pin (2026-08-07 directive / R2). Ownership established in PR #7795.
#
# Until 2026-11-15 these were typed literals 1.0653062380758782... /
# 0.92323330514983772..., commented "current-main-verified". They were not:
# they match the CONVENTION-C nucleon traces recorded in bean qou-am5t
# (1.06530622861316 / 0.92323329718615) to ~9e-9 relative. On those retired
# traces the 5 % gate below PASSED (-2.61 %); on the canonical ones it FAILS
# (+28.3 %). The gate is deliberately NOT widened (anti-fit directive).
_TR_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "atomic-tr-m-mpfr-50dps-proton.witness.json")
with open(_TR_SRC) as _f:
    _TRW = json.load(_f, parse_float=str)
if (_TRW.get("q0Anchor") != "proton"
        or _TRW.get("intra_ordering_frame") != "borromean"):
    raise SystemExit(f"refusing: {_TR_SRC} is not the borromean/proton witness "
                     f"(q0Anchor={_TRW.get('q0Anchor')!r}, "
                     f"intra_ordering_frame={_TRW.get('intra_ordering_frame')!r})")
_TR = {r["atom"]: r["tr_M_at_q0_50dps"] for r in _TRW["results"]}
TR_P = mp.mpf(_TR["proton"])
TR_N = mp.mpf(_TR["neutron"])
TR_SOURCE = {
    "witness": os.path.basename(_TR_SRC),
    "field": "results[atom].tr_M_at_q0_50dps",
    "word": "borromean", "convention": "D", "q0Anchor": "proton",
    "q0Value": _TRW.get("q0Value"),
    "superseded_typed_literals_convention_C": {
        "p": "1.065306238075878215688040411687927620546686279347",
        "n": "0.92323330514983772546573530276491123416377319107628",
        "split_pred_on_them": "1.3315", "rel_err_pct_on_them": "-2.61",
    },
}

# mu_ext targets, READ from their owning witness
# (deltalambda-extensivity-gap-synthesis.witness.json,
# `extensivity_multipliers_target`). Until 2026-10-13 these were typed
# literals 4.444146924325849 / 3.2918285794896933, stale against that witness
# (which carries 6.706071811638838 / 4.905446773035623). Parsed with
# parse_float=str so the witness's decimal text reaches mp.mpf verbatim and
# never passes through a Python float.
_MU_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "deltalambda-extensivity-gap-synthesis.witness.json")
with open(_MU_SRC) as _f:
    _MU = json.load(_f, parse_float=str)["extensivity_multipliers_target"]
MU_T = mp.mpf(_MU["T"])
MU_3HE = mp.mpf(_MU["3He"])

# AME binding energies (MeV) — direction cross-check only
B_T_AME = AME_B_TRITIUM_MEV_VALIDATION
B_3HE_AME = mp.mpf("7.718058")


def w(a, b):
    """inverse-product per-bond weight = Mayer ideal-gas normalization."""
    return 1 / (a * b)


def product_aggregate(bonds):
    v = mp.mpf(1)
    for a, b in bonds:
        v *= w(a, b)
    return v


def main():
    T_bonds = [(TR_P, TR_N), (TR_P, TR_N), (TR_N, TR_N)]
    HE3_bonds = [(TR_P, TR_P), (TR_P, TR_N), (TR_P, TR_N)]

    ratio = product_aggregate(T_bonds) / product_aggregate(HE3_bonds)
    reduction = (TR_P / TR_N) ** 2
    target = MU_T / MU_3HE
    relerr = (ratio - target) / target * 100
    true_exp = mp.log(target) / mp.log(TR_P / TR_N)

    # physics direction
    nn_binds_more = TR_N < TR_P
    ame_dir_ok = B_T_AME > B_3HE_AME  # T more bound than 3He

    reduction_exact = mp.almosteq(ratio, reduction, rel_eps=mp.mpf(10) ** -40)

    print("=== per-knot p!=n bond weight: Mayer grounding ===")
    print("W(T)/W(3He)          =", mp.nstr(ratio, 10))
    print("(tr_p/tr_n)^2        =", mp.nstr(reduction, 10), "(structural reduction, pp<->nn swap)")
    print("reduction exact      =", reduction_exact)
    print("target mu(T)/mu(3He) =", mp.nstr(target, 10))
    print("rel err              =", mp.nstr(relerr, 4), "%")
    print("true exponent s      =", mp.nstr(true_exp, 6), "(model = exactly 2)")
    print("nn binds more (tr_n<tr_p) =", nn_binds_more)
    print("AME dir (B_T>B_3He)  =", ame_dir_ok, "-> 3He less bound (Coulomb) : sign CORRECT")

    assertions = [
        {
            "name": "split_reduces_to_trp_trn_squared",
            "detail": "W(T)/W(3He) == (tr_p/tr_n)^2 (structural, only diff is pp<->nn swap)",
            "passed": bool(reduction_exact),
        },
        {
            "name": "split_matches_target_under_5pct",
            "detail": f"|rel err| = {mp.nstr(abs(relerr), 4)}% (gate: < 5%; pred {mp.nstr(ratio,6)} vs {mp.nstr(target,6)})",
            "passed": bool(abs(relerr) < 5),
        },
        {
            "name": "physics_sign_correct",
            "detail": "tr_n<tr_p => nn binds more => 3He less bound; matches AME B(T)>B(3He)",
            "passed": bool(nn_binds_more and ame_dir_ok),
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    witness = {
        "computation": "perknot-pn-bond-mayer-grounding",
        "description": (
            "Categorical grounding of the inverse-product per-bond weight "
            "w(a,b)=1/(tr_M(a)tr_M(b)) behind the T/3He mu_ext-split LEAD "
            "(bean qou-r1sr, PR #3841). Structural reduction to (tr_p/tr_n)^2, "
            "Mayer/ideal-gas pair-correlation normalization (b2 level of the "
            "Ursell cluster expansion), and correct Coulomb/isospin sign. "
            "EXPLORATORY; scope-(a); no fit."
        ),
        "audit_only": True,
        "engine": "python3/mpmath",
        "engineVersion": "50dps",
        "assertions": assertions,
        "allPassed": all_passed,
        "data": {
            "discipline": "EXPLORATORY",
            "production_wired": False,
            "tr_M": {"p": mp.nstr(TR_P, 40), "n": mp.nstr(TR_N, 40)},
            "tr_M_source": TR_SOURCE,
            "split_pred": mp.nstr(ratio, 40),
            "structural_reduction": "(tr_p/tr_n)^2",
            "structural_reduction_exact": bool(reduction_exact),
            "target_mu_ratio": mp.nstr(target, 40),
            "rel_err_pct": mp.nstr(relerr, 6),
            "true_exponent": mp.nstr(true_exp, 8),
            "model_exponent": 2,
            "categorical_home": (
                "Mayer/ideal-gas normalization 1/(Z_a Z_b) of the pair "
                "correlation g2=tr(ab)/(tr(a)tr(b))-1; tr_M = Plancherel-"
                "weighted partition sum Sum_lambda y_lambda chi_lambda. b2 "
                "(pairwise) level of B/m_e = Sum_k b_k."
            ),
            "physics": (
                "tr_n<tr_p => w(nn)>w(pp) => nn binds more => 3He less bound; "
                "correct Coulomb/isospin sign (AME B(T)=8.482 > B(3He)=7.718)."
            ),
            "honest_bounds": (
                "b2/pairwise object. Main's Ursell frame: pairwise b2 is the "
                "SATURATED ceiling; the OPEN magnitude gap is the CONNECTED b4. "
                "Grounds the p!=n isospin discriminator but is ORTHOGONAL to "
                "the extensivity magnitude closure (does not reproduce full "
                "non-monotone mu_ext; 4He not max)."
            ),
            "anti_numerology_flag": (
                f"true exponent {mp.nstr(true_exp, 4)} (model exactly 2). On the "
                "retired convention-C traces it read 2.184 (live targets) and "
                "2.097 (stale targets). Never fit it "
                "(Ursell-doc guardrail, Rule-14 hidden DOF)."
            ),
            "verdict": (
                "STRUCTURE GROUNDED, MAGNITUDE "
                + ("REPRODUCED" if abs(relerr) < 5 else "NOT REPRODUCED")
                + ": the inverse-product weight is the Mayer b2 "
                "normalization and the T/3He split reduces exactly to "
                "(tr_p/tr_n)^2 with correct Coulomb sign; on the canonical "
                "traces (borromean, D, proton) its magnitude misses the target "
                f"by {mp.nstr(relerr, 4)}%. The earlier -2.61% held only on "
                "retired convention-C traces. Scope-(a) negative for the "
                "magnitude; ORTHOGONAL to the open connected-b4 extensivity "
                "gap. No wiring; gate not widened."
            ),
        },
    }

    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    # Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "perknot-pn-bond-mayer-grounding.witness.json",
    )
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    print("allPassed =", all_passed)


if __name__ == "__main__":
    main()
