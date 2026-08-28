#!/usr/bin/env python3
"""Does the pinch's MARKED PAIR select the Klein quartic?  No -- it EXCLUDES it.
(bean qou-8p1b)

Context
-------
`s4_genus3_pencil_infinite_family.py` (bean qou-8p1a) showed the S_4 bridge is
near-vacuous: infinitely many pairwise non-isomorphic genus-3 curves admit S_4,
a whole pencil of them.  The chapter's follow-up sharpening was that the
degeneration supplies MORE data than "genus 3 and admits S_4":

    pinching ONE non-separating cycle on a genus-4 curve yields a one-node
    curve of arithmetic genus 4 whose normalization has genus 3 TOGETHER WITH
    TWO MARKED POINTS -- the two preimages of the node (3 + 1 = 4).

and since the pinched cycle is S_4-invariant, S_4 preserves that pair setwise.
The hope was that requiring an S_4-stable point pair would cut the pencil down,
ideally to the Klein quartic.  This script tests that hope.

Result
------
It does not cut the pencil down.  It cuts EVERYTHING down: **S_4 has no orbit
of size <= 2 on P^2 at all**, so no smooth plane quartic -- no member of the
pencil, and in particular not the Klein quartic -- carries an S_4-stable pair
of points.

The argument is short and is a genuine obstruction, not a numerical near-miss.
Let {p, q} be an S_4-stable pair on P^2 (allowing p = q).  Permuting the pair
gives a homomorphism S_4 -> S_2, whose kernel K has index 1 or 2 in S_4.

  * index 1: every element of S_4 fixes p, so the line through p is an
    S_4-invariant 1-dimensional subspace of C^3;
  * index 2: K is the unique index-2 subgroup A_4, and the line through p is
    an A_4-invariant 1-dimensional subspace.

Both are impossible, because both representations are ABSOLUTELY IRREDUCIBLE:
an absolutely irreducible representation has no proper invariant subspace over
any extension field, in particular no invariant line.  So no such pair exists.

Why "faithful in PGL_3" already forces irreducible
---------------------------------------------------
The argument above is applied to OUR S_4, whose absolute irreducibility is
machine-verified below.  To carry it to an arbitrary genus-3 target one needs:
every faithful 3-dimensional representation of S_4 is irreducible.  That is
short, and here is the split between what this script checks and what is
standard character theory:

  * A reducible 3-dimensional representation decomposes (Maschke, char 0) into
    summands of dimensions (1,1,1) or (1,2).
  * Every 1-dimensional representation of S_4 factors through the
    abelianisation S_4 / [S_4, S_4], so its kernel contains [S_4, S_4] = A_4.
    **Machine-verified here**: the derived subgroup is computed and has order
    12.
  * The 2-dimensional irreducible representation of S_4 has kernel V_4
    (it factors through S_4 / V_4 = S_3).  **Standard, cited not recomputed.**
  * Hence a (1,1,1) decomposition has kernel containing A_4, and a (1,2)
    decomposition has kernel containing A_4 inter V_4 = V_4.  Both are
    nontrivial, so neither is faithful.

Also relevant: 3-dimensional PROJECTIVE representations of S_4 all lift to
linear ones (the relevant covers contribute irreducibles of dimensions 2 and 4,
not 3), so working with linear representations loses nothing.  Standard, cited.

Consequence for the Bring -> Klein degeneration
-----------------------------------------------
Under the chapter's own three premises --

  (H1) the pinch is of a single S_4-invariant NON-SEPARATING cycle, i.e.
       exactly one node (this is what "arithmetic genus 4, geometric genus 3"
       in the chapter's own chain means);
  (H2) S_4 acts FAITHFULLY on the normalization (this is what "S_4 survives
       the pinch and embeds in Aut" asserts);
  (H3) the normalization is NON-hyperelliptic, so its canonical model is a
       smooth plane quartic and Aut acts through PGL_3 -- true of the Klein
       quartic;

-- the configuration the degeneration is supposed to produce DOES NOT EXIST.
(H1) supplies an S_4-stable pair; (H2)+(H3) put S_4 faithfully inside PGL_3,
where every faithful 3-dimensional representation of S_4 is irreducible, and
the argument above then forbids the pair.

So the marked-point data is not the separator the chapter hoped for.  It is an
obstruction, and it points the other way: it EXCLUDES every non-hyperelliptic
target, the Klein quartic included.

Scope
-----
**scope-(b), a structural exclusion, not a scope-(a) numerical negative.**  It
is licensed as (b) because a proved invariant forbids the configuration -- an
orbit/index count against absolute irreducibility -- rather than because some
computed quantity came out with the wrong magnitude.  The invariant is named
and machine-verified below (commutant dimension 1, equivalently character norm
1, for both S_4 and A_4).

What is NOT excluded, stated precisely so this is not over-read:

  * **Hyperelliptic** genus-3 targets.  If the normalization is hyperelliptic
    its canonical map is 2:1 onto a conic, Aut does not act through PGL_3 in
    the above way, and the argument does not apply.  Indeed
    y^2 = x^8 + 14x^4 + 1 has Aut of order 48 containing S_4.  The Klein
    quartic is not hyperelliptic, so this escape does not rescue it.
  * Degenerations violating (H1) -- several nodes, or a separating cycle.
    These change the genus bookkeeping and are simply a different claim from
    the one the chapter's chain makes.
  * Degenerations violating (H2) -- if S_4 does not act faithfully on the
    normalization, then "S_4 survives" is false as stated and the bridge
    premise has to be rewritten anyway.
  * The Bring surface itself, and whether any S_4-invariant cycle exists on
    it: not addressed here.  This script constrains the TARGET, not the source.

Exact arithmetic only: integer matrices and Fraction linear algebra, no floats.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "s4-marked-pair-obstruction.witness.json"

IDENT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def trace(g):
    return g[0][0] + g[1][1] + g[2][2]


def build_S4():
    """G = { diag(e) * P_sigma : prod(e) = +1 }, the irreducible S_4 in PGL_3."""
    gens = []
    for sigma in itertools.permutations(range(3)):
        gens.append(tuple(tuple(1 if sigma[i] == j else 0 for j in range(3))
                          for i in range(3)))
    for e in itertools.product((1, -1), repeat=3):
        if e[0] * e[1] * e[2] == 1:
            gens.append(tuple(tuple(e[i] if i == j else 0 for j in range(3))
                              for i in range(3)))
    G = set(gens) | {IDENT}
    changed = True
    while changed:
        changed = False
        for a in list(G):
            for b in list(G):
                c = matmul(a, b)
                if c not in G:
                    G.add(c)
                    changed = True
    return sorted(G)


def inverse_of(g, G):
    for h in G:
        if matmul(g, h) == IDENT:
            return h
    raise RuntimeError("no inverse")


def derived_subgroup(G):
    """[G, G] -- for G = S_4 this is A_4, the unique index-2 subgroup."""
    comms = set()
    for a in G:
        ai = inverse_of(a, G)
        for b in G:
            bi = inverse_of(b, G)
            comms.add(matmul(matmul(a, b), matmul(ai, bi)))
    H = set(comms) | {IDENT}
    changed = True
    while changed:
        changed = False
        for a in list(H):
            for b in list(H):
                c = matmul(a, b)
                if c not in H:
                    H.add(c)
                    changed = True
    return sorted(H)


def rref_rank(rows, ncols):
    m = [list(r) for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for k in range(rank, len(m)):
            if m[k][col] != 0:
                piv = k
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = Fraction(1) / m[rank][col]
        m[rank] = [x * inv for x in m[rank]]
        for k in range(len(m)):
            if k != rank and m[k][col] != 0:
                f = m[k][col]
                m[k] = [x - f * y for x, y in zip(m[k], m[rank])]
        rank += 1
        if rank == len(m):
            break
    return rank


def commutant_dim(H):
    """dim { X in M_3(Q) : X h = h X for all h in H }.  1 <=> absolutely irred."""
    rows = []
    for g in H:
        for r in range(3):
            for c in range(3):
                row = [Fraction(0)] * 9
                for k in range(3):
                    row[3 * r + k] += g[k][c]
                    row[3 * k + c] -= g[r][k]
                rows.append(row)
    return 9 - rref_rank(rows, 9)


def character_norm(H):
    """(1/|H|) * sum_h chi(h)^2 ; equals 1 exactly when chi is irreducible."""
    return Fraction(sum(trace(h) ** 2 for h in H), len(H))


def main() -> int:
    print("=" * 74)
    print("qou-8p1b : does the pinch's marked pair select the Klein quartic?")
    print("=" * 74)

    checks: dict[str, bool] = {}

    G = build_S4()
    checks["S4_order_24"] = len(G) == 24
    print(f"\nS_4 as an irreducible subgroup of PGL_3 : |G| = {len(G)}")

    # order profile, to pin the isomorphism type (same test as qou-8p1a)
    def order_of(g):
        n, cur = 1, g
        while cur != IDENT:
            cur = matmul(cur, g)
            n += 1
        return n

    prof: dict[int, int] = {}
    for g in G:
        o = order_of(g)
        prof[o] = prof.get(o, 0) + 1
    checks["S4_order_profile"] = prof == {1: 1, 2: 9, 3: 8, 4: 6}
    print(f"  element-order profile {dict(sorted(prof.items()))} "
          f"(S_4) : {checks['S4_order_profile']}")

    A4 = derived_subgroup(G)
    checks["A4_order_12"] = len(A4) == 12
    print(f"\nA_4 = [G, G] : |A_4| = {len(A4)} (want 12, index 2)")
    # A_4 is the UNIQUE index-2 subgroup: any index-2 subgroup is normal and
    # contains every square, hence contains [G,G]; equal orders force equality.
    squares = {matmul(g, g) for g in G}
    checks["A4_contains_all_squares"] = squares.issubset(set(A4))
    print(f"  contains every square of G (=> unique index-2 subgroup) : "
          f"{checks['A4_contains_all_squares']}")

    # -- the invariant that does the work --------------------------------
    cd_G, cd_A = commutant_dim(G), commutant_dim(A4)
    cn_G, cn_A = character_norm(G), character_norm(A4)
    checks["S4_absolutely_irreducible"] = cd_G == 1 and cn_G == 1
    checks["A4_absolutely_irreducible"] = cd_A == 1 and cn_A == 1
    print("\nTHE INVARIANT (two independent computations each):")
    print(f"  S_4 : commutant dim = {cd_G}, character norm <chi,chi> = {cn_G}"
          f"  => absolutely irreducible : {checks['S4_absolutely_irreducible']}")
    print(f"  A_4 : commutant dim = {cd_A}, character norm <chi,chi> = {cn_A}"
          f"  => absolutely irreducible : {checks['A4_absolutely_irreducible']}")
    print("  (an absolutely irreducible rep has NO invariant line over any")
    print("   extension field, hence no fixed point in P^2)")

    # -- the orbit consequence -------------------------------------------
    # A stable pair {p,q} gives S_4 -> S_2; the kernel has index 1 or 2, so it
    # is S_4 itself or A_4, and p is fixed by it -- an invariant line.  Both
    # are now excluded.
    no_small_orbit = (checks["S4_absolutely_irreducible"]
                      and checks["A4_absolutely_irreducible"])
    checks["no_S4_orbit_of_size_le_2"] = no_small_orbit
    print(f"\nCONSEQUENCE: S_4 has no orbit of size <= 2 on P^2 : {no_small_orbit}")
    print("  orbit size 1 needs an S_4-invariant line  -- excluded above")
    print("  orbit size 2 needs an A_4-invariant line  -- excluded above")
    print("  (index-2 kernel must be A_4: it is the unique index-2 subgroup)")

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (bean qou-8p1b)
-----------------------
The marked-pair sharpening is NOT a separator.  It is an OBSTRUCTION, and it
excludes the Klein quartic rather than selecting it.

Under the chapter's own premises -- (H1) one S_4-invariant non-separating
cycle, hence one node and an S_4-stable pair of preimages; (H2) S_4 faithful on
the normalization; (H3) the normalization non-hyperelliptic, so S_4 sits
faithfully in PGL_3 -- the required configuration does not exist, because S_4
has no orbit of size <= 2 on P^2.  The Klein quartic satisfies (H3), so it is
excluded.

SCOPE-(b), a structural exclusion licensed by a proved invariant (absolute
irreducibility of the 3-dimensional representation of S_4 and of its
restriction to A_4, each verified twice here).  NOT a scope-(a) numerical
near-miss.

NOT excluded, and the honest escape routes:
  * hyperelliptic genus-3 targets (canonical map 2:1 onto a conic, so Aut does
    not act through PGL_3 this way).  Klein is not hyperelliptic.
  * pinches violating (H1) -- several nodes, or a separating cycle.
  * actions violating (H2) -- but then "S_4 survives" is false as stated.
  * anything about the Bring surface itself.  This constrains the TARGET only.
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The marked-pair data supplied by the pinch does not select the "
            "Klein quartic -- it excludes it. S_4 has no orbit of size <= 2 on "
            "P^2, so no smooth plane quartic carries an S_4-stable point pair. "
            "Bean qou-8p1b (parent qou-8pl1)."
        ),
        "computation": {
            "script": "computations/s4_marked_pair_obstruction.py",
            "arithmetic": "exact integer matrices + Fraction linear algebra; no floating point",
        },
        "data": {
            "groups": {
                "S4_order": len(G),
                "S4_element_order_profile": {str(k): v for k, v in sorted(prof.items())},
                "A4_order": len(A4),
                "A4_is_derived_subgroup": True,
                "A4_unique_index_2": checks["A4_contains_all_squares"],
            },
            "invariant": {
                "S4_commutant_dim": cd_G,
                "S4_character_norm": str(cn_G),
                "S4_absolutely_irreducible": checks["S4_absolutely_irreducible"],
                "A4_commutant_dim": cd_A,
                "A4_character_norm": str(cn_A),
                "A4_absolutely_irreducible": checks["A4_absolutely_irreducible"],
            },
            "conclusion": {
                "no_S4_orbit_of_size_le_2_on_P2": no_small_orbit,
                "argument": (
                    "an S_4-stable pair {p,q} gives S_4 -> S_2; the kernel has "
                    "index 1 or 2, so it is S_4 or the unique index-2 subgroup "
                    "A_4; either way the line through p is an invariant "
                    "1-dimensional subspace, contradicting absolute "
                    "irreducibility"
                ),
                "consequence": (
                    "no smooth plane quartic -- no pencil member, and not the "
                    "Klein quartic -- carries an S_4-stable pair of points"
                ),
            },
            "premises_under_which_klein_is_excluded": {
                "H1": "one S_4-invariant non-separating cycle: exactly one node, giving an S_4-stable pair of preimages (the chapter's own g_arith=4 -> g_geom=3)",
                "H2": "S_4 acts faithfully on the normalization (the chapter's own 'S_4 survives')",
                "H3": "the normalization is non-hyperelliptic, so Aut acts through PGL_3 -- true of the Klein quartic",
            },
            "scope": (
                "scope-(b) STRUCTURAL EXCLUSION, licensed by a proved invariant "
                "(absolute irreducibility of the 3-dim rep of S_4 and of its "
                "restriction to A_4, each verified two independent ways: "
                "commutant dimension and character norm). Not a scope-(a) "
                "numerical negative."
            ),
            "not_excluded": [
                "hyperelliptic genus-3 targets (canonical map 2:1 onto a conic; "
                "e.g. y^2 = x^8 + 14x^4 + 1 with |Aut| = 48 containing S_4). "
                "Klein is not hyperelliptic, so this does not rescue it.",
                "pinches with several nodes, or of a separating cycle (violates H1)",
                "non-faithful actions on the normalization (violates H2, but then "
                "'S_4 survives' is false as stated)",
                "anything about the Bring surface itself -- this constrains the "
                "target, not the source",
            ],
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
