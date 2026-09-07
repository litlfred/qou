#!/usr/bin/env python3
"""The framework's abelian connection supplies no twist — measured (bean qou-d0qq, plan step 2).

Candidate C3 of the framework-side plan: the abelianised Cartan connection A⁰ = X dz = λ_SW on the
colour cubic {P(X, z) = 0} (mi-sw-abelianisation-cartan; ColorSpectralCubicGeometry) could be the
rank-one twist L = exp(∮ A⁰) that turns the untwisted (finite-order) Gauss–Manin monodromy of the
root map into a monodromy with real eigenvalue ratio −q₀².  It cannot, and the reason is holomorphy:

  * PUSH-DOWN.  The push-down of A⁰ to the base ℂ∖Δ is the symmetric function Σ_j X_j(z) dz =
    p₁(z) dz = −(z + 1) dz (Vieta), a polynomial 1-form, hence exact: its holonomy around every
    lasso is 1.  Checked symbolically.
  * PER SHEET.  Each lasso around a simple branch point z_k exchanges two sheets and fixes the
    third.  Around the small circle, the fixed sheet X_f(z) is single-valued and holomorphic inside,
    so ∮ X_f dz = 0; the two exchanged sheets satisfy ∮ (X_a + X_b) dz = ∮ (p₁ − X_f) dz = 0.  The
    loop on the CURVE that closes (the lasso traversed twice) has radial parts cancelling sheet by
    sheet, so its integral is exactly ∮_circle (X_a + X_b) dz = 0: the holonomy of exp(∮ A⁰) around
    the ramification point is 1 on every sheet.  Checked numerically at 50 dps by the trapezoid rule
    on the circle (geometric convergence for a periodic analytic integrand), with N doubled to show
    convergence, for all six branch points.

So the only rank-one system the framework's own geometry produces on ℂ∖Δ is trivial, and the
deformation 1 ↦ q₀ must enter as an EXTERNAL twist exponent (C3′: e^{2πiμ} = −q₀²) — which is the
KZ level in geometric clothing.  Scope (b): the invariant is holomorphy + Vieta.  Nothing here reads
q₀; anchor independent.  No float64: mpmath 50 dps for the circle integrals, sympy for Vieta.

Reuses P, roots_at, lasso geometry from colour_cubic_branch_monodromy_probe.py (imported, not
re-typed); branch points from the committed witness colour-cubic-branch-monodromy.witness.json.

Run:  PYTHONPATH=computations python3 -u computations/probes/colour_cubic_abelian_twist_holonomy_probe.py \
        2>&1 | tee /tmp/abelian_twist.log
"""
from __future__ import annotations

import json
import os
import sys
import time

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from colour_cubic_branch_monodromy_probe import P, X, z, roots_at  # noqa: E402

mp.mp.dps = 50
T0 = time.monotonic()
HERE = os.path.dirname(os.path.abspath(__file__))
BRANCH_WITNESS = os.path.join(HERE, "colour-cubic-branch-monodromy.witness.json")


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:6.1f}s] {msg}", flush=True)


def branch_points():
    """The six roots of the discriminant, from the committed witness if present, else recomputed."""
    if os.path.exists(BRANCH_WITNESS):
        w = json.load(open(BRANCH_WITNESS))
        blob = w.get("data", w)
        for key in ("branch_points", "branch_points_z", "z_k"):
            if key in blob:
                vals = blob[key]
                out = []
                for v in (vals.values() if isinstance(vals, dict) else vals):
                    s = v if isinstance(v, str) else v.get("z", v.get("value"))
                    out.append(mp.mpc(*[mp.mpf(t) for t in s.strip("()").split(",")]) if isinstance(s, str) and "," in s else mp.mpmathify(s))
                if len(out) == 6:
                    return out, "witness"
    D = sp.discriminant(P, X)
    coeffs = [sp.Rational(c) for c in sp.Poly(D, z).all_coeffs()]
    return list(mp.polyroots([mp.mpf(str(c)) for c in coeffs], maxsteps=400, extraprec=200)), "recomputed"


def circle_integrals(zk, r, N):
    """Trapezoid rule for ∮ X_j dz on |z − z_k| = r, tracking the three sheets by continuity.
    Returns the three sheet integrals (in the order of the starting root triple), the
    permutation induced by the loop, and the minimum root separation met."""
    pts = [zk + r * mp.exp(2j * mp.pi * mp.mpf(i) / N) for i in range(N + 1)]
    roots = list(roots_at(pts[0]))
    start = list(roots)
    integrals = [mp.mpc(0)] * 3
    min_sep = mp.inf
    prev_pts = pts[0]
    prev_roots = roots
    for i in range(1, N + 1):
        zi = pts[i]
        cand = list(roots_at(zi))
        new = []
        for pr in prev_roots:
            j = min(range(3), key=lambda t: abs(cand[t] - pr))
            new.append(cand[j])
        seps = [abs(cand[a] - cand[b]) for a in range(3) for b in range(a + 1, 3)]
        min_sep = min(min_sep, min(seps))
        dz = zi - prev_pts
        for s in range(3):
            integrals[s] += (prev_roots[s] + new[s]) / 2 * dz
        prev_roots, prev_pts = new, zi
    perm = [min(range(3), key=lambda t: abs(start[t] - prev_roots[s])) for s in range(3)]
    return integrals, perm, min_sep


def main() -> int:
    print("=" * 78)
    print(" abelian twist holonomy of the colour cubic — zero on every sheet (qou-d0qq)")
    print("=" * 78)
    checks = []

    # ---- push-down: Vieta ⇒ polynomial ⇒ exact -----------------------------------------
    coeffs = sp.Poly(P, X).all_coeffs()
    p1 = sp.simplify(-coeffs[1] / coeffs[0])
    checks.append(("push-down sum_j X_j = -(z+1) (Vieta), a polynomial in z", sp.simplify(p1 + (z + 1)) == 0))
    checks.append(("polynomial 1-form p1(z) dz is exact: primitive -(z^2/2 + z)", sp.simplify(sp.diff(-(z ** 2 / 2 + z), z) - p1) == 0))
    log(f"push-down of A⁰: Σ_j X_j dz = ({p1}) dz — exact")

    # ---- per sheet: circle integrals at every branch point ------------------------------
    bps, src = branch_points()
    log(f"six branch points ({src}); |D| roots: {[mp.nstr(b, 8) for b in bps]}")
    checks.append(("six branch points obtained", len(bps) == 6))
    r = mp.mpf("0.11150636379232188547") / 2   # half the lasso radius of the branch probe: strictly inside
    per_point = []
    all_fixed_zero = all_pair_zero = all_closed_zero = all_converged = True
    for k, zk in enumerate(sorted(bps, key=lambda c: (mp.re(c), mp.im(c)))):
        I1, perm1, sep1 = circle_integrals(zk, r, 800)
        I2, perm2, sep2 = circle_integrals(zk, r, 1600)
        fixed = [s for s in range(3) if perm2[s] == s]
        swapped = [s for s in range(3) if perm2[s] != s]
        is_transposition = len(fixed) == 1 and len(swapped) == 2
        f = fixed[0] if is_transposition else None
        fixed_int = abs(I2[f]) if is_transposition else mp.inf
        pair_int = abs(I2[swapped[0]] + I2[swapped[1]]) if is_transposition else mp.inf
        total = abs(sum(I2))
        # convergence is tested on the two meaningful quantities — the fixed sheet's integral and the
        # exchanged pair's sum — which are periodic analytic data on the circle; an individual exchanged
        # sheet is NOT periodic (it swaps across the loop) and its separate trapezoid sum converges only
        # algebraically, which is irrelevant to the holonomy
        if is_transposition:
            fixed1 = abs(I1[f]); pair1 = abs(I1[swapped[0]] + I1[swapped[1]])
            conv = max(abs(abs(I2[f]) - fixed1), abs(abs(I2[swapped[0]] + I2[swapped[1]]) - pair1))
        else:
            conv = mp.inf
        # the closed loop on the curve = lasso twice; radial parts cancel sheet by sheet, so
        # its integral on sheet s is ∮_circle (X_s + X_{τ s}) dz = pair sum for the exchanged
        # sheets and 2∮ X_f dz for the fixed one (both zero)
        closed_loop = max(pair_int, 2 * fixed_int) if is_transposition else mp.inf
        tol = mp.mpf(10) ** -30
        all_fixed_zero &= fixed_int < tol
        all_pair_zero &= pair_int < tol
        all_closed_zero &= closed_loop < tol
        all_converged &= conv < tol
        per_point.append({"z_k": mp.nstr(zk, 30), "radius": mp.nstr(r, 20), "permutation": perm2,
                          "is_transposition": is_transposition, "fixed_sheet_integral_abs": mp.nstr(fixed_int, 10),
                          "exchanged_pair_integral_abs": mp.nstr(pair_int, 10), "total_abs": mp.nstr(total, 10),
                          "closed_loop_on_curve_abs": mp.nstr(closed_loop, 10),
                          "trapezoid_N800_vs_N1600_fixed_and_pair": mp.nstr(conv, 10), "min_root_separation": mp.nstr(min(sep1, sep2), 10),
                          "holonomy_exp_closed_loop_minus_1_abs": mp.nstr(abs(mp.exp(closed_loop) - 1) if closed_loop < 1 else mp.inf, 10)})
        log(f"z_{k} = {mp.nstr(zk, 10)}: perm {perm2}, |∮X_fixed| = {mp.nstr(fixed_int, 4)}, |∮(X_a+X_b)| = {mp.nstr(pair_int, 4)}, "
            f"|Σ| = {mp.nstr(total, 4)}, N-convergence {mp.nstr(conv, 4)}")
    checks.append(("every small circle induces a transposition (matches the branch probe)", all(p["is_transposition"] for p in per_point)))
    checks.append(("fixed-sheet circle integral vanishes at every branch point (< 1e-30, 50 dps)", all_fixed_zero))
    checks.append(("exchanged-pair circle integral vanishes at every branch point (< 1e-30)", all_pair_zero))
    checks.append(("closed loop on the curve (lasso twice): integral < 1e-30 on every sheet ⇒ holonomy exp(∮A⁰) = 1", all_closed_zero))
    checks.append(("trapezoid rule converged on the fixed-sheet and pair integrals (N = 800 vs 1600 agree to 1e-30)", all_converged))

    ok = 0
    print()
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    wb = WitnessBuilder("colour-cubic-abelian-twist-holonomy", engine="mpmath+sympy", _script_path=__file__)
    wb.set_description(
        "qou-d0qq, framework-side plan step 2 (candidate C3): the abelianised Cartan connection A⁰ = X dz "
        "on the colour cubic supplies NO twist on ℂ∖Δ. Push-down Σ_j X_j dz = −(z+1) dz is exact (Vieta); "
        "around every branch point the fixed sheet's circle integral and the exchanged pair's sum both "
        "vanish to 1e-30 at 50 dps (trapezoid, geometric convergence, N doubled), so the closed loop on the "
        "curve (lasso twice) has zero integral on every sheet and holonomy exp(∮A⁰) = 1. Scope (b) — "
        "invariant: holomorphy of the fixed sheet inside the circle + Vieta. The deformation 1 ↦ q₀ "
        "therefore cannot come from the framework's own abelian connection; it enters as an external "
        "twist exponent (C3′), i.e. the KZ level. Nothing reads q₀; anchor independent.")
    wb.set_content_block("conj:hecke-monodromy-step-two")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0", expected="1",
                         tolerance="0.5", source="sympy exact / mpmath 50 dps trapezoid on the circle")
    wb.add_parameter("branch_points_source", src)
    wb.add_parameter("circle_radius", mp.nstr(r, 25))
    wb.add_parameter("q0Anchor_reason", "independent: no q0 is read; the cubic, its branch points and A⁰ are q-free")
    wb.add_data("push_down", {"p1": str(p1), "primitive": "-(z^2/2 + z)"})
    wb.add_data("per_branch_point", per_point)
    wb.add_data("verdict", (
        "NEGATIVE, scope (b): the framework's abelian connection A⁰ = λ_SW has trivial holonomy around every "
        "ramification point and a trivial push-down, so it is not the twist; candidate C3 is dead and C3′ "
        "(external exponent μ with e^{2πiμ} = −q₀²) is the survivor. Combined with UntwistedMonodromyPrune "
        "(finite-order eigenvalues are never > 1), no framework geometry in the corpus produces the "
        "deformation 1 ↦ q₀ — it is an input."))
    wb.add_caveat("The prolongation jets λ_SW^{(n)} ~ (z − z_k)^{1/2 − n} carry square-root monodromy −1 (NaStokesKeystone.lean); a root of unity, not a real q₀ > 1 — covered by UntwistedMonodromyPrune, not re-measured here.")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(HERE, '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
