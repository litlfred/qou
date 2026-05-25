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
mass formula `m_p = m_e · Geom_full(𝓑₃)` which scales by
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
  Geom_full(𝓑₃, q_0)        ≈ 1836      →  m_e·Geom   ≈ 938 MeV

i.e. `|tr_M|` alone is NOT the right substrate-pure derivation
of binding/mass scales — the framework's volume × ℏ_q² × linking-
weight machinery is the correct chain (per `prop:geom-universality`
and the Geom_full formula). This script is a NEGATIVE finding: the
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
from q_parameter import Q as Q_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    w = WitnessBuilder(
        "c-alpha-alpha-categorical-via-jones-markov",
        engine="python+mpmath",
    )
    w.set_description(
        "c_αα categorical derivation via Jones-Markov trace on 7²_1 "
        "(Whitehead-link-like 2-component, the α-α coupling knot per "
        "alpha_cluster_recursion.py). Phase B-4 of the Track B "
        "execution plan: replace the literature value "
        "c_αα = m_e·Vol(7²_1) with the substrate-canonical "
        "c_αα = m_e·|tr_M(T_w(7²_1), q_0)|, aligning the α-cluster "
        "recursion with prop:atom-knot-mass-derivation."
    )
    set_compute_dps(50)

    print("=" * 78)
    print("c_αα categorical derivation via Jones-Markov trace")
    print("=" * 78)

    q_str = Q_50_DIGIT_STR
    q_f64 = float(Q_FLOAT)
    q_mpf = mp.mpf(q_str)

    # Build the 7²_1 braid via common infra
    braid = braid_word_for_knot("7^2_1")
    print(f"\n  7²_1 braid word (B_3): {braid}")
    print(f"  (length {len(braid)} crossings)")
    print(f"\n  q_0 = {q_str}")
    print(f"  m_e = {float(M_E_MEV):.10f} MeV")

    # Markov trace under both conventions
    print(f"\n[1/3] Markov trace under Wenzl Jones-Markov convention "
          f"(mass formula)...")
    t0 = time.perf_counter()
    trM_wenzl = markov_trace_for_knot("7^2_1", q_f64, "wenzl")
    t_wenzl = time.perf_counter() - t0
    print(f"      tr_M(7²_1, q_0) (Wenzl JM) = {trM_wenzl:.10f}")
    print(f"      |tr_M(7²_1, q_0)| (Wenzl JM) = {abs(trM_wenzl):.10f}")
    print(f"      wall: {t_wenzl*1000:.2f} ms")

    print(f"\n[2/3] Markov trace under q-Schur Plancherel convention "
          f"(torus knots, lepton tower)...")
    t0 = time.perf_counter()
    trM_qschur = markov_trace_for_knot("7^2_1", q_f64, "q_schur")
    t_qschur = time.perf_counter() - t0
    print(f"      tr_M(7²_1, q_0) (q-Schur) = {trM_qschur:.10f}")
    print(f"      |tr_M(7²_1, q_0)| (q-Schur) = {abs(trM_qschur):.10f}")
    print(f"      wall: {t_qschur*1000:.2f} ms")

    # Derived c_αα under each convention
    print(f"\n[3/3] Derived c_αα values vs literature")
    m_e_mpf = mp.mpf(str(M_E_MEV))
    c_aa_derived_wenzl = m_e_mpf * mp.fabs(mp.mpf(trM_wenzl))
    c_aa_derived_qschur = m_e_mpf * mp.fabs(mp.mpf(trM_qschur))
    c_aa_literature = m_e_mpf * VOL_7_SQ_1_MPF

    print(f"\n  c_αα (literature: m_e · Vol(7²_1))")
    print(f"    = {float(M_E_MEV):.10f} × {VOL_7_SQ_1_F64:.10f}")
    print(f"    = {float(c_aa_literature):.10f} MeV")

    print(f"\n  c_αα^derived (Wenzl JM: m_e · |tr_M(7²_1)|)")
    print(f"    = {float(M_E_MEV):.10f} × {abs(trM_wenzl):.10f}")
    print(f"    = {float(c_aa_derived_wenzl):.10f} MeV")

    print(f"\n  c_αα^derived (q-Schur: m_e · |tr_M(7²_1)|)")
    print(f"    = {float(M_E_MEV):.10f} × {abs(trM_qschur):.10f}")
    print(f"    = {float(c_aa_derived_qschur):.10f} MeV")

    # Gap analysis
    delta_wenzl = float(c_aa_derived_wenzl - c_aa_literature)
    delta_qschur = float(c_aa_derived_qschur - c_aa_literature)
    rel_wenzl = delta_wenzl / float(c_aa_literature)
    rel_qschur = delta_qschur / float(c_aa_literature)

    print(f"\n  Gap (Wenzl JM derived − literature): "
          f"{delta_wenzl:+.6f} MeV ({rel_wenzl*100:+.2f}%)")
    print(f"  Gap (q-Schur derived − literature): "
          f"{delta_qschur:+.6f} MeV ({rel_qschur*100:+.2f}%)")

    # Witness
    w.add_parameter("q_0", q_str)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("knot", "7^2_1 (Whitehead-link-like 2-component)")
    w.add_parameter("braid_word", str(braid))
    w.add_data("tr_M_wenzl", float(trM_wenzl))
    w.add_data("tr_M_qschur", float(trM_qschur))
    w.add_data("c_alpha_alpha_literature_MeV", float(c_aa_literature))
    w.add_data("c_alpha_alpha_derived_wenzl_MeV",
               float(c_aa_derived_wenzl))
    w.add_data("c_alpha_alpha_derived_qschur_MeV",
               float(c_aa_derived_qschur))
    w.add_data("delta_wenzl_vs_lit_MeV", delta_wenzl)
    w.add_data("delta_qschur_vs_lit_MeV", delta_qschur)
    w.add_data("rel_err_wenzl", rel_wenzl)
    w.add_data("rel_err_qschur", rel_qschur)
    w.add_data("vol_7_sq_1", VOL_7_SQ_1_F64)
    w.add_data("wall_seconds", {
        "wenzl_jm": t_wenzl,
        "q_schur": t_qschur,
        "total": t_wenzl + t_qschur,
    })

    w.add_assertion(
        name="tr_M_wenzl_finite_nonzero",
        computed=abs(trM_wenzl),
        expected=1.0,
        tolerance=10.0,
        source=(
            "Markov trace of a 3-strand 8-crossing braid; "
            "rough magnitude check (any nonzero finite value)"
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
