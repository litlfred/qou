#!/usr/bin/env python3
"""derived_chi_catalogue_sweep.py — production isotope sweep.

Multiprocessing-parallel via `derived_chi_catalogue_parallel.parallel_chi_q_via_gp_batch`
to bypass the `pyhecke_native.chi_q_via_gp` GIL hold (~3-Nx speedup on
N-core boxes; see `docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`).

Phase 3 of the catalogue work-plan: builds derived `(K, λ, A)` cells
for **every production isotope × every Wedderburn partition** using the
Rust pyhecke_native backend (Geck-Pfeiffer reduction + Hecke characters).

## Atom registry

Sources the canonical production isotope table from
[`paper_six_term_isotope_sweep.ISOTOPES`](sweeps/paper_six_term_isotope_sweep.py)
(12 light isotopes through ⁹Be). For each `(name, Z, N)`:

  - Strand count `n_strands = 3·A` (3 strands per nucleon)
  - Braid word from `mass_at_3A_proper.atom_braid_word_3A(Z, N)`
  - Partitions enumerated via `pyhecke_native.partitions_of(n_strands)`
  - Character `χ^λ(β_atom)(q)` from `pyhecke_native.chi_q_via_gp`

The Rust backend uses the **Kauffman convention** `t = q²` natively;
all emitted cells carry `q_convention = "kauffman"`.

## Scope control

Per CLAUDE.md long-compute discipline, atom sweeps are gated by
`--max-A` (default 4 — covers p, n, D, T, ³He, ⁴He in ~2 seconds).
Heavier atoms (`A ∈ {5..9}`) take minutes to hours; trigger them via:

    python3 -u derived_chi_catalogue_sweep.py --max-A 9 \\
        2>&1 | tee /tmp/derived_chi_catalogue_sweep_full.log

Progress lines emit every isotope + every 10% of partitions.

## Out of scope

- Heavier isotopes (A > 9) — needs `atom_braid_word_3A` extension
  or a separate registry entry; deferred to follow-up.
- Organic chemistry molecules — the user's eventual target. Will need
  a new (molecule → braid_word) generator; deferred.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke-native" / "python"))

import _path_bridge  # noqa: E402, F401

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import (  # noqa: E402
    DerivedChiCatalogue,
    KnotPartitionAtomCell,
    load_catalogue,
)
from derived_chi_catalogue_parallel import (  # noqa: E402
    parallel_chi_q_via_gp_batch,
)
from derived_chi_catalogue_bar_symmetry_audit import (  # noqa: E402
    conjugate_partition,
    laurent_substitute_bar,
    laurent_negate,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def split_partitions_by_conjugacy(
    parts: list[tuple[int, ...]],
) -> tuple[list[tuple[int, ...]], list[tuple[tuple[int, ...], tuple[int, ...]]]]:
    """Partition a list of λ's into:
      - self-conjugate λ (λᵀ = λ; compute directly)
      - non-self-conjugate pairs (λ, λᵀ) with λ < λᵀ lex
        (compute one, derive the other via bar symmetry)
    """
    seen: set[tuple[int, ...]] = set()
    self_conj: list[tuple[int, ...]] = []
    pairs: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for lam in parts:
        if lam in seen:
            continue
        lam_T = conjugate_partition(lam)
        if lam_T == lam:
            self_conj.append(lam)
            seen.add(lam)
            continue
        # Pick the lex-smaller as the "compute" partition.
        if lam < lam_T:
            pairs.append((lam, lam_T))
        else:
            pairs.append((lam_T, lam))
        seen.add(lam)
        seen.add(lam_T)
    return self_conj, pairs


def derive_conjugate_from_bar_symmetry(
    chi_lambda_pairs: list[tuple[int, str]],
    braid_length: int,
) -> list[tuple[int, str]]:
    """Compute χ^{λᵀ}(T_β) from χ^λ(T_β) via the Hecke bar identity:

        χ^{λᵀ}(T_β) = ε(β) · χ^λ(T_β) | _{q → −q⁻¹},
        ε(β) = (−1)^|β|  (verified empirically; see
        `2026-06-07-bar-symmetry-audit.witness.json`).
    """
    substituted = laurent_substitute_bar(chi_lambda_pairs)
    sign = +1 if (braid_length % 2 == 0) else -1
    if sign == -1:
        return laurent_negate(substituted)
    return substituted


# ── Production isotope registry (mirrors paper_six_term_isotope_sweep.ISOTOPES) ──
# Each entry: (label, Z, N, has_braid_in_production).
# `has_braid_in_production=False` for free p, n (treated as single-nucleon
# trivial braids in the same 3-strand-per-nucleon framework).
# Per the Copilot review on PR #1952: the `codata_mass_MeV` column was
# removed because (a) it was never used in the sweep, and (b) keeping
# hardcoded CODATA-style literals here risks re-introducing P31 audit
# issues if a future agent starts treating them as inputs to the
# binding-energy prediction.
PRODUCTION_ISOTOPES = [
    ("p",   1, 0, False),
    ("n",   0, 1, False),
    ("D",   1, 1, True),
    ("T",   1, 2, True),
    ("3He", 2, 1, True),
    ("4He", 2, 2, True),
    ("5Li", 3, 2, True),
    ("6Li", 3, 3, True),
    ("7Li", 3, 4, True),
    ("7Be", 4, 3, True),
    ("8Be", 4, 4, True),
    ("9Be", 4, 5, True),
]


# ── Braid-word format conversion ───────────────────────────────────

def production_braid_word_to_rust(Z: int, N: int) -> tuple[list[tuple[int, int]], str]:
    """Convert production (c, d, gen_0based) braid triples to the
    pyhecke_native (sign, gen_1based) format expected by chi_q_via_gp.

    Returns (rust_word, pretty_string). Crossings with `d != 0` are
    "averaged" interfaces (e.g. p-n color-weighted); the canonical
    Markov-trace input uses just the sign of c."""
    word_triples = atom_braid_word_3A(Z, N)
    rust_word: list[tuple[int, int]] = []
    pretty_parts: list[str] = []
    for (c, d, gen_0based) in word_triples:
        sign = 1 if c >= 0 else -1
        rust_word.append((sign, gen_0based + 1))
        if sign > 0:
            pretty_parts.append(f"σ_{gen_0based + 1}")
        else:
            pretty_parts.append(f"σ_{gen_0based + 1}^(-1)")
    return rust_word, "·".join(pretty_parts) if len(pretty_parts) < 20 else (
        "·".join(pretty_parts[:8]) + f"·…·({len(pretty_parts)} crossings)"
    )


# ── Per-(atom, partition) derivation ──────────────────────────────


def derive_cell(
    atom_label: str,
    knot_name: str,
    partition: tuple[int, ...],
    n_strands: int,
    rust_word: list[tuple[int, int]],
    braid_pretty: str,
    *,
    derivation_ref: str,
    chi_pairs_precomputed: list[tuple[int, str]] | None = None,
) -> KnotPartitionAtomCell:
    """Derive a single (K, λ, A) cell via pyhecke_native.chi_q_via_gp.

    `chi_pairs_precomputed` lets the caller supply the q-Laurent
    pairs from a batch precompute (e.g. parallel_chi_q_via_gp_batch);
    if None, the per-cell synchronous path is used."""
    if chi_pairs_precomputed is None:
        laurent = ph.chi_q_via_gp(list(partition), n_strands, rust_word)
        chi_pairs: list[tuple[int, str]] = sorted(
            (int(d), str(c)) for (d, c) in laurent
        )
    else:
        chi_pairs = chi_pairs_precomputed
    return KnotPartitionAtomCell(
        knot=knot_name,
        partition=partition,
        atom=atom_label,
        braid_word=braid_pretty,
        strand_count=n_strands,
        chi_lambda_q_laurent=chi_pairs,
        mu_eigenvalues=["?"],
        # Hoefsmit dim = number of SYT of shape lambda; deferred follow-up.
        k_lambda=2,  # default; per-atom SDP decides max-|μ| later
        y_lambda_at_zero="?",  # T18-template extension to atoms is a follow-up
        y_star_shadow_price=None,
        tier="derived",
        q_convention="kauffman",
        derivation_ref=derivation_ref,
        notes=(
            f"Derived via pyhecke_native.chi_q_via_gp (Geck-Pfeiffer reduction "
            f"+ Hecke characters). λ has {len(partition)} parts; braid has "
            f"{len(rust_word)} crossings on {n_strands} strands."
        ),
    )


# ── Main sweep ────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--max-A", type=int, default=4,
        help="Sweep isotopes with mass number A ≤ this (default 4 — light "
             "atoms only, finishes in seconds). A=9 takes hours; run via "
             "`tee /tmp/sweep.log` per CLAUDE.md long-compute discipline.",
    )
    parser.add_argument(
        "--max-partitions-per-atom", type=int, default=0,
        help="Cap partitions per atom (0 = all). Useful for smoke-testing.",
    )
    parser.add_argument(
        "--merge-existing", action="store_true",
        help="Merge into existing catalogue witness instead of rebuilding "
             "from scratch (preserves Phase 2 cells).",
    )
    parser.add_argument(
        "--workers", type=int, default=0,
        help="Worker count for parallel per-partition character computation "
             "(default: os.cpu_count(); 1 = serial). The parallel wrapper "
             "auto-detects whether to use threads (when pyhecke_native "
             "releases the GIL — Patch 1 landed in v0.9.0, see "
             "`docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`) "
             "or processes (older pyhecke_native installs). On a stock "
             "v0.9.0+ install, threads are selected and scale near-linearly "
             "with cpu_count.",
    )
    args = parser.parse_args()
    workers = args.workers if args.workers > 0 else (os.cpu_count() or 1)

    t0 = time.monotonic()
    # Distinct witness name from the Phase 1+2 build script
    # (`derived_chi_catalogue_build.py`, which owns
    # `derived-chi-catalogue.witness.json` carrying the 12-cell T17 /
    # Schur-Weyl cross-check). The production sweep emits the full 715-cell
    # catalogue, so it gets its own `derived-chi-catalogue-sweep.witness.json`
    # — otherwise the two producers clobber one file.
    wb = WitnessBuilder(
        "derived-chi-catalogue-sweep",
        engine="pyhecke-native + python",
        start_time=t0,
    )
    wb.set_description(
        f"Phase 3 production isotope sweep (max-A={args.max_A}). "
        f"Builds derived (K, λ, A) cells for every production isotope × "
        f"every Wedderburn partition via pyhecke_native.chi_q_via_gp. "
        f"Kauffman convention t = q² natively."
    )

    print("=" * 78)
    print(f" derived_chi_catalogue — Phase 3 production sweep (max-A={args.max_A})")
    print("=" * 78)

    if args.merge_existing:
        try:
            cat = load_catalogue()
            print(f"  loaded existing catalogue: {len(cat.cells)} cells ({cat.tier_counts()})")
        except FileNotFoundError:
            cat = DerivedChiCatalogue()
            print("  no existing catalogue — starting fresh")
    else:
        cat = DerivedChiCatalogue()

    initial_count = len(cat.cells)

    derivation_ref = (
        "pyhecke_native.chi_q_via_gp (Geck-Pfeiffer + Hecke characters) on "
        "atom_braid_word_3A from folio-assistant/computations/mass_at_3A_proper.py"
    )

    total_cells_emitted = 0
    atom_summary: dict[str, dict] = {}
    sweep_t0 = time.monotonic()

    for (label, Z, N, has_braid) in PRODUCTION_ISOTOPES:
        A = Z + N
        if A > args.max_A:
            print(f"  ◦ skip {label} (A={A} > max-A={args.max_A})")
            continue

        n_strands = 3 * A if A > 0 else 3  # single-nucleon p, n still get B_3
        knot_name = f"atom-braid-{label}"

        # For p/n with A=1, atom_braid_word_3A may not be defined cleanly;
        # use a trivial 3-strand braid (no crossings → identity).
        if not has_braid or A == 1:
            rust_word: list[tuple[int, int]] = []
            braid_pretty = "Id (no crossings — single-nucleon trivial)"
        else:
            rust_word, braid_pretty = production_braid_word_to_rust(Z, N)

        parts = ph.partitions_of(n_strands)
        if args.max_partitions_per_atom > 0:
            parts = parts[: args.max_partitions_per_atom]

        atom_t0 = time.monotonic()
        atom_cells = 0
        part_tuples = [tuple(p) for p in parts]
        # Tier 3 — split into (self-conjugate, (λ, λᵀ) pairs); only ONE
        # of each pair gets a chi_q_via_gp call. The other is derived
        # via the bar-symmetry identity (verified to 100% on 348 pairs).
        self_conj, pairs_lt_T = split_partitions_by_conjugacy(part_tuples)
        compute_set = list(self_conj) + [lam for (lam, _lT) in pairs_lt_T]
        derived_count = len(pairs_lt_T)
        print(f"  • {label} (Z={Z}, N={N}, A={A}, B_{n_strands}, "
              f"{len(rust_word)} crossings, {len(parts)} partitions, "
              f"workers={workers})", flush=True)
        print(f"      Tier 3: {len(self_conj)} self-conj + {len(pairs_lt_T)} "
              f"non-self-conj pairs ⇒ {len(compute_set)} chi_q_via_gp calls "
              f"+ {derived_count} bar-derived (~{100 * derived_count / max(len(part_tuples), 1):.0f}% saved)",
              flush=True)
        # Parallel batch compute on just the "primary" partition of each pair.
        compute_t0 = time.monotonic()
        chi_results = parallel_chi_q_via_gp_batch(
            partitions=compute_set,
            n_strands=n_strands,
            word=rust_word,
            workers=workers,
        )
        compute_dt = time.monotonic() - compute_t0
        # Tier 3 — derive the λᵀ conjugates via bar identity.
        bar_t0 = time.monotonic()
        for (lam_lo, lam_hi) in pairs_lt_T:
            chi_lo = chi_results[lam_lo]
            chi_results[lam_hi] = derive_conjugate_from_bar_symmetry(
                chi_lo, braid_length=len(rust_word),
            )
        bar_dt = time.monotonic() - bar_t0
        # Materialise cells from the merged result.
        for lam in part_tuples:
            try:
                cell = derive_cell(
                    label, knot_name, lam, n_strands, rust_word,
                    braid_pretty, derivation_ref=derivation_ref,
                    chi_pairs_precomputed=chi_results[lam],
                )
                cat.add(cell)
                atom_cells += 1
                total_cells_emitted += 1
            except ValueError:
                # Cell duplicate from --merge-existing or repeat partition
                pass
        print(f"      batch compute: {compute_dt:.2f}s "
              f"({len(compute_set)} chi_q_via_gp calls) + "
              f"{1000 * bar_dt:.1f}ms bar-derive ({derived_count} pairs)",
              flush=True)
        atom_dt = time.monotonic() - atom_t0
        print(f"      done: {atom_cells} cells in {atom_dt:.2f}s")
        atom_summary[label] = {
            "Z": Z, "N": N, "A": A, "n_strands": n_strands,
            "crossings": len(rust_word), "partitions_swept": len(parts),
            "cells_emitted": atom_cells, "elapsed_seconds": atom_dt,
        }

    sweep_dt = time.monotonic() - sweep_t0

    print()
    print("=" * 78)
    print(" SWEEP COMPLETE")
    print("=" * 78)
    print(f"  cells: {initial_count} → {len(cat.cells)} ({total_cells_emitted} new)")
    print(f"  tier counts: {cat.tier_counts()}")
    print(f"  total sweep wall: {sweep_dt:.2f}s")
    print()
    print(f"  per-atom summary:")
    for label, summary in atom_summary.items():
        print(f"    {label:5s} A={summary['A']:2d} n={summary['n_strands']:3d}  "
              f"cells={summary['cells_emitted']:5d}  t={summary['elapsed_seconds']:6.2f}s")

    # The sweep emits at least one new cell when starting from scratch
    # (no --merge-existing) or when a higher --max-A includes atoms not
    # yet in the catalogue. A no-op re-run with --merge-existing is OK.
    sweep_did_something = total_cells_emitted > 0 or args.merge_existing
    wb.add_assertion(
        "sweep_ran_to_completion",
        computed=sweep_did_something,
        expected=True,
        source="The Phase 3 sweep must either emit new (K, λ, A) cells or "
               "be a no-op re-run with --merge-existing (in which case all "
               "expected cells were already in the catalogue).",
    )

    wb.add_data("catalogue", cat.to_dict())
    wb.add_data("sweep_parameters", {
        "max_A": args.max_A,
        "max_partitions_per_atom": args.max_partitions_per_atom,
        "merge_existing": args.merge_existing,
    })
    wb.add_data("per_atom_summary", atom_summary)
    wb.add_data("sweep_wall_seconds", sweep_dt)
    wb.add_data("backend", "pyhecke_native.chi_q_via_gp (Rust)")

    out = wb.save()
    print()
    print(f"  ✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
