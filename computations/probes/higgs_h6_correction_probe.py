"""Probe: does the residual ~0.5% in the Higgs formula come from h^6 corrections?

The categorical Higgs mass formula (PR #1159) gives:
  predicted from m_W: 124.26 GeV (dev -0.67% from m_H = 125.10)
  predicted from m_Z: 125.64 GeV (dev +0.44%)

Both within 1% but NOT exact. If the structural form is correct, the
residual should come from higher-order Yekutieli MI corrections at
k = 3 (h^6) or higher.

This probe:
1. Computes the required h^6 correction coefficient to close the
   W and Z anchored predictions to m_H exactly
2. Tests if the required coefficient has clean substrate-natural form

The reframed extended formula:
  m_H = m_W · (P_4/P_2) · (6/5) · (1 - h^4·2G) · (1 + h^6·C_6)

Solving for C_6 from m_W anchor:
  C_6 = (m_H/predicted_no_h6 - 1) / h^6

If a clean structural C_6 matches the W and Z anchors consistently,
the formula closes within numerical precision at h^6.

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
from math import comb
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0
G_CATALAN = mp.catalan
VOL_B3 = 8 * G_CATALAN

M_W_GEV = mpf("80.379")
M_Z_GEV = mpf("91.1876")
M_H_GEV = mpf("125.10")


def trace_polynomial(m: int, h: mpf) -> mpf:
    return sum(mpf(comb(m + j, 2 * j)) / 2 * h ** (2 * j) for j in range(m + 1))


def main():
    print("=" * 80)
    print("Higgs formula residual: does h^6 close the ~0.5% gap?")
    print("=" * 80)

    P_2 = trace_polynomial(2, H_0)
    P_3 = trace_polynomial(3, H_0)
    P_4 = trace_polynomial(4, H_0)
    six_fifths = mpf(6) / 5
    h4_correction = 1 - H_0 ** 4 * VOL_B3 / 4
    base = six_fifths * h4_correction

    print(f"h_0 = {float(H_0):.10f}")
    print(f"h_0^4 = {float(H_0 ** 4):.10f}")
    print(f"h_0^6 = {float(H_0 ** 6):.10f}")
    print(f"(6/5)·(1-h^4·2G) = {float(base):.10f}")
    print()

    # Predictions without h^6 correction
    m_H_no_h6_from_W = M_W_GEV * (P_4 / P_2) * base
    m_H_no_h6_from_Z = M_Z_GEV * (P_4 / P_3) * base

    # Required h^6 correction to close exactly
    factor_W = M_H_GEV / m_H_no_h6_from_W
    factor_Z = M_H_GEV / m_H_no_h6_from_Z

    # If correction is (1 + h^6 · C_6), then C_6 = (factor - 1) / h^6
    C_6_from_W = (factor_W - 1) / H_0 ** 6
    C_6_from_Z = (factor_Z - 1) / H_0 ** 6

    print(f"Predictions WITHOUT h^6 correction:")
    print(f"  from m_W: {float(m_H_no_h6_from_W):.6f} GeV (dev {float((m_H_no_h6_from_W - M_H_GEV)/M_H_GEV*100):+.4f}%)")
    print(f"  from m_Z: {float(m_H_no_h6_from_Z):.6f} GeV (dev {float((m_H_no_h6_from_Z - M_H_GEV)/M_H_GEV*100):+.4f}%)")
    print()
    print(f"Required h^6 correction coefficients (assuming form 1 + h^6 · C_6):")
    print(f"  from m_W: C_6 = {float(C_6_from_W):.4f}")
    print(f"  from m_Z: C_6 = {float(C_6_from_Z):.4f}")
    print(f"  difference: {float(C_6_from_W - C_6_from_Z):.4f}")
    print()

    if abs(float(C_6_from_W - C_6_from_Z)) > 50:
        print("  → Required C_6 values DIFFER significantly between W and Z anchors")
        print("  → The residual is NOT consistent with a simple h^6 correction")
        print("    (would need a more complex form, or h^6 isn't the right order)")
    else:
        print("  → Required C_6 values are CONSISTENT — h^6 correction structure likely")

    # Average C_6 to get a target
    C_6_target = (C_6_from_W + C_6_from_Z) / 2
    print(f"  Average C_6 (target): {float(C_6_target):.4f}")
    print()

    # Test substrate-natural candidates for C_6
    print("=" * 80)
    print(f"Searching for substrate-natural C_6 ≈ {float(C_6_target):.4f}")
    print("=" * 80)

    C_6_candidates = [
        ("Vol(B_3)² / h_0 ≈ ?", VOL_B3 ** 2 / H_0),
        ("Vol(B_3) · G ≈ ?", VOL_B3 * G_CATALAN),
        ("2G · π ≈ 5.75", 2 * G_CATALAN * mp.pi),
        ("π²", mp.pi ** 2),
        ("(2G)² ≈ 3.36", (2 * G_CATALAN) ** 2),
        ("4 · 2G ≈ 7.33", 4 * 2 * G_CATALAN),
        ("Vol(B_3) ≈ 7.33", VOL_B3),
        ("Vol(B_3) · h_0 ≈ 1.53", VOL_B3 * H_0),
        ("π² · h_0 ≈ 2.06", mp.pi ** 2 * H_0),
        ("11 (matching 11/6 alt from h^4 probe)", mpf(11)),
        ("3·π ≈ 9.42", 3 * mp.pi),
        ("2π · G ≈ 5.75", 2 * mp.pi * G_CATALAN),
        ("4G·π ≈ 11.51", 4 * G_CATALAN * mp.pi),
        ("16G ≈ 14.66", 16 * G_CATALAN),
        ("π²/G ≈ 10.77", mp.pi ** 2 / G_CATALAN),
        ("(P_4 · 5)/h_0 ≈ ?", P_4 * 5 / H_0),
    ]
    print(f"{'candidate C_6':<45} {'value':>14} {'dev':>14}")
    print("-" * 75)
    results = []
    for label, val in C_6_candidates:
        dev = float((val - C_6_target) / C_6_target * 100)
        marker = "  ★★★ <5%" if abs(dev) < 5 else "  ★★ <20%" if abs(dev) < 20 else ""
        print(f"{label:<45} {float(val):>14.4f} {dev:>+13.2f}%{marker}")
        results.append({"label": label, "value": float(val), "dev_pct": dev})

    sorted_results = sorted(results, key=lambda r: abs(r["dev_pct"]))
    print("\n" + "=" * 80)
    print("BEST 5 matches:")
    print("=" * 80)
    for i, r in enumerate(sorted_results[:5]):
        print(f"  {i+1}. {r['label']:<45} dev = {r['dev_pct']:+.2f}%")

    # Verify cross-anchor consistency with best match
    best = sorted_results[0]
    if abs(best["dev_pct"]) < 5:
        print(f"\n✓ Best candidate {best['label']} = {best['value']:.4f}")
        print(f"  Refined formula: m_H = m_W · (P_4/P_2) · (6/5) · (1-h^4·2G) · (1+h^6·C_6)")
        C_6_best = mpf(best["value"])
        h6_factor = 1 + H_0 ** 6 * C_6_best
        m_H_with_h6_W = m_H_no_h6_from_W * h6_factor
        m_H_with_h6_Z = m_H_no_h6_from_Z * h6_factor
        print(f"\n  Verification with C_6 = {best['value']}:")
        print(f"    From m_W: {float(m_H_with_h6_W):.6f} GeV (dev {float((m_H_with_h6_W - M_H_GEV)/M_H_GEV*100):+.4f}%)")
        print(f"    From m_Z: {float(m_H_with_h6_Z):.6f} GeV (dev {float((m_H_with_h6_Z - M_H_GEV)/M_H_GEV*100):+.4f}%)")
    else:
        print(f"\n✗ No close structural match for C_6 ≈ {float(C_6_target):.2f}")
        print(f"  The W/Z anchor inconsistency (Δ = {float(C_6_from_W - C_6_from_Z):.2f}) likely indicates")
        print(f"  the residual has multiple terms, not a single h^6 coefficient")

    # Witness
    witness = {
        "compute": "higgs_h6_correction_probe",
        "description": (
            "Probes whether residual ~0.5% in Higgs categorical formula "
            "(PR #1159) closes via h^6-order correction with structural "
            "coefficient. Solves for required C_6 from W and Z anchors; "
            "tests substrate-natural candidates."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "VOL_B3": str(VOL_B3),
        },
        "predictions_without_h6": {
            "from_W_GeV": float(m_H_no_h6_from_W),
            "from_Z_GeV": float(m_H_no_h6_from_Z),
            "measured_GeV": float(M_H_GEV),
            "dev_W_pct": float((m_H_no_h6_from_W - M_H_GEV) / M_H_GEV * 100),
            "dev_Z_pct": float((m_H_no_h6_from_Z - M_H_GEV) / M_H_GEV * 100),
        },
        "required_C_6": {
            "from_W": float(C_6_from_W),
            "from_Z": float(C_6_from_Z),
            "average_target": float(C_6_target),
            "anchor_difference": float(C_6_from_W - C_6_from_Z),
            "anchors_consistent": bool(abs(float(C_6_from_W - C_6_from_Z)) < 50),
        },
        "candidates": results,
        "best_match": best,
        "verdict": (
            f"Best candidate: {best['label']} = {best['value']:.4f}, "
            f"dev {best['dev_pct']:+.2f}% from required"
        ),
        "interpretation": (
            "If a clean substrate-natural C_6 matches AND W/Z anchors give "
            "consistent C_6, the residual is structurally closed at h^6. "
            "If anchors differ significantly, the residual has more complex "
            "structure (anchor-dependent corrections, or h^6 isn't the "
            "right order)."
        ),
        "status": "exploratory",
        "tags": [
            "higgs-mass-formula",
            "h6-correction",
            "categorical-residual",
            "cross-anchor-consistency",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "higgs-h6-correction-probe.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
