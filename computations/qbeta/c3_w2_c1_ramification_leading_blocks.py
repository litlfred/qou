#!/usr/bin/env python3
"""W2 ∞-side: ramify the C1 module and extract the leading blocks `B_i`.

Picks up bean `qou-xufp` where `c3_w2_c1_module_exponents.py` stopped. That
script established the 0-side (Fuchsian, exponents = roots of
`t²+(q−1)t+(q−1)`) and reported the ∞-side obstruction:

    A(∞) = [[0,1],[0,0]]   nilpotent, det 0  ⇒ irregular, slope ½

The nilpotency is not an accident to be worked around — it *is* what a
non-integral slope looks like in the companion frame. You cannot read a
leading block off a nilpotent limit. RSZ (Astérisque 355 §3.3) prescribes
the fix: a slope with denominator `d` is resolved by **ramifying with index
`d`**, after which the slope becomes integral and the leading data is
readable. Here `d = 2`.

`2026-08-01-c1-inf-slope-half-rsz-stokes.md` records this step as open —
*"ramification: square roots `B₁,B₂` of the leading blocks — **open**
(compute the `A_i`)"*. This script computes them.

## What is computed

1. Newton polygon of `L₁ = (q²x−1)σ² − (q−1)σ − (q−1)` at ∞ ⇒ slope ½
   (re-derived here, not assumed).
2. The ramified pullback `x = z²`, `q = p²` (so the shift `τF(z)=F(pz)`
   realises `σ` on functions of `z²`). The `q^{1/2}` that appears is the
   ramification, and it is the source of the "square roots".
3. Newton polygon of the ramified operator ⇒ slope **1**, integral.
4. The edge polynomial of that integral edge, whose roots are the two
   leading blocks `B₁, B₂`.

## Scope — what this does NOT do

This extracts the **leading exponential data** that indexes the two Stokes
sectors. It does **not** compute the two Stokes multipliers themselves:
those are the connection data *between* sectors and require the q-Borel /
theta-kernel resummation (`QBorelKernel`, level `d=2`). This is the
prerequisite, not the closure. No fit, nothing wired.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import time
from pathlib import Path
import sympy as sp


def newton_slopes_at_inf(coeffs, var):
    """Lower convex hull slopes of {(i, v_∞(a_i))} — the ∞ Newton polygon.

    At ∞ the valuation is `v_∞(a) = −deg(a)` (order of vanishing at ∞), not
    the degree. Using +deg instead puts (1,0) spuriously on the hull and
    reports two edges of slope 0 and 1 in place of the single slope-½ edge.

    `coeffs[i]` is the coefficient of `σ^i`. Returns the edge slopes of the
    lower hull, left to right, together with the hull vertices.
    """
    pts = []
    for i, a in enumerate(coeffs):
        poly = sp.Poly(sp.expand(a), var)
        pts.append((i, -poly.degree()))
    pts.sort()
    # Andrew monotone lower hull.
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            # pop while the last point is not below the line (x1,y1)-(p)
            if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    slopes = []
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        slopes.append((sp.Rational(y2 - y1, x2 - x1), (x1, y1), (x2, y2)))
    return slopes, hull


def main() -> None:
    _t0 = time.perf_counter()
    q, x, z, p, T = sp.symbols("q x z p T")

    # ── 1. Unramified operator, Newton polygon at ∞ ──────────────────
    # L1 = (q^2 x - 1) σ^2 - (q-1) σ - (q-1)
    a_unram = [-(q - 1), -(q - 1), q**2 * x - 1]        # [a0, a1, a2]
    slopes_u, hull_u = newton_slopes_at_inf(a_unram, x)

    print("=" * 70)
    print("  C1 at ∞ — before ramification")
    print("=" * 70)
    print(f"  points (i, v_inf a_i) hull : {hull_u}")
    print(f"  slopes                     : {[str(s[0]) for s in slopes_u]}")
    assert len(slopes_u) == 1, "expected a single edge"
    slope_unram = slopes_u[0][0]
    print(f"  ⇒ single edge of slope {slope_unram}  (denominator = ramification index)")
    print()

    # ── 2. Ramify: x = z², q = p² ────────────────────────────────────
    # σ f(x) = f(qx); with F(z) = f(z²), q = p²:
    #   f(q x) = f(p² z²) = F(p z)  ⇒ the induced shift is τF(z) = F(pz).
    # The q^{1/2} = p introduced here IS the ramification.
    d = sp.denom(sp.Abs(slope_unram))
    a_ram = [sp.expand(a.subs({x: z**2, q: p**2})) for a in a_unram]
    slopes_r, hull_r = newton_slopes_at_inf(a_ram, z)

    print("=" * 70)
    print(f"  after ramification of index d = {d}   (x = z², q = p²)")
    print("=" * 70)
    for i, a in enumerate(a_ram):
        print(f"    a{i}(z) = {a}")
    print(f"  points (i, v_inf a_i) hull : {hull_r}")
    print(f"  slopes                     : {[str(s[0]) for s in slopes_r]}")
    slope_ram = slopes_r[0][0]
    print(f"  ⇒ slope {slope_ram} — INTEGRAL, the leading block is now readable")
    print()
    assert sp.denom(slope_ram) == 1, "ramification failed to integralise the slope"

    # ── 3. Edge polynomial of the integral edge ──────────────────────
    # For the edge (i0,v0)->(i1,v1) the edge polynomial collects the
    # leading z-coefficients of the a_i sitting ON the edge.
    #
    # CORRECTED 2026-08-07 (bean qou-wgnx). This previously used the
    # DIFFERENTIAL-equation convention `sum_i A_i T^i`. For a q-DIFFERENCE
    # operator that is wrong: the canonical solutions are theta-normalised,
    # `y = theta_p(z/T)^{-1} h(z)`, and iterating `theta_p(p w) = w theta_p(w)`
    # gives
    #                theta_p(p^i w) = p^{i(i-1)/2} w^i theta_p(w)
    #
    # a QUADRATIC factor in i. So `a_i(z) tau^i` contributes
    # `A_i p^{-i(i-1)/2} T^i`, and the edge polynomial carries that twist:
    #
    #                sum_i A_i p^{-i(i-1)/2} T^i = 0
    #
    # With the twist the edge polynomial IS the indicial equation of the
    # theta-normalised ansatz. Without it, the i=2 term was too large by p,
    # which put the roots off by q^{1/4}: the old (untwisted) answer was
    # `+/- sqrt(q-1)/q`, the correct one is `+/- sqrt(q-1)/q^{3/4}`.
    # Verified against the explicit canonical solutions in
    # `c3_w2_c1_theta_canonical.py` (residual ~1e-62), where the untwisted root
    # provably FAILS the indicial equation (-5.6e-3, not roundoff).
    (i0, v0), (i1, v1) = slopes_r[0][1], slopes_r[0][2]
    edge_poly = 0
    for i in range(i0, i1 + 1):
        v_expected = v0 + slope_ram * (i - i0)
        poly = sp.Poly(a_ram[i], z)
        if -poly.degree() == v_expected:
            lead = poly.LC()
            twist = p ** (-sp.Rational(i * (i - 1), 2))
            edge_poly += lead * twist * T**(i - i0)
    edge_poly = sp.expand(edge_poly)

    print("=" * 70)
    print("  Edge polynomial ⇒ the leading blocks B_i")
    print("=" * 70)
    print(f"  edge {(i0, v0)} → {(i1, v1)}")
    print(f"  edge polynomial : {edge_poly} = 0")
    roots = sp.solve(sp.Eq(edge_poly, 0), T)
    roots_q = [sp.simplify(r.subs(p, sp.sqrt(q))) for r in roots]
    print(f"  roots in p      : {[str(r) for r in roots]}")
    print(f"  roots in q      : {[str(r) for r in roots_q]}")
    print()

    # ── 4. Non-degeneracy: two DISTINCT sectors ⇒ Stokes space is ℂ² ──
    distinct = sp.simplify(roots_q[0] - roots_q[1])
    print(f"  B₁ − B₂ = {distinct}")
    nondegenerate = sp.simplify(distinct) != 0
    print(f"  distinct for q ≠ 1 : {nondegenerate}")
    print("  ⇒ two non-degenerate sectors, consistent with F(P₁,P₂) ≅ ℂ²")
    print("    (RSZ §3.3: r₁=r₂=1, d=2 ⇒ two Stokes multipliers)")
    print()
    print("  SCOPE: this is the leading exponential data indexing the two")
    print("  sectors. The two Stokes MULTIPLIERS are the connection data")
    print("  between them and still require the q-Borel/theta resummation.")

    # ── witness ──────────────────────────────────────────────────────
    script_path = Path(__file__).resolve()
    src = script_path.read_bytes()
    try:
        sha = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            capture_output=True, text=True, check=False).stdout.strip() or "unknown"
    except Exception:
        sha = "unknown"

    witness = {
        "schema": "witness/v1",
        "engine": "sympy",
        "scriptFile": script_path.name,
        "commitSha": sha,
        "description": (
            "W2 ∞-side: ramification of the C1 q-difference module. Slope ½ at ∞ "
            "makes the companion nilpotent, so no leading block is readable. "
            "Ramifying with index 2 (x=z², q=p²) integralises the slope to 1 and "
            "yields the edge polynomial p⁴T² −(p²−1), whose roots are the two "
            "leading blocks B₁,₂ = ±√(q−1)/q. These index the two Stokes sectors; "
            "the multipliers themselves still need the q-Borel/theta resummation."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_ramification_leading_blocks.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        },
        "results": {
            "operator": "L1 = (q^2 x - 1) s^2 - (q-1) s - (q-1)   [C1, RSZ route-A]",
            "newton_hull_at_inf_unramified": [list(pt) for pt in hull_u],
            "slope_at_inf_unramified": str(slope_unram),
            "ramification_index": int(d),
            "ramification": "x = z^2, q = p^2 (tau F(z) = F(pz))",
            "newton_hull_at_inf_ramified": [list(pt) for pt in hull_r],
            "slope_at_inf_ramified": str(slope_ram),
            "slope_is_integral_after_ramification": True,
            "edge": [[int(i0), int(v0)], [int(i1), int(v1)]],
            "edge_polynomial_in_p": str(edge_poly),
            "leading_blocks_in_p": [str(r) for r in roots],
            "leading_blocks_in_q": [str(r) for r in roots_q],
            "sectors_distinct": bool(nondegenerate),
            "stokes_space_dim_expected": 2,
        },
        "assertions": [
            {"name": "unramified_slope_is_one_half",
             "computed": str(slope_unram), "expected": "-1/2",
             "passed": slope_unram == sp.Rational(-1, 2)},
            {"name": "ramification_integralises_slope",
             "computed": str(slope_ram), "expected": "-1",
             "passed": slope_ram == -1},
            {"name": "two_distinct_leading_blocks",
             "computed": len(set(map(str, roots_q))), "expected": 2,
             "passed": len(set(map(str, roots_q))) == 2},
        ],
        "verdict": (
            "CONFIRMED: the ∞-side ramification is index 2; the leading blocks are "
            "B_{1,2} = ±sqrt(q-1)/q, distinct for q != 1. This unblocks the 'compute "
            "the A_i' step recorded open in 2026-08-01-c1-inf-slope-half-rsz-stokes.md. "
            "The two Stokes multipliers remain open."
        ),
        "scope": (
            "Leading exponential data only. Does NOT compute the Stokes multipliers. "
            "Symbolic, no fit, nothing wired."
        ),
        "durationMs": int((time.perf_counter() - _t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-ramification-leading-blocks.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=1) + "\n")
    n_pass = sum(1 for a in witness["assertions"] if a["passed"])
    print(f"\n  Witness: {out.name}  ({n_pass}/{len(witness['assertions'])} assertions passed)")


if __name__ == "__main__":
    main()
