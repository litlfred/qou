"""The `4.0x short` magnitude headline is quoted at a degree the encoding cannot express.

Bean `qou-brng` -- the MAGNITUDE, this bean's stated real target.

## What this corrects

`qbeta_class_b_nonsigndefinite_bond_probe` computes the symmetry-coefficient cap

    a_A^eff(k, m)  =  E_0 * delta(m) * k / 4          (its R5 / R8 / R9)

and reports its best cell as `a_A^eff = 5.963 MeV` against the SEMF's
`a_A = 23.7 MeV`, i.e. **4.0x short**.  AGENTS.md quotes that figure
("4.0x short ... (23.7 / 5.963)"), and it is the number the bean's magnitude
question is calibrated against.

**It is evaluated at `k = 12`.**  That probe's own constant says so:
`K_DEGREES = (2, 12)  # chain and close-packed`.

And `QOU.Mass.LinearLayoutNoBulk` -- sorry-free, merged as PR #7155 -- proves
the encoding cannot express degree 12.  Its own docstring names the case:

    `not_linearLayout_of_degree_ge_three` ... the max-contact packing
    (degree up to 12) and the complete graph (degree `n - 1`) are not
    linear-layout graphs.

`atom_braid_word_3A` emits every inter-nucleon letter at generator `3k+2`, so
the coordination graph of any word it can build is a subgraph of the path on
the ordering: `degree <= 2`, `|E| <= n`.  **`k = 2` is the only expressible
degree**, and `k = 12` is the close-packed value the same corpus excluded.

Neither the probe nor the bean's R5/R8/R9 entries mention `LinearLayout` at all
(grep: zero hits in the probe).  The two results are both on `main` and have
never been composed.

## What the composition gives

At the expressible degree the shortfall is **not 4.0x**.  Measured below.

## Scope

This changes no derivation and no bond factor -- every number here is the other
probe's own arithmetic re-evaluated at `k = 2` instead of `k = 12`.  It is a
**scope correction to a quoted figure**, not a new result, and it makes the gap
WIDER.  It does not close, narrow or reopen the magnitude question; it says what
the magnitude question's own calibration number should be.

One thing it explicitly does NOT claim: that `k = 2` is the right model.  The
well-mixed law of `bondSum_wellMixed` is a mean-field model (its own docstring
says so), and a chain is not well-mixed.  The honest reading is that BOTH cells
are model evaluations and the expressible one is the one the encoding supports.

## A correction I made and retracted inside this session, recorded because the
## direction matters

I first read the probe's `a_A^eff = E_0.delta.k/4` as substituting the degree
`k` into `symmetryCoeff = energySlope * mu / 4`'s MIXING parameter `mu`, and
reconstructed `mu <= 2k/A` from the non-negativity of `bondSum_wellMixed`'s own
counts -- concluding the cap was understated 2x.  **That is wrong.**
`SymmetrySignAmGm.lean` states the well-mixed assignment explicitly as
`E_pn ~ 2E.ZN/A^2`, i.e. `mu = k/A` -- the VALUE, where I had used a BOUND that
is 2x looser.  With `mu = k/A` the SEMF's own `1/A` cancels it exactly and
`a_A = symmetryCoeff * A = E_0.delta.k/4` is precisely the probe's formula.

The retracted claim flattered the framework (a smaller shortfall); the surviving
one does not.  Recorded because AGENTS.md asks for the direction to be stated.

NO ASSERTION HERE IS A FIT: every number is derived or measured.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_ROOT = _Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "computations" / "qbeta",
           _ROOT / "tools" / "qou-substrate" / "python"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402

from qbeta_class_b_nonsigndefinite_bond_probe import (  # noqa: E402
    A_A_TARGET, E0, H, MAX_M, Q0, bond_factors,
)

mp.mp.dps = 50

EXPRESSIBLE_DEGREE = 2      # LinearLayoutNoBulk.degree_le_two
QUOTED_DEGREE = 12          # the probe's close-packed cell, and AGENTS.md's


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def energy_slope(bpp, bpn, bnn):
    """`delta = (log b_pp + log b_nn)/2 - log b_pn` — SymmetrySignAmGm.delta."""
    return (mp.log(bpp) + mp.log(bnn)) / 2 - mp.log(bpn)


def a_A_eff(delta, k):
    """`E_0 . delta . k / 4` — the other probe's R5 formula, unchanged."""
    return E0 * delta * mp.mpf(k) / 4


def main() -> int:
    cap = 2 * mp.log(Q0)
    print(f"q0   = {mp.nstr(Q0, 25)}")
    print(f"E_0  = {mp.nstr(E0, 20)} MeV")
    print(f"cap  = 2 ln q0 = {mp.nstr(cap, 20)}")
    print(f"SEMF a_A target = {A_A_TARGET} MeV")

    # ------------------------------------------------------------ section 1
    hdr("[1] Reproducing the quoted cells, unchanged")

    b1 = bond_factors(1)
    d1 = energy_slope(b1["pp"], b1["pn"], b1["nn"])
    print(f"  m = 1:  b = ({mp.nstr(b1['pp'], 10)}, {mp.nstr(b1['pn'], 10)}, "
          f"{mp.nstr(b1['nn'], 10)})   delta = {mp.nstr(d1, 12)}")
    assert d1 < 0                                   # R4: wrong SEMF sign at m=1

    for k in (EXPRESSIBLE_DEGREE, QUOTED_DEGREE):
        v = a_A_eff(cap, k)
        print(f"  R5 cap at k = {k:2d}: {mp.nstr(v, 10):>14s} MeV   "
              f"({mp.nstr(A_A_TARGET / v, 6)}x short)")
    assert abs(a_A_eff(cap, 2) - mp.mpf("0.441")) < mp.mpf("0.002"), "R5 k=2"
    assert abs(a_A_eff(cap, 12) - mp.mpf("2.647")) < mp.mpf("0.002"), "R5 k=12"
    print("\n  Both reproduce the recorded R5 figures — the formula is untouched.")

    # ------------------------------------------------------------ section 2
    hdr("[2] The multiplicity scan at BOTH degrees")

    print("    m |     delta    | a_A^eff(k=12)  short | a_A^eff(k=2)   short")
    best12 = best2 = None
    for m in range(1, MAX_M + 1):
        bm = bond_factors(m)
        if min(bm.values()) <= 0:
            print(f"   {m:2d} | a bond factor is non-positive — log undefined")
            continue
        dm = energy_slope(bm["pp"], bm["pn"], bm["nn"])
        v12, v2 = a_A_eff(dm, 12), a_A_eff(dm, 2)
        print(f"   {m:2d} | {mp.nstr(dm, 10):>11s}  | {mp.nstr(v12, 8):>10s} "
              f"{mp.nstr(A_A_TARGET/v12, 6):>7s} | {mp.nstr(v2, 8):>10s} "
              f"{mp.nstr(A_A_TARGET/v2, 6):>7s}")
        if best12 is None or v12 > best12:
            best12 = v12
        if best2 is None or v2 > best2:
            best2 = v2

    print(f"\n  best over m at k = 12 : {mp.nstr(best12, 10)} MeV  "
          f"-> {mp.nstr(A_A_TARGET/best12, 6)}x short   <- the QUOTED headline")
    print(f"  best over m at k =  2 : {mp.nstr(best2, 10)} MeV  "
          f"-> {mp.nstr(A_A_TARGET/best2, 6)}x short   <- the EXPRESSIBLE degree")
    assert abs(best12 - mp.mpf("5.963")) < mp.mpf("0.002"), best12
    ratio = best12 / best2
    print(f"\n  the two differ by exactly the degree ratio 12/2 = 6: "
          f"{mp.nstr(ratio, 12)}")
    assert abs(ratio - 6) < mp.mpf(10) ** -30

    # ------------------------------------------------------------ section 3
    hdr("[3] Why k = 12 is not available")

    print("""  QOU.Mass.LinearLayoutNoBulk (sorry-free; PR #7155, merged):

    degree_le_two                    every vertex has at most two neighbours
    not_linearLayout_of_degree_ge_three
        "the max-contact packing (degree up to 12) and the complete graph
         (degree n-1) are not linear-layout graphs"
    card_edgeFinset_le               |E| <= n

  `atom_braid_word_3A` emits every inter-nucleon letter at generator `3k+2`, so
  the coordination graph of ANY word it can build is a subgraph of the path on
  the ordering.  Measured in that PR: all 246 words at A = 2..8, every ordering,
  position-based AND strand-tracked, are the path.

  So `k = 12` — the close-packed cell — is exactly the degree that result
  excludes, and `k = 2` — the chain — is what the encoding emits.""")

    # ------------------------------------------------------------ section 4
    hdr("[4] The corrected calibration figure")

    print(f"""  quoted    (k = 12, close-packed, NOT expressible):
      a_A^eff = {mp.nstr(best12, 10)} MeV   -> {mp.nstr(A_A_TARGET/best12, 6)}x short

  expressible (k = 2, the chain the encoding emits):
      a_A^eff = {mp.nstr(best2, 10)} MeV   -> {mp.nstr(A_A_TARGET/best2, 6)}x short

  The magnitude question's calibration number is therefore
  **{mp.nstr(A_A_TARGET/best2, 6)}x**, not 4.0x — a factor 6 wider, exactly the
  degree ratio.  Both cells use the SAME derived bond factors and the SAME
  formula; only `k` differs.

  AND THE m-SCAN IS ITSELF NOT AVAILABLE AS A SELECTION.  R9 of the source probe
  reports the whole `m = 1..12` table precisely because picking the `m` that
  maximises the residual is the discrete-parameter fit AGENTS.md's
  NO FITTING directive names.  At the canonical `m = 1` and the expressible
  `k = 2` the derived law gives {mp.nstr(a_A_eff(energy_slope(b1['pp'], b1['pn'], b1['nn']), 2), 8)} MeV
  — negative, since `delta < 0` there: the wrong SEMF sign, before magnitude is
  even reached.

  So the magnitude gap at the encoding's own layout and canonical multiplicity
  is not "4.0x" and not a shortfall at all — it is a SIGN failure, with the
  magnitude question arising only on cells the layout result excludes.""")

    # ------------------------------------------------------------ section 5
    hdr("[5] Scope")

    print("""  A scope correction to a quoted figure.  No derivation, bond factor or
  formula changes; `k` moves from the close-packed 12 to the expressible 2.
  It makes the gap WIDER, which is the direction that does not flatter the
  framework.

  NOT claimed: that `k = 2` is the right physical model (the well-mixed law is
  a mean-field model by its own docstring, and a chain is not well-mixed); that
  the magnitude question is closed, narrowed or reopened; that any bond family
  is excluded.  The bean stays open on exactly the question it had.

  INHERITED SCOPE LIMIT, and it is load-bearing.  `LinearLayoutNoBulk` is closed
  over the TEMPLATE encoding `atom_braid_word_3A` only -- the bean's own
  2026-09-13 note says so, and the gamma-gamma-selected words of owner ruling
  `qou-ales` have NOT been measured strand-tracked.  So the correct reading is:
  at the degree the TEMPLATE encoding can express, the figure is 23.8x.  If a
  gamma-gamma-selected word turns out to express a higher degree, the quoted
  4.0x could come back -- and that measurement is `qou-brng`'s existing open
  workplan item, not something settled here.""")

    print("\nPROBE OK — all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
