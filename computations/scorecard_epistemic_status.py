#!/usr/bin/env python3
"""Epistemic status of every compared row on the accuracy scorecard (ACCURACY.md).

Compute-accuracy epic item A2 (owner dispatch 2026-11-27, "dispatch siblings to do
all"). The scorecard used to carry a free-text "Status" per row, written in the
renderer, and several of those strings had drifted from the corpus: the meson ratio
m_K/m_pi was labelled "Derived" while the corpus records its (3,4) fusion pair as
scan-selected, and the alpha_EM Form B row was counted as derived although its own
witness names three hypotheses it is conditional on.

This producer moves the label out of the renderer. Each row gets exactly one of

    Calibration  an input the model is pinned to (CAL-1/2/3 or the q0 pin); not scored
    Derived      computed from the model with no hypothesis, choice or fit outstanding
    Selected     an object (pair, cell, chart, branch) was chosen against the target;
                 a fit by AGENTS.md "NO FITTING", even with no continuous parameter
    Conditional  derived given a named, unproved hypothesis (a section-3b-cond class,
                 a conjecture, or an inherited conditional input)
    Unclassified no corpus artefact decides it yet; shown as a visible gap

and a BASIS: a repository file plus a verbatim excerpt that must occur in it. The
producer refuses (assertion fails, allPassed false, the scorecard gate goes red) if
any basis file is missing or no longer contains its excerpt, so a label cannot
outlive the artefact that decides it. The renderer
(scripts/generate-accuracy-scorecard.py) reads only this witness for the label.

No numbers are computed here; there is no float arithmetic.

Usage: python3 computations/scorecard_epistemic_status.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

STATUSES = ("Calibration", "Derived", "Selected", "Conditional", "Unclassified")

ALPHA_LADDER = "computations/alpha-em-schwinger-ladder.witness.json"
PER_OBS = "computations/per-observable-100x-status.witness.json"
MK_AUDIT = "docs/audits/2026-11-20-mk-mpi-derivation-status.md"
RULINGS = "docs/coordination/owner-rulings.md"
KOIDE = "computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json"
EW_LEAN = "folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakBringSchwingerBridge.lean"
SEIFERT = "computations/alpha/alpha-em-seifert-kappa-pairing.witness.json"
U1 = "computations/u1-hypercharge-assignment.witness.json"

# row id -> (status, basis file, verbatim excerpt that must occur in the basis file, gloss)
ROWS: dict[str, tuple[str, str, str, str]] = {
    # Table 3.1a
    "m_e": ("Calibration", PER_OBS, "CAL-1 anchor", "calibration input 1"),
    "m_p": ("Calibration", PER_OBS, "CAL-2 numerical anchor", "q0 pin; not scored"),
    "m_pi": ("Calibration", "AGENTS.md", "m_π (PDG)", "CAL-3 proxy; calibration input 3"),
    "m_mu": ("Derived", PER_OBS, '"role": "validation"',
             "proton-pinned q0 evaluated at the muon; scored as validation, no outstanding hypothesis"),
    "m_tau_over_m_e": ("Conditional", KOIDE, "Koide",
                       "conditional on KoideTopologicalProtectionHypothesis"),
    "mk_over_mpi": ("Selected", MK_AUDIT, "selected",
                    "the (3,4) fusion pair and the EM factor were chosen from a scan against the target"),
    "m_k": ("Selected", MK_AUDIT, "selected", "m_K = (m_K/m_pi) x m_pi pin; inherits the selection"),
    "m_n": ("Conditional", PER_OBS, "INHERITS A CONDITIONAL Q_beta",
            "m_p + m_e + Q_beta; Q_beta conditional on C1-C3"),
    "delta_m_np": ("Conditional", PER_OBS, "INHERITS A CONDITIONAL Q_beta",
                   "inherits the conditional Q_beta (C1-C3)"),
    # Table 3.2a (K_A rows: owner ruling 2026-11-25 scope note)
    "ka_rows": ("Selected", RULINGS, "is the cell nearest AME out of a 6",
                "the 2H start value is the grid cell nearest AME out of 6 models x 4 charts"),
    "hecke_1d_chain": ("Unclassified", "ACCURACY.md", "1D Symbolic Hecke Chain",
                       "no corpus artefact classifies this row yet"),
    # Table 3.3a
    "charge_Q": ("Derived", U1, "c is NOT a free knob",
                 "Q = writhe/2 with the fixed coupling c = 1/2"),
    "alpha_form_b": ("Conditional", ALPHA_LADDER,
                     "conditional on ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass",
                     "1-loop (1 - h_A^2 alpha) factor proved (EmFermionLoopFourTopology); the value is "
                     "conditional on ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass"),
    "alpha_form_c": ("Conditional", ALPHA_LADDER, "AlphaEmTwoLoopBlochSchwingerClass",
                     "conditional on AlphaEmTwoLoopBlochSchwingerClass"),
    "alpha_seifert": ("Conditional", SEIFERT, "Conditional/unproved",
                      "Seifert determinant ratio exact; its derivation as the CS Gram Jacobian is open"),
    "alpha_legacy_cs": ("Unclassified", "ACCURACY.md", "legacy Witten",
                        "legacy baseline; no corpus artefact classifies it"),
    "rydberg_form_b": ("Conditional", ALPHA_LADDER, "BringZeroModeBlochClass",
                       "(1/2) m_e alpha^2 with Form B alpha; inherits its three hypotheses"),
    "rydberg_form_c": ("Conditional", ALPHA_LADDER, "AlphaEmTwoLoopBlochSchwingerClass",
                       "(1/2) m_e alpha^2 with Form C alpha; inherits its hypothesis"),
    "coulomb_3h_3he": ("Unclassified", "ACCURACY.md", "Bare topological",
                       "nuclear-geometry factor open; not yet classified"),
    "mirror_coulomb": ("Unclassified", "ACCURACY.md", "Mirror-nuclei Coulomb",
                       "not yet classified"),
    "vsepr": ("Unclassified", "ACCURACY.md", "VSEPR", "Table 3.3b rows; not yet classified"),
    # Table 3.4a
    "beta_tm_rows": ("Unclassified", "ACCURACY.md", "Bare monotone transfer-matrix",
                     "zero-fit proxy; not yet classified"),
    "q_beta_free_neutron": ("Conditional", PER_OBS, "qbeta_conditional_t3_split",
                            "T^3 weight-trace split on V^3; conditional on C1-C3"),
    "v_weak": ("Conditional", EW_LEAN, "ElectroweakVevFixedPointClass",
               "conditional on ElectroweakVevFixedPointClass"),
}


def main() -> int:
    failures: list[str] = []
    rows_out: dict[str, dict[str, str]] = {}
    for rid, (status, basis, excerpt, gloss) in ROWS.items():
        if status not in STATUSES:
            failures.append(f"{rid}: unknown status {status!r}")
        p = REPO / basis
        if not p.is_file():
            failures.append(f"{rid}: basis file missing: {basis}")
        elif excerpt not in p.read_text(encoding="utf-8"):
            failures.append(f"{rid}: basis {basis} no longer contains {excerpt!r}")
        rows_out[rid] = {"status": status, "basis": basis, "basis_excerpt": excerpt, "gloss": gloss}
    for f in failures:
        print("FAIL", f)

    counts = {s: sum(1 for r in rows_out.values() if r["status"] == s) for s in STATUSES}
    wb = WitnessBuilder("scorecard-epistemic-status", engine="python (no arithmetic)", output_dir=HERE)
    wb.set_description(
        "Per-row epistemic status (Calibration / Derived / Selected / Conditional / Unclassified) "
        "for ACCURACY.md, each with a basis file and a verbatim excerpt that must still occur in it. "
        "Owner dispatch 2026-11-27. Consumed by scripts/generate-accuracy-scorecard.py.")
    wb.add_data("statuses", list(STATUSES))
    wb.add_data("rows", rows_out)
    wb.add_data("counts", counts)
    wb.add_assertion("every_basis_present_and_quoting", computed=str(len(failures)), expected="0",
                     tolerance="0", source="each basis file exists and contains its excerpt")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "labels only: reads no q0 and computes no number"})
    print(f"{len(rows_out)} rows; {counts}; failures {len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
