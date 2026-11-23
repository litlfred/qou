#!/usr/bin/env python3
"""
Probe — MEASURE the surface exponent, which is the inverse dimension of the
coordination graph, and compare it with the production word's own dimension.

CONTEXT. `QOU.Mass.CoordinationSurfaceDeficit` (#6761) splits the per-nucleon
binding of a bounded-degree bond count into a volume term and a boundary
deficit whose whole A-dependence is the surface fraction A_surf/A. Its
magnitude test — the surface-to-volume ratio a_S/a_V = c(k-k')/k — was measured
GENERIC (67.9 % of its plausible window reachable by choosing a facet and a
shell treatment, `qou-kqdn`), so the ratio does not constrain the geometry.

This probe tests the one thing in that split that is NOT free to be chosen.
For a compact d-dimensional cluster the boundary is (d-1)-dimensional, so

    A_surf ~ c·A^((d-1)/d)   =>   A_surf/A ~ c·A^(-1/d),

and `QOU.Mass.SurfaceExponentIsDimension.perNucleonExp_exponent_inj` proves
distinct exponents are distinct functions of A: no choice of amplitude can
disguise a wrong dimension. So MEASURING the exponent p in

    B/A = a_V - b·A^(-p) - a_C Z^2/A^(4/3) - a_A (N-Z)^2/A^2 + a_P delta/A^(3/2)

measures 1/d directly. The production braid word `atom_braid_word_3A` writes one
inter-nucleon letter per adjacent pair, so its coordination graph is the path
P_A: two endpoints of bond-degree 1, interior degree 2, A_surf = 2 CONSTANT.
That is d = 1 and predicts p = 1 (`chain_perNucleon`: B/A = eps - eps/A).

WHAT IS MEASURED (2548 measured AME nuclides, #6611's selection and helpers):
  1. the profiled exponent p*: for each p the model is LINEAR in its
     coefficients, so p is profiled by exact least squares on a grid plus a
     golden-section refinement — no nonlinear search, no starting guess;
  2. how sharply p is determined: the width of the interval where the residual
     sum of squares stays within 1 % of its minimum;
  3. the production chain's exponent p = 1 scored on the same footing;
  4. a GENERICITY MEASUREMENT of p itself, by the method `qou-rav3` prescribes
     and `qou-kqdn` applied to its own ratio: what fraction of the plausible
     window does p reach as the analysis choices are varied? A quantity that
     reaches most of its window is not a prediction, whatever it lands on.

NOTHING IS WIRED AND NOTHING IS FITTED TO PRODUCTION. The coefficients are
diagnostics of the DATA's shape, reported to be checked against; the framework
side contributes only the exponent predictions p = 1 (chain, proved) and
p = 1/3 (a 3-D packing, assumed).

Arithmetic: mpmath 50 dps; AME values loaded from decimal strings; the normal
equations solved with mp.lu_solve. No float64 anywhere.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

import cyclic_triple_bond_cross_term_probe as ct  # noqa: E402
from binding_log_free_energy import M_E_MEV  # noqa: E402

mp.mp.dps = 50
Q, TOL = ct.Q, ct.TOL
M_E = mp.mpf(str(M_E_MEV))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
EPS = E0 * mp.log((Q ** 2 + 1) / Q)
ROOT = Path(__file__).resolve().parents[2]
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"

P_CHAIN = mp.mpf(1)               # d = 1, the production word's path graph (PROVED)
P_PACKING = mp.mpf(1) / 3         # d = 3, a compact packing (ASSUMED geometry)
WINDOW = (mp.mpf(0), mp.mpf(2))   # plausible window for an inverse dimension d >= 1/2


def fit(X, y):
    """least squares by normal equations, exact mp arithmetic; (coef, R^2, RSS)."""
    n, k = len(X), len(X[0])
    XtX, Xty = mp.matrix(k, k), mp.matrix(k, 1)
    for i in range(k):
        for j in range(k):
            XtX[i, j] = sum(X[r][i] * X[r][j] for r in range(n))
        Xty[i] = sum(X[r][i] * y[r] for r in range(n))
    c = mp.lu_solve(XtX, Xty)
    yhat = [sum(c[i] * X[r][i] for i in range(k)) for r in range(n)]
    my = sum(y) / n
    rss = sum((y[r] - yhat[r]) ** 2 for r in range(n))
    tot = sum((y[r] - my) ** 2 for r in range(n))
    return [c[i] for i in range(k)], 1 - rss / tot, rss


def build(rows, p, pairing=True, asym=True):
    """design matrix [1, A^-p, Coulomb, (asymmetry), (pairing)] and response B/A."""
    X, y = [], []
    for (A, Z, N, B) in rows:
        Am = mp.mpf(A)
        row = [mp.mpf(1), Am ** (-p), mp.mpf(Z * Z) / Am ** (mp.mpf(4) / 3)]
        if asym:
            row.append((mp.mpf(N - Z) / Am) ** 2)
        if pairing:
            d = mp.mpf(1) if (Z % 2 == 0 and N % 2 == 0) else (mp.mpf(-1) if (Z % 2 and N % 2) else mp.mpf(0))
            row.append(d / Am ** (mp.mpf(3) / 2))
        X.append(row)
        y.append(B / Am)
    return X, y


def rss_at(rows, p, **kw):
    X, y = build(rows, p, **kw)
    return fit(X, y)[2]


def profile(rows, lo, hi, steps=24, refine=40, **kw):
    """grid then golden-section: returns (p*, rss*). No starting guess, no gradient."""
    best = None
    for i in range(steps + 1):
        p = lo + (hi - lo) * i / steps
        r = rss_at(rows, p, **kw)
        if best is None or r < best[1]:
            best = (p, r)
    step = (hi - lo) / steps
    a, b = max(lo, best[0] - step), min(hi, best[0] + step)
    gr = (mp.sqrt(5) - 1) / 2
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd = rss_at(rows, c, **kw), rss_at(rows, d, **kw)
    for _ in range(refine):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = rss_at(rows, c, **kw)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = rss_at(rows, d, **kw)
        if b - a < mp.mpf("1e-12"):
            break
    p = (a + b) / 2
    return p, rss_at(rows, p, **kw)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    # ---- the chain identity the Lean proves, checked numerically -------------
    def bondCount(k, kp, Aint, Asurf):
        return (k * Aint + kp * Asurf) / 2
    ok = all(abs(bondCount(mp.mpf(2), mp.mpf(1), mp.mpf(A) - 2, mp.mpf(2)) - (mp.mpf(A) - 1)) < TOL
             for A in (2, 3, 4, 12, 56, 208))
    checks.append(("chain_bondCount: the path graph's bond count is A−1 at k=2, k'=1, A_surf=2 (six A)", ok))
    ok = all(abs(EPS * bondCount(mp.mpf(2), mp.mpf(1), mp.mpf(A) - 2, mp.mpf(2)) / A
                 - (EPS - EPS * mp.mpf(A) ** (-P_CHAIN))) < TOL for A in (2, 4, 56, 208))
    checks.append(("chain_is_dimension_one: ε·bondCount/A = ε − ε·A^(−1), i.e. the chain is the p = 1 member", ok))

    print(f"  E_0 = {mp.nstr(E0, 10)} MeV   ε = E_0·ln[2]_q = {mp.nstr(EPS, 10)} MeV")
    print(f"  the production word's graph: path P_A — endpoints degree 1, interior degree 2, A_surf = 2 (constant)")
    print(f"  predicted exponents:  chain (d=1) p = {mp.nstr(P_CHAIN, 6)}    compact packing (d=3) p = {mp.nstr(P_PACKING, 6)}\n")

    # ---- data ---------------------------------------------------------------
    rows = []
    for ent in json.loads(AME.read_text())["entries"]:
        Z, N, A = ent["Z"], ent["N"], ent["A"]
        bpa = ent.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not bpa or ent.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B > 0:
            rows.append((A, Z, N, B))
    print(f"  {len(rows)} measured AME nuclides")
    checks.append(("AME selection reproduces #6611's 2548 measured nuclides", len(rows) == 2548))

    # ---- control: the exponent FIXED at 1/3 is the SEMF ----------------------
    # #6761 used the basis WITHOUT a pairing column; reproduce that exactly first.
    Xc, yc = build(rows, P_PACKING, pairing=False)
    coefc, r2_c, _ = fit(Xc, yc)
    aS_aV_c = -coefc[1] / coefc[0]
    print(f"\n  control — exponent FIXED at p = 1/3, #6761's basis (no pairing column): "
          f"R² = {mp.nstr(r2_c, 6)}, a_V = {mp.nstr(coefc[0], 6)} MeV, a_S/a_V = {mp.nstr(aS_aV_c, 6)}")
    checks.append(("control: on #6761's own basis, p fixed at 1/3 reproduces its a_S/a_V = 0.9607 (to 3 dp)",
                   abs(aS_aV_c - mp.mpf("0.9607")) < mp.mpf("0.0015")))
    checks.append(("control: on #6761's own basis, p fixed at 1/3 reproduces its R² = 0.964 (to 3 dp)",
                   abs(r2_c - mp.mpf("0.964")) < mp.mpf("0.0015")))
    X, y = build(rows, P_PACKING)
    coef13, r2_13, rss_13 = fit(X, y)
    aS_aV = -coef13[1] / coef13[0]
    print(f"  control — exponent FIXED at p = 1/3, this probe's basis (pairing column added): "
          f"R² = {mp.nstr(r2_13, 6)}, a_V = {mp.nstr(coef13[0], 6)} MeV, a_S/a_V = {mp.nstr(aS_aV, 6)}")
    checks.append(("adding the pairing column improves the p = 1/3 fit (it is a real term, not noise)",
                   r2_13 > r2_c))

    # ---- the chain's own exponent, scored on the same footing ---------------
    X1, y1 = build(rows, P_CHAIN)
    _, r2_1, rss_1 = fit(X1, y1)
    print(f"  the production chain — exponent FIXED at p = 1 (d = 1):  R² = {mp.nstr(r2_1, 6)}, "
          f"RSS = {mp.nstr(rss_1, 6)}")

    # ---- profiled exponent --------------------------------------------------
    p_star, rss_star = profile(rows, WINDOW[0] + mp.mpf("0.02"), WINDOW[1])
    Xs, ys = build(rows, p_star)
    coefs, r2_star, _ = fit(Xs, ys)
    d_star = 1 / p_star
    print(f"\n  PROFILED exponent (grid + golden section, no starting guess):")
    print(f"    p*   = {mp.nstr(p_star, 8)}        =>  d = 1/p* = {mp.nstr(d_star, 8)}")
    print(f"    R²   = {mp.nstr(r2_star, 8)}   a_V = {mp.nstr(coefs[0], 6)} MeV   "
          f"b/a_V = {mp.nstr(-coefs[1] / coefs[0], 6)}")
    print(f"    RSS(p*) = {mp.nstr(rss_star, 6)}   RSS(1/3) = {mp.nstr(rss_13, 6)}   RSS(1) = {mp.nstr(rss_1, 6)}")
    checks.append(("the profiled optimum is interior to the scan window (a genuine minimum, not a boundary artifact)",
                   WINDOW[0] + mp.mpf("0.03") < p_star < WINDOW[1] - mp.mpf("0.03")))
    checks.append(("profiling can only improve on a fixed exponent: RSS(p*) ≤ RSS(1/3) and ≤ RSS(1)",
                   rss_star <= rss_13 and rss_star <= rss_1))
    checks.append(("the measured exponent is closer to the 3-D packing value 1/3 than to the chain's 1",
                   abs(p_star - P_PACKING) < abs(p_star - P_CHAIN)))
    checks.append(("the production chain's exponent p = 1 is REJECTED: it costs more than 3× the minimum RSS",
                   rss_1 > 3 * rss_star))

    # ---- how sharply is p determined? ---------------------------------------
    DETERMINED = mp.mpf("0.30")   # a variant whose 1 %-RSS interval is wider than this
                                  # does not CONSTRAIN p, so it is not evidence ABOUT p

    def interval(rr, pv, rv, **kw):
        """width of the interval where RSS stays within 1 % of its minimum."""
        thresh = rv * mp.mpf("1.01")
        def edge(lo, hi):
            for _ in range(50):
                m = (lo + hi) / 2
                if rss_at(rr, m, **kw) < thresh:
                    lo = m
                else:
                    hi = m
                if abs(hi - lo) < mp.mpf("1e-8"):
                    break
            return (lo + hi) / 2
        a = edge(pv, WINDOW[0] + mp.mpf("0.02"))
        b = edge(pv, WINDOW[1])
        return a, b

    p_lo, p_hi = interval(rows, p_star, rss_star)
    width = p_hi - p_lo
    print(f"\n  determinacy — interval where RSS stays within 1 % of its minimum:")
    print(f"    p ∈ [{mp.nstr(p_lo, 6)}, {mp.nstr(p_hi, 6)}]   width {mp.nstr(width, 6)}   "
          f"=> d ∈ [{mp.nstr(1 / p_hi, 6)}, {mp.nstr(1 / p_lo, 6)}]")
    checks.append(("the exponent IS determined: the 1 %-RSS interval is narrower than 0.30 in p",
                   width < mp.mpf("0.30")))
    checks.append(("the chain's p = 1 lies OUTSIDE the 1 %-RSS interval", not (p_lo <= P_CHAIN <= p_hi)))

    # ---- genericity of the exponent, by qou-rav3's own method ---------------
    print(f"\n  GENERICITY of p, by the method qou-rav3 prescribes (qou-kqdn applied it to its own ratio):")
    variants = [
        ("full basis, all nuclides", rows, {}),
        ("A >= 16", [r for r in rows if r[0] >= 16], {}),
        ("A >= 40", [r for r in rows if r[0] >= 40], {}),
        ("no pairing column", rows, {"pairing": False}),
        ("N = Z ± 1 only, no asymmetry column", [r for r in rows if abs(r[2] - r[1]) <= 1],
         {"asym": False}),
    ]
    print(f"    a variant whose 1 %-RSS interval is wider than {mp.nstr(DETERMINED, 3)} does not CONSTRAIN p,")
    print(f"    so it is not evidence ABOUT p. The threshold is the one already used above, not chosen here.")
    hdr = ("variant".ljust(38) + "n".rjust(6) + "p*".rjust(11) + "d = 1/p*".rjust(11)
           + "1%-RSS width".rjust(14) + "  constrains?")
    print("    " + hdr)
    ps, ps_det, ivals = [], [], {}
    for nm, rr, kw in variants:
        pv, rv = profile(rr, WINDOW[0] + mp.mpf("0.02"), WINDOW[1], **kw)
        a, b = interval(rr, pv, rv, **kw)
        w = b - a
        det = w < DETERMINED
        ps.append(pv)
        ivals[nm] = (a, b, det)
        if det:
            ps_det.append(pv)
        print(f"    {nm:<38}{len(rr):>6}{mp.nstr(pv, 6):>11}{mp.nstr(1 / pv, 6):>11}"
              f"{mp.nstr(w, 4):>14}  {'yes' if det else 'NO'}")
    span = max(ps) - min(ps)
    frac = span / (WINDOW[1] - WINDOW[0])
    span_d = (max(ps_det) - min(ps_det)) if len(ps_det) > 1 else mp.mpf(0)
    frac_d = span_d / (WINDOW[1] - WINDOW[0])
    print(f"    all {len(variants)} variants          : p ∈ [{mp.nstr(min(ps), 6)}, {mp.nstr(max(ps), 6)}]"
          f"   = {mp.nstr(frac * 100, 4)} % of the window [{mp.nstr(WINDOW[0], 2)}, {mp.nstr(WINDOW[1], 2)}]")
    print(f"    the {len(ps_det)} that constrain p : p ∈ [{mp.nstr(min(ps_det), 6)}, {mp.nstr(max(ps_det), 6)}]"
          f"   = {mp.nstr(frac_d * 100, 4)} % of the window")
    print(f"    for comparison            : qou-kqdn's a_S/a_V reached 67.9 %,  qou-rav3's k reached 73.7 %")
    checks.append(("the exponent is far less generic than the two quantities the corpus measured generic "
                   "(a_S/a_V at 67.9 %, k at 73.7 %): every variant, determining or not, stays under 30 %",
                   frac < mp.mpf("0.30")))
    # PRE-REGISTERED EXPECTATION THAT FAILED, recorded rather than dropped: I expected the
    # variants that constrain p to agree within 10 % of the window, so that the spread above
    # would be loss of constraint rather than disagreement. It is NOT. Every variant constrains
    # p (widths 0.06 .. 0.14, all < 0.30), and the all-nuclide and A >= 40 intervals are
    # DISJOINT. So the disagreement is real: no single power-law exponent describes the whole
    # chart, and the fitted "dimension" drifts with the mass cut. The expectation was wrong;
    # the probe is not. The check below asserts what was measured.
    a_all, b_all, det_all = ivals["full basis, all nuclides"]
    a_hvy, b_hvy, det_hvy = ivals["A >= 40"]
    disjoint = b_all < a_hvy or b_hvy < a_all
    print(f"    the all-nuclide and A >= 40 intervals: [{mp.nstr(a_all, 6)}, {mp.nstr(b_all, 6)}] vs "
          f"[{mp.nstr(a_hvy, 6)}, {mp.nstr(b_hvy, 6)}]  ->  {'DISJOINT' if disjoint else 'overlapping'}")
    checks.append(("the spread is genuine DISAGREEMENT, not loss of constraint: every variant constrains p, "
                   "and the all-nuclide and A>=40 1 %-RSS intervals are disjoint, so no single power-law "
                   "exponent describes the whole chart",
                   all(v[2] for v in ivals.values()) and disjoint))
    checks.append(("every analysis variant rejects the chain: no variant's p* exceeds 0.6",
                   max(ps) < mp.mpf("0.6")))

    # ---- cross-check against the prior corpus closure of the A^(-1) scaling --
    # QOU.MassTheory.ChainBindingNoSaturationPeak.chainPerNucleon_eq_hyperbola already proves,
    # by `ring`, that an isobaric chain's per-nucleon binding is EXACTLY c1 + c2/A. My
    # chain_perNucleon is that same object at k=2, k'=1: the scaling is a corpus fact and this
    # work re-derives it from the boundary DEGREE, which the corpus states only as a bond count.
    c1, c2 = EPS, -EPS
    ok = all(abs((c1 + c2 / mp.mpf(A)) - (EPS - EPS * mp.mpf(A) ** (-P_CHAIN))) < TOL
             for A in (2, 4, 12, 56, 208))
    checks.append(("the chain law is the hyperbola c1 + c2/A that ChainBindingNoSaturationPeak proves: "
                   "this re-derives its SCALING from the boundary degree, it does not discover it", ok))

    # a - b*A^(-p) with b,p > 0 is MONOTONE, so it cannot make the iron peak on its own
    # (qou's Faddeev-Niemi verdict records that scope-(b) exclusion for pure power laws).
    # The peak here must come from the Coulomb column, and it does:
    def model(A_, Z_, N_):
        Am = mp.mpf(A_)
        d = mp.mpf(1) if (Z_ % 2 == 0 and N_ % 2 == 0) else (mp.mpf(-1) if (Z_ % 2 and N_ % 2) else mp.mpf(0))
        return (coefs[0] + coefs[1] * Am ** (-p_star) + coefs[2] * mp.mpf(Z_ * Z_) / Am ** (mp.mpf(4) / 3)
                + coefs[3] * (mp.mpf(N_ - Z_) / Am) ** 2 + coefs[4] * d / Am ** (mp.mpf(3) / 2))
    surf_only = [coefs[0] + coefs[1] * mp.mpf(A) ** (-p_star) for (A, Z, N, B) in rows]
    checks.append(("the surface term alone is monotone in A (it cannot make the iron peak; the fitted "
                   "exponent is the DEFICIT's, with Coulomb carried separately)",
                   all(surf_only[i] <= surf_only[j] for i, j in
                       [(rows.index(r1), rows.index(r2)) for r1, r2 in
                        zip(sorted(rows)[:-1], sorted(rows)[1:]) if r1[0] < r2[0]][:200])))
    fitted_peak = max(rows, key=lambda r: model(r[0], r[1], r[2]))
    print(f"\n  the fitted model peaks at A = {fitted_peak[0]} (Z = {fitted_peak[1]}); "
          f"AME's measured peak is at A = {max(rows, key=lambda r: r[3] / r[0])[0]}")
    checks.append(("with Coulomb carried separately the fitted model DOES turn over, and near iron "
                   "(40 <= A <= 80)", 40 <= fitted_peak[0] <= 80))

    # ---- the chain's magnitude, for the record ------------------------------
    plateau = max(B / A for (A, Z, N, B) in rows)
    print(f"\n  for the record — the chain's plateau is ε = {mp.nstr(EPS, 6)} MeV against a measured peak "
          f"B/A of {mp.nstr(plateau, 6)} MeV (factor {mp.nstr(plateau / EPS, 6)}; qou-ib3g's 3.0075)")

    # ---- arithmetic discipline ---------------------------------------------
    checks.append(("NO-FLOAT64: every reported quantity is an mpmath mpf",
                   all(isinstance(v, mp.mpf) for v in
                       [p_star, rss_star, r2_star, rss_13, rss_1, width, frac, frac_d, EPS, E0, plateau] + ps)))

    print("\n  checks")
    for nm, ok in checks:
        print(f"    [{'PASS' if ok else 'FAIL'}] {nm}")
    npass = sum(1 for _, o in checks if o)
    print(f"\n  {npass}/{len(checks)} checks passed")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
