"""Tritium 8_11 Jones-Markov probe — corrects Track B Phase B-2 framing.

Phase B-2 of the Track B execution plan was originally framed as
"R5-full for tritium (H_5)" assuming the canonical 8_11 braid lives
in B_5. **This assumption was wrong.** Per the knot_braid_database
(PR #1263), 8_11 has braid index **3**, with the canonical 8-crossing
B_3 representative `σ_1² σ_2⁻¹ σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ σ_2⁻¹`.

Tritium therefore lives at H_3 — same Hecke algebra as deuteron and
³He. R5-full's existing H_3 machinery can handle it; no Python H_5
Hoefsmit seminormal implementation is needed.

## Probe — |tr_M(8_11, q_0)| via common infra

Uses `markov_trace_for_knot("8_11", q_0, ...)` from PR #1263 to
compute the bare Markov trace under both conventions, comparing to
the AME tritium binding value.

## Empirical finding (this run)

  |tr_M(8_11, q_0)|_Wenzl   ≈ 0.1856   →  m_e·|tr_M| ≈ 0.0949 MeV
  |tr_M(8_11, q_0)|_qSchur  ≈ 0.1961   →  m_e·|tr_M| ≈ 0.1002 MeV
  AME B(³H)                 = 8.4818 MeV

The bare Markov-trace value is ~89× smaller than the AME binding
— SAME PATTERN as Phase B-4 c_αα probe (PR #1274), and the same
pattern as proton mass derivation (where bare |tr_M(𝓑₃)| ≈ 1 vs
m_p ≈ 1836·m_e).

Existing tritium prediction in `low-isotope-mass-table.witness.json`
gives 8.468598 MeV (err −1556 ppm vs AME) — this prediction does
NOT come from bare |tr_M(8_11)|; it goes through the canonical
multi-nucleon atom braid via the VolDensity / canonical chain.

## Track B implication

Phase B-2's substantive scope shrinks to: **add tritium to
R5_FULL_SUBSTRATE_REGISTRY at H_3** (not H_5). The R5-full search
machinery already supports H_3. The deferred-because-of-H_5 note
in `r5_full_canonical_knot_solver.py` lines 18-19 was based on the
incorrect B_5 assumption.

This script is the probe; the actual registry addition is a
separate follow-up (~30 LOC change in r5_full_canonical_knot_solver.py
plus a re-run to confirm 8_11 emerges as the cost-minimum).

## Status: EXPLORATORY

Per CLAUDE.md production-vs-exploratory discipline.

## Cross-references

- `markov_trace_for_knot.py` (PR #1263 common infra)
- `knot_braid_database.py` (PR #1263; 8_11 catalogued as B_3)
- `c_alpha_alpha_categorical_via_jones_markov.py` (PR #1274; same
  pattern on 7²_1)
- `r5_full_canonical_knot_solver.py` (the target of follow-up
  registry addition)
- `docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md`
  (PR #1270 — needs minor correction noting 8_11 is B_3)
"""
from __future__ import annotations


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

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from knot_braid_database import braid_word_for_knot, n_strands_for_knot  # noqa: E402
from markov_trace_for_knot import markov_trace_for_knot  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# AME 2020 reference
AME_BINDING_3H_MEV = 8.481798


def main() -> int:
    w = WitnessBuilder(
        "tritium-8-11-jones-markov-probe",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md",
    )
    w.set_description(
        "Phase B-2 probe (EXPLORATORY): corrects the B_5 → B_3 "
        "misframing of tritium's canonical knot (8_11 has braid index "
        "3, not 5). Computes |tr_M(8_11, q_0)| via common-infra "
        "(markov_trace_for_knot, mp.mpf at 50 dps) under both Wenzl "
        "JM and q-Schur conventions and confirms the same bare-|tr_M| "
        "<< AME pattern documented at 7²_1 (PR #1274) and 𝓑₃ "
        "(proton-mass). The framework's VolDensity chain is the "
        "correct substrate-pure derivation; bare |tr_M| is not."
    )
    set_compute_dps(50)

    print("=" * 78)
    print("Tritium 8_11 Jones-Markov probe (Phase B-2)")
    print("=" * 78)

    # Braid catalogue check (correcting the B_5 → B_3 assumption)
    braid = braid_word_for_knot("8_11")
    n_strands = n_strands_for_knot("8_11")
    print(f"\n  8_11 catalogued braid: {braid}")
    print(f"  Strand count (catalogued): n = {n_strands}")
    print(f"  Length: {len(braid)} crossings")
    if n_strands == 3:
        print(f"  → Tritium canonical knot 8_11 IS in B_3 / H_3 "
              f"(NOT B_5 as the original Track B design doc assumed)")

    q_str = Q_50_DIGIT_STR
    me_mpf = mp.mpf(str(M_E_MEV))
    ame_mpf = mp.mpf(str(AME_BINDING_3H_MEV))
    print(f"\n  q_0 (50 dps) = {q_str}")
    print(f"  m_e = {mp.nstr(me_mpf, 25)} MeV")
    print(f"  AME B(³H) = {AME_BINDING_3H_MEV} MeV")

    # Trace under both conventions — mp.mpf at 50 dps (L1 floor)
    print(f"\n[1/2] |tr_M(8_11, q_0)| Wenzl JM (mass-formula, mpf 50 dps)")
    t0 = time.perf_counter()
    trM_wenzl = markov_trace_for_knot("8_11", q_str, "wenzl")
    t_wenzl = time.perf_counter() - t0
    print(f"      tr_M = {mp.nstr(trM_wenzl, 25)}")
    print(f"      |tr_M| = {mp.nstr(abs(trM_wenzl), 25)}")
    print(f"      m_e · |tr_M| = {mp.nstr(me_mpf * abs(trM_wenzl), 12)} MeV")
    print(f"      wall: {t_wenzl*1000:.2f} ms")

    print(f"\n[2/2] |tr_M(8_11, q_0)| q-Schur (torus-knot, mpf 50 dps)")
    t0 = time.perf_counter()
    trM_qschur = markov_trace_for_knot("8_11", q_str, "q_schur")
    t_qschur = time.perf_counter() - t0
    print(f"      tr_M = {mp.nstr(trM_qschur, 25)}")
    print(f"      |tr_M| = {mp.nstr(abs(trM_qschur), 25)}")
    print(f"      m_e · |tr_M| = {mp.nstr(me_mpf * abs(trM_qschur), 12)} MeV")
    print(f"      wall: {t_qschur*1000:.2f} ms")

    # Gap analysis vs AME (mpf throughout)
    pred_wenzl = me_mpf * abs(trM_wenzl)
    pred_qschur = me_mpf * abs(trM_qschur)
    ratio_wenzl = ame_mpf / pred_wenzl
    ratio_qschur = ame_mpf / pred_qschur

    print(f"\n  AME B(³H) / (m_e·|tr_M|_Wenzl)   = {mp.nstr(ratio_wenzl, 6)}×")
    print(f"  AME B(³H) / (m_e·|tr_M|_qSchur)  = {mp.nstr(ratio_qschur, 6)}×")
    print(f"\n  Same pattern as PR #1274's c_αα probe on 7²_1:")
    print(f"  bare |tr_M| << binding-scale by ~88-90× factor.")
    print(f"  VolDensity chain (Vol/ℏ_q² × linking_weight) is the")
    print(f"  correct substrate-pure derivation.")

    # Witness
    w.add_parameter("q_0_50dps", q_str)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("knot", "8_11 (tritium hyperbolic knot)")
    # JSON-friendly serialization: list of [sign, gen] pairs
    w.add_parameter("braid_word", [list(t) for t in braid])
    w.add_parameter("n_strands_catalogued", n_strands)
    w.add_parameter("evaluator_precision", "mp.mpf at 50 dps (L1 floor) via "
                                          "markov_trace_for_knot mpf default")
    w.add_data("tr_M_wenzl", mp.nstr(trM_wenzl, 25))
    w.add_data("tr_M_qschur", mp.nstr(trM_qschur, 25))
    w.add_data("m_e_times_abs_tr_M_wenzl_MeV", mp.nstr(pred_wenzl, 25))
    w.add_data("m_e_times_abs_tr_M_qschur_MeV", mp.nstr(pred_qschur, 25))
    w.add_data("AME_binding_3H_MeV", AME_BINDING_3H_MEV)
    w.add_data("ratio_AME_to_bare_wenzl", mp.nstr(ratio_wenzl, 25))
    w.add_data("ratio_AME_to_bare_qschur", mp.nstr(ratio_qschur, 25))
    w.add_data("wall_seconds", {
        "wenzl_jm": t_wenzl,
        "q_schur": t_qschur,
    })
    w.add_data("phase_b_2_correction", {
        "original_assumption": (
            "tritium 8_11 is in B_5 / H_5, requiring new Python "
            "Hoefsmit seminormal implementation"
        ),
        "corrected_finding": (
            "8_11 has braid index 3; canonical representative is "
            "in B_3 / H_3; R5-full's existing H_3 machinery handles "
            "it without new code"
        ),
    })

    w.add_assertion(
        name="braid_index_8_11_is_3",
        computed=n_strands,
        expected=3,
        tolerance=0,
        source=(
            "knot_braid_database.HYPERBOLIC_NSTRANDS — corrects "
            "the r5_full_canonical_knot_solver.py line 18-19 'B_5/8_11' "
            "comment"
        ),
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554
    # wiring, 2026-05-31). Each nucleus's canonical T_w knot
    # operator uniqueness at the empty-constraint SDP level.
    w.add_data("lean_uniqueness_ref", {
        "tritium": "qou:QOU.BraidKnot.tritium_uniqueness_closed",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). The real per-nucleus SDP (multi-term cost + non-empty constraints) is per-nucleus substantive open work. Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })


    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
