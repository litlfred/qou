#!/usr/bin/env python3
"""derived_chi_catalogue_production_wire_demo.py — Phase 3 production wire-up.

Demonstrates the pattern for replacing inline `chi_lambda_braid` / `chi_q_via_gp`
calls in production scripts with catalogue `lookup_derived` reads, using a
production-equivalent computation (Markov trace for atomic Tritium braids).

## Wire-up pattern

For a production script that currently does

    for atom in ISOTOPES:
        word = atom_braid_word_3A(Z, N)
        for lam in pyhecke_native.partitions_of(n_strands):
            chi = pyhecke_native.chi_q_via_gp(lam, n_strands, word)
            ...

replace the inner call with

    from derived_chi_catalogue import load_catalogue
    cat = load_catalogue()
    for atom in ISOTOPES:
        for lam in pyhecke_native.partitions_of(n_strands):
            try:
                cell = cat.lookup_derived(f"atom-braid-{atom}", lam, atom)
                chi = cell.chi_lambda_q_laurent  # q-Laurent, exact, derived
            except KeyError:
                # Catalogue miss → compute fresh (and consider adding to catalogue)
                chi = pyhecke_native.chi_q_via_gp(lam, n_strands, word)

This demo runs both paths side-by-side on the Tritium (A=3, n=9) braid and
verifies the catalogue cells exactly match the direct chi_q_via_gp output.

## Why "wire" matters

Per the work-plan
(`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`)
Phase 3: "Replace the relevant extracted `χ^λ` reads in
`closed_form_tau_M.py` / per-atom mass-table sweep with catalogue reads."

The failing-loud guard `cat.lookup_derived(K, λ, A)` raises if the cell has
`tier != "derived"`. Production sites can therefore claim derived provenance
on their L2 dashboards (per CLAUDE.md Precision goals); any cal-anchored
fallback surfaces as a raise rather than a silent circular value.

## What this demo asserts

For every λ ⊢ 9 in the production Tritium catalogue:

  catalogue.lookup_derived("atom-braid-T", λ, "T").chi_lambda_q_laurent
    ==
  pyhecke_native.chi_q_via_gp(λ, 9, atom_braid_word_3A(1, 2))

If any mismatch — the wire-up is unsafe. If all match — the wire-up is
ready to land in `closed_form_tau_M.py` and the per-atom sweep.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import load_catalogue  # noqa: E402
from derived_chi_catalogue_sweep import production_braid_word_to_rust  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder(
        "derived-chi-catalogue-production-wire-demo",
        engine="python+pyhecke_native",
        start_time=t0,
    )
    wb.set_description(
        "Phase 3 production wire-up demo. For every λ ⊢ 9 in the Tritium "
        "catalogue, verifies `catalogue.lookup_derived` returns the same "
        "q-Laurent as a direct `pyhecke_native.chi_q_via_gp` call. If all "
        "pass, the wire-up pattern is safe to roll out to `closed_form_tau_M.py` "
        "and the per-atom mass-table sweep."
    )

    print("=" * 78)
    print(" Phase 3 production wire-up demo (Tritium, A=3, n=9)")
    print("=" * 78)

    cat = load_catalogue()
    print(f"  catalogue: {len(cat.cells)} cells loaded")

    # Tritium production data.
    Z, N = 1, 2
    A = Z + N
    n_strands = 3 * A
    rust_word, braid_pretty = production_braid_word_to_rust(Z, N)
    print(f"  Tritium braid: {braid_pretty}")
    print(f"  strand count: {n_strands}")
    print(f"  crossings: {len(rust_word)}")

    parts = [tuple(p) for p in ph.partitions_of(n_strands)]
    print(f"  partitions of {n_strands}: {len(parts)}")
    print()

    matches = 0
    catalogue_misses = 0
    compute_mismatches = 0
    timings = {"catalogue_lookup_total": 0.0, "direct_compute_total": 0.0}

    for lam in parts:
        # Catalogue path (the "wire-up" pattern)
        t_cat = time.monotonic()
        try:
            cell = cat.lookup_derived("atom-braid-T", lam, "T")
            catalogue_chi = cell.chi_lambda_q_laurent
        except KeyError:
            catalogue_chi = None
            catalogue_misses += 1
        timings["catalogue_lookup_total"] += time.monotonic() - t_cat

        # Direct-compute baseline (the "old" pattern)
        t_compute = time.monotonic()
        direct_raw = ph.chi_q_via_gp(list(lam), n_strands, rust_word)
        direct_chi = sorted((int(d), str(c)) for (d, c) in direct_raw)
        timings["direct_compute_total"] += time.monotonic() - t_compute

        if catalogue_chi is None:
            continue  # miss — counted above
        if sorted(catalogue_chi) == direct_chi:
            matches += 1
        else:
            compute_mismatches += 1

    print(f"  results:")
    print(f"    matches:              {matches} / {len(parts)}")
    print(f"    catalogue misses:     {catalogue_misses}")
    print(f"    compute mismatches:   {compute_mismatches}")
    print()
    print(f"  timing:")
    print(f"    catalogue lookups:    {1000 * timings['catalogue_lookup_total']:.2f} ms")
    print(f"    direct compute:       {1000 * timings['direct_compute_total']:.2f} ms")
    speedup = (timings["direct_compute_total"]
               / max(timings["catalogue_lookup_total"], 1e-9))
    print(f"    speedup (wire vs raw): {speedup:.1f}×")
    print()

    safe_to_wire = (
        compute_mismatches == 0
        and catalogue_misses == 0
        and matches == len(parts)
    )
    wb.add_assertion(
        "wire_up_safe_for_tritium",
        computed=safe_to_wire,
        expected=True,
        source="Every catalogue.lookup_derived for (atom-braid-T, λ, T) must "
               "exactly match pyhecke_native.chi_q_via_gp for all λ ⊢ 9. "
               "If all match, the wire-up pattern is safe to roll out to "
               "closed_form_tau_M.py and the per-atom mass-table sweep.",
    )

    wb.add_data("partitions_total", len(parts))
    wb.add_data("matches", matches)
    wb.add_data("catalogue_misses", catalogue_misses)
    wb.add_data("compute_mismatches", compute_mismatches)
    wb.add_data("catalogue_lookup_ms", 1000 * timings["catalogue_lookup_total"])
    wb.add_data("direct_compute_ms", 1000 * timings["direct_compute_total"])
    wb.add_data("speedup", speedup)
    wb.add_data(
        "interpretation",
        f"{matches}/{len(parts)} cells match direct compute; wire-up "
        f"speedup {speedup:.1f}× (catalogue replaces "
        f"{timings['direct_compute_total']:.2f}s of GP reduction with "
        f"{timings['catalogue_lookup_total']*1000:.2f}ms of dict lookups). "
        "Production sites can now adopt the lookup_derived pattern "
        "with confidence."
    )

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if safe_to_wire:
        print(f"  ★ SAFE TO WIRE — {matches}/{len(parts)} cells verified, ")
        print(f"    {speedup:.0f}× speedup from catalogue lookup vs direct compute.")
        print(f"    Next: replace chi_q_via_gp calls in closed_form_tau_M.py + per-atom sweep.")
    else:
        print(f"  UNSAFE — {compute_mismatches} mismatches, {catalogue_misses} misses.")
        print(f"    Wire-up NOT ready; investigate before adopting in production.")

    out = wb.save()
    print()
    print(f"  ✓ Witness: {out.name}")
    return 0 if safe_to_wire else 1


if __name__ == "__main__":
    sys.exit(main())
