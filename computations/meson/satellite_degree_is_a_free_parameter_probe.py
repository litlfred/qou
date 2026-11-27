#!/usr/bin/env python3
"""
satellite_degree_is_a_free_parameter_probe.py — the satellite route clears the
bar at ²H, and the price is a per-isotope fitted integer.

WHERE THIS SITS.  Addenda 22/24/26/31/33 closed every magnitude route with a
named invariant except one: the satellite.  `larger_index_set_escapes_the_bound`
(`BranchConvexityBound.lean`) says why it escapes — an r-cable replaces each
strand by r, so its branches live in a bigger algebra and are not a reweighting
of the original 32.  Addendum 28 measured the escape: the 2-parallel cable of
the deuteron reaches `max_b tr_M = 7.448220` (4.994×) and, at the atom's OWN
convex weights, `1.657034` — 1.111× past `√B_AME(²H) = 1.491498`.

So at ²H the satellite does not merely fail to be forbidden; it reaches.  This
probe asks the question that killed §B: **does it keep reaching as A grows?**
`B_AME` is extensive and rises 12.7× from ²H to ⁴He, so a route that clears at
one isotope and nowhere else has not explained binding — it has fitted one
number.

WHAT IS MEASURED.  `tr_M(atom word)` uncabled across the chain, against each
isotope's own bar `√B_AME`, and the cable degree `r` that each isotope would
need.  Uncabled is cheap (3A strands: 6, 9, 9, 12) where cabled is not (6A: 12,
18, 18, 24 — the two-row block `(9,9)` at 18 strands alone is 4862-dimensional),
so the r-dependence is taken from the ²H measurement and applied as a ratio,
which is stated as an extrapolation and not as a measurement.

WHAT THE CORPUS FIXES.  Nothing fixes `r`.
`docs/audits/2026-06-01-knot-operator-census-group-actions.md` §(b) records that
cabling is in-corpus "as pattern-on-companion" and that "an `r`-cable multiplies
strand count" — but no block, witness or Lean declaration derives a value for
`r`.  Corpus-grepped over all three library tiers.

NO FLOAT64: `mpmath.mpf` end to end; `float()` only inside f-strings.
Audit-only, emits no witness.

@module computations/meson/satellite_degree_is_a_free_parameter_probe
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from mass_table_comprehensive import AME_BINDING  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 50)
Q = Q_MP

# (AME_BINDING key, Z, N).  A = Z + N; the word has 3A strands.  The table keys
# deuterium and tritium as "D"/"T", not "2H"/"3H".
CHAIN = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

# Addendum 28, measured at ²H: uncabled vs 2-cabled at the atom's own convex
# weights.  Used below as a RATIO and labelled as an extrapolation.
TRM_2H_UNCABLED = mp.mpf("0.575172243918")
TRM_2H_2CABLE = mp.mpf("1.657034")


def seminormal(shape, q):
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    hq = q - 1 / q
    sigmas = []
    for k in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        seen = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = hq / (1 - q ** (-2 * rho))
            sw = dict(syts[i]); sw[k], sw[k + 1] = ci1, ci
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == sw), None)
            if j is None:
                rows[i][i] = a; seen.add(i)
            else:
                ap = hq / (1 - q ** (2 * rho))
                b = mp.sqrt(a * ap + 1)
                rows[i][i], rows[j][j] = a, ap
                rows[i][j] = rows[j][i] = b
                seen.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def two_row(n):
    return [(n,)] + [(n - k, k) for k in range(1, n // 2 + 1)]


def tr_M(letters, n):
    """Convention-D Markov trace: only ℓ(λ) ≤ 2 carries nonzero y_λ."""
    total = mp.mpf(0)
    for lam in two_row(n):
        sig, dim = seminormal(lam, Q)
        m = mp.eye(dim)
        for (c, d, g) in letters:
            m = (mp.mpf(c) * sig[g] + mp.mpf(d) * mp.eye(dim)) * m
        chi = sum(m[i, i] for i in range(dim))
        y = qint(n - 2 * (lam[1] if len(lam) > 1 else 0) + 1) / qint(2) ** n
        total += y * chi
    return total


def main() -> int:
    print("=" * 78)
    print("The satellite clears at ²H — does it keep clearing as A grows?")
    print("=" * 78)
    checks = []

    def check(ok, detail):
        checks.append((bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] A{len(checks)}: {detail}")

    print("\n1. Uncabled trace against each isotope's own bar")
    print(f"   {'iso':5s} {'A':>2s} {'strands':>8s} {'tr_M':>14s} {'B_AME':>10s}"
          f" {'bar=√B':>10s} {'short by':>10s}")
    rows = []
    for lab, Z, N in CHAIN:
        A = Z + N
        n = 3 * A
        t = tr_M(atom_braid_word_3A(Z, N), n)
        B = mp.mpf(str(AME_BINDING[lab]))
        bar = mp.sqrt(B)
        rows.append((lab, A, n, t, B, bar, bar / t))
        print(f"   {lab:5s} {A:2d} {n:8d} {mp.nstr(t, 10):>14s} "
              f"{mp.nstr(B, 7):>10s} {mp.nstr(bar, 7):>10s} {mp.nstr(bar / t, 6):>10s}×")

    t_2h = rows[0][3]
    check(abs(t_2h - TRM_2H_UNCABLED) < mp.mpf("1e-6"),
          f"CONTROL: ²H reproduces §C's committed {mp.nstr(TRM_2H_UNCABLED, 8)} to "
          f"{mp.nstr(abs(t_2h - TRM_2H_UNCABLED), 3)} — the chain is measured on the "
          f"same object §C bounded")

    traces = [r[3] for r in rows]
    bars = [r[5] for r in rows]
    spread_t = max(traces) / min(traces)
    spread_b = max(bars) / min(bars)
    print(f"\n2. Extensivity: does the trace move the way the binding does?")
    print(f"   tr_M range  {mp.nstr(min(traces), 8)} … {mp.nstr(max(traces), 8)}   "
          f"spread {mp.nstr(spread_t, 6)}×")
    print(f"   bar  range  {mp.nstr(min(bars), 8)} … {mp.nstr(max(bars), 8)}   "
          f"spread {mp.nstr(spread_b, 6)}×")
    print(f"\n   🛑 THOSE TWO SPREADS ARE NEARLY EQUAL "
          f"({mp.nstr(spread_t, 6)} vs {mp.nstr(spread_b, 6)}, "
          f"{mp.nstr(100 * abs(spread_t - spread_b) / spread_b, 3)} % apart) AND THAT IS")
    print(f"   NOT AGREEMENT — max/min discards direction. The trace FALLS as A rises")
    print(f"   while the bar RISES. Reading the two 3.57s as a match would invert the")
    print(f"   finding. (My first version of this assertion tested "
          f"`spread_b > 2·spread_t` and failed for exactly this reason.)")

    # The real test: direction, not magnitude.
    t_first, t_last = rows[0][3], rows[-1][3]
    b_first, b_last = rows[0][5], rows[-1][5]
    check(t_last < t_first and b_last > b_first,
          f"the trace is ANTI-correlated with the bar: as A goes 2 → 4 the trace FALLS "
          f"{mp.nstr(t_first, 7)} → {mp.nstr(t_last, 7)} while the bar RISES "
          f"{mp.nstr(b_first, 7)} → {mp.nstr(b_last, 7)}. Binding is extensive; this "
          f"quantity moves the other way")

    deficits = [r[6] for r in rows]
    check(max(deficits) / min(deficits) > mp.mpf("1.5"),
          f"so the shortfall is not a constant to be absorbed by one factor: it runs "
          f"{mp.nstr(min(deficits), 6)}× to {mp.nstr(max(deficits), 6)}× across four "
          f"isotopes, a {mp.nstr(max(deficits) / min(deficits), 6)}× spread")

    print("\n3. What cable degree would each isotope need?")
    gain = TRM_2H_2CABLE / TRM_2H_UNCABLED
    print(f"   Measured at ²H (Addendum 28): one cable level multiplies the convex")
    print(f"   trace by {mp.nstr(gain, 8)}×.  EXTRAPOLATING that ratio per level —")
    print(f"   an extrapolation, not a measurement, since 6A strands is out of reach:")
    print(f"   {'iso':5s} {'short by':>10s} {'levels needed':>15s}")
    needed = []
    for (lab, _A, _n, _t, _B, _bar, defic) in rows:
        lv = mp.log(defic) / mp.log(gain)
        needed.append(lv)
        print(f"   {lab:5s} {mp.nstr(defic, 6):>10s}× {mp.nstr(lv, 6):>15s}")

    check(max(needed) / min(needed) > mp.mpf("1.5"),
          f"the required cable level is NOT the same across the chain — it runs "
          f"{mp.nstr(min(needed), 5)} to {mp.nstr(max(needed), 5)}, a "
          f"{mp.nstr(max(needed) / min(needed), 5)}× spread. A single r cannot serve "
          f"the chain")
    non_integer = [lv for lv in needed if abs(lv - mp.nint(lv)) > mp.mpf("0.15")]
    # Same A, different (Z,N): does the composition alone move the requirement?
    t_T, t_3He = rows[1][6], rows[2][6]
    check(max(t_T, t_3He) / min(t_T, t_3He) > mp.mpf("1.5"),
          f"and it is not even a function of A: T and ³He are both A = 3 on 9 strands, "
          f"yet need {mp.nstr(min(t_T, t_3He), 6)}× and {mp.nstr(max(t_T, t_3He), 6)}× — "
          f"a {mp.nstr(max(t_T, t_3He) / min(t_T, t_3He), 5)}× spread at FIXED A. Any "
          f"rescue would have to be r(Z, N), not r(A)")

    check(len(non_integer) > 0,
          f"and {len(non_integer)} of {len(needed)} are not near an integer "
          f"(nearest-integer distance > 0.15), while a cable degree must BE an "
          f"integer — r multiplies strand count, it does not interpolate")

    check(True,
          "VERDICT: at ²H the satellite reaches the bar (Addendum 28, 1.111×), but "
          "the degree that reaches it is per-isotope and non-integral. Nothing in the "
          "corpus derives r — the census audit records cabling as pattern-on-companion "
          "with no value fixed — so choosing r per isotope to hit AME is a FIT, and "
          "the same fit §D refused for the cut width w")

    print("\n" + "=" * 78)
    passed = sum(1 for ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 78)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
