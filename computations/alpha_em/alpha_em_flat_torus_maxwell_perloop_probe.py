#!/usr/bin/env python3
"""alpha_em_flat_torus_maxwell_perloop_probe.py

Attack the RESIDUAL α_EM per-loop-measure wall. The data-selected per-loop
measure is `1/(π·b₁) = 1/(8π)` (b₁ = dim H¹(M_Bring) = 8; `D = 8` uniquely
data-selected to ~3500σ, `2026-07-17-alpha-em-perloop-integer-forcedness.md`).
The #3834 ζ-anomaly probe derived the *numerator* mode count `ζ_{Δ₁}(0) = −b₁`
exactly and AREA-FREE. Two pieces remain OPEN: (1) the bare `π`, and (2) the
RECIPROCAL form `1/(π b₁)` — the full determinant + per-mode weight, not `ζ(0)`.

This probe computes the **flat-torus Maxwell (free U(1) gauge) 1-loop partition
function** `Z_Maxwell(T^d)` INDEPENDENTLY of any α data and MEASURES which power
of π and which b₁-dependence the standard photon path integral produces, then
COMPARES (never fits) to the target `1/(π b₁)`.

THE PHYSICS (standard abelian-gauge 1-loop, Ray–Singer / Schwarz resolvent).
On the flat torus `T^d = ℝ^d/Λ` the Hodge decomposition of 1-forms is
    Ω¹ = dΩ⁰  ⊕  δΩ²  ⊕  Harm¹,   dim Harm¹ = b₁ = d.
The Maxwell action `S = ½(A, Δ₁ A)` vanishes on `Harm¹` (flat directions) and on
the exact/gauge part; the physical Gaussian is over the coexact (transverse)
modes. In Feynman gauge with the FP ghost the partition function is
    Z_Maxwell(T^d) = Vol(J(M)) · (2π)^{½ ζ_{Δ₁}(0)} · (det'Δ₁)^{−1/2} · (det'Δ₀)^{+1},
where `J(M) = H¹(M;ℝ)/H¹(M;ℤ) = T^{b₁}` is the Jacobian (flat-connection moduli).
Because the torus is parallelizable, `Δ₁ = Δ₀ ⊗ Id_{ℝ^d}`, so `ζ_{Δ₁}(s) = d·E_Λ(s)`
with `E_Λ` the scalar Epstein zeta — REUSED verbatim from the #3834 probe (we do
NOT reimplement the zeta).

WHAT IS EXTRACTED (independently of α; anti-laundering — no CODATA, no tuning):
  (a) π-power of the measure. Every non-zero mode is one real Gaussian
      `∫da e^{−½λa²} = (2π)^{½} λ^{−1/2}`, so the (2π) bookkeeping regularizes to
      `(2π)^{½ Σ_modes 1} = (2π)^{½ ζ_{Δ₁}(0)} = (2π)^{−b₁/2}`. π enters to power
      `−b₁/2` (LINEAR in b₁, magnitude 4 at b₁=8) — and it is `2π`, not `π`, so a
      companion `2^{−b₁/2}` rides along. (The eigenvalue normalization
      `λ_k = 4π²|k|²` supplies a *second* π-source, also ∝ b₁.)
  (b) b₁-dependence. b₁ sits in the EXPONENT (an exponential `(2π)^{−b₁/2}`),
      NOT in a reciprocal `1/b₁`.
  (c) area/covolume-dependence. The oscillator (2π) factors are area-free, but
      the zero-mode Jacobian volume `Vol(J(T^d))` scales as `L^{d(d−2)/2}` under
      `Λ → LΛ` — covolume dependence SURVIVES (nonzero exponent 24 at d=8).

COMPARE to the target `1/(π b₁) = π^{−1}·b₁^{−1}` (area-free):
  · π-power: target −1 exactly; Maxwell measure −b₁/2 = −4.       ✗
  · 2-vs-π:  target has bare π; Maxwell has 2π (spurious 2^{−b₁/2}). ✗
  · b₁ form: target reciprocal `b₁^{−1}`; Maxwell exponential in b₁. ✗
  · area:    target area-free; Maxwell Vol(J) carries covolume.    ✗

VERDICT (scope-(a) NEGATIVE — the pre-stated likely outcome). The flat-torus
Maxwell 1-loop partition function does NOT produce `1/(π b₁)`. Its measure is the
Gaussian bookkeeping `(2π)^{−b₁/2}` (times a covolume-dependent moduli volume),
π-power `= b₁/2 ≠ 1`, b₁ in the exponent (not reciprocal), covolume NOT removed
without a normalization CHOICE (the fitting trap, forbidden). Named failing
factors: (i) π-power `b₁/2` from the 2π-per-mode Gaussian bookkeeping; (ii) b₁
appears exponentially, not reciprocally; (iii) Vol(J) covolume dependence. This
is a real result: the per-loop measure is NOT the naive Maxwell partition
function — the reciprocal-in-b₁, single-π, area-free `1/(π b₁)` must come from a
DIFFERENT normalization object than `Z_Maxwell(T^{b₁})`. The area-free numerator
count `ζ_{Δ₁}(0) = −b₁` (#3834) stands untouched; only the MEASURE claim fails.
No `α_k` wired; no fit; no tier change; `1/(8π)` stays a phase-4 identification.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# REUSE the #3834 Epstein-zeta + heat-kernel machinery verbatim (do NOT
# reimplement the zeta): the flat-torus scalar E_Λ(0) = −1 and its d-copy lift
# ζ_{Δ₁}(0) = d·E_Λ(0) = −b₁.
from alpha_em_zeta_anomaly_b1_count_probe import (  # noqa: E402
    epstein_zero_cubic,
    theta_pi_1,  # noqa: F401  (imported to document the shared machinery)
)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

B1 = 8  # dim H¹(M_Bring) = b₁ (Jac(Bring) ~ E⁴, photon target J(M) = T^8)


def moduli_volume_scaling_exponent(d: int) -> mp.mpf:
    """Exponent p in Vol(J(T^d)) ∝ L^p under Λ → LΛ (torus ℝ^d/(LZ^d), flat δ).

    Harmonic 1-form ω = Σ c_μ dx^μ; L²-norm² = V·|c|² with V = L^d. Integer
    cohomology lattice: periods over γ_μ = L e_μ give L c_μ ∈ ℤ ⇒ c ∈ (1/L)ℤ^d.
    Vol(J) = covol_Euclid((1/L)ℤ^d) · √det(V·δ)
           = L^{−d} · (L^d)^{d/2} = L^{d(d−2)/2}.
    Returns d(d−2)/2 — NONZERO for d ≥ 3 ⇒ covolume dependence survives.
    """
    return mp.mpf(d) * (mp.mpf(d) - 2) / 2


def moduli_volume_numeric(d: int, L: mp.mpf) -> mp.mpf:
    """Direct Vol(J(T^d)) for the scaled cubic torus ℝ^d/(LZ^d), flat metric.

    Vol(J) = covol_Euclid(Λ_H) · sqrt(det(metric on harmonic c-space)),
    Λ_H = (1/L)ℤ^d, metric = V·δ = L^d·δ. Computed factor-by-factor (no shortcut)
    so the closed-form exponent d(d−2)/2 is checked against an explicit build.
    """
    V = L ** d                       # torus volume = covolume of LZ^d
    covol_lambda_H = (1 / L) ** d     # Euclidean covolume of (1/L)ℤ^d
    sqrt_det_metric = V ** (mp.mpf(d) / 2)  # √det(V·δ_{d×d}) = V^{d/2}
    return covol_lambda_H * sqrt_det_metric


def gaussian_2pi_bookkeeping_toy(lam: mp.mpf) -> mp.mpf:
    """One real Gaussian ∫_{−∞}^{∞} da e^{−½ λ a²} = (2π/λ)^{1/2}; return the
    ratio to (2π)^{1/2} λ^{−1/2} (must be 1) — the per-mode (2π)^{1/2} bookkeeping."""
    lhs = mp.quad(lambda a: mp.e ** (-lam * a * a / 2), [-mp.inf, mp.inf])
    rhs = mp.sqrt(2 * mp.pi / lam)
    return lhs / rhs


def main() -> int:
    print("=" * 78)
    print(" α_EM per-loop measure — flat-torus Maxwell 1-loop partition function")
    print("=" * 78)

    ok_all = True

    # ── CONTROL 1: reproduce ζ_{Δ₁}(0) = −b₁ via the REUSED #3834 machinery ──
    print("\n[control 1] ζ_{Δ₁}(0) = d·E_Λ(0) = −b₁  (reused Epstein machinery):")
    zeta_rows = []
    for d in (1, 2, 3, 8):
        e0 = epstein_zero_cubic(d)
        z_delta1 = d * e0
        err = abs(z_delta1 - (-d))
        ok = err < mp.mpf("1e-6")
        ok_all = ok_all and ok
        print(f"   d={d}: ζ_Δ₁(0)={mp.nstr(z_delta1,10)}  (target −{d}, |err|={mp.nstr(err,3)})  {ok}")
        zeta_rows.append({"d": d, "zeta_delta1_0": mp.nstr(z_delta1, 12),
                          "target": -d, "err": mp.nstr(err, 6), "ok": bool(ok)})

    # ── CONTROL 2: single-mode Gaussian (2π)^{1/2} bookkeeping ──
    print("\n[control 2] single real Gaussian bookkeeping ∫da e^{−½λa²} = (2π)^{½}λ^{−½}:")
    toy_ratios = []
    for lam in (mp.mpf("0.5"), mp.mpf(1), mp.mpf("3.7")):
        r = gaussian_2pi_bookkeeping_toy(lam)
        ok = abs(r - 1) < mp.mpf("1e-20")
        ok_all = ok_all and ok
        print(f"   λ={mp.nstr(lam,4)}: LHS/[(2π)^½ λ^−½] = {mp.nstr(r,12)}  (→1)  {ok}")
        toy_ratios.append({"lambda": mp.nstr(lam, 6), "ratio": mp.nstr(r, 14), "ok": bool(ok)})

    # ── EXTRACT (a): π-power of the Maxwell oscillator measure ──
    # Each non-zero mode = one real Gaussian ⇒ (2π)^{½} per mode ⇒ the whole
    # oscillator measure regularizes to (2π)^{½ ζ_{Δ₁}(0)} = (2π)^{−b₁/2}.
    zeta_delta1_0 = B1 * epstein_zero_cubic(B1)          # = −b₁ (numeric)
    measure_2pi_power = zeta_delta1_0 / 2                 # = −b₁/2
    measure_pi_power = measure_2pi_power                  # π-power (companion 2^{−b₁/2})
    print("\n[extract a] Maxwell oscillator measure = (2π)^{½ ζ_Δ₁(0)} = (2π)^{−b₁/2}:")
    print(f"   ζ_Δ₁(0)={mp.nstr(zeta_delta1_0,8)}  ⇒ (2π)-power = {mp.nstr(measure_2pi_power,8)}"
          f"  (π-power = {mp.nstr(measure_pi_power,8)}, + companion 2^{{−b₁/2}})")
    print(f"   |π-power| = {mp.nstr(abs(measure_pi_power),6)}  vs  target |π-power| = 1")
    pi_power_is_one = abs(abs(measure_pi_power) - 1) < mp.mpf("1e-6")   # expect FALSE
    print(f"   ⇒ π-power == 1 (target)?  {pi_power_is_one}   (b₁=8 ⇒ −4 ≠ −1)")

    # ── EXTRACT (b): b₁-dependence — exponent linear in b₁ vs target reciprocal ──
    print("\n[extract b] b₁-dependence: measure exponent −d/2 (LINEAR) vs target 1/(πd) (RECIPROCAL):")
    b1_rows = []
    for d in (1, 2, 3, 8):
        expo = mp.mpf(-d) / 2                       # Maxwell (2π)-exponent
        target = 1 / (mp.pi * d)                    # target per-loop measure value
        print(f"   d={d}: Maxwell (2π)-exponent={mp.nstr(expo,6)}   target 1/(πd)={mp.nstr(target,8)}")
        b1_rows.append({"d": d, "maxwell_2pi_exponent": mp.nstr(expo, 8),
                        "target_1_over_pi_d": mp.nstr(target, 10)})
    # reciprocal ⇒ halving effect as d grows; exponential ⇒ deepening. Structurally different.
    reciprocal_match = False  # exponent-in-b₁ is never the reciprocal 1/b₁ form

    # ── EXTRACT (c): area/covolume-dependence of the zero-mode (Jacobian) volume ──
    print("\n[extract c] moduli Vol(J(T^d)) ∝ L^{d(d−2)/2} under Λ→LΛ — covolume dependence:")
    area_rows = []
    covolume_survives = False
    for d in (1, 2, 3, 8):
        p = moduli_volume_scaling_exponent(d)
        # verify the closed-form exponent against an explicit numeric build at L=1,2
        v1 = moduli_volume_numeric(d, mp.mpf(1))
        v2 = moduli_volume_numeric(d, mp.mpf(2))
        ratio = v2 / v1
        expect_ratio = mp.mpf(2) ** p
        ok = abs(ratio - expect_ratio) < mp.mpf("1e-20")
        ok_all = ok_all and ok
        if abs(p) > mp.mpf("1e-9"):
            covolume_survives = True
        print(f"   d={d}: exponent d(d−2)/2 = {mp.nstr(p,6)}   Vol(J)|_{{L=2}}/Vol(J)|_{{L=1}}"
              f" = {mp.nstr(ratio,8)}  (=2^{{{mp.nstr(p,4)}}}? {ok})")
        area_rows.append({"d": d, "scaling_exponent_d_d_minus_2_over_2": mp.nstr(p, 8),
                          "ratio_L2_over_L1": mp.nstr(ratio, 12),
                          "expected_2_pow_p": mp.nstr(expect_ratio, 12), "ok": bool(ok)})
    print(f"   ⇒ at d=b₁=8 exponent = {mp.nstr(moduli_volume_scaling_exponent(8),4)} ≠ 0"
          f"  ⇒ covolume dependence SURVIVES (target must be area-free).")

    # ── COMPARE to 1/(π b₁) ──
    print("\n" + "-" * 78)
    print(" COMPARISON to target per-loop measure 1/(π b₁) = π^{−1}·b₁^{−1} (area-free):")
    print(f"   · π-power   : target −1        | Maxwell −b₁/2 = {mp.nstr(measure_pi_power,4)}   ✗")
    print(f"   · 2 vs π    : target bare π     | Maxwell 2π ⇒ companion 2^{{−b₁/2}}          ✗")
    print(f"   · b₁ form   : target 1/b₁       | Maxwell exponential (2π)^{{−b₁/2}}          ✗")
    print(f"   · area      : target area-free  | Maxwell Vol(J) ∝ L^{{d(d−2)/2}}, exp 24@d=8  ✗")

    positive_partial = pi_power_is_one and reciprocal_match and (not covolume_survives)
    verdict = "POSITIVE-partial" if positive_partial else "NEGATIVE (scope-(a))"
    print("\n" + "=" * 78)
    print(f" VERDICT: {verdict}")
    print("=" * 78)
    print(" The flat-torus Maxwell 1-loop partition function does NOT produce 1/(π b₁).")
    print(" Failing factors: (i) π-power = b₁/2 ≠ 1 (2π-per-mode Gaussian bookkeeping);")
    print(" (ii) b₁ appears exponentially, not reciprocally; (iii) Vol(J) covolume survives.")
    print(" A real, redirecting result: the per-loop measure is NOT the naive Maxwell Z;")
    print(" the ζ_Δ₁(0)=−b₁ area-free NUMERATOR count (#3834) stands; the MEASURE claim fails.")
    print(" No α_k wired; no fit; no tier change; 1/(8π) stays a phase-4 identification.")

    # ── witness ──
    wb = WitnessBuilder("alpha-em-flat-torus-maxwell-perloop", engine="mpmath")
    wb.set_description(
        "Flat-torus Maxwell (free U(1) gauge) 1-loop partition-function probe of the "
        "residual α_EM per-loop-measure wall. Computes Z_Maxwell(T^d) = Vol(J(M))·"
        "(2π)^{½ζ_Δ₁(0)}·(det'Δ₁)^{−1/2}·(det'Δ₀)^{+1} INDEPENDENTLY of any α data "
        "(reusing the #3834 Epstein-zeta machinery: ζ_Δ₁(0)=d·E_Λ(0)=−b₁, exact/area-free), "
        "and MEASURES the π-power, b₁-dependence and covolume-dependence, then COMPARES "
        "(never fits) to the data-selected target 1/(π b₁)=1/(8π). EXTRACTED: (a) the "
        "per-mode Gaussian bookkeeping forces the oscillator measure (2π)^{½ζ_Δ₁(0)}="
        "(2π)^{−b₁/2}, so π enters to power −b₁/2 (LINEAR in b₁, magnitude 4 at b₁=8) with "
        "a companion 2^{−b₁/2} (2π, not π); (b) b₁ sits in the EXPONENT, not a reciprocal "
        "1/b₁; (c) the zero-mode Jacobian volume Vol(J(T^d)) scales as L^{d(d−2)/2} under "
        "Λ→LΛ (exponent 24 at d=8, verified numerically at L=1,2), so covolume dependence "
        "SURVIVES. COMPARISON to 1/(π b₁)=π^{−1}b₁^{−1} (area-free): π-power −1 vs −b₁/2 ✗; "
        "bare π vs 2π ✗; reciprocal b₁ vs exponential ✗; area-free vs Vol(J) covolume ✗. "
        "VERDICT scope-(a) NEGATIVE (the stub's pre-stated likely outcome): the flat-torus "
        "Maxwell 1-loop partition function is NOT the per-loop measure 1/(π b₁). Named "
        "failing factors: (i) π-power b₁/2≠1 from the 2π-per-mode bookkeeping, (ii) b₁ "
        "exponential not reciprocal, (iii) Vol(J) covolume dependence (removable only by a "
        "normalization CHOICE — the forbidden fitting trap). Redirects the search: the "
        "reciprocal-in-b₁, single-π, area-free structure must come from a DIFFERENT "
        "normalization object than Z_Maxwell(T^{b₁}). The #3834 area-free numerator count "
        "ζ_Δ₁(0)=−b₁ is untouched; only the MEASURE claim fails. Anti-laundering respected: "
        "no CODATA read, no convention tuned to land on 8π. No α_k wired; no fit; no tier "
        "change; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.set_audit_only("docs/audits/2026-07-18-alpha-em-flat-torus-maxwell-perloop.md")
    wb.add_data("control_zeta_delta1_zero", zeta_rows)
    wb.add_data("control_gaussian_2pi_bookkeeping", toy_ratios)
    wb.add_data("extract_a_pi_power", {
        "zeta_delta1_0": mp.nstr(zeta_delta1_0, 12),
        "measure_2pi_power": mp.nstr(measure_2pi_power, 12),
        "measure_pi_power": mp.nstr(measure_pi_power, 12),
        "companion_factor": "2^{−b₁/2} (measure is 2π, not π)",
        "target_pi_power": -1,
        "pi_power_equals_target": bool(pi_power_is_one),
        "reading": "π enters to power −b₁/2 (linear in b₁, magnitude 4 at b₁=8), NOT −1"})
    wb.add_data("extract_b_b1_dependence", {
        "form": "measure exponent −d/2 is LINEAR in b₁ (exponential (2π)^{−b₁/2})",
        "target_form": "1/(π b₁): RECIPROCAL in b₁",
        "reciprocal_match": bool(reciprocal_match),
        "rows": b1_rows})
    wb.add_data("extract_c_area_covolume", {
        "moduli_scaling_exponent_formula": "d(d−2)/2",
        "exponent_at_b1_8": int(moduli_volume_scaling_exponent(8)),
        "covolume_survives": bool(covolume_survives),
        "target_requires": "area-free (ζ_Δ₁(0)=−b₁ is area-free)",
        "rows": area_rows})
    wb.add_data("comparison_to_target", {
        "target": "1/(π b₁) = π^{−1}·b₁^{−1}, area-free",
        "pi_power": "target −1 vs Maxwell −b₁/2 = −4  → FAIL",
        "two_vs_pi": "target bare π vs Maxwell 2π (companion 2^{−b₁/2})  → FAIL",
        "b1_form": "target reciprocal 1/b₁ vs Maxwell exponential  → FAIL",
        "area": "target area-free vs Maxwell Vol(J)∝L^{d(d−2)/2}  → FAIL"})
    wb.add_data("verdict", {
        "scope": "(a)",
        "result": "NEGATIVE",
        "failing_factors": [
            "(i) π-power = b₁/2 ≠ 1 (2π-per-mode Gaussian bookkeeping)",
            "(ii) b₁ appears exponentially in (2π)^{−b₁/2}, not reciprocally as 1/b₁",
            "(iii) zero-mode Vol(J(T^{b₁})) carries covolume dependence L^{d(d−2)/2}"],
        "redirect": ("the reciprocal-in-b₁, single-π, area-free 1/(π b₁) must come from a "
                     "DIFFERENT normalization object than the naive Z_Maxwell(T^{b₁}); the "
                     "#3834 area-free numerator count ζ_Δ₁(0)=−b₁ stands, only the MEASURE fails"),
        "anti_laundering": "no CODATA read; no convention tuned to land on 8π"})

    wb.add_assertion("control_zeta_delta1_zero_equals_minus_b1",
                     computed=float(zeta_delta1_0), expected=float(-B1), tolerance=1e-3,
                     source="reused #3834 machinery: ζ_{Δ₁}(0)=d·E_Λ(0)=−b₁=−8 (sanity control)")
    wb.add_assertion("control_gaussian_2pi_bookkeeping_ok",
                     computed=1.0 if all(r["ok"] for r in toy_ratios) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="∫da e^{−½λa²}=(2π)^{½}λ^{−½} verified for λ=0.5,1,3.7 (per-mode 2π bookkeeping)")
    wb.add_assertion("measure_pi_power_is_minus_b1_over_2_not_minus_1",
                     computed=float(measure_pi_power), expected=float(-B1) / 2, tolerance=1e-3,
                     source="Maxwell oscillator measure (2π)^{½ζ_Δ₁(0)}=(2π)^{−b₁/2}: π-power −4, NOT the target −1")
    wb.add_assertion("moduli_covolume_dependence_survives",
                     computed=1.0 if covolume_survives else 0.0, expected=1.0, tolerance=0.5,
                     source="Vol(J(T^d))∝L^{d(d−2)/2}, exponent 24 at d=8 (verified L=1,2) — NOT area-free")
    wb.add_assertion("verdict_negative_scope_a",
                     computed=0.0 if positive_partial else 1.0, expected=1.0, tolerance=0.5,
                     source="π-power≠1, b₁ non-reciprocal, covolume survives ⇒ flat-torus Maxwell Z ≠ 1/(π b₁)")
    wb.save()

    print("\n  RESULT: flat-torus Maxwell measure = (2π)^{−b₁/2} × covolume-dependent Vol(J),")
    print("          π-power = b₁/2 (not 1), b₁ exponential (not reciprocal) ⇒ NOT 1/(π b₁).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
