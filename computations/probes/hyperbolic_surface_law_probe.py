#!/usr/bin/env python3
"""
Probe — the hyperbolic surface law against AME: does the framework's OWN geometry
predict the surface term, and how badly does it fit?

CONTEXT. Four merged tranches on the binding-law arc (#6761, #6780, #6801, #6886)
imported the compact EUCLIDEAN surface law A_surf ~ A^(2/3), and the corpus
objected each time that the ambient geometry is H^3. `QOU.Mass.HyperbolicSurfaceLaw`
is the hyperbolic computation, and it is exact: a ball of radius R in H^3 has
V = pi(sinh 2R - 2R) (Bolyai's formula, HELD: library/arxiv-1010.5321v3 §3.1) and
S = V' = 2pi(cosh 2R - 1), and

    S - 2V = 2 pi (e^(-2R) + 2R - 1) >= 0    so    S/V >= 2   for every R > 0.

In Euclidean space S/V = 3/R -> 0 and that vanishing is the whole origin of the
A^(-1/3) surface term. In H^3 the surface fraction never vanishes: a hyperbolic
cluster FAILS HasBulk under any radius assignment, its "surface term" is a
CONSTANT shift of the volume coefficient, and the residual A-dependence is
f - 2 <= 4R/(sinh 2R - 2R), which with R ~ (1/2) ln A is of order (ln A)/A.

PRE-REGISTERED EXPECTATION, stated before running: the hyperbolic form fits
WORSE than the Euclidean import, because the corpus had measured that using H^3
consistently costs 2.64x on the Coulomb radius (sm-26-parameter-chip-away.md).

THAT EXPECTATION FAILED. The hyperbolic (ln A)/A fits BETTER: RSS 31.44 against
38.53 (ratio 0.816), and it beats the best pure power #6780 found (38.19). The
exact ball at its best v0 also beats the import (35.18). Section 3b then asks
whether the win is generic: it is not — 0 of 9 "reasonable" shapes beat the
Euclidean import and the hyperbolic one beats all 9; and within its own family
(ln A)^m/A^p at m = 1 the optimum sits at p* = 0.912, within 0.09 of the
hyperbolic p = 1. One caution the same scan surfaces: letting m float to 2 keeps
improving (21.90 at p* = 0.34), so log factors ARE absorbing structure, and the
hyperbolic point is the best PREDICTED shape, not the global optimum of a
two-parameter search — which would be a fit, and is not claimed.

WHAT IS MEASURED:
  1. the Lean identities numerically, including V' = S by finite difference and
     Bolyai's formula at curvature 1, and S/V -> 2 numerically;
  2. B/A fitted on [1, phi(A), Coulomb, asymmetry, pairing] for three surface
     shapes phi: Euclidean A^(-1/3), hyperbolic leading (ln A)/A, and the chain's
     1/A (p = 1), with RSS and R^2 side by side;
  3. the EXACT hyperbolic fraction f(R(A)) with V(R(A)) = v0*A, profiled over the
     one volume-per-nucleon parameter v0 by grid + golden section — no starting
     guess — so the hyperbolic form gets its best possible showing;
  4. the Stokes bridge: an affine singular count over an affine kite count has a
     ratio tending to a nonzero constant (affine_over_affine_not_surfaceTerm),
     checked numerically on the corpus's measured affine Seifert invariants.

Arithmetic: mpmath 50 dps. No float64 anywhere.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

import surface_exponent_is_dimension_probe as sx  # noqa: E402  (#6780's exact least squares)

mp.mp.dps = 50
TOL = mp.mpf(10) ** (-40)
ROOT = Path(__file__).resolve().parents[2]
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"
PI = mp.pi


def hyp_vol(R):
    return PI * (mp.sinh(2 * R) - 2 * R)


def hyp_area(R):
    return 4 * PI * mp.sinh(R) ** 2


def bolyai_vol(x, k):
    """Horvath §3.1, Bolyai: pi k^3 sinh(2x/k) - 2 pi k^2 x."""
    return PI * k ** 3 * mp.sinh(2 * x / k) - 2 * PI * k ** 2 * x


def R_of_A(v0, A, cache={}):
    """radius with V(R) = v0*A, by root-finding; cached per (v0, A)."""
    key = (mp.nstr(v0, 30), A)
    if key not in cache:
        target = v0 * A
        # good bracket: V ~ (pi/2) e^{2R} for large R
        guess = mp.log(2 * target / PI + 2) / 2
        cache[key] = mp.findroot(lambda R: hyp_vol(R) - target, guess)
    return cache[key]


def design(rows, phi):
    X, y = [], []
    for (A, Z, N, B) in rows:
        Am = mp.mpf(A)
        d = mp.mpf(1) if (Z % 2 == 0 and N % 2 == 0) else (mp.mpf(-1) if (Z % 2 and N % 2) else mp.mpf(0))
        X.append([mp.mpf(1), phi(Am), mp.mpf(Z * Z) / Am ** (mp.mpf(4) / 3),
                  (mp.mpf(N - Z) / Am) ** 2, d / Am ** (mp.mpf(3) / 2)])
        y.append(B / Am)
    return X, y


def main() -> int:
    checks: list[tuple[str, bool]] = []

    # ---- 1. the Lean identities ------------------------------------------
    print("  THE HYPERBOLIC BALL — identities the Lean proves, checked numerically\n")
    ok = all(abs(hyp_area(R) - 2 * PI * (mp.cosh(2 * R) - 1)) < TOL for R in (mp.mpf("0.3"), 1, 5, 20))
    checks.append(("hypArea_eq: 4 pi sinh^2 R = 2 pi (cosh 2R - 1)", ok))
    ok = all(abs(hyp_vol(R) - bolyai_vol(R, mp.mpf(1))) < TOL for R in (mp.mpf("0.3"), 1, 5, 20))
    checks.append(("hypVol IS Bolyai's held formula (horvath2010 §3.1) at curvature k = 1", ok))
    # S and 2V agree to ~4R digits at large R, so compare RELATIVE to S: the first version used an
    # absolute 1e-40 and failed at R = 20 on cancellation alone (S ~ 7e17). A check defect, not the Lean's.
    ok = all(abs((hyp_area(R) - 2 * hyp_vol(R)) - 2 * PI * (mp.exp(-2 * R) + 2 * R - 1)) < TOL * hyp_area(R)
             for R in (mp.mpf("0.3"), 1, 5, 20))
    checks.append(("hypArea_sub_two_mul_hypVol: S - 2V = 2 pi (e^(-2R) + 2R - 1) exactly (relative to S)", ok))
    # mp.diff picks its own step; the first version used h = 1e-20 and divided 50-dps rounding by 2h,
    # which inflates it to ~1e-23 — a check defect, not the Lean's. Relative tolerance 1e-30.
    ok = all(abs(mp.diff(hyp_vol, R) - hyp_area(R)) < mp.mpf(10) ** (-30) * hyp_area(R)
             for R in (mp.mpf("0.5"), 1, 3, 8))
    checks.append(("hasDerivAt_hypVol: V'(R) = S(R) by central difference at 50 dps — the area rests "
                   "on the held volume", ok))
    print(f"    {'R':>5}{'S/V (hyperbolic)':>20}{'3/R (Euclidean)':>18}{'S/V - 2':>16}{'bound 4R/(sinh2R-2R)':>24}")
    fr = {}
    for R in (mp.mpf("0.5"), 1, 2, 5, 10, 20):
        R = mp.mpf(R)
        f = hyp_area(R) / hyp_vol(R)
        fr[R] = f
        bnd = 4 * R / (mp.sinh(2 * R) - 2 * R)
        print(f"    {mp.nstr(R, 3):>5}{mp.nstr(f, 12):>20}{mp.nstr(3 / R, 8):>18}{mp.nstr(f - 2, 6):>16}{mp.nstr(bnd, 6):>24}")
    checks.append(("surfaceFraction_ge_two: S/V >= 2 at every R sampled", all(f >= 2 for f in fr.values())))
    checks.append(("surfaceFraction_sub_two_le: S/V - 2 <= 4R/(sinh 2R - 2R) at every R sampled",
                   all(fr[R] - 2 <= 4 * R / (mp.sinh(2 * R) - 2 * R) + TOL for R in fr)))
    checks.append(("S/V -> 2: at R = 20 the fraction is within 1e-15 of 2 (the limit the Lean does "
                   "not formalise, checked numerically)", abs(fr[mp.mpf(20)] - 2) < mp.mpf("1e-15")))
    checks.append(("the Euclidean fraction 3/R -> 0 while the hyperbolic one -> 2: at R = 20 they "
                   "differ by more than 1.8", abs(fr[mp.mpf(20)] - 3 / mp.mpf(20)) > mp.mpf("1.8")))

    # ---- 2. data -------------------------------------------------------------
    rows = []
    for ent in json.loads(AME.read_text())["entries"]:
        Z, N, A = ent["Z"], ent["N"], ent["A"]
        bpa = ent.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not bpa or ent.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B > 0:
            rows.append((A, Z, N, B))
    checks.append(("AME selection reproduces #6611's 2548 measured nuclides", len(rows) == 2548))

    print(f"\n  THE SURFACE SHAPE AGAINST AME — B/A on [1, phi(A), Coulomb, asymmetry, pairing], "
          f"{len(rows)} nuclides")
    print(f"    PRE-REGISTERED: the hyperbolic (ln A)/A fits WORSE than the Euclidean A^(-1/3).\n")
    shapes = [("Euclidean   A^(-1/3)", lambda A: A ** (-mp.mpf(1) / 3)),
              ("hyperbolic  (ln A)/A", lambda A: mp.log(A) / A),
              ("chain       1/A     ", lambda A: 1 / A)]
    res = {}
    print(f"    {'surface shape phi(A)':<26}{'RSS':>12}{'R^2':>12}{'a_V (MeV)':>12}{'coef/a_V':>12}")
    for nm, phi in shapes:
        X, y = design(rows, phi)
        coef, r2, rss = sx.fit(X, y)
        res[nm] = (rss, r2, coef)
        print(f"    {nm:<26}{mp.nstr(rss, 6):>12}{mp.nstr(r2, 7):>12}{mp.nstr(coef[0], 6):>12}"
              f"{mp.nstr(coef[1] / coef[0], 6):>12}")
    rss_e, rss_h, rss_c = res["Euclidean   A^(-1/3)"][0], res["hyperbolic  (ln A)/A"][0], res["chain       1/A     "][0]
    # PRE-REGISTERED EXPECTATION THAT FAILED, recorded rather than dropped. This check first
    # asserted rss_h > rss_e — that the framework's own geometry would fit WORSE than the imported
    # Euclidean packing, because sm-26 had measured a 2.64x consistency cost on the Coulomb radius.
    # It fits BETTER: 31.44 against 38.53, a ratio of 0.816. The expectation was wrong; the probe is
    # not. The check now asserts what was measured. Section 3b below tests whether the win is generic.
    checks.append(("PRE-REGISTERED EXPECTATION FAILED (recorded): the hyperbolic (ln A)/A fits BETTER "
                   "than the Euclidean A^(-1/3) — RSS smaller — where a worse fit was predicted",
                   rss_h < rss_e))
    checks.append(("...but BETTER than the chain's bare 1/A: the logarithm does real work "
                   "(RSS smaller than the chain's)", rss_h < rss_c))
    checks.append(("the hyperbolic surface coefficient has the SEMF sign (negative — a deficit)",
                   res["hyperbolic  (ln A)/A"][2][1] < 0))
    print(f"\n    hyperbolic/Euclidean RSS ratio = {mp.nstr(rss_h / rss_e, 5)}   "
          f"(sm-26 measured 2.64x on the Coulomb radius)")
    print(f"    hyperbolic/chain     RSS ratio = {mp.nstr(rss_h / rss_c, 5)}")

    # ---- 3. the EXACT hyperbolic fraction, profiled over v0 ------------------
    print(f"\n  THE EXACT FRACTION f(R(A)) = S/V at V(R(A)) = v0*A, profiled over v0 (grid + golden)")

    def rss_at(v0):
        X, y = design(rows, lambda A: hyp_area(R_of_A(v0, int(A))) / hyp_vol(R_of_A(v0, int(A))))
        return sx.fit(X, y)[2]
    lo, hi = mp.mpf(-3), mp.mpf(3)          # log10 v0
    best = None
    for i in range(13):
        lv = lo + (hi - lo) * i / 12
        r = rss_at(mp.mpf(10) ** lv)
        if best is None or r < best[1]:
            best = (lv, r)
    a, b = best[0] - (hi - lo) / 12, best[0] + (hi - lo) / 12
    gr = (mp.sqrt(5) - 1) / 2
    c_, d_ = b - gr * (b - a), a + gr * (b - a)
    fc, fd = rss_at(mp.mpf(10) ** c_), rss_at(mp.mpf(10) ** d_)
    for _ in range(25):
        if fc < fd:
            b, d_, fd = d_, c_, fc
            c_ = b - gr * (b - a)
            fc = rss_at(mp.mpf(10) ** c_)
        else:
            a, c_, fc = c_, d_, fd
            d_ = a + gr * (b - a)
            fd = rss_at(mp.mpf(10) ** d_)
    lv_star = (a + b) / 2
    v0_star = mp.mpf(10) ** lv_star
    rss_x = rss_at(v0_star)
    Rmin, Rmax = R_of_A(v0_star, min(r[0] for r in rows)), R_of_A(v0_star, max(r[0] for r in rows))
    print(f"    v0* = {mp.nstr(v0_star, 6)} (log10 {mp.nstr(lv_star, 4)})   RSS = {mp.nstr(rss_x, 6)}   "
          f"R(A) spans [{mp.nstr(Rmin, 4)}, {mp.nstr(Rmax, 4)}]")
    print(f"    exact-hyperbolic / Euclidean RSS ratio = {mp.nstr(rss_x / rss_e, 5)}")
    # Same failed pre-registration for the exact ball: predicted worse, measured better (35.18 vs 38.53).
    checks.append(("PRE-REGISTERED EXPECTATION FAILED (recorded): the exact hyperbolic ball at its best "
                   "v0 ALSO fits better than the Euclidean A^(-1/3)", rss_x < rss_e))
    checks.append(("the profiled v0 is interior to the scanned decade range (not a boundary artefact)",
                   lo + mp.mpf("0.1") < lv_star < hi - mp.mpf("0.1")))
    # The first version asserted exact <= leading "because it has one more free number". WRONG:
    # (ln A)/A is the ball's LARGE-R asymptotic shape with a free amplitude, not a member of the
    # exact family {f(R(A)) : v0}, so nothing forces that order — and the data go the other way.
    # What the exact fit actually says: at its best v0 the nuclei sit at R in [0.34, 1.5], the
    # SMALL-radius regime where S/V ~ 3/R is near-Euclidean, NOT the large-R regime where the
    # (ln A)/A form lives. So the data prefer the asymptotic SHAPE over a literal extensive-volume
    # ball. That is the honest reading and the check below asserts it.
    R_at_A56 = R_of_A(v0_star, 56)
    print(f"    at v0*, iron sits at R = {mp.nstr(R_at_A56, 4)}: S/V there is {mp.nstr(hyp_area(R_at_A56) / hyp_vol(R_at_A56), 5)}"
          f" against Euclidean 3/R = {mp.nstr(3 / R_at_A56, 5)} — the near-Euclidean regime")
    checks.append(("the exact ball at its best v0 puts every nucleus at R < 2 (near-Euclidean regime), "
                   "and its asymptotic (ln A)/A SHAPE fits better than the ball itself: the data prefer "
                   "the shape, not a literal extensive-volume hyperbolic ball", Rmax < 2 and rss_h < rss_x))

    # ---- 3b. GENERICITY — the qou-rav3 / qou-kqdn discipline, applied to my own win --------
    print(f"\n  GENERICITY — is (ln A)/A a lucky point, or the optimum of its family?")
    print(f"    Family (ln A)^m / A^p, p profiled for each m; and a zoo of 'reasonable' shapes.")

    def rss_shape(phi):
        X, y = design(rows, phi)
        return sx.fit(X, y)[2]

    def profile_p(m):
        f = lambda p: rss_shape(lambda A: mp.log(A) ** m / A ** p)
        lo_, hi_ = mp.mpf("0.05"), mp.mpf(3)
        best_ = None
        for i in range(30):
            p_ = lo_ + (hi_ - lo_) * i / 29
            r_ = f(p_)
            if best_ is None or r_ < best_[1]:
                best_ = (p_, r_)
        a_, b_ = max(lo_, best_[0] - (hi_ - lo_) / 29), min(hi_, best_[0] + (hi_ - lo_) / 29)
        g_ = (mp.sqrt(5) - 1) / 2
        c1, d1 = b_ - g_ * (b_ - a_), a_ + g_ * (b_ - a_)
        f1, f2 = f(c1), f(d1)
        for _ in range(30):
            if f1 < f2:
                b_, d1, f2 = d1, c1, f1
                c1 = b_ - g_ * (b_ - a_); f1 = f(c1)
            else:
                a_, c1, f1 = c1, d1, f2
                d1 = a_ + g_ * (b_ - a_); f2 = f(d1)
        p_ = (a_ + b_) / 2
        return p_, f(p_)
    fam = {}
    print(f"    {'m':>3}{'p*':>10}{'RSS at p*':>12}   note")
    for m in (0, 1, 2):
        p_, r_ = profile_p(m)
        fam[m] = (p_, r_)
        note = {0: "pure power (#6780 found 0.364 / 38.19)", 1: "log-corrected: (ln A)/A is p = 1",
                2: "log-squared"}[m]
        print(f"    {m:>3}{mp.nstr(p_, 6):>10}{mp.nstr(r_, 6):>12}   {note}")
    checks.append(("m = 0 reproduces #6780: the best pure power is p* ~ 0.364 with RSS ~ 38.19",
                   abs(fam[0][0] - mp.mpf("0.364")) < mp.mpf("0.01") and abs(fam[0][1] - mp.mpf("38.19")) < mp.mpf("0.1")))
    checks.append(("the log-corrected family's optimum p* is within 0.15 of the hyperbolic value p = 1: "
                   "(ln A)/A is near the optimum of its own family, not a lucky point on its flank",
                   abs(fam[1][0] - 1) < mp.mpf("0.15")))
    checks.append(("the m = 1 optimum beats the m = 0 optimum: the logarithm itself is what does the "
                   "work, not a shifted exponent", fam[1][1] < fam[0][1]))

    zoo = [("A^(-1/4)", lambda A: A ** (-mp.mpf(1) / 4)), ("A^(-1/2)", lambda A: A ** (-mp.mpf(1) / 2)),
           ("A^(-2/3)", lambda A: A ** (-mp.mpf(2) / 3)), ("1/ln A", lambda A: 1 / mp.log(A)),
           ("ln A / A^(1/3)", lambda A: mp.log(A) / A ** (mp.mpf(1) / 3)),
           ("ln A / A^(1/2)", lambda A: mp.log(A) / A ** (mp.mpf(1) / 2)),
           ("ln A / A^(2/3)", lambda A: mp.log(A) / A ** (mp.mpf(2) / 3)),
           ("(ln A)^2 / A", lambda A: mp.log(A) ** 2 / A), ("1/A^2", lambda A: A ** (-2))]
    beats = 0
    print(f"    zoo of 'reasonable' shapes against Euclidean RSS {mp.nstr(rss_e, 6)}:")
    for nm, phi in zoo:
        r_ = rss_shape(phi)
        b_ = r_ < rss_e
        beats += int(b_)
        print(f"      {nm:<16}{mp.nstr(r_, 6):>10}   {'beats Euclidean' if b_ else '-'}")
    print(f"    {beats} of {len(zoo)} zoo shapes beat the Euclidean A^(-1/3); the hyperbolic (ln A)/A "
          f"at {mp.nstr(rss_h, 6)} beats all of them: {all(rss_h < rss_shape(phi) for _, phi in zoo)}")
    checks.append(("the hyperbolic (ln A)/A beats EVERY shape in the zoo, so it is not merely one of many "
                   "shapes that happen to beat the Euclidean import",
                   all(rss_h < rss_shape(phi) for _, phi in zoo)))

    # ---- 4. the Stokes bridge --------------------------------------------------
    print(f"\n  THE STOKES BRIDGE — affine singular count / affine kite count -> nonzero constant")
    # the corpus's measured affine Seifert invariants of the canonical closure (six nuclei):
    seifert = {"crossings 12A-1": (12, -1), "chi = -9A+1": (-9, 1), "2g = 8A": (8, 0), "sigma 6A-1": (6, -1)}
    A_big = mp.mpf(10) ** 6
    ratios = {}
    for nm, (al, be) in seifert.items():
        # against the kite-tail 3A-1, itself affine
        ratios[nm] = (al * A_big + be) / (3 * A_big - 1)
        print(f"    {nm:<18} / (3A-1)  at A = 1e6:  {mp.nstr(ratios[nm], 8)}   (-> {mp.nstr(mp.mpf(al) / 3, 6)})")
    checks.append(("every measured affine invariant over the affine kite-tail count tends to a "
                   "NONZERO constant, never to 0: no affine singular count is a surface term "
                   "(affine_over_affine_not_surfaceTerm)",
                   all(abs(r - mp.mpf(al) / 3) < mp.mpf("1e-5") and abs(r) > mp.mpf("0.1")
                       for (nm, (al, be)), r in zip(seifert.items(), ratios.values()))))
    print(f"    The A-scaling of Yekutieli's SINGULAR count itself is not computed anywhere in the")
    print(f"    corpus; that is the open item, beaned, not guessed.")

    checks.append(("NO-FLOAT64: every reported quantity is an mpmath mpf",
                   all(isinstance(v, mp.mpf) for v in [rss_e, rss_h, rss_c, rss_x, v0_star, TOL] + list(fr.values()))))

    print("\n  checks")
    for nm, ok_ in checks:
        print(f"    [{'PASS' if ok_ else 'FAIL'}] {nm}")
    npass = sum(1 for _, o in checks if o)
    print(f"\n  {npass}/{len(checks)} checks passed")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
