#!/usr/bin/env python3
"""Identify, exactly, which link each corpus deuteron braid word closes to.

Adjudication support for `qou-e5jf` (three inconsistent deuteron knot
assignments). The corpus disagreement is *not* primarily numerical: the
sites disagree about **which braid word is the canonical deuteron word**,
and the knot is then a *computation* from that word, not a choice. This
script performs that computation for every deuteron word live in the
corpus, so the fork can be adjudicated on derivation rather than on
agreement with `B_AME` (which is the forbidden inverted-CODATA ground).

Method — no SnapPy required (it is absent from this environment):

  * component count: exact cycle count of the permutation the braid
    induces (signs are irrelevant to the permutation);
  * writhe: exact integer sum of generator signs;
  * Alexander polynomial: the reduced Burau representation over
    Z[t, t^-1] via `sympy` exact rational functions, normalised by
    Birman, *Braids, Links and Mapping Class Groups*, Thm. 3.11:

        Delta(t) * (1 + t + ... + t^(n-1))  =  +- t^k * det(Burau_r(beta) - I)

  * determinant: |Delta(-1)|.

Everything is integer or symbolic. No float appears at any point, and
the script deliberately emits **no witness** -- it is a read-only
identification aid, not a producer.

The reference rows are the point of the exercise: they let a reader
check the machinery against words whose closures are textbook facts
(unknot, Hopf link, trefoil, figure-eight, 6_2) before trusting the
corpus rows underneath them.

  Ref: [manuscript] bean qou-e5jf; docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md
"""
from __future__ import annotations

import sympy as sp

t = sp.symbols("t")


def burau_reduced(word: list[int], n: int) -> sp.Matrix:
    """Reduced Burau matrix ((n-1) x (n-1)) of a braid word in B_n."""

    def gen(i: int) -> sp.Matrix:
        """Reduced Burau image of the POSITIVE generator sigma_i."""
        if n == 2:
            return sp.Matrix([[-t]])
        M = sp.eye(n - 1)
        if i == 1:
            M[0, 0] = -t
            M[0, 1] = 1
        elif i == n - 1:
            M[n - 2, n - 3] = t
            M[n - 2, n - 2] = -t
        else:
            M[i - 1, i - 2] = t
            M[i - 1, i - 1] = -t
            M[i - 1, i] = 1
        return M

    R = sp.eye(n - 1)
    for g in word:
        # sigma_i^-1 maps to the MATRIX INVERSE. Substituting t -> 1/t
        # instead is a different (wrong) map: it agrees with the inverse
        # only in B_2, and silently returns det 3 for the figure-eight
        # (correct value 5) and det 5 for 6_2 (correct value 11).
        M = gen(abs(g))
        R = R * (M.inv() if g < 0 else M)
    return sp.simplify(R)


def perm_cycles(word: list[int], n: int) -> int:
    """Number of components of the braid closure = cycles of the
    induced permutation. Generator signs do not affect it."""
    pi = list(range(n))
    for g in word:
        i = abs(g) - 1
        pi[i], pi[i + 1] = pi[i + 1], pi[i]
    seen = [False] * n
    cycles = 0
    for s in range(n):
        if not seen[s]:
            cycles += 1
            x = s
            while not seen[x]:
                seen[x] = True
                x = pi[x]
    return cycles


def analyse(word: list[int], n: int) -> dict:
    writhe = sum((g > 0) - (g < 0) for g in word)
    comps = perm_cycles(word, n)
    burau_det = sp.factor(sp.simplify(sp.det(burau_reduced(word, n) - sp.eye(n - 1))))
    cyclotomic = sum(t**k for k in range(n))
    alexander = sp.simplify(sp.cancel(burau_det / cyclotomic))
    determinant = sp.simplify(sp.Abs(alexander.subs(t, -1)))
    return {
        "word": word,
        "n_strands": n,
        "writhe": writhe,
        "components": comps,
        "burau_det": burau_det,
        "alexander": alexander,
        "determinant": determinant,
    }


# Textbook closures, used to validate the machinery before the corpus rows.
REFERENCE: list[tuple[str, list[int], int]] = [
    ("unknot        sigma_1                  in B_2", [1], 2),
    ("Hopf link     sigma_1^2                in B_2", [1, 1], 2),
    ("trefoil 3_1   sigma_1^3                in B_2", [1, 1, 1], 2),
    ("figure-8 4_1  (s1 s2^-1)^2             in B_3", [1, -2, 1, -2], 3),
    ("knot 6_2      s1^3 s2^-1 s1 s2^-1      in B_3", [1, 1, 1, -2, 1, -2], 3),
]

# Every deuteron braid word live in the corpus (see the audit doc for
# file:line provenance of each).
CORPUS: list[tuple[str, list[int], int]] = [
    ("deltalambda/deuteron-octahedral-gluing.witness.json  sigma_1^3", [1, 1, 1], 2),
    ("probes/he_nu_sdp_psd_count_test.py:63                 D word", [1, -2, 1, 1, 1, -2], 3),
    ("gb-filtration-jet-order-reader.witness.json:41        D word", [-1, 2, -1, 2, 2], 3),
]


def report(rows: list[tuple[str, list[int], int]], heading: str) -> None:
    print(f"\n=== {heading} ===")
    for label, word, n in rows:
        r = analyse(word, n)
        print(f"\n{label}")
        print(f"    word       = {word}   strands = {n}")
        print(f"    writhe     = {r['writhe']:+d}    components = {r['components']}")
        print(f"    Alexander  = {r['alexander']}")
        print(f"    |Delta(-1)| (determinant) = {r['determinant']}")


def main() -> int:
    report(REFERENCE, "REFERENCE (textbook closures -- validates the machinery)")
    report(CORPUS, "CORPUS deuteron words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
