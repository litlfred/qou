"""The crossing budget's GLUON DRESSING must have odd length — and every count
the corpus proposes is even, so every corpus nucleon model is excluded.

# Ref: QOU.Mass.AltCharShiftMultiset.gluon_dressing_must_be_odd -- the Lean,
#      sorry-free, proved BEFORE this probe (formalize-first)
# Ref: QOU.Mass.AltCharShiftMultiset.both_corpus_budgets_are_odd
# Ref: QOU.Mass.AltCharShiftMultiset.wordChar_sign -- the parity this rests on
# Ref: computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py -- records
#      that pyhecke.atom carries THREE mutually inconsistent nucleon models
# Ref: computations/qbeta/qbeta_adjunction_ilp_probe.py -- "the MINIMUM is
#      three gluon crossings", by integer feasibility; an INDEPENDENT route
# Ref: bean qou-99qc, OWNER RULING 2026-09-13 -- SDP scope is (B) whole element

THE QUESTION.  Under scope (B) the confinement SDP asks every Wedderburn
projection to be PSD; the alternating block is one-dimensional, so there PSD is
`0 <= character`; and the character's sign is `(-1)^length`.  So the crossing
budget must be EVEN.  The corpus budget is 11.  Which part is wrong?

THE ANSWER, AND IT IS NOT WHERE THE CORPUS HAS BEEN ARGUING.  The nucleon is
`core . quark . gluon`.  The B_3 core `(sigma_0 sigma_1^-1)^3` is 6 letters
(EVEN); the quark block is 3 (ODD).  So admissibility turns on exactly one
thing -- whether the gluon dressing has ODD length.  It is a parity constraint,
not a count, which is what makes it a statement about the budget.

WHY THE 9-VS-11 DEBATE CANNOT SETTLE IT.  The live
`pyhecke.atom.nucleon_word_letters` emits 11 (6+3+2); `build_nucleon_nf` emits
9 (6+3), its docstring saying "B_3 IS the gluon structure".  Those differ by
**2** -- the same parity -- so no choice between them changes anything here.

AND EVERY PROPOSED GLUON COUNT IS EVEN:

  * `stable-atom-properties.md` -- "the unique integer solution sigma_0 ->
    sigma_0 (2 gluon crossings) that restores stability";
  * `gluon-stabiliser-ledger.md` -- "two gluon crossings and the neutron four"
    (already struck through in the corpus, on other grounds);
  * `categorical-neutron-properties.md` -- an earlier "4 gluon crossings, 13
    total", recorded there as wrong on its own terms.

AN INDEPENDENT CONVERGENCE.  `qbeta_adjunction_ilp_probe` measured, by integer
feasibility over {sigma_0, sigma_1, L_+, L_-}, that "the MINIMUM is three gluon
crossings", and flagged the 2-crossing blocks as a tension it could not settle
("the predicate is my reading ... one confirmed prediction does not make it the
corpus's predicate").  Parity is a different argument from different premises
and reaches the same verdict on the 2.

🛑 WHAT IS NOT CLAIMED: that parity selects 3.  ANY odd dressing satisfies it --
1, 3, 5 alike, and this probe checks that explicitly.  Three is merely the
smallest odd count that ALSO clears that probe's feasibility floor.  Combining
the two arguments to manufacture a unique answer would be selection against the
target, which AGENTS.md bans.  Parity EXCLUDES 2 and 4; it does not choose.

SCOPE.  **(b) structural**, invariant named: the sign of the alternating
character.  Conditional on scope (B) and on the corpus alphabet (letter shifts
in {0, -1/2, -1}); a letter with shift `d >= 1/(q^2-1) ~ 4.31` would break the
per-letter negativity, and nothing in the corpus supplies one.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

set_compute_dps(60)
mp.mp.dps = 40

Q0 = mp.mpf(str(_oc.Q0))
H0 = mp.mpf(str(_oc.H0))

#: the corpus alphabet as shift-in-units-of-h (the three `Letter` constructors)
SHIFTS = {"sigma": mp.mpf(0), "fixed": mp.mpf("-0.5"), "inv": mp.mpf(-1)}

#: the decomposition the corpus builds, as (generator, shift-in-h)
CORE = [(0, mp.mpf(0)), (1, mp.mpf(-1))] * 3            # B_3 = (s0 s1^-1)^3
QUARK = {
    "p": [(0, mp.mpf(0)), (0, mp.mpf("-0.5")), (1, mp.mpf("-0.5"))],
    "n": [(0, mp.mpf("-0.5")), (0, mp.mpf("-0.5")), (1, mp.mpf(-1))],
}
GLUON = [(0, mp.mpf(0)), (0, mp.mpf(0))]                # the 2-letter dressing

#: gluon counts the corpus has proposed, with their sources.
CORPUS_GLUON_COUNTS = {
    2: "stable-atom-properties.md -- 'the unique integer solution sigma_0 -> "
       "sigma_0 (2 gluon crossings) that restores stability'",
    4: "categorical-neutron-properties.md (earlier, recorded there as wrong on "
       "its own terms) and gluon-stabiliser-ledger.md (struck through)",
}

TOL = mp.mpf("1e-30")

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def alt_letter(d) -> mp.mpf:
    return -1 / Q0 + mp.mpf(str(d)) * H0


def alt_word(letters) -> mp.mpf:
    out = mp.mpf(1)
    for _g, d in letters:
        out *= alt_letter(d)
    return out


def main() -> int:
    w = WitnessBuilder("qbeta-crossing-budget-gluon-parity")
    w.set_description(
        "The crossing budget must be EVEN under scope (B), because the "
        "alternating block is 1-dimensional and the character's sign is "
        "(-1)^length. The B_3 core is 6 letters (even) and the quark block 3 "
        "(odd), so admissibility turns on exactly one thing: the GLUON "
        "DRESSING must have ODD length. Proved first in Lean "
        "(gluon_dressing_must_be_odd, sorry-free). Consequences measured here: "
        "every gluon count the corpus proposes (2 and the retracted 4) is EVEN "
        "and therefore excluded; and the 9-vs-11 budget debate cannot bear on "
        "this at all, because 9 and 11 differ by 2 and so share a parity. "
        "Converges independently with qbeta_adjunction_ilp_probe's measured "
        "minimum of three gluon crossings. NOT claimed: that parity selects 3 "
        "-- any odd dressing satisfies it, and this probe checks that."
    )

    print("== 1. the decomposition's parities ==")
    print(f"     core  {len(CORE)} letters  ({'even' if len(CORE) % 2 == 0 else 'odd'})")
    print(f"     quark {len(QUARK['p'])} letters  ({'even' if len(QUARK['p']) % 2 == 0 else 'odd'})")
    print(f"     gluon {len(GLUON)} letters  ({'even' if len(GLUON) % 2 == 0 else 'odd'})")
    check("the_obstruction_is_located_in_the_quark_block",
          len(CORE) % 2 == 0 and len(QUARK["p"]) % 2 == 1
          and len(QUARK["n"]) % 2 == 1,
          f"core {len(CORE)} is EVEN and the quark block {len(QUARK['p'])} is "
          f"ODD for both nucleons, so the core contributes nothing to the "
          f"parity and the whole question reduces to the gluon dressing. This "
          f"is what makes the result a budget statement rather than a claim "
          f"about one word", w)

    print("\n== 2. the 9-vs-11 debate is parity-irrelevant ==")
    nine, eleven = len(CORE) + len(QUARK["p"]), len(CORE) + len(QUARK["p"]) + len(GLUON)
    check("nine_and_eleven_have_the_same_parity_so_neither_helps",
          nine % 2 == eleven % 2 == 1 and eleven - nine == 2,
          f"build_nucleon_nf emits {nine} (B_3 IS the gluon structure, per its "
          f"own docstring) and the live nucleon_word_letters emits {eleven}. "
          f"They differ by {eleven - nine}, so they share a parity and BOTH are "
          f"odd. Whichever the corpus picks, the alternating block excludes it. "
          f"Lean: both_corpus_budgets_are_odd", w)

    print("\n== 3. every gluon count the corpus proposes is EVEN ==")
    verdicts = {}
    for k, src in CORPUS_GLUON_COUNTS.items():
        total = nine + k
        dressing = [(0, mp.mpf(0))] * k
        val = alt_word(CORE + QUARK["p"] + dressing)
        verdicts[k] = {"total_crossings": total, "total_parity":
                       "even" if total % 2 == 0 else "odd",
                       "altChar": mp.nstr(val, 20),
                       "admissible": bool(val > 0), "source": src}
        print(f"     {k} gluon crossings -> total {total} ({'even' if total % 2 == 0 else 'odd'}), "
              f"altChar {mp.nstr(val, 12)}, admissible={val > 0}")
    check("every_corpus_proposed_gluon_count_is_even_hence_excluded",
          all(k % 2 == 0 and not verdicts[k]["admissible"]
              for k in CORPUS_GLUON_COUNTS),
          f"the corpus proposes {sorted(CORPUS_GLUON_COUNTS)} gluon crossings; "
          f"both are EVEN, so both leave the total ODD and both are excluded in "
          f"the alternating block. This is a measured consequence of the parity "
          f"theorem, not an independent finding", w)

    print("\n== 4. ANY odd dressing works, ANY even one fails — parity, not a count ==")
    keys = list(SHIFTS)
    sweep = {}
    bad: list[str] = []
    for k in range(0, 6):
        adm = set()
        for combo in itertools.product(keys, repeat=k):
            dressing = [(i % 2, SHIFTS[c]) for i, c in enumerate(combo)]
            val = alt_word(CORE + QUARK["p"] + dressing)
            adm.add(bool(val > 0))
        sweep[k] = {"dressings_tested": len(keys) ** k,
                    "all_admissible": adm == {True},
                    "all_excluded": adm == {False}}
        expect_admissible = (k % 2 == 1)
        if adm != {expect_admissible}:
            bad.append(f"k={k} mixed: {adm}")
        print(f"     k={k}: {len(keys)**k:3d} dressings, "
              f"{'ALL admissible' if adm == {True} else 'ALL excluded'}")
    check("odd_dressings_are_ALL_admissible_and_even_ones_ALL_excluded",
          not bad,
          f"swept every dressing over the 3-letter alphabet at each length "
          f"k = 0..5 ({sum(len(keys)**k for k in range(6))} in total). At every "
          f"ODD k all are admissible; at every EVEN k all are excluded; no "
          f"length is mixed. So the constraint is a PARITY and not a count -- "
          f"k = 1, 3 and 5 all satisfy it, and parity alone does NOT select 3", w)

    print("\n== 5. the ILP floor and the parity are independent and agree ==")
    ilp_min = 3
    check("the_smallest_count_satisfying_BOTH_is_three_but_parity_does_not_pick_it",
          ilp_min % 2 == 1 and sweep[ilp_min]["all_admissible"]
          and not sweep[2]["all_admissible"],
          f"qbeta_adjunction_ilp_probe measured by INTEGER FEASIBILITY that the "
          f"minimum gluon dressing is {ilp_min}; parity independently requires "
          f"it to be ODD. {ilp_min} is the smallest count meeting both, and 2 "
          f"meets neither. 🛑 The two arguments are recorded as CONVERGING, not "
          f"combined: that probe says its own predicate is 'my reading' and not "
          f"established as the corpus's, and choosing 3 because two arguments "
          f"intersect there would be selection against the target", w)

    print("\n== 6. the corpus nucleon words as built, both excluded ==")
    built = {}
    for kind in ("p", "n"):
        word = CORE + QUARK[kind] + GLUON
        val = alt_word(word)
        built[kind] = {"length": len(word), "altChar": mp.nstr(val, 25),
                       "admissible": bool(val > 0)}
        print(f"     {kind}: {len(word)} letters, altChar {mp.nstr(val, 20)}, "
              f"admissible={val > 0}")
    check("both_corpus_nucleons_as_built_are_excluded",
          all(not built[k]["admissible"] and built[k]["length"] == 11
              for k in ("p", "n")),
          f"both are 11 letters and both have negative alternating character, "
          f"so under scope (B) neither is admissible -- and by section 4 that "
          f"is not repairable by changing WHICH letters are used, only by "
          f"changing HOW MANY", w)

    w.add_data("decomposition", {
        "core": {"letters": len(CORE), "parity": "even",
                 "what": "B_3 = (sigma_0 sigma_1^-1)^3, the Borromean gluon field"},
        "quark": {"letters": len(QUARK["p"]), "parity": "odd",
                  "what": "the flavour crossings; THIS is where the "
                          "obstruction lives"},
        "gluon": {"letters": len(GLUON), "parity": "even",
                  "what": "the dressing whose parity decides admissibility"},
    })
    w.add_data("budgets", {
        "build_nucleon_nf": {"crossings": nine, "parity": "odd",
                             "note": "its docstring: 'B_3 IS the gluon structure'"},
        "nucleon_word_letters_live": {"crossings": eleven, "parity": "odd"},
        "difference": eleven - nine,
        "verdict": "same parity, so the 9-vs-11 argument cannot bear on this",
    })
    w.add_data("corpus_proposed_gluon_counts", verdicts)
    w.add_data("parity_sweep", sweep)
    w.add_data("independent_convergence", {
        "ilp_minimum": ilp_min,
        "ilp_source": "qbeta_adjunction_ilp_probe -- integer feasibility over "
                      "{sigma_0, sigma_1, L_+, L_-}",
        "ilp_own_caveat": "'the predicate is my reading of (G x)_gamma ... one "
                          "confirmed prediction does not make it the corpus's "
                          "predicate' -- so it is scope-(a), not settled",
        "parity_requirement": "odd",
        "relationship": "INDEPENDENT arguments that agree on excluding 2. NOT "
                        "combined to select 3 -- parity admits 1, 3, 5 alike",
    })
    w.add_data("corpus_nucleons_as_built", built)
    w.add_data("scope", {
        "class": "(b) structural",
        "invariant": "the sign of the alternating character, = (-1)^length",
        "conditional_on": ["scope (B) whole element (owner ruling 2026-09-13)",
                           "the corpus alphabet, shifts in {0, -1/2, -1}"],
        "what_is_NOT_claimed": "that parity selects 3, or any particular count. "
                               "It excludes 2 and 4 and admits every odd count",
    })
    # AGENTS.md q0-anchor rule: "Say which pin you used. Any new witness
    # must record its q0 so a later reader can tell which layer it belongs
    # to without inferring it from a call site."
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.save()

    ok = not FAILED
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
