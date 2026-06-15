#!/usr/bin/env python3
"""qbeta_reeb_sinh_fmap_brane_tower_probe.py
=============================================

Test the **`1/u^k` f-map** between a fibre-level Reeb `sinh(ℓη)` q-weight
and the observable c_k ladder rung — the structural route to the
data-blocked q-difference recurrence (PR #1880 cont. 12) and the
brane-tower level-selection question GAP-A-3.

## Hypothesis (this probe is its falsifier)

The companion probe `qbeta_reeb_sinh_parity_probe.py` (PR #1887)
established that:
  (a) `sinh(kη)` is bar-ODD — the unique Reeb component that can source
      the first bar-antisymmetric coefficient c_3 (Lean-proved
      `QBetaReebSinhParity`);
  (b) the observable slope ratio `(dc_3/dη)/(d sinh(kη)/dη)` matches the
      ladder factor `1/u^3` — so a fibre-level `sinh(ℓη)` would need an
      amplification of `1/u^k` to land on the observable c_k.

So the structural claim under test is:

    c_k(q) = sinh(ℓ_k · η(q)) / f_k(η, u)             (★)

with `f_k` the candidate **f-map** (the 1/u^k amplification) and `ℓ_k` an
integer **brane-tower level** (GAP-A-3 identifies `ℓ_k = ℓ(K, q_0)`).
The pruning test is cross-anchor:

    Solve (★) for ℓ at q_proton → ℓ_p
    Solve (★) for ℓ at q_muon   → ℓ_m
    PASS  ⟺  ℓ_p ≈ ℓ_m  AND  the common value is a natural integer.

A pass identifies ℓ_3 + the f-map; a fail quantifies the mismatch and
either pins ℓ_3 to a non-integer (refuting "ℓ = brane-tower level") or
splits the f-map candidates.

## Candidates for f_k (k=3)

All bar-EVEN, closed-form in {η, h=2sinh η, b, u}, no fits:

    1. f = u^3                   — pure ladder amplification (the audit
                                   "1/u^k" framing)
    2. f = 2 cosh(η) · u^3       — mirrors the P_m(h) denominator
                                   (cheat-sheet §3): bar-even cosh times
                                   ladder
    3. f = (2 sinh η)^3 = h^3    — pure bar-odd^k (denominator is the
                                   k-th power of h = q − q⁻¹); bar-EVEN
                                   for even k, bar-ODD for odd k — so
                                   THIS one is bar-odd at k=3, meaning
                                   sinh(ℓη)/h^3 is bar-EVEN, would
                                   require a bar-EVEN c_3 (refuted —
                                   but we run it as a parity control)
    4. f = b^3 · u^0 · ...       — substrate-only b^k (control)

Honest expectation: a PASS would be a major positive — the first
cross-anchor structural identification of c_3 since the bracket closed.
A FAIL is also informative: the SIZE of the (ℓ_p − ℓ_m) mismatch
quantifies how far the brane-tower-level hypothesis sits from the
observable swing.

## No-fit discipline

Every f-map candidate is a closed-form expression in the substrate
scalars. The solve is an inverse-sinh, not a fit; integer-check on ℓ
is the pruning gate. Cross-anchor agreement is necessary, not
sufficient, exactly as in PR #1831 / #1880.

## References
- Lean parity: `QBetaReebSinhParity` (PR #1887)
- f-map / amplification finding: PR #1887 companion probe
- c_3 cross-anchor target: `qbeta_utils.c3_target_at` (PR #1831)
- Brane-tower level (GAP-A-3): `docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md`
- Data-blocked recurrence (the structural route): PR #1880
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, asinh, sinh, cosh, log, fabs, nint  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402


def solve_ell(c_target: mpf, f_denom: mpf, eta: mpf) -> mpf:
    """Solve  sinh(ℓ·η) = c_target · f_denom  for ℓ.

    Returns ℓ = asinh(c_target · f_denom) / η.
    """
    return asinh(c_target * f_denom) / eta


def f_candidates(eta: mpf, h: mpf, b: mpf, u: mpf) -> dict[str, mpf]:
    """Closed-form f-map denominator candidates evaluated at one anchor.

    f_k(η, h, b, u)  for  c_k = sinh(ℓ·η) / f_k.
    """
    return {
        "u^3":                  u ** 3,
        "2·cosh(η) · u^3":      2 * cosh(eta) * u ** 3,
        "h^3 = (2·sinh η)^3":   h ** 3,
        "b^3 · u^3":            b ** 3 * u ** 3,
        "cosh(η)·h·u^2":        cosh(eta) * h * u ** 2,
        "u^3 / (1+η²)":         u ** 3 / (1 + eta ** 2),
    }


# Tolerances for the cross-anchor pass / near-integer gate / round-trip.
TOL_ELL_DIFF = mpf("1e-3")      # |ℓ_p − ℓ_m| within 1e-3
TOL_INT_DIST = mpf("0.05")      # within 0.05 of the nearest integer
INTEGER_ABS_MAX = 200           # plausible brane-tower levels
TOL_ROUNDTRIP_PPM = mpf("1e4")  # rounded ℓ must reproduce c_3 within 1% (10⁴ ppm)
                                # — kills the trivial ℓ=0 solution from
                                # the small-argument asinh.


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)
    eta_p = log(qp)
    eta_m = log(qm)
    sub_p = substrate_ladder_quantities(qp)
    sub_m = substrate_ladder_quantities(qm)

    c3_p = c3_target_at(qp, q_codata, me)
    c3_m = c3_target_at(qm, q_codata, me)

    print("=" * 78)
    print(" Q_β c_3 Reeb-sinh f-map probe — cross-anchor ℓ_3 brane-tower test")
    print("=" * 78)
    print(f"  η(q_p) = {float(eta_p):.10f}   η(q_m) = {float(eta_m):.10f}")
    print(f"  u(q_p) = {float(sub_p['u']):.6e}   u(q_m) = {float(sub_m['u']):.6e}")
    print(f"  c_3 target (proton) = {fmt(c3_p)[:18]}")
    print(f"  c_3 target (muon)   = {fmt(c3_m)[:18]}")
    print(f"  cross-anchor swing  = {fmt(fabs(c3_p - c3_m))[:14]}")
    print()
    print(f"  test: c_3 = sinh(ℓ·η) / f  with ℓ integer at BOTH anchors")
    print(f"  pass gate: |ℓ_p − ℓ_m| < {float(TOL_ELL_DIFF)},  "
          f"|ℓ − round(ℓ)| < {float(TOL_INT_DIST)},  |ℓ| ≤ {INTEGER_ABS_MAX},")
    print(f"  AND  the rounded integer round-trips to c_3 within {float(TOL_ROUNDTRIP_PPM)} ppm.")
    print(f"  (Round-trip guard kills the trivial ℓ=0 solution, which gives c_3=0 ≠ −2.07.)")
    print()

    fp = f_candidates(eta_p, sub_p["h"], sub_p["b"], sub_p["u"])
    fm = f_candidates(eta_m, sub_m["h"], sub_m["b"], sub_m["u"])

    print(f"  {'f-map candidate':<28}{'ℓ_p':>12}{'ℓ_m':>12}"
          f"{'|ℓ_p−ℓ_m|':>14}{'nearest':>8}"
          f"{'round-trip ppm (p)':>22}  verdict")
    print(f"  {'-'*28}{'-'*12}{'-'*12}{'-'*14}{'-'*8}{'-'*22}  {'-'*16}")

    results = []
    closures = []
    for name in fp.keys():
        try:
            ell_p = solve_ell(c3_p, fp[name], eta_p)
            ell_m = solve_ell(c3_m, fm[name], eta_m)
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            print(f"  {name:<28}  ERROR: {e}")
            continue
        diff = fabs(ell_p - ell_m)
        nearest = int(nint(ell_p))          # nearest integer in mp domain (full dps)
        ell_p_f = float(ell_p)              # for display only
        int_dist = fabs(ell_p - mpf(nearest))
        in_range = abs(nearest) <= INTEGER_ABS_MAX
        cross_ok = diff < TOL_ELL_DIFF
        int_ok = int_dist < TOL_INT_DIST and in_range

        # Round-trip guard: substitute the rounded integer back into the
        # f-map and check it reproduces c_3 within tolerance.  This kills
        # the trivial ℓ=0 solution (gives sinh(0)=0 ⇒ c_3=0 ≠ -2.07).
        c3_recovered_p = sinh(mpf(nearest) * eta_p) / fp[name]
        rt_err_ppm_mpf = fabs(c3_recovered_p - c3_p) / fabs(c3_p) * mpf("1e6")
        rt_ok = rt_err_ppm_mpf < TOL_ROUNDTRIP_PPM
        rt_err_ppm_p = float(rt_err_ppm_mpf)   # display / serialize only
        closure = cross_ok and int_ok and rt_ok

        # Continuous-ℓ cross-anchor check: even if ℓ is not a small
        # integer, the GAP-A-3 brane-tower hypothesis (in its weaker
        # form: ℓ is anchor-independent, possibly rational) demands
        # ℓ(q_p) = ℓ(q_m). Quantify the RELATIVE mismatch (a real
        # continuous-ℓ closure would give |Δℓ|/|ℓ| ≪ swing_c3/|c_3|).
        rel_diff = float(diff / fabs(ell_p)) if fabs(ell_p) > mpf("1e-30") else float("inf")

        verdict = (
            f"CLOSURE ℓ={nearest}" if closure
            else "rt-fail (trivial)" if cross_ok and int_ok and not rt_ok
            else "non-int" if cross_ok and not int_ok
            else "cross-fail"
        )
        print(f"  {name:<28}{ell_p_f:>12.6f}{float(ell_m):>12.6f}"
              f"{float(diff):>14.2e}{nearest:>8d}"
              f"{rt_err_ppm_p:>22.2e}  {verdict}")
        results.append({
            "f_candidate": name,
            "ell_proton": fmt(ell_p),
            "ell_muon": fmt(ell_m),
            "ell_diff_abs": float(diff),
            "ell_diff_rel": rel_diff,
            "nearest_int": nearest,
            "int_distance": float(int_dist),
            "roundtrip_ppm_proton": rt_err_ppm_p,
            "cross_anchor_match": cross_ok,
            "integer_match": int_ok,
            "roundtrip_match": rt_ok,
            "closure": closure,
        })
        if closure:
            closures.append((name, nearest))

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if closures:
        print(f"  POSITIVE — {len(closures)} f-map candidate(s) reproduce c_3 at both")
        print(f"  anchors with the SAME integer ℓ_3 (brane-tower level):")
        for n, ell in closures:
            print(f"    • {n}:  ℓ_3 = {ell}")
        verdict = "POSITIVE_BRANE_TOWER_LEVEL_IDENTIFIED"
    else:
        # Diagnostic: of the 6 candidates, which ones pass cross-anchor at all?
        cross_only = [r for r in results if r["cross_anchor_match"]]
        print(f"  NEGATIVE — no f-map candidate yields the SAME integer ℓ_3 at both")
        print(f"  anchors within tolerance. {len(cross_only)} pass cross-anchor (ℓ_p ≈ ℓ_m)")
        print(f"  but none lands on an integer.")
        print()
        print(f"  This refutes the strict 'ℓ_k = natural integer brane-tower level'")
        print(f"  hypothesis for k=3 across the six f-map candidates here. Either ℓ_3")
        print(f"  is NOT a small integer (the GAP-A-3 framing needs sharpening — e.g.")
        print(f"  ℓ_k might be a rational with anchor-dependent normalisation), or the")
        print(f"  f-map family above is too narrow (extends to log(u)-factor variants,")
        print(f"  Bessel-style profiles, or multi-η weighted sinh sums).")
        if cross_only:
            best = min(cross_only, key=lambda r: r["int_distance"])
            print()
            print(f"  Closest-to-integer cross-anchor passer:")
            print(f"    {best['f_candidate']}:  ℓ_p ≈ {best['ell_proton'][:12]},  "
                  f"nearest = {best['nearest_int']},  "
                  f"distance = {best['int_distance']:.4f}")
            print()
            print(f"  Continuous-ℓ structural reading (drop integer constraint):")
            print(f"  for each candidate, |Δℓ|/|ℓ| is the relative cross-anchor mismatch;")
            print(f"  swing_c3 / |c_3| = {float(fabs(c3_p - c3_m) / fabs(c3_p)):.4f} is the")
            print(f"  reference scale.  A genuine fibre-level ℓ (anchor-independent)")
            print(f"  would have |Δℓ|/|ℓ| ≪ this; values ≳ this mean the f-map family")
            print(f"  cannot absorb the cross-anchor swing into a single ℓ.")
            for r in sorted(cross_only, key=lambda r: r["ell_diff_rel"])[:3]:
                print(f"    {r['f_candidate']:<28}  |Δℓ|/|ℓ| = {r['ell_diff_rel']:.4e}")
        verdict = "NEGATIVE_NO_INTEGER_BRANE_TOWER_LEVEL"

    # Witness
    wb = WitnessBuilder(
        "qbeta-reeb-sinh-fmap-brane-tower-probe", engine="mpmath",
    )
    wb.set_description(
        "Test the 1/u^k f-map between a fibre-level Reeb sinh(ℓη) "
        "q-weight and the observable Q_β c_k ladder rung — the "
        "structural route the data-blocked recurrence axis (#1880) "
        "leaves open, sharpened via the Reeb-sinh parity lead (#1887). "
        "For each closed-form f-map candidate, solve c_3 = sinh(ℓ·η)/f "
        "at both anchors and ask: is ℓ_3 the SAME natural integer at "
        "q_proton and q_muon (= brane-tower level, GAP-A-3)? PASS would "
        "be the first cross-anchor structural identification of c_3; "
        "FAIL pins down whether ℓ_3 is non-integer or the f-map family "
        "needs to extend. No fits; closed-form denominators only."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("eta_proton", fmt(eta_p))
    wb.add_data("eta_muon", fmt(eta_m))
    wb.add_data("u_proton", fmt(sub_p["u"]))
    wb.add_data("u_muon", fmt(sub_m["u"]))
    wb.add_data("c3_target_proton", fmt(c3_p))
    wb.add_data("c3_target_muon", fmt(c3_m))
    wb.add_data("n_candidates", len(results))
    wb.add_data("n_closures", len(closures))
    wb.add_data("verdict", verdict)
    wb.add_data("candidates", results)
    wb.add_data("interpretation", (
        "A POSITIVE would identify ℓ_3 (the GAP-A-3 brane-tower level) "
        "and the f-map simultaneously. A NEGATIVE (no integer ℓ_3 with "
        "cross-anchor agreement under these six closed-form f-map "
        "candidates) sharpens the open structural question: either the "
        "brane-tower index is not a small integer (rational? "
        "anchor-dependent?) or the f-map family must extend beyond "
        "u^k, h^k, and the cosh/u/h products tested here."
    ))
    # Invariants
    wb.add_assertion(
        "cross_anchor_c3_swing_resolvable",
        computed=1.0 if fabs(c3_p - c3_m) > mpf("1e-3") else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "ell_solver_returns_finite_for_at_least_one_candidate",
        computed=1.0 if len(results) >= 1 else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-reeb-sinh-fmap-brane-tower-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
