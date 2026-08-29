#!/usr/bin/env python3
"""Does the S_4 bridge single out the Klein quartic?  NO. (bean qou-8pl1)

The eightfold-way chapter's colour route argues:

    Bring Sigma_4 (genus 4, Aut = S_5)
      --pinch an S_4-invariant cycle-->  nodal, geometric genus 3
      --normalize-->                    Klein quartic (genus 3, Aut = PSL(2,7))

with the selection step justified by: "S_4 survives the pinch, S_4 embeds in
PSL(2,7) as a point stabilizer, and the Hurwitz bound caps genus-3
automorphism groups at 168 = 84(3-1), so PSL(2,7) is the unique maximal
option."

That argument was already withdrawn as invalid (an upper bound is not a
selection principle).  This script establishes the stronger, concrete negative:

    THERE IS ANOTHER GENUS-3 CURVE ADMITTING S_4.

Namely the **Fermat quartic** F : x^4 + y^4 + z^4 = 0.  Genus
(4-1)(4-2)/2 = 3, and Aut(F) has order 96 with S_4 as a subgroup.  So even a
*correct* argument that "the normalization has genus 3 and inherits S_4" would
not reach the Klein quartic: S_4 does not distinguish the two.

What we verify explicitly, by constructing the groups as concrete matrix
groups over Q(i) acting on P^2:

  1. Aut(Fermat quartic) contains the group  D = (mu_4)^3 / mu_4  of coordinate
     scalings by 4th roots of unity (order 16), semidirect the coordinate
     permutations S_3 (order 6) -- order 96 in total.  Each element is checked
     to genuinely preserve x^4 + y^4 + z^4.
  2. That group contains a subgroup isomorphic to S_4, exhibited concretely as
     V_4 : S_3 where V_4 is the 2-torsion sign-flip subgroup
     {(x,y,z) -> (+-x,+-y,+-z)} / scalars and S_3 permutes coordinates.
     Isomorphism to S_4 is verified by checking the induced action on the three
     nontrivial elements of V_4 is the full S_3, plus order and structure.
  3. The Fermat quartic is NOT the Klein quartic: |Aut| = 96 != 168.

Conclusion: `S_4 embeds in Aut` is satisfied by at least two distinct genus-3
curves, so it cannot be the selection principle.  Identifying the normalization
requires an invariant that separates them -- see the sub-beans on qou-8pl1.

Exact arithmetic only: coefficients live in Z[i], no floating point anywhere.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "s4-genus3-competitor-fermat.witness.json"


# ---------------------------------------------------------------------------
# Exact Z[i] arithmetic (a + b*i), enough for 4th roots of unity.
# ---------------------------------------------------------------------------
class Zi:
    __slots__ = ("a", "b")

    def __init__(self, a: int, b: int = 0) -> None:
        self.a, self.b = a, b

    def __mul__(self, o: "Zi") -> "Zi":
        return Zi(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def __pow__(self, n: int) -> "Zi":
        r = Zi(1, 0)
        for _ in range(n):
            r = r * self
        return r

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Zi) and (self.a, self.b) == (o.a, o.b)

    def __hash__(self) -> int:
        return hash((self.a, self.b))

    def __repr__(self) -> str:
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"{self.b}i" if self.b != 1 else "i"
        return f"({self.a}{'+' if self.b > 0 else '-'}{abs(self.b)}i)"


ONE, I_, M1, MI = Zi(1, 0), Zi(0, 1), Zi(-1, 0), Zi(0, -1)
MU4 = [ONE, I_, M1, MI]  # 4th roots of unity


# ---------------------------------------------------------------------------
# Group elements: (scal, perm) acting on (x,y,z) as
#   x_j  ->  scal[j] * x_{perm(j)}
# taken modulo overall scalar (projective).
# ---------------------------------------------------------------------------
def normalize(scal, perm):
    """Kill the overall-scalar ambiguity: divide by the first coordinate's
    scaling, so scal[0] == 1 in every canonical representative."""
    inv = {ONE: ONE, I_: MI, M1: M1, MI: I_}[scal[0]]
    return (tuple(inv * s for s in scal), perm)


def compose(g, h):
    """g after h."""
    (sg, pg), (sh, ph) = g, h
    perm = tuple(pg[ph[j]] for j in range(3))
    scal = tuple(sg[ph[j]] * sh[j] for j in range(3))
    return normalize(scal, perm)


def preserves_fermat(g) -> bool:
    """x^4+y^4+z^4 is preserved iff every scaling enters as a 4th power = 1.

    Substituting x_j -> s_j * x_{p(j)} sends the form to
    sum_j s_j^4 * x_{p(j)}^4 = sum_j x_{p(j)}^4 (since s_j^4 = 1 for
    s_j in mu_4), which is the same form since p is a permutation."""
    scal, _ = g
    return all(s ** 4 == ONE for s in scal)


def build_fermat_group():
    S3 = list(itertools.permutations(range(3)))
    els = set()
    for perm in S3:
        for scal in itertools.product(MU4, repeat=3):
            g = normalize(scal, perm)
            assert preserves_fermat(g), f"non-preserving element {g}"
            els.add(g)
    return els


def subgroup_generated(gens, universe):
    cur = {normalize((ONE, ONE, ONE), (0, 1, 2))}
    frontier = list(cur)
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                x = compose(g, h)
                assert x in universe, "escaped the ambient group"
                if x not in cur:
                    cur.add(x)
                    new.append(x)
        frontier = new
    return cur


def element_order(g, ident):
    n, x = 1, g
    while x != ident:
        x = compose(x, g)
        n += 1
        if n > 200:
            raise RuntimeError("order blew up")
    return n


def main() -> int:
    ident = normalize((ONE, ONE, ONE), (0, 1, 2))
    G = build_fermat_group()
    print("=" * 74)
    print("1. Aut(Fermat quartic) as a concrete matrix group over Z[i]")
    print("=" * 74)
    print(f"  |G| = {len(G)}   (expected 96 = 16 * 6)")
    print("  every element verified to preserve x^4 + y^4 + z^4")

    # V_4 : the 2-torsion sign-flip subgroup, modulo scalars.
    v4_gens = [
        normalize((ONE, M1, M1), (0, 1, 2)),  # (x, -y, -z)
        normalize((M1, ONE, M1), (0, 1, 2)),  # (-x, y, -z)
    ]
    V4 = subgroup_generated(v4_gens, G)
    # S_3 : coordinate permutations, no scaling.
    s3_gens = [
        normalize((ONE, ONE, ONE), (1, 0, 2)),  # swap x,y
        normalize((ONE, ONE, ONE), (1, 2, 0)),  # 3-cycle
    ]
    S3sub = subgroup_generated(s3_gens, G)
    S4 = subgroup_generated(v4_gens + s3_gens, G)

    print()
    print("=" * 74)
    print("2. S_4 as a subgroup: V_4 : S_3")
    print("=" * 74)
    print(f"  |V_4| = {len(V4)}      (sign flips mod scalars)")
    print(f"  |S_3| = {len(S3sub)}      (coordinate permutations)")
    print(f"  |<V_4, S_3>| = {len(S4)}  (expected 24 = |S_4|)")

    # Structural checks that pin the isomorphism type to S_4 (not the other
    # order-24 groups: Z/24, Z/12xZ/2, D_12, Dic_3, A_4xZ/2, Z/3:Z/8).
    orders = {}
    for g in S4:
        o = element_order(g, ident)
        orders[o] = orders.get(o, 0) + 1
    print(f"  element-order profile: {dict(sorted(orders.items()))}")
    s4_profile = {1: 1, 2: 9, 3: 8, 4: 6}
    is_s4_profile = dict(sorted(orders.items())) == s4_profile
    print(f"  matches S_4 profile {s4_profile}: {is_s4_profile}")

    # V_4 normal in S_4, and S_3 acts on its 3 nontrivial elements as full S_3.
    v4_nontrivial = [g for g in V4 if g != ident]
    normal = all(
        compose(compose(h, n), inverse(h, ident, G)) in V4
        for h in S4
        for n in V4
    )
    induced = set()
    for h in S3sub:
        img = tuple(
            sorted(
                v4_nontrivial.index(compose(compose(h, n), inverse(h, ident, G)))
                for n in v4_nontrivial
            )
        )
        perm = tuple(
            v4_nontrivial.index(compose(compose(h, n), inverse(h, ident, G)))
            for n in v4_nontrivial
        )
        induced.add(perm)
    print(f"  V_4 normal in <V_4,S_3>: {normal}")
    print(f"  S_3 induces {len(induced)} distinct permutations of V_4\\{{1}} "
          f"(expected 6 = |S_3|, i.e. the FULL symmetric action)")

    is_s4 = len(S4) == 24 and is_s4_profile and normal and len(induced) == 6

    print()
    print("=" * 74)
    print("3. The Fermat quartic is NOT the Klein quartic")
    print("=" * 74)
    print(f"  |Aut(Fermat)| = {len(G)}")
    print("  |Aut(Klein)|  = 168   (= 84*(3-1), the Hurwitz bound)")
    print(f"  equal? {len(G) == 168}")
    print("  genus(Fermat quartic) = (4-1)(4-2)/2 = 3   [smooth plane quartic]")
    print("  genus(Klein quartic)  = 3                  [smooth plane quartic]")

    print()
    print("=" * 74)
    print("VERDICT (bean qou-8pl1)")
    print("=" * 74)
    print("  Two DISTINCT genus-3 curves both admit S_4 in their automorphism")
    print("  group: the Klein quartic (|Aut| = 168) and the Fermat quartic")
    print("  (|Aut| = 96). Therefore:")
    print()
    print("    'S_4 survives the pinch and S_4 embeds in PSL(2,7)'")
    print("     does NOT select the Klein quartic.")
    print()
    print("  This is stronger than the already-withdrawn Hurwitz-bound error.")
    print("  That error was that an upper bound is not a selection principle.")
    print("  This is that the S_4 datum ITSELF has no separating power: even a")
    print("  fully correct 'genus 3, inherits S_4' argument stops short of the")
    print("  Klein quartic, because at least one other genus-3 curve satisfies")
    print("  both conditions.")
    print()
    print("  Scope-(a): the Bring -> Klein degeneration is NOT refuted. What is")
    print("  refuted is the S_4 bridge as an argument FOR it. Settling the")
    print("  conjecture needs an invariant that separates Klein from Fermat")
    print("  (and from any other S_4-admitting genus-3 curve) -- period matrix,")
    print("  defining equation, or the full automorphism group of the actual")
    print("  normalization. See the qou-8pl1 sub-beans.")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The S_4 bridge does not single out the Klein quartic: the Fermat "
            "quartic is a second genus-3 curve admitting S_4. Bean qou-8pl1."
        ),
        "computation": {
            "script": "computations/s4_genus3_competitor_fermat.py",
            "arithmetic": "exact Z[i]; no floating point",
        },
        "data": {
            "fermat_quartic": {
                "equation": "x^4 + y^4 + z^4 = 0",
                "genus": 3,
                "aut_order": len(G),
                "aut_structure": "(mu_4)^3/mu_4 : S_3  =  (Z/4)^2 : S_3",
                "contains_S4": is_s4,
                "s4_order": len(S4),
                "s4_element_order_profile": {str(k): v for k, v in sorted(orders.items())},
                "v4_normal": normal,
                "s3_induces_full_symmetric_action_on_V4": len(induced) == 6,
            },
            "klein_quartic": {
                "equation": "x^3 y + y^3 z + z^3 x = 0",
                "genus": 3,
                "aut_order": 168,
                "aut_structure": "PSL(2,7)",
                "contains_S4": True,
                "note": "S_4 is the point stabilizer of the action on the 7 Fano points",
            },
            "verdict": (
                "S_4 embeds in the automorphism group of BOTH genus-3 curves, so "
                "the S_4 bridge cannot select the Klein quartic."
            ),
            "scope": (
                "scope-(a). Refutes the S_4 bridge AS AN ARGUMENT for the "
                "Bring->Klein degeneration. Does NOT refute the degeneration "
                "itself, which remains open and requires a separating invariant."
            ),
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
    print(f"\nwrote {_OUT.name}")
    return 0 if is_s4 else 1


def inverse(g, ident, universe):
    for h in universe:
        if compose(g, h) == ident:
            return h
    raise RuntimeError("no inverse found")


if __name__ == "__main__":
    raise SystemExit(main())
