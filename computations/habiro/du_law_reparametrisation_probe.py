#!/usr/bin/env python3
"""Is the fresh Habiro D(u) an IRREGULAR break, or a reparametrisation?

Bean `qou-iayk` blocks the Habiro regeneration on this argument:

    "the EXPONENTS are off by +6, +5, 0, -1. An irregular offset is NOT
     explainable by a normalisation, and one atom (3He) matches exactly
     while its A=3 partner (T) is off by 5."

This probe tests "irregular" against the data. It does NOT argue that the
fresh values are correct -- see VERDICT.

DATA PROVENANCE
---------------
old : `denom_factored` in the committed
      computations/habiro-coefficients-extended.witness.json
new : re-run of computations/habiro/habiro_coefficients_extended.py on
      2026-08-23, post the PR #5376 LaurentQ parser fix. 4/4 clean. The
      re-run's witness was NOT committed; only the factorisations are
      transcribed here, and each is re-derivable by re-running the producer.

    atom   Z N A   old                       new
    D      1 1 2   32*u^40*(u^2+1)^5         192*u^46*(u^4+1)^5
    T      1 2 3   128*u^61*(u^2+1)^8        768*u^66*(u^4+1)^8
    3He    2 1 3   128*u^58*(u^2+1)^8        768*u^58*(u^4+1)^8
    4He    2 2 4   512*u^79*(u^2+1)^11       3072*u^78*(u^4+1)^11

All quantities are INTEGERS. Everything below is exact integer / Fraction
arithmetic -- there is no floating point in this file, by construction.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
_T0 = time.time()
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))

# name, Z, N, A, old_pref, old_uexp, old_base, old_k, new_pref, new_uexp, new_base, new_k
ROWS = [
    ("D",   1, 1, 2,   32, 40, 2,  5,   192, 46, 4,  5),
    ("T",   1, 2, 3,  128, 61, 2,  8,   768, 66, 4,  8),
    ("3He", 2, 1, 3,  128, 58, 2,  8,   768, 58, 4,  8),
    ("4He", 2, 2, 4,  512, 79, 2, 11,  3072, 78, 4, 11),
]


def facts() -> dict:
    """The three structural tests. Exact integer arithmetic throughout."""
    # FACT 1 -- the (1+u^b)^k exponent is 3A-1 in BOTH frames. Zero free
    # parameters across four atoms; only the BASE moves u^2 -> u^4, which is
    # the signature of the substitution u -> u^2 in that factor.
    k_old_ok = all(ok == 3 * A - 1 for _, _, _, A, _, _, _, ok, _, _, _, _ in ROWS)
    k_new_ok = all(nk == 3 * A - 1 for _, _, _, A, _, _, _, _, _, _, _, nk in ROWS)
    base_moved = all(ob == 2 and nb == 4 for *_, ob, _, _, _, nb, _ in
                     [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11])
                      for r in ROWS])

    # FACT 2 -- prefactor: old is exactly 2^(2A+1); new/old is a CONSTANT.
    pref_old_ok = all(op == 2 ** (2 * A + 1) for _, _, _, A, op, *_ in ROWS)
    ratios = {r[0]: Fraction(r[8], r[4]) for r in ROWS}
    pref_ratio_const = len(set(ratios.values())) == 1

    # FACT 3 -- the offset is ADDITIVE in Z and N: the 2x2 interaction
    # vanishes. This is the ONLY constraint a 3-parameter additive model
    # tests against 4 points, and it is the honest weight of this fact.
    e = {(r[1], r[2]): r[9] for r in ROWS}
    interaction = e[(2, 2)] - e[(2, 1)] - e[(1, 2)] + e[(1, 1)]

    # the additive closed form implied, stated only if the interaction vanishes
    closed_form = None
    if interaction == 0:
        dN = e[(1, 2)] - e[(1, 1)]
        dZ = e[(2, 1)] - e[(1, 1)]
        c = e[(1, 1)] - dZ - dN
        closed_form = {"coef_Z": dZ, "coef_N": dN, "const": c}
        assert all(dZ * r[1] + dN * r[2] + c == r[9] for r in ROWS)

    return {
        "fact1_k_unchanged_eq_3A_minus_1": bool(k_old_ok and k_new_ok),
        "fact1_base_u2_to_u4": bool(base_moved),
        "fact1_free_parameters": 0,
        "fact2_old_prefactor_is_2_pow_2A_plus_1": bool(pref_old_ok),
        "fact2_prefactor_ratio_constant": bool(pref_ratio_const),
        "fact2_prefactor_ratio": str(next(iter(ratios.values()))),
        "fact2_free_parameters": 1,
        "fact3_interaction": interaction,
        "fact3_additive": interaction == 0,
        "fact3_closed_form": closed_form,
        "fact3_constraints_tested": 1,
        "fact3_free_parameters": 3,
    }


def main(argv: list[str] | None = None) -> int:
    f = facts()
    print("D(u) reparametrisation probe -- bean qou-iayk")
    print()
    print("FACT 1  (1+u^b)^k exponent k = 3A-1 in BOTH frames, base u^2 -> u^4")
    print(f"        k unchanged : {f['fact1_k_unchanged_eq_3A_minus_1']}   "
          f"base moved: {f['fact1_base_u2_to_u4']}   free params: 0")
    print("FACT 2  prefactor")
    print(f"        old = 2^(2A+1) : {f['fact2_old_prefactor_is_2_pow_2A_plus_1']}   "
          f"new/old constant: {f['fact2_prefactor_ratio_constant']} = {f['fact2_prefactor_ratio']}")
    print("FACT 3  exponent offset is ADDITIVE in Z,N (2x2 interaction)")
    print(f"        interaction = {f['fact3_interaction']}   additive: {f['fact3_additive']}")
    if f["fact3_closed_form"]:
        cf = f["fact3_closed_form"]
        print(f"        implied     : u^({cf['coef_Z']}Z + {cf['coef_N']}N + {cf['const']})")
    print()
    print("        WEIGHT: fact 3 is 4 points against a 3-parameter additive")
    print("        model, so it tests exactly ONE constraint. Weak alone.")
    print("        Facts 1 and 2 are not fits (0 and 1 free parameters).")

    all_pass = (f["fact1_k_unchanged_eq_3A_minus_1"] and f["fact1_base_u2_to_u4"]
                and f["fact2_prefactor_ratio_constant"] and f["fact3_additive"])
    print()
    print(f"VERDICT: 'irregular' is REFUTED: {all_pass}")
    print("         This removes the bean's stated reason to block. It does NOT")
    print("         establish that the fresh values are correct -- reading (a),")
    print("         a producer defect beyond the parser, remains live and")
    print("         untested here.")

    if argv and "--self-test" in argv:
        # the probe must be able to FAIL: perturb one exponent and re-check
        import copy
        saved = copy.deepcopy(ROWS)
        try:
            ROWS[3] = ("4He", 2, 2, 4, 512, 79, 2, 11, 3072, 77, 4, 11)  # 78 -> 77
            broken = facts()
            fires = not broken["fact3_additive"]
        finally:
            ROWS[:] = saved
        holds = facts()["fact3_additive"]
        print()
        print(f"  self-test: additivity FAILS on a perturbed exponent : {fires}  (expect True)")
        print(f"  self-test: additivity HOLDS on the real data        : {holds}  (expect True)")
        print("  no witness written")
        return 0 if (fires and holds) else 1

    from qou_substrate.witness import WitnessBuilder  # noqa: E402

    payload = {
        "computation": "du-law-reparametrisation",
        "description": (
            "Bean qou-iayk. Tests the bean's blocking claim that the fresh "
            "Habiro D(u) exponents are IRREGULAR, against the recorded "
            "factorisations. Exact integer arithmetic; no floating point."),
        "scope": (
            "scope-(a) MEASUREMENT. Refutes 'irregular'. Does NOT establish "
            "that the fresh values are correct: reading (a) of the bean, a "
            "producer defect beyond the PR #5376 parser fix, is untested here "
            "and remains live. Wires nothing; regenerates no witness."),
        "assertions": [
            {"name": "1_k_exponent_unchanged",
             "passed": f["fact1_k_unchanged_eq_3A_minus_1"],
             "detail": ("(1+u^b)^k carries k = 3A-1 in BOTH frames on all four "
                        "atoms; only the base moves u^2 -> u^4. Zero free "
                        "parameters, so this is not a fit.")},
            {"name": "2_prefactor_ratio_constant",
             "passed": f["fact2_prefactor_ratio_constant"],
             "detail": (f"new/old prefactor is the constant "
                        f"{f['fact2_prefactor_ratio']} on all four atoms; old "
                        "is exactly 2^(2A+1). One free parameter, four ratios.")},
            {"name": "3_exponent_offset_additive",
             "passed": f["fact3_additive"],
             "detail": (f"2x2 interaction = {f['fact3_interaction']}, so the "
                        "offset is additive in Z and N -- the same functional "
                        "shape as the landed law. WEIGHT: 4 points against a "
                        "3-parameter additive model tests exactly ONE "
                        "constraint. Weak alone; corroborative here.")},
        ],
        "allPassed": bool(all_pass),
        "result": f,
        "context": {
            "beans": ["qou-iayk", "qou-3zby", "qou-kcii"],
            "refutes": ("qou-iayk: 'An irregular offset is NOT explainable by a "
                        "normalisation, and one atom (3He) matches exactly while "
                        "its A=3 partner (T) is off by 5.'"),
            "note": ("The producer d_u_closed_form_proof.py states in its own "
                     "docstring that this law is NOT a test of witness "
                     "correctness: the committed witness satisfies the law "
                     "exactly and still FAILS the outer identity on all four "
                     "atoms. So 'the old data fits the law 4-for-4' is not "
                     "evidence the old values are right."),
        },
    }
    b = WitnessBuilder.wrap_legacy(
        "du-law-reparametrisation", payload, script_path=__file__,
        engine="python-exact-integer", engine_version=sys.version.split()[0],
        output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\nwitness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
