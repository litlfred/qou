#!/usr/bin/env python3
"""The A+Z vs 3A reading picks a DIFFERENT atom — so the count is load-bearing.

Answers one item from bean `qou-jgg0`'s own "Not established" list, verbatim:

    "That the 7 mass-chapter citations are load-bearing; whether any DEPENDS
     on the A+Z count for a result was not measured."

`wedderburn-mass-formula.md` is one of those seven. **Measured: yes, and the
dependence is not a shift in a number, it is a change of subject.**

  reading (a)  def:atomic-braid   n = A + Z = 2Z + N   ->  unique atom is DEUTERIUM
  reading (b)  production         n = 3A    = 3(Z+N)   ->  unique atom is HYDROGEN-1

"Unique atom" means the unique atom at which p(n) = 3, i.e. at which the three
extremal Wedderburn blocks exhaust the partitions of n. That exhaustion is the
whole reason the n = 3 point is interesting: it is the one place where the
"three extremal invariants" are not a truncation of a longer list.

Both readings are live in the corpus. `qou-jgg0` measured 824 strand-count
lines across 377 files using 3A against 9 lines across 4 files using A+Z, plus
a THIRD count 3A+Z in `atomic-mass-gb-nf.md`. This probe does not adjudicate
them -- (a) vs (b) is explicitly reserved to the author in that bean -- it
measures what turns on the choice.

WHY IT MATTERS HERE AND NOW. PR #7171 (merged, commit 20671dcc1) added
`rem:level-zero-discards-braid-noncommutativity`, which asserts

    "Deuterium is the unique atom with n = A + Z = 3."

True under (a). Under (b) the unique such atom is hydrogen-1 and deuterium sits
at n = 6, where p(6) = 11 and the extremal blocks do NOT exhaust. So that
remark, and the probe behind it, are (a)-CONDITIONAL and do not say so. Same
for `deuterium_is_the_untested_exact_point_probe.py` check 1, which asserts
"D sits in H_{A+Z} = H_3".

That is the "conditional-proved != premise-established" discipline: the
sentences are correct given a premise the corpus has not settled, and they
state them flatly.

NOT DECIDED HERE. Which reading is right, whether either object is wrong, and
whether the other six mass-chapter citations are load-bearing. Scope (a) in the
refutation taxonomy: this constrains what depends on the choice; it excludes
nothing.

NO FLOAT64, and none is reachable: every quantity is an exact integer
(partition counts, strand counts). No mpmath, no float, no witness.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from sympy.functions.combinatorial.numbers import partition

REPO = Path(__file__).resolve().parent.parent.parent
MASS = REPO / "content/quantum-observable-universe/mass-theory"

# Sweep bound for the enumerative half of checks 2-3. The EXACT argument in
# check 4 does not depend on it; the sweep is corroboration, not the proof.
Z_MAX, N_MAX = 20, 30


def n_a(Z: int, N: int) -> int:
    """def:atomic-braid: 'H_{A+Z}(q) ... with A + Z strands, where A = Z + N'."""
    return (Z + N) + Z


def n_b(Z: int, N: int) -> int:
    """production canonical_braid: n_strands = 3 * (Z + N)."""
    return 3 * (Z + N)


def atoms():
    """Real atoms only: Z >= 1. Z = 0 is not an atom, and admitting it would
    manufacture spurious solutions (e.g. Z=0, N=3 under reading (a))."""
    for Z in range(1, Z_MAX + 1):
        for N in range(0, N_MAX + 1):
            yield Z, N


def main() -> int:
    fails: list[str] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("The A+Z vs 3A reading picks a DIFFERENT atom -- the count is load-bearing.\n")

    print("CHECK 1 -- p(n) = 3 has exactly one solution, and it is n = 3")
    vals = [int(partition(n)) for n in range(1, 41)]
    strictly_increasing = all(b > a for a, b in zip(vals, vals[1:]))
    sols = [n for n, v in zip(range(1, 41), vals) if v == 3]
    check("p is strictly increasing on n >= 1 (so p(n)=3 has <= 1 solution)",
          strictly_increasing, f"p(1..8) = {vals[:8]}")
    check("the solution is n = 3", sols == [3], f"solutions in 1..40: {sols}")
    check("p(6) = 11, so at 6 strands the extremal blocks do NOT exhaust",
          int(partition(6)) == 11, f"p(6) = {int(partition(6))}")

    print("\nCHECK 2 -- under reading (a), n = A+Z, the unique such atom is DEUTERIUM")
    hits_a = [(Z, N) for Z, N in atoms() if int(partition(n_a(Z, N))) == 3]
    check("exactly one atom in the swept range", len(hits_a) == 1, f"hits = {hits_a}")
    check("and it is (Z=1, N=1) = deuterium", hits_a == [(1, 1)],
          f"A+Z = {n_a(1, 1)}")

    print("\nCHECK 3 -- under reading (b), n = 3A, the unique such atom is HYDROGEN-1")
    hits_b = [(Z, N) for Z, N in atoms() if int(partition(n_b(Z, N))) == 3]
    check("exactly one atom in the swept range", len(hits_b) == 1, f"hits = {hits_b}")
    check("and it is (Z=1, N=0) = hydrogen-1", hits_b == [(1, 0)],
          f"3A = {n_b(1, 0)}")

    print("\nCHECK 4 -- EXACT, not merely swept: solve each reading against n = 3")
    # (a) 2Z + N = 3 with Z >= 1, N >= 0  ->  (Z,N) = (1,1) only. Z=1,N=0 gives 2.
    exact_a = [(Z, N) for Z in range(1, 4) for N in range(0, 4) if 2 * Z + N == 3]
    # (b) 3(Z+N) = 3  ->  Z + N = 1, Z >= 1  ->  (1,0) only.
    exact_b = [(Z, N) for Z in range(1, 4) for N in range(0, 4) if 3 * (Z + N) == 3]
    check("(a) 2Z + N = 3 with Z >= 1 has the unique solution (1,1)",
          exact_a == [(1, 1)], f"{exact_a}")
    check("(b) 3(Z+N) = 3 with Z >= 1 has the unique solution (1,0)",
          exact_b == [(1, 0)], f"{exact_b}")
    check("the two readings name DIFFERENT atoms", exact_a != exact_b,
          "deuterium vs hydrogen-1")

    print("\nCHECK 5 -- deuterium under reading (b) is NOT an exhaustion point")
    check("D has 3A = 6 strands and p(6) = 11 != 3",
          n_b(1, 1) == 6 and int(partition(n_b(1, 1))) == 11,
          f"3A = {n_b(1, 1)}, p = {int(partition(n_b(1, 1)))}")

    print("\nCHECK 6 -- the merged artifacts assert the DEUTERIUM form, unqualified")
    rem = (MASS / "level-zero-discards-braid-noncommutativity.md").read_text()
    flat = " ".join(rem.split())
    check("rem:level-zero... asserts 'the unique atom with $n = A + Z = 3$'",
          "Deuterium is the unique atom with $n = A + Z = 3$" in flat)
    check("and does NOT mention the 3A reading or qou-jgg0",
          not re.search(r"3A|3\s*\\?cdot\s*A|jgg0", rem),
          "so the claim is (a)-conditional and does not say so")

    print("\nCHECK 7 -- both readings are live in the mass chapter, same symbol")
    wmf = (MASS / "wedderburn-mass-formula.md").read_text()
    swd = (MASS / "schur-weyl-mass-decomposition.md")
    check("wedderburn-mass-formula.md uses H_{A+Z}",
          "H_{A+Z}" in " ".join(wmf.split()))
    if swd.exists():
        check("schur-weyl-mass-decomposition.md uses H_{3A}",
              "H_{3A}" in " ".join(swd.read_text().split()),
              "same chapter, same symbol A, different algebra")
    else:
        check("schur-weyl-mass-decomposition.md present", False, "file missing")

    total = 15
    print(f"\n{total - len(fails)}/{total} checks passed")
    if fails:
        print("FAILED: " + "; ".join(fails))
    print("\nNOT DECIDED HERE: which reading is right. That is qou-jgg0's (a)/(b)")
    print("question and is explicitly the author's. This measures what turns on it.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
