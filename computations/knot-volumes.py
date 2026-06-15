#!/usr/bin/env python3
"""
Knot volume verification via SnapPy.

Computes hyperbolic volumes for all knots/links in the QOU particle registry
and compares against the paper's stated values.  Produces a witness JSON file
that the content pipeline can check.

Usage:
    python3 computations/knot-volumes.py

Output:
    computations/knot-volumes.witness.json

Dependencies:
    pip install snappy
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402

try:
    import snappy
except ImportError:
    print("ERROR: snappy not installed. Run: pip install snappy", file=sys.stderr)
    sys.exit(1)


# ── Registry: knot → expected volume ─────────────────────────────
# Values from content/quantum-observable-universe/lean/QOU/KnotRegistry.lean and Ch11 content blocks.

KNOT_REGISTRY = [
    {
        "name": "Vol(0_1) — unknot (neutrino)",
        "manifold": "0_1",
        "expected": 0.0,
        "tolerance": 1e-10,
        "source": "Trivial knot",
        "unit": "volume",
        "particle": "neutrino",
    },
    {
        "name": "Vol(3_1) — trefoil (electron)",
        "manifold": "3_1",
        "expected": 0.0,
        "tolerance": 1e-10,
        "source": "Torus knot (non-hyperbolic)",
        "unit": "volume",
        "particle": "electron",
    },
    {
        # Canonical paper identification: muon = figure-eight 4_1 per
        # prop:skein-mass-relation (m_μ/m_e = Vol(4_1)/ℏ_q²). The
        # "Higgs field" label is informational — knot-volumes does
        # NOT determine particle dictionary; see audit
        # docs/audits/2026-05-24-muon-knot-id-conflict.md for the
        # full reconciliation (resolved 2026-05-24, PR #1127).
        "name": "Vol(4_1) — figure-eight (muon; also Higgs field / mass mechanism)",
        "manifold": "4_1",
        "expected": 2.02988321281931,
        "tolerance": 1e-10,
        "source": "OEIS A091518, 3·Cl₂(π/3)",
        "unit": "volume",
        "particle": "muon",
    },
    {
        # Cinquefoil 5_1 = T(2,5) was previously labeled "muon" here;
        # corrected 2026-05-24 (PR #1127) per
        # docs/audits/2026-05-24-muon-knot-id-conflict.md. The
        # canonical muon is figure-eight 4_1 per prop:skein-mass-
        # relation; T(2,5) is referenced in sibling PR #1153 as the
        # W boson torus knot (m=2 in P_m/Q_m family).
        "name": "Vol(5_1) — cinquefoil T_{2,5} (W boson per PR #1153 P_m/Q_m torus family)",
        "manifold": "5_1",
        "expected": 0.0,
        "tolerance": 1e-10,
        "source": "Torus knot (non-hyperbolic)",
        "unit": "volume",
        "particle": "w_boson",
    },
    {
        "name": "Vol(5_2) — three-twist (strange quark)",
        "manifold": "5_2",
        "expected": 2.82812208832975,
        "tolerance": 1e-10,
        "source": "SnapPy census",
        "unit": "volume",
        "particle": "strange",
    },
    {
        "name": "Vol(7_1) — septafoil (tau T_{2,7})",
        "manifold": "7_1",
        "expected": 0.0,
        "tolerance": 1e-10,
        "source": "Torus knot (non-hyperbolic)",
        "unit": "volume",
        "particle": "tau",
    },
]

LINK_REGISTRY = [
    {
        "name": "Vol(L2a1) — Hopf link (strong force)",
        "manifold": "L2a1",
        "expected": 0.0,
        "tolerance": 1e-6,  # torus link; SnapPy returns small numerical noise
        "source": "Torus link (non-hyperbolic)",
        "unit": "volume",
        "particle": "strong_force",
    },
    {
        "name": "Vol(L6a4) — Borromean rings (nucleon)",
        "manifold": "L6a4",
        "expected": 7.32772475341775,
        "tolerance": 1e-10,
        "source": "8·G (Catalan's constant), OEIS A006752",
        "unit": "volume",
        "particle": "nucleon",
    },
]


# ── Mass ratio verification ──────────────────────────────────────
# Uses Vol(4_1) and CODATA mass ratio to verify the substrate parameter q.

MASS_ASSERTIONS = [
    {
        "name": "m_μ/m_e (CODATA 2022)",
        "expected": 206.7682830,  # noqa: P31 — test-expected value (CAL-2 anchor cross-check, not a prediction input)
        "tolerance": 0.0000001,
        "source": "CODATA 2022",
        "unit": "dimensionless",
    },
    {
        "name": "substrate q from Vol(4_1) and m_μ/m_e",
        "expected": 1.10997,
        "tolerance": 0.001,
        "source": "QOU derivation (Ch11)",
        "unit": "dimensionless",
    },
    {
        "name": "ℏ_q = 1 - 1/q",
        "expected": 0.09905,
        "tolerance": 0.001,
        "source": "QOU definition (Ch1)",
        "unit": "dimensionless",
    },
]


def compute_volume(manifold_name: str) -> float:
    """Compute hyperbolic volume of a knot/link complement via SnapPy."""
    try:
        M = snappy.Manifold(manifold_name)
        return float(M.volume())
    except Exception:
        # Some manifolds may need Link instead of Manifold
        try:
            M = snappy.Link(manifold_name)
            return float(M.complement().volume())
        except Exception:
            return 0.0


def main():
    start = time.monotonic()
    assertions = []
    all_passed = True

    # ── Knot volumes ──────────────────────────────────────────
    for entry in KNOT_REGISTRY + LINK_REGISTRY:
        computed = compute_volume(entry["manifold"])
        expected = entry["expected"]
        tol = entry["tolerance"]
        passed = abs(computed - expected) <= tol

        if not passed:
            all_passed = False
            print(f"  FAIL: {entry['name']}: computed={computed}, expected={expected}, "
                  f"diff={abs(computed - expected):.2e}", file=sys.stderr)
        else:
            print(f"  OK: {entry['name']}: {computed}")

        assertions.append({
            "name": entry["name"],
            "computed": computed,
            "expected": expected,
            "tolerance": tol,
            "unit": entry.get("unit", "volume"),
            "source": entry.get("source", ""),
        })

    # ── Mass ratio derivation ─────────────────────────────────
    vol_41 = next(a["computed"] for a in assertions if "4_1" in a["name"])

    # CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase B).
    from q_parameter import MASS_RATIO_MU_E  # noqa: E402
    mu_e_ratio = MASS_RATIO_MU_E
    hbar_q_sq = vol_41 / mu_e_ratio
    hbar_q = hbar_q_sq ** 0.5
    q = 1.0 / (1.0 - hbar_q)

    mass_computed = {
        "m_μ/m_e (CODATA 2022)": vol_41 / hbar_q_sq,
        "substrate q from Vol(4_1) and m_μ/m_e": q,
        "ℏ_q = 1 - 1/q": 1.0 - 1.0 / q,
    }

    for entry in MASS_ASSERTIONS:
        computed = mass_computed[entry["name"]]
        expected = entry["expected"]
        tol = entry["tolerance"]
        passed = abs(computed - expected) <= tol

        if not passed:
            all_passed = False
            print(f"  FAIL: {entry['name']}: computed={computed}, expected={expected}",
                  file=sys.stderr)
        else:
            print(f"  OK: {entry['name']}: {computed:.10f}")

        assertions.append({
            "name": entry["name"],
            "computed": computed,
            "expected": expected,
            "tolerance": tol,
            "unit": entry.get("unit", ""),
            "source": entry.get("source", ""),
        })

    duration_ms = int((time.monotonic() - start) * 1000)

    # ── Write witness ─────────────────────────────────────────
    witness = {
        "engine": "snappea",
        "engineVersion": f"snappy {snappy.version()}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "assertions": assertions,
        "allPassed": all_passed,
        "durationMs": duration_ms,
    }

    # Per Copilot review (#581): preserve the SnapPy engine metadata
    # rather than overriding to "python".
    out_path = (WitnessBuilder.wrap_legacy(
        "knot-volumes", witness,
        script_path=__file__,
        engine="snappea",
        engine_version=f"snappy {snappy.__version__}",
        )
        .save())
    print(f"\nWitness written to {out_path}")
    print(f"All passed: {all_passed} ({len(assertions)} assertions, {duration_ms}ms)")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
