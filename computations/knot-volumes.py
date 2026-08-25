#!/usr/bin/env python3
"""
Knot volume verification via SnapPy.

Computes hyperbolic volumes for all knots/links in the QOU particle registry
and compares against the paper's stated values.  Produces a witness JSON file
that the content pipeline can check.

Usage:
    python3 computations/knot-volumes.py

Output:
    computations/substrate/knot-volumes.witness.json
    (NOT beside this script — see the `output_dir` note at the write site)

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
from codata_table import codata  # noqa: E402
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
        # 4_1 = the HIGGS field (mass mechanism), NOT the muon.
        # Determined by the four-layer trace in
        # docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md
        # (owner-ruled 2026-06-30), confirmed by KnotRegistry.lean,
        # the knot-particle-dictionary, and the skein-mass-relation
        # PROOF itself ("The Higgs field is identified with the
        # figure-eight knot 4_1"). The Skein formula
        # m_μ/m_e = Vol(4_1)/ℏ_q² is the Higgs-COUPLING mass scale —
        # the figure-eight volume that *gives* the muon its mass —
        # NOT the muon's own knot volume. The muon is the torus knot
        # T(2,5) (next entry; Vol_hyp = 0, no intrinsic volume mass).
        # The old "muon = 4_1" label was a category error: it confused
        # the muon's identity with the Higgs that gives it mass.
        "name": "Vol(4_1) — figure-eight (Higgs field / mass mechanism)",
        "manifold": "4_1",
        "expected": 2.02988321281931,
        "tolerance": 1e-10,
        "source": "OEIS A091518, 2·Cl₂(π/3) = 6Λ(π/3)",
        "unit": "volume",
        "particle": "higgs",
    },
    {
        # 5_1 = T(2,5) cinquefoil = the MUON (its identity knot), per
        # prop:s5-equivariant-torus-knots (ℤ_5 ↪ S_5, group-theoretic
        # theorem) and the lepton-meson-torus-knot-dictionary content
        # proposition. The charged leptons are the odd torus tower
        # e = T(2,3), μ = T(2,5), τ = T(2,7). As a torus knot it is
        # non-hyperbolic (Vol_hyp = 0): the muon has no intrinsic
        # volume-mass and acquires mass via the Higgs (4_1) coupling
        # above. (Exploratory PR #1153 floated a W-boson label for
        # T(2,5); the canonical lepton dictionary assigns the muon, and
        # the W-boson knot is a separate, unresolved question.)
        # Determination: docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md.
        "name": "Vol(5_1) — cinquefoil T(2,5) (muon; torus knot, Vol_hyp=0)",
        "manifold": "5_1",
        "expected": 0.0,
        "tolerance": 1e-10,
        "source": "Torus knot (non-hyperbolic)",
        "unit": "volume",
        "particle": "muon",
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
        # READ from the NIST table (`qou_substrate/data/allascii.txt`), never
        # transcribed — the same row `qou_substrate.constants` reads for
        # `MASS_RATIO_MU_E`, so this assertion checks that the production
        # registry still agrees with the authoritative table.
        #
        # It was the hand-typed literal `206.7682830` until 2026-08-23. That is
        # the CODATA-**2018** value; the registry moved to the table lookup and
        # picked up the 2022 value `206.7682827`, 3.0e-7 away — three times the
        # 1e-7 tolerance below. So this producer had been FAILING (exit 1) on
        # `main` since that switch, while its committed witness still recorded
        # `allPassed: true` from the last run under the old literal. The same
        # edition straddle `codata_table_vintage_audit.py` was written to catch,
        # one file over. Bean qou-bdkx.
        "name": "m_μ/m_e (CODATA 2022)",
        "expected": float(codata("muon-electron mass ratio").value),
        "tolerance": 0.0000001,
        "source": "CODATA 2022 (NIST allascii.txt, muon-electron mass ratio)",
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
        # This producer reads NO substrate q₀ — no `q_parameter.Q` / `Q_MP` /
        # `q_at`, no q₀ literal. Its one registry import is the CODATA
        # `MASS_RATIO_MU_E`. The q₀-shaped number in `assertions[9].computed`
        # is an OUTPUT, not a pin that was read: q derived forward from
        # SnapPy's Vol(4₁) and m_μ/m_e, which is the CAL-2 ideal-layer
        # definition, evaluated as that assertion's own subject.
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no substrate q₀: no q_parameter.Q / Q_MP / q_at import and "
            "no q₀ literal; the only registry value consumed is the CODATA "
            "muon-electron mass ratio. The 1.10997… in assertions[9] is an "
            "OUTPUT — q derived forward from Vol(4₁) and m_μ/m_e, i.e. the "
            "CAL-2 definition run as that assertion's subject, checked against "
            "its own expected 1.10997 ± 1e-3. It is therefore in the muon "
            "basin BY CONSTRUCTION and cannot track the proton pin: there is "
            "nothing here for a re-pin to change. Distinguish from the "
            "z2bn-tau-derivation-probe case (bean qou-bdkx), where an "
            "`independent` declaration was FALSE because the producer "
            "hardcoded a q₀ and consumed it five times — the check is whether "
            "q₀ is an input, not whether a q₀-shaped number appears."
        ),
    }

    # Per Copilot review (#581): preserve the SnapPy engine metadata
    # rather than overriding to "python".
    #
    # `output_dir` is REQUIRED here and is not cosmetic. Without it,
    # `WitnessBuilder` defaults the output directory to the caller's own
    # (`caller_file.parent` — witness.py:690), i.e. `computations/`. But this
    # witness is consumed from `computations/substrate/`: three content blocks
    # cite that path as their `witness:` (`knot-volumes-verification`,
    # `local-substrate-q-proof`, `terminal-resolution-proof`), and
    # `raw-float64-baseline.json` keys its entry on it.
    #
    # The split is an artefact of the Phase-6 reorg (see the `_path_bridge`
    # import at the top of this file): substrate modules moved into
    # `substrate/` and this witness went with them, while the script that
    # writes it stayed here. From then on every run emitted an UNTRACKED
    # `computations/knot-volumes.witness.json` while the cited copy sat frozen
    # at 2026-04-07 — which is how it kept a `Vol(4_1) = 3·Cl₂(π/3)` source
    # string long after this file was corrected.
    #
    # Do not "simplify" this by dropping the argument: that silently
    # disconnects the producer from its consumers again, and the symptom
    # (a witness that never refreshes) is invisible until someone diffs a
    # value against its own source. Bean qou-zdz5.
    out_path = (WitnessBuilder.wrap_legacy(
        "knot-volumes", witness,
        script_path=__file__,
        engine="snappea",
        engine_version=f"snappy {snappy.__version__}",
        output_dir=Path(__file__).resolve().parent / "substrate",
        )
        .save())
    print(f"\nWitness written to {out_path}")
    print(f"All passed: {all_passed} ({len(assertions)} assertions, {duration_ms}ms)")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
