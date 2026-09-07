#!/usr/bin/env python3
"""bond_product_order_three_probe.py — the bond product at order 3, and what it costs. (qou-qqm4)

## The question

`atom_bond_product_closed_form_probe` establishes, on 9 words at `A = 2…5`, that the atom word's
normalised Markov trace is a product over nucleon blocks and adjacent-pair bonds, to **orders 0, 1
and 2**. Its own scope note says "orders 0, 1, 2 only". This probe asks the obvious next question —
does the product survive order 3, and does the bond factor need new inputs to get there?

## The answer

**Yes, and no.** The product holds at order 3 on every word tested, and the order-3 bond factor is
**not a new measurement at all**: it is forced by data the corpus already had.

Two findings, in increasing order of how much they explain.

### 1. The cubic coefficient is minus the quadratic one — for all three bonds

Normalising each bond factor to `(1/2)·(1 + ρε + τε² + υε³)`, the measured values are

    pp   (1,  2,  1/2,  −1/2)
    pn   (1,  0,  3/2,  −3/2)
    nn   (1, −2,  5/2,  −5/2)

so `υ_b = −τ_b` in every case. Order 3 introduces **zero** new degrees of freedom into the bond.
That is an observation about three numbers, and on its own it is the weaker of the two findings —
three coincidences is not a mechanism.

### 2. The three bonds are exactly `z`, `(z + z')/2`, `z'` — the two Markov parameters

`bond_factors_are_z_plus_d_probe` (PR #6992) identified each bond factor as `z_D + d`, the
convention-D Markov parameter plus the interface letter's diagonal correction, at orders ≤ 2. That
identity still holds at order 3 (asserted below). But writing it that way understates it, because
the two `d`s that are non-zero are **not independent of `z`**:

    d_sigma_inv         = −h                  and   z' := z − h    is the NEGATIVE-crossing
                                                     Markov parameter — `OcneanuTrace`'s
                                                     `markovParam_inv_eq_sub`, forced by the
                                                     quadratic relation, not a new constant
    d_averaged_weighted = −h/2                so    z + d = (z + z')/2

so the whole table collapses to the two Markov parameters and their average, with **no offset and
no free parameter anywhere**:

    pp   z            = (1/2)·(1,  2,  1/2, −1/2)      positive crossing
    pn   (z + z')/2   = (1/2)·(1,  0,  3/2, −3/2)      the average of the two
    nn   z'  = z − h  = (1/2)·(1, −2,  5/2, −5/2)      negative crossing

3/3, orders 0-3, nothing re-fitted. `υ = −τ` in finding 1 is then not three coincidences: it is
`z`'s own third coefficient (`−1/2` against `+1/2`) and `h`'s (`+1` against `−1`), inherited by
every bond. That the bond factor has no free parameter **at any order tested** is what makes the
whole closed form parameter-free rather than merely few-parameter.

The `pn` row also gives the corpus's `the_pn_bond_is_an_average_and_cannot_be_extremal_probe` its
literal arithmetic content: the mixed bond *is* the mean of the like-bonds, coefficient by
coefficient.

### 3. Why `z + d` is the shape — and what the corpus already proves about it

The `d` in `z + d` is not a fitted offset per bond: `pattern_scalar` adds it **uniformly** across
every basis pattern (`e11`/`e22`, `e21`, `e12`) — asserted below over all four letter kinds and 48
`(b, g)` sites, with both diagonal and off-diagonal patterns exercised. So an interface letter acts
as `σ + d·1`, and `tr` is linear, giving

    bond  =  tr(σ-part)  +  d  =  z + d

with the first term measured to **be** `z_D` on exactly the kind whose `d` vanishes (`sigma` → `pp`,
4 coefficients, above).

Each of the three factors then has a Lean counterpart already on `main`, and finding 2 says which:

    pp   tr (a * g n)    = tr a * z      `DisjointBlockTraceLaw.tr_mul_gen`      (PR #6979)
    nn   tr (a * ginv n) = tr a * z'     `DisjointBlockTraceLaw.tr_mul_geninv`   (PR #6979)
         z' = z − h                      `OcneanuTrace.markovParam_inv_eq_sub`
    pn   the average                     `DisjointBlockTraceLaw.tr_mul_avg_gen`  (added here)

The `pn` line is the one that was missing, and it is a two-line consequence of linearity: the
averaged interface letter is `(g n + ginv n)/2`, so `tr (a * that) = tr a * (z + z')/2`. It is added
to `DisjointBlockTraceLaw` in this branch because that file already carries the other two and the
measurement above is what motivates it.

🛑 **Stated honestly: all three are proved FROM the `TwoSidedMarkov` class, which has no instance**
— conditional-proved is not premise-established. So the order-3 identity here is the arithmetic
shadow of a *conditional* theorem, not of an established one, and it is evidence **for** that
conditional's premise rather than a consequence of anything settled. What is unconditional is the
measurement and the uniformity of `d`; the Lean supplies the reason the two would compose.

## 🛑 A limit this creates, which also applies to PR #6992

`d_averaged_weighted = −h·(1/2 − δ/4)` with `δ = O(ε³)`, and `h = O(ε)`. So the `δ` term first
contributes at **`ε⁴`**, and through `K = 3`

    d_averaged  ==  d_averaged_weighted     (asserted below, not assumed)

identically. **Order 3 cannot tell the `pn` interface's kind from plain `averaged`.** #6992 reports
the mixed bond as `averaged_weighted`; what is actually measured — there at `K = 2` and here at
`K = 3` — is that it is neither `sigma` nor `sigma_inv`. Discriminating `averaged_weighted` from
`averaged` needs order **4**, which this probe does not reach. Recorded because #6992's kind table
reads as three determinations and is really two-and-a-half.

## Scope

Orders 0-3; `A ≤ 3` for the product test (`A = 3` is 125 s per word at `K = 3` and `A = 4` is
~25× that, so the sweep stops there). Bond and nucleon factors are extracted from `A = 1` and
`A = 2` and the `A = 3` words — including the unsorted `pnp` from
`atom_word_explicit_ordering_probe` — are held out. Exact `Fraction` arithmetic throughout: no
float, no `q₀` evaluated, no witness written, nothing wired, no Lean.

SCOPE — (a) scope-limited.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

_ORIG = _D.atom_canonical_crossings

K = 3

# Held-out targets: order-3 series of the free and atom words at A = 3, measured by the same
# `trace_expansion` used everywhere in this arc. 125 s per word, so they are recorded rather than
# recomputed on every invocation; `--verify-live` re-measures them. If a fresh run ever disagrees,
# the TARGET is what to re-derive.
TARGETS: dict[str, dict[str, list[F]]] = {
    "3p": {"free": [F(1, 8), F(9, 16), F(3), F(891, 64)],
           "atom": [F(1, 32), F(17, 64), F(47, 32), F(1847, 256)]},
    "T": {"free": [F(1, 8), F(-1, 16), F(39, 32), F(199, 32)],
          "atom": [F(1, 32), F(-5, 64), F(59, 128), F(85, 128)]},
    "3He": {"free": [F(1, 8), F(1, 4), F(55, 32), F(69, 8)],
            "atom": [F(1, 32), F(1, 8), F(79, 128), F(203, 64)]},
    "3n": {"free": [F(1, 8), F(-3, 8), F(3, 2), F(19, 4)],
           "atom": [F(1, 32), F(-7, 32), F(33, 32), F(-13, 8)]},
    "pnp": {"free": [F(1, 8), F(1, 4), F(55, 32), F(69, 8)],
            "atom": [F(1, 32), F(1, 16), F(67, 128), F(9, 4)]},
}

ORDERINGS = {"3p": ['p', 'p', 'p'], "T": ['p', 'n', 'n'], "3He": ['p', 'p', 'n'],
             "3n": ['n', 'n', 'n'], "pnp": ['p', 'n', 'p']}
ZN = {"3p": (3, 0), "T": (1, 2), "3He": (2, 1), "3n": (0, 3), "pnp": (2, 1)}
# `pnp` needs the `ordering=` parameter added to the canonical builder in
# `atom_word_explicit_ordering_probe`; the others are the sorted default.
UNSORTED = {"pnp"}

KIND = {"pp": "sigma", "pn": "averaged_weighted", "nn": "sigma_inv"}


def pmul(a: list[F], b: list[F]) -> list[F]:
    return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(K + 1)]


def pdiv(a: list[F], b: list[F]) -> list[F]:
    """Truncated `a / b`, `b[0] != 0`."""
    out = [F(0)] * (K + 1)
    for k in range(K + 1):
        out[k] = (a[k] - sum(out[i] * b[k - i] for i in range(k))) / b[0]
    return out


def measure(Z: int, N: int, inter: bool, order: list[str] | None = None) -> list[F]:
    """Exact order-3 series of one word, through the corpus's own [◇] expansion."""
    if order is not None:
        _D.atom_canonical_crossings = (
            lambda z, n, **kw: _ORIG(z, n, **{**kw, "ordering": order}))
    try:
        ser, _ = _D.trace_expansion(Z, N, inter, K)
    finally:
        _D.atom_canonical_crossings = _ORIG
    return list(ser)


def z_d_series() -> list[F]:
    """`z_D = q³/(q²+1)` at `q = 1+ε`, as an order-3 series."""
    q = [F(1), F(1), F(0), F(0)]
    q2 = pmul(q, q)
    q3 = pmul(q2, q)
    return pdiv(q3, [q2[0] + 1, q2[1], q2[2], q2[3]])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-live", action="store_true",
                    help="re-measure the A=3 targets (~21 min) instead of using the recorded ones")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 94)
    print("  The bond product at ORDER 3 — and the bond factor needs no new input to get there")
    print("=" * 94)

    # ---- inputs: nucleons at A=1, bonds at A=2 (cheap, always live) ---------------------
    nuc = {"p": measure(1, 0, False), "n": measure(0, 1, False)}
    bond = {}
    for b, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        x, y = ("p", "p") if b == "pp" else ("p", "n") if b == "pn" else ("n", "n")
        bond[b] = pdiv(measure(Z, N, True), pmul(nuc[x], nuc[y]))

    print("\n  INPUTS (measured live; nucleons at A=1, bonds at A=2 — normalised to leading 1)")
    for k, v in nuc.items():
        print(f"     nucleon {k:3s} {str(v[0]):>6s} · {[str(x / v[0]) for x in v]}")
    for k, v in bond.items():
        print(f"     bond    {k:3s} {str(v[0]):>6s} · {[str(x / v[0]) for x in v]}")

    # ---- 1. υ = −τ ---------------------------------------------------------------------
    print("\n  1. NO NEW FREEDOM AT ORDER 3 — the cubic coefficient is minus the quadratic")
    ok1 = True
    for b, v in bond.items():
        tau, ups = v[2] / v[0], v[3] / v[0]
        hit = ups == -tau
        ok1 = ok1 and hit
        print(f"     {b:3s} τ = {str(tau):>6s}   υ = {str(ups):>6s}   υ+τ = {str(ups + tau):>4s}"
              f"  {'ok' if hit else 'FAIL'}")
    print(f"     ⇒ {'3/3 — order 3 adds no degree of freedom to any bond.' if ok1 else 'FAIL — some bond needs a genuinely new cubic input.'}")

    # ---- 2. the bonds ARE the two Markov parameters and their average -----------------------
    print("\n  2. THE MECHANISM — the three bonds are exactly z, (z+z')/2, z'  (no offset at all)")
    z = z_d_series()
    h = _D.series_h(K)
    zp = [z[i] - h[i] for i in range(K + 1)]                  # z' = z − h, forced by q² = hq + 1
    avg = [(z[i] + zp[i]) / 2 for i in range(K + 1)]
    print(f"     z   (positive crossing)  {[str(x) for x in z]}")
    print(f"     h                        {[str(x) for x in h]}")
    print(f"     z' = z − h (negative)    {[str(x) for x in zp]}")
    print(f"     (z + z')/2  (average)    {[str(x) for x in avg]}")
    ok2 = True
    for b, pred, why in (("pp", z, "z"), ("pn", avg, "(z+z')/2"), ("nn", zp, "z' = z − h")):
        hit = pred == bond[b]
        ok2 = ok2 and hit
        print(f"     {b:3s} = {why:<12s} {[str(x) for x in pred]}  vs measured "
              f"{[str(x) for x in bond[b]]}  {'ok' if hit else 'MISMATCH'}")
    # and the equivalent `z + d` form of #6992, so the two statements are visibly the same object
    ok2b = all([z[i] + _D.letter_d_series(KIND[b], K)[i] for i in range(K + 1)] == bond[b]
               for b in KIND)
    print(f"     (#6992’s `z + d` form agrees, 3/3: {ok2b} — d_sigma_inv = −h and "
          f"d_averaged = −h/2 are\n      not new constants, which is why the offsets vanish above.)")
    ok2 = ok2 and ok2b
    print(f"     ⇒ {'3/3 — the bond factor has NO free parameter at any order tested.' if ok2 else 'FAIL — the identification breaks at order 3. That is the finding.'}")

    # ---- 2a. why z+d is the shape: d is a uniform scalar -----------------------------------
    print("\n  2a. WHY THAT SHAPE — `d` is added uniformly, so a letter acts as `σ + d·1`")
    eps = [F(0), F(1)] + [F(0)] * (K - 1)
    h = _D.series_h(K)
    zero = [F(0)] * (K + 1)
    ok2a, sites, pats = True, 0, set()
    for kind in ("sigma", "sigma_inv", "averaged", "averaged_weighted"):
        d = _D.letter_d_series(kind, K)
        for b in range(16):
            for g in range(3):
                with_d = _D.pattern_scalar(b, g, eps, h, d, K)
                no_d = _D.pattern_scalar(b, g, eps, h, zero, K)
                ok2a = ok2a and [with_d[i] - no_d[i] for i in range(K + 1)] == d
                pats.add(((b >> g) & 1) == ((b >> (g + 1)) & 1))
                sites += 1
    print(f"     checked {sites} (kind, b, g) sites; diagonal AND off-diagonal patterns present: "
          f"{sorted(pats) == [False, True]}")
    print(f"     ⇒ {'`d` is a uniform scalar, not a per-pattern offset — so tr(a·letter) = tr(a)·(z+d) by linearity.' if ok2a else 'FAIL — `d` is pattern-dependent; the z+d reading is wrong.'}")
    print("       The `tr(a·σ) = tr(a)·z` half is `DisjointBlockTraceLaw.tr_mul_gen` on main —")
    print("       but proved FROM `TwoSidedMarkov`, a class with no instance. Conditional, not settled.")

    # ---- 2b. the honest limit ------------------------------------------------------------
    same = _D.letter_d_series("averaged", K) == _D.letter_d_series("averaged_weighted", K)
    print("\n  2b. WHAT ORDER 3 CANNOT SEE — `averaged` vs `averaged_weighted`")
    print(f"     d_averaged          {[str(x) for x in _D.letter_d_series('averaged', K)]}")
    print(f"     d_averaged_weighted {[str(x) for x in _D.letter_d_series('averaged_weighted', K)]}")
    print(f"     identical through K={K}: {same}   (δ = O(ε³) enters d only via h·δ = O(ε⁴))")
    print(f"     ⇒ {'the pn kind is measured as NOT sigma / NOT sigma_inv; separating it from plain' if same else 'they already differ — order 3 DOES discriminate the pn kind.'}")
    if same:
        print("       `averaged` needs order 4. #6992’s kind table is two-and-a-half determinations.")

    # ---- 3. the held-out product test ------------------------------------------------------
    print(f"\n  3. HELD OUT — A = 3 words predicted at order 3 from the A≤2 factors above")
    if args.verify_live and not TARGETS:
        pass
    tgt = {}
    for name in ORDERINGS:
        if args.verify_live or name not in TARGETS:
            Z, N = ZN[name]
            o = ORDERINGS[name] if name in UNSORTED else None
            t = time.time()
            tgt[name] = {"free": measure(Z, N, False, o), "atom": measure(Z, N, True, o)}
            print(f"     (measured {name} live, {time.time()-t:.0f}s)", flush=True)
        else:
            tgt[name] = TARGETS[name]

    ok3, hits, tot = True, 0, 0
    print(f"\n     {'word':<6}{'part':<6}{'k':<3}{'predicted':>16}{'measured':>16}")
    for name, order in ORDERINGS.items():
        free = [F(1), F(0), F(0), F(0)]
        for x in order:
            free = pmul(free, nuc[x])
        atom = list(free)
        for x, y in zip(order, order[1:]):
            atom = pmul(atom, bond["pp" if x == y == "p" else "nn" if x == y == "n" else "pn"])
        for part, pred in (("free", free), ("atom", atom)):
            for k in range(K + 1):
                mv = tgt[name][part][k]
                hit = pred[k] == mv
                ok3 = ok3 and hit
                hits += int(hit)
                tot += 1
                print(f"     {name:<6}{part:<6}{k:<3}{str(pred[k]):>16}{str(mv):>16}"
                      f"  {'ok' if hit else 'FAIL'}")
    print(f"     ⇒ {hits}/{tot} " + ("— the bond product holds at order 3, including on the unsorted `pnp`."
                                     if ok3 else "— the product FAILS at order 3. That is the finding; report it as such."))

    ok = ok1 and ok2 and ok2a and ok3
    print(f"\n  SCOPE. Orders 0-3, A ≤ 3 for the product test. The three bond factors are exactly the")
    print("  two Markov parameters and their average — no offset, no free parameter at any order")
    print("  tested — but the `pn` kind is NOT pinned to `averaged_weighted` by anything here: order")
    print("  4 is where `averaged_weighted` would predict a DEVIATION from the plain average, and")
    print("  that is the next discriminating measurement. Nothing evaluated at q₀, no witness.")
    print(f"\n  ({time.time()-t0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
