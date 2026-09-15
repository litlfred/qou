#!/usr/bin/env python3
"""Confirm the model dichotomy on the one family anyone would try: k[G].

`QOU.FrobeniusHopfData.dichotomy_of_scalars_field` (Lean, sorry-free) says that
in a preadditive monoidal category whose scalars form a field, every model of
`def:frobenius-hopf-substrate` has `A` a zero object or a retract of the tensor
unit.  Over `ModuleCat k` that means `dim A <= 1`.

The prediction this probe tests is the *sharp* one, and it is falsifiable: for
`|G| > 1` there must exist **no** linear map `S' : k[G] -> k[G]` satisfying the
left antipode axiom against the FROBENIUS comultiplication.  Not "the standard
antipode `g -> g^-1` happens to fail" -- no map at all.

So this does not test `g -> g^-1`.  It solves the whole linear system for `S'`
and reports whether it is consistent.

Setup, all standard:

    lambda(sum a_g g) = a_e                 Frobenius form, taken as the counit
    Delta(1)          = sum_h h (x) h^-1    the Frobenius (dual-basis) comultiplication
    Delta(x)          = (x (x) 1) Delta(1)  since Delta is a map of A-bimodules
                      = sum_h xh (x) h^-1

The left antipode axiom `Delta >> (S' |> A) >> mu = eps >> eta` reads, on the
basis element `g`,

    sum_h S'(gh) . h^-1  =  delta_{g,e} . e

Writing `S'(k) = sum_j M[k][j] j` and collecting the coefficient of the basis
element `m` turns that into a square linear system in the |G|^2 unknowns M:

    for all g, m:   sum_h M[gh][m h]  =  delta_{g,e} . delta_{m,e}

which this probe solves exactly over Q by fraction-free Gaussian elimination.

ARITHMETIC: exact throughout.  Group-algebra coefficients are integers and the
elimination runs in `fractions.Fraction`.  There is no float anywhere in this
file -- not as an input, not as an intermediate, not in a comparison.  Nothing
here is measured against an experimental value, so there is no anchor and no
q0 to pin.

Emits no witness: it records a structural yes/no about a linear system, not a
numeric quantity that anything downstream re-derives.

Beans: `qou-aawz` (is there a non-trivial FrobeniusHopfData?), `qou-c64q`.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from typing import Callable


# --------------------------------------------------------------------------
# Finite groups, as (elements, multiply, inverse, identity)
# --------------------------------------------------------------------------


class Group:
    """A finite group given by its multiplication table."""

    def __init__(self, name: str, elements: list, mul: Callable, identity) -> None:
        self.name = name
        self.elements = list(elements)
        self.mul = mul
        self.identity = identity
        self.index = {g: i for i, g in enumerate(self.elements)}
        # Derive inverses from the table rather than trusting a formula.
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
    return Group(f"Z/{n}", list(range(n)), lambda a, b: (a + b) % n, 0)


def symmetric3() -> Group:
    """S_3 as permutations of (0,1,2), written as tuples."""
    from itertools import permutations

    els = sorted(permutations(range(3)))

    def mul(a, b):
        # (a*b)(i) = a(b(i))
        return tuple(a[b[i]] for i in range(3))

    return Group("S_3", els, mul, (0, 1, 2))


# --------------------------------------------------------------------------
# The linear system
# --------------------------------------------------------------------------


def antipode_system(G: Group) -> tuple[list[list[Fraction]], list[Fraction]]:
    """Build the |G|^2 x |G|^2 system `sum_h M[gh][m h] = delta_{g,e} delta_{m,e}`.

    Unknowns are indexed `(k, j) -> k * |G| + j`, meaning the coefficient of the
    basis element `j` in `S'(k)`.
    """
    n = G.order
    idx = G.index
    dim = n * n
    rows: list[list[Fraction]] = []
    rhs: list[Fraction] = []

    for g in G.elements:
        for m in G.elements:
            row = [Fraction(0)] * dim
            for h in G.elements:
                k = G.mul(g, h)          # S' is evaluated at g*h
                j = G.mul(m, h)          # and contributes to the coefficient of m
                row[idx[k] * n + idx[j]] += Fraction(1)
            rows.append(row)
            target = Fraction(1) if (g == G.identity and m == G.identity) else Fraction(0)
            rhs.append(target)

    return rows, rhs


def is_consistent(rows: list[list[Fraction]], rhs: list[Fraction]) -> bool:
    """Exact Gaussian elimination; returns whether the system has a solution."""
    a = [row[:] + [rhs[i]] for i, row in enumerate(rows)]
    nrows = len(a)
    ncols = len(rows[0]) if rows else 0

    pivot_row = 0
    for col in range(ncols):
        pivot = None
        for r in range(pivot_row, nrows):
            if a[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = Fraction(1) / a[pivot_row][col]
        a[pivot_row] = [x * inv for x in a[pivot_row]]
        for r in range(nrows):
            if r != pivot_row and a[r][col] != 0:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrows:
            break

    # Inconsistent iff some row is all-zero in the coefficients with nonzero rhs.
    for r in range(nrows):
        if all(x == 0 for x in a[r][:ncols]) and a[r][ncols] != 0:
            return False
    return True


def standard_antipode_convolution_at_one(G: Group) -> dict:
    """`(S * id)(1) = sum_h S(h) . h^-1` for the standard `S(g) = g^-1`.

    Returns the element as a coefficient dict over the group, so the report can
    show WHY the standard antipode fails, not merely that it does.
    """
    coeffs: dict = {}
    for h in G.elements:
        # S(h) . h^-1 = h^-1 . h^-1 = (h^-1)^2
        hi = G.inv[h]
        prod = G.mul(hi, hi)
        coeffs[prod] = coeffs.get(prod, 0) + 1
    return {k: v for k, v in coeffs.items() if v != 0}


# --------------------------------------------------------------------------


def main() -> int:
    groups = [cyclic(1), cyclic(2), cyclic(3), cyclic(4), symmetric3()]

    print("Frobenius-Hopf model dichotomy -- the k[G] family")
    print("=" * 72)
    print()
    print("Lean prediction (dichotomy_of_scalars_field, sorry-free):")
    print("  over a field, a FrobeniusHopfData has dim A <= 1, so for |G| > 1")
    print("  the left antipode axiom must be UNSATISFIABLE by any linear S'.")
    print()

    failures = []
    for G in groups:
        rows, rhs = antipode_system(G)
        consistent = is_consistent(rows, rhs)
        expected = G.order == 1
        verdict = "OK" if consistent == expected else "MISMATCH"
        if consistent != expected:
            failures.append(G.name)

        std = standard_antipode_convolution_at_one(G)
        std_str = " + ".join(
            f"{c}*{g!r}" if c != 1 else f"{g!r}" for g, c in sorted(std.items(), key=repr)
        )
        target = f"{G.identity!r}"

        print(f"{G.name:>6}  |G| = {G.order:<2}  "
              f"system {'CONSISTENT' if consistent else 'INCONSISTENT':<12} "
              f"expected {'CONSISTENT' if expected else 'INCONSISTENT':<12} {verdict}")
        print(f"         standard S(g)=g^-1:  (S*id)(1) = {std_str}")
        print(f"         must equal eps(1).1 = {target}"
              f"   -> {'holds' if std == {G.identity: 1} else 'FAILS'}")
        print()

    print("=" * 72)
    if failures:
        print(f"MISMATCH on: {', '.join(failures)} -- the Lean prediction is CONTRADICTED.")
        return 1

    print("All groups agree with the Lean dichotomy.")
    print()
    print("Reading: for every |G| > 1 the antipode axiom is unsatisfiable by ANY")
    print("linear map, not merely by the standard antipode -- which is the strong")
    print("form of the prediction. k[G] is a Frobenius algebra and a Hopf algebra")
    print("and is still not a FrobeniusHopfData, because axiom 3 pins Delta to the")
    print("Frobenius comultiplication and axiom 2 then demands an antipode against")
    print("that Delta rather than against the Hopf one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
