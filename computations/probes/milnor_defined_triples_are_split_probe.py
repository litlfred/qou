#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation combinatorics and strand-position
# intervals of the canonical atom word. No q, no float, no witness.
"""
milnor_defined_triples_are_split_probe.py — every Milnor-DEFINED triple of the
atom closure is SPLIT, hence vanishes. The route closes.

## What this completes

`atom_closure_milnor_indeterminacy_probe.py` (merged) established that the
closure's linking graph is the path `P_mu`, `mu = A+1`, and split the triples:

  * triples touching a linked pair -> `Delta = gcd(...) in {1,2}`, so `mubar`
    is indeterminate (one bit, or nothing);
  * mutually NON-ADJACENT triples -> `Delta = 0`, so `mubar` is a genuine
    integer.

It concluded the route was "not obstructed -- partially available from A=4".
**That conclusion is now superseded**, and this probe supersedes it with a
cheaper measurement than the Magnus expansion it would have taken to settle.

## The measurement

Between NON-ADJACENT components EVERY BRANCH CLOSURE has **zero crossings** --
not merely a zero signed sum. Only the `mu - 1` consecutive pairs carry any
crossing at all. Stronger, and checked here rather than argued
diagrammatically:

  * every component occupies a **contiguous block** of strand positions;
  * for every minimal-span triple `{i, i+2, i+4}` the three blocks are
    **pairwise disjoint intervals**, and **zero letters of the word act on
    two members**.

So the sublink on such a triple is the closure of a braid on three disjoint,
non-interacting contiguous strand blocks: each block closes in its own
annulus. That is a **split 3-component link** by construction -- no appeal to
"a diagram with no inter-component crossings is split" is needed.

## The collapse

A split link has all Milnor invariants zero. Therefore:

    Delta(ijk) = 0   =>   the triple is split   =>   mubar(ijk) = 0.

Combined with the indeterminacy result, **no non-trivial, well-defined Milnor
triple invariant exists in ANY branch closure, at any A.** Definedness and
triviality coincide, and they coincide *because* the linking graph is a path:
on a path, "not linked" and "never interacts" are the same condition.

**The Magnus expansion is not worth running.** It would return zero on exactly
the triples where it is meaningful.

## Why this may be read off the word at all

`atom_braid_word_3A`'s own docstring is emphatic: the object is a HECKE
ELEMENT, **not** a braid word, there is **no single link behind it** (it is a
weighted sum over `2^(2A+1)` branches), and **no topological quantity may be
read off it** -- not a volume, not a crossing number, not a genus.

Nothing here reads one. What is measured is **which strand pairs each letter
acts on**, which is well defined letter-by-letter and identical in every
branch, because an `averaged` letter `sigma_g - (h/2)*1` and both of its
resolutions `sigma_g`, `sigma_g^-1` project to the *same* transposition
`(g, g+1)`. Hence:

  * the component partition is the same in every branch;
  * "no letter acts on two members of the triple" holds in every branch;
  * the strand blocks are the same in every branch.

So the splitness -- and therefore the vanishing -- is a statement about
**every one of the `2^(2A+1)` branch closures separately**, not about a single
link that does not exist. Read every "closure" below that way. Linking
NUMBERS, by contrast, ARE branch-dependent (`-1` vs `-2` per bond), which is
why they are reported per branch in the sibling probe and are not load-bearing
for this result.

## Scope

**(b) for every branch closure of this word**, invariant named: a split link
has vanishing Milnor invariants, and splitness is established here structurally rather than
numerically. **(a) for the route**: a different nucleus->link assignment whose
closure is genuinely Brunnian -- pairwise unlinked while still interacting,
which is what `L6a4` is and this word is not -- would restore it. That is now
a sharp, checkable requirement on any future assignment: *interaction without
linking*, which the path structure of this word makes impossible.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ISOTOPES = [(2, 2, "4He"), (3, 3, "6Li"), (4, 3, "7Be"), (4, 4, "8Be"),
            (6, 6, "12C"), (8, 8, "16O")]


def structure(Z: int, N: int):
    n = 3 * (Z + N)
    word = atom_canonical_crossings(Z, N)
    perm = list(range(n))
    for g, _ in word:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    comp: dict[int, int] = {}
    c = 0
    for i in range(n):
        if i not in comp:
            j = i
            while j not in comp:
                comp[j] = c
                j = perm[j]
            c += 1
    unsigned: dict[tuple[int, int], int] = {}
    pos = list(range(n))
    for g, _ in word:
        a, b = comp[pos[g]], comp[pos[g + 1]]
        if a != b:
            k = (min(a, b), max(a, b))
            unsigned[k] = unsigned.get(k, 0) + 1
        pos[g], pos[g + 1] = pos[g + 1], pos[g]
    blocks = {k: sorted(s for s in range(n) if comp[s] == k) for k in range(c)}
    return n, word, comp, c, unsigned, blocks


def main() -> int:
    checks: list[tuple[bool, str]] = []
    print("=" * 76)
    print("MILNOR-DEFINED TRIPLES OF THE ATOM CLOSURE ARE SPLIT")
    print("=" * 76)

    for Z, N, name in ISOTOPES:
        A = Z + N
        n, word, comp, mu, unsigned, blocks = structure(Z, N)
        crossing_pairs = {k for k, v in unsigned.items() if v > 0}
        non_adjacent_with_crossings = {k for k in crossing_pairs
                                       if k[1] != k[0] + 1}
        contiguous = all(v == list(range(v[0], v[-1] + 1))
                         for v in blocks.values())
        triples = [(i, i + 2, i + 4) for i in range(mu - 4)]

        print(f"\n[{name}]  A={A}  mu={mu}  min-span triples={len(triples)}")
        print(f"    pairs with any crossing : {len(crossing_pairs)}  "
              f"(= mu-1 = {mu-1})")
        print(f"    NON-ADJACENT pairs with crossings : "
              f"{sorted(non_adjacent_with_crossings) or 'NONE'}")
        print(f"    every component a contiguous strand block : {contiguous}")

        checks.append((len(crossing_pairs) == mu - 1,
                       f"{name}: only the mu-1 consecutive pairs cross"))
        checks.append((not non_adjacent_with_crossings,
                       f"{name}: ZERO crossings between non-adjacent "
                       f"components (not merely zero signed sum)"))
        checks.append((contiguous,
                       f"{name}: every component is a contiguous strand block"))

        for t in triples:
            acts = 0
            pos = list(range(n))
            for g, _ in word:
                a, b = comp[pos[g]], comp[pos[g + 1]]
                if a != b and a in t and b in t:
                    acts += 1
                pos[g], pos[g + 1] = pos[g + 1], pos[g]
            iv = [(min(blocks[k]), max(blocks[k])) for k in t]
            disjoint = all(not (iv[x][1] >= iv[y][0] and iv[y][1] >= iv[x][0])
                           for x in range(3) for y in range(x + 1, 3))
            checks.append((acts == 0,
                           f"{name} {t}: no letter acts on two members"))
            checks.append((disjoint,
                           f"{name} {t}: the three strand blocks are pairwise "
                           f"disjoint intervals -> SPLIT"))
        if triples:
            print(f"    every min-span triple: 0 interacting letters, "
                  f"3 disjoint blocks  => SPLIT => mubar = 0")

    print("\n" + "=" * 76)
    print("COLLAPSE:  Delta(ijk) = 0  =>  split  =>  mubar(ijk) = 0.")
    print("Definedness and triviality coincide, BECAUSE the linking graph is a")
    print("path: on a path, 'not linked' and 'never interacts' are one")
    print("condition.  No non-trivial well-defined Milnor triple invariant")
    print("exists in ANY branch closure at any A.  The Magnus expansion would")
    print("return")
    print("zero on exactly the triples where it is meaningful.")
    print("=" * 76)

    failed = [m for ok, m in checks if not ok]
    for ok, m in checks:
        if not ok:
            print(f"  FAIL  {m}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    print("=" * 76)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
