#!/usr/bin/env python3
"""
Bridge: Term 6 (Habiro residue) → MPFR 50 dps witness schema.

The existing producer ``term6_residues_at_roots.py`` computes T6
in f64 + sympy via principal-part-at-roots-of-unity, emitting
``term6-residues-at-roots.witness.json`` keyed by particle name.

The consumer
``mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp(A)``
expects a sibling witness
``term6-habiro-residue-mpfr-50dps.witness.json`` keyed by
``atom == f"A={A}"`` with a ``term6_b_pred_mev_50dps`` field.

This script bridges the two — reads the existing f64 values and
re-emits them in the expected schema.  T6 is **not** lifted to
50 dps here (the upstream producer is still f64); the f64 value
is wrapped in ``mp.mpf(str(value))`` for downstream consumption.

The T6 magnitudes for A=1 atoms are small (~2 MeV for proton/
neutron, divided by m_e gives ~4 cat units vs m_p_hecke ~1.18M),
so the f64 → 50 dps precision loss is ~10⁻¹⁵ of m_p_hecke,
well below the 1.50 % residual gate.

A=0 (electron) is **not in the upstream witness** — T6 for the
electron via the residue-at-roots path needs its own derivation
(the electron's tr_M(σ_1^3, q) has a different pole structure
than the nucleon braids).  Surfaced as a documented gap.

Output: ``term6-habiro-residue-mpfr-50dps.witness.json``
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# P31 compliance: m_e from codata_constants module-level (single source).
from codata_constants import M_E_MEV as _M_E_MEV_CONST  # noqa: E402
M_E_MEV_MP = mp.mpf(str(_M_E_MEV_CONST))
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, load_and_hash_upstream  # noqa: E402

SRC_PATH = _pb.witness_path("term6-residues-at-roots.witness.json", HERE)
OUT_PATH = _pb.witness_path("term6-habiro-residue-mpfr-50dps.witness.json", HERE)


def main() -> int:
    src, src_hash = load_and_hash_upstream(SRC_PATH)
    rows = src.get("data", {}).get("results", [])

    # Group by A and select the canonical representative per A.
    # For A=1 we use the proton (Z=1, N=0); for A=2 the deuteron;
    # for A=3 the triton (or ³He, identical structure); for A=4 ⁴He.
    # T6 at A=1 must apply uniformly to {p, n, e} consumers, so the
    # f64 proton row is used as the A=1 representative.  T6 for the
    # electron at H_2 is a separate derivation and is surfaced as a
    # null row with documented gap.
    canonical = {}
    for r in rows:
        A = r.get("A")
        if A is None:
            continue
        # Prefer proton for A=1, deuteron for A=2, triton for A=3, He-4 for A=4.
        prefer = {
            1: "proton", 2: "deuteron", 3: "tritium", 4: "helium-4",
        }
        if r.get("atom") == prefer.get(A) or A not in canonical:
            canonical[A] = r

    out_rows = []
    for A in sorted(canonical.keys()):
        r = canonical[A]
        # The upstream value 'term6_at_q0_real' is in mass-formula
        # cat-units (dimensionless multiplier of m_e).  Convert to
        # MeV by multiplying by the module-level M_E_MEV_MP (P31 compliant).
        cat_units = float(r["term6_at_q0_real"])
        # Use mpmath 50-dps str roundtrip to preserve precision.
        t6_b_pred_MeV = M_E_MEV_MP * mp.mpf(repr(cat_units))
        out_rows.append({
            "atom":                  f"A={A}",
            "A":                     A,
            "source_particle":       r.get("atom"),
            "term6_b_pred_mev_50dps": str(t6_b_pred_MeV),
            "term6_cat_units_f64":   str(cat_units),
            "precision_note":        (
                "Bridged from f64 source 'term6-residues-at-roots'; "
                "downstream consumer wraps in mp.mpf for 50-dps arithmetic. "
                "Upstream precision is f64 (~10^-15 relative)."
            ),
        })

    # Document electron gap (A=0 is not in the upstream witness).
    out_rows.append({
        "atom":             "A=0",
        "A":                0,
        "source_particle":  "electron (NOT YET DERIVED)",
        "term6_b_pred_mev_50dps": None,
        "term6_cat_units_f64":   None,
        "precision_note":   (
            "Electron T6 at H_2 (σ_1^3 trefoil) is a separate "
            "derivation — the upstream f64 producer does not "
            "cover non-nucleon braids.  Surfaced as a documented "
            "gap pending an electron-specific residue compute."
        ),
    })

    w = WitnessBuilder("term6-habiro-residue-mpfr-50dps", engine="mpmath")
    w.set_description(
        "Term 6 (Habiro residue) bridged from the f64 producer "
        "'term6_residues_at_roots.py' into the schema expected by "
        "mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp(A). "
        "T6 magnitudes for A=1 are small (~2 MeV / m_e ≈ 4 cat units) "
        "relative to m_p_hecke (~1.18e6), so the f64 → 50 dps wrap "
        "is precision-safe at the current 1.50 % m_p closure gate. "
        "Electron T6 (A=0 / H_2) is surfaced as a null row pending "
        "an electron-specific residue derivation."
    )
    w.set_audit_only("docs/audits/2026-05-16-t1-t4-tower-closure-plan.md")
    w.add_upstream(SRC_PATH)
    w.add_parameter("m_e_MeV", str(M_E_MEV_MP))
    w.add_parameter("dps", mp.mp.dps)
    w.add_data("results_by_atom", out_rows)
    w.set_content_block("prop:term6-binding-density")
    w.save()
    print(f"  Wrote {OUT_PATH.name} with {len(out_rows)} A-keyed rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
