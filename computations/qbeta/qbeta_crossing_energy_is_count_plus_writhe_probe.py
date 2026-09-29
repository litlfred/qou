#!/usr/bin/env python3
"""qou-99qc: crossing ENERGY is crossing COUNT plus a writhe term, so it
re-ranks candidates iff the writhe differs -- and it is not a braid invariant
at all, unlike the observable it would be used to select for.

# Ref: content/quantum-observable-universe/lean/QOU/Mass/CrossingEnergySelectionEqualsCount.lean
# Ref: content/quantum-observable-universe/lean/QOU/Braiding/crossing_energy_channels.lean
# Ref: computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py  (the measured disagreement)
# Ref: computations/qbeta/qbeta_cost_minimal_budget_under_reading3_probe.py   (count-minimal budget)
# Ref: .beans/qou-99qc--...md

WHY THIS EXISTS. The owner objected (2026-09-14, verbatim): *"The selection rule
shouldn't be minimum crossing... It may be higher energy than a non-minimal
crossing."* The sibling probe measured that crossing energy and crossing count
DO disagree on the gluon dressing, and left open WHEN. The companion Lean
settles it structurally; this probe is the measured half.

THE STRUCTURE, and it is the corpus's own. `QOU.Braiding.crossingEnergy p m q =
p*q - m/q` splits (`crossingEnergy_split`) into

    symChannel  = (p - m) * (q + 1/q)/2     multiplicity = the WRITHE
    asymChannel = (p + m) * (q - 1/q)/2     multiplicity = the COUNT

The writhe is a braid invariant; the crossing count is not. Everything below
follows from that one asymmetry.

RESULT 1 -- THE IDENTITY. `E_cross(w) = n_plus * h + W/q` exactly, where
`h = q - 1/q` and `W = n_plus - n_minus`. Verified on every gluon candidate the
sibling probe tabulates, at 60 dps. This is the same split regrouped so that
the non-invariant multiplicity sits alone on one term.

RESULT 2 -- THE OBSERVABLE IS A BRAID-ELEMENT INVARIANT. `tr_M` is a trace, so
it is constant on cyclic rotations of the word (measured: agrees to 1.6e-61,
i.e. exactly at 60 dps) and unchanged by inserting a cancelling pair (measured:
delta EXACTLY zero). A corollary worth having on its own: the gluon's POSITION
as a contiguous block is immaterial -- prepending it gives the identical trace
to appending it -- so block placement is not a degree of freedom in the
candidate set.

RESULT 3 -- THE COST IS NOT. The same cancelling-pair insertion that leaves the
trace alone raises `E_cross` by exactly `h = 0.2091`. So `E_cross` is a function
of the WORD where the observable is a function of the braid ELEMENT: two
presentations of one object are ranked differently by the cost and identically
by the thing being predicted.

RESULT 4 -- AT FIXED WRITHE THE TWO COSTS ARE ONE ORDERING. Over every ordered
pair of candidates with equal writhe, the energy comparison and the count
comparison agree in every case. That is the `iff` of
`energy_le_iff_count_le_of_writhe_eq`, measured.

RESULT 5 -- AND EVERY DISAGREEMENT CARRIES A WRITHE DIFFERENCE. The converse is
NOT claimed and is measured separately: pairs with differing writhe may still
agree. What is established is the one-way implication -- disagreement implies
differing writhe -- which is what bounds the upgrade.

WHAT THIS MEANS FOR THE OPEN ITEM. Swapping the count for the energy changes no
selection within a fixed-writhe family; it re-ranks only across writhe. So the
owner's objection to the count is not answered by the energy, because the energy
is the count plus a writhe correction. A genuine upgrade must not be a function
of `(n_plus, n_minus)` at all -- which is exactly what an embedding energy
(O'Hara / Moebius via the Bring surface) is, and it is not built.

WHAT IS NOT CLAIMED. That either cost should be adopted or retired. That any
candidate should be selected. No Q_beta is computed here at all, deliberately:
the claims are about invariance and ordering, and a target that is never
evaluated cannot be selected on (AGENTS.md NO FITTING).

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_crossing_energy_is_count_plus_writhe_probe.py \
       2>&1 | tee /tmp/qbeta_ecross_count_writhe.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)

#: the corpus atom, as the sibling probe builds it: core + quark + gluon.
CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
GENS = (0, 0, 1)

#: exact at 60 dps -- both sides are algebraic in q0.
TOL = mp.mpf("1e-50")
#: the trace comparisons run through a normal form, so they carry a few ulp.
TRTOL = mp.mpf("1e-55")

FAILED: list[str] = []
#: number of `check` calls made, so the summary line cannot drift.
CHECKS = [0]


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    CHECKS[0] += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def counts(letters):
    """`(n_plus, n_minus)` over PURE crossings.  The bar-fixed letter
    (`d = -h/2`) is not a crossing and raises rather than being fudged --
    same guard as `def:crossing-energy`."""
    npos = nneg = 0
    for _, d in letters:
        if d == Z:
            npos += 1
        elif d == NEG1:
            nneg += 1
        else:
            raise ValueError("crossing counts undefined on the bar-fixed letter")
    return npos, nneg


def ecross(letters) -> mp.mpf:
    npos, nneg = counts(letters)
    return npos * Q0 - nneg / Q0


#: the gluon candidates, verbatim from the sibling probe so the two tables are
#: comparable line for line.
CANDIDATES = {
    "(empty)": [],
    "sigma_1": [(1, Z)],
    "sigma_1^-1": [(1, NEG1)],
    "sigma_0": [(0, Z)],
    "sigma_0^-1": [(0, NEG1)],
    "sigma_0 sigma_0 (LIVE)": [(0, Z), (0, Z)],
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
    "sigma_0^-1 sigma_1^-1": [(0, NEG1), (1, NEG1)],
    "sigma_0 sigma_1^-1": [(0, Z), (1, NEG1)],
}


def main() -> int:
    w = WitnessBuilder("qbeta-crossing-energy-is-count-plus-writhe")
    w.set_description(
        "The owner objected that crossing COUNT is the wrong selection cost and "
        "proposed crossing ENERGY; a sibling probe measured that they disagree "
        "and left open when. Measured here: E_cross = n_plus*h + W/q exactly, "
        "so the energy is the count plus a writhe correction. The observable is "
        "a braid-ELEMENT invariant -- tr_M is constant on cyclic rotations "
        "(1.6e-61) and exactly unchanged by inserting a cancelling pair, which "
        "also makes a contiguous gluon's position immaterial -- while E_cross "
        "rises by exactly h under that same insertion, so the cost is a WORD "
        "functional. Over every equal-writhe pair the energy ordering and the "
        "count ordering coincide, so swapping the cost re-ranks only across "
        "writhe. Conclusion: the objection to the count is not answered by the "
        "energy; a genuine upgrade must not be a function of (n_plus, n_minus) "
        "at all. Adopts neither cost, selects no candidate, computes no Q_beta."
    )

    print("qou-99qc — crossing energy = crossing count + writhe term")
    print(f"  q0 = {mp.nstr(Q0, 20)}   h = q - 1/q = {mp.nstr(H0, 20)}")
    print()

    # ---- 1. the identity, on every candidate -----------------------------
    print("== 1. E_cross = n+ * h + W/q, exactly ==")
    print(f"  {'candidate':24s} {'n+':>3s} {'n-':>3s} {'W':>3s} "
          f"{'E_cross':>20s} {'n+ h + W/q':>20s}")
    ident_ok = True
    rows = []
    for name, ls in CANDIDATES.items():
        npos, nneg = counts(ls)
        wr = npos - nneg
        lhs, rhs = ecross(ls), npos * H0 + wr / Q0
        ident_ok &= abs(lhs - rhs) < TOL
        rows.append({"candidate": name, "n_plus": npos, "n_minus": nneg,
                     "writhe": wr, "E_cross": mp.nstr(lhs, 30)})
        print(f"  {name:24s} {npos:3d} {nneg:3d} {wr:3d} "
              f"{mp.nstr(lhs, 14):>20s} {mp.nstr(rhs, 14):>20s}")
    check("ecross_equals_npos_h_plus_writhe_over_q", ident_ok,
          f"exact to < {mp.nstr(TOL, 3)} on all {len(CANDIDATES)} candidates; "
          f"this is the corpus's own symChannel/asymChannel split regrouped so "
          f"the non-invariant multiplicity (the count) sits alone on one term", w)
    w.add_data("candidates", rows)

    # ---- 2. the observable is a braid-ELEMENT invariant ------------------
    print("\n== 2. tr_M is a braid-element invariant ==")
    live = base("p") + [(0, Z), (0, Z)]
    t0 = tr(live)
    print(f"    word length {len(live)}   tr_M = {mp.nstr(t0, 25)}")

    rot_max = mp.mpf(0)
    for k in range(1, len(live)):
        rot_max = max(rot_max, abs(tr(live[k:] + live[:k]) - t0))
    print(f"    max |tr(rotation) - tr(W)| over all {len(live) - 1} rotations "
          f": {mp.nstr(rot_max, 6)}")
    check("tr_M_is_constant_on_cyclic_rotations", rot_max < TRTOL,
          f"max deviation {mp.nstr(rot_max, 6)} over all {len(live) - 1} "
          f"rotations -- tr_M is a trace, so it is a class function and the "
          f"observable is constant on conjugacy classes", w)

    pre = [(0, Z), (0, Z)] + base("p")
    d_pos = abs(tr(pre) - t0)
    print(f"    gluon prepended instead of appended        : "
          f"delta {mp.nstr(d_pos, 6)}")
    check("contiguous_gluon_position_is_not_a_degree_of_freedom", d_pos < TRTOL,
          f"prepending the 2-letter gluon gives the same trace as appending it "
          f"(delta {mp.nstr(d_pos, 6)}) -- a corollary of cyclicity, and it "
          f"removes block PLACEMENT from the candidate set", w)

    canc = live + [(1, Z), (1, NEG1)]
    d_canc = abs(tr(canc) - t0)
    print(f"    cancelling pair sigma_1 sigma_1^-1 appended: "
          f"delta {mp.nstr(d_canc, 6)}")
    check("tr_M_unchanged_by_a_cancelling_pair", d_canc < TRTOL,
          f"delta {mp.nstr(d_canc, 6)} -- the insertion changes no braid "
          f"element, and the observable does not see it", w)

    # ---- 3. the cost is NOT ----------------------------------------------
    print("\n== 3. E_cross is a WORD functional, not a braid invariant ==")
    e_live = ecross([(0, Z), (0, Z)])
    e_canc = ecross([(0, Z), (0, Z), (1, Z), (1, NEG1)])
    shift = e_canc - e_live
    print(f"    E_cross(gluon)                 = {mp.nstr(e_live, 20)}")
    print(f"    E_cross(gluon + cancelling)    = {mp.nstr(e_canc, 20)}")
    print(f"    shift                          = {mp.nstr(shift, 20)}   "
          f"h = {mp.nstr(H0, 20)}")
    check("cancelling_pair_shifts_ecross_by_exactly_h",
          abs(shift - H0) < TOL and H0 > 0,
          f"shift {mp.nstr(shift, 20)} = h exactly, and h > 0 for q > 1. The "
          f"SAME insertion left tr_M exactly unchanged (check above), so the "
          f"cost ranks two presentations of one braid element differently while "
          f"the observable ranks them identically", w)
    w.add_data("cancelling_pair_shift", mp.nstr(shift, 30))

    # ---- 4. at fixed writhe the two orderings coincide -------------------
    print("\n== 4. equal writhe => the energy order IS the count order ==")
    names = list(CANDIDATES)
    eq_w_pairs = agree = 0
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pa, ma = counts(CANDIDATES[a])
            pb, mb = counts(CANDIDATES[b])
            if pa - ma != pb - mb:
                continue
            eq_w_pairs += 1
            e_order = ecross(CANDIDATES[a]) <= ecross(CANDIDATES[b])
            c_order = (pa + ma) <= (pb + mb)
            if e_order == c_order:
                agree += 1
            else:
                print(f"    DISAGREE at equal writhe: {a} vs {b}")
    print(f"    equal-writhe ordered pairs: {eq_w_pairs}; orderings agree in "
          f"{agree}")
    check("equal_writhe_pairs_order_identically_under_both_costs",
          eq_w_pairs > 0 and agree == eq_w_pairs,
          f"{agree}/{eq_w_pairs} -- the measured half of "
          f"`energy_le_iff_count_le_of_writhe_eq`. Swapping the cost changes no "
          f"selection inside a fixed-writhe family", w)

    # ---- 5. every disagreement carries a writhe difference ---------------
    print("\n== 5. every disagreement carries a writhe difference ==")
    diff_w_pairs = diff_w_disagree = 0
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pa, ma = counts(CANDIDATES[a])
            pb, mb = counts(CANDIDATES[b])
            if pa - ma == pb - mb:
                continue
            diff_w_pairs += 1
            if (ecross(CANDIDATES[a]) <= ecross(CANDIDATES[b])) != \
               ((pa + ma) <= (pb + mb)):
                diff_w_disagree += 1
    print(f"    differing-writhe ordered pairs: {diff_w_pairs}; of these the "
          f"two costs disagree on {diff_w_disagree}")
    check("disagreement_occurs_only_where_the_writhe_differs",
          diff_w_disagree > 0,
          f"{diff_w_disagree} of {diff_w_pairs} differing-writhe pairs "
          f"disagree, against 0 of {eq_w_pairs} equal-writhe pairs. The "
          f"CONVERSE is NOT claimed: a differing-writhe pair may still agree, "
          f"and {diff_w_pairs - diff_w_disagree} of them do. What is "
          f"established is the one-way implication, which is what bounds the "
          f"upgrade", w)
    w.add_data("pair_census", {
        "equal_writhe_pairs": eq_w_pairs,
        "equal_writhe_disagreements": eq_w_pairs - agree,
        "differing_writhe_pairs": diff_w_pairs,
        "differing_writhe_disagreements": diff_w_disagree,
    })

    # ---- 6. the sibling probe's headline pair, structurally explained ----
    print("\n== 6. the sibling's headline disagreement is a writhe difference ==")
    e_p, e_m = ecross([(1, Z)]), ecross([(1, NEG1)])
    wp = counts([(1, Z)])[0] - counts([(1, Z)])[1]
    wm = counts([(1, NEG1)])[0] - counts([(1, NEG1)])[1]
    print(f"    sigma_1    : count 1, writhe {wp:+d}, E = {mp.nstr(e_p, 14)}")
    print(f"    sigma_1^-1 : count 1, writhe {wm:+d}, E = {mp.nstr(e_m, 14)}")
    gap = e_p - e_m
    predicted = (wp - wm) * (Q0 + 1 / Q0) / 2
    print(f"    gap {mp.nstr(gap, 20)}   (W+ - W-)*symmetricWeight "
          f"{mp.nstr(predicted, 20)}")
    check("headline_gap_equals_the_writhe_term_exactly",
          abs(gap - predicted) < TOL,
          f"the pair the sibling probe reports as count-tied and "
          f"energy-separated differs by exactly "
          f"`(W1 - W2)*symmetricWeight q` = {mp.nstr(predicted, 20)} -- i.e. by "
          f"the writhe term and nothing else, which is "
          f"`crossingEnergy_sub_eq_writhe_term_of_count_eq`", w)

    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): " + ", ".join(FAILED))
        w.save()
        return 1
    print(f"all {len(CANDIDATES)} candidates, {CHECKS[0]}/{CHECKS[0]} checks pass")
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
