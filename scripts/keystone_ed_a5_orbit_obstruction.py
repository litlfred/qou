#!/usr/bin/env python3
"""Keystone ED ↔ S²(2,3,5) lead: the A₅-orbit obstruction.

Parameter-free, q₀-free structural check for the s5-so3 keystone
(docs/audits/2026-06-28-ed-a5-orbit-obstruction-rescope.md).

Claim under test: can the icosahedral group A₅ act on the exceptional
divisor ED ≅ ℂP¹ preserving its 6 branch points {ζ₅ᵏ : k=0..4} ∪ {∞}
(the corpus base divisor, hyperelliptic-quintic.md / brings-riemann-hurwitz.md)?

Result: NO. A point-stabiliser of any SO(3) action on S² = ℂP¹ is cyclic;
the cyclic subgroups of A₅ have orders only {1,2,3,5} (= the element
orders of A₅). Hence the orbit sizes are 60/{1,2,3,5} = {60,30,20,12}
— the classical 12 vertices / 20 faces / 30 edges / 60 generic. The
minimum nonzero orbit is 12 > 6, and every finite A₅-invariant subset of
ℂP¹ is a union of orbits, so NO A₅-invariant set has 6 points. The ED's
6-point branch divisor is therefore not A₅-invariant: A₅ is not a Möbius
symmetry of the marked ED. (The manifest marked symmetry is the cyclic
C₅ / ζ₅ pentagon.)

This refutes a *direct* "ED carries A₅ ⇒ ED/A₅ = S²(2,3,5)" identification.
It is a scope-limited negative (a): it does NOT exclude the icosahedral
connection, which runs through Klein's icosahedral–quintic correspondence
(the Bring radical), not a base action.
"""
from itertools import permutations
import math


def parity(p):
    s = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s ^= 1
    return s


def perm_order(p):
    n = len(p)
    visited = [False] * n
    o = 1
    for i in range(n):
        if not visited[i]:
            length, j = 0, i
            while not visited[j]:
                visited[j] = True
                j = p[j]
                length += 1
            o = o * length // math.gcd(o, length)
    return o


def main():
    A5 = [p for p in permutations(range(5)) if parity(p) == 0]
    assert len(A5) == 60, "A5 must have order 60"
    stab_orders = sorted({perm_order(p) for p in A5})          # cyclic-stabiliser orders
    orbit_sizes = sorted({60 // k for k in stab_orders})       # orbit-stabiliser
    print(f"|A5| = {len(A5)}")
    print(f"cyclic point-stabiliser orders (= element orders of A5): {stab_orders}")
    print(f"orbit sizes on S^2 = CP^1 (60/|stab|):                   {orbit_sizes}")
    n_branch = 6  # {zeta5^k : k=0..4} ∪ {∞}
    six_is_orbit = n_branch in orbit_sizes
    six_invariant_possible = n_branch >= min(orbit_sizes)      # union-of-orbits floor
    print(f"6 is an A5 orbit size? {six_is_orbit}")
    print(f"min nonzero orbit = {min(orbit_sizes)}; a finite A5-invariant set is a "
          f"union of orbits, so size 6 < {min(orbit_sizes)} is impossible.")
    assert not six_is_orbit and n_branch < min(orbit_sizes), \
        "expected: no A5-invariant set of size 6"
    print("VERDICT: the 6-point ED branch divisor {zeta5^k, ∞} is NOT A5-invariant — "
          "the direct ED↔S²(2,3,5) A5-action identification fails (scope-limited).")


if __name__ == "__main__":
    main()
