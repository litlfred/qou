#!/usr/bin/env python3
"""Are the six adopted antipode axioms independent, or does the package shrink?

`def:frobenius-hopf-substrate` axiom 2 (2026-09-15, owner decision) asks for six
conditions on `S` at once:

    1 anti_mul       S(xy)      = S(y) S(x)
    2 anti_comul     Delta(S x) = sum S(x_2) (x) S(x_1)
    3 unit           S(1)       = 1
    4 counit         eps(S x)   = eps(x)
    5 involutive     S(S x)     = x
    6 form           lambda(S x) = lambda(x)

Classically anti-algebra and anti-coalgebra are THEOREMS derived from the
convolution antipode axiom, not axioms.  Here they are asserted, so the question
is whether any of the six follows from the other five.  That is red-team item 2
of docs/audits/2026-09-15-antipode-anti-automorphism-package.md, and it was
recorded as UNMEASURED.  This probe measures it.

METHOD -- semantic independence by counter-model.  Fix the group algebra `k[G]`
with its Frobenius structure (the same structure as the sibling probe: mu = group
multiplication, Delta(x) = sum_h xh (x) h^-1, eps = lambda = coefficient of the
identity).  Those structure maps involve no `S`, so every structure axiom holds
for every candidate `S` and the six conditions are the only thing varying.  Then
for each axiom i, search the candidate maps for one satisfying all five others
and VIOLATING i.  Such a map is a model of {axioms} \ {i} that is not a model of
i, which proves i is not derivable from the other five.

WHAT A NEGATIVE DOES NOT SHOW.  Finding no counter-model over these groups does
NOT prove the axiom is dependent.  It says this family cannot decide it.  The
verdicts below are therefore INDEPENDENT (proved, by exhibited witness) or
UNDECIDED-HERE (no witness in the searched space) -- never "dependent".

CANDIDATE SPACE.  `S` is taken monomial: `S(g) = sigma(g)` for a function
sigma : G -> G, coefficient 1.  That is where the classical antipode lives and
where the vacuous `S = id` lives, so it is the space the axioms are meant to cut
down.  A general linear `S` is a |G| x |G| matrix and is NOT searched; a witness
found here is still a witness, so the INDEPENDENT verdicts are unaffected, but an
UNDECIDED-HERE is weaker for that reason too.  Exhaustive |G|^|G| up to S_3
(46656 maps); D_4 would be 16777216, so only its 40320 bijections are searched.

A PREDICTED BLIND SPOT, asserted rather than assumed: on `k[G]` the counit and
the Frobenius form are the SAME map (both are "coefficient of the identity"), so
axioms 4 and 6 are literally the same condition here and no counter-model can
separate them.  In the Lean structure they are separate fields -- `frobeniusForm`
is constrained only by the two snake identities, `counit` only by the counit laws,
and nothing ties them -- so their independence is a real open question that this
family is structurally unable to answer.  The probe checks the coincidence rather
than trusting it.

ARITHMETIC: exact.  Every coefficient is a Python `int`; there is no float in
this file -- not as an input, not as an intermediate, not in a comparison.  No
experimental value is touched, so there is no anchor and no q0 to pin.

Emits no witness: it records structural yes/no verdicts about an axiom system,
not a numeric quantity anything downstream re-derives.

Beans: `qou-k4zx`, `qou-c64q`.
"""

from __future__ import annotations

import sys
from itertools import permutations, product

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from frobenius_hopf_intermediate_axioms_probe import (  # noqa: E402
    Group,
    cyclic,
    dihedral4,
    klein,
    symmetric3,
)

# --------------------------------------------------------------------------
# The six axioms, each on a monomial S given as a dict sigma : G -> G
# --------------------------------------------------------------------------


def ax1_anti_mul(G: Group, s: dict) -> bool:
    """`S(xy) = S(y) S(x)`."""
    return all(s[G.mul(x, y)] == G.mul(s[y], s[x])
               for x in G.elements for y in G.elements)


def ax2_anti_comul(G: Group, s: dict) -> bool:
    """`Delta(S x) = (S (x) S) . beta . Delta(x)`.

    `Delta(x) = sum_h xh (x) h^-1`, so the left side is the multiset
    `{(S(x) h, h^-1)}` and the right side, after the braiding swaps the two
    legs, is `{(S(h^-1), S(xh))}`.
    """
    for x in G.elements:
        lhs = sorted((G.mul(s[x], h), G.inv[h]) for h in G.elements)
        rhs = sorted((s[G.inv[h]], s[G.mul(x, h)]) for h in G.elements)
        if lhs != rhs:
            return False
    return True


def ax3_unit(G: Group, s: dict) -> bool:
    """`S(1) = 1`."""
    return s[G.e] == G.e


def ax4_counit(G: Group, s: dict) -> bool:
    """`eps . S = eps`, with `eps(g) = [g = 1]`."""
    return all((s[x] == G.e) == (x == G.e) for x in G.elements)


def ax5_involutive(G: Group, s: dict) -> bool:
    """`S . S = id`."""
    return all(s[s[x]] == x for x in G.elements)


def ax6_form(G: Group, s: dict) -> bool:
    """`lambda . S = lambda`, with `lambda(sum a_g g) = a_e`.

    On `k[G]` this is the SAME predicate as `ax4_counit` -- see the module
    docstring.  Written out separately, not aliased, so that
    `check_counit_form_coincide` below is a real check rather than a tautology
    about one function called twice.
    """
    return all((1 if s[x] == G.e else 0) == (1 if x == G.e else 0)
               for x in G.elements)


AXIOMS = [
    ("1 anti_mul", ax1_anti_mul),
    ("2 anti_comul", ax2_anti_comul),
    ("3 unit", ax3_unit),
    ("4 counit", ax4_counit),
    ("5 involutive", ax5_involutive),
    ("6 form", ax6_form),
]


# --------------------------------------------------------------------------
# Candidate spaces
# --------------------------------------------------------------------------


def all_maps(G: Group):
    """Every function `G -> G`.  `|G|^|G|` of them."""
    for image in product(G.elements, repeat=G.order):
        yield dict(zip(G.elements, image))


def all_bijections(G: Group):
    """Every bijection `G -> G`.  `|G|!` of them."""
    for image in permutations(G.elements):
        yield dict(zip(G.elements, image))


def candidates(G: Group):
    """Exhaustive where that is cheap, bijections only where it is not."""
    if G.order ** G.order <= 100_000:
        return all_maps(G), f"all {G.order ** G.order} maps"
    return all_bijections(G), f"the {_fact(G.order)} bijections only"


def _fact(n: int) -> int:
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


# --------------------------------------------------------------------------
# The measurement
# --------------------------------------------------------------------------


def find_counter_model(G: Group, drop: int):
    """A map satisfying every axiom but `drop`, and violating `drop`."""
    gen, _ = candidates(G)
    for s in gen:
        if AXIOMS[drop][1](G, s):
            continue
        if all(f(G, s) for j, (_, f) in enumerate(AXIOMS) if j != drop):
            return s
    return None


def minimal_forcing_subsets(G: Group, target: int):
    """Which subsets of the other axioms already force `target` on `k[G]`?

    An UNDECIDED-HERE verdict says only "no counter-model was found".  That is
    not a reason, and a reason is what tells you whether the family is the wrong
    instrument or the axiom is genuinely redundant.  So for each subset of the
    other five, check whether every candidate satisfying the subset also
    satisfies `target`, and keep the subsets minimal under inclusion.
    """
    others = [j for j in range(len(AXIOMS)) if j != target]
    cands = list(candidates(G)[0])
    forcing = []
    for size in range(0, len(others) + 1):
        for sub in _subsets(others, size):
            if any(set(f) <= set(sub) for f in forcing):
                continue                     # not minimal
            if all(AXIOMS[target][1](G, s)
                   for s in cands
                   if all(AXIOMS[j][1](G, s) for j in sub)):
                forcing.append(sub)
        if forcing:
            break                            # minimal size reached
    return forcing


def _subsets(xs, k):
    from itertools import combinations
    return [list(c) for c in combinations(xs, k)]


def check_counit_form_coincide(G: Group) -> bool:
    """Assert, rather than assume, that axioms 4 and 6 coincide on `k[G]`."""
    gen, _ = candidates(G)
    return all(ax4_counit(G, s) == ax6_form(G, s) for s in gen)


def fmt(G: Group, s: dict) -> str:
    return "  ".join(f"{g!r}->{s[g]!r}" for g in G.elements)


def main() -> int:
    groups = [cyclic(1), cyclic(2), cyclic(3), cyclic(4), klein(),
              symmetric3(), dihedral4()]

    print("=" * 78)
    print("AXIOM INDEPENDENCE OF THE SIX ANTIPODE CONDITIONS")
    print("=" * 78)
    print()
    print("A counter-model to axiom i is a map satisfying the other five and")
    print("violating i.  One anywhere proves i is not derivable from them.")
    print()

    witnesses: dict[int, tuple[str, dict]] = {}

    for G in groups:
        gen_desc = candidates(G)[1]
        found = []
        for i, (name, _) in enumerate(AXIOMS):
            if i in witnesses:
                found.append("-")          # already proved elsewhere
                continue
            s = find_counter_model(G, i)
            if s is None:
                found.append(".")
            else:
                witnesses[i] = (G.name, s)
                found.append("W")
        print(f"  {G.name:<5} |G| = {G.order}  ({gen_desc})")
        print(f"        axioms 1..6: {' '.join(found)}"
              "     W = witness found here, . = none, - = already proved")

    print()
    print("-" * 78)
    print("VERDICTS")
    print("-" * 78)
    n_indep = 0
    for i, (name, _) in enumerate(AXIOMS):
        if i in witnesses:
            gname, s = witnesses[i]
            n_indep += 1
            print(f"  {name:<16} INDEPENDENT   witness on {gname}:")
            print(f"  {'':<16}   S = {fmt([g for g in groups if g.name == gname][0], s)}")
        else:
            print(f"  {name:<16} UNDECIDED-HERE   no counter-model in the searched space")

    print()
    print("-" * 78)
    print("WHY THE UNDECIDED ONES ARE UNDECIDED -- MINIMAL FORCING SUBSETS")
    print("-" * 78)
    print("  For each axiom with no counter-model, the smallest sets of the")
    print("  others that ALREADY force it on this family.  An empty set means")
    print("  the family satisfies it unconditionally.")
    print()
    # Two exhaustively-searched groups on opposite sides of commutativity, so a
    # forcing that is an artifact of `G` abelian (where an anti-automorphism is
    # just an automorphism) shows up as a disagreement between the columns.
    # D_4 is excluded here: only its bijections were searched, and restricting
    # to bijections would itself manufacture forcings involving `involutive`.
    probe_groups = [klein(), symmetric3()]
    for i, (name, _) in enumerate(AXIOMS):
        if i in witnesses:
            continue
        for PG in probe_groups:
            subs = minimal_forcing_subsets(PG, i)
            if not subs:
                print(f"    {name:<16} on {PG.name:<4} forced by NOTHING"
                      " -- a counter-model exists outside the searched space")
                continue
            for sub in subs:
                shown = ", ".join(AXIOMS[j][0] for j in sub) or "(nothing -- holds always)"
                print(f"    {name:<16} on {PG.name:<4} <= {{{shown}}}")

    print()
    print("-" * 78)
    print("THE PREDICTED BLIND SPOT, CHECKED")
    print("-" * 78)
    coincide = {G.name: check_counit_form_coincide(G) for G in groups}
    ok = all(coincide.values())
    print("  On k[G] the counit and the Frobenius form are the same map, so")
    print("  axioms 4 and 6 are the same condition and NO counter-model can")
    print("  separate them.  Checked, per group (True = they coincide):")
    print(f"    {coincide}")
    print()
    if ok:
        print("  So an UNDECIDED-HERE on axiom 4 or 6 is a statement about this")
        print("  FAMILY, not about the axioms: in the Lean structure `counit` and")
        print("  `frobeniusForm` are separate fields tied by nothing, and deciding")
        print("  their independence needs a Frobenius object where lambda != eps.")
    else:
        print("  !! The coincidence FAILED on some group -- the docstring's")
        print("     structural claim is wrong and the 4/6 verdicts must be re-read.")

    print()
    print("=" * 78)
    print(f"RESULT: {n_indep} of 6 proved independent; "
          f"{6 - n_indep} undecided in this family.")
    print("=" * 78)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
