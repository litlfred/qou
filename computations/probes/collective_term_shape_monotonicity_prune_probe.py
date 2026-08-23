#!/usr/bin/env python3
"""Probe — shape-matching R against SEMF-like forms on the plateau sample is
uninformative BY CONSTRUCTION, and the fix is to vary Z at fixed A.

Bean qou-jh26 ranks the Delta_lambda EXTENSIVE term among the closeable items:
the six failed ansaetze were structural (they forced an extensive quantity into
an intensive per-block weight), so what is wanted is a separate additive
extensive object supplying

    R := B_AME/A - B_chain/A .

This probe asks two questions before any wide search, per the formalize-first
rule, and BOTH come back negative. Recording them is the point: each is a
direction a later agent would otherwise spend a session on.

## 1. Is R per-NUCLEON or per-BOND? Inconclusive.

A linear chain has A nucleons and A-1 bonds, so the two normalisations differ
most at small A. Over A >= 12 the relative spread is

    per-nucleon  0.1894        per-bond  0.1969

essentially identical. The data does not distinguish them. Worse, neither is
CONSTANT: R/A varies ~19% across A >= 12 and is NON-MONOTONE -- it rises
1.196 -> 1.408 through 56Fe and then DROPS to 1.165 at 208Pb. So R is not a
single extensive constant under either normalisation, and the framing "find the
extensive additive term" is under-specified as stated.

## 2. Does the 208Pb drop track Coulomb? THE CORRELATION IS AN ARTIFACT.

The drop is where a Coulomb term should bite, and the framework does have a
derived charge object (`def:coulomb-charge`, Q = 2Z + eps). Testing R/A against
Z^2/A^(4/3) over the five plateau nuclides 12C..56Fe gives r = 0.985, which
looks like a strong lead.

**It is not.** Z^2/A^(4/3) is monotone in A across that sample, and so is R/A,
so the correlation measures monotonicity and nothing else. Controls on the SAME
five points:

    Coulomb  Z^2/A^(4/3)   r = 0.985
    CONTROL  log A         r = 0.9961     <-- BEATS the Coulomb form
    CONTROL  sqrt(A)       r = 0.9847
    CONTROL  A^(2/3)       r = 0.9791
    CONTROL  A             r = 0.9654

`log A` -- which has no physical claim on R at all, and which the extensivity
prune already EXCLUDED as a binding functional -- scores higher than the
candidate. Any monotone-in-A ansatz scores r >~ 0.97 here. The correlation is
not evidence, and a coefficient fitted through it would be fitted to
monotonicity.

Including 208Pb the correlation reverses to r = -0.1518, so the entire
discriminating power of the sample sits in ONE nuclide. A shape claim resting
on one point is not a claim.

## What this prunes, and what to do instead

**Scope-(a).** Excluded: reading a correlation between R and any monotone-in-A
form, on a plateau sample, as evidence for that form. Not excluded: the
Coulomb term itself, which remains physically expected and has a derived object
in the corpus -- only this ROUTE to identifying it is void.

**The prescription.** Break the monotone degeneracy by varying Z at fixed or
near-fixed A -- isobars (A fixed, Z varying) or an isotopic chain. There
Z^2/A^(4/3) moves while A-driven surface/volume terms do not, so the two are
separable and a correlation carries information. That is a different data
request than the mass-ladder sample everything on this axis has used so far.

NO FLOAT64: AME and chain values as strings into mpmath, all arithmetic at
40 dps. NO WITNESS by design -- the tables reproduce every number, and nothing
here is wired.

Bean qou-jh26.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp

E0_STR = "4.1859813632944758969"

# (label, Z, A, B_AME/A, B_chain/A) — production _bond_type_L, convention D,
# proton pin; same table the collective-term budget probe emits.
ROWS = [
    ("2H", 1, 2, "1.1123", "1.4164"), ("3H", 1, 3, "2.8273", "2.0466"),
    ("3He", 2, 3, "2.5727", "1.7915"), ("4He", 2, 4, "7.0739", "2.1703"),
    ("6Li", 3, 6, "5.3323", "2.4216"), ("12C", 6, 12, "7.6801", "2.6729"),
    ("16O", 8, 16, "7.9762", "2.7358"), ("24Mg", 12, 24, "8.2607", "2.7986"),
    ("40Ca", 20, 40, "8.5513", "2.8489"), ("56Fe", 26, 56, "8.7904", "2.8977"),
    ("208Pb", 82, 208, "7.8675", "2.9907"),
]


def _pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = mp.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    return num / den if den else mp.mpf(0)


def main() -> int:
    mp.mp.dps = 40
    E0 = mp.mpf(E0_STR)

    print("Two structural questions about R, asked BEFORE any wide search.\n")

    # ---- 1. per-nucleon vs per-bond -------------------------------------
    print("1. IS R PER-NUCLEON OR PER-BOND?  (a chain has A nucleons, A-1 bonds)\n")
    print(f"   {'iso':<7}{'A':>5}{'R_tot/E0':>12}{'/A':>10}{'/(A-1)':>10}")
    per_n, per_b = [], []
    for lab, _Z, A, ame, ch in ROWS:
        Rtot = (mp.mpf(ame) - mp.mpf(ch)) * A / E0
        a, b = Rtot / A, Rtot / (A - 1)
        if A >= 12:
            per_n.append(a)
            per_b.append(b)
        print(f"   {lab:<7}{A:>5}{mp.nstr(Rtot, 6):>12}"
              f"{mp.nstr(a, 5):>10}{mp.nstr(b, 5):>10}")

    def spread(v):
        return (max(v) - min(v)) / (sum(v) / len(v))

    sn, sb = spread(per_n), spread(per_b)
    print(f"\n   A>=12 relative spread   per-NUCLEON {mp.nstr(sn, 4)}"
          f"   per-BOND {mp.nstr(sb, 4)}")
    print("   -> INCONCLUSIVE: the two normalisations are indistinguishable.")
    print("      And neither is CONSTANT -- ~19% spread, and NON-MONOTONE")
    print("      (rises to 56Fe, drops at 208Pb). R is not a single extensive")
    print("      constant, so 'find the extensive term' is under-specified.\n")

    # ---- 2. the Coulomb shape lead, and its control ----------------------
    print("2. DOES THE 208Pb DROP TRACK COULOMB?  The correlation is an ARTIFACT.\n")
    plateau = [r for r in ROWS if r[2] >= 12 and r[0] != "208Pb"]
    R = [(mp.mpf(a) - mp.mpf(c)) / E0 for _l, _Z, _A, a, c in plateau]
    A_ = [mp.mpf(A) for _l, _Z, A, _a, _c in plateau]
    cands = {
        "Coulomb  Z^2/A^(4/3)": [mp.mpf(Z) ** 2 / mp.mpf(A) ** mp.mpf("4/3")
                                 for _l, Z, A, _a, _c in plateau],
        "CONTROL  log A      ": [mp.log(a) for a in A_],
        "CONTROL  sqrt(A)    ": [mp.sqrt(a) for a in A_],
        "CONTROL  A^(2/3)    ": [a ** mp.mpf("2/3") for a in A_],
        "CONTROL  A          ": A_,
    }
    print("   Pearson r of R/A against each, over the SAME five plateau points:")
    rs = {}
    for k, v in cands.items():
        rs[k] = _pearson(v, R)
        print(f"     {k}   r = {mp.nstr(rs[k], 4)}")

    coul = rs["Coulomb  Z^2/A^(4/3)"]
    best_ctrl = max(v for k, v in rs.items() if k.startswith("CONTROL"))
    print(f"\n   `log A` scores {mp.nstr(best_ctrl, 4)} — HIGHER than the Coulomb")
    print(f"   form's {mp.nstr(coul, 4)}. Every monotone control clears 0.96.")
    print("   Z^2/A^(4/3) is monotone in A here and so is R/A, so the")
    print("   correlation measures MONOTONICITY, not Coulomb. A coefficient")
    print("   fitted through it would be fitted to monotonicity.\n")

    allrows = [r for r in ROWS if r[2] >= 12]
    Rall = [(mp.mpf(a) - mp.mpf(c)) / E0 for _l, _Z, _A, a, c in allrows]
    call = [mp.mpf(Z) ** 2 / mp.mpf(A) ** mp.mpf("4/3")
            for _l, Z, A, _a, _c in allrows]
    r_all = _pearson(call, Rall)
    print(f"   Including 208Pb the correlation REVERSES: r = {mp.nstr(r_all, 4)}.")
    print("   So the entire discriminating power sits in ONE nuclide. A shape")
    print("   claim resting on one point is not a claim.\n")

    print("WHAT THIS PRUNES, AND WHAT TO DO INSTEAD\n")
    print("   Scope-(a). Excluded: reading a correlation between R and any")
    print("   monotone-in-A form, on a plateau sample, as evidence for that")
    print("   form. NOT excluded: the Coulomb term itself, which stays")
    print("   physically expected and has a derived object in the corpus")
    print("   (def:coulomb-charge, Q = 2Z + eps). Only this ROUTE is void.\n")
    print("   Prescription: break the degeneracy by varying Z at fixed or")
    print("   near-fixed A -- isobars, or an isotopic chain. There Z^2/A^(4/3)")
    print("   moves while the A-driven surface/volume terms do not, so the two")
    print("   separate and a correlation carries information. That is a")
    print("   different data request than the mass ladder used so far.\n")

    # ---- guards ----------------------------------------------------------
    assert abs(sn - sb) < mp.mpf("0.05"), \
        "per-nucleon vs per-bond should be indistinguishable on this sample"
    assert best_ctrl > coul, \
        "the point of this probe is that a CONTROL beats the Coulomb form"
    assert r_all < 0, "including 208Pb should reverse the sign"
    print("(no witness by design — the tables reproduce every number.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
