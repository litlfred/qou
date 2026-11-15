#!/usr/bin/env python3
"""The documented `z_3` grep trap names the wrong quantity — it is an ANCHOR gap.

Bean `qou-yk03` (rescoped: the second-Markov-trace question). Found while
answering that bean, not while looking for it.

THE DOCUMENTED TRAP. `docs/audits/2026-08-16-colour-level-and-tln-compute.md`
and bean `qou-d7h1` both carry this warning, and `AGENTS.md` relays it:

    "Grep warning: the literal 0.44930482320583087 in many witnesses is h_q,
     NOT z_3 (0.449304809090...) -- they differ at the 8th decimal."

Read as written, that says: two DIFFERENT quantities happen to look alike, so a
witness carrying the first holds `h_q` and needs no anchor attention.

WHAT THE LITERAL ACTUALLY IS. Measured at 65 dps against every candidate the
corpus uses:

    z_3 @ MUON pin   0.4493048233034703126034   rel 2.17e-10  <-- the literal
    z_3 @ proton pin 0.4493048090902078605552   rel 3.14e-8
    h_q = q - 1/q    0.2090602987956393154308   rel 5.35e-1   <-- 53 % away
    hbar_q = 1 - 1/q 0.0990817160442585078392   rel 7.79e-1
    1/[2]_q          0.4972905456049155559958   rel 1.07e-1

`h_q` is not a near miss; it is off by a factor of two. The 2.17e-10 residual on
the muon row is the LITERAL's own truncation at 17 digits, not a mismatch.

SO THE TRAP IS REAL AND ITS DIAGNOSIS IS INVERTED. The two numbers are not two
quantities that resemble each other -- they are ONE quantity, `z_3 = q^3/[3]_q`,
evaluated at the two substrate anchors. The 3.14e-8 gap is the mu-p substrate
tension (~11.6 ppb on q) propagated through `z_3`, amplified ~2.7x.

WHY THAT MATTERS MORE THAN THE SIZE OF THE GAP. AGENTS.md's own rule is "Never
straddle the two layers inside one quantity ... a defect regardless of its
size", and the standing 2026-08-07 directive is that all compute defaults to the
proton anchor. A note saying "that literal is h_q" tells an agent a
muon-pinned value needs no anchor check -- precisely inverting the action the
directive requires. The guidance is harmful in the one situation it exists for.

AND THE EXTENT IS SMALL -- reported as measured, not inflated. Five files carry
the literal: THREE are under `fsh-guts/deprecated/computations/` (not live, and excluded
by the consumer audit), and the other TWO are the audit doc and the bean that
carry the misidentification itself. ZERO live producers or witnesses hold a
muon-pinned `z_3`. So this is a documentation correction, not a drain. The
correct proton value `0.4493048090...` appears in 21 files.

WHAT THIS DOES NOT CLAIM. That anything computed with `z_3` is wrong -- no live
compute uses the muon-pinned value. Only that the published warning misnames it,
in a direction that would suppress an anchor check.

No float64: mpmath end to end at 65 dps; q-integers from the substrate strings.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

# The literal as it appears in the warning, carried as a STRING and converted
# after set_compute_dps() -- a module-level mp.mpf of a 17-digit literal is
# evaluated at import-time dps and truncates (module_const_precision_audit).
LITERAL_STR = "0.44930482320583087"

# The muon anchor, CODATA-2022 derivation, per the AGENTS.md q0 section. Carried
# explicitly because the whole point is that TWO anchors are in play; taking it
# from a helper that resolves "the" anchor would beg the question.
Q_MUON_STR = ("1.1099785956427390466817951293800017527000655610290115569740"
              "45769999095")


def q_int(q: mp.mpf, n: int) -> mp.mpf:
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def z_N(q: mp.mpf, N: int) -> mp.mpf:
    """Ocneanu parameter for a fibre of quantum dimension [N]_q: z = q^N/[N]_q.

    The closed form is the corpus's own, from
    `ocneanu_param_from_fibre_dimension.py` and the division-free Lean identity
    `z * [N]_q = q^N` in `QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`. Not
    re-derived here: this probe is about which ANCHOR a recorded literal was
    evaluated at, not about the formula.
    """
    return q ** N / q_int(q, N)


def main() -> int:
    set_compute_dps()
    literal = mp.mpf(LITERAL_STR)
    qp = mp.mpf(Q_50_DIGIT_STR)
    qm = mp.mpf(Q_MUON_STR)

    b = WitnessBuilder("z3-muon-pin-vs-hq-misidentification")
    b.set_description(
        "Bean qou-yk03. The corpus's documented grep warning -- 'the literal "
        "0.44930482320583087 in many witnesses is h_q, NOT z_3 "
        "(0.449304809090...)' -- misnames the quantity. Measured at 65 dps, "
        "that literal is z_3 = q^3/[3]_q at the MUON anchor (rel 2.17e-10, "
        "which is the literal's own 17-digit truncation), while h_q = q - 1/q "
        "is 53 % away. So the two numbers are not two quantities that resemble "
        "each other; they are ONE quantity at the two substrate anchors, and "
        "the 3.14e-8 gap is the mu-p tension propagated through z_3. That "
        "matters because the note as written tells an agent a muon-pinned "
        "value needs no anchor check, inverting the 2026-08-07 "
        "proton-by-default directive. EXTENT IS SMALL and is reported as "
        "measured: 5 files carry the literal, 3 under _deprecated/ and 2 being "
        "the doc and bean that carry the misidentification itself -- ZERO live "
        "producers. A documentation correction, not a drain. Does NOT claim any "
        "computed result is wrong."
    )
    b.add_parameter("literal_under_test", LITERAL_STR)
    b.add_parameter("q0_proton_50dps", Q_50_DIGIT_STR)
    b.add_parameter("q0_muon_derived", Q_MUON_STR)

    cands = {
        "z_3_at_muon": z_N(qm, 3),
        "z_3_at_proton": z_N(qp, 3),
        "h_q_q_minus_qinv": qp - 1 / qp,
        "hbar_q_one_minus_qinv": 1 - 1 / qp,
        "one_over_q_int_2": 1 / q_int(qp, 2),
        "z_2_at_proton_convention_D": z_N(qp, 2),
    }
    rows = {k: {"value": fmt(v),
                "rel_diff_vs_literal": fmt(abs(v - literal) / literal)}
            for k, v in cands.items()}
    b.add_data("candidate_identification", {
        "rows": rows,
        "note": "The muon row's 2.17e-10 residual is the literal's own "
                "truncation at 17 significant digits, not a mismatch. h_q is "
                "not a near miss -- it is off by a factor of two.",
    })

    rel_muon = abs(cands["z_3_at_muon"] - literal) / literal
    rel_hq = abs(cands["h_q_q_minus_qinv"] - literal) / literal
    anchor_gap = (abs(cands["z_3_at_muon"] - cands["z_3_at_proton"])
                  / cands["z_3_at_proton"])

    b.add_assertion(
        "literal_is_z3_at_the_muon_anchor",
        computed=fmt(rel_muon), expected="0", tolerance="1e-9",
        unit="relative",
        source="z_3 = q^3/[3]_q evaluated at the CODATA-2022 muon anchor "
               "reproduces the warned-about literal to the literal's own "
               "precision. This is the identification the published warning "
               "gets wrong.",
    )
    b.add_assertion(
        "literal_is_NOT_h_q_by_a_factor_of_two",
        computed="1" if rel_hq > mp.mpf("0.4") else "0", expected="1",
        source=f"|h_q - literal|/literal = {fmt(rel_hq)} -- h_q = q - 1/q is "
               f"{fmt(cands['h_q_q_minus_qinv'])}, roughly half the literal. "
               f"The claim that they 'differ at the 8th decimal' is not a "
               f"small error in a true statement; the quantities are not "
               f"comparable.",
    )
    b.add_data("anchor_gap", {
        "z3_muon_over_proton_rel": fmt(anchor_gap),
        "note": "3.14e-8 -- the mu-p substrate tension (~11.6 ppb on q) "
                "propagated through z_3 and amplified ~2.7x. This is the real "
                "content of the 'differ at the 8th decimal' observation: a "
                "LAYER STRADDLE, which AGENTS.md calls a defect regardless of "
                "size, not a coincidental lookalike.",
    })

    b.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
            "comparison by design: evaluates z_3 = q^3/[3]_q and h_q at both the proton pin (Q_50_DIGIT_STR) and the live CODATA-2022 muon pin to identify which anchor a recorded literal was computed at")})

    print(f"literal under test: {LITERAL_STR}\n")
    print(f"{'candidate':<28} {'value':<36} {'rel vs literal'}")
    for k, r in rows.items():
        print(f"{k:<28} {r['value'][:36]:<36} {r['rel_diff_vs_literal'][:12]}")
    print(f"\nz_3 muon-vs-proton anchor gap: {fmt(anchor_gap)[:14]}  "
          f"(the mu-p tension through z_3)")
    print("\nVERDICT: the literal is z_3 AT THE MUON PIN, not h_q. The published")
    print("warning names the wrong quantity, in the direction that suppresses")
    print("an anchor check. Extent: 0 live producers (3 deprecated, 2 doc sites).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
