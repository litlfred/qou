#!/usr/bin/env python3
"""qou-99qc: 🛑 the crossing-budget parity result is a READING-1 theorem, and
the live reading is 3 — under which the budget is not constrained at all.

# Ref: computations/qbeta/qbeta_altchar_sign_is_length_parity_probe.py      (the parity theorem)
# Ref: computations/qbeta/qbeta_crossing_budget_gluon_parity_probe.py       (the budget sweep)
# Ref: computations/qbeta/qbeta_reading3_scope_fork_probe.py                (the A/B scope fork)
# Ref: computations/qbeta/qbeta_bar_parity_forces_a_unique_quark_letter_probe.py
# Ref: .beans/qou-ales--...md   (OWNER RULING 2026-09-12: reading 3, keep 1 and 2 for later)
# Ref: .beans/qou-99qc--...md

THIS PROBE CORRECTS MY OWN MERGED WORK. Three PRs (#7319, #7325, #7336) built a
length-parity exclusion on the alternating block `(1,1,1)`. The mathematics is
untouched and stays sorry-free; what was wrong is the READING it was attached
to, and therefore everything it was said to exclude.

THE THREE READINGS, and the corpus names them. Owner, 2026-09-12, verbatim:
*"try PSD condfinement 3 for now, but keep 1 2 for later"* (bean `qou-ales`):

    reading 1  literal `Matrix.PosSemidef` on every Wedderburn block
    reading 2  symmetric-part PSD
    reading 3  Frobenius positivity: `chi_lambda(w) >= 0` on every block
               with `y_lambda > 0`                          <-- SELECTED

WHAT I GOT WRONG. I recorded the 2026-09-13 owner answer in AGENTS.md as *"every
Wedderburn projection of the full 11-letter word must be `Matrix.PosSemidef`"*.
That sentence is reading **1**. The fork the owner answered was explicitly about
reading **3**'s scope — `qbeta_reading3_scope_fork_probe` states it as *"(A)
reading 3 applies to the gamma-gamma-SELECTED CORE only / (B) reading 3 applies
to the WHOLE 11-crossing word"*. So **(B) moved the letter scope and left the
reading alone.** Live criterion: reading 3, whole word.

WHY THAT IS FATAL TO THE PARITY RESULT SPECIFICALLY. Under convention D
`y_(1^3) = 0` — and that vanishing IS convention D, not a coincidence of the pin
(`markovWeights_eq_jones_of_threeRow_eq_zero`; D is the two-row truncation). So
reading 3 does not constrain the alternating block AT ALL, and the parity
theorem lives entirely in the block reading 3 ignores.

RESULT 1 -- READING 3 DOES NOT CONSTRAIN THE CROSSING BUDGET. Sweeping every
generator assignment and every dressing over the corpus alphabet, k = 0..3:

    k   length  parity  admissible (p)   admissible (n)
    0     9      odd        4/8              4/8
    1    10      even      18/48            18/48
    2    11      odd      149/288          145/288
    3    12      even     594/1728         594/1728

Odd lengths 9 and 11 are admissible in quantity. There is no parity signal, and
no monotone in k either. **The budget is simply not decided by this criterion.**

RESULT 2 -- THE QUARK FAMILY IS NOT EMPTY UNDER READING 3, AND I SAID IT WAS.
`qbeta_bar_parity_forces_a_unique_quark_letter_probe` checks
`all(is_psd(M) for every block)` — reading 1 — and concludes the SDP half
"rejects the whole family". Re-measured under reading 3, **one of the six
survives**: (slot 2, sigma), `chi_(2,1) = +0.0574586606`. So the family has a
survivor, and the bean's "what replaces the element" item has a candidate from
the corpus's own family that the reading-1 measurement hid.

RESULT 3 -- WHAT SURVIVES UNCHANGED: THE ELEMENT REJECTION. Both census
assignments stay excluded under reading 3 — p (slot 0, sigma) `chi_(2,1) =
-0.2805933509`, n (slot 2, inv) `-0.3719563247`. `nuc11_interleaved` fails the
`(2,1)` block, `y_(2,1) = 0.2473 > 0`, so that failure BINDS. AGENTS.md called
`(1,1,1)` the exclusion "already on record" and `(2,1)` "additional"; it is the
other way round — `(2,1)` is the whole of it, and it is enough. **Nothing
downstream of the element rejection moves**, and the L2 rows stay un-re-scored.

RESULT 4 -- AND THE PARITY THEOREM SAYS SOMETHING DECISION-RELEVANT ABOUT THE
PARKED READING. Under reading 1 no odd-length word over the corpus alphabet is
admissible at all, and **all three nucleon constructions in the tree are odd**
(9, 11 interleaved, 11 gen-grouped — `qou-1qsw`). So adopting reading 1 would
not merely tighten the selection, it would empty it: every nucleon model dies on
length, whatever its dressing, and a survivor would need either an even-length
model or a letter outside the alphabet (shift `d >= 1/(q^2-1) = 4.3094` against
the corpus's `{0, -1/2, -1}`). That is an argument about reading 1's viability
for THIS corpus, and it is the parity work's real contribution.

WHAT IS NOT CLAIMED. That reading 3 is right and reading 1 wrong — that is the
owner's parked call and nothing here touches it. That the budget is
unconstrained full stop: it is unconstrained *by this criterion*, and the
γγ-construction half still forces the 6-letter core. That the (slot 2, sigma)
survivor should be adopted — it is one admissible point among many and
selecting it because it survives would be selection against the target.

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_reading3_does_not_constrain_the_budget_probe.py \
       2>&1 | tee /tmp/qbeta_reading3_budget.log
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

#: convention-D Markov weights at level 2. `y_(1^3) = 0` is not imposed here --
#: it is implied by `Y3 + 2*Y21 = 1`, which check 1 verifies exactly.
Y3 = (Q0 ** 4 + 1) / (Q0 ** 2 + 1) ** 2
Y21 = Q0 ** 2 / (Q0 ** 2 + 1) ** 2

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)
SHIFTS = (Z, HALF, NEG1)

#: the B_3 gamma-gamma core, (sigma_0 sigma_1^-1)^3 -- 6 letters, even.
CORE = [(0, Z), (1, NEG1)] * 3
#: the quark block's shift multiset, per nucleon (determined by flavour).
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}

#: the one-letter quark family, in the sibling probe's (slot, kind) coordinates.
GENS = (0, 0, 1)
SLOTS = (0, 1, 2)
KINDS = ("sigma", "inv")
NUM_SHIFT = {"sigma": Z, "fixed": HALF, "inv": NEG1}
GLUON2 = [(0, Z), (0, Z)]
CENSUS_P, CENSUS_N = (0, "sigma"), (2, "inv")

#: every nucleon construction `pyhecke.atom` carries (bean qou-1qsw).
CORPUS_NUCLEON_LENGTHS = {
    "build_nucleon_nf": 9,
    "build_atom_nf_exact (nuc11_interleaved)": 11,
    "nucleon_gen_chains (gen-grouped)": 11,
}

TOL = mp.mpf("1e-25")
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


def chi3(letters):
    """The one-dimensional `(3)` character: `sigma -> q`, so a letter
    `sigma_g + d*h` has value `q + d*h`.  Multiplicative, and independent of
    which generator each letter sits on."""
    v = mp.mpf(1)
    for _, d in letters:
        v *= (Q0 + d * H0)
    return v


def chi21(letters):
    """Extracted by subtraction from `tr_{z_D} = y_(3) chi_(3) + y_(2,1)
    chi_(2,1)` -- exact, and inheriting convention D and the proton pin from
    that quantity and nothing else."""
    return (tr(letters) - Y3 * chi3(letters)) / Y21


def reading3(letters) -> bool:
    """`chi_lambda(w) >= 0` on every block with `y_lambda > 0`.  Under D that
    is `(3)` and `(2,1)`; `y_(1^3) = 0`, so the alternating block is not
    constrained."""
    return chi3(letters) >= 0 and chi21(letters) >= 0


def quark_letters(slot: int, kind: str):
    quark = [(GENS[i], NUM_SHIFT[kind] if i == slot else NUM_SHIFT["fixed"])
             for i in SLOTS]
    return CORE + quark + GLUON2


def main() -> int:
    w = WitnessBuilder("qbeta-reading3-does-not-constrain-the-budget")
    w.set_description(
        "CORRECTS my own merged work (#7319/#7325/#7336). The crossing-budget "
        "length-parity exclusion is a READING-1 theorem; the owner selected "
        "reading 3 (Frobenius positivity on blocks with y_lambda > 0) on "
        "2026-09-12, and the 2026-09-13 (B) answer moved the LETTER scope, not "
        "the reading. Under convention D y_(1^3) = 0, so reading 3 does not "
        "constrain the alternating block where the parity theorem lives. "
        "Measured: reading 3 admits every dressing count k = 0..3 for both "
        "nucleons, including the odd lengths 9 and 11 -- the budget is not "
        "decided by this criterion. Two further corrections: the one-letter "
        "quark family is NOT empty under reading 3 (1 of 6 survives, (slot 2, "
        "sigma), chi_(2,1) = +0.0574586606), and the element rejection that "
        "does stand rests on (2,1) ALONE, not on (1,1,1). The parity theorem "
        "survives as a statement about the parked reading 1, where it is "
        "annihilating: all three corpus nucleon models are odd."
    )

    print("qou-99qc — reading 1 vs reading 3, and what the budget actually "
          "constrains")
    print(f"  q0 (proton pin) = {mp.nstr(Q0, 20)}")
    print(f"  h = q - 1/q     = {mp.nstr(H0, 20)}")
    print(f"  z_D             = {mp.nstr(ZD, 20)}")
    print()

    # ---- 1. calibration: y_(1^3) = 0 is convention D, not an artefact -----
    print("== 1. calibration — the weights, and the vanishing third row ==")
    tot = Y3 + 2 * Y21
    print(f"  y_(3)   = {mp.nstr(Y3, 20)}")
    print(f"  y_(2,1) = {mp.nstr(Y21, 20)}")
    print(f"  y_(3) + 2 y_(2,1) = {mp.nstr(tot, 25)}")
    check("y_1cubed_vanishes_under_convention_D",
          abs(tot - 1) < TOL,
          f"y_(3) + 2 y_(2,1) = 1 to {mp.nstr(abs(tot - 1), 4)}, and the three "
          f"block dimensions are 1, 2, 1 -- so y_(1^3) = 0 EXACTLY. This is the "
          f"two-row truncation that defines convention D "
          f"(markovWeights_eq_jones_of_threeRow_eq_zero), not a numerical "
          f"accident of the pin. It is why reading 3 cannot see the "
          f"alternating block at all", w)

    ident_c21 = chi21([])
    check("chi21_of_the_identity_is_the_block_dimension",
          abs(ident_c21 - 2) < TOL,
          f"chi_(2,1)(1) = {mp.nstr(ident_c21, 20)}, block dimension 2 -- the "
          f"subtraction extraction is calibrated before any verdict is read "
          f"off it", w)

    letter_c3 = [Q0 + d * H0 for d in SHIFTS]
    print(f"  chi_(3) per letter: " +
          ", ".join(mp.nstr(v, 12) for v in letter_c3))
    check("the_3_block_can_never_bind_on_this_alphabet",
          all(v > 0 for v in letter_c3),
          f"every corpus letter has chi_(3) > 0 "
          f"({mp.nstr(min(letter_c3), 12)} at worst), and chi_(3) is "
          f"multiplicative, so chi_(3)(w) > 0 for EVERY word. The whole content "
          f"of reading 3 on this alphabet is chi_(2,1) >= 0 -- reproduced here "
          f"independently of the sibling probe that first reported it", w)
    print()

    # ---- 2. the budget sweep under reading 3 ------------------------------
    print("== 2. reading 3 against the crossing budget ==")
    print("   k  length  parity   admissible (p)    admissible (n)")
    table = {}
    for k in range(0, 4):
        row = {}
        for nuc in ("p", "n"):
            ok_n = tot_n = 0
            for qg in itertools.product((0, 1), repeat=3):
                base = CORE + [(g, s) for g, s in zip(qg, QSHIFT[nuc])]
                for dr in itertools.product(
                        itertools.product((0, 1), SHIFTS), repeat=k):
                    tot_n += 1
                    if reading3(base + list(dr)):
                        ok_n += 1
            row[nuc] = (ok_n, tot_n)
        table[k] = row
        par = "even" if (9 + k) % 2 == 0 else "odd"
        print(f"   {k}    {9 + k:2d}    {par:4s}    "
              f"{row['p'][0]:5d}/{row['p'][1]:<6d}    "
              f"{row['n'][0]:5d}/{row['n'][1]:<6d}")

    every_k_has_survivors = all(
        table[k][n][0] > 0 for k in table for n in ("p", "n"))
    check("reading3_does_not_constrain_the_crossing_budget",
          every_k_has_survivors,
          "every dressing count k = 0..3 has admissible configurations for "
          "BOTH nucleons, so reading 3 selects no gluon count. The parity "
          "constraint of #7336 (gluon dressing must be ODD) has no force under "
          "the live reading -- it is a reading-1 statement", w)

    odd_ok = table[0]["p"][0] > 0 and table[2]["p"][0] > 0
    check("reading3_admits_ODD_length_words_in_quantity",
          odd_ok,
          f"length 9 ({table[0]['p'][0]}/{table[0]['p'][1]}) and length 11 "
          f"({table[2]['p'][0]}/{table[2]['p'][1]}) are both admissible for the "
          f"proton -- directly contradicting the consequence I drew from the "
          f"parity theorem, which excluded every odd length. The THEOREM is "
          f"fine; it is about the block reading 3 ignores", w)
    print()

    # ---- 3. the quark family, re-measured --------------------------------
    print("== 3. the one-letter quark family under reading 3 ==")
    print("   slot kind    chi_(3)         chi_(2,1)        reading 3")
    fam = {}
    for sl in SLOTS:
        for kd in KINDS:
            L = quark_letters(sl, kd)
            c3, c21 = chi3(L), chi21(L)
            fam[(sl, kd)] = (c3, c21, reading3(L))
            tag = ("  <- census p" if (sl, kd) == CENSUS_P else
                   "  <- census n" if (sl, kd) == CENSUS_N else "")
            print(f"    {sl}   {kd:<6s} {mp.nstr(c3, 12):<15s} "
                  f"{mp.nstr(c21, 12):<16s} "
                  f"{'ADMISSIBLE' if fam[(sl, kd)][2] else 'excluded'}{tag}")

    survivors = [k for k, v in fam.items() if v[2]]
    check("reading3_leaves_exactly_one_survivor_in_the_quark_family",
          len(survivors) == 1 and survivors[0] == (2, "sigma"),
          f"survivors = {survivors}, chi_(2,1) = "
          f"{mp.nstr(fam[(2, 'sigma')][1], 12)}. The sibling probe reports the "
          f"family as entirely rejected; it checks all(is_psd(M)) over EVERY "
          f"block, which is reading 1. Under the live reading the family is not "
          f"empty -- so qou-99qc's 'what replaces the element' item has a "
          f"candidate the reading-1 measurement hid", w)

    check("both_census_assignments_stay_excluded_under_reading3",
          not fam[CENSUS_P][2] and not fam[CENSUS_N][2],
          f"p {CENSUS_P} chi_(2,1) = {mp.nstr(fam[CENSUS_P][1], 12)}, "
          f"n {CENSUS_N} chi_(2,1) = {mp.nstr(fam[CENSUS_N][1], 12)} -- both "
          f"negative, and y_(2,1) = {mp.nstr(Y21, 8)} > 0, so the (2,1) failure "
          f"BINDS. The element rejection stands on (2,1) alone; nothing "
          f"downstream of it moves and the L2 rows stay un-re-scored", w)
    print()

    # ---- 4. what the parity theorem does constrain -----------------------
    print("== 4. reading 1 — where the parity theorem does bite ==")
    odd_models = {k: v for k, v in CORPUS_NUCLEON_LENGTHS.items() if v % 2 == 1}
    for name, ln in CORPUS_NUCLEON_LENGTHS.items():
        print(f"    {name:<42s} {ln:2d}  {'odd' if ln % 2 else 'even'}")
    threshold = 1 / (Q0 ** 2 - 1)
    print(f"    positivity threshold on a letter's shift: d >= "
          f"{mp.nstr(threshold, 12)}")
    print(f"    corpus alphabet shifts: 0, -1/2, -1")
    check("reading1_would_annihilate_every_corpus_nucleon_model",
          len(odd_models) == len(CORPUS_NUCLEON_LENGTHS),
          f"all {len(CORPUS_NUCLEON_LENGTHS)} nucleon constructions in the tree "
          f"are ODD, so under reading 1 -- where the parity theorem does apply "
          f"-- every one of them is excluded on LENGTH, whatever its dressing. "
          f"A survivor would need an even-length model or a letter with shift "
          f"d >= {mp.nstr(threshold, 10)}, against the alphabet's "
          f"max of 0. That is a fact about reading 1's viability for this "
          f"corpus, and it is the parity work's real contribution", w)

    w.add_data("readings", {
        "1": "literal Matrix.PosSemidef on every Wedderburn block -- PARKED",
        "2": "symmetric-part PSD -- PARKED",
        "3": "Frobenius positivity, chi_lambda(w) >= 0 on every block with "
             "y_lambda > 0 -- SELECTED by the owner 2026-09-12",
        "owner_verbatim": "try PSD condfinement 3 for now, but keep 1 2 for later",
        "scope_ruling_2026_09_13": "(B) whole element -- this moved the LETTER "
                                   "scope of reading 3; it did NOT change the "
                                   "reading, and AGENTS.md said it did",
    })
    w.add_data("budget_sweep_reading3", {
        f"k{k}": {"length": 9 + k,
                  "parity": "even" if (9 + k) % 2 == 0 else "odd",
                  "p_admissible": table[k]["p"][0], "p_total": table[k]["p"][1],
                  "n_admissible": table[k]["n"][0], "n_total": table[k]["n"][1]}
        for k in table})
    w.add_data("quark_family_reading3", {
        f"slot{sl}_{kd}": {"chi3": mp.nstr(fam[(sl, kd)][0], 20),
                           "chi21": mp.nstr(fam[(sl, kd)][1], 20),
                           "admissible": bool(fam[(sl, kd)][2])}
        for sl in SLOTS for kd in KINDS})
    w.add_data("corrects", {
        "AGENTS.md": "the 2026-09-13 ruling paragraph named reading 1 "
                     "('every Wedderburn projection ... Matrix.PosSemidef') "
                     "for a fork that was about reading 3's scope; and it "
                     "called (1,1,1) the exclusion already on record with "
                     "(2,1) additional, which is backwards",
        "qbeta_altchar_sign_is_length_parity_probe": "its exclusion is "
                                                     "reading-1 scoped",
        "qbeta_crossing_budget_gluon_parity_probe": "the ODD-dressing "
                                                    "constraint is reading-1 "
                                                    "scoped and has no force "
                                                    "under reading 3",
        "qbeta_bar_parity_forces_a_unique_quark_letter_probe": "its "
            "psd_feasible() is reading 1; under reading 3 one of the six "
            "configurations survives",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited",
        "unconditional": [
            "y_(1^3) = 0 under convention D",
            "reading 3 admits every k = 0..3 for both nucleons",
            "both census assignments fail chi_(2,1) >= 0",
            "all three corpus nucleon models have odd length",
        ],
        "not_claimed": [
            "that reading 3 is correct and reading 1 wrong -- parked owner call",
            "that the budget is unconstrained by anything -- the gamma-gamma "
            "construction half still forces the 6-letter core",
            "that the (slot 2, sigma) survivor should be adopted",
        ],
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
