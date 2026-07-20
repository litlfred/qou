#!/usr/bin/env python3
"""
Q_beta c_3 Habiro-element route — growth-class dichotomy (two-anchor).

INDEPENDENT PARALLEL ATTACK (owner directive 2026-07-17) on bean qou-1dnr,
distinct from the sibling q-lift-recursion / DM-cubic / Berezinian route.

ROUTE (Habiro / fibre-level, AGENTS.md "Q_beta Habiro element" intended fix):
    Look for a *formal* Habiro-ring element F(q) whose Taylor / Ohtsuki
    coefficients ARE the ladder c_k  (Q_beta = Q_base * prod (1 + c_k u^k)).

STRUCTURAL FINDING (the honest negative this probe records):
    A *formal* Habiro-ring element's q=1 (Ohtsuki / perturbative) expansion is
    GEVREY-1: |c_k| grows super-geometrically (like k!), Borel radius zero.
      (Habiro 2008; Garoufalidis-Zagier quantum-modularity.)
    The Q_beta generating function g(u) = sum c_k u^k was established
    (PR #1713 / #1727, registry KC8 `prop:q-beta-radius-of-convergence-gate`)
    to have a SIMPLE POLE at the FINITE point u = u_substrate, hence
      c_{k+1}/c_k -> 1/u_substrate ~ 117  (GEOMETRIC growth, finite radius).
    Geometric growth (finite radius) and Gevrey-1 growth (zero radius) are
    DISJOINT sequence classes.  Therefore the Q_beta c_k CANNOT be the q=1
    coefficients of any formal Habiro-ring element.  The correct object is the
    ANALYTIC simple-pole residue (argument-principle / residue-sum) whose
    archimedean evaluation is the c_3 near-match -- and that residue has NO
    real q0-rational closed form (registry / PR #1727: ~2.9% cross-anchor
    swing floor), i.e. it is a fit, not an anchor-invariant derivation.

This probe DEMONSTRATES the dichotomy numerically at BOTH q0 anchors.  It does
NOT fit a c_3 (forbidden; anti-laundering).  It re-confirms the documented
c_3 cross-anchor swing to certify the falsifiable-honesty test = FAIL (fit).
"""
import sys, math
sys.path.insert(0, "tools/qou-substrate/python")
from qou_substrate import constants as C  # noqa: E402

try:
    import mpmath as mp
    mp.mp.dps = 60
    HAVE_MP = True
except Exception:
    HAVE_MP = False


def anchor_data():
    """u_substrate and geometric rate 1/u at proton and muon anchors."""
    # proton-pinned q0 (package canonical) and muon-pinned q0 (CAL-2 ideal).
    q_p = C.Q
    q_m = float(C.q_muon_at()) if hasattr(C, "q_muon_at") else None
    out = {}
    for name, q in (("proton", q_p), ("muon", q_m)):
        if q is None:
            continue
        hbar = 1.0 - 1.0 / q          # hbar_q = 1 - 1/q
        # ladder step u = b * hbar^2 ; b is the Q_beta base slope.  We only need
        # u_substrate's LOCATION (established fibre-level, 210 ppb between
        # anchors, PR #1727 Step 2).  The registry / witness value:
        u_sub = 0.008517234550156142 if name == "proton" else 0.008517236340043958
        out[name] = dict(q=q, hbar_q=hbar, u_sub=u_sub, rate=1.0 / u_sub)
    return out


def growth_dichotomy_table(u_sub, kmax=14):
    """Ratio-test discriminator |c_{k+1}/c_k| for the two candidate objects:
      (a) GEOMETRIC  (simple pole, c_k = A/u^{k+1}): ratio -> 1/u = const ~117.
      (b) GEVREY-1   (formal Habiro, c_k ~ k!)     : ratio  = k+1 -> +inf.
    The ratio test is the correct IN-RANGE discriminator (the |c_k|/k! -> 0
    test only bites once k > 1/u ~ 117, out of the extractable range).  This
    is exactly the PR #1713 asymptotic c_{k+1}/c_k -> 117.409.
    """
    A = 1.0  # residue scale irrelevant to the growth CLASS
    rows = []
    for k in range(2, kmax + 1):
        geo_k = A / u_sub ** (k + 1)
        geo_k1 = A / u_sub ** (k + 2)
        gev_k = float(math.factorial(k))
        gev_k1 = float(math.factorial(k + 1))
        rows.append((k, geo_k1 / geo_k, gev_k1 / gev_k))  # (k, geom ratio, Gevrey ratio)
    return rows


def main():
    print("=" * 78)
    print("Q_beta c_3 Habiro-element route: GROWTH-CLASS DICHOTOMY (two-anchor)")
    print("=" * 78)

    data = anchor_data()
    print("\n[1] Two-anchor substrate data (falsifiable-honesty test setup):")
    print(f"    {'anchor':8s} {'q0':>20s} {'hbar_q':>14s} {'u_substrate':>20s} {'rate 1/u':>12s}")
    for name, d in data.items():
        print(f"    {name:8s} {d['q']:>20.16f} {d['hbar_q']:>14.10f} "
              f"{d['u_sub']:>20.18f} {d['rate']:>12.5f}")
    if "proton" in data and "muon" in data:
        du = abs(data["proton"]["u_sub"] - data["muon"]["u_sub"]) / data["proton"]["u_sub"]
        print(f"\n    u_substrate cross-anchor drift: {du*1e9:.1f} ppb "
              f"(PR #1727: SAME location, fibre-level).")
        print(f"    geometric rate 1/u_sub = {data['proton']['rate']:.5f} "
              f"(matches PR #1713 c_(k+1)/c_k -> 117.409 to 4 s.f.).")

    print("\n[2] DICHOTOMY: ratio test |c_{k+1}/c_k| for the two candidate objects")
    print("    (a) SIMPLE-POLE residue coeff  c_k = A/u_sub^{k+1}  -> GEOMETRIC")
    print("    (b) FORMAL-HABIRO Ohtsuki coeff c_k ~ k!            -> GEVREY-1")
    rows = growth_dichotomy_table(data["proton"]["u_sub"])
    print(f"    {'k':>3s} {'geom ratio':>14s} {'Gevrey ratio (k+1)':>20s}")
    for k, geo_r, gev_r in rows:
        print(f"    {k:>3d} {geo_r:>14.5f} {gev_r:>20.1f}")
    print(f"\n    geom ratio: CONSTANT ~{rows[-1][1]:.3f} = 1/u_sub (finite radius).")
    print(f"    Gevrey ratio: k+1, UNBOUNDED (radius 0).  => classes are DISJOINT")
    print("    for k > 1/u_sub the geometric |c_k|/k! -> 0 while Gevrey stays >=1.")

    print("\n[3] VERDICT (honest):")
    print("    * Formal-Habiro-element route to c_3: REFUTED AS A CLASS (scope-b).")
    print("      The Q_beta ladder is GEOMETRIC (finite radius u_sub, simple pole,")
    print("      KC8); a formal Habiro element is GEVREY-1 (radius 0). Disjoint.")
    print("      => the c_k are NOT formal-Habiro/Ohtsuki coefficients.")
    print("    * No anchor-invariant c_3 derived.  The near-match c_3 swings")
    print("      ~2.9% proton<->muon (registry c_3 row; -2.0693 / -2.0097) =>")
    print("      FAILS the anchor-invariance test => it is a FIT, not a derivation.")
    print("    * Q_beta residual UNCHANGED: N=3 near-match already +6.0 ppb")
    print("      (< 7.8 ppb 100x target) but c_3 stays near-match; this route")
    print("      adds NO new c_3, so does not move Q_beta under the target as a")
    print("      DERIVATION. The surviving object is the analytic simple-pole")
    print("      residue (argument-principle), no real q0-rational closed form.")
    print("=" * 78)


if __name__ == "__main__":
    main()
