#!/usr/bin/env python3
"""
Trace whether c_αα = m_e · Vol(7²_1) is reproducible from the
framework's three-constant calibration (m_e, m_μ/m_e → q_0,
Q_β(³H)) without ever using B(¹²C) as an input.

Two independent computations:

(A) c_αα via pure topology — no AME, no β-chain:
    c_αα_topo = m_e · Vol(7²_1) = 2.42699... MeV
    Vol(7²_1) from SnapPy is a TOPOLOGICAL invariant of the link.
    m_e is calibration input.  No other AME used.

(B) c_αα via β-chain — uses only Q_β(³H):
    The framework's compound-β-decay-shell-calibration proposition
    claims y_target(A_magic) is derivable from the chain Q-values
    reaching the magic anchor.  The single Q_β(³H) = 0.78233341 MeV plus
    the chain of intermediate predictable Q values can in principle
    extract the cumulative shell contribution at A=12 and hence c_αα.

    For this to count as derivation-only, the intermediate Q values
    in the chain must themselves be PREDICTED by the framework
    (not AME-fitted).  This script checks whether such predictions
    exist in the codebase.

If (A) and (B) agree, c_αα is fully derived.
If only (A) is available, it's a topological prediction with no
independent β-chain confirmation (still zero-parameter given m_e).
If (B) requires extra AME inputs, the α-cluster formula is not
zero-parameter in the strict sense.

Output: c-alpha-from-Q-beta-trace.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from experimental_constants import M_E_MEV, Q_TRITIUM_MEV
from witness_base import WitnessBuilder


# Knot volumes from canonical knot_volumes module (mpmath 50dps).
# See PR #781 knot-vol propagation.
from knot_volumes import CATALAN_G, VOL_BORROMEAN, VOL_7_SQ_1  # noqa: E402


def main():
    w = WitnessBuilder("c-alpha-from-Q-beta-trace",
                        engine="topology+β-chain-audit")
    w.set_description(
        "Audit: is c_αα = m_e · Vol(7²_1) ≈ 2.427 MeV reproducible from "
        "the framework's three-constant calibration (m_e, q_0, Q_β(³H)) "
        "without using B(¹²C) or other AME inputs?"
    )

    # ─────────────────────────────────────────────────────────────
    # (A) Pure topological derivation
    # ─────────────────────────────────────────────────────────────
    print("=" * 90)
    print("(A) c_αα from pure topology + m_e")
    print("=" * 90)
    c_alpha_topo = M_E_MEV * VOL_7_SQ_1
    print(f"  m_e             = {M_E_MEV} MeV                    [calibration]")
    print(f"  Vol(7²_1)       = {VOL_7_SQ_1:.10f}      [SnapPy topological invariant]")
    print(f"  c_αα = m_e·Vol  = {c_alpha_topo:.6f} MeV")
    print()
    print("  Inputs: m_e (allowed), Vol(7²_1) (pure topology).")
    print("  No AME input.  No β-chain.")
    print()
    print("  Topological justification: 7²_1 is the 2-component link")
    print("  realising two 'linked Borromean triples' (α-α coupling).")
    print("  This is framework-structural IF the α-particle is a")
    print("  4-Borromean closure and α-α coupling inherits the 7²_1")
    print("  link class from the Jones structure.  Check in paper:")
    print("  shell-closure-stability.md derives electron-shell magic")
    print("  numbers (Z=2,10,18,...) via SDP terminality — but does NOT")
    print("  explicitly derive Vol(7²_1) as THE α-α coupling knot.")
    print()

    # ─────────────────────────────────────────────────────────────
    # (B) β-chain derivation
    # ─────────────────────────────────────────────────────────────
    print("=" * 90)
    print("(B) c_αα via compound-β-decay shell calibration")
    print("=" * 90)
    print("  Framework claim (compound-beta-shell-calibration.md):")
    print("    y_target(A_magic) is derivable from cumulative Q-values")
    print("    of β-decays reaching each magic anchor.")
    print()
    print("  At minimum the chain needs Q values for EVERY")
    print("  intermediate β-decay between reference (say ³H) and")
    print("  target A_magic = 12 (for ¹²C-derived c_αα).")
    print()
    print("  Isobar chain from stable reference to ¹²C:")
    print("    ¹²B → ¹²C    Q_β = 13.37 MeV   (AME)")
    print("    ¹²N → ¹²C    Q_β = 17.34 MeV   (AME)")
    print("    (¹²C is stable — terminal of chain)")
    print()
    print("  To reach ¹²C from the ³H calibration anchor, one would")
    print("  need to sum Q values along a full network of β decays,")
    print("  e.g. via ³H → ³He → (capture) → … → ¹²C.  Each step's")
    print("  Q value is EXPERIMENTAL unless the framework can PREDICT")
    print("  the non-magic Q^(3) values between steps.")
    print()
    print("  Check: does the codebase have a non-magic-Q predictor?")

    # Scan codebase for evidence
    from pathlib import Path
    search_root = Path(__file__).parent
    non_magic_q_predictors = []
    this_file = Path(__file__).name
    for p in search_root.glob("*.py"):
        if p.name == this_file:
            continue  # don't self-match
        try:
            txt = p.read_text()
            if any(s in txt for s in (
                "predict_Q_beta", "Q_beta_predict", "beta_Q_from_",
                "non_magic_Q",
            )):
                non_magic_q_predictors.append(p.name)
        except (OSError, UnicodeDecodeError):
            # Skip files we can't read (permissions, encoding).  Other
            # exception types should surface as bugs.
            pass

    if non_magic_q_predictors:
        print(f"\n  Found potential predictors: {non_magic_q_predictors}")
    else:
        print("\n  No non-magic-Q predictor script found in folio-assistant/")
        print("  computations/.  The β-chain path REQUIRES AME-sourced Q_β")
        print("  values for every intermediate non-magic step — making")
        print("  route (B) effectively AME-informed in practice.")
    print()

    # ─────────────────────────────────────────────────────────────
    # Verdict
    # ─────────────────────────────────────────────────────────────
    print("=" * 90)
    print("VERDICT")
    print("=" * 90)
    print()
    print("  Route (A) topological: c_αα_topo = {:.4f} MeV".format(c_alpha_topo))
    print("    uses only m_e + Vol(7²_1).  Zero extra AME input.")
    print("    VALID under the three-constant calibration rule.")
    print()
    print("  Route (B) β-chain:")
    print("    The framework's claim that magic-anchor y_target is")
    print("    derivable from Q_β chains requires, at minimum, a")
    print("    PREDICTOR for non-magic intermediate Q values — which")
    print("    is NOT PRESENT in the codebase.  In practice the chain")
    print("    is AME-populated for every intermediate step.")
    print()
    print("  So: c_αα is a ONE-ROUTE derivation — the topological")
    print("  identification 7²_1 ↔ α-α.  The numerical match")
    print("  Vol(7²_1) = 4.7495 is a topological fact (SnapPy),")
    print("  and c_αα_topo = m_e · Vol(7²_1) = 2.427 MeV is the")
    print("  zero-parameter prediction.")
    print()
    print("  THE OPEN QUESTION: is 7²_1 THE CORRECT knot for α-α")
    print("  coupling?  The paper asserts this as a topological claim")
    print("  (two-linked-Borromean-triples structure) but does not")
    print("  derive it from first principles.  The alternative is that")
    print("  7²_1 was reverse-engineered from observing Vol(7²_1)·m_e")
    print("  ≈ c_αα (extracted from ¹²C binding) — in which case route")
    print("  (A) is implicitly AME-fitted via topology selection.")
    print()
    print("  Distinguishing these interpretations requires a derivation")
    print("  of the α-α coupling knot from the framework's Hecke / SDP")
    print("  structure without reference to ¹²C AME data.  That")
    print("  derivation is NOT present in the current content blocks.")

    # Save
    w.add_parameter("m_e_MeV", M_E_MEV)
    w.add_parameter("Vol_7_sq_1", VOL_7_SQ_1)
    w.add_parameter("Q_beta_tritium_MeV", Q_TRITIUM_MEV)
    w.add_data("route_A_topological", {
        "c_alpha_MeV": c_alpha_topo,
        "formula": "m_e · Vol(7²_1)",
        "inputs_used": ["m_e (calibration)", "Vol(7²_1) (SnapPy topology)"],
        "ame_inputs": [],
        "valid_under_three_constant_rule": True,
    })
    w.add_data("route_B_beta_chain", {
        "predictor_present": len(non_magic_q_predictors) > 0,
        "predictor_files": non_magic_q_predictors,
        "ame_inputs_required_in_practice": True,
        "reason": "No non-magic-Q predictor → every intermediate Q uses AME",
    })
    w.add_data("verdict", {
        "c_alpha_zero_parameter_under_rule": True,
        "caveat": (
            "Zero-parameter ONLY under the interpretation that 7²_1 is "
            "independently derived from the framework's topology.  If "
            "7²_1 was chosen by matching Vol(7²_1) to c_αα/m_e extracted "
            "from ¹²C AME, the derivation is implicitly AME-fitted."
        ),
    })
    w.save()


if __name__ == "__main__":
    main()
