"""
constit_factor_varying_q_phase5k2.py — Phase 5k.2: varying-q sweep
to confirm the unit-coefficient h^5 finding at q_0 (Phase 5k.1).

Phase 5k.1 found that the residual

  r(q_0) := ρ_Z^constit(q_0) - (2*q_0 - 1)

equals h^5(q_0) with coefficient c = 1.016 — only 1.6% off unity.

If this is a TRUE structural identity (ρ = (2q - 1) + h^5 + O(h^7)),
the coefficient c(q) := r(q) / h(q)^5 should be 1 (to leading order)
for ALL q in the substrate window, not just at q_0.

This script tests that hypothesis directly by measuring ρ_Z^constit
at multiple q values, computing the residual, dividing by h^5, and
checking if c(q) is approximately 1 across the window.

  measurement pipeline at each q:
    1. y_λ(q) via y_lambda_wenzl_bridge_numeric (Wenzl normalization)
    2. χ_λ(𝓑_p · 𝓑_n, q) via chi_lambda_braid (Rust kernel, q_value=q)
    3. tr_M_constit(D) = Σ_{λ⊢6} y_λ(q) · χ_λ(𝓑_constit_D, q)
    4. tr_M_constit(³He) = Σ_{λ⊢9} y_λ(q) · χ_λ(𝓑_constit_3He, q)
    5. ρ(q) = tr_M_constit(³He) / tr_M_constit(D)

  Ref: conj:constit-factor-2q-minus-1.md (PR #831)
  Ref: PR #831 Phase 5k.1 (constit_factor_residual_phase5k.py)
  Ref: PR #819 Phase 5c.1 (delta_lambda_fr_identity_phase5c.py)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import chi_lambda_braid, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from canonical_braid_marshalling import marshal_to_chi_lambda_braid  # noqa: E402


# Substrate-window q values to test.  q_0 is the canonical 50-digit
# substrate pin from q_parameter (Q_50_DIGIT_STR) so this witness is
# precision-comparable with other canonical-q witnesses across the
# codebase.  Surrounding q values frame the substrate window.
Q_VALUES = ["1.05", "1.08", Q_50_DIGIT_STR, "1.13", "1.17"]


def compute_tau_M_constit(Z: int, N: int, q_val: mp.mpf,
                          dps: int = 50) -> mp.mpf:
    """Compute tr_M(𝓑_constit_K) = Σ_λ y_λ · χ_λ(𝓑_constit_K) at q.

    Uses the CONSTIT factorisation (include_inter=False), so the
    braid word has no interface generators.

    Per Gemini PR #854 review: braid marshalling centralized in
    `canonical_braid_marshalling.marshal_to_chi_lambda_braid` (see
    that module for the (c, d) → (sign, gen) convention).
    """
    word = atom_braid_word_3A(Z, N, include_inter=False)
    h_val = float(Q0 - 1 / Q0)  # h at the substrate point — defines word  # noqa: I8 — sign-classification param for marshal_to_chi_lambda_braid (matched vs d within eps=1e-10), not a precision coefficient
    word_m = marshal_to_chi_lambda_braid(word, h_val)
    n = 3 * (Z + N)
    # Pass q as a string to avoid f64 quantization; use mpfr_50dps
    # precision for chi_lambda_braid to match y_λ's 50-dps pin.
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    # Batch character evaluation across partitions (F-A of ffi-roundtrip-
    # audit): one PyO3 crossing + rayon-parallel inside Rust, vs the
    # p(n) per-shape FFI calls the loop used to make.
    from hecke_characters import chi_lambdas_braid
    parts = list(partitions_of(n))
    chi_values = chi_lambdas_braid(parts, word_m, q_value=q_str,
                                    precision="mpfr_50dps")
    total = mp.mpf(0)
    for lam, chi in zip(parts, chi_values):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        total += y * mp.mpf(str(chi))
    return total


def measure_rho_at_q(q_val: mp.mpf, dps: int = 50) -> tuple[dict, mp.mpf]:
    """Compute ρ_Z^constit(q) = tr_M_constit(³He) / tr_M_constit(D).

    Per Gemini PR #854 review: returns the high-precision rho as an
    mp.mpf object alongside the f64-summarized dict, so downstream
    analysis preserves full 50-dps precision instead of round-tripping
    through a 30-digit string.

    Returns:
        (summary_dict, rho_mpf) — summary for the witness JSON, mpf for
        precision-preserving analysis.
    """
    t0 = time.time()
    tau_D = compute_tau_M_constit(1, 1, q_val, dps=dps)
    t1 = time.time()
    tau_3He = compute_tau_M_constit(2, 1, q_val, dps=dps)
    t2 = time.time()
    if tau_D == 0:
        return {"q": float(q_val), "error": "tau_M_constit(D) = 0"}, mp.mpf(0)
    rho = tau_3He / tau_D
    return {
        "q": float(q_val),
        "tau_M_constit_D": float(tau_D),
        "tau_M_constit_3He": float(tau_3He),
        "rho_Z_constit": float(rho),
        "rho_Z_constit_str": mp.nstr(rho, 30),
        "wall_seconds_D": t1 - t0,
        "wall_seconds_3He": t2 - t1,
    }, rho


def analyze_residual(q_val: mp.mpf, rho: mp.mpf) -> dict:
    """Compute residual against (2q - 1) and the c = residual / h^5
    coefficient (Phase 5k.1 hypothesis: c ≈ 1)."""
    predicted = 2 * q_val - 1
    residual = rho - predicted
    h = q_val - 1 / q_val
    h5 = h ** 5
    c_h5 = residual / h5 if h5 != 0 else mp.mpf("nan")
    return {
        "predicted_2q_minus_1": float(predicted),
        "residual": float(residual),
        "h": float(h),
        "h_to_5": float(h5),
        "c_residual_over_h5": float(c_h5),
        "rel_err_pct": float(abs(residual) / predicted * 100),
    }


def main() -> int:
    set_compute_dps(50)

    # Construct the WitnessBuilder BEFORE the sweep so the recorded
    # durationMs reflects the full compute, not just the save step.
    builder = WitnessBuilder(
        "constit-factor-varying-q-phase5k2", engine="python"
    )

    print(f"=== Phase 5k.2: varying-q sweep, q ∈ {Q_VALUES} ===\n")

    results = []
    for q_str in Q_VALUES:
        q_val = mp.mpf(q_str)
        print(f"  q = {q_str} ...")
        meas, rho_mpf = measure_rho_at_q(q_val)
        if "error" in meas:
            print(f"    ERROR: {meas['error']}")
            continue
        ana = analyze_residual(q_val, rho_mpf)
        meas.update(ana)
        results.append(meas)
        print(f"    ρ_Z^constit = {meas['rho_Z_constit']:.10f}")
        print(f"    (2q - 1)    = {meas['predicted_2q_minus_1']:.10f}")
        print(f"    residual    = {meas['residual']:+.4e}")
        print(f"    h^5(q)      = {meas['h_to_5']:.4e}")
        print(f"    c = r / h^5 = {meas['c_residual_over_h5']:+.4f}")
        print(f"    rel.err     = {meas['rel_err_pct']:.4f}%")
        print()

    print(f"=== Summary table ===\n")
    print(f"  {'q':>8} {'ρ_Z^constit':>14} {'(2q-1)':>14} "
          f"{'residual':>14} {'h^5':>14} {'c=r/h^5':>10}")
    for r in results:
        print(f"  {r['q']:>8.5f} {r['rho_Z_constit']:>14.8f} "
              f"{r['predicted_2q_minus_1']:>14.8f} "
              f"{r['residual']:>+14.4e} "
              f"{r['h_to_5']:>14.4e} "
              f"{r['c_residual_over_h5']:>+10.4f}")
    print()

    # Verdict
    c_values = [r["c_residual_over_h5"] for r in results]
    c_min, c_max = min(c_values), max(c_values)
    c_mean = sum(c_values) / len(c_values)
    c_spread = (c_max - c_min) / abs(c_mean) if c_mean != 0 else float("inf")
    print(f"=== Verdict ===\n")
    print(f"  c(q) range across {len(results)} q-points:")
    print(f"    min  = {c_min:+.4f}")
    print(f"    max  = {c_max:+.4f}")
    print(f"    mean = {c_mean:+.4f}")
    print(f"    spread / |mean| = {c_spread*100:.2f}%")
    if c_spread < 0.10 and abs(c_mean - 1.0) < 0.10:
        print(f"\n  ✓ UNIT-COEFFICIENT h^5 CONFIRMED across the substrate "
              f"window (c ≈ 1 ± 10%).")
        verdict = "unit-coefficient-h5-confirmed"
    elif c_spread < 0.10:
        print(f"\n  ⚠ c(q) is constant (~{c_mean:.3f}) but NOT unity. "
              f"Suggests ρ = (2q-1) + c·h^5 + O(h^7) with c ≠ 1.")
        verdict = "constant-coefficient-but-not-unity"
    else:
        print(f"\n  ✗ c(q) varies significantly across q "
              f"(spread {c_spread*100:.1f}%). The h^5 hypothesis is "
              f"NOT confirmed; the residual has a more complex "
              f"q-dependence.")
        verdict = "h5-form-not-confirmed"

    # Witness — builder constructed at start of main() for accurate
    # durationMs; populate now that the sweep has finished.
    # Phase 5k.2 is a falsification probe; the conjecture's primary
    # computation wiring points at constit_factor_and_volhyp_test.py
    # (Phase 5g categorical search). This witness is supplementary,
    # tracked via auditOnly per docs/audits/2026-05-20-constit-factor-closure-chain.md.
    builder.set_audit_only("docs/audits/2026-05-20-constit-factor-closure-chain.md")
    builder.add_parameter("q_values", Q_VALUES)
    builder.set_description(
        "Phase 5k.2: varying-q sweep to confirm Phase 5k.1's unit-"
        "coefficient h^5 finding. For each q in the substrate window, "
        "computes ρ_Z^constit(q) = tr_M_constit(³He, q) / "
        "tr_M_constit(D, q) using y_λ(q) Wenzl weights and "
        "χ_λ(𝓑_constit, q) Hecke characters. Tests whether "
        "c(q) := (ρ - (2q-1)) / h^5 is approximately 1 across q, "
        "which would confirm the structural identity ρ = (2q-1) + "
        "h^5 + O(h^7)."
    )
    builder.add_data("per_q_results", results)
    builder.add_data("c_h5_range", {
        "min": c_min, "max": c_max, "mean": c_mean,
        "relative_spread": c_spread,
    })
    builder.add_data("verdict", verdict)
    # Per Copilot PR #854: Phase 5k.2 is a falsification probe; encode
    # the EXPECTED REFUTATION as the passing assertion so CI/audits
    # don't treat the refutation as a regression.  The hypothesis
    # tested ("c(q) ≡ 1 with small spread") is expected to FAIL; this
    # assertion records that the spread is LARGE (refutation succeeded).
    builder.add_assertion(
        name="phase_5k_2_unit_h5_hypothesis_falsified",
        computed=float(c_spread > 0.5),   # 1.0 if spread > 50% (refuted)
        expected=1.0,
        tolerance=0.5,                    # binary outcome
        unit="dimensionless (refutation-confirmed boolean)",
        source=(
            f"Phase 5k.2 falsification probe: c(q) = (ρ - (2q-1)) / h^5 "
            f"varies by spread/|mean| = {c_spread*100:.1f}% across {len(results)} "
            f"q-points. The unit-coefficient h^5 hypothesis (c ≡ 1) "
            f"requires spread < 10%; observed spread = {c_spread*100:.1f}% "
            f"confirms the hypothesis is FALSIFIED — exactly the expected "
            f"outcome of this falsification probe.  Verdict: {verdict}."
        ),
    )
    builder.save()
    print(f"\nWitness written: constit-factor-varying-q-phase5k2.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
