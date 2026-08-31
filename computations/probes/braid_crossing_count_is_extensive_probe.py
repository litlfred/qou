#!/usr/bin/env python3
"""braid_crossing_count_is_extensive_probe.py

The Stokes singularity-count route, tested: the canonical braid's crossing
count is AFFINE in A, so it cannot be the surface term. Scope-(b).

WHY THIS EXISTS
---------------
`docs/audits/2026-08-30-nonabelian-stokes-and-the-surface-term.md` unpacked
Yekutieli's non-abelian Stokes construction and found a genuine bulk/boundary
split: the Riemann-product estimate has a good term counted by 2-cells (area)
and a bad term with |bad(tau,k)| <= a0 + a1*2^k -- one dimension down -- where
an index is BAD exactly when the map is not linear and injective, bounded by
the number of SINGULAR POINTS of the map. That audit closed with a falsifiable
prediction: if the framework's surface term arises this way, a_S should be
proportional to a singularity count of the spanning surface. For a knot diagram
the natural such count is the CROSSING NUMBER, and the framework supplies one
per nucleus (`canonical_braid_crossings.atom_canonical_crossings`).

This is that test. It fails, structurally.

MEASURED on the six N=Z self-conjugate nuclei (no mirror convention anywhere):

    A= 2  crossings= 23      A= 8  crossings= 95
    A= 4  crossings= 47      A=12  crossings=143
    A= 6  crossings= 71      A=16  crossings=191

    crossings = 12*A - 1  EXACTLY, all six.

Since n_strands = 3*A, that is 4*n_strands - 1: the construction places four
crossings per strand and the strand count is linear in A. The crossing count is
therefore EXTENSIVE (volume-like) BY CONSTRUCTION, not as a numerical accident.

WHY THAT IS AN EXCLUSION, NOT A MISS
------------------------------------
A surface term scales as A^(2/3). In the cube variable m = A^(1/3) the ratio of
count to surface is

    (12*m^3 - 1) / m^2  =  12*m - 1/m^2

which is STRICTLY MONOTONE on m > 0, hence injective, hence constant at no two
distinct points. So no single coefficient makes the crossing count a surface
term at even two mass numbers, let alone six. Proved sorry-free in
`QOU.Mass.AffineCountIsNotASurfaceTerm.no_constant_surface_coefficient`.

Scope-(b) is claimed ONLY for the form "crossing count times a constant", and
only because that proved invariant licenses it. Whether crossings play some
other role in a closure is untouched and stays scope-(a).

Quantitatively, for the record: the deficit/crossings ratio spreads 580.7% over
the chain and deficit/A^(2/3) spreads 227.9%. Neither is constant. But the
numbers are not the argument -- the monotonicity theorem is; the numbers would
not become evidence if they happened to be closer.

WHAT THIS ACTUALLY TELLS US -- the useful half
----------------------------------------------
Yekutieli's split lives on a KITE: a 1-simplex plus a 2-simplex, with the bad
set stratifying a 2-dimensional cell structure. The framework's canonical braid
is a WORD -- a 1-dimensional object. A word has no 2-cell structure to
stratify, so its crossing count is the wrong kind of object for the bad-set
role no matter what its coefficient is.

So the Stokes route is not refuted; it is untestable against the CURRENT braid
encoding. Testing it needs the spanning surface (Seifert surface: genus,
boundary components, or a genuine 2-cell decomposition), which the framework
does not presently construct. That is a sharper and more actionable statement
of the gap than "find a mechanism".

NO FLOAT64: mpmath 65 dps; AME from the vendored table; q0 via Q_MP.
"""

import sys
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

import canonical_mass as cm  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 65

CHAIN = [(1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (8, 8)]


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def main():
    wb = WitnessBuilder("braid-crossing-count-is-extensive", engine="mpmath")
    wb.set_description(
        "Tests the prediction from the non-abelian Stokes audit that the "
        "surface coefficient a_S tracks a singularity count. The canonical "
        "braid's crossing count is 12*A - 1 EXACTLY on all six N=Z nuclei "
        "(= 4*n_strands - 1), hence affine in A and extensive by construction. "
        "A surface term scales as A^(2/3), and (12m^3-1)/m^2 = 12m - 1/m^2 is "
        "strictly monotone, so no constant coefficient works at even two mass "
        "numbers (QOU.Mass.AffineCountIsNotASurfaceTerm). Scope-(b) for that "
        "form only. The useful half: Yekutieli's bad set stratifies a 2-cell "
        "structure and a braid WORD is 1-dimensional, so the route needs the "
        "spanning surface, which the framework does not construct."
    )

    q = +Q_MP
    aV = cm.proton_mass_mev() * (1 - 1 / q) ** 2
    ok = True

    print(f"{'A':>3s}{'crossings':>11s}{'12A-1':>8s}{'match':>7s}"
          f"{'deficit':>12s}{'def/cross':>12s}{'def/A^(2/3)':>13s}")
    rows, r_cross, r_surf = {}, [], []
    all_match = True
    for Z, N in CHAIN:
        A = Z + N
        c = len(atom_canonical_crossings(Z, N))
        pred = 12 * A - 1
        all_match &= (c == pred)
        d = aV * A - B(Z, A)
        x = d / c
        y = d / mp.mpf(A) ** (mp.mpf(2) / 3)
        r_cross.append(x)
        r_surf.append(y)
        rows[A] = (c, d, x, y)
        print(f"{A:>3d}{c:>11d}{pred:>8d}{'YES' if c == pred else 'NO':>7s}"
              f"{mp.nstr(d,7):>12s}{mp.nstr(x,6):>12s}{mp.nstr(y,6):>13s}")

    wb.add_data("chain", {str(A): {"crossings": c, "deficit_MeV": fmt(d),
                                   "deficit_per_crossing": fmt(x),
                                   "deficit_per_A23": fmt(y)}
                          for A, (c, d, x, y) in rows.items()})

    wb.add_assertion(
        name="crossing_count_is_exactly_twelve_A_minus_one",
        computed=str(all_match), expected="True", tolerance="0",
        unit="exact match on all six N=Z nuclei",
        source=("n_strands = 3A and the construction places 4 crossings per "
                "strand, so crossings = 4*n_strands - 1 = 12A - 1: affine in "
                "A, extensive BY CONSTRUCTION"))
    if not all_match:
        ok = False
        print("   FAIL: crossing count is not 12A-1")

    def spread(r):
        lo, hi = min(r), max(r)
        return (hi - lo) / min(abs(v) for v in r)

    sc, ss = spread(r_cross), spread(r_surf)
    print(f"\ndeficit/crossings spread {mp.nstr(sc*100,5)} %"
          f"   deficit/A^(2/3) spread {mp.nstr(ss*100,5)} %")
    wb.add_data("ratio_spreads", {
        "deficit_per_crossing": fmt(sc), "deficit_per_A23": fmt(ss),
        "note": ("recorded for completeness; the ARGUMENT is the monotonicity "
                 "theorem, not these numbers -- they would not become evidence "
                 "if they happened to be closer")})
    wb.add_assertion(
        name="neither_ratio_is_constant",
        computed=fmt(min(sc, ss)), expected="2.279", tolerance="0.01",
        unit="smaller of the two fractional spreads",
        source="deficit/crossings 580.7%, deficit/A^(2/3) 227.9%")
    if abs(min(sc, ss) - mp.mpf("2.279")) > mp.mpf("0.01"):
        ok = False
        print("   FAIL: spread moved")

    wb.add_data("what_the_route_needs_instead", {
        "why_untestable_here": ("Yekutieli's bad set stratifies a 2-dimensional "
                                "cell structure (a kite: 1-simplex + 2-simplex); "
                                "a braid WORD is 1-dimensional and has no 2-cell "
                                "structure to stratify"),
        "what_would_test_it": ("the spanning surface -- Seifert genus, boundary "
                               "components, or a genuine 2-cell decomposition -- "
                               "which the framework does not presently construct"),
        "scope": ("(b) for 'crossing count times a constant' via the proved "
                  "monotonicity invariant; (a) for any wider claim about "
                  "crossings"),
    })

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
