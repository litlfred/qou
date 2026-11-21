#!/usr/bin/env python3
"""
growing_width_cut_shape_exclusion_probe.py — the growing-width cut is excluded
by the very extensivity that made it look promising, and no value of `w` is
chosen (or needs to be) to see it.

THE FRONT, inherited.  Addendum 23 Front 1 measured the cut entropy

    S(k) = - sum_{mu |- k, ell(mu) <= 2}  f^mu y^{(k)}_mu ln y^{(k)}_mu ,
    y^{(k)}_{(k-j,j)} = [k - 2j + 1]_q / [2]_q^k ,

found it EXTENSIVE (`S(k)/k -> ln[2]_q`), and left the front OPEN with the
verdict *"`w` is a free parameter, and that is the whole problem"* — matching
would fix `w ~ 2.9`, which nothing derives.

THE MOVE HERE.  Do not try to derive `w`.  Ask instead whether ANY constant `w`
can work — and the answer is no, for a reason that needs no fit and survives an
arbitrary overall rescaling on top of `w`:

  * `S(k)/k` is INCREASING in `k` (measured below, monotone over 1..64, rising
    to `ln[2]_q` strictly from below).
  * Hence for fixed `w` the model's per-nucleon prediction
    `g_w(A) := E0*S(floor(wA))/A` is NON-DECREASING in `A`.
  * But the AME per-nucleon binding is NOT: it PEAKS at 4He (7.0739 MeV) and
    DIPS at 6Li (5.3323 MeV).  That is the 4He peak, a fact about the data, not
    about this framework.

A non-decreasing function cannot equal a function that decreases across the
same two points — and multiplying by any positive constant preserves that.  So
the failure is in the SHAPE, not the normalisation, and the whole two-parameter
family (`w`, plus an arbitrary overall scale) is excluded at once.

**The extensivity is what kills it.**  Addendum 23 read `S(k)/k -> ln[2]_q` as
the escape — the object is a volume law, so the fixed-width theorem does not
reach it.  That reading is correct.  But a volume law is exactly a constant per
strand, and a constant per strand is a monotone per nucleon; the property that
made the escape real is the property that forecloses it.

**A CORRECTION TO THE PRIOR ADDENDUM, measured here.**  Addendum 23 states that
*"at `w = 3`, the whole nucleon, the cut is the entire system and the entropy is
identically zero"*, and uses that endpoint to bracket `w`.  It is FALSE for this
`S`.  `S(3A) > 0` at every `A` tested — `S(6) = 2.8437`, `S(12) = 6.6650` —
because `S` is the entropy of the Markov TRACE state restricted to `H_k(q)`,
and a trace state is maximally mixed on each block, never pure.  The
zero-at-the-endpoint intuition belongs to the entanglement entropy of a
bipartition of a PURE state, which this is not: A2 below shows `S` is not even
symmetric under `k <-> n - k`, so no Schmidt argument applies and there is no
"the balanced cut is the maximiser" justification available for `w = 3/2`
either.

SCOPE — (b), and narrow.  What is excluded is the ONE-PARAMETER family "cut of
width `wA` with `w` constant across isotopes", together with any overall
rescaling of it.  The invariant is the monotonicity of `S(k)/k` against the
non-monotonicity of `B/A`, both measured, neither fitted.  NOT excluded: a cut
whose width depends on the isotope's own structure rather than on a constant
`w`; any other entropy of any other object.  Nothing here says what the missing
binding term IS.

NO FIT.  No `w` is selected anywhere in this file.  The grid over `w` in A5
scans to FALSIFY a universal claim ("for every w, the model is monotone"), which
is the legitimate direction; it never picks a best-scoring `w`.  The one
quantitative optimum reported (A7) is the best-constant bound
`sqrt(rmax/rmin)`, a closed-form identity being VERIFIED, not a search result.

@module computations/meson/growing_width_cut_shape_exclusion_probe
"""

from __future__ import annotations

import pathlib
import re
import sys
from math import factorial  # float64-ok: exact integer factorial for hook_dim

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, ame_binding_mev  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

Q = Q_MP
E0 = mp.mpf(str(M_E_MEV)) / (Q * (Q - 1))

ISO = [("2H", 1, 2), ("3H", 1, 3), ("3He", 2, 3), ("4He", 2, 4),
       ("6Li", 3, 6), ("7Li", 3, 7), ("12C", 6, 12), ("16O", 8, 16)]

_FAILED: list[str] = []


# bean qou-srvu. Each `check` below is a real falsifiable claim -- it prints
# [PASS]/[FAIL], is tallied, and decides this script's exit code -- but none of
# them reached the witness, so `save()` emitted `allPassed: true` over an EMPTY
# assertions list: green while asserting nothing, and in direct contradiction
# with the same run's exit code. Recorded here and flushed to the witness just
# before `save()`, which needs no call-site change. The assertion NAME is the
# label the message already carries ("A1", "C2", ...); the whole message
# becomes `source`, so every caveat in it travels with the assertion. No
# threshold is introduced: every one already sits at its call site.
_CHECKS: list[tuple[bool, str]] = []


def check(ok: bool, msg: str) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")
    _CHECKS.append((bool(ok), msg))
    if not ok:
        _FAILED.append(msg)


def _flush_assertions(wb) -> None:
    """Emit each recorded check as a witness assertion."""
    for i, (ok, msg) in enumerate(_CHECKS, 1):
        label = msg.split(":", 1)[0].strip()
        if not re.fullmatch(r"[A-Z]\d+", label):
            label = f"check_{i}"
        wb.add_assertion(label, computed=ok, expected=True, source=msg)


# -- the closed form, exactly as Addendum 23 defines it --------------------

def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def markov_weight(lam, k):
    j = lam[1] if len(lam) > 1 else 0
    return qint(k - 2 * j + 1) / qint(2) ** k


def two_row_shapes(k):
    for j in range(0, k // 2 + 1):
        yield (k - j, j) if j else (k,)


def S(k):
    """von Neumann entropy of the k-strand convention-D Markov state."""
    s = mp.mpf(0)
    for lam in two_row_shapes(k):
        y = markov_weight(lam, k)
        if y > 0:
            s -= hook_dim(lam) * y * mp.log(y)
    return s


def total_mass(k):
    return sum((hook_dim(lam) * markov_weight(lam, k)
                for lam in two_row_shapes(k)), mp.mpf(0))


def g(w, A):
    """The model's per-nucleon prediction at cut width `wA`."""
    k = int(mp.floor(w * A))
    if k < 1:
        return mp.mpf(0)
    return E0 * S(k) / A


def main() -> int:
    wb = WitnessBuilder("growing-width-cut-shape-exclusion", engine="python-exact")
    wb.set_description(
        "Excludes the one-parameter growing-width cut of Addendum 23 Front 1 "
        "WITHOUT selecting any w. S(k)/k is increasing, so the model's "
        "per-nucleon prediction is non-decreasing in A for every fixed w; the "
        "AME per-nucleon binding is not, peaking at 4He (7.0739) and dipping at "
        "6Li (5.3323). A non-decreasing function cannot match a function that "
        "decreases across the same two points, and an arbitrary positive "
        "rescaling preserves that -- so the failure is in the SHAPE, not the "
        "normalisation, and the family is excluded scope (b). Also corrects "
        "Addendum 23's claim that the entropy is identically zero at w = 3: "
        "S(3A) > 0 at every A, because S is a TRACE-state entropy, not a "
        "pure-state bipartition entropy (it is not even symmetric under "
        "k <-> n-k).")

    ln2q = mp.log(qint(2))
    KMAX = 64

    print("=" * 92)
    print("The growing-width cut is excluded by its own extensivity")
    print("=" * 92)
    print(f"\n  q0 = {mp.nstr(Q, 20)}    E0 = {mp.nstr(E0, 12)} MeV"
          f"    ln[2]_q = {mp.nstr(ln2q, 12)}")

    # -- controls ---------------------------------------------------------
    print("\n0. Controls")
    masses = [total_mass(k) for k in range(1, 21)]
    check(all(abs(m - 1) < mp.mpf("1e-40") for m in masses),
          "C1: the k-strand Markov measure sums to 1 for k = 1..20 - S is the "
          "entropy of a genuine state, not of an unnormalised weight")

    # Addendum 23 publishes these to four decimals; compare at that precision
    # and no further.  (An earlier draft of this probe invented trailing digits
    # and the assertion correctly failed -- do not re-add precision the source
    # does not carry.)
    prior = {2: "4.3363", 4: "11.9036", 6: "19.7479", 12: "44.4404"}
    tie_ok = True
    for A, want in prior.items():
        got = E0 * S((3 * A) // 2)
        if abs(got - mp.mpf(want)) > mp.mpf("5e-5"):
            tie_ok = False
            print(f"        A={A}: got {mp.nstr(got, 12)} want {want}")
    check(tie_ok,
          "C2: reproduces Addendum 23's balanced-cut table (E0*S(floor(1.5A)) "
          "at A = 2, 4, 6, 12) to the four decimals it publishes - same object, "
          "so the verdict below is about theirs")

    # -- A1/A2: the prior addendum's endpoint is wrong --------------------
    print("\n1. Correcting the prior addendum's endpoint")
    full = {A: S(3 * A) for _n, _z, A in ISO}
    check(all(v > mp.mpf("0.5") for v in full.values()),
          "A1: S(3A) > 0 at EVERY A - Addendum 23's \"at w = 3 the cut is the "
          "entire system and the entropy is identically zero\" is FALSE. S is a "
          f"TRACE-state entropy: S(6) = {mp.nstr(full[2], 10)}, "
          f"S(12) = {mp.nstr(full[4], 10)}")

    asym = [abs(S(k) - S(6 - k)) for k in (1, 2)]
    check(all(d > mp.mpf("0.4") for d in asym),
          "A2: S is NOT symmetric under k <-> n-k (S(1) = 0 vs S(5) = 2.2124 "
          "at n = 6) - so it is not a pure-state bipartition entropy, no "
          "Schmidt argument applies, and there is no \"balanced cut is the "
          "maximiser\" justification available for w = 3/2 either")

    # -- A3/A4: the invariant ---------------------------------------------
    print("\n2. The invariant: S(k)/k increases to ln[2]_q from below")
    dens = [S(k) / k for k in range(1, KMAX + 1)]
    check(all(dens[i] < dens[i + 1] for i in range(len(dens) - 1)),
          f"A3: S(k)/k is STRICTLY INCREASING over k = 1..{KMAX} - the entropy "
          "density rises with the cut width")
    shortfall = 1 - dens[-1] / ln2q
    check(all(d < ln2q for d in dens) and dens[-1] > mp.mpf("0.64")
          and shortfall > mp.mpf("0.05"),
          f"A4: and it approaches ln[2]_q = {mp.nstr(ln2q, 10)} strictly from "
          f"BELOW, and SLOWLY - at k = {KMAX} the density is still "
          f"{mp.nstr(100 * shortfall, 6)} % short "
          f"(S({KMAX})/{KMAX} = {mp.nstr(dens[-1], 10)}). So the asymptotic "
          "`E0*w*ln[2]_q per nucleon` OVERSTATES the model in the "
          "light-nucleus range, where k is single- or double-digit")

    print("\n     k    S(k)      S(k)/k")
    for k in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64):
        print(f"   {k:3d}  {mp.nstr(S(k), 9):>10}  {mp.nstr(S(k) / k, 9):>10}")

    # -- A5/A6/A7: the exclusion ------------------------------------------
    print("\n3. Therefore the model is monotone in A - for every w")
    grid = [mp.mpf(i) / 200 for i in range(20, 601)]     # w in [0.10, 3.00]
    viol = [w for w in grid if g(w, 4) > g(w, 6)]
    check(not viol,
          f"A5: g_w(4) <= g_w(6) for ALL {len(grid)} values of w on a 0.005 "
          "grid over [0.10, 3.00] - the model's per-nucleon prediction never "
          "decreases from 4He to 6Li. (A grid used to FALSIFY a universal "
          "claim, not to select a w)")

    b4 = ame_binding_mev(2, 4) / 4
    b6 = ame_binding_mev(3, 6) / 6
    check(b4 > b6,
          f"A6: but the DATA decreases there - B/A is {mp.nstr(b4, 8)} at 4He "
          f"and {mp.nstr(b6, 8)} at 6Li. This is the 4He peak, a fact about "
          "AME, not about this framework")

    print("\n4. The exclusion")
    print("\n   iso   A     B/A       g_w(A) at w=1.5    required ratio")
    ratios = []
    for name, Z, A in ISO:
        bA = ame_binding_mev(Z, A) / A
        gw = g(mp.mpf("1.5"), A)
        ratios.append((name, bA / gw))
        print(f"   {name:5s} {A:2d}  {mp.nstr(bA, 8):>9}  {mp.nstr(gw, 8):>15}"
              f"    {mp.nstr(bA / gw, 8):>10}")

    rmin = min(r for _n, r in ratios)
    rmax = max(r for _n, r in ratios)
    best_err = mp.sqrt(rmax / rmin)

    check((b4 > b6) and not viol,
          "A7: THE EXCLUSION - for every w and every positive overall scale c, "
          "c*g_w(4) <= c*g_w(6) while B/A decreases across those two isotopes, "
          "so no member of the family matches both. The failure is in the "
          "SHAPE, not the normalisation")

    print(f"\n   Best-constant bound at w = 3/2: the required rescaling spans "
          f"[{mp.nstr(rmin, 8)}, {mp.nstr(rmax, 8)}],")
    print(f"   so the best single constant is off by sqrt(rmax/rmin) = "
          f"{mp.nstr(best_err, 8)}x on the extremes.")
    print("   (A closed-form identity verified, not a fitted optimum.)")

    wb.add_data("q0", mp.nstr(Q, 20))
    wb.add_data("E0_MeV", mp.nstr(E0, 20))
    wb.add_data("ln_2q", mp.nstr(ln2q, 20))
    wb.add_data("S_3A_positive", {str(A): mp.nstr(v, 12) for A, v in full.items()})
    wb.add_data("density_increasing_to_kmax", KMAX)
    wb.add_data("density_at_kmax", mp.nstr(dens[-1], 20))
    wb.add_data("w_grid_monotonicity_violations", len(viol))
    wb.add_data("B_over_A_4He", mp.nstr(b4, 20))
    wb.add_data("B_over_A_6Li", mp.nstr(b6, 20))
    wb.add_data("required_rescale_min", mp.nstr(rmin, 20))
    wb.add_data("required_rescale_max", mp.nstr(rmax, 20))
    wb.add_data("best_constant_multiplicative_error", mp.nstr(best_err, 20))
    wb.add_data("verdict",
                "scope-(b): the one-parameter constant-w growing-width cut, and "
                "any overall rescaling of it, is excluded by the monotonicity of "
                "S(k)/k against the non-monotonicity of B/A. A cut whose width "
                "depends on the isotope's own structure is NOT excluded.")
    wb.add_data("corrects",
                "Addendum 23 Front 1: 'at w = 3 the cut is the entire system and "
                "the entropy is identically zero' is false; S(3A) > 0 at every A.")
    wb.add_caveat(
        "Scope (b) and narrow: what is excluded is the one-parameter family "
        "'cut of width wA with w constant across isotopes', together with any "
        "overall positive rescaling of it. A cut whose width depends on the "
        "isotope's own structure is NOT excluded, and nothing here says what "
        "the missing binding term is.")
    wb.add_caveat(
        "No w is selected anywhere. The grid over w scans to FALSIFY a "
        "universal monotonicity claim, which is the legitimate direction; it "
        "never picks a best-scoring w. The sqrt(rmax/rmin) figure is a "
        "closed-form identity verified, not a fitted optimum.")
    wb.add_caveat(
        "S(k)/k is measured monotone over k = 1..64, not proved monotone for "
        "all k. The exclusion needs it only on the range the isotopes reach.")
    _flush_assertions(wb)
    wb.save()

    ntotal = len(_CHECKS)
    print("\n" + "=" * 92)
    print(f"{ntotal - len(_FAILED)}/{ntotal} assertions passed")
    print("=" * 92)
    return 1 if _FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
