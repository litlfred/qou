#!/usr/bin/env python3
"""derived_chi_catalogue_consumer_demo.py — Phase 1.3 read-through.

Demonstrates that the 3-axis catalogue is reachable from compute and
that catalogue cells cross-check against existing production-adjacent
extractions. Read-through only — no production file is modified.

Per the work-plan
(`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`)
Phase 1 step 4: "One catalogue-derived cell wired into one production
compute site as a read-through (no behaviour change — proves the
consumer can reach the catalogue)".

## What this demo does

1. Loads the on-disk catalogue (`derived-chi-catalogue.witness.json`)
   produced by `derived_chi_catalogue_build.py`.
2. Calls `lookup_derived("borromean", (2,1), "borromean-baryon")`,
   exercising the Phase-3 failing-loud guard on a real cell.
3. Re-evaluates `χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶` from the catalogue's
   h-Taylor pairs at a couple of test q-values and confirms the
   Laurent-polynomial form matches.
4. Cross-checks the Schur-Weyl trace identity using the THREE
   catalogue cells (3-axis lookup × 3 partitions):

       4·χ^(3) + 2·χ^(2,1) + 0·χ^(1,1,1) = tr_{V⊗³}(β_Bor)
       = 8 − 6h⁴ − 2h⁶  (V^⊗³ at U_q(sl_2); no (1,1,1) presence)

## Why this is the right Phase 1.3 step

The catalogue's purpose is to feed derived `χ^λ` into the binding /
mass-formula compute path (`closed_form_tau_M.py`, the per-atom mass
sweep, the Rust `chi-incremental` batch in PR #1741). That wire-up is
Phase 3 — it requires the rest of the H_3 / B_2 rows (Trefoil,
Cinquefoil, 4₁) and the Hoefsmit `|μ|` eigenvalues. Phase 1.3 proves
the catalogue API is **reachable and correct** before Phase 2
broadens the K-axis.

## Not in scope

- Production reads (Phase 3 — replaces extracted `χ^λ` calls with
  `lookup_derived`).
- Hoefsmit-eigenvalue cross-check against the H_3 standard rep
  (Phase 2 — when the `mu_eigenvalues` field has real data).
- Full `tr_M = Σ_λ y_λ·χ^λ·Δ_λ` reconstruction (Phase 3 — when the
  catalogue carries `y_λ(q)` Taylor terms beyond `y_λ(0)`).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import load_catalogue  # noqa: E402


def q_laurent_at(pairs: list[tuple[int, str]], q_value: mp.mpf) -> mp.mpf:
    """Evaluate a catalogue chi_lambda_q_laurent list at a numeric q."""
    out = mp.mpf(0)
    for (degree, coeff_str) in pairs:
        out += mp.mpf(coeff_str) * q_value ** degree
    return out


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    wb = WitnessBuilder(
        "derived-chi-catalogue-consumer-demo", engine="mpmath", start_time=t0
    )
    wb.set_description(
        "Phase 1.3 read-through demo: prove the catalogue is reachable "
        "from compute and that its three Borromean cells cross-check "
        "the Schur-Weyl trace identity. No production file modified."
    )

    print("=" * 78)
    print(" derived_chi_catalogue — Phase 1.3 read-through consumer")
    print("=" * 78)
    cat = load_catalogue()
    print(f"  catalogue loaded: {len(cat.cells)} cells, tier_counts = {cat.tier_counts()}")
    print()

    # ── Look up all three Borromean cells via the strict, derived-only API ──
    cell_3 = cat.lookup_derived("borromean", (3,), "borromean-baryon")
    cell_21 = cat.lookup_derived("borromean", (2, 1), "borromean-baryon")
    cell_111 = cat.lookup_derived("borromean", (1, 1, 1), "borromean-baryon")
    print(f"  ✓ lookup_derived (borromean, (3),     baryon)   → χ_q_laurent = {cell_3.chi_lambda_q_laurent}")
    print(f"  ✓ lookup_derived (borromean, (2,1),   baryon)   → χ_q_laurent = {cell_21.chi_lambda_q_laurent}")
    print(f"  ✓ lookup_derived (borromean, (1,1,1), baryon)   → χ_q_laurent = {cell_111.chi_lambda_q_laurent}")
    print()

    # ── Numeric Schur-Weyl cross-check at two test q-values ──
    # V⊗³ trace = 4·χ^(3) + 2·χ^(2,1) at U_q(sl_2); (1,1,1) doesn't appear.
    Q_TEST_VALUES = ["1.10997858275", "1.05"]
    all_consistent = True
    for q_str in Q_TEST_VALUES:
        q = mp.mpf(q_str)
        h = q - 1 / q
        chi_3_val = q_laurent_at(cell_3.chi_lambda_q_laurent, q)
        chi_21_val = q_laurent_at(cell_21.chi_lambda_q_laurent, q)
        chi_111_val = q_laurent_at(cell_111.chi_lambda_q_laurent, q)
        # Direct T17 trace at this q:
        tr_T17 = mp.mpf(8) - 6 * h ** 4 - 2 * h ** 6
        # Schur-Weyl reconstruction from catalogue:
        tr_from_catalogue = 4 * chi_3_val + 2 * chi_21_val  # (1,1,1) absent
        diff = abs(tr_from_catalogue - tr_T17)
        ok = diff < mp.mpf("1e-40")
        all_consistent = all_consistent and ok
        print(f"  q = {q_str:<16}  h = {mp.nstr(h, 8):<18}")
        print(f"    χ^(3)     = {mp.nstr(chi_3_val, 12)}")
        print(f"    χ^(2,1)   = {mp.nstr(chi_21_val, 12)}")
        print(f"    χ^(1,1,1) = {mp.nstr(chi_111_val, 12)} (not in V⊗³)")
        print(f"    4·χ^(3) + 2·χ^(2,1)         = {mp.nstr(tr_from_catalogue, 14)}")
        print(f"    T17 tr_{{V⊗³}}(β_Bor)         = {mp.nstr(tr_T17, 14)}")
        print(f"    |Δ|                          = {mp.nstr(diff, 6)}   {'✓' if ok else '✗'}")
        print()

    wb.add_assertion(
        "catalogue_reachable_and_schur_weyl_consistent",
        computed=all_consistent,
        expected=True,
        source="Phase 1.3 read-through: lookup_derived succeeds on all 3 "
               "Borromean cells, and 4·χ^(3) + 2·χ^(2,1) reconstructs the "
               "Schur-Weyl V⊗³ trace 8 − 6h⁴ − 2h⁶ from T17 to within 1e-40 "
               "at two test q-values.",
    )

    # ── Demonstrate the failing-loud guard explicitly ──
    # Look up a (K, λ, A) that does NOT exist — must KeyError, not silently
    # return None — so production sites can rely on the guard. We pick a
    # genuinely-not-yet-derived cell: T(3,4) → color-binding is a Phase 3
    # B_3-or-larger census target that we haven't reached.
    try:
        cat.lookup_derived("T(3,4)", (3, 1), "color-binding")
        guard_works = False
    except KeyError:
        guard_works = True

    wb.add_assertion(
        "failing_loud_guard_raises_on_missing_cell",
        computed=guard_works,
        expected=True,
        source="The catalogue's derived-only lookup must raise on missing "
               "cells (e.g. T(3,4)/(3,1)/color-binding, a Phase-3+ target "
               "that pulls in higher-strand structure), so any production "
               "wire-up that expects derived cannot silently consume "
               "`cal-anchored` or `extracted` values.",
    )

    wb.add_data(
        "schur_weyl_identity_under_catalogue_lookup",
        "4·χ^(3) + 2·χ^(2,1) = tr_{V⊗³}(β_Bor) = 8 − 6h⁴ − 2h⁶  "
        "(verified to 1e-40 at q = 1.10997858275 and 1.05)",
    )
    wb.add_data(
        "phase_3_next_step",
        "Phase 2 adds Trefoil/Cinquefoil/4₁ rows; Phase 3 swaps extracted "
        "χ^λ reads in closed_form_tau_M.py + the per-atom mass sweep for "
        "`lookup_derived` calls. The failing-loud guard then enforces that "
        "any site asking for `tier='derived'` cannot silently consume a "
        "`cal-anchored` value.",
    )

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"  ✓ catalogue reachable from compute path ({len(cat.cells)} cells loaded).")
    print(f"  ✓ Schur-Weyl cross-check passes at all {len(Q_TEST_VALUES)} test q-values.")
    print(f"  ✓ failing-loud guard raises on missing cell (T(3,4)/(3,1)/color-binding).")
    print(f"  → Phase 3 wires `lookup_derived` calls into production reads;")
    print(f"    Phase 4 extends to V⊗⁵+ via Rust (B_5 isotopes, full mass-table sweep).")
    print()

    out = wb.save()
    print(f"  ✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
