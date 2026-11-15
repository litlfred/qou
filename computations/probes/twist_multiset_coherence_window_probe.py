#!/usr/bin/env python3
"""Where sign-coherence is load-bearing in the first-generation twist multisets.

Bean `qou-h0zz` (item c, the quark side) / `qou-kebu`; carrier Lean is
`QOU/StandardModel/SignCoherentTwist.lean`.

The arc's write-up credits all four first-generation multisets to
sign-coherence or component-constancy.  Exhaustive enumeration over
`{-1,0,1}^3` shows that **over-attributes two of them**: coherence does work
only at totals `T in {-1, 0, +1}`, and of the four fermions only `d` (T = -1)
and `nu` (T = 0) sit in that window.  `u` (T = +2) and `e` (T = -3) are forced
by range and total alone.

PRECISION: integers only.  No float anywhere, no mpmath needed -- every
quantity here is an exact integer or a set of them, so there is no arithmetic
to lose.  Emits no witness: this records a structural fact about a finite
enumeration, not a measured value.

Run: python3 computations/probes/twist_multiset_coherence_window_probe.py
Exit 0 iff every check passes.
"""

from itertools import product

RANGE = (-1, 0, 1)
STRANDS = 3

# Totals pinned by the SM spectrum, T = 3Q (bean qou-h0zz item 1 -- this is an
# ANCHOR, not a derivation, and nothing in this probe changes that).
PINNED = {"u": 2, "d": -1, "nu": 0, "e": -3}

_failures = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))
    if not ok:
        _failures.append(name)


def coherent(t) -> bool:
    """No strand pair carries twists of opposite sign."""
    return not any(a > 0 and b < 0 for a in t for b in t)


def multisets(total: int, require_coherent: bool) -> set:
    return {
        tuple(sorted(t))
        for t in product(RANGE, repeat=STRANDS)
        if sum(t) == total and (coherent(t) if require_coherent else True)
    }


def has_mixed_sign_at(total: int) -> bool:
    return any(
        max(t) > 0 and min(t) < 0
        for t in product(RANGE, repeat=STRANDS)
        if sum(t) == total
    )


def main() -> int:
    print(__doc__.strip().splitlines()[0])
    print()

    lo, hi = STRANDS * min(RANGE), STRANDS * max(RANGE)
    totals = range(lo, hi + 1)

    print(f"  enumeration: {len(RANGE)}^{STRANDS} = "
          f"{len(RANGE) ** STRANDS} assignments, totals {lo}..{hi}")
    print()
    print("   T   | no coherence                  | with coherence   | mixed-sign reaches T")
    print("  -----+-------------------------------+------------------+---------------------")
    table = {}
    for T in totals:
        allm, cohm, mixed = multisets(T, False), multisets(T, True), has_mixed_sign_at(T)
        table[T] = (allm, cohm, mixed)
        print(f"  {T:>4} | {str(sorted(allm)):<29} | {str(sorted(cohm)):<16} | {mixed}")
    print()

    # 1. The window: coherence changes the answer at exactly these totals.
    window = sorted(T for T, (a, c, _) in table.items() if a != c)
    check("coherence is load-bearing at exactly T in {-1,0,1}",
          window == [-1, 0, 1], f"measured {window}")

    # 2. Inside the window it always collapses two multisets to one.
    check("inside the window: 2 multisets -> 1",
          all(len(table[T][0]) == 2 and len(table[T][1]) == 1 for T in window))

    # 3. Outside it, coherence is vacuous AND the multiset is already unique.
    outside = [T for T in totals if T not in window]
    check("outside the window: already unique, coherence vacuous",
          all(len(table[T][0]) == 1 and table[T][0] == table[T][1] for T in outside),
          f"T in {outside}")

    # 4. The window is exactly where a mixed-sign assignment exists -- that is
    #    the mechanism, not a coincidence.
    check("window == totals reachable by a mixed-sign assignment",
          sorted(T for T, (_, _, m) in table.items() if m) == window)

    # 5. Per-fermion attribution: which of the four need the interpretive step.
    needs = sorted(f for f, T in PINNED.items() if PINNED[f] in window)
    free = sorted(f for f, T in PINNED.items() if PINNED[f] not in window)
    check("exactly d and nu need coherence", needs == ["d", "nu"], f"measured {needs}")
    check("u and e are forced by range+total alone", free == ["e", "u"], f"measured {free}")

    # 6. The specific multisets the Lean asserts.
    expected = {"u": (0, 1, 1), "d": (-1, 0, 0), "nu": (0, 0, 0), "e": (-1, -1, -1)}
    for f, T in sorted(PINNED.items()):
        got = table[T][1]
        check(f"{f}: coherent multiset at T={T} is {expected[f]}",
              got == {expected[f]}, f"got {sorted(got)}")

    print()
    if _failures:
        print(f"FAILED {len(_failures)} check(s): {', '.join(_failures)}")
        return 1
    print("All checks passed.")
    print()
    print("  Reading: the one interpretive step in this arc -- that the physical")
    print("  state is the ribbon-equivalence class rather than a chosen spelling")
    print("  -- carries TWO of the four first-generation fermions, not four.")
    print("  It does NOT derive the totals, which stay pinned by T = 3Q.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
