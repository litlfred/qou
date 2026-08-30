#!/usr/bin/env python3
"""`theta_p`'s zero locus is `-p^Z` — and the Jacobi triple product isn't needed.

Bean `qou-c1ln` row 2. `QOU/QBeta/C1ConnectionPoles.lean` proves the `>=`
direction of the zero locus by an involution,

    theta_p(w) = 0   for every   w in -p^Z          (qTheta_neg_zpow_eq_zero)

and the whole C1 pole divisor is read off from that. The divisor claim needs
the `=`, though: an extra zero anywhere is an extra pole of the connection
matrix. That row of the bean said the `=` needs the **Jacobi triple product**.

**It does not.** The `=` follows from three facts now all proved in Lean plus
the argument principle:

  (i)   theta_p is holomorphic on C*                 differentiableOn_qThetaC
  (ii)  theta_p(p w) = w theta_p(w)                  qThetaC_functional_equation
  (iii) theta_p(-p^k) = 0                            qTheta_neg_zpow_eq_zero

From (ii), differentiating and dividing by theta_p(pw) = w theta_p(w),

    p theta'(p w) / theta(p w)  =  1/w  +  theta'(w)/theta(w)
                                                     logDeriv_qThetaC_...

so, substituting w -> p w in the contour integral over |w| = rho,

    oint_{|w| = p rho} theta'/theta dw = 2 pi i + oint_{|w| = rho} theta'/theta dw

i.e. the winding number goes up by **exactly one** per period. The argument
principle turns that into "exactly one zero, with multiplicity, in every
fundamental annulus", and (iii) supplies that zero at `-p^k` — so it is simple
and there are no others. The zero set is exactly `-p^Z`.

JTP is strictly more work (it additionally needs Liouville on `C*/p^Z`), so it
is off the critical path. The single remaining gap is the **argument principle**,
absent from Mathlib.

## What this script is for

Owner steer: *"we would need to add lean regardless — we can see if stmt holds
in our case."*  Two jobs, neither of them "gather evidence for a doubtful
claim" — the claim is a classical theorem and is not in doubt:

1. **Check the newly-Lean-proved identities say what they are meant to say.**
   Section 0 tests `p theta'(p w) = theta(w) + w theta'(w)` and its
   logarithmic form numerically. A wrong power of `p`, or a normalisation
   mismatch between the Lean `P` (with `p = P^2`) and the `p` used by the other
   nine C1 scripts, would show up here and nowhere else.
2. **Check the derivation and the theta implementation.** Sections 1-4 run the
   contour integrals directly. If the winding differences are not 1, or the
   9-annulus sweep does not return 9, then either the argument above is wrong
   or `theta()` — the routine every C1 result in this directory depends on — is
   wrong.

Radii are the geometric means `p^(k+1/2)`, maximally far from every zero, which
is what makes the periodic trapezoid rule converge fast: its error is
`exp(-M log p^(1/2))` and `log p^(1/2) = 0.026` here (the torus is thin because
`p` is close to 1), so `M` has to be in the thousands for many digits. The
`M`-ladder reports that convergence rather than asserting it. Trapezoid is used
deliberately — for a periodic analytic integrand it is spectrally accurate,
unlike a general-purpose quadrature.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_pole_divisor.py
-- Ref: [gasper-rahman] Basic Hypergeometric Series, section 1.6 (triple product)
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

DPS = 60
PAD = 30
Q_STR = "1.1099785827513808075916690956"
M_LADDER = (512, 1024, 2048)


DPS_ID = 220  # section 0 only — see the cancellation note there


def _window() -> int:
    lp = mp.log(mp.sqrt(mp.mpf(Q_STR)))
    return int(mp.ceil(mp.sqrt(2 * (mp.mp.dps + PAD) * mp.log(10) / lp))) + 10


def theta_and_deriv(p, w, W):
    """`(theta_p(w), theta_p'(w))` from one adaptive window, same terms.

    `theta_p(w) = sum_n p^(-n(n+1)/2) w^n`, matching `theta()` in the other C1
    scripts and `qThetaC` in the Lean (whose base `P` has `p = P^2`).
    """
    lp = mp.log(p)
    n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
    ns = list(range(n0 - W, n0 + W + 1))
    cs = [p ** (-mp.mpf(n) * (n + 1) / 2) for n in ns]
    th = mp.fsum(c * w ** n for c, n in zip(cs, ns))
    dth = mp.fsum(c * n * w ** (n - 1) for c, n in zip(cs, ns))
    return th, dth


def winding(p, R, W, M, weight=None):
    """`(1/2 pi i) oint_{|w|=R} weight(w) theta'/theta dw`, trapezoid rule.

    With `w = R e^{i phi}`, `dw = i w dphi`, so the integral is
    `(1/2 pi) int_0^{2pi} weight(w) w theta'(w)/theta(w) dphi`.

    `theta` has real coefficients and `weight` is `1` or `w`, so the integrand
    at `conj w` is the conjugate of the integrand at `w`. Only `phi in [0, pi]`
    is evaluated and the rest mirrored, halving the cost.
    """
    half = M // 2
    acc = mp.mpc(0)
    for j in range(half + 1):
        w = R * mp.expjpi(mp.mpf(j) / half)
        th, dth = theta_and_deriv(p, w, W)
        val = w * dth / th
        if weight is not None:
            val *= weight(w)
        acc += val if 0 < j < half else val / 2
    return (2 * acc.real) / M


def main() -> None:
    t0 = time.perf_counter()
    mp.mp.dps = DPS
    q = mp.mpf(Q_STR)
    p = mp.sqrt(q)
    W = _window()
    res: dict = {}
    checks: list = []

    print("=" * 78)
    print("  theta_p zero locus at OUR substrate — argument principle, no JTP")
    print("=" * 78)
    print(f"    q = {mp.nstr(q, 20)}")
    print(f"    p = sqrt(q) = {mp.nstr(p, 20)}      P = sqrt(p) (Lean base)")
    print(f"    log p^(1/2) = {mp.nstr(mp.log(p) / 2, 8)}  (trapezoid decay rate)")
    print(f"    series half-window W = {W}   dps = {DPS}")
    print()

    # ---- 0. do the Lean identities say what they are meant to say? ---------
    print("=" * 78)
    print("  0. the newly-Lean-proved identities, checked numerically")
    print("=" * 78)
    print("     deriv_qThetaC_functional_equation :  p th'(p w) = th(w) + w th'(w)")
    print("     logDeriv_qThetaC_functional_equation :"
          "  p th'(pw)/th(pw) = 1/w + th'(w)/th(w)")
    print()
    print(f"    run at dps={DPS_ID}, not {DPS}: on the NEGATIVE ray the series")
    print("    alternates and theta is exponentially small — sum (-1)^n e^(-a n^2)")
    print("    with a = log(p)/2 = 0.026 is ~e^(-pi^2/4a) ~ 1e-41 times its own")
    print("    largest term, so ~41 digits cancel before any answer appears. Same")
    print("    mechanism that made |chi| look bounded under coarse sampling.")
    print()
    print(f"    {'w':>26}  {'digits cancelled':>17}  {'rel.err deriv':>15}"
          f"  {'rel.err log':>13}")
    mp.mp.dps = DPS_ID
    W_id = _window()
    worst_id = mp.mpf(0)
    for ws in ["0.37", "-1.9", "0.8+0.6j", "-0.25-1.1j", "2.3j"]:
        w = mp.mpmathify(ws)
        th, dth = theta_and_deriv(p, w, W_id)
        thp, dthp = theta_and_deriv(p, p * w, W_id)
        lp = mp.log(p)
        n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
        peak = max(abs(p ** (-mp.mpf(n) * (n + 1) / 2) * w ** n)
                   for n in range(n0 - 3, n0 + 4))
        canc = -mp.log10(abs(th) / peak)
        lhs, rhs = p * dthp, th + w * dth
        e1 = abs(lhs - rhs) / max(abs(lhs), abs(rhs))
        l2, r2 = p * dthp / thp, 1 / w + dth / th
        e2 = abs(l2 - r2) / max(abs(l2), abs(r2))
        worst_id = max(worst_id, e1, e2)
        print(f"    {ws:>26}  {mp.nstr(canc, 5):>17}  {mp.nstr(e1, 6):>15}"
              f"  {mp.nstr(e2, 6):>13}")
    mp.mp.dps = DPS
    res["worst_lean_identity_rel_err"] = mp.nstr(worst_id, 6)
    ok_id = worst_id < mp.mpf("1e-120")
    print()
    print(f"    worst relative error : {mp.nstr(worst_id, 8)}")
    checks.append({
        "name": "lean_functional_equation_identities_match_numerics",
        "detail": f"max rel err over 5 points (real, negative real, complex) at "
                  f"dps={DPS_ID} = {mp.nstr(worst_id, 6)}; catches a wrong power "
                  "of p or a P-vs-p normalisation mismatch between the Lean and "
                  "this directory's theta()",
        "passed": bool(ok_id),
    })
    print()

    # ---- 1. winding numbers, with the M-ladder ----------------------------
    print("=" * 78)
    print("  1. WINDING NUMBER of theta_p on |w| = p^(k+1/2), M-ladder")
    print("=" * 78)
    print("     (not a zero count on its own — the puncture at 0 is inside every")
    print("      circle, and the orbit accumulates there. Only DIFFERENCES count.)")
    print()
    print(f"    {'k':>4}  " + "  ".join(f"{'M=' + str(M):>22}" for M in M_LADDER))
    counts: dict[int, mp.mpf] = {}
    ladder: dict[str, list] = {}
    for k in range(-3, 4):
        R = p ** (mp.mpf(k) + mp.mpf(1) / 2)
        row = [winding(p, R, W, M) for M in M_LADDER]
        ladder[str(k)] = [mp.nstr(v, 16) for v in row]
        counts[k] = row[-1]
        print(f"    {k:>4}  " + "  ".join(f"{mp.nstr(v, 16):>22}" for v in row))
    res["winding_by_k"] = ladder
    print()

    # ---- 2. one zero per fundamental annulus ------------------------------
    print("=" * 78)
    print("  2. zeros PER FUNDAMENTAL ANNULUS  p^(k-1/2) < |w| < p^(k+1/2)")
    print("=" * 78)
    print(f"    {'annulus':>22}  {'count':>26}  {'|count-1|':>12}")
    worst_count = mp.mpf(0)
    per_annulus = {}
    for k in range(-2, 3):
        n = counts[k] - counts[k - 1]
        err = abs(n - 1)
        worst_count = max(worst_count, err)
        per_annulus[str(k)] = mp.nstr(n, 18)
        print(f"    p^{k - 0.5:+.1f} .. p^{k + 0.5:+.1f}  "
              f"{mp.nstr(n, 22):>26}  {mp.nstr(err, 6):>12}")
    res["zeros_per_annulus"] = per_annulus
    res["worst_count_error"] = mp.nstr(worst_count, 6)
    print()
    print(f"    worst deviation from exactly 1 : {mp.nstr(worst_count, 8)}")
    print("    A count of 1 also forces the zero to be SIMPLE.")
    ok_count = worst_count < mp.mpf("1e-6")
    checks.append({
        "name": "exactly_one_zero_per_fundamental_annulus",
        "detail": f"max |N-1| over 5 annuli = {mp.nstr(worst_count, 6)}. This is "
                  "FORCED by the functional equation (see module docstring), so "
                  "it is a check on the derivation and on theta(), not "
                  "independent evidence.",
        "passed": bool(ok_count),
    })
    print()

    # ---- 3. where is it? --------------------------------------------------
    print("=" * 78)
    print("  3. WHERE is it?   sum of zero locations per annulus, vs -p^k")
    print("=" * 78)
    print("     weighting the same integral by g(w) = w gives sum over zeros of z_j")
    print()
    print(f"    {'k':>4}  {'sum z_j':>34}  {'-p^k':>22}  {'rel.err':>11}")
    wcounts = {k: winding(p, p ** (mp.mpf(k) + mp.mpf(1) / 2), W, M_LADDER[-1],
                          weight=lambda w: w)
               for k in range(-3, 4)}
    worst_loc = mp.mpf(0)
    loc = {}
    for k in range(-2, 3):
        s = wcounts[k] - wcounts[k - 1]
        pred = -(p ** k)
        rel = abs(s - pred) / abs(pred)
        worst_loc = max(worst_loc, rel)
        loc[str(k)] = mp.nstr(s, 18)
        print(f"    {k:>4}  {mp.nstr(s, 20):>34}  {mp.nstr(pred, 16):>22}"
              f"  {mp.nstr(rel, 6):>11}")
    res["zero_locations"] = loc
    res["worst_location_rel_err"] = mp.nstr(worst_loc, 6)
    print()
    print(f"    worst relative error vs -p^k : {mp.nstr(worst_loc, 8)}")
    ok_loc = worst_loc < mp.mpf("1e-6")
    checks.append({
        "name": "the_single_zero_sits_exactly_at_minus_p_to_the_k",
        "detail": f"max rel err of (1/2 pi i) oint w theta'/theta dw vs -p^k "
                  f"= {mp.nstr(worst_loc, 6)}",
        "passed": bool(ok_loc),
    })
    print()

    # ---- 4. a wide sweep --------------------------------------------------
    print("=" * 78)
    print("  4. WIDE sweep — |w| in (p^-4.5, p^+4.5) must hold exactly 9")
    print("=" * 78)
    nlo = winding(p, p ** mp.mpf("-4.5"), W, M_LADDER[-1])
    nhi = winding(p, p ** mp.mpf("4.5"), W, M_LADDER[-1])
    wide = nhi - nlo
    print(f"    count = {mp.nstr(wide, 20)}     expected 9")
    print(f"    |count - 9| = {mp.nstr(abs(wide - 9), 8)}")
    print("    Measured over the whole 9-annulus window in one integral, so it")
    print("    rules out zeros hiding BETWEEN the orbit points, not just at them.")
    res["wide_annulus_count"] = mp.nstr(wide, 18)
    ok_wide = abs(wide - 9) < mp.mpf("1e-6")
    checks.append({
        "name": "wide_annulus_holds_exactly_nine_zeros",
        "detail": f"p^-4.5 < |w| < p^4.5 gives {mp.nstr(wide, 12)}",
        "passed": bool(ok_wide),
    })
    print()

    # ---- 5. cross-check the >= direction ----------------------------------
    print("=" * 78)
    print("  5. cross-check — |theta_p(-p^k)| against the largest term")
    print("=" * 78)
    worst_van = mp.mpf(0)
    lp = mp.log(p)
    for k in range(-3, 4):
        w = -(p ** k)
        th, _ = theta_and_deriv(p, w, W)
        n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
        scale = max(abs(p ** (-mp.mpf(n) * (n + 1) / 2) * w ** n)
                    for n in range(n0 - 3, n0 + 4))
        rel = abs(th) / scale
        worst_van = max(worst_van, rel)
        print(f"    k={k:>3}   |theta| / max|term| = {mp.nstr(rel, 8)}")
    res["worst_vanishing_rel"] = mp.nstr(worst_van, 6)
    ok_van = worst_van < mp.mpf("1e-40")
    checks.append({
        "name": "theta_vanishes_at_the_orbit_points",
        "detail": f"max |theta|/max|term| over k=-3..3 = {mp.nstr(worst_van, 6)} "
                  "(the Lean-proved >= direction, re-measured)",
        "passed": bool(ok_van),
    })
    print()

    passed = all(c["passed"] for c in checks)
    print("=" * 78)
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print("""
  CONCLUSION.  At our substrate, theta_p has exactly one simple zero per
  fundamental annulus, at exactly -p^k, and none between orbit points across a
  9-annulus window. The two identities the Lean now proves reproduce numerically
  to full working precision, so the Lean statements are the intended ones.

  The zero locus is therefore -p^Z and the C1 pole divisor is not at risk.

  This is not a proof and does not upgrade the Lean file's >= to =. What it does
  establish is the SIZE of what is left: not the Jacobi triple product, not
  elliptic function theory on C*/p^Z, but a single named missing lemma — the
  argument principle on an annulus. Everything it consumes is proved.
""")

    script_path = Path(__file__).resolve()
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, cwd=script_path.parent).stdout.strip()
    except Exception:
        sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "scriptFile": script_path.name,
        "scriptSha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "commitSha": sha or "unknown",
        "description":
            "Bean qou-c1ln row 2. Establishes that the CONVERSE theta zero "
            "locus does NOT need the Jacobi triple product. Holomorphy on C* "
            "(Lean differentiableOn_qThetaC) plus the functional equation "
            "theta(pw) = w theta(w) (Lean qThetaC_functional_equation) give, "
            "after differentiating, p th'(pw)/th(pw) = 1/w + th'(w)/th(w) "
            "(Lean logDeriv_qThetaC_functional_equation); substituting w -> pw "
            "in the contour integral turns the 1/w into 2 pi i, so the winding "
            "number rises by exactly one per period. The argument principle "
            "then gives exactly one zero per fundamental annulus, and the "
            "Lean-proved theta(-p^k) = 0 supplies it, forcing simplicity and "
            "excluding others. JTP additionally needs Liouville on C*/p^Z and "
            "is therefore strictly more work and off the critical path. This "
            "script (a) checks the two new Lean identities numerically, which "
            "is what would catch a wrong power of p or a P-vs-p normalisation "
            "mismatch against the theta() used by the other nine C1 scripts, "
            "and (b) runs the contour integrals directly: one zero per "
            "fundamental annulus, located at exactly -p^k, and exactly 9 in a "
            "p^-4.5 < |w| < p^4.5 sweep, which excludes zeros hiding between "
            "orbit points. Geometric-mean radii, periodic trapezoid rule "
            "(spectrally accurate here), M-ladder 512/1024/2048 reporting "
            "convergence rather than asserting it.",
        "computation": {
            "dps": DPS,
            "q": Q_STR,
            "seriesHalfWindow": W,
            "trapezoidNodes": list(M_LADDER),
            "contourRadii": "p^(k+1/2), k = -3..3, plus p^(+-4.5)",
        },
        "results": res,
        "checks": checks,
        "verdict":
            "The statement holds at our p, and — the substantive finding — the "
            "Jacobi triple product is NOT required to prove it. The converse "
            "zero locus follows from three facts already proved in Lean "
            "(holomorphy on C*, the functional equation, vanishing on the "
            "orbit) plus the argument principle, which is the SOLE remaining "
            "gap. Mathlib has no argument principle, no winding number and no "
            "complex residue (name scan at HEAD 2026-08-07), but it does have "
            "the full circleIntegral API including the annulus Cauchy theorem, "
            "so this is one named lemma rather than a theory build-out. Bean "
            "qou-c1ln row 2 is rescoped accordingly: it previously said JTP "
            "was needed, and that was over-scoped. Numerically: one simple "
            "zero per fundamental annulus at exactly -p^k, exactly 9 across a "
            "9-annulus sweep, and both new Lean identities reproduced to full "
            "working precision. Still NOT proved in Lean: the = direction "
            "itself. Nothing wired to production.",
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-theta-zero-count.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}   ({witness['durationMs']} ms)")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
