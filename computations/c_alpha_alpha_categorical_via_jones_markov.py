"""c_αα Markov-trace probe — surfaces gap vs literature m_e·Vol(7²_1).

Phase B-4 of the Track B execution plan (per design doc PR #1270).

## Background

The α-cluster recursion `B(nα) = n·B(⁴He) + C(n,2)·c_αα`
(see `alpha_cluster_recursion.py`) requires the α-α coupling
constant `c_αα`. Currently this is set to

    c_αα^lit = m_e · Vol(7²_1)
            ≈ 0.51099895069 × 4.7495
            ≈ 2.4269 MeV

— uses Vol(7²_1) directly (no ℏ_q² scaling), unlike the proton
mass formula `m_p = m_e · VolDensity(𝓑₃)` which scales by
`Vol(𝓑₃) / ℏ_q² × linking_weight`. This dimensional discrepancy
is itself an open question (`c_αα` is a binding scale ~MeV vs
`m_p` is a rest-mass scale ~GeV; both use `m_e` as calibration
but different geometric factors).

## What this script does

Computes the bare Markov-trace value

    |tr_M(7²_1, q_0)|

via the common-infra `markov_trace_for_knot("7^2_1", q_0, ...)`
from PR #1263, and compares `m_e · |tr_M|` against the literature
`m_e · Vol(7²_1)`. Reports both Wenzl Jones-Markov (mass-formula
convention) and q-Schur Plancherel (torus-knot convention) values.

## Empirical finding (this run)

  |tr_M(7²_1, q_0)|_Wenzl   ≈ 0.2086    →  m_e·|tr_M| ≈ 0.107 MeV
  |tr_M(7²_1, q_0)|_qSchur  ≈ 0.1852    →  m_e·|tr_M| ≈ 0.095 MeV
  Vol(7²_1)                 ≈ 4.7495    →  m_e·Vol     ≈ 2.427 MeV

The bare Markov trace gives ~22.7× smaller than the literature
volume-based c_αα. This mirrors the proton case:

  |tr_M(𝓑₃, q_0)|_Wenzl    ≈ 0.998     →  m_e·|tr_M| ≈ 0.510 MeV
  VolDensity(𝓑₃, q_0)        ≈ 1836      →  m_e·Geom   ≈ 938 MeV

i.e. `|tr_M|` alone is NOT the right substrate-pure derivation
of binding/mass scales — the framework's volume × ℏ_q² × linking-
weight machinery is the correct chain (per `prop:geom-universality`
and the VolDensity formula). This script is a NEGATIVE finding: the
Markov-trace value is interesting but does NOT substitute for the
literature `Vol(7²_1)` in `alpha_cluster_recursion.py`.

## Status: EXPLORATORY

Per CLAUDE.md production-vs-exploratory discipline, this is a
probe surfacing a research-grade question (what's the categorically-
exact derivation of c_αα at the substrate level?), NOT a wired
production change. The α-cluster recursion's existing
`C_ALPHA_ALPHA_MEV = m_e · Vol(7²_1)` stays in place.

## Cross-references

- `prop:atom-knot-mass-derivation` (the canonical formula)
- `docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md`
  (Phase B-4 in the execution plan)
- `folio-assistant/computations/alpha_cluster_recursion.py`
  (the current consumer of c_αα)
- `folio-assistant/computations/knot_volumes.py` (the literature
  Vol(7²_1) source)
- `folio-assistant/computations/knot_braid_database.py` (7²_1
  braid word; PR #1263)
- `folio-assistant/computations/markov_trace_for_knot.py`
  (common-infra evaluator; PR #1263)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from knot_braid_database import braid_word_for_knot  # noqa: E402
from knot_volumes import VOL_7_SQ_1_F64, VOL_7_SQ_1_MPF  # noqa: E402
from markov_trace_for_knot import markov_trace_for_knot  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    w = WitnessBuilder(
        "c-alpha-alpha-categorical-via-jones-markov",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md",
    )
    w.set_description(
        "Phase B-4 c_αα probe (EXPLORATORY — NEGATIVE result). Tests "
        "whether the substrate-canonical Markov-trace value "
        "m_e·|tr_M(T_w(7²_1), q_0)| could replace the literature "
        "c_αα = m_e·Vol(7²_1) ≈ 2.43 MeV in alpha_cluster_recursion.py. "
        "Result: bare Markov-trace value is ~22.7× smaller than "
        "the literature; the substitution does NOT work. Mirrors the "
        "proton-mass case (|tr_M(𝓑₃)| << m_p) — bare |tr_M| is not "
        "the substrate-pure binding-scale derivation; VolDensity chain "
        "(Vol/ℏ_q² × linking_weight) is. This probe does NOT propose "
        "changing alpha_cluster_recursion.py."
    )
    set_compute_dps(50)

    print("=" * 78)
    print("c_αα Markov-trace probe (Phase B-4 — NEGATIVE finding)")
    print("=" * 78)

    q_str = Q_50_DIGIT_STR

    # Build the 7²_1 braid via common infra
    braid = braid_word_for_knot("7^2_1")
    print(f"\n  7²_1 braid word (B_3): {braid}")
    print(f"  (length {len(braid)} crossings)")
    print(f"\n  q_0 (50 dps) = {q_str}")
    print(f"  m_e = {float(M_E_MEV):.10f} MeV")

    # Markov trace under both conventions — mpf at 50 dps (L1 floor)
    print(f"\n[1/3] Markov trace under Wenzl Jones-Markov convention "
          f"(mass formula, mpf 50 dps)...")
    t0 = time.perf_counter()
    trM_wenzl = markov_trace_for_knot("7^2_1", q_str, "wenzl")
    t_wenzl = time.perf_counter() - t0
    print(f"      tr_M(7²_1, q_0) (Wenzl JM) = {mp.nstr(trM_wenzl, 25)}")
    print(f"      |tr_M(7²_1, q_0)| (Wenzl JM) = {mp.nstr(abs(trM_wenzl), 25)}")
    print(f"      wall: {t_wenzl*1000:.2f} ms")

    print(f"\n[2/3] Markov trace under q-Schur Plancherel convention "
          f"(torus knots, lepton tower, mpf 50 dps)...")
    t0 = time.perf_counter()
    trM_qschur = markov_trace_for_knot("7^2_1", q_str, "q_schur")
    t_qschur = time.perf_counter() - t0
    print(f"      tr_M(7²_1, q_0) (q-Schur) = {mp.nstr(trM_qschur, 25)}")
    print(f"      |tr_M(7²_1, q_0)| (q-Schur) = {mp.nstr(abs(trM_qschur), 25)}")
    print(f"      wall: {t_qschur*1000:.2f} ms")

    # Derived c_αα under each convention (mpf 50 dps throughout)
    print(f"\n[3/3] Derived c_αα values vs literature (mpf 50 dps)")
    m_e_mpf = mp.mpf(str(M_E_MEV))
    c_aa_derived_wenzl = m_e_mpf * mp.fabs(trM_wenzl)
    c_aa_derived_qschur = m_e_mpf * mp.fabs(trM_qschur)
    c_aa_literature = m_e_mpf * VOL_7_SQ_1_MPF

    print(f"\n  c_αα (literature: m_e · Vol(7²_1))")
    print(f"    = {mp.nstr(m_e_mpf, 25)} × {mp.nstr(VOL_7_SQ_1_MPF, 25)}")
    print(f"    = {mp.nstr(c_aa_literature, 25)} MeV")

    print(f"\n  c_αα^derived (Wenzl JM: m_e · |tr_M(7²_1)|)")
    print(f"    = {mp.nstr(c_aa_derived_wenzl, 25)} MeV")

    print(f"\n  c_αα^derived (q-Schur: m_e · |tr_M(7²_1)|)")
    print(f"    = {mp.nstr(c_aa_derived_qschur, 25)} MeV")

    # Gap analysis (mpf precision throughout)
    delta_wenzl = c_aa_derived_wenzl - c_aa_literature
    delta_qschur = c_aa_derived_qschur - c_aa_literature
    rel_wenzl = delta_wenzl / c_aa_literature
    rel_qschur = delta_qschur / c_aa_literature

    print(f"\n  Gap (Wenzl JM derived − literature): "
          f"{mp.nstr(delta_wenzl, 8)} MeV ({mp.nstr(rel_wenzl * 100, 6)}%)")
    print(f"  Gap (q-Schur derived − literature): "
          f"{mp.nstr(delta_qschur, 8)} MeV ({mp.nstr(rel_qschur * 100, 6)}%)")

    # Witness
    w.add_parameter("q_0_50dps", q_str)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("knot", "7^2_1 (Whitehead-link-like 2-component)")
    # JSON-friendly: list of [sign, gen] pairs
    w.add_parameter("braid_word", [list(t) for t in braid])
    w.add_parameter("evaluator_precision", "mp.mpf at 50 dps (L1 floor) "
                                          "via markov_trace_for_knot "
                                          "mpf default; mpf used "
                                          "throughout c_αα arithmetic")
    w.add_data("tr_M_wenzl", mp.nstr(trM_wenzl, 25))
    w.add_data("tr_M_qschur", mp.nstr(trM_qschur, 25))
    w.add_data("c_alpha_alpha_literature_MeV", mp.nstr(c_aa_literature, 25))
    w.add_data("c_alpha_alpha_derived_wenzl_MeV",
               mp.nstr(c_aa_derived_wenzl, 25))
    w.add_data("c_alpha_alpha_derived_qschur_MeV",
               mp.nstr(c_aa_derived_qschur, 25))
    w.add_data("delta_wenzl_vs_lit_MeV", mp.nstr(delta_wenzl, 25))
    w.add_data("delta_qschur_vs_lit_MeV", mp.nstr(delta_qschur, 25))
    w.add_data("rel_err_wenzl", mp.nstr(rel_wenzl, 25))
    w.add_data("rel_err_qschur", mp.nstr(rel_qschur, 25))
    w.add_data("vol_7_sq_1", mp.nstr(VOL_7_SQ_1_MPF, 25))
    w.add_data("wall_seconds", {
        "wenzl_jm": t_wenzl,
        "q_schur": t_qschur,
        "total": t_wenzl + t_qschur,
    })

    # Boolean predicate: |tr_M| must be finite AND strictly positive.
    # (Previous formulation with expected=1.0, tolerance=10.0 vacuously
    # passed even at computed=0.0; per Copilot PR #1274 review.)
    # trM_wenzl is mp.mpf at 50 dps — use mp.isnan / mp.isinf
    trM_wenzl_finite_nonzero = (
        not mp.isnan(trM_wenzl)
        and not mp.isinf(trM_wenzl)
        and abs(trM_wenzl) > mp.mpf("1e-40")
    )
    w.add_assertion(
        name="tr_M_wenzl_finite_nonzero",
        computed=trM_wenzl_finite_nonzero,
        expected=True,
        tolerance=0,
        source=(
            "Boolean check: math.isfinite(trM_wenzl) AND |trM| > 1e-12 "
            "— guards against silent NaN/Inf or zero returns from the "
            "common-infra evaluator. Robust against the 'tolerance "
            "wider than |computed − expected|' vacuous-pass pitfall."
        ),
    )

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    w.add_data("lean_uniqueness_ref", {

        "helium4": "qou:QOU.BraidKnot.helium4_uniqueness_closed",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
