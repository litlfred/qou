"""Investigate whether 171/143 - 6/5 deviation has structural meaning at h^4 order.

PR #1154 found NEGATIVE: no clean cardinality ratio matches 171/143
exactly. But the deviation 6/5 → 171/143 is exactly:
    171/143 / (6/5) = 0.99650...
    deviation = 1 - 0.99650 = 0.00350

If this is a h^4-order correction (not noise), then:
    171/143 = (6/5) · (1 - h_0^4 · C)
for some categorical constant C.

At h_0 = 0.20856: h_0^4 = 0.00189.
Solving: C = 0.00350 / 0.00189 = 1.851

This probe tests if 1.851 has a clean substrate-natural form, e.g.,
1 + 4·h_0 ≈ 1.834 or √π ≈ 1.772.

If a clean structural C matches, the 0.35% "noise" reframes as a
LEADING h^4-CORRECTION term, validating the categorical interpretation.

Status: EXPLORATORY (structural-deviation analysis).
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
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0          # ≈ 0.20856
HBAR_Q = (Q_0 - 1) / Q_0           # ≈ 0.0989
VOL_B3 = 8 * mp.catalan            # ≈ 7.328
G_CATALAN = mp.catalan             # ≈ 0.9160

TARGET = mpf("171") / mpf("143")        # ≈ 1.1958
HYPO_6_5 = mpf("6") / mpf("5")           # = 1.2

# Required correction factor
CORRECTION_NEEDED = TARGET / HYPO_6_5     # ≈ 0.99650
DELTA = 1 - CORRECTION_NEEDED             # ≈ 0.00350

# If delta = h_0^4 · C, then C = delta / h_0^4
C_REQUIRED = DELTA / H_0 ** 4

print(f"Target:      171/143 = {float(TARGET):.10f}")
print(f"Hypothesis:  6/5 = {float(HYPO_6_5):.10f}")
print(f"Ratio:       (171/143)/(6/5) = {float(CORRECTION_NEEDED):.10f}")
print(f"Deviation:   δ = 1 - ratio = {float(DELTA):.10f}")
print()
print(f"h_0^4 = {float(H_0 ** 4):.10f}")
print(f"If δ = h_0^4 · C, then C = {float(C_REQUIRED):.10f}")
print()
print("Searching for substrate-natural C ≈", float(C_REQUIRED))
print("=" * 80)

# Candidate substrate-natural values for C
C_CANDIDATES = [
    ("1 + 4·h_0 (≈1.834)",          1 + 4 * H_0),
    ("1 + 2·√h_0",                   1 + 2 * mp.sqrt(H_0)),
    ("√(π) (≈1.772)",                mp.sqrt(mp.pi)),
    ("π/√(π-1) (≈2.21)",             mp.pi / mp.sqrt(mp.pi - 1)),
    ("2·G (Catalan) ≈ 1.832",         2 * G_CATALAN),
    ("φ + h_0 ≈ 1.827",              (mp.sqrt(5) + 1) / 2 + H_0),
    ("e/√2 ≈ 1.922",                  mp.e / mp.sqrt(2)),
    ("√(π · h_0) · π (≈1.85)",        mp.sqrt(mp.pi * H_0) * mp.pi),
    ("Vol(B_3)/4 ≈ 1.832",            VOL_B3 / 4),
    ("4 · h_0 · π ≈ 2.62",            4 * H_0 * mp.pi),
    ("[3]_q at q_0",                  (Q_0 ** 3 - Q_0 ** (-3)) / (Q_0 - 1/Q_0)),
    ("[2]_q² / 2 at q_0 ≈ 2.21",      ((Q_0 + 1/Q_0) ** 2) / 2),
    ("1 + h_0 + √h_0 ≈ 1.66",         1 + H_0 + mp.sqrt(H_0)),
    ("2 - h_0/√2 ≈ 1.853",            2 - H_0 / mp.sqrt(2)),
    ("π · h_0² (≈0.137)",             mp.pi * H_0 ** 2),
    ("π/√(3) ≈ 1.814",                mp.pi / mp.sqrt(3)),
    ("11/6 (≈1.833)",                 mpf(11) / 6),
    ("log(6.36) ≈ 1.85",              mp.log(mpf("6.36"))),
    ("2 · sin(2π/5) ≈ 1.902",         2 * mp.sin(2 * mp.pi / 5)),
    ("π · cos(θ_W) ≈ 2.77",           mp.pi * mpf("0.8815")),
]

print(f"{'candidate C':<45} {'value':>14} {'dev from required':>18}")
print("-" * 80)
results = []
for label, val in C_CANDIDATES:
    dev_pct = (float(val) - float(C_REQUIRED)) / float(C_REQUIRED) * 100
    marker = "  ★★★ MATCH <1%" if abs(dev_pct) < 1 else "  ★★ <3%" if abs(dev_pct) < 3 else "  ★ <10%" if abs(dev_pct) < 10 else ""
    print(f"{label:<45} {float(val):>14.6f} {dev_pct:>+17.3f}%{marker}")
    results.append({
        "label": label,
        "value": float(val),
        "deviation_pct_from_required": dev_pct,
    })

# Best match
sorted_results = sorted(results, key=lambda r: abs(r["deviation_pct_from_required"]))
print("\n" + "=" * 80)
print("BEST 5 (by abs deviation from required C):")
print("=" * 80)
for i, r in enumerate(sorted_results[:5]):
    print(f"  {i+1}. {r['label']:<45} dev = {r['deviation_pct_from_required']:+.3f}%")

best = sorted_results[0]
print("\n" + "=" * 80)
print("VERDICT — reframing 0.35% deviation as structural h^4 correction")
print("=" * 80)
if abs(best["deviation_pct_from_required"]) < 1:
    print(f"✓ {best['label']} gives required C within 1%.")
    print(f"  Reframed identity: 171/143 = (6/5) · (1 - h_0^4 · {best['label']})")
    print(f"  Verify: predicted = (6/5) · (1 - h_0^4 · {best['value']:.4f}) = ")
    pred = (mpf(6) / 5) * (1 - H_0 ** 4 * mpf(str(best["value"])))
    print(f"    {float(pred):.10f}")
    print(f"  Target: {float(TARGET):.10f}")
    print(f"  Match: {(float(pred) - float(TARGET)) / float(TARGET) * 100:+.4f}%")
elif abs(best["deviation_pct_from_required"]) < 5:
    print(f"~ {best['label']} gives required C within 5% — suggestive but not conclusive.")
else:
    print(f"✗ Best match {best['label']} is off by {best['deviation_pct_from_required']:.1f}%.")
    print(f"  The 0.35% deviation does NOT have a clean substrate-natural h^4 correction.")
    print(f"  Either (a) the deviation IS measurement noise, OR")
    print(f"  (b) the correction is at higher h-order (h^6, h^8) with a complex coefficient")

# Test: maybe the correction is at h^2 or h^6 order instead?
print("\n" + "=" * 80)
print("Alternative: maybe correction is at h^2 or h^6 order?")
print("=" * 80)
for order_label, order_val in [("h^2", H_0 ** 2), ("h^4", H_0 ** 4), ("h^6", H_0 ** 6), ("ℏ_q²", HBAR_Q ** 2)]:
    c_required_this_order = DELTA / order_val
    print(f"  If δ = {order_label} · C, then C = {float(c_required_this_order):.6f}")
    for simple_label, simple_val in [
        ("1", mpf(1)),
        ("2", mpf(2)),
        ("π", mp.pi),
        ("G", G_CATALAN),
        ("4G", 4 * G_CATALAN),
        ("[2]_q", Q_0 + 1/Q_0),
        ("11/6", mpf(11)/6),
        ("Vol(B_3)/4 ≈ 1.832", VOL_B3 / 4),
        ("Vol(B_3) ≈ 7.33", VOL_B3),
        ("Vol(B_3) · 2", 2 * VOL_B3),
        ("Vol(B_3)/h_0 ≈ 35.1", VOL_B3 / H_0),
    ]:
        sv = float(simple_val)
        diff_pct = (sv - float(c_required_this_order)) / float(c_required_this_order) * 100
        if abs(diff_pct) < 3:
            print(f"    {simple_label} = {sv:.4f} matches required ({diff_pct:+.2f}%)")

# Final verdict + witness
print("\n" + "=" * 80)
print("FINAL VERDICT")
print("=" * 80)
print(f"Required C at h^4 order: {float(C_REQUIRED):.6f}")
print(f"Best substrate-natural match: {best['label']} = {best['value']:.6f}")
print(f"  ({best['deviation_pct_from_required']:+.3f}% from required)")

witness = {
    "compute": "six_fifths_deviation_h4_correction_probe",
    "description": (
        "Investigates whether the 0.35% deviation between 171/143 and "
        "6/5 has structural meaning as a h^4-order correction. "
        "If 171/143 = 6/5 · (1 - h_0^4 · C), seeks substrate-natural C."
    ),
    "parameters": {
        "precision": "mpfr",
        "dps": 50,
        "Q_0": str(Q_0),
        "H_0": str(H_0),
        "TARGET": str(TARGET),
        "HYPO_6_5": str(HYPO_6_5),
        "DELTA": float(DELTA),
        "h0_to_4": float(H_0 ** 4),
        "C_REQUIRED": float(C_REQUIRED),
    },
    "candidates": results,
    "best_match": best,
    "verdict": (
        f"Best match {best['label']} differs from required C by {best['deviation_pct_from_required']:+.3f}%"
    ),
    "interpretation": (
        "If a clean substrate-natural C (matching to <1%) is found, the "
        "0.35% deviation is reframed as a structural h^4 correction and "
        "the 6/5 hypothesis becomes the LEADING-ORDER prediction. "
        "Otherwise, the deviation remains attributable to measurement "
        "noise or higher-order corrections."
    ),
    "status": "exploratory",
    "tags": [
        "deviation-structural-meaning",
        "h4-correction",
        "six-fifths-hypothesis",
        "leading-order-vs-noise",
    ],
    "scriptCommitSha": (
        subprocess.check_output(["git", "rev-parse", "HEAD"])
        .decode().strip()
    ),
}
out_path = Path(__file__).parent / "six-fifths-deviation-h4-correction-probe.witness.json"
out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
print(f"\nWitness: {out_path.relative_to(Path.cwd())}")
