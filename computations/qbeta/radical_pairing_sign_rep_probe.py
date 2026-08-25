#!/usr/bin/env python3
"""radical_pairing_sign_rep_probe.py — the Gram radical pairs with a braid to
give its SIGN-REPRESENTATION value, so `G x = nf` is unsatisfiable for EVERY
braid, not just the two the SDP probe happens to use.

Bean `qou-cds2`. This closes the question left open by
`gram_mp_path_convention_d_migration_probe`: that probe measured a 47 %
radical component in both anchors of `qbeta_braid_nf_sdp_offset_probe` and
concluded its premise ("G is invertible (rank 6)") is false under convention
D. What it could not say was WHY, or whether another knot would do better.

WHAT THIS ESTABLISHES

    <v, nf(beta)>  =  (-1/q) ^ writhe(beta)        exact

where `v` is the Gram radical (the q-antisymmetriser, `radical_mp`) and
`nf(beta)` is the braid's normal form in `H_3(q)`. Measured over thirteen
braid words spanning writhe -3..+3, agreement to 1.3e-51 at 50 dps.

`-1/q` is the ANTISYMMETRIC eigenvalue of the Hecke relation
`(sigma - q)(sigma + 1/q) = 0`, and the q-antisymmetriser is its projector. So
the pairing is the value of beta in the one-dimensional SIGN REPRESENTATION,
and the identity is what the radical *is* — not an artefact of the NF basis.

THE CONSEQUENCE. `G` is symmetric with kernel spanned by `v`, so its range is
exactly `v`-perp and `G x = nf` is solvable iff `<v, nf> = 0`. A zpow of a
nonzero base is never zero, so `<v, nf>` never vanishes:

    G x = nf is UNSATISFIABLE FOR EVERY BRAID.

Not a bad choice of anchor, and not fixable by choosing another knot. Lean,
sorry-free, generic `Field`: `QOU.QBeta.signRepValue_append` (multiplicative
over concatenation, from `writhe_append`), `signRepValue_inv` (mirror inverts
it, from `writhe_inv`), `signRepValue_ne_zero` (the exclusion), and
`radical_pairing_ne_zero_of_sign_rep` (the consequence, stated against the
measured identity as a hypothesis).

WHERE THE MISSING COMPONENT BELONGS. It is graded by WRITHE — precisely what
the Ocneanu trace does not see. Link invariance is restored by a
writhe-dependent prefactor OUTSIDE the trace (Jones 1987 Sec. 5, block
`prop:jones-markov-trace-stabilisation`), and under D the pin additionally
forces the antisymmetriser weight `y_(1^3)` to vanish
(`TemperleyLiebTower.conventionD_kills_antisymmetriser`), so the trace is
blind to that channel by construction. The SDP probe was asking the trace to
reproduce content that structurally lives outside it. This is the same writhe
thread as the ladder-phase result in
`qbeta_ladder_phase_mirror_covariance_probe`, reached from the other end.

WHAT THIS DOES NOT DO. It does not re-pose the SDP on the quotient, and it
does not report an offset angle — doing so would answer a question that has no
solution in the form asked. It identifies what must be quotiented and proves
the obstruction is universal. Re-deriving the demand on `H_3(q)/rad` is
separate work. No value is wired, no registry tier moves, D stays canonical.

Anchor: proton (default). All arithmetic in mpmath from the 50-dps q_0 string.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke import gram as g  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

DPS = 50

#: (label, braid word as signed 1-indexed generators). Spans writhe -3..+3,
#: includes both anchors, a pure-positive tower, a pure-negative one, and a
#: commutator (writhe 0 but not the identity word).
WORDS = [
    ("identity",            []),
    ("(s1 s2^-1)^2 [4_1]",  [1, -2, 1, -2]),
    ("(s1 s2^-1)^3 [B_3]",  [1, -2, 1, -2, 1, -2]),
    ("s1",                  [1]),
    ("s1^2",                [1, 1]),
    ("s1^3",                [1, 1, 1]),
    ("s1^-1",               [-1]),
    ("s2^-3",               [-2, -2, -2]),
    ("s1 s2",               [1, 2]),
    ("s1 s2 s1",            [1, 2, 1]),
    ("s1^2 s2^-1",          [1, 1, -2]),
    ("s1^-1 s2^-1",         [-1, -2]),
    ("[s1,s2^-1] comm",     [1, -2, -1, 2]),
]


def _word_nf(word):
    """Normal form of a braid word; sigma^-1 = sigma - h*I from the Hecke relation."""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for s in word:
        gen = abs(s) - 1
        nf = g.hm_mp(nf, 1, 0, gen) if s > 0 else g.hm_mp(nf, 1, -g.h_mp(), gen)
    return nf


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    v = mp.matrix(g.radical_mp(DPS))

    print("=" * 78)
    print(" <v, nf(beta)> = (-1/q)^writhe(beta)  —  the radical pairing IS the sign rep")
    print("=" * 78)
    print(f"\n  {'braid word':<22}{'writhe':>7}{'<v,nf>':>21}{'(-1/q)^w':>21}{'|diff|':>11}")
    print("  " + "-" * 82)

    rows, worst = [], mp.mpf(0)
    with mp.workdps(DPS):
        for name, w in WORDS:
            nfm = mp.matrix(_word_nf(w))
            pair = mp.fsum(v[i] * nfm[i] for i in range(6))
            writhe = sum(1 if s > 0 else -1 for s in w)
            pred = (-1 / q) ** writhe
            d = abs(pair - pred)
            worst = max(worst, d)
            rows.append({"word": name, "writhe": writhe,
                         "radical_pairing": fmt(pair), "sign_rep_value": fmt(pred),
                         "abs_diff": fmt(d)})
            print(f"  {name:<22}{writhe:>7}{mp.nstr(pair, 15):>21}"
                  f"{mp.nstr(pred, 15):>21}{mp.nstr(d, 5):>11}")

        min_abs = min(abs(mp.mpf(r["radical_pairing"])) for r in rows)

    print(f"\n  worst |<v,nf> - (-1/q)^writhe| = {mp.nstr(worst, 6)}")
    print(f"  min |<v,nf>| over all words   = {mp.nstr(min_abs, 6)}   (never 0)")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  `-1/q` is the ANTISYMMETRIC eigenvalue of (sigma - q)(sigma + 1/q) = 0 and
  the q-antisymmetriser is its projector, so this identity says the radical
  pairing is beta's value in the one-dimensional SIGN REPRESENTATION. It is
  what the radical is, not a feature of the NF basis.

  G is symmetric with kernel spanned by v, so G x = nf is solvable iff
  <v,nf> = 0 — and a zpow of a nonzero base never vanishes. So G x = nf is
  UNSATISFIABLE FOR EVERY BRAID. The SDP probe's obstruction is universal;
  no other knot escapes it.

  The unreachable piece is graded by WRITHE, which is exactly what the
  Ocneanu trace does not see: invariance needs a writhe prefactor OUTSIDE the
  trace, and under D the pin kills the antisymmetriser weight outright. The
  probe was asking the trace for content that lives outside it.

  NOT done here: re-posing the SDP on H_3(q)/rad. Reporting an offset angle
  for a demand with no solution would be answering a different question.
""")

    wb = WitnessBuilder("radical-pairing-sign-rep", engine="mpmath")
    wb.set_description(
        "The convention-D Gram radical (the q-antisymmetriser) pairs with any "
        "braid's H_3(q) normal form to give exactly that braid's value in the "
        "one-dimensional SIGN representation: <v, nf(beta)> = (-1/q)^writhe"
        "(beta), measured over 13 braid words spanning writhe -3..+3, exact to "
        "1.3e-51 at 50 dps. `-1/q` is the antisymmetric eigenvalue of the Hecke "
        "relation and the q-antisymmetriser is its projector, so this is what "
        "the radical IS rather than a basis artefact. CONSEQUENCE: G is "
        "symmetric with kernel spanned by v, so G x = nf is solvable iff "
        "<v,nf> = 0, and a zpow of a nonzero base never vanishes — therefore "
        "G x = nf is UNSATISFIABLE FOR EVERY BRAID, not merely for the two "
        "anchors of qbeta_braid_nf_sdp_offset_probe whose premise ('G is "
        "invertible (rank 6)') this refutes. No other knot escapes it. Lean, "
        "sorry-free, generic Field: signRepValue_append (multiplicative, from "
        "writhe_append), signRepValue_inv (mirror inverts it, from writhe_inv, "
        "and needs no q != 0), signRepValue_ne_zero, and "
        "radical_pairing_ne_zero_of_sign_rep. The unreachable component is "
        "graded by WRITHE — precisely what the Ocneanu trace does not see "
        "(invariance needs a writhe prefactor outside the trace, Jones 1987 "
        "Sec. 5) and what convention D's pin kills outright "
        "(conventionD_kills_antisymmetriser). SCOPE: does NOT re-pose the SDP "
        "on the quotient and reports no offset angle; that would answer a "
        "question with no solution in the form asked. No value wired, no tier "
        "moved, D stays canonical."
    )
    wb.add_data("identity", "<v, nf(beta)> = (-1/q)^writhe(beta)")
    wb.add_data("radical", "q-antisymmetriser v_i = (-1/q)^len(w_i)")
    wb.add_data("rows", rows)
    wb.add_data("worst_abs_diff", fmt(worst))
    wb.add_data("min_abs_pairing", fmt(min_abs))
    wb.add_data("lean_declarations", [
        "QOU.QBeta.signRepValue_append",
        "QOU.QBeta.signRepValue_inv",
        "QOU.QBeta.signRepValue_ne_zero",
        "QOU.QBeta.radical_pairing_ne_zero_of_sign_rep",
    ])
    wb.add_data("reposes_sdp_on_quotient", False)
    wb.add_data("closes_cds2", False)

    wb.add_assertion(
        name="radical_pairing_equals_sign_rep_value_on_every_word",
        computed=str(int(worst < mp.mpf(10) ** -45)), expected="1", tolerance=0,
        source=f"max over 13 braid words (writhe -3..+3) of "
               f"|<v,nf> - (-1/q)^writhe| = {mp.nstr(worst, 6)} at 50 dps. The "
               "words include both SDP anchors, a pure-positive tower, a "
               "pure-negative one, and a writhe-0 commutator that is not the "
               "identity word — so the match is not an artefact of vanishing "
               "writhe.",
    )
    wb.add_assertion(
        name="pairing_never_vanishes_so_Gx_eq_nf_is_unsatisfiable_for_every_braid",
        computed=str(int(min_abs > mp.mpf("0.1"))), expected="1", tolerance=0,
        source=f"min |<v,nf>| over the 13 words = {mp.nstr(min_abs, 6)}, and "
               "structurally it is a zpow of -1/q, which is nonzero for q != 0 "
               "at every integer exponent (QOU.QBeta.signRepValue_ne_zero). "
               "Since G is symmetric with kernel span(v), its range is v-perp, "
               "so G x = nf is solvable iff the pairing vanishes — it never "
               "does. The obstruction is universal, not anchor-specific.",
    )
    wb.add_assertion(
        name="writhe_grading_is_what_makes_it_a_framing_quantity",
        computed=str(int(all(
            abs(mp.mpf(r["radical_pairing"]) - (-1 / q) ** r["writhe"])
            < mp.mpf(10) ** -45 for r in rows)
            and len({r["writhe"] for r in rows}) >= 5)), expected="1", tolerance=0,
        source="the pairing depends on the braid word ONLY through its writhe "
               f"({len({r['writhe'] for r in rows})} distinct writhes among the 13 "
               "words; e.g. `s1 s2` and `s1^2` both have writhe 2 and pair "
               "identically). Writhe is exactly the grading the Ocneanu trace "
               "does not carry — invariance needs a writhe prefactor outside "
               "the trace — so the unreachable component is a framing quantity, "
               "which is why no re-solve inside the trace can recover it.",
    )
    out = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
