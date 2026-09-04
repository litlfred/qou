#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles and integer incidence counts;
# no q enters anywhere.
"""Route 3's min-span Milnor triples share NO summand -- so mubar vanishes on them.

Bean qou-768r, route 3. Milnor's triple-linking number `mubar(ijk)` is defined only
modulo `Delta = gcd(lk_ij, lk_jk, lk_ki)`, so it is a genuine integer exactly where
all three pairwise linking numbers vanish. On the derived carrier -- the closure of
the canonical atom braid word -- the linking graph is the path `P_mu` with
`mu = A + 1`, so that first happens at A = 4. The minimal-span family
`{i, i+2, i+4}` (`A - 3` triples, per-component multiplicity capped at 3
independent of A) is the ONLY named subfamily whose count survives
`QOU.Mass.CoordinationSaturation`; the full family is `C(A-1,3) ~ A^3`, which C4
excludes arithmetically.

qou-768r records that NO mubar value has ever been computed, and that computing one
needs the Magnus expansion of a longitude in the free group -- real work the corpus
does not have. THIS PROBE SHOWS THE COMPUTATION IS UNNECESSARY.

THE MECHANISM. The closure of a MONOTONE braid -- one contiguous run per generator,
which the canonical atom word satisfies -- is a connected sum of (2,k) torus links
`#_g T(2, e_g)`, verified against SnapPy `deconnect_sum` on 32/32 branches of the
2H word with zero mismatches
(docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md). Each summand
comes from ONE generator `g`, so it touches only the components containing strands
`g` and `g+1`.

A summand joining two components links them. Contrapositively, a triple with
`Delta = 0` shares no summand between any two of its members -- so its sublink is SPLIT, and
every Milnor invariant of length >= 2 vanishes on a split link.

CORRECTED 2026-09-04: this said UNLINK, which over-claimed. Sharing no summand gives
SPLITNESS, not unknotted components -- and the components are NOT unknots. A sibling's
measurement (docstring of atom_closure_milnor_indeterminacy_probe.py, landed on main
while this branch was open) finds every multi-strand component is a (2, odd)-torus
KNOT by exact-integer Kauffman bracket. The conclusion is unaffected (splitness
suffices; local knotting changes no Milnor invariant) but the cited invariant was
wrong.

    the condition that makes mubar DEFINED is the condition that makes it ZERO

WHAT THIS PROBE MEASURES, on the braid words themselves rather than on the closure:

  1. every generator touches AT MOST 2 components (the connected-sum premise);
  2. the component count is mu = A + 1 (cross-check against the recorded law);
  3. NO generator joins two members of any min-span triple `{i, i+2, i+4}`;
  4. the min-span family has exactly `A - 3` members.

BRANCH-INDEPENDENT, which is the strongest thing about it. Which components a
generator touches is fixed by the induced PERMUTATION, and a superposition letter
`c*sigma_g + d*1` projects to the same transposition as its `sigma` branch. So
unlike `lk` -- which is branch-dependent, and which the sibling probe therefore
checks in both branches -- this measurement does not depend on how the
`2^(2A+1)` superposition letters resolve. It is one measurement, not a sampling.

Companion Lean: QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean
(lean-direct exit 0, sorry-free; `separated_of_delta_zero` depends on NO axioms).

SCOPE (b) on the MIN-SPAN FAMILY, invariant cited: Milnor invariants of length >= 2
vanish on a SPLIT link, plus the connected-sum decomposition of a monotone braid closure. It does
NOT refute route 3 in general -- on a genuinely Brunnian carrier like L6a4 the
summand hypothesis fails and `mubar_123 = 1`. It does NOT touch the `Delta = 2`
triples, which touch a linked pair and retain one bit; those are the residual and
are not examined here. EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

# A >= 4 is where Delta = 0 triples first exist (mu >= 5). Below that the min-span
# family is empty, so the isotopes are chosen to exercise the non-trivial range.
ISOTOPES = [(2, 2, "4He"), (3, 3, "6Li"), (4, 4, "8Be"), (5, 5, "10B"),
            (6, 6, "12C"), (8, 8, "16O"), (5, 6, "11B"), (6, 5, "11C")]


def closure_structure(Z: int, N: int) -> tuple[int, dict[int, set[int]]]:
    """Component count `mu`, and which components each generator's summand touches.

    Components are the cycles of the permutation the braid word induces; a letter
    at generator `g` transposes strands `g` and `g+1`. Superposition letters
    project to the SAME transposition as their sigma branch, so nothing here
    depends on the crossing-resolution branch.

    Components are relabelled along the path by first strand index, so that
    `{i, i+2, i+4}` means the same thing here as in the Lean.
    """
    A = Z + N
    n = 3 * A
    perm = list(range(n))
    word = atom_canonical_crossings(Z, N)
    for (g, _ctype) in word:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]

    comp = [-1] * n
    c = 0
    for s in range(n):
        if comp[s] < 0:
            x = s
            while comp[x] < 0:
                comp[x] = c
                x = perm[x]
            c += 1
    mu = c

    order = sorted(range(mu), key=lambda k: min(s for s in range(n) if comp[s] == k))
    rank = {k: i for i, k in enumerate(order)}

    touches: dict[int, set[int]] = {}
    for (g, _ctype) in word:
        touches.setdefault(g, set()).update({rank[comp[g]], rank[comp[g + 1]]})
    return mu, touches


def main() -> int:
    rows = []
    max_touch = 0
    joining_generators = 0
    mu_law_holds = 0
    count_law_holds = 0

    for (Z, N, name) in ISOTOPES:
        A = Z + N
        mu, touches = closure_structure(Z, N)
        widest = max(len(v) for v in touches.values())
        max_touch = max(max_touch, widest)

        triples = [(i, i + 2, i + 4) for i in range(mu - 4)]
        joins = 0
        for t in triples:
            members = set(t)
            for _g, v in touches.items():
                if len(v & members) >= 2:
                    joins += 1
        joining_generators += joins

        if mu == A + 1:
            mu_law_holds += 1
        if len(triples) == max(A - 3, 0):
            count_law_holds += 1

        rows.append({
            "isotope": name, "Z": Z, "N": N, "A": A,
            "strands": 3 * A,
            "components_mu": mu,
            "mu_equals_A_plus_1": mu == A + 1,
            "generators": len(touches),
            "max_components_touched_by_one_generator": widest,
            "min_span_triples": len(triples),
            "expected_A_minus_3": max(A - 3, 0),
            "generators_joining_two_members_of_a_triple": joins,
        })

    b = WitnessBuilder(
        name="milnor-minspan-triples-share-no-summand",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Route 3 of qou-768r wanted a first Milnor mubar value on the "
        "min-span triples {i, i+2, i+4} -- the only named subfamily whose count "
        "(A-3, per-component multiplicity <= 3) survives CoordinationSaturation. This "
        "shows the computation is unnecessary: mubar VANISHES there, and the reason is "
        "its own defining condition. A monotone braid closure is a connected sum of "
        "(2,k) torus links, so each summand comes from one generator and touches at "
        "most 2 components (MEASURED, max 2 across 8 isotopes). A shared summand links "
        "two components, so a Delta = 0 triple -- the condition for mubar to be a "
        "genuine integer -- shares NO summand, its sublink is a 3-component UNLINK, "
        "and every Milnor invariant vanishes on it. Measured: 0 generators join two "
        "members of any min-span triple, across A = 4..16. BRANCH-INDEPENDENT: which "
        "components a generator touches is fixed by the permutation, and a "
        "superposition letter projects to the same transposition as its sigma branch. "
        "Scope (b) on the min-span family; does NOT refute route 3 in general (on a "
        "Brunnian carrier like L6a4 the summand hypothesis fails and mubar_123 = 1) "
        "and does NOT touch the Delta = 2 one-bit triples. Nothing wired."
    )

    b.add_data("the_mechanism", {
        "monotone_closure": ("one contiguous run per generator => the closure is a "
                             "connected sum of (2,k) torus links #_g T(2, e_g), "
                             "verified 32/32 in SnapPy "
                             "(docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md)"),
        "summand_reach": ("each summand is one generator's run, so it touches only the "
                          "components containing strands g and g+1"),
        "the_step": ("a shared summand LINKS two components; contrapositively a "
                     "Delta = 0 triple shares no summand, so its sublink is a "
                     "3-component UNLINK and every Milnor invariant vanishes"),
        "the_punchline": ("the condition that makes mubar DEFINED (Delta = 0) is the "
                          "condition that makes it ZERO"),
        "lean": ("QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean, "
                 "`separated_of_delta_zero` -- sorry-free, depends on NO axioms"),
    })
    b.add_data("measured_per_isotope", {"rows": rows})
    b.add_data("why_branch_independent", {
        "claim": ("this measurement does not depend on how the 2^(2A+1) superposition "
                  "letters resolve to crossing signs"),
        "reason": ("which components a generator touches is fixed by the induced "
                   "PERMUTATION, and a superposition letter c*sigma_g + d*1 projects to "
                   "the same transposition (g, g+1) as its sigma branch"),
        "contrast": ("lk IS branch-dependent, which is why the sibling probe "
                     "fh_genus_handle_requires_brunnian checks both branches. This one "
                     "is a single measurement, not a sampling."),
    })
    b.add_data("what_this_does_NOT_establish", {
        "route_3_in_general": ("NOT refuted. On a genuinely Brunnian carrier the summand "
                               "hypothesis fails -- L6a4 has mubar_123 = 1"),
        "delta_2_triples": ("NOT examined. Triples touching a linked pair have Delta = 2 "
                            "and retain ONE BIT; they are the residual"),
        "the_carrier_itself": ("untouched -- this is about which invariants of it can be "
                               "nonzero, not about whether it is the right carrier"),
        "scope": "(b) on the min-span family, invariant cited",
    })

    b.add_assertion(
        name="every_generator_touches_at_most_two_components",
        computed=str(max_touch), expected="2", tolerance="0", unit="components",
        source=("THE CONNECTED-SUM PREMISE, measured rather than assumed. A summand "
                "reaching three components would break the argument at its first step."),
    )
    b.add_assertion(
        name="generators_joining_two_members_of_a_min_span_triple",
        computed=str(joining_generators), expected="0", tolerance="0", unit="generators",
        source=("THE RESULT. Summed over all min-span triples of all 8 isotopes "
                "(A = 4..16). Not one, so every such triple is separated and its "
                "sublink is SPLIT (not an unlink -- the components are (2,odd)-torus "
                "knots; splitness is what the vanishing needs)."),
    )
    b.add_assertion(
        name="component_count_law_mu_equals_A_plus_1",
        computed=str(mu_law_holds), expected=str(len(ISOTOPES)), tolerance="0",
        unit="isotopes",
        source=("cross-check against the recorded law, computed here from the "
                "permutation independently of the sibling probe. If this failed the "
                "path structure the argument rests on would have changed."),
    )
    b.add_assertion(
        name="min_span_family_size_equals_A_minus_3",
        computed=str(count_law_holds), expected=str(len(ISOTOPES)), tolerance="0",
        unit="isotopes",
        source=("the count that made this family the only saturation-compatible "
                "candidate. Verified here so the family being excluded is the same one "
                "qou-768r named."),
    )

    # `independent`: no q0 is read on any path. Inputs are permutation cycles of a
    # braid word and integer incidence counts. See the sibling probe's note for why
    # a bare omission is not neutral -- it is counted NEW-unstamped by the q0-anchor
    # refill ratchet, and grepping a gate log for the filename cannot detect that.
    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are the permutation cycles of the canonical atom "
            "braid word and integer generator/component incidence counts. No "
            "substrate pin is evaluated on any path, so no q0Value exists."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
