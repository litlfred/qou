#!/usr/bin/env python3
"""atom_word_explicit_ordering_probe.py — the closed form on an UNSORTED nucleon ordering.

The discriminating case for the bond product, and the first word of its kind the corpus can build.

## Why this needed a change to the word builder

`atom_braid_word_3A` has always laid nucleons down **sorted**, `['p']*Z + ['n']*N`, because it takes
`(Z, N)` and nothing else. So every claim in this arc — the corpus's `∏ᵢ (z + dᵢ)` bond model, and
the closed form of PR #6920 — has only ever been checked on sorted words. The corpus's recorded
invariance is about the **intra**-nucleon letter order (that function's own docstring, and
`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`); it says nothing about the
**inter**-nucleon sequence, and no unsorted sequence could be built at all.

This probe adds `ordering=` to the canonical builder rather than hand-assembling a word. That choice
is the whole point: this arc exists because a word quietly differed from what its comment claimed
(owner ruling `qou-hu1f`), so a hand-built word would be evidence about my typing, not about the
model. `ordering=None` reproduces the sorted word exactly, and **check 1 asserts that** rather than
trusting it.

## What is tested

    1. BACKWARDS COMPATIBILITY.  ordering=None == ordering=['p']*Z+['n']*N, letter for letter,
       over every (Z,N) with A ≤ 4 — 14 words. The guard on mismatched content also fires.

    2. THE HELD-OUT PREDICTION.  `pnp` (Z=2, N=1) has the same CONTENT as `ppn` = ³He, so its
       free half is identical; only its bonds differ — two mixed interfaces where ³He has one
       `pp` and one `pn`. The closed form therefore predicts

           tr(atom; pnp) = tr(p)² · tr(n) · (z + d_pn)²

       against ³He's `tr(p)² · tr(n) · (z + d_pp)(z + d_pn)`. Nothing is fitted: both factors
       were measured on OTHER words (single nucleons at n = 3; one-interface words at A = 3),
       and `pnp` is a word the builder could not previously produce at all.

    3. THE ORDERING GENUINELY MOVES THE ANSWER.  `pnp` and `ppn` must DIFFER — otherwise check 2
       is satisfied by a constant and tests nothing.

## Scope

Orders 0, 1, 2; one unsorted ordering at `A = 3`. A pass says the bond product survives an
inter-nucleon rearrangement in this one case, which is the first evidence of any kind on that
question. It does not establish it for all orderings or all `A`. Exact `Fraction` arithmetic
throughout; no `q₀` evaluated, no float, no witness written, nothing wired, no Lean.
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from itertools import product
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

# Measured on smaller objects, in #6920 and confirmed as `z + d` in
# `bond_factors_are_z_plus_d_probe`. Inputs here, not fitted to anything below.
NUC = {"p": [F(1, 2), F(3, 4), F(23, 8)], "n": [F(1, 2), F(-1, 2), F(3, 2)]}
BOND = {"pp": [F(1, 2), F(1), F(1, 4)],
        "pn": [F(1, 2), F(0), F(3, 4)],
        "nn": [F(1, 2), F(-1), F(5, 4)]}


def mul(a, b):
    return [a[0] * b[0], a[0] * b[1] + a[1] * b[0],
            a[0] * b[2] + a[1] * b[1] + a[2] * b[0]]


def predict(order: list[str]) -> tuple[list[F], list[F]]:
    """Predicted `(free, atom)` order-2 series for an ARBITRARY nucleon ordering."""
    free = [F(1), F(0), F(0)]
    for x in order:
        free = mul(free, NUC[x])
    atom = list(free)
    for x, y in zip(order, order[1:]):
        key = "pp" if x == y == "p" else "nn" if x == y == "n" else "pn"
        atom = mul(atom, BOND[key])
    return free, atom


def measure(Z: int, N: int, order: list[str] | None) -> tuple[list[F], list[F]]:
    """Exact order-2 series of the free and atom words, through the corpus's own expansion."""
    orig = _D.atom_canonical_crossings
    if order is not None:
        _D.atom_canonical_crossings = (
            lambda z, n, **kw: orig(z, n, **{**kw, "ordering": order}))
    try:
        f, _ = _D.trace_expansion(Z, N, False, 2)
        a, _ = _D.trace_expansion(Z, N, True, 2)
    finally:
        _D.atom_canonical_crossings = orig
    return list(f), list(a)


def main() -> int:
    t0 = time.time()
    print("=" * 92)
    print("  The closed form on an UNSORTED nucleon ordering — the discriminating case")
    print("=" * 92)

    # ---- 1. backwards compatibility -------------------------------------------------
    print("\n  1. BACKWARDS COMPATIBILITY — ordering=None must equal the explicit sorted list")
    compat, checked = True, 0
    for A in (1, 2, 3, 4):
        for Z in range(A + 1):
            N = A - Z
            same = (atom_canonical_crossings(Z, N)
                    == atom_canonical_crossings(Z, N, ordering=['p'] * Z + ['n'] * N))
            compat = compat and same
            checked += 1
    guard = False
    try:
        atom_canonical_crossings(2, 1, ordering=['p', 'p', 'p'])
    except ValueError:
        guard = True
    print(f"     identical on {checked}/{checked} words with A ≤ 4: {compat}")
    print(f"     mismatched-content guard fires: {guard}")
    ok1 = compat and guard
    print(f"     ⇒ {'no existing caller can be affected — the default path is unchanged.' if ok1 else 'FAIL — the parameter changed default behaviour; do not use this.'}")

    # ---- 2. the held-out prediction --------------------------------------------------
    print(f"\n  2. HELD-OUT — `pnp` (Z=2, N=1), a word the builder could not previously produce")
    ifs = [(g, k) for g, k in atom_canonical_crossings(2, 1, ordering=['p', 'n', 'p'])
           if g % 3 == 2]
    print(f"     pnp interface letters: {ifs}")
    print(f"     ppn interface letters: "
          f"{[(g, k) for g, k in atom_canonical_crossings(2, 1) if g % 3 == 2]}")

    ok2 = True
    print(f"\n     {'ordering':<8}{'quantity':<10}{'predicted':>14}{'measured':>14}")
    rows = {}
    for order in (['p', 'n', 'p'], ['p', 'p', 'n']):
        pf, pa = predict(order)
        mf, ma = measure(2, 1, order)
        pd = [x - y for x, y in zip(pf, pa)]
        md = [x - y for x, y in zip(mf, ma)]
        rows[''.join(order)] = md
        for label, pv, mv in (("c₀", pd[0], md[0]),
                              ("c₁", pd[1], md[1]),
                              ("c₂", pd[1] + pd[2], md[1] + md[2])):
            hit = pv == mv
            ok2 = ok2 and hit
            print(f"     {''.join(order):<8}{label:<10}{str(pv):>14}{str(mv):>14}"
                  f"  {'ok' if hit else 'FAIL'}")
    print(f"     ⇒ {'6/6 — the bond product survives an inter-nucleon rearrangement.' if ok2 else 'FAIL — the closed form does NOT extend to unsorted orderings. That is the finding.'}")

    # ---- 3. the ordering must actually matter ----------------------------------------
    print(f"\n  3. CONTROL — `pnp` and `ppn` must DIFFER, or check 2 is satisfied by a constant")
    moved = rows['pnp'] != rows['ppn']
    print(f"     pnp  c₀,c₁,c₂ = {[str(rows['pnp'][0]), str(rows['pnp'][1]), str(rows['pnp'][1] + rows['pnp'][2])]}")
    print(f"     ppn  c₀,c₁,c₂ = {[str(rows['ppn'][0]), str(rows['ppn'][1]), str(rows['ppn'][1] + rows['ppn'][2])]}")
    print(f"     ⇒ {'they differ — check 2 has content.' if moved else 'IDENTICAL — check 2 tests nothing; the probe is vacuous.'}")

    ok = ok1 and ok2 and moved
    print(f"\n  SCOPE. Orders 0,1,2; ONE unsorted ordering at A = 3. A pass says the bond product")
    print("  survives an inter-nucleon rearrangement in this one case — the first evidence of any")
    print("  kind on that question, since no unsorted word could be built before. It does NOT")
    print("  establish it for all orderings or all A. The corpus's recorded invariance is about")
    print("  INTRA-nucleon letter order and was never about this.")
    print(f"\n  ({time.time()-t0:.1f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
