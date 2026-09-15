#!/usr/bin/env python3
"""Which axioms on `S` constrain it, and which of those kill every model?

`QOU.FrobeniusHopfData.dichotomy_of_scalars_field` (Lean, sorry-free) shows the
CURRENT axiom set -- the convolution-inverse condition
`Delta >> (S |> A) >> mu = eps >> eta` -- has no non-trivial model over a field.
The live question is what to put in its place, and the candidates sit on a
spectrum between "no condition on S at all" and that one.

This probe measures the spectrum on the family that should be a model of any
honest answer: the group algebra `k[G]` with its FROBENIUS comultiplication.
For each group and each candidate `S`, it checks every axiom of
`def:frobenius-hopf-substrate` plus five candidate intermediates, and reports a
table.

The two numbers that decide the question are, for each axiom family:

  * does it ADMIT a non-trivial model?   (else the definition is empty)
  * does it PIN `S`?                     (else `S` is decoration, which is the
                                          defect PR #7369 was opened to fix)

STRUCTURES on `k[G]`, all standard:

    mu(g (x) h) = gh                 eta(1) = e
    lambda(sum a_g g) = a_e          eps = lambda
    Delta(x)    = sum_h xh (x) h^-1  coev(1) = sum_h h (x) h^-1
    ev          = lambda . mu

CANDIDATE ANTIPODES: `S = inv` (`g -> g^-1`, the group inverse -- the classical
antipode) and `S = id`, which is included precisely because it is the vacuous
answer: any axiom family that `S = id` satisfies is a family that does not pin
`S`.

COHERENCE: associators and unitors are suppressed.  In `Vect_k` with the chosen
bases the standard identifications make them identity maps, so an axiom's
element form is exactly its categorical form.  Nothing here depends on
strictness beyond that.

ARITHMETIC: exact.  Every coefficient is a Python `int`; there is no float in
this file -- not as an input, not as an intermediate, not in a comparison.  No
experimental value is touched, so there is no anchor and no q0 to pin.

Emits no witness: it records structural yes/no verdicts about axiom systems,
not a numeric quantity anything downstream re-derives.

Beans: `qou-aawz`, `qou-c64q`.  Audit:
docs/audits/2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md
"""

from __future__ import annotations

import sys
from itertools import permutations
from typing import Callable

# --------------------------------------------------------------------------
# Groups
# --------------------------------------------------------------------------


class Group:
    def __init__(self, name: str, elements, mul, identity, abelian: bool) -> None:
        self.name = name
        self.elements = list(elements)
        self.mul = mul
        self.e = identity
        self.abelian = abelian
        self.inv = {}
        for g in self.elements:
            found = [h for h in self.elements if mul(g, h) == identity]
            if len(found) != 1:
                raise ValueError(f"{name}: {g!r} has {len(found)} inverses")
            self.inv[g] = found[0]

    @property
    def order(self) -> int:
        return len(self.elements)


def cyclic(n: int) -> Group:
    return Group(f"Z/{n}", range(n), lambda a, b: (a + b) % n, 0, abelian=True)


def klein() -> Group:
    els = [(0, 0), (0, 1), (1, 0), (1, 1)]
    return Group("V_4", els, lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2),
                 (0, 0), abelian=True)


def symmetric3() -> Group:
    els = sorted(permutations(range(3)))
    return Group("S_3", els, lambda a, b: tuple(a[b[i]] for i in range(3)),
                 (0, 1, 2), abelian=False)


def dihedral4() -> Group:
    """D_4 as (r, s) with r in Z/4, s in Z/2, and s r s = r^-1."""
    els = [(r, s) for s in (0, 1) for r in range(4)]

    def mul(a, b):
        ra, sa = a
        rb, sb = b
        # (r_a s_a)(r_b s_b): move s_a past r_b, inverting r_b when s_a = 1
        r = (ra + (rb if sa == 0 else -rb)) % 4
        return (r, (sa + sb) % 2)

    return Group("D_4", els, mul, (0, 0), abelian=False)


# --------------------------------------------------------------------------
# Linear algebra over the group basis, exact integer coefficients
# --------------------------------------------------------------------------


def add_into(acc: dict, key, coeff: int) -> None:
    acc[key] = acc.get(key, 0) + coeff
    if acc[key] == 0:
        del acc[key]


def eq(a: dict, b: dict) -> bool:
    return {k: v for k, v in a.items() if v != 0} == {k: v for k, v in b.items() if v != 0}


class GroupAlgebra:
    """`k[G]` with its Frobenius comultiplication and a chosen `S`."""

    def __init__(self, G: Group, S: Callable) -> None:
        self.G = G
        self.S = S

    # -- structure maps, each on a basis element, returning a linear combination

    def mu(self, g, h) -> dict:
        return {self.G.mul(g, h): 1}

    def eta(self) -> dict:
        return {self.G.e: 1}

    def eps(self, g) -> int:
        return 1 if g == self.G.e else 0

    def delta(self, x) -> dict:
        out: dict = {}
        for h in self.G.elements:
            add_into(out, (self.G.mul(x, h), self.G.inv[h]), 1)
        return out

    def coev(self) -> dict:
        out: dict = {}
        for h in self.G.elements:
            add_into(out, (h, self.G.inv[h]), 1)
        return out

    def ev(self, g, h) -> int:
        return self.eps(self.G.mul(g, h))

    def s(self, g) -> dict:
        return {self.S(self.G, g): 1}


# --------------------------------------------------------------------------
# The axioms, each `A -> bool`, checked on every basis element
# --------------------------------------------------------------------------


def ax_mul_assoc(A: GroupAlgebra) -> bool:
    G = A.G
    return all(G.mul(G.mul(x, y), z) == G.mul(x, G.mul(y, z))
               for x in G.elements for y in G.elements for z in G.elements)


def ax_unit_laws(A: GroupAlgebra) -> bool:
    G = A.G
    return all(G.mul(G.e, x) == x and G.mul(x, G.e) == x for x in G.elements)


def ax_counit_laws(A: GroupAlgebra) -> bool:
    """`(eps (x) id) Delta = id` and `(id (x) eps) Delta = id`."""
    for x in A.G.elements:
        left: dict = {}
        right: dict = {}
        for (a, b), c in A.delta(x).items():
            if A.eps(a):
                add_into(left, b, c * A.eps(a))
            if A.eps(b):
                add_into(right, a, c * A.eps(b))
        if not eq(left, {x: 1}) or not eq(right, {x: 1}):
            return False
    return True


def ax_comul_assoc(A: GroupAlgebra) -> bool:
    """`(Delta (x) id) Delta = (id (x) Delta) Delta`."""
    for x in A.G.elements:
        lhs: dict = {}
        rhs: dict = {}
        for (a, b), c in A.delta(x).items():
            for (a1, a2), c2 in A.delta(a).items():
                add_into(lhs, (a1, a2, b), c * c2)
            for (b1, b2), c2 in A.delta(b).items():
                add_into(rhs, (a, b1, b2), c * c2)
        if not eq(lhs, rhs):
            return False
    return True


def ax_frobenius(A: GroupAlgebra) -> bool:
    """Both Frobenius conditions: `Delta(xy) = (Delta x)(1 (x) y) = (x (x) 1)(Delta y)`."""
    G = A.G
    for x in G.elements:
        for y in G.elements:
            target = A.delta(G.mul(x, y))

            left: dict = {}
            for (a, b), c in A.delta(x).items():
                add_into(left, (a, G.mul(b, y)), c)

            right: dict = {}
            for (a, b), c in A.delta(y).items():
                add_into(right, (G.mul(x, a), b), c)

            if not eq(left, target) or not eq(right, target):
                return False
    return True


def ax_snake(A: GroupAlgebra) -> bool:
    """`(id (x) ev)(coev (x) id) = id` and its mirror."""
    G = A.G
    for x in G.elements:
        left: dict = {}
        right: dict = {}
        for (a, b), c in A.coev().items():
            # (id (x) ev)(coev (x) id) : x -> sum a . ev(b, x)
            if A.ev(b, x):
                add_into(left, a, c * A.ev(b, x))
            # (ev (x) id)(id (x) coev) : x -> sum ev(x, a) . b
            if A.ev(x, a):
                add_into(right, b, c * A.ev(x, a))
        if not eq(left, {x: 1}) or not eq(right, {x: 1}):
            return False
    return True


def ax_antipode(A: GroupAlgebra) -> bool:
    """THE CURRENT AXIOM: `sum S(x_1) x_2 = eps(x) . 1`, and its mirror."""
    for x in A.G.elements:
        left: dict = {}
        right: dict = {}
        for (a, b), c in A.delta(x).items():
            for sa, cs in A.s(a).items():
                add_into(left, A.G.mul(sa, b), c * cs)
            for sb, cs in A.s(b).items():
                add_into(right, A.G.mul(a, sb), c * cs)
        target = {A.G.e: A.eps(x)} if A.eps(x) else {}
        if not eq(left, target) or not eq(right, target):
            return False
    return True


def ax_anti_algebra(A: GroupAlgebra) -> bool:
    """`S(xy) = S(y) S(x)` and `S(1) = 1`."""
    G = A.G
    if not eq(A.s(G.e), {G.e: 1}):
        return False
    for x in G.elements:
        for y in G.elements:
            lhs = A.s(G.mul(x, y))
            rhs: dict = {}
            for sy, c1 in A.s(y).items():
                for sx, c2 in A.s(x).items():
                    add_into(rhs, G.mul(sy, sx), c1 * c2)
            if not eq(lhs, rhs):
                return False
    return True


def ax_anti_coalgebra(A: GroupAlgebra) -> bool:
    """`Delta(S x) = sum S(x_2) (x) S(x_1)` and `eps . S = eps`."""
    for x in A.G.elements:
        for sx, cs in A.s(x).items():
            if A.eps(sx) != A.eps(x):
                return False
        lhs: dict = {}
        for sx, cs in A.s(x).items():
            for k, c in A.delta(sx).items():
                add_into(lhs, k, cs * c)
        rhs: dict = {}
        for (a, b), c in A.delta(x).items():
            for sb, c1 in A.s(b).items():
                for sa, c2 in A.s(a).items():
                    add_into(rhs, (sb, sa), c * c1 * c2)
        if not eq(lhs, rhs):
            return False
    return True


def ax_involutive(A: GroupAlgebra) -> bool:
    """`S . S = id`."""
    for x in A.G.elements:
        out: dict = {}
        for sx, c in A.s(x).items():
            for ssx, c2 in A.s(sx).items():
                add_into(out, ssx, c * c2)
        if not eq(out, {x: 1}):
            return False
    return True


def ax_form_invariant(A: GroupAlgebra) -> bool:
    """`lambda . S = lambda` -- the Frobenius form is `S`-invariant."""
    return all(
        sum(c * A.eps(sx) for sx, c in A.s(x).items()) == A.eps(x)
        for x in A.G.elements
    )


STRUCTURE_AXIOMS = [
    ("mul_assoc", ax_mul_assoc),
    ("unit laws", ax_unit_laws),
    ("counit laws", ax_counit_laws),
    ("comul_assoc", ax_comul_assoc),
    ("frobenius", ax_frobenius),
    ("snake", ax_snake),
]

S_AXIOMS = [
    ("antipode (CURRENT)", ax_antipode),
    ("anti-algebra", ax_anti_algebra),
    ("anti-coalgebra", ax_anti_coalgebra),
    ("S^2 = id", ax_involutive),
    ("lambda o S = lambda", ax_form_invariant),
]


# --------------------------------------------------------------------------


def main() -> int:
    groups = [cyclic(1), cyclic(2), cyclic(3), cyclic(4), klein(), symmetric3(), dihedral4()]
    candidates = [
        ("S = inv (g -> g^-1)", lambda G, g: G.inv[g]),
        ("S = id  (the VACUOUS one)", lambda G, g: g),
    ]

    print("Which axioms on S admit a non-trivial model, and which pin S?")
    print("=" * 78)
    print()
    print("Family: k[G] with the FROBENIUS comultiplication Delta(x) = sum_h xh (x) h^-1.")
    print("`S = id` is included because it is the vacuous answer: any family it")
    print("satisfies is a family that does NOT pin S.")
    print()

    # The structure axioms must hold regardless of S -- check once per group.
    print("Structure axioms (independent of S):")
    struct_ok = True
    for G in groups:
        A = GroupAlgebra(G, lambda GG, g: GG.inv[g])
        results = [(nm, fn(A)) for nm, fn in STRUCTURE_AXIOMS]
        bad = [nm for nm, ok in results if not ok]
        flag = "all hold" if not bad else f"FAIL: {', '.join(bad)}"
        print(f"  {G.name:>5}  |G| = {G.order:<2}  {flag}")
        struct_ok = struct_ok and not bad
    print()
    if not struct_ok:
        print("A structure axiom failed -- k[G] is not a Frobenius object as set up here.")
        print("The rest of this probe would be meaningless. Stop.")
        return 1

    header = f"{'group':>5} {'|G|':>3}  {'S':<28}" + "".join(
        f"{nm:>22}" for nm, _ in S_AXIOMS)
    print(header)
    print("-" * len(header))

    table: dict = {}
    for G in groups:
        for label, S in candidates:
            A = GroupAlgebra(G, S)
            row = [fn(A) for _, fn in S_AXIOMS]
            table[(G.name, label)] = row
            cells = "".join(f"{('hold' if r else 'FAIL'):>22}" for r in row)
            print(f"{G.name:>5} {G.order:>3}  {label:<28}{cells}")
        print()

    # ---- the two questions that decide the design ----
    print("=" * 78)
    print("READING")
    print()

    nontrivial = [G for G in groups if G.order > 1]

    # 1. Does each family admit a non-trivial model (with either candidate S)?
    print("(1) ADMITS a non-trivial model?  (some S works for some |G| > 1)")
    for i, (nm, _) in enumerate(S_AXIOMS):
        ok = any(table[(G.name, lbl)][i] for G in nontrivial for lbl, _ in candidates)
        print(f"      {nm:<22} {'YES' if ok else 'NO -- every model is trivial'}")
    print()

    # 2. Does each family exclude the vacuous S = id?
    print("(2) PINS S?  (does the family EXCLUDE the vacuous S = id?)")
    for i, (nm, _) in enumerate(S_AXIOMS):
        id_ok_abelian = [G.name for G in nontrivial
                         if G.abelian and table[(G.name, "S = id  (the VACUOUS one)")][i]]
        id_ok_nonab = [G.name for G in nontrivial
                       if not G.abelian and table[(G.name, "S = id  (the VACUOUS one)")][i]]
        if not id_ok_abelian and not id_ok_nonab:
            verdict = "excludes S = id everywhere"
        elif id_ok_nonab:
            verdict = f"S = id survives even non-abelian ({', '.join(id_ok_nonab)}) -- pins nothing"
        else:
            verdict = f"S = id survives on abelian ({', '.join(id_ok_abelian)}) only"
        print(f"      {nm:<22} {verdict}")
    print()

    print("The design tension, if the table shows what it should: the ONLY family")
    print("that excludes S = id everywhere is the convolution antipode axiom, and it")
    print("is the only one with no non-trivial model. Everything weaker admits k[G]")
    print("and leaves S under-determined on abelian groups.")
    print()

    # ---- the adopted axiom set, as a single verdict ----
    print("=" * 78)
    print("THE ADOPTED AXIOM SET (2026-09-15), AS A UNIT")
    print()
    print("`def:frobenius-hopf-substrate` axiom 2 now asks for all six at once:")
    print("  anti-algebra + anti-coalgebra + S(1)=1 + eps.S=eps + S^2=id + lambda.S=lambda")
    print("The claim the change rests on is that k[G] with S(g) = g^-1 IS a model.")
    print("This is that claim, as one yes/no per group:")
    print()

    ADOPTED = [ax_anti_algebra, ax_anti_coalgebra, ax_involutive, ax_form_invariant]
    bad_model = []
    for G in groups:
        row = []
        for label, S in candidates:
            A = GroupAlgebra(G, S)
            struct = all(fn(A) for _, fn in STRUCTURE_AXIOMS)
            adopted = all(fn(A) for fn in ADOPTED)
            row.append((label, struct and adopted))
        inv_ok = row[0][1]
        id_ok = row[1][1]
        # what we require: S = inv is always a model; S = id is EXCLUDED on
        # non-abelian groups (that is the whole point of the anti-algebra law).
        want_id = G.abelian
        verdict = "OK" if (inv_ok and id_ok == want_id) else "MISMATCH"
        if verdict != "OK":
            bad_model.append(G.name)
        print(f"  {G.name:>5}  |G| = {G.order:<2}  "
              f"S = inv: {'MODEL' if inv_ok else 'not a model':<12}"
              f"S = id: {'model' if id_ok else 'EXCLUDED':<12}{verdict}")

    print()
    if bad_model:
        print(f"MISMATCH on: {', '.join(bad_model)} -- the adopted axiom set does NOT")
        print("behave as the change assumes. This is a falsification, not a nit.")
        return 1

    print("Every group: k[G] with the classical antipode IS a model, and the vacuous")
    print("S = id is EXCLUDED exactly on the non-abelian ones. That is the trade the")
    print("change accepts -- S is constrained, not determined. On a commutative A the")
    print("axioms cannot tell S = id from anything else, and nothing here hides that.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
