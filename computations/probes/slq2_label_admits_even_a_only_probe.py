#!/usr/bin/env python3
# polynomial_q_not_applicable: pure permutation combinatorics of the canonical
# atom word plus integer parity. No q, no float, nothing evaluated at q0.
"""
slq2_label_admits_even_a_only_probe.py — Finkelstein's SLq(2) knot->irrep
labelling admits the canonical atom word for EVEN A only.

## The route

`library/arxiv-0806.3105v3` (Finkelstein, *Knots and preons*, held) gives a
DERIVED knot -> representation map: the kinematic eigenstates of a quantum
knot are matrix elements of `SLq(2)` irreps

    D^{N/2}_{w/2, (r+1)/2},   (N, w, r) = (crossings, writhe, rotation)

read straight off topological invariants -- no volume, no census scan, nothing
fitted. That makes it a candidate for the nucleus->link map that
`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md` shows the census route
cannot supply. The corpus already adopts the sibling Bilson-Thompson
construction at the LEPTON level (`breit-wheeler-vertex-literature.md`), so
this is pushing an existing commitment up to nuclei, not importing a new one.

## `r` needs no fetch: for a closed braid on n strands, r = n

The rotation number (Whitney degree) of a coherently-oriented closed braid on
`n` strands is `n`. Finkelstein's own trefoil values confirm it: the trefoil is
the closure of `sigma_1^3` in `B_2`, and he records `r = +-2`. So for the atom
word `r = 3A`, the framework's own strand count.

## The label is not free — it must be a real irrep index

`D^j_{m m'}` requires `j - m` and `j - m'` to be integers.

- `j - m = (N - w)/2` is **always** an integer: each crossing contributes +-1
  to the writhe, so `w = N (mod 2)`.
- `j - m' = (N - r - 1)/2` is the binding constraint.

For a closed braid, Seifert's algorithm gives `n` circles and `c` bands, so
`chi = n - c`; and `chi = 2 - 2g - mu` for a genus-`g` surface with `mu`
boundary components. Hence `c - n = 2g + mu - 2`, and

    (N - r - 1) even   <=>   mu odd.

**So the labelling admits exactly the closures with an ODD number of
components.** For a knot (`mu = 1`) that is automatic, which is why the
dictionary is stated for knots.

## Measured: mu = A + 1, so the map admits EVEN A only

The component count is the number of cycles of the underlying permutation.
Superposition letters (`c*sigma_g + d*1`) resolve to `sigma_g` or the
identity, and **both project to the same permutation**, so `mu` is
branch-independent -- it is the one quantity here that does not depend on
which of the `2^(2A+1)` branches is taken.

Measured below over ten isotopes including asymmetric ones: **`mu = A + 1`**
exactly. Cross-check: the deuteron's `mu = 3` reproduces the 3 components
measured independently in SnapPy over all 32 branches by the 2026-08-25 audit.

Therefore `mu` odd <=> `A` even, and:

    A EVEN  (2H, 4He, 6Li, 8Be, 12C, 16O)  -> label consistent
    A ODD   (3H, 3He, 5Li, 7Be, 7Li)       -> NO valid label, for ANY branch

## Scope

**(a)** for this labelling applied to this word. It does not refute the
SLq(2) route -- it locates precisely what a generalisation must supply: a
**link** version of the labelling, since the parity condition is exactly the
knot condition. Odd-A nuclei include the A=3 mirror pair the arc's convention
systematic already lives on, so the excluded half is not incidental.

## A RETRACTED first attempt, recorded because the error is instructive

My first pass fed `N = 10A - 2` -- the count of *genuine* braid letters -- into
the parity test as though it were the crossing number, and concluded the label
was valid at `A = 3` only. **That test was ill-posed.** The atom word carries
`2A+1` superposition letters, so its crossing count is a RANGE over
`2^(2A+1)` branches, not one number; `10A - 2` is only the minimum. The
corrected test routes through `mu`, which is branch-independent, and gives the
opposite answer. A quantity that varies across branches cannot decide a
question about the closure.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ISOTOPES = [
    (1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 2, "5Li"),
    (3, 3, "6Li"), (4, 3, "7Be"), (3, 4, "7Li"), (4, 4, "8Be"),
    (6, 6, "12C"), (8, 8, "16O"),
]


def closure_components(Z: int, N: int) -> int:
    """Cycles of the atom word's underlying permutation = components of its
    closure.  Superposition letters project to the same transposition as their
    sigma branch, so this is branch-independent."""
    n = 3 * (Z + N)
    perm = list(range(n))
    for g, _ in atom_canonical_crossings(Z, N):
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    seen = [False] * n
    cycles = 0
    for i in range(n):
        if not seen[i]:
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
    return cycles


def main() -> int:
    checks: list[tuple[bool, str]] = []
    print("=" * 78)
    print("SLq(2) LABEL D^{N/2}_{w/2,(r+1)/2} — which nuclei can it index?")
    print("=" * 78)

    print("\n[1] Component count of the atom-word closure (branch-independent)\n")
    print(f"{'iso':>5} {'A':>3} {'n=3A':>5} {'r=n':>4} {'mu':>4} {'A+1':>4} "
          f"{'mu odd':>7} {'label OK':>9}")
    for Z, N, name in ISOTOPES:
        A = Z + N
        mu = closure_components(Z, N)
        ok = mu % 2 == 1
        print(f"{name:>5} {A:>3} {3*A:>5} {3*A:>4} {mu:>4} {A+1:>4} "
              f"{str(ok):>7} {str(ok):>9}")
        checks.append((mu == A + 1, f"{name}: mu = A + 1"))
        checks.append((ok == (A % 2 == 0),
                       f"{name}: label consistent  <=>  A even"))

    # The deuteron cross-check against an independent SnapPy measurement.
    checks.append((closure_components(1, 1) == 3,
                   "2H: mu = 3, matching the 32/32 SnapPy branch measurement "
                   "in the 2026-08-25 audit"))

    print("\n  => mu = A + 1 exactly, so mu is odd iff A is even.")
    print("     The parity condition (N - r - 1) even <=> mu odd comes from")
    print("     Seifert on a closed braid: chi = n - c = 2 - 2g - mu.")

    print("\n[2] Consequence\n")
    even = [n for Z, N, n in ISOTOPES if (Z + N) % 2 == 0]
    odd = [n for Z, N, n in ISOTOPES if (Z + N) % 2 == 1]
    print(f"    label consistent (A even) : {', '.join(even)}")
    print(f"    NO valid label (A odd)    : {', '.join(odd)}")
    print("\n    The exclusion is structural, not numerical: it holds for EVERY")
    print("    one of the 2^(2A+1) branches, because mu does not depend on the")
    print("    branch.  A generalisation must supply a LINK version of the")
    print("    labelling — the parity condition IS the knot condition.")

    print("\n" + "=" * 78)
    failed = [m for ok, m in checks if not ok]
    for ok, m in checks:
        if not ok:
            print(f"  FAIL  {m}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    print("=" * 78)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
