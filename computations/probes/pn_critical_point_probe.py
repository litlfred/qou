#!/usr/bin/env python3
"""
pn_critical_point_probe — `r_pn ~ 1` is not an artefact. The p-n bond sits at
the TRACE-ZERO (critical) point of the transfer-matrix family, where the two
eigenvalues have EQUAL MODULUS, the spectral gap closes and the correlation
length diverges. The colour split `delta` is the ONLY thing regulating it, and
it opens the gap LINEARLY, giving a correlation length of ~7000 strand
spacings -- effectively infinite for any nucleus.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows the spectral-gap probe,
which found `r_pp = r_nn = 1/q^2` but `r_pn = 0.99986` and left open whether
that near-unity was real or a near-degeneracy artefact.

## The question

`spectral_gap_bond_decay_probe` read the per-bond decay off `|lambda_2/lambda_1|`
of the transfer matrix `T(1,d) = [[h+d, 1], [1, d]]`. `pp` and `nn` gave exactly
`1/q^2`; `pn` gave `0.999856986228`, i.e. 1 to one part in 6992. Eigenvalues
`+1.00552` and `-1.00538` are nearly equal in modulus -- exactly the situation
where a ratio-of-eigenvalues reading stops meaning "decay rate", so it had to be
checked before being used.

## It is a critical point, and the identities are exact

`trace T(1,d) = h + 2d`, so **trace vanishes iff `d = -h/2`**. At trace zero the
spectrum is `+/-lambda`: equal moduli, ratio exactly 1, **no spectral gap and an
infinite correlation length**.

The p-n offset `d_pn = -h(1/2 - delta/4)` sits a hair off that point, and both
displacements are exact (verified to 45 digits):

    d_pn + h/2      = h*delta/4 = 7.19016280934e-5
    trace(T_pn)     = h*delta/2 = 0.000143803256187

So **`delta = 0` puts the p-n bond exactly at criticality**, and the colour split
is the sole regulator. This is a structural fact about the framework, not a
numerical coincidence.

## How the gap opens — LINEARLY, and I got this wrong first

With `t = trace = h*delta/2` and `D = det = (h+d)d - 1 < 0`,

    |l2/l1| = (sqrt(t^2 - 4D) - t) / (sqrt(t^2 - 4D) + t)
            ~ 1 - t/sqrt(-D)                     for small t

    ==>   1 - r  ~  h*delta / (2*sqrt(1 + h^2/4))

EXACT closed form, no expansion:  `1 - r = 2t / (sqrt(t^2 - 4D) + t)`, which
reproduces the measured `0.00014301377225689` to below `1e-40`.

The small-t expansion `h*delta/(2*sqrt(1 + h^2/4))` gives
`0.00014302399982344` -- it **drops 1.02e-8**, a `7.15e-5` relative error --
and that dropped piece is **not harmless downstream**: the weight at
separation `s` is `r^{s-1}`, so the two `r`s differ by `1.0e-8` at `s = 2`
but by `7.2e-5` at `s ~ xi`. The error COMPOUNDS, so a sum over separations
inherits the larger figure. Likewise `xi = -1/ln(r) = 6991.83` exactly,
where the `1/(1-r)` shortcut gives `6992.33`.

And `delta` is `flavor_split_LEADING` -- itself a leading term, not exact --
so every figure here inherits that truncation too. Flagged, not fixed.

**That constant is `tanh(ln q_0)`, and it is EXACT -- identified by a sibling,
confirmed here.** `main` landed `qou-cds1` Step 28
(`qbeta_bond_decay_rates_from_transfer_spectrum_probe`), reaching the same
object independently and giving the closed form `tanh(ln q_0) = 0.103963710`
where this probe had only the number. The two agree because my expansion
coefficient IS that function, by an exact identity I had not noticed:

    (q + 1/q)^2  =  q^2 + 2 + 1/q^2  =  4 + h^2        (since h = q - 1/q)
    =>  2*sqrt(1 + h^2/4)  =  sqrt(4 + h^2)  =  q + 1/q
    =>  h / (2*sqrt(1 + h^2/4))  =  h/(q + 1/q)  =  tanh(ln q).

Verified at 50 dps: all three forms give `0.10396371005241014568`, pairwise
agreement `1.67e-52`.  So the law is

    1 - r_pn  =  tanh(ln q_0) * delta  +  O(delta^2)

with a named closed form, not an empirical constant.  **Do NOT carry the
sibling's EM reading of it**: they downgraded that themselves (`qou-i9gk`,
`main` `85c2bb0468`) -- `tanh(ln q)` is "odd part over even part", which any
bar decomposition produces, so the match to the taxonomy's EM ratio is formal.
The closed form stands; the interpretation does not.

`(1-r)/delta` is constant across a x1024 sweep of `delta` (3.0 decades):
`0.1039562759 -> 0.1039637028`, agreeing to **4 significant figures** with a
**relative variation of 7.14e-5**, against the probe's `1e-4` assertion. That
is what fixes the power.  (Corrected after Copilot review on #6411: this read
"6 digits across four decades", overstating both the precision and the span.)

**My first pass printed "the gap opens like sqrt(delta)". That was wrong** -- I
had divided by `sqrt(delta)` and read a halving column as a constant one. The
correct diagnostic is `(1-r)/delta`, and it is flat. Recorded because the wrong
scaling would have made the p-n range parametrically larger than it is.

## What it means, and what it explains

The correlation length in strand spacings is

    xi = -1/log(r) ~ 1/(1-r) ~ 6992

so **every p-n pair in any nucleus is deep inside the correlation length.** That
is exactly why `spectral_gap_bond_decay_probe` overshoots at `A >= 6`: with
`xi ~ 7000` the model counts all `Z*N` p-n pairs at essentially full strength,
so `B` grows like `Z*N` and lands `+19 %` at `6Li`, `+36 %` at `7Li`.

So the `Z*N` overshoot is not a separate defect to be fixed -- it is the direct
consequence of the p-n bond being critical, and any pairwise model built on
these transfer matrices will have it.

## What is NOT claimed

  * NOT that nature's p-n interaction is long-range. This is a statement about
    the FRAMEWORK's transfer matrices. Nature's p-n force has a ~1.4 fm range;
    if the framework says `xi ~ 7000` spacings, that is a **discrepancy the
    framework owns**, not a prediction to celebrate.
  * NOT that the criticality is derived from first principles. It is measured:
    `d_pn` happens to equal `-h/2 + h*delta/4`, and `-h/2` happens to be the
    trace-zero point. Whether the colour weighting was CONSTRUCTED to sit there
    is a question about `bring_color_weighted`'s derivation that this probe
    does not answer. **ANSWERED, in the sibling probe on this same branch:**
    `pn_criticality_is_forced_probe` shows the trace is AFFINE in the bond
    offset with endpoints `d_pp = 0` and `d_nn = -h`, so the midpoint `-h/2`
    is trace-zero identically. ANY interpolation placing p-n at the midpoint
    lands on criticality -- it is forced by averaging, and carries no
    independent information. Read the two together; this caveat is the
    weaker half.
  * NOT a binding value, and nothing is wired or fitted.
  * The `|l2/l1|`-as-decay reading is still the assumed form flagged in the
    previous probe; this probe tests whether the ratio is meaningful, not
    whether the form is right.

Scope **(a)**: measurement plus exact identities.

NO FLOAT64: mpmath `mpf` at 60 dps, 50-digit proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
TOL = mp.mpf(10) ** -45


def fmt(x, n=12):
    return mp.nstr(x, n)


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    dx = flavor_split_leading(q)

    def spec(d):
        tr = h + 2 * d
        dt = (h + d) * d - 1
        r = mp.sqrt(tr * tr - 4 * dt)
        e = [(tr + r) / 2, (tr - r) / 2]
        e.sort(key=lambda x: -abs(x))
        return e

    def ratio(d):
        e = spec(d)
        return abs(e[1]) / abs(e[0])

    print("pn_critical_point_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}   delta = {fmt(dx)}")
    print()
    print("THE CRITICAL POINT")
    print("-" * 78)
    print("  T(1,d) = [[h+d, 1],[1, d]];  trace = h + 2d, zero iff d = -h/2.")
    print("  At trace zero the spectrum is +/-lambda: EQUAL MODULI, ratio")
    print("  exactly 1, no spectral gap, INFINITE correlation length.")
    print()
    print(f"  ratio at d = -h/2 exactly: {fmt(ratio(-h / 2))}")
    assert abs(ratio(-h / 2) - 1) < TOL, "trace zero must give ratio exactly 1"
    d_pn = -h * (mp.mpf(1) / 2 - dx / 4)
    print(f"\n  d_pn        = {fmt(d_pn)}")
    print(f"  -h/2        = {fmt(-h / 2)}")
    print(f"  d_pn + h/2  = {fmt(d_pn + h / 2)}   h*delta/4 = {fmt(h * dx / 4)}")
    assert abs((d_pn + h / 2) - h * dx / 4) < TOL, "offset must be h*delta/4"
    print(f"  trace(T_pn) = {fmt(h + 2 * d_pn)}   h*delta/2 = {fmt(h * dx / 2)}")
    assert abs((h + 2 * d_pn) - h * dx / 2) < TOL, "trace must be h*delta/2"
    print("\n  Both exact to 45 digits.  So delta = 0 puts the p-n bond EXACTLY")
    print("  at criticality, and the colour split is the SOLE regulator.")
    print()

    print("HOW THE GAP OPENS — linearly, and I got this wrong on the first pass")
    print("-" * 78)
    print(f"{'delta':>18} {'1 - ratio':>20} {'(1-r)/delta':>15} {'(1-r)/sqrt':>14}")
    cols = []
    for k in range(6):
        dd = dx / mp.mpf(4) ** k
        d_ = -h * (mp.mpf(1) / 2 - dd / 4)
        rr = 1 - ratio(d_)
        cols.append(rr / dd)
        print(f"{fmt(dd, 10):>18} {fmt(rr, 12):>20} {fmt(rr / dd, 10):>15} "
              f"{fmt(rr / mp.sqrt(dd), 10):>14}")
    assert abs(cols[-1] - cols[0]) / cols[0] < mp.mpf("1e-4"), \
        "(1-r)/delta must be constant -> the law is LINEAR in delta"
    print(f"\n  (1-r)/delta varies by {fmt(abs(cols[-1]-cols[0])/cols[0], 4)}"
          f" relative across a x1024 sweep (3.0 decades),")
    print("  agreeing to 4 significant figures against a 1e-4 assertion:")
    print("  the gap is LINEAR in delta.  The sqrt column HALVES, which is what")
    print("  a wrong diagnostic looks like -- my first pass divided by sqrt and")
    print("  reported sqrt scaling.  Recorded because the wrong law would have")
    print("  made the p-n range parametrically larger than it is.")
    print()

    t = h + 2 * d_pn
    Dt = (h + d_pn) * d_pn - 1
    root = mp.sqrt(t * t - 4 * Dt)
    exact = 2 * t / (root + t)              # EXACT, no expansion
    approx = h * dx / (2 * mp.sqrt(1 + h**2 / 4))   # small-t expansion
    # the coefficient is EXACTLY tanh(ln q): (q+1/q)^2 = 4 + h^2, so
    # 2*sqrt(1+h^2/4) = q + 1/q, hence h/(2*sqrt(1+h^2/4)) = tanh(ln q).
    # Identified by the sibling qou-cds1 Step 28; asserted here.
    _tanh = mp.tanh(mp.log(q))
    assert abs(h / (2 * mp.sqrt(1 + h**2 / 4)) - _tanh) < mp.mpf(10)**-45
    assert abs(h / (q + 1 / q) - _tanh) < mp.mpf(10)**-45
    print(f"  expansion coeff = tanh(ln q_0) = {fmt(_tanh, 20)}  (EXACT)")
    meas = 1 - ratio(d_pn)
    print("  EXACT closed form (no expansion):")
    print("    1 - r = 2t / (sqrt(t^2 - 4D) + t),   t = h*delta/2, D = det < 0")
    print(f"      exact    {fmt(exact)}")
    print(f"      measured {fmt(meas)}   agree to "
          f"{fmt(abs(exact - meas), 4)}")
    assert abs(exact - meas) < mp.mpf("1e-40"), "exact form must be exact"
    print("\n  the small-t EXPANSION, kept only to show what it costs:")
    print("    1 - r ~ t/sqrt(-D) = h*delta/(2*sqrt(1 + h^2/4))")
    print(f"      approx   {fmt(approx)}")
    print(f"      DROPPED  {fmt(approx - exact, 6)}   "
          f"({fmt(abs(approx - exact) / exact, 6)} relative)")
    print()

    r_ex = ratio(d_pn)
    xi = -1 / mp.log(r_ex)                 # EXACT
    xi_approx = 1 / (1 - r_ex)             # the 1/(1-r) shortcut
    print("WHAT IT EXPLAINS — the Z*N overshoot is not a separate defect")
    print("-" * 78)
    print(f"  correlation length xi = -1/ln(r) = {fmt(xi, 12)} spacings  (EXACT)")
    print(f"    the 1/(1-r) shortcut gives      {fmt(xi_approx, 12)}, "
          f"off by {fmt(xi_approx - xi, 4)}")
    print("  -- small here, but it COMPOUNDS in r^(s-1): the two rs differ by")
    print("     1e-8 at s=2 and 7.2e-5 at s ~ xi, so a downstream sum over")
    print("     separations inherits the larger error, not the smaller one.")
    print("  delta itself is flavor_split_LEADING -- a leading term, not an")
    print("  exact quantity -- so everything here inherits THAT truncation too.")
    print("  Every p-n pair in ANY nucleus is deep inside that length, so a")
    print("  pairwise model counts all Z*N of them at essentially full strength.")
    print("  That is exactly the overshoot spectral_gap_bond_decay_probe found:")
    print("    6Li +19.1 %,  7Li +36.4 %  (alternating ordering)")
    print("  So the Z*N growth is a CONSEQUENCE of p-n criticality, and any")
    print("  pairwise model built on these transfer matrices will have it.")
    assert xi > 1000, "the correlation length must be effectively unbounded"
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that nature's p-n force is long-range.  This is about the")
    print("    FRAMEWORK's matrices.  Nature's p-n range is ~1.4 fm; xi ~ 7000")
    print("    spacings is a DISCREPANCY the framework owns, not a prediction.")
    print("  * NOT that the criticality is derived.  It is MEASURED: d_pn equals")
    print("    -h/2 + h*delta/4, and -h/2 happens to be trace-zero.  Whether")
    print("    bring_color_weighted was CONSTRUCTED to sit there is a question")
    print("    about its derivation that this probe does not answer.")
    print("    -> ANSWERED by pn_criticality_is_forced_probe (same branch):")
    print("       the trace is AFFINE in d with endpoints 0 and -h, so the")
    print("       midpoint IS trace-zero.  Forced by averaging; carries no")
    print("       independent information.  Read the two together.")
    print("  * NOT a binding value.  Nothing wired, nothing fitted.")
    print("  * The |l2/l1|-as-decay reading remains the ASSUMED form flagged in")
    print("    the previous probe.  This tests whether the ratio is meaningful,")
    print("    not whether the form is right.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
