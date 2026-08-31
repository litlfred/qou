#!/usr/bin/env python3
"""every_seifert_invariant_is_affine_probe.py

Not just the crossing count: EVERY Seifert invariant of the canonical braid
closure is affine in A. The framework's nuclear encoding has no sub-linear
geometric content at all, so no surface term can come out of it.

WHY THIS EXISTS
---------------
`braid_crossing_count_is_extensive_probe` excluded the crossing count as a
surface term (crossings = 12A - 1, affine, and a strictly-monotone ratio
against A^(2/3) forbids any constant coefficient -- scope-(b), proved in
`QOU.Mass.AffineCountIsNotASurfaceTerm`). It closed by saying the Stokes route
needs the SPANNING SURFACE rather than the braid word, and named the Seifert
surface as the thing to build.

Built. It does not help, and the reason is more general than the crossing count.

MEASURED on the six N=Z self-conjugate nuclei, from the Seifert algorithm on a
braid closure (Seifert circles = strands, bands = crossings, chi = n - l, and
chi = 2 - 2g - mu for the connected surface):

    A     n     l     chi    mu    g
    2     6    23    -17     3     8
    4    12    47    -35     5    16
    6    18    71    -53     7    24
    8    24    95    -71     9    32
   12    36   143   -107    13    48
   16    48   191   -143    17    64

Every one is exactly affine:

    n_strands       = 3A
    crossings       = 12A - 1
    euler_char      = -9A + 1
    components mu   =   A + 1
    SEIFERT GENUS g =  4A          (exact, integral, all six)

The crossing-type census is affine too: sigma = 6A - 1, sigma_inv = 4A - 1,
averaged = 2A, and averaged_weighted = 1 -- exactly one, independent of A.

CONSEQUENCE
-----------
The previous exclusion was for one invariant. This is for the package: there is
no Seifert quantity of this construction that scales as A^(2/3), because the
construction is affine in A in EVERY coordinate. The same strictly-monotone
argument (`no_constant_surface_coefficient`) applies verbatim to each: an affine
function and c*A^(2/3) agree at no two mass numbers.

So the gap is UPSTREAM of the surface term. It is not that the framework has a
surface and we have not measured it correctly; the framework's nuclear encoding
has no surface -- it is a word of length linear in A on a strand count linear in
A, and every derived invariant inherits that. A surface term must come from
geometry the encoding does not currently carry.

The single `averaged_weighted` crossing is the ONLY non-extensive feature
anywhere in the construction: O(1), the same one crossing at every A. O(1) is
not A^(2/3) either, but it is the one place a non-extensive quantity exists, and
it is recorded here for whoever looks next.

A NOTE ON HOW THIS WAS NEARLY MISREPORTED
-----------------------------------------
My first pass assumed 1-based braid generators and got a half-integral genus
(7.5, 15.5, ...) and "Seifert graph components = 2", which reads as a SPLIT
canonical closure -- a striking claim about the framework. It was my bug: the
generators are 0-based (0 .. n-2, all present). The internal contradiction that
caught it was the script printing "gens used = 5/5" beside "missing = [5]". The
corrected data is connected, integral, and above.

NO FLOAT64: integer arithmetic throughout; no floating point is used or needed.
"""

import sys
from collections import Counter
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

CHAIN = [(1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (8, 8)]


def seifert(Z, N):
    """Seifert data of the canonical braid closure. 0-based generators."""
    A = Z + N
    w = atom_canonical_crossings(Z, N)
    n, ell = 3 * A, len(w)
    perm = list(range(n))
    for g, _ in w:
        i = int(g)
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    seen, mu = [False] * n, 0
    for s in range(n):
        if not seen[s]:
            mu += 1
            c = s
            while not seen[c]:
                seen[c] = True
                c = perm[c]
    chi = n - ell
    two_g = 2 - mu - chi
    return dict(A=A, n=n, ell=ell, chi=chi, mu=mu, two_g=two_g,
                types=Counter(t for _, t in w))


def main():
    wb = WitnessBuilder("every-seifert-invariant-is-affine", engine="python-int")
    wb.set_description(
        "EVERY Seifert invariant of the canonical braid closure is exactly "
        "affine in A on the six N=Z nuclei: n=3A, crossings=12A-1, chi=-9A+1, "
        "components=A+1, GENUS=4A. So the previous scope-(b) exclusion of the "
        "crossing count as a surface term extends to the whole Seifert package "
        "-- no invariant of this construction scales as A^(2/3), because the "
        "construction is affine in every coordinate. The gap is UPSTREAM: the "
        "framework's nuclear encoding has no surface to measure. The single "
        "`averaged_weighted` crossing (exactly 1 at every A) is the only "
        "non-extensive feature anywhere in it."
    )

    ok = True
    forms = {
        "n_strands": lambda A: 3 * A,
        "crossings": lambda A: 12 * A - 1,
        "euler_char": lambda A: -9 * A + 1,
        "components": lambda A: A + 1,
        "two_genus": lambda A: 8 * A,
    }
    rows, mismatches = {}, []

    print(f"{'A':>3s}{'n':>5s}{'l':>6s}{'chi':>7s}{'mu':>5s}{'g':>5s}"
          f"   sigma sigma_inv averaged avg_wtd")
    for Z, N in CHAIN:
        d = seifert(Z, N)
        A = d["A"]
        t = d["types"]
        rows[A] = d
        got = {"n_strands": d["n"], "crossings": d["ell"],
               "euler_char": d["chi"], "components": d["mu"],
               "two_genus": d["two_g"]}
        for k, f in forms.items():
            if got[k] != f(A):
                mismatches.append((A, k, got[k], f(A)))
        print(f"{A:>3d}{d['n']:>5d}{d['ell']:>6d}{d['chi']:>7d}{d['mu']:>5d}"
              f"{d['two_g'] // 2:>5d}   {t['sigma']:>5d} {t['sigma_inv']:>9d} "
              f"{t['averaged']:>8d} {t['averaged_weighted']:>7d}")

    print("\nexact affine forms: n=3A, crossings=12A-1, chi=-9A+1, "
          "mu=A+1, genus=4A")
    wb.add_data("seifert_chain", {
        str(A): {"n_strands": d["n"], "crossings": d["ell"],
                 "euler_char": d["chi"], "components": d["mu"],
                 "genus": d["two_g"] // 2,
                 "types": dict(d["types"])}
        for A, d in rows.items()})
    wb.add_data("affine_forms", {
        "n_strands": "3A", "crossings": "12A - 1", "euler_char": "-9A + 1",
        "components": "A + 1", "genus": "4A",
        "sigma": "6A - 1", "sigma_inv": "4A - 1", "averaged": "2A",
        "averaged_weighted": "1 (the ONLY non-extensive feature)"})

    wb.add_assertion(
        name="every_seifert_invariant_is_exactly_affine_in_A",
        computed=str(len(mismatches)), expected="0", tolerance="0",
        unit="mismatches against the affine forms over 5 invariants x 6 nuclei",
        source=("n=3A, crossings=12A-1, chi=-9A+1, mu=A+1, 2g=8A; all exact, "
                "all integral, all six N=Z nuclei"))
    if mismatches:
        ok = False
        print(f"   FAIL: {mismatches[:4]}")

    # genus specifically, since it was the named next step
    genera = {A: d["two_g"] // 2 for A, d in rows.items()}
    wb.add_assertion(
        name="seifert_genus_is_exactly_four_A",
        computed=str(all(g == 4 * A for A, g in genera.items())),
        expected="True", tolerance="0",
        unit="genus = 4A on all six",
        source=("the spanning surface named as the next step: built, and it is "
                "linear in A like everything else in the construction"))
    if not all(g == 4 * A for A, g in genera.items()):
        ok = False
        print("   FAIL: genus is not 4A")

    # the one O(1) feature
    aw = {A: d["types"]["averaged_weighted"] for A, d in rows.items()}
    wb.add_assertion(
        name="exactly_one_averaged_weighted_crossing_at_every_A",
        computed=str(sorted(set(aw.values()))), expected="[1]", tolerance="0",
        unit="distinct counts of averaged_weighted across the chain",
        source=("the only non-extensive feature in the construction: O(1), not "
                "O(A). O(1) is not A^(2/3) either, but it is the one place a "
                "non-extensive quantity exists here"))
    if sorted(set(aw.values())) != [1]:
        ok = False
        print("   FAIL: averaged_weighted is not always 1")

    wb.add_data("consequence", {
        "scope": ("(b) for any Seifert invariant of THIS construction as a "
                  "surface term, via QOU.Mass.AffineCountIsNotASurfaceTerm's "
                  "strictly-monotone ratio, which applies verbatim to each "
                  "affine invariant"),
        "where_the_gap_actually_is": ("upstream of the surface term: the "
                                      "encoding is a word of length linear in A "
                                      "on a strand count linear in A, so every "
                                      "derived invariant inherits that. A "
                                      "surface term needs geometry the encoding "
                                      "does not carry"),
        "indexing_bug_recorded": ("a first pass assumed 1-based generators, got "
                                  "half-integral genus and 'components = 2', "
                                  "which reads as a SPLIT canonical closure. "
                                  "That was my bug -- generators are 0-based, "
                                  "0..n-2, all present. Caught by the script "
                                  "printing 'gens used = 5/5' beside "
                                  "'missing = [5]'"),
    })

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
