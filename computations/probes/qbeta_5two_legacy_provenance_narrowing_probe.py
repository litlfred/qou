#!/usr/bin/env python3
"""
qou-hfei forensic narrowing: the ~1e-4 error in the two legacy 5₂ V literals.

The corpus carried, citing "GGM eq 21", two literals

    legacy σ₁ (Im V₁ slot) = 1.3790860299
    legacy σ₃ (V₃)         = -2.7580990292

each ~1e-4 (rel 7.9e-5 / 1.05e-4) from the extraction convention

    σ = Re( 3·Li₂(y) + (log y + b·πi)² ) + π²/2,   y a root of y³−2y²+3y−1,
    σ₁ = ext(y₁, b=-1),   σ₃ = ext(y₃, b=+1).

Prior work (bean qou-hfei) refuted two error sources by direct test:
Li₂-series truncation and root imprecision. This probe adds FIVE more and,
decisively, shows that **no degradation of the current formula reproduces the
legacy pair** — which sharpens (and mildly corrects) the bean's "the formula
was right, the evaluation was sloppy" framing: a sloppy evaluation of *this*
formula does not land on the legacy numbers.

Refuted here (scope-(a), direct test), for both legacy values:
  H1 truncated π (3–10 digits)         → converges to the TRUE value, not legacy
  H2 root rounded to 3–8 dp            → map is insensitive; no effect (confirms bean)
  H3 perturbed/typo'd cubic coeffs     → nearest legacy repro off by ≥ 8e-3 (8.3e-3)
  H4 clean rational-π² additive shift  → implied shifts are 0.49999·π² and
                                          0.50003·π², independently off π²/2
  H5 low mpmath working precision      → even dps=6 converges to the TRUE value

Conclusion: the legacy pair is NOT a degraded evaluation of the current
formula. It is consistent only with a *different* computation (different
normalization/source) that agrees to ~4 sig figs. Source remains unidentified.
The values are unused in production (V₃ follows from V₁ via the proved sum rule
V₃ = −2·Re(V₁) − 3π²/2); this is cold forensics → recommend `wontfix`.

Self-contained (mpmath only). No fit; no production wiring.
"""
import mpmath as mp
import itertools

mp.mp.dps = max(50, mp.mp.dps)
I = mp.mpc(0, 1)
L1 = mp.mpf("1.3790860299")
L3 = mp.mpf("-2.7580990292")


def _sV(y, branch, pi):
    return 3 * mp.polylog(2, y) + (mp.log(y) + branch * pi * I) ** 2


def _ext(y, branch, pi=None):
    pi = mp.pi if pi is None else pi
    return mp.re(_sV(y, branch, pi)) + pi ** 2 / 2


def _roots(dps=40):
    mp.mp.dps = dps
    rts = mp.polyroots([1, -2, 3, -1], maxsteps=400, extraprec=400)
    y3 = next(r for r in rts if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 3))
    y1 = next(r for r in rts if mp.im(r) > 0)
    return y1, y3


def main() -> int:
    mp.mp.dps = 40
    y1, y3 = _roots()
    s1t, s3t = _ext(y1, -1), _ext(y3, +1)
    print("qou-hfei — provenance narrowing of the legacy 5₂ V literals\n")
    print(f"  TRUE   σ₁ = {mp.nstr(s1t, 15)}   σ₃ = {mp.nstr(s3t, 15)}")
    print(f"  LEGACY σ₁ = {mp.nstr(L1, 12)} (Δ {mp.nstr(L1 - s1t, 3)})"
          f"   σ₃ = {mp.nstr(L3, 12)} (Δ {mp.nstr(L3 - s3t, 3)})\n")

    refuted = {}

    # H1 truncated π
    h1 = min(
        (max(abs(_ext(y1, -1, mp.mpf(mp.nstr(mp.pi, d))) - L1),
             abs(_ext(y3, +1, mp.mpf(mp.nstr(mp.pi, d))) - L3)))
        for d in range(3, 11)
    )
    refuted["H1_truncated_pi_min_maxerr"] = mp.nstr(h1, 4)

    # H2 rounded root
    def _rr(nd):
        y1r = mp.mpc(round(float(mp.re(y1)), nd), round(float(mp.im(y1)), nd))
        y3r = mp.mpf(round(float(y3), nd))
        return max(abs(_ext(y1r, -1) - L1), abs(_ext(y3r, +1) - L3))
    refuted["H2_rounded_root_min_maxerr"] = mp.nstr(min(_rr(nd) for nd in range(3, 9)), 4)

    # H3 perturbed cubic
    best = None
    for da, db, dc in itertools.product([-1, 0, 1], repeat=3):
        coeffs = [1, -2 + da, 3 + db, -1 + dc]
        if coeffs == [1, -2, 3, -1]:
            continue
        try:
            rr = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
        except Exception:  # noqa: BLE001
            continue
        for r in rr:
            for br in (-1, 0, 1):
                try:
                    v = _ext(r, br)
                except Exception:  # noqa: BLE001
                    continue
                for val, L in ((v, L1), (v, L3)):
                    e = abs(val - L)
                    if best is None or e < best:
                        best = e
    refuted["H3_perturbed_cubic_best_err"] = mp.nstr(best, 4)

    # H4 implied additive shift vs π²/2
    c1 = L1 - mp.re(_sV(y1, -1, mp.pi))
    c3 = L3 - mp.re(_sV(y3, +1, mp.pi))
    refuted["H4_shift_c1_over_pi2"] = mp.nstr(c1 / mp.pi ** 2, 10)
    refuted["H4_shift_c3_over_pi2"] = mp.nstr(c3 / mp.pi ** 2, 10)

    # H5 low working precision
    def _lp(dps):
        y1d, y3d = _roots(dps)
        s1 = mp.mpf(str(_ext(y1d, -1)))
        s3 = mp.mpf(str(_ext(y3d, +1)))
        mp.mp.dps = 40
        return max(abs(s1 - L1), abs(s3 - L3))
    refuted["H5_low_precision_min_maxerr"] = mp.nstr(min(_lp(d) for d in (6, 7, 8, 9, 10)), 4)
    mp.mp.dps = 40

    print("  Refuted error sources (min |error| vs legacy, over the swept parameter):")
    for k, v in refuted.items():
        print(f"    {k:34s} = {v}")

    print("\n  VERDICT: no degradation of the current formula (π precision, root "
          "rounding,\n  cubic coefficients, additive shift, working precision) "
          "reproduces the legacy\n  pair (all ≥ ~6e-5 from legacy while the TRUE "
          "value is reproduced instead).\n  The legacy pair is a DIFFERENT "
          "computation agreeing to ~4 sig figs, not a\n  sloppy eval of this "
          "formula. Source unidentified; values unused → wontfix.")

    # Assertions: each refuted source stays away from the legacy value.
    assert h1 > mp.mpf("5e-5"), "H1 unexpectedly reproduced legacy"
    assert best > mp.mpf("1e-3"), "H3 unexpectedly reproduced legacy"
    assert min(_lp(d) for d in (6, 7, 8)) > mp.mpf("5e-5"), "H5 unexpectedly reproduced legacy"
    print("\n  [assert] H1, H3, H5 all stay > 5e-5 from legacy — PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
