#!/usr/bin/env python3
"""
Wire the categorical binding-energy formula into the mass-table pipeline.

The formula (from PR #1307 / deuteron-binding-interface-closure witness):
  B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|

where:
  y_λ = Wenzl Markov weight (from q-Schur or Wenzl bridge)
  χ^λ(β_K) = Hoefsmit character on the FULL braid (include_inter=True)
  sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)} (Lean-proved, commit 25cb9f38)
  f^λ = hook-length formula dim (Lean-proved, commit 60be505b)

CORRECTION (2026-05-29): this formula does NOT close the deuteron. The
bare per-λ sum gives B(D) = 0.380 MeV, off by -82.9% from AME (2.225).
The C_knot below is the deficit ratio B_AME/(m_e·|sum|) = 5.852 — a factor
FITTED to AME, not a derived geometric layer. The earlier "zero free
parameters / interface IS the geometric layer" claim is retracted: the χ^λ
used here is already interface-inclusive (include_inter=True) and still
undershoots by -83%. See docs/audits/2026-05-18-delta-lambda-gating-context.md
(CORRECTION 2026-05-29) and delta-lambda-binding-full-evaluation.witness.json.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import json
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from _precision import set_compute_dps, fmt  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402


def main():
    set_compute_dps()
    t0 = time.perf_counter()
    set_compute_dps()

    m_e = mp.mpf(M_E_MEV)

    print("=" * 70)
    print("  Categorical binding energy: B(K) = m_e × |Σ y_λ χ^λ sgn f^λ|")
    print("=" * 70)
    print()

    # ── Load precomputed sums from interface-closure witness ────
    closure_path = _pb.witness_path("deuteron-binding-interface-closure.witness.json", HERE)
    if closure_path.exists():
        closure = record_upstream(closure_path, _UPSTREAM_RECORDS)
        d = closure.get("data", {})
        sum_with = d.get("sum_with_interface", 0)
        sum_no = d.get("sum_no_interface", 0)
        print(f"From interface-closure witness:")
        print(f"  Σ with interface:    {sum_with}")
        print(f"  Σ without interface: {sum_no}")
        print(f"  Interface flip: {sum_with / sum_no:.4f}×")
        print()

        B_D_AME = AME_B_DEUTERON_MEV_VALIDATION  # AME 2020 deuteron binding (MeV)
        B_D_pred = m_e * abs(mp.mpf(str(sum_with)))
        err_pct = float((B_D_pred - B_D_AME) / B_D_AME * 100)

        print(f"B(D) predicted = m_e × |{sum_with}| = {float(B_D_pred):.6f} MeV")
        print(f"B(D) AME 2020  = {float(B_D_AME):.6f} MeV")
        print(f"Error: {err_pct:+.2f}%")
        print()

        # C_knot is the deficit ratio: how far the bare per-λ sum
        # undershoots AME. It is FITTED (defined as B_AME/(m_e·|sum|)),
        # not derived — see module docstring CORRECTION (2026-05-29).
        C_knot = B_D_AME / (m_e * abs(mp.mpf(str(sum_with))))
        print(f"C_knot(D) = B_AME / (m_e × |sum|) = {float(C_knot):.6f}")
        print(f"  This is a FITTED deficit ratio (B_AME / m_e|sum|), NOT derived.")
        print(f"  The bare per-λ formula is off by {err_pct:+.1f}% — gate still open.")
        print()

        # Build witness
        wb = WitnessBuilder("binding-energy-categorical-deuteron", start_time=t0)
        wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
        wb.data["formula"] = "B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0) · f^λ|"
        wb.data["sum_with_interface"] = str(sum_with)
        wb.data["sum_without_interface"] = str(sum_no)
        wb.data["B_D_pred_MeV"] = fmt(B_D_pred, 12)
        wb.data["B_D_AME_MeV"] = fmt(B_D_AME, 12)
        wb.data["C_knot_deuteron"] = fmt(C_knot, 6)
        wb.data["err_pct"] = f"{err_pct:.4f}"
        wb.data["free_parameters"] = 0
        wb.data["status"] = "delta_lambda_gate_open"
        wb.data["note"] = (
            "RETRACTED (2026-05-29): the per-λ formula does NOT close the deuteron. "
            "Bare B(D) = m_e·|sum| undershoots AME by -82.9%. C_knot = B_AME/(m_e·|sum|) "
            "= 5.852 is a FITTED deficit ratio, not a derived geometric layer; the χ^λ "
            "here is already interface-inclusive (include_inter=True) and still misses "
            "by -83%. The Δ_λ gate remains open. See "
            "docs/audits/2026-05-18-delta-lambda-gating-context.md (CORRECTION 2026-05-29)."
        )
        wb.data["lean_proofs"] = {
            "sgn_formula": "commit 25cb9f38 — (-1)^{n(λ)} = sgn(w_0^{S_{λ'}}), 2712 partitions verified",
            "dim_formula": "commit 60be505b — dim(V_λ) = regular-rep multiplicity (Burnside)",
            "bar_pair_orbit": "commit 0166a17a — factor 2 = |Orb_bar(triv)| (bar-pair orbit size)",
        }

        wb.add_assertion(
            "bare_perlambda_undershoots_deuteron",
            computed=round(err_pct, 1),
            expected=-82.9,
            tolerance=0.5,
            source="Bare per-λ B(D) = m_e·|sum| misses AME by -82.9%; "
                   "C_knot = 5.852 is the FITTED deficit ratio, not a "
                   "derived layer. Δ_λ gate remains open.",
        )
        # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
        wb.add_data("lean_uniqueness_ref", {
            "deuteron": "qou:QOU.BraidKnot.deuteron_uniqueness_closed",
            "framework_doc":
                "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
            "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
        })

        wb.save()
        print(f"✓ Witness: binding-energy-categorical-deuteron.witness.json")
    else:
        print("ERROR: deuteron-binding-interface-closure.witness.json not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
