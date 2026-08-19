#!/usr/bin/env python3
"""
Probe — the collective term's SIGN SCREEN is regime-confined, and I over-stated it.

`collective_term_budget_probe.py` (PR #4973, my own) established three screens on
the missing many-body term `R(A) := B_AME/A - B_chain/A`. The SIGN screen read:

    "sign | -0.3041 at 2H, > 0 at all 13 heavier rows => MIXED-SIGN in A |
     kills anything manifestly non-negative *by construction* -- an entropy, a
     KL divergence, a dimension count, a sum of squares, a positive Plancherel
     weight"

That was measured on a **14-isotope** convenience sample. Run over the **full
AME2020 table** (3554 nuclides with Z>=1, N>=1, B>0) the screen does not hold as
stated.

## What the full table shows

**7 rows have R < 0. Every one has B_AME/A < 1.73 MeV/nucleon.**

    A  Z  N  nuclide   B_AME/A   status
    5  4  1  5Be        0.0180   particle-UNBOUND
    7  1  6  7H         0.9400   particle-UNBOUND
    6  1  5  6H         0.9616   particle-UNBOUND
    2  1  1  2H         1.1123   bound -- the weakest-bound stable nucleus
    4  3  1  4Li        1.1538   particle-UNBOUND
    5  1  4  5H         1.3364   particle-UNBOUND
    4  1  3  4H         1.7204   particle-UNBOUND

Six of the seven are **particle-unbound** drip-line exotics; the seventh is the
deuteron. Typical well-bound nuclei sit at 7-8.8 MeV/nucleon.

**Among the 3519 nuclides with B_AME/A > 5: ZERO negatives.** There

    R in [+2.1009, +5.8926]

— strictly positive, one-signed, and bounded within a factor of 2.8.

## Why this matters: the negatives measure a DIFFERENT, already-proved defect

The framework cannot produce an unbound or barely-bound nucleus at all:
`B_sym = a[(Z-1)L_pp + L_pn + (N-1)L_nn]` with every `L > 0` is positive for
every `(Z,N)` (the two-nucleon floor work; `single_crossing_binds`). So exactly
where nature has ~zero binding, the chain necessarily over-binds and `R < 0`.

The negative rows are therefore a re-measurement of the KNOWN structural defect —
the same one that makes the diproton and dineutron come out bound — not evidence
about the missing many-body term's sign structure. Using them to constrain a
collective term conflates the two.

## Correction to the screen, stated at the right scope

**Withdrawn as stated:** "the collective term is mixed-sign in A, so anything
non-negative by construction is excluded." That inference does not survive the
full table.

**Replacement, scope-(a):** on the well-bound regime (`B_AME/A > 5`, 3519 of
3554 nuclides = 99.0% of the chart) `R` is **strictly positive and bounded in
[2.10, 5.89] MeV/nucleon**. Non-negative candidates — an entropy, a KL
divergence, a dimension count, a positive Plancherel weight — are **NOT excluded
there**, and the earlier screen should not be cited to exclude them.

On the 7 drip-line rows `R < 0`, but the framework independently cannot model
those systems, so they constrain the *interface* defect rather than the
collective term.

## A hypothesis of mine that the measurement killed

I expected the negatives to be **2H alone**, on the reasoning that `R(2H)` is by
construction the deuteron's single-bond error and therefore contaminated. That
was wrong: there are seven, and six are not the deuteron. The correct statement
is about the *binding regime*, not about a single contaminated point — a
different and better-supported claim than the one I set out to make. Recorded
because the wrong version is the tidier story.

## What this changes for the search

A strictly-positive, bounded target is far better conditioned than a mixed-sign
one. The remaining two screens are unaffected:

* magnitude -- plateau `R/alpha = 1.3240` per nucleon, 1.90x the chain's own
  asymptote;
* scaling -- per `(A-1)` bond 19.4% spread on `A >= 24` vs per `C(A,2)` pair
  184.6%, the latter falling monotonically, so an unsuppressed all-pairs term is
  still excluded.

NO WITNESS: a subtraction over the committed AME2020 table plus the production
`_bond_type_L`; the tables reproduce it.

Bean qou-brg3 successor; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp

ALPHA = "4.1859813632944758969"
WELL_BOUND = "5.0"
NAMES = {(1, 1): "2H", (1, 3): "4H", (3, 1): "4Li", (1, 4): "5H",
         (4, 1): "5Be", (1, 5): "6H", (1, 6): "7H"}


def main() -> int:
    mp.mp.dps = 30
    import mass_binding_dashboard as M
    L = M._bond_type_L()
    ame = M._ame_table()
    a = mp.mpf(ALPHA)
    Lpp, Lpn, Lnn = L["pp"], L["pn"], L["nn"]

    rows = []
    for (Z, A), v in ame.items():
        N = A - Z
        if A < 2 or Z < 1 or N < 1:
            continue
        B = mp.mpf(str(v[0]))
        if B <= 0:
            continue
        ch = a * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
        rows.append((B / A, (B - ch) / A, A, Z, N))

    neg = sorted(r for r in rows if r[1] < 0)
    wb = [r for r in rows if r[0] > mp.mpf(WELL_BOUND)]

    print("The collective term's SIGN SCREEN is regime-confined — correcting my own.\n")
    print(f"  full AME2020 sample: {len(rows)} nuclides (Z>=1, N>=1, B>0)")
    print("  the original screen was measured on a 14-isotope convenience sample\n")
    print(f"## All {len(neg)} rows with R < 0\n")
    print("|  A |  Z |  N | nuclide | B_AME/A |       R | status |")
    print("| -: | -: | -: | ------- | ------: | ------: | ------ |")
    for b, R, A, Z, N in neg:
        st = "bound (weakest stable)" if (Z, N) == (1, 1) else "particle-UNBOUND"
        print(f"| {A:2d} | {Z:2d} | {N:2d} | {NAMES.get((Z, N), '?'):<7} "
              f"| {mp.nstr(b, 6):>9} | {mp.nstr(R, 6):>9} | {st} |")
    hi = max(b for b, _R, _A, _Z, _N in neg)
    print(f"\n  every negative row has B_AME/A <= {mp.nstr(hi, 6)}; typical well-bound is 7-8.8")
    print(f"  six of {len(neg)} are particle-unbound drip-line exotics\n")

    print(f"## The well-bound regime (B_AME/A > {WELL_BOUND})\n")
    print(f"  {len(wb)} of {len(rows)} nuclides = {100*len(wb)/len(rows):.1f}% of the chart")
    print(f"  R in [{mp.nstr(min(r[1] for r in wb), 6)}, {mp.nstr(max(r[1] for r in wb), 6)}] MeV/nucleon")
    print(f"  rows with R < 0 among them: {sum(1 for r in wb if r[1] < 0)}")
    print("  -> strictly positive, one-signed, bounded within a factor of "
          f"{mp.nstr(max(r[1] for r in wb) / min(r[1] for r in wb), 3)}\n")

    print("## Why the negatives are a DIFFERENT, already-proved defect\n")
    print("  B_sym = a[(Z-1)L_pp + L_pn + (N-1)L_nn] with every L > 0 is positive for")
    print("  every (Z,N) — the framework cannot produce an unbound nucleus at all")
    print("  (single_crossing_binds; the two-nucleon floor). So exactly where nature")
    print("  has ~zero binding, the chain must over-bind and R < 0. Those rows")
    print("  re-measure the KNOWN interface defect, not the collective term's sign.\n")

    print("## Correction, at the right scope\n")
    print("  WITHDRAWN as stated: 'the collective term is mixed-sign in A, so anything")
    print("  non-negative by construction is excluded.' It does not survive the full table.")
    print("  REPLACEMENT, scope-(a): on the well-bound regime R is strictly positive and")
    print("  bounded, so an entropy / KL divergence / dimension count / positive")
    print("  Plancherel weight is NOT excluded there. Do not cite the old screen to")
    print("  exclude them.\n")
    print("  A hypothesis the measurement killed: I expected the negatives to be 2H")
    print("  ALONE (R(2H) being by construction the deuteron's single-bond error, hence")
    print("  contaminated). Wrong — there are seven and six are not the deuteron. The")
    print("  correct claim is about the binding REGIME, not one contaminated point.")
    print("  Recorded because the wrong version is the tidier story.\n")
    print("  UNAFFECTED: the magnitude screen (R/alpha = 1.3240 per nucleon, 1.90x the")
    print("  chain asymptote) and the scaling screen (per (A-1) 19.4% vs per C(A,2)")
    print("  184.6% on A >= 24, so an unsuppressed all-pairs term stays excluded).")
    print("\n(no witness by design — a subtraction over the committed AME2020 table.)")

    assert all(b < mp.mpf("1.75") for b, _R, _A, _Z, _N in neg), "a negative row is well-bound"
    assert sum(1 for r in wb if r[1] < 0) == 0, "well-bound regime must be all-positive"
    return 0


if __name__ == "__main__":
    sys.exit(main())
