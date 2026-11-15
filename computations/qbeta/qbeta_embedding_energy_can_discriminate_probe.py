#!/usr/bin/env python3
"""qou-99qc: the gluon candidates are DISTINCT LINKS — so an isotopy-class
energy (O'Hara / Moebius via the Bring embedding) CAN break the tie that a
letter-sum cannot. A formalize-first green light for the route, before the
bridge is built.

# Ref: computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py  (the tie this prunes)
# Ref: computations/mobius_cross_energy_hopf_calibration.py                   (the integrator, calibrated to 2*pi^2)
# Ref: folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean
# Ref: .beans/qou-99qc--...md

WHY THIS RUNS BEFORE THE BRIDGE. The owner's proposal is to select the gluon
dressing by an EMBEDDING energy (O'Hara / Moebius, via how the word embeds in
the Bring surface) rather than by crossing count or crossing energy. Building
that bridge is a research tranche. The formalize-first discipline says: find the
invariant the whole proposal depends on, and check it first.

THE INVARIANT IT DEPENDS ON. Moebius energy is a property of an EMBEDDING and
is not a knot invariant; what IS an invariant of the isotopy class is the
INFIMUM over that class (Freedman-He-Wang). So a selection rule built on it can
only ever distinguish candidates that are DIFFERENT LINKS. If the tied
candidates close to the SAME link, the bridge is stillborn -- it would return
one number for both, exactly as the letter-sum does, and no amount of
implementation work would change that.

THE TEST, and it needs no embedding. The Markov trace at an admissible `z` is a
link invariant once normalised by writhe (conjugation invariance is automatic
for a trace; stabilisation contributes the `z` factor). `z_D = q^3/(q^2+1)` is
admissible under convention D. So for two words of EQUAL WRITHE, a difference in
`tr_{z_D}` is sufficient to conclude the closures are different links. Note the
direction: distinguishing is SUFFICIENT, not necessary -- convention D
annihilates the `(1,1,1)` block, so this truncated invariant may fail to
separate some genuinely different links. That asymmetry is in the safe
direction for this prune.

RESULT -- GREEN LIGHT. All four two-crossing gluon candidates have writhe `+2`,
so the writhe normalisation is IDENTICAL across them, and all four give
DISTINCT `(tr_p, tr_n)` pairs. The sharpest case is `sigma_1 sigma_0` against
`sigma_0 sigma_1`: same letter multiset, same writhe, differing only in ORDER,
and their traces differ (`6.78e-2` on the proton, `1.42e-2` on the neutron).
**They are different links.** So the candidates the letter-sum ties are
genuinely distinct isotopy classes, and an isotopy-class functional is not
structurally barred from separating them.

WHY THAT MATTERS BEYOND THIS ARC. It also explains WHY `E_cross` fails here
rather than merely recording that it does. `E_cross` is a sum over letters, so
it is constant on the permutation orbit of a letter multiset; the closure is
not. Any functional of the multiset alone is therefore structurally incapable of
selecting among these candidates, for every `q` and every choice of coefficients
-- this is a scope-(b) exclusion of the whole letter-sum CLASS, with the
invariant named: the closure is order-sensitive and a letter-sum is not.

WHAT IS NOT CLAIMED. That the O'Hara/Moebius energy WOULD separate them -- only
that it is not barred from doing so, which is what a prune establishes. That the
bridge is easy: it still needs a canonical embedding (or the minimiser), which
is the open research content. That any candidate should be adopted. No selection
by proximity to a measured value; no Q_beta appears in this probe at all.

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py \
       2>&1 | tee /tmp/qbeta_embedding_discriminate.log
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)
CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
GENS = (0, 0, 1)

#: the two-crossing gluon candidates the letter-sum ties at `2q`.
TWO_CROSSING = {
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
    "sigma_0 sigma_0": [(0, Z), (0, Z)],
}

SEP = mp.mpf("1e-25")
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


def writhe(gluon) -> int:
    """Sum of crossing signs. Only pure crossings occur in the gluon, so
    `d = 0` is `+1` and `d = -h` is `-1`; the bar-fixed letter never appears
    here and would have no crossing sign."""
    out = 0
    for _, d in gluon:
        if d == Z:
            out += 1
        elif d == NEG1:
            out -= 1
        else:
            raise ValueError("no crossing sign for the bar-fixed letter")
    return out


def main() -> int:
    w = WitnessBuilder("qbeta-embedding-energy-can-discriminate")
    w.set_description(
        "A formalize-first prune run BEFORE the Bring->O'Hara bridge is built. "
        "Moebius energy is a property of an embedding, not a knot invariant; "
        "the invariant is the infimum over the isotopy class, so a selection "
        "rule built on it can only separate candidates that are DIFFERENT "
        "LINKS. Tested without any embedding: the Markov trace at the "
        "admissible z_D is a link invariant once normalised by writhe, and all "
        "four two-crossing gluon candidates have writhe +2 -- identical "
        "normalisation -- yet give four DISTINCT (tr_p, tr_n) pairs. The "
        "sharpest case is sigma_1 sigma_0 vs sigma_0 sigma_1: same letter "
        "multiset, same writhe, differing only in ORDER, and the traces "
        "differ. They are different links, so an isotopy-class energy is NOT "
        "structurally barred from breaking the tie -- green light for the "
        "route. It also upgrades the E_cross failure from an observation to a "
        "scope-(b) exclusion of the whole letter-sum CLASS: a sum over letters "
        "is constant on the permutation orbit of a multiset and the closure is "
        "not."
    )

    print("qou-99qc — can an isotopy-class energy discriminate at all?")
    print(f"  q0 = {mp.nstr(Q0, 20)}   z_D = {mp.nstr(ZD, 20)}")
    print()

    # ---- 1. identical writhe, so the normalisation cannot differ ---------
    print("== 1. writhe — is the normalisation common to all candidates? ==")
    wr = {n: writhe(g) for n, g in TWO_CROSSING.items()}
    for n, v in wr.items():
        print(f"    {n:<20s} writhe = {v:+d}")
    check("all_two_crossing_candidates_share_one_writhe",
          len(set(wr.values())) == 1,
          f"every candidate has writhe {wr['sigma_1 sigma_0']:+d}, so ANY "
          f"writhe-based normalisation of the Markov trace is identical across "
          f"them. Without this the trace comparison below would be confounded "
          f"by the normalisation rather than measuring the link", w)
    print()

    # ---- 2. the traces, and whether they separate ------------------------
    print("== 2. Markov trace at z_D, per candidate ==")
    tp = {n: tr(base("p") + g) for n, g in TWO_CROSSING.items()}
    tn = {n: tr(base("n") + g) for n, g in TWO_CROSSING.items()}
    print(f"    {'gluon':<20s} {'tr(w_p)':<26s} {'tr(w_n)'}")
    for n in TWO_CROSSING:
        print(f"    {n:<20s} {mp.nstr(tp[n], 18):<26s} {mp.nstr(tn[n], 18)}")

    pairs = {(mp.nstr(tp[n], 20), mp.nstr(tn[n], 20)) for n in TWO_CROSSING}
    check("the_four_tied_candidates_are_four_distinct_links",
          len(pairs) == len(TWO_CROSSING),
          f"{len(pairs)} distinct (tr_p, tr_n) pairs over "
          f"{len(TWO_CROSSING)} candidates at equal writhe. The Markov trace at "
          f"an admissible z is a link invariant after writhe normalisation "
          f"(conjugation invariance is automatic for a trace; stabilisation "
          f"gives the z factor), so equal writhe plus different trace is "
          f"SUFFICIENT for different closures", w)
    print()

    # ---- 3. the sharp case: order alone ----------------------------------
    print("== 3. the sharp case — same multiset, same writhe, order alone ==")
    a, b = "sigma_1 sigma_0", "sigma_0 sigma_1"
    dp, dn = abs(tp[a] - tp[b]), abs(tn[a] - tn[b])
    print(f"    |tr_p({a}) - tr_p({b})| = {mp.nstr(dp, 12)}")
    print(f"    |tr_n({a}) - tr_n({b})| = {mp.nstr(dn, 12)}")
    check("reordering_ALONE_changes_the_link",
          dp > SEP and dn > SEP,
          f"{a} and {b} have the SAME letter multiset and the SAME writhe and "
          f"differ only in order; their traces differ by {mp.nstr(dp, 6)} "
          f"(proton) and {mp.nstr(dn, 6)} (neutron). The closure is "
          f"order-SENSITIVE", w)

    check("every_letter_sum_functional_is_structurally_barred_here",
          dp > SEP and dn > SEP,
          "a sum over letters is constant on the permutation orbit of a letter "
          "multiset, and the closure is not -- so NO functional of the "
          "multiset alone can select among these candidates, for any q and any "
          "coefficients. This upgrades the E_cross tie from an observation to "
          "a scope-(b) exclusion of the whole letter-sum class, invariant "
          "named: order-sensitivity of the closure", w)

    check("an_isotopy_class_energy_is_NOT_barred",
          len(pairs) == len(TWO_CROSSING),
          "the candidates are distinct isotopy classes, so the O'Hara/Moebius "
          "INFIMUM -- which is a function of the class -- takes potentially "
          "different values on them. Green light: the Bring->O'Hara route is "
          "not stillborn on discriminability. It does NOT follow that the "
          "energy would in fact separate them; a prune establishes only that "
          "it is not excluded", w)

    w.add_data("method", {
        "why_no_embedding_needed": "Moebius energy needs an embedding, but the "
                                   "QUESTION -- are these the same link? -- is "
                                   "answerable with a link invariant alone",
        "invariant": "Markov trace at z_D, normalised by writhe",
        "admissibility": "z_D = q^3/(q^2+1) is an admissible Markov parameter "
                         "under convention D",
        "direction": "distinguishing is SUFFICIENT, not necessary -- convention "
                     "D annihilates the (1,1,1) block, so this truncated "
                     "invariant may fail to separate some different links. The "
                     "asymmetry is in the safe direction for a prune",
    })
    w.add_data("candidates", {
        n: {"writhe": wr[n], "tr_p": mp.nstr(tp[n], 25),
            "tr_n": mp.nstr(tn[n], 25)}
        for n in TWO_CROSSING})
    w.add_data("verdict", {
        "distinct_links": len(pairs),
        "of": len(TWO_CROSSING),
        "letter_sum_class": "scope-(b) excluded -- constant on the permutation "
                            "orbit while the closure is not",
        "isotopy_class_energy": "NOT excluded -- green light for the "
                                "Bring->O'Hara route",
    })
    w.add_data("scope", {
        "class": "(b) structural for the letter-sum exclusion; (a) for the "
                 "green light",
        "not_claimed": [
            "that the O'Hara/Moebius energy would in fact separate them",
            "that the bridge is easy -- it still needs a canonical embedding "
            "or the minimiser",
            "that any candidate should be adopted",
        ],
        "no_selection_by_accuracy": "no Q_beta appears in this probe at all",
    })

    ok = not FAILED
    # AGENTS.md q0-anchor rule: "Say which pin you used. Any new witness
    # must record its q0 so a later reader can tell which layer it belongs
    # to without inferring it from a call site."
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.save()
    print()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
