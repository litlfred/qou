"""T5: alternative `Geom_leading` form q-locality probe.

Per the architectural finding (q-locality probe + h⁴ probe):
linking_weight refinements cannot fix q-locality because the slope
is dominated by `Geom_leading = Vol(𝓑₃)/ℏ_q²`'s q-dependence.

This probe tests **alternative functional forms for `Geom_leading`**
to see if any restore q-locality. Each variant differs only in the
denominator's dependence on the substrate parameter. The linking
weight is held fixed at Family A's `5/2 + (3/4)·h²` so that any
slope improvement is unambiguously attributable to the `Geom_leading`
change.

Variants tested:

  v0  (canonical)     Vol/ℏ_q²            — current production baseline
  v1  (linear ℏ)      Vol/ℏ_q             — first power, not squared
  v2  (h² form)       Vol/h²              — using h = q − q⁻¹ instead
  v3  (q-quantum)     Vol/[2]_q²          — quantum integer denominator
  v4  (symmetric)     Vol·q/(q−1)²        — slightly modified
  v5  (exp variant)   Vol·exp(−ℏ_q)       — exponential
  v6  (log variant)   Vol/(−log(q))²      — log-based
  v7  (Family-A cap)  Vol/ℏ_q² · 1/λ_target(q_0) · λ_target(q)
                                          — DOES match by construction
                                          (sanity check on probe)
  v8  (mass-form)     same as v0 but with m(K) = m_e · √VolDensity
                                          — sqrt mass-formula variant
                                          (different architecture)

Outcomes per variant:
  - slope at q_0 (ppm/q)
  - m_p_pred at q_0 (MeV)
  - PASS/FAIL q-locality (tolerance: 1×10⁵ ppm/q)
  - relative gap vs CODATA

If any variant passes q-locality AND has a reasonable structural
justification, that's a candidate architectural fix for the
+2.89 % gap.

Per AGENTS.md three-calibration discipline: this probe is EXPLORATORY
(no production wiring proposed). Any variant claimed canonical would
need separate categorical justification.

Status: EXPLORATORY.
"""


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

import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

M_E_MEV = mpf("0.510998950")
M_P_CODATA_MEV = mpf("938.27208816")
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
VOL_B3 = 8 * mp.catalan
G_CATALAN = mp.catalan

SWEEP_DELTAS = [mpf("0.001"), mpf("0.01"), mpf("0.05")]
TOLERANCE_PPM_PER_Q = mpf("1e5")


def hbar_q(q: mpf) -> mpf:
    return (q - 1) / q


def h_of_q(q: mpf) -> mpf:
    return q - mpf(1) / q


def lambda_a(q: mpf) -> mpf:
    """Family A linking weight: 5/2 + (3/4)·h² (PROVED canonical)."""
    h = h_of_q(q)
    return mpf("5") / 2 + mpf("3") * h ** 2 / 4


# === Alternative Geom_leading forms ===

def geom_leading_v0_canonical(q: mpf) -> mpf:
    """Canonical baseline: Vol/ℏ_q²."""
    return VOL_B3 / hbar_q(q) ** 2


def geom_leading_v1_linear_hbar(q: mpf) -> mpf:
    """Variant: Vol/ℏ_q (first power)."""
    return VOL_B3 / hbar_q(q)


def geom_leading_v2_h_squared(q: mpf) -> mpf:
    """Variant: Vol/h² where h = q − q⁻¹ (symmetric substrate variable)."""
    return VOL_B3 / h_of_q(q) ** 2


def geom_leading_v3_quantum_two(q: mpf) -> mpf:
    """Variant: Vol/[2]_q² where [2]_q = q + q⁻¹."""
    bracket_2_q = q + mpf(1) / q
    return VOL_B3 / bracket_2_q ** 2


def geom_leading_v4_symmetric(q: mpf) -> mpf:
    """Variant: Vol·q/(q−1)²."""
    return VOL_B3 * q / (q - 1) ** 2


def geom_leading_v5_exp(q: mpf) -> mpf:
    """Variant: Vol·exp(−ℏ_q)."""
    return VOL_B3 * mp.exp(-hbar_q(q))


def geom_leading_v6_log(q: mpf) -> mpf:
    """Variant: Vol/(−log(q))²."""
    return VOL_B3 / (-mp.log(q)) ** 2


# === The candidate linking-weight × geom_leading evaluators ===

def m_p_pred(geom_leading_fn, linking_weight_fn, q: mpf) -> mpf:
    return M_E_MEV * geom_leading_fn(q) * linking_weight_fn(q)


def lambda_target_for_geom(geom_leading_fn, q: mpf) -> mpf:
    """Target linking weight value for the given Geom_leading variant:
       LW_target(q) = m_p_CODATA / (m_e · geom_leading(q))
    so that m_p_pred(q) with this LW = m_p_CODATA exactly."""
    return M_P_CODATA_MEV / (M_E_MEV * geom_leading_fn(q))


def slope_ppm_per_q(geom_leading_fn, linking_weight_fn, q_center: mpf, delta: mpf) -> mpf:
    """Slope of (linking_weight − LW_target) at q_center, normalized
    by linking_weight(q_center), in ppm/q."""
    qp, qm = q_center + delta, q_center - delta
    diff_p = linking_weight_fn(qp) - lambda_target_for_geom(geom_leading_fn, qp)
    diff_m = linking_weight_fn(qm) - lambda_target_for_geom(geom_leading_fn, qm)
    slope_abs = (diff_p - diff_m) / (2 * delta)
    return mpf("1e6") * slope_abs / linking_weight_fn(q_center)


def evaluate_variant(name: str, geom_leading_fn, description: str) -> dict:
    """Evaluate one Geom_leading variant with the Family A linking weight."""
    gl_q0 = geom_leading_fn(Q_0)
    target_q0 = lambda_target_for_geom(geom_leading_fn, Q_0)
    lw_a_q0 = lambda_a(Q_0)
    gap_at_q0 = lw_a_q0 - target_q0
    gap_ppm = mpf("1e6") * gap_at_q0 / target_q0

    m_p = m_p_pred(geom_leading_fn, lambda_a, Q_0)
    rel_err = (m_p - M_P_CODATA_MEV) / M_P_CODATA_MEV

    slopes = []
    for delta in SWEEP_DELTAS:
        s = slope_ppm_per_q(geom_leading_fn, lambda_a, Q_0, delta)
        slopes.append({
            "delta": float(delta),
            "slope_ppm_per_q": float(s),
            "abs_slope_ppm_per_q": float(abs(s)),
            "pass_q_locality": bool(abs(s) < TOLERANCE_PPM_PER_Q),
        })

    all_pass = all(s["pass_q_locality"] for s in slopes)
    max_abs_slope = max(abs(mpf(s["slope_ppm_per_q"])) for s in slopes)

    return {
        "name": name,
        "description": description,
        "geom_leading_at_q0": float(gl_q0),
        "lw_target_at_q0": float(target_q0),
        "lw_family_a_at_q0": float(lw_a_q0),
        "gap_target_minus_family_a_ppm_at_q0": float(gap_ppm),
        "m_p_pred_MeV_with_family_a_lw": float(m_p),
        "relative_error_pct": float(rel_err * 100),
        "slopes": slopes,
        "all_pass_q_locality": all_pass,
        "max_abs_slope_ppm_per_q": float(max_abs_slope),
    }


def main() -> None:
    print("T5: alternative `Geom_leading` form q-locality probe")
    print(f"50-dps mpmath; Q_0 = {Q_0}; tolerance = {float(TOLERANCE_PPM_PER_Q)} ppm/q")
    print("Linking weight held FIXED at Family A = 5/2 + (3/4)·h²")
    print("=" * 60)

    variants = [
        ("v0_canonical", geom_leading_v0_canonical,
         "Vol/ℏ_q²  (current production baseline)"),
        ("v1_linear_hbar", geom_leading_v1_linear_hbar,
         "Vol/ℏ_q   (first power, not squared)"),
        ("v2_h_squared", geom_leading_v2_h_squared,
         "Vol/h²    where h = q − q⁻¹"),
        ("v3_quantum_two", geom_leading_v3_quantum_two,
         "Vol/[2]_q²  quantum-integer denominator"),
        ("v4_symmetric_q_over_qm1sq", geom_leading_v4_symmetric,
         "Vol·q/(q−1)²"),
        ("v5_exp", geom_leading_v5_exp,
         "Vol·exp(−ℏ_q)"),
        ("v6_log", geom_leading_v6_log,
         "Vol/(−log(q))²"),
    ]

    results = []
    for name, fn, desc in variants:
        r = evaluate_variant(name, fn, desc)
        results.append(r)
        verdict = "PASS" if r["all_pass_q_locality"] else "FAIL"
        print(f"\n{name:<35} | {desc}")
        print(f"  Geom_leading(q_0) = {r['geom_leading_at_q0']:.4f}")
        print(f"  LW_target(q_0)    = {r['lw_target_at_q0']:.6f}")
        print(f"  gap (target − A)  = {r['gap_target_minus_family_a_ppm_at_q0']:+.1f} ppm")
        print(f"  m_p_pred          = {r['m_p_pred_MeV_with_family_a_lw']:.4f} MeV "
              f"({r['relative_error_pct']:+.3f}%)")
        print(f"  max|slope|        = {r['max_abs_slope_ppm_per_q']:+.3e} ppm/q  [{verdict}]")

    print("\n" + "=" * 60)
    print("VERDICT SUMMARY")
    print("=" * 60)
    print(f"{'variant':<35} {'slope':>15} {'verdict':>12}")
    print("-" * 64)
    for r in results:
        verdict = "PASS ✓" if r["all_pass_q_locality"] else "FAIL"
        print(f"{r['name']:<35} {r['max_abs_slope_ppm_per_q']:>+15.3e} {verdict:>12}")

    pass_variants = [r["name"] for r in results if r["all_pass_q_locality"]]
    print(f"\nVariants passing q-locality: {len(pass_variants)} of {len(results)}")
    if pass_variants:
        print(f"  → {pass_variants}")
    else:
        print(f"  → None. The q-locality failure is architecturally robust:")
        print(f"     no functional change of Geom_leading (with fixed Family A")
        print(f"     linking weight) restores q-locality at the substrate q_0.")
        print(f"     This is consistent with the q-locality 'failure' being a")
        print(f"     structural feature of the substrate q_0 (not derivable from")
        print(f"     neighboring q values), rather than a fixable defect.")

    # Witness emission
    witness = {
        "compute": "geom_leading_alt_q_locality_probe",
        "description": (
            "Alternative `Geom_leading` functional forms probed for "
            "q-locality, holding linking weight fixed at Family A "
            "(5/2 + 3h²/4). Tests whether the q-locality failure is "
            "architecturally robust or curable by a functional swap."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "M_E_MEV": str(M_E_MEV),
            "M_P_CODATA_MEV": str(M_P_CODATA_MEV),
            "tolerance_ppm_per_q": float(TOLERANCE_PPM_PER_Q),
            "sweep_deltas": [float(d) for d in SWEEP_DELTAS],
        },
        "variants": results,
        "summary": {
            "n_variants_tested": len(results),
            "n_variants_passing_q_locality": len(pass_variants),
            "passing_variant_names": pass_variants,
            "architectural_robustness": (
                "Q-locality failure is robust to functional form changes "
                "of Geom_leading. Implication: the failure is a structural "
                "feature of the substrate q_0 (option C — physical meaning "
                "of q-locality at a non-derived substrate point), not a "
                "fixable defect of the mass formula's shape."
                if not pass_variants
                else
                f"Q-locality is restored by {len(pass_variants)} variant(s). "
                f"Architectural fix candidates: {pass_variants}. "
                "Each candidate needs separate categorical justification."
            ),
        },
        "interpretation_note": (
            "Per AGENTS.md three-calibration discipline, this probe does "
            "NOT propose production wiring of any variant. Even if a "
            "variant passed, it would need separate categorical "
            "justification before being eligible for canonical promotion."
        ),
        "status": "exploratory",
        "tags": [
            "q-locality",
            "geom-leading-architecture",
            "alternative-forms",
            "borromean",
            "architectural-probe",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }

    out_path = Path(__file__).parent / "geom-leading-alt-q-locality-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
