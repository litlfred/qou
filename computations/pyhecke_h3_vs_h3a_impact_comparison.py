"""Pyhecke H_3 vs H_{3A} impact comparison — quantify the legacy bug.

Companion to PR #1238's audit + PR #1240's deprecation warning. This
script does NOT modify any production code; it COMPUTES the per-atom
difference between:

  Legacy (BUG):  atom_per_generator_volumes (H_3 weights, hardcoded)
  Proper:        per_generator_V_hat_3A     (H_{3A} weights, dynamic)

For atoms A = 1..6, computes both V̂_full lists and reports:
  - max |Δ| per atom (= maximum per-generator divergence)
  - relative error per atom
  - whether the H_3 bug is "small" or "large" for that atom

The goal: provide a numerical baseline showing the SCALE of impact,
so the full migration sweep (separate PR) has a measurable target.

HONEST FRAMING: this is a DIAGNOSTIC. It does NOT fix the bug; it
QUANTIFIES it.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import os
import subprocess
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Bootstrap pyhecke path (matches hecke_core.py pattern)
_PYHECKE_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "tools", "pyhecke", "python")
)
if os.path.isdir(_PYHECKE_PATH) and _PYHECKE_PATH not in sys.path:
    sys.path.insert(0, _PYHECKE_PATH)


def main():
    print("=" * 80)
    print("Pyhecke H_3 vs H_{3A} impact comparison (PR #1238 audit follow-up)")
    print("=" * 80)
    print()

    # Try to import both — gracefully report if either is unavailable
    legacy_avail = True
    proper_avail = True
    try:
        # Suppress the just-added DeprecationWarning for this comparison
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # Use hecke_core wrapper which sets q_int in the proper namespace
            from hecke_core import atom_per_generator_volumes
            from q_parameter import Q as Q0_FLOAT, Q_MP
    except Exception as e:
        print(f"  ⚠ Legacy import failed: {e}")
        legacy_avail = False

    try:
        from mass_at_3A_proper import per_generator_V_hat_3A
    except Exception as e:
        print(f"  ⚠ Proper import failed: {e}")
        proper_avail = False

    if not (legacy_avail and proper_avail):
        print()
        print("Cannot run comparison — exiting with diagnostic witness.")
        write_witness({"status": "import_failed",
                       "legacy_available": legacy_avail,
                       "proper_available": proper_avail})
        return

    # Test atoms: H, D, T, ³He, ⁴He, ⁶Li (Z, N pairs)
    test_atoms = [
        ("p",     1, 0),
        ("n",     0, 1),
        ("D",     1, 1),
        ("T",     1, 2),
        ("³He",   2, 1),
        ("⁴He",   2, 2),
        ("⁶Li",   3, 3),
    ]

    print(f"  {'atom':<8} {'A':>3} {'3A':>4} {'#gens':>6} {'|Δ_full|_max':>14}  {'rel %':>10}  flag")
    print(f"  {'-'*8} {'-'*3} {'-'*4} {'-'*6} {'-'*14}  {'-'*10}  ----")

    results = []
    for sym, Z, N in test_atoms:
        A = Z + N
        try:
            legacy_vols = atom_per_generator_volumes(Z, N, include_inter=True)
        except Exception as e:
            print(f"  {sym:<8} {A:>3} {3*A:>4}    ERROR (legacy): {e}")
            continue
        try:
            proper_vols = per_generator_V_hat_3A(Z, N)
        except Exception as e:
            print(f"  {sym:<8} {A:>3} {3*A:>4}    ERROR (proper): {e}")
            continue

        # Compare V_full per generator
        if len(legacy_vols) != len(proper_vols):
            print(f"  {sym:<8} length mismatch: legacy={len(legacy_vols)}, proper={len(proper_vols)}")
            continue

        delta_max = 0.0
        rel_max = 0.0
        for i, (leg, pro) in enumerate(zip(legacy_vols, proper_vols)):
            v_leg = float(leg.get("full", 0))
            v_pro = float(pro.get("full", 0))
            d = abs(v_leg - v_pro)
            r = d / max(abs(v_leg), 1e-30) * 100
            if d > delta_max:
                delta_max = d
                rel_max = r

        flag = ""
        if A == 1:
            flag = "(H_3 correct ✓)"
        elif delta_max < 1e-6:
            flag = "(small)"
        elif delta_max < 0.01:
            flag = "(moderate)"
        else:
            flag = "(LARGE)"

        results.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "n_gens": len(legacy_vols),
            "max_abs_delta": delta_max,
            "max_rel_pct": rel_max,
            "flag": flag,
        })

        print(f"  {sym:<8} {A:>3} {3*A:>4} {len(legacy_vols):>6} {delta_max:>14.6e}  {rel_max:>9.4f}%  {flag}")

    print()
    print("=" * 80)
    print("Honest interpretation")
    print("=" * 80)
    print()
    print("  - A = 1 atoms (p, n): legacy uses H_3 weights, which is CORRECT")
    print("    (the algebra IS H_3 for single-nucleon braid). Δ = 0 expected.")
    print()
    print("  - A > 1 atoms (D, T, ³He, ⁴He, ⁶Li, ...): legacy uses H_3 weights")
    print("    for the H_{3A} braid — wrong. Δ measures the bug's numerical impact.")
    print()
    print("  - The Δ values above are the SCALE of error in V̂_full per generator")
    print("    that propagates downstream into mass-formula predictions.")
    print()
    print("  Full migration sweep (separate PR) needs to:")
    print("    1. Update 15+ caller scripts to use per_generator_V_hat_3A")
    print("    2. Regenerate all affected witnesses")
    print("    3. Compare before/after PDG-difference for each atom")
    print()

    write_witness({
        "status": "comparison_complete",
        "legacy_available": True,
        "proper_available": True,
        "test_atoms": [
            {"sym": sym, "Z": Z, "N": N} for sym, Z, N in test_atoms
        ],
        "results": results,
        "interpretation": (
            "A = 1: legacy H_3 weights correct (Δ = 0 expected). "
            "A > 1: legacy uses wrong H_3 weights for H_{3A} braid; "
            "Δ measures bug's per-generator V̂_full impact. "
            "Downstream mass-formula predictions inherit this error."
        ),
        "next_steps": (
            "Full migration sweep (separate PR): "
            "(1) update 15+ caller scripts to use per_generator_V_hat_3A; "
            "(2) regenerate affected witnesses; "
            "(3) compare before/after PDG-difference per atom."
        ),
    })


def write_witness(payload):
    payload["compute"] = "pyhecke_h3_vs_h3a_impact_comparison"
    payload["description"] = (
        "Diagnostic comparison of legacy atom_per_generator_volumes (H_3 "
        "weights) vs proper per_generator_V_hat_3A (H_{3A} weights) for "
        "atoms A = 1..6. Companion to PR #1238 audit. Quantifies the "
        "legacy bug's per-generator V̂_full impact."
    )
    payload["scriptCommitSha"] = (
        subprocess.check_output(["git", "rev-parse", "HEAD"])
        .decode().strip()
    )
    payload["tags"] = [
        "pyhecke-h3-vs-h3a",
        "impact-quantification",
        "pr-1238-followup",
        "migration-prep",
    ]
    payload["status"] = "exploratory"
    out_path = Path(__file__).parent / "pyhecke-h3-vs-h3a-impact-comparison.witness.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"  Witness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
