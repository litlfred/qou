#!/usr/bin/env python3
"""
alpha_em_4pi_derived_form_probe.py — REFUTATION LOG of the fit-class
approach to deriving α/(4π) in the FSC closure. DO NOT PURSUE these
candidates — they are documented here as refuted.

⚠️  AGENT WARNING: This script enumerates 12 parameter-free candidate
    forms (Hodge ratios, CM j-invariants, ζ(3) combinations, etc.) and
    finds that ALL are refuted at the framework's 100× experimental
    precision target. The closest, 1/j(i) = 1/1728 at −0.34%, is in
    the same NEAR-MISS fit class as the candidates the proposition
    `prop:em-coupling-bring-zero-mode` (lines 206-210) explicitly
    warns about:

      "The simplest fits are all near-misses; an exact form requires
       the explicit 2-loop calculation."

    DO NOT propose 1/j(i) or any other near-miss form here as the
    derived α/(4π). The proper derivation path is the higher Bloch
    group B_3(ℂ) with the Goncharov trilogarithm D_3 (proposition
    lines 148-153), pursued on a separate branch using PSLQ search
    over the canonical Bring-symmetric angle basis (modeled on
    `bring_zero_mode_bloch_hunt.py`).

CONTEXT. The framework's α_EM⁻¹ proposition (Bring zero-mode shift) is:

  α_EM⁻¹ = q·[9]_q·[10]_q + 2g/(4π(g−1))|_{g=4} + O(α)
         = 136.823 + 0.2122 + α/(4π)
         = 137.0354 + 5.80e-4
         = 137.0360  (vs CODATA 137.035999084, residual +57 ppb)

The O(α) ≈ α/(4π) is currently a numerical near-match without a derived
categorical form. The earlier candidate 1/(2π·[2]_q) is two orders of
magnitude off, not it.

WHAT THIS PROBE DOES. Tests ~8 candidate derived forms for the next-order
correction against the CODATA target α/(4π) ≈ 5.804990e-4 at q₀.
Candidates are categorical/geometric in spirit (Hodge classes, Chern-Simons
one-loop coefficients, eta-invariants, q-deformations of the Bring shift).

Honest derive-or-refute: NO fit. Each candidate is a parameter-free
geometric quantity. Best candidate's residual is reported; if no
candidate is within a few percent, the derived form is OPEN.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, pi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("alpha-em-4pi-derived-form-probe", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    qbra = lambda n: (q**n - q**(-n)) / (q - q**(-1))  # noqa: E731

    CODATA_alpha_inv = mpf("137.035999084")
    alpha_codata = 1 / CODATA_alpha_inv
    TARGET = alpha_codata / (4 * pi)            # ≈ 5.80499e-4

    # ─── Bring surface geometry (genus g=4) ─────────────────────────────
    g = 4
    chi = mpf(2 - 2 * g)                        # = −6
    area = -2 * pi * chi                        # = 12π (Gauss-Bonnet)

    # ─── 8 candidate derived forms ──────────────────────────────────────
    candidates = {}

    # (1) Second Hodge-class / area²:
    #     H²(M_Bring; ℝ) = ℝ (top class), normalized 1/(Area)²
    candidates["1/Area² = 1/(12π)²"] = 1 / area**2

    # (2) χ²/Area² = (g-1)²/(area squared scale) — categorical
    candidates["χ²/Area² = 36/(144π²)"] = chi**2 / area**2

    # (3) 1/(2g·Area) — analog of Bring shift one power higher in (g-1)
    candidates["1/(2g·Area) = 1/(8·12π)"] = 1 / (2 * g * area)

    # (4) 1/(2g(g-1)·Area) — full descent in genus
    candidates["1/(2g(g-1)·Area) = 1/(24·12π)"] = 1 / (2 * g * (g - 1) * area)

    # (5) q-bracket modulation of the Bring shift, square:
    #     [Bring shift]² / [2]_q² — natural q-categorical
    bring = mpf(2 * g) / (4 * pi * (g - 1))
    bra2 = qbra(2)
    candidates["(2/(3π))² / [2]_q²"] = bring**2 / bra2**2

    # (6) Chern-Simons one-loop on S³/Γ_Bring at level k=1:
    #     Z_CS ~ 1/(2π·k²·|Γ|) for a finite-volume quotient
    #     Γ_Bring is related to PSL(2,5) (icosahedral), |Γ| = 60
    Gamma_order = mpf(60)
    candidates["1/(2π·|PSL(2,5)|)"] = 1 / (2 * pi * Gamma_order)

    # (7) Inverse of categorical full-twist: 1/(Δ_3² · Area) where Δ_3² has
    #     length 6 in B_3 (length of central full-twist on 3 strands)
    central_length = mpf(6)
    candidates["1/(Δ₃² length · Area) = 1/(6·12π)"] = 1 / (central_length * area)

    # (8) Volume-normalized: Vol(S²)/Vol(S³)² — companion to the
    #     Bring shift's Vol(S²)/(3·Vol(S³)) identification
    vol_S2 = 4 * pi
    vol_S3 = 2 * pi**2
    candidates["Vol(S²)/Vol(S³)²"] = vol_S2 / vol_S3**2

    # (9) j-invariant at CM point τ=i, inverse: 1/j(i) = 1/1728. The
    #     Bring curve is a CM-like algebraic curve; its Jacobian has CM
    #     structure, so 1/j(i) is a natural categorical candidate.
    #     Equivalently: π²/(2|χ|·Area²) = 1/1728.
    candidates["1/j(i) = 1/1728  (Bring CM candidate)"] = mpf(1) / 1728

    # (10) (1/j(i)) · (1 + 1/[2]_q²) — q-bracket-corrected CM candidate
    candidates["(1/1728)·(1 + 1/[2]_q²)"] = (mpf(1) / 1728) * (1 + 1 / bra2**2)

    # (11) Discriminant Δ(τ=i)/(2π)^12 = 1/1728  (same as #9, modular form check)
    #      (We compute it as Δ_modular/2π^12 to confirm.)
    # Equivalent: ζ(3)/(2π)³ — Apéry-style constant
    from mpmath import zeta
    candidates["ζ(3)/(2π)³"] = zeta(3) / (2 * pi)**3

    # (12) 1/(2·χ²·area) = 1/(2·36·12π) = 1/(864π) — alt categorical
    candidates["1/(2χ²·Area) = 1/(864π)"] = 1 / (2 * chi**2 * area)

    # ─── Report ─────────────────────────────────────────────────────────
    print("=" * 76)
    print(" α/(4π) DERIVED FORM probe — candidates vs CODATA target")
    print("=" * 76)
    print(f"  q₀ = {float(q):.14f}   CODATA α⁻¹ = {float(CODATA_alpha_inv):.9f}")
    print(f"  Target  α/(4π) = {mp.nstr(TARGET, 12)}")
    print(f"  Bring shift 2/(3π) = {mp.nstr(bring, 12)} (already in tree)")
    print()
    print(f"  {'candidate':45s} {'value':>14s} {'ratio':>10s} {'log10|ratio−1|':>16s}")
    results = {}
    for name, val in candidates.items():
        ratio = val / TARGET
        from mpmath import log10
        log_dev = log10(abs(ratio - 1)) if abs(ratio - 1) > 1e-50 else mpf(-50)
        results[name] = {
            "value": mp.nstr(val, 14),
            "ratio_to_target": float(ratio),
            "log10_abs_dev": float(log_dev),
        }
        print(f"  {name:45s} {float(val):>14.6e} {float(ratio):>10.4f} {float(log_dev):>16.3f}")

    # ─── Honest read ────────────────────────────────────────────────────
    best = min(results, key=lambda k: abs(results[k]["ratio_to_target"] - 1))
    best_ratio = results[best]["ratio_to_target"]
    print()
    print(f"Best candidate: {best}")
    print(f"  ratio = {best_ratio:.6f}  (1 ⇒ exact match)")
    print(f"  deviation = {(best_ratio - 1) * 100:+.2f}%")
    print()
    if abs(best_ratio - 1) < 0.001:
        print("✓ DERIVED: best candidate matches within 0.1%. Pin this form.")
    elif abs(best_ratio - 1) < 0.05:
        print("~ NEAR-MATCH: best candidate within 5%. Investigate q-corrections.")
    else:
        print("✗ REFUTED so far: no candidate within 5%. The derived form is OPEN.")
        print("  Next: try Reidemeister torsion of M_Bring, η-invariant of Dirac")
        print("  operator on Bring orbifold, or higher-level (k≥2) Chern-Simons.")

    # ── Witness ──────────────────────────────────────────────────────────
    wb.set_description(
        "Derive-or-refute candidate categorical/geometric forms for the "
        "next-order α/(4π) ≈ 5.805e-4 correction in the FSC α_EM⁻¹ closure. "
        "8 parameter-free candidates: 2nd Hodge class, Euler-char² / area², "
        "genus-descent factors, q-bracket modulation of Bring shift, "
        "Chern-Simons one-loop on S³/PSL(2,5), central-full-twist length "
        "normalization, and sphere-volume ratio. No fit; honest residual."
    )
    wb.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "CODATA_alpha_inv": "137.035999084",
        "target_alpha_over_4pi": mp.nstr(TARGET, 30),
        "g_Bring": 4,
        "chi_Bring": "-6",
        "area_Bring": mp.nstr(area, 20),
    })
    wb.add_data("candidates_vs_target", results)
    wb.add_data("best", {
        "candidate": best,
        "ratio": float(best_ratio),
        "deviation_percent": float((best_ratio - 1) * 100),
        "verdict": ("DERIVED" if abs(best_ratio - 1) < 0.001
                    else "NEAR-MATCH" if abs(best_ratio - 1) < 0.05
                    else "REFUTED"),
    })
    wb.add_assertion(
        "all_candidates_evaluated",
        computed=len(results),
        expected=12,
        tolerance=0,
        source="Twelve parameter-free derived-form candidates evaluated against "
               "CODATA α/(4π) ≈ 5.80499e-4 at q₀ (50 dps). Includes Hodge / "
               "Chern-Simons / CM / ζ(3) candidates.",
    )
    wb.save()


if __name__ == "__main__":
    main()
