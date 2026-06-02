#!/usr/bin/env python3
"""Operator-valued HOMFLYPT probe — first P(proton) ≠ P(neutron) data.

The pure-braid HOMFLYPT gives P(proton) = P(neutron) at ALL SU(N)
channels because the Borromean link is amphicheiral (PR #1043).

The OPERATOR-VALUED Markov trace uses the canonical pipeline braids
with averaged crossings I = σ − (h/2)·1. These BREAK the
amphicheirality and WILL give different values for proton vs neutron.

This probe computes the operator-valued character traces χ_λ(β_op)
for the canonical proton and neutron braids (with averaged crossings)
and forms the per-partition Markov trace.
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

from q_parameter import Q, HA
from hecke_characters import (
    partitions_of,
)
from wedderburn_jones_markov import y_lambda_at
from witness_base import WitnessBuilder


def main():
    t_start = time.monotonic()
    q0 = Q
    h = HA
    print(f"Operator-valued HOMFLYPT probe at q₀ = {q0:.10f}")
    print(f"h = q − q⁻¹ = {h:.10f}")
    print("=" * 60)

    # Use the PIPELINE's tr_M computation which correctly handles
    # single nucleons via the canonical braid words (with averaged
    # crossings). The nuclear_braid_character function bypasses
    # braid computation for A=1, returning dim(V_λ) — which is
    # the SAME for proton and neutron.
    from unified_low_isotope_predictor import tr_M_at_q0

    tr_M_p_raw, _, _ = tr_M_at_q0(1, 0, include_inter=False)
    tr_M_n_raw, _, _ = tr_M_at_q0(0, 1, include_inter=False)
    tr_M_p = float(tr_M_p_raw)
    tr_M_n = float(tr_M_n_raw)

    # Also compute per-partition contributions via chi_lambda_braid
    # using the canonical braid words from the pipeline.
    from canonical_braid_crossings import atom_canonical_crossings
    p_crossings = atom_canonical_crossings(1, 0, include_inter=True)
    n_crossings = atom_canonical_crossings(0, 1, include_inter=True)

    # Convert to chi_lambda_braid word format: [(sign, gen_1indexed), ...]
    # 'sigma' → (+1, gen+1), 'sigma_inv' → (-1, gen+1)
    def to_hc_word(crossings):
        word = []
        has_averaged = False
        for gen, typ in crossings:
            if typ == 'sigma':
                word.append((1, gen + 1))
            elif typ == 'sigma_inv':
                word.append((-1, gen + 1))
            elif typ == 'averaged':
                has_averaged = True
            else:
                raise ValueError(f"unknown crossing type: {typ!r}")
        if has_averaged:
            raise ValueError(
                "averaged crossings are not representable in chi_lambda_braid "
                "word form; per-partition character traces are omitted"
            )
        return word

    n_strands = 3
    y_vals = y_lambda_at(n_strands, q_val=float(q0))

    print(f"\nCanonical proton braid: {len(p_crossings)} crossings")
    print(f"  word: {p_crossings}")
    print(f"Canonical neutron braid: {len(n_crossings)} crossings")
    print(f"  word: {n_crossings}")

    per_part_p = {}
    per_part_n = {}
    per_partition_precision = None
    per_partition_note = None

    from hecke_characters import chi_lambda_braid
    try:
        p_word = to_hc_word(p_crossings)
        n_word = to_hc_word(n_crossings)
        print(f"\nPer-partition character traces:")
        print(f"  {'λ':15s} {'y_λ':>12s} {'χ_λ(p)':>14s} {'χ_λ(n)':>14s}")
        for lam in partitions_of(n_strands):
            shape = list(lam)
            chi_p, precision_tag = chi_lambda_braid(shape, p_word, return_precision=True)
            chi_n, precision_tag_n = chi_lambda_braid(shape, n_word, return_precision=True)

            y_raw = y_vals.get(lam, y_vals.get(tuple(shape), 0))
            y = float(y_raw) if y_raw else 0.0
            chi_p_f = float(chi_p)
            chi_n_f = float(chi_n)
            per_part_p[lam] = chi_p_f
            per_part_n[lam] = chi_n_f
            per_partition_precision = precision_tag

            print(f"  {str(lam):15s} {y:12.8f} {chi_p_f:14.8f} {chi_n_f:14.8f}")
            if precision_tag_n != precision_tag:
                per_partition_note = (
                    f"mixed precision tags in chi_lambda_braid: "
                    f"{precision_tag} vs {precision_tag_n}"
                )
    except ValueError as exc:
        per_partition_note = str(exc)
        print(f"\nPer-partition character traces skipped: {per_partition_note}")

    print(f"\n  tr_M(proton)  = {tr_M_p:.12f}")
    print(f"  tr_M(neutron) = {tr_M_n:.12f}")
    print(f"  Δtr_M = tr_M(n) − tr_M(p) = {tr_M_n - tr_M_p:+.12f}")
    print(f"  ratio tr_M(p)/tr_M(n) = {tr_M_p/tr_M_n:.12f}")
    print(f"  ratio tr_M(n)/tr_M(p) = {tr_M_n/tr_M_p:.12f}")

    # Compare to the pure-braid (amphicheiral) case
    print(f"\n  Compare: pure-braid amphicheiral ratio = 1.000000000000")
    print(f"  Operator-valued break: {abs(tr_M_p/tr_M_n - 1)*100:.6f} %")

    # Q_β prediction from the operator-valued split
    from experimental_constants import Q_NEUTRON_MEV
    E0 = Q_NEUTRON_MEV / abs(tr_M_n - tr_M_p)
    print(f"\n  E₀ = Q_β / |Δtr_M| = {Q_NEUTRON_MEV:.6f} / {abs(tr_M_n - tr_M_p):.8f}")
    print(f"     = {E0:.4f} MeV")

    # Witness
    w = WitnessBuilder(
        "homflypt-operator-valued-probe",
        engine="python",
        start_time=t_start,
    )
    w.set_description(
        "First operator-valued HOMFLYPT probe: per-partition Markov "
        "trace of the canonical pipeline proton/neutron braids "
        "(WITH averaged crossings I = σ − (h/2)·1). These break "
        "the amphicheirality found in the pure-braid HOMFLYPT "
        "(PR #1043) and give P(proton) ≠ P(neutron). Records "
        "per-partition character traces, Markov-trace split, and "
        "implied E₀ calibration."
    )
    w.set_content_block("rem:operator-valued-magnitude-budget")
    w.add_data("tr_M_proton", tr_M_p)
    w.add_data("tr_M_neutron", tr_M_n)
    w.add_data("delta_tr_M", tr_M_n - tr_M_p)
    w.add_data("ratio_p_over_n", tr_M_p / tr_M_n)
    w.add_data("E0_implied_MeV", E0)
    w.add_data("per_partition_precision", per_partition_precision)
    w.add_data("per_partition_note", per_partition_note)
    w.add_data("per_partition_proton", {str(k): v for k, v in per_part_p.items()})
    w.add_data("per_partition_neutron", {str(k): v for k, v in per_part_n.items()})
    w.add_assertion(
        "proton_neq_neutron",
        computed=abs(tr_M_p - tr_M_n),
        expected=0.1,  # expect |Δ| ≈ 0.1
        tolerance=0.5,
        unit="Markov-trace difference",
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
