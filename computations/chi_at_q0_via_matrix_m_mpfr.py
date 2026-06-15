#!/usr/bin/env python3
"""chi_at_q0_via_matrix_m_mpfr.py — fast per-λ chi at q_0 producer
for the **sign-only chi_q_via_gp braid convention** (matches the
derived_chi_catalogue cells emitted by PR #1952 + #1980).

## Scope — important distinction

The repo has TWO production paths for computing χ^λ at the
substrate:

  1. **sign-only / Geck-Pfeiffer / `chi_q_via_gp`**: takes a braid
     word as `(sign, gen)` pairs — every crossing is ±1. This is
     what `derived_chi_catalogue` (715 cells) stores. My matrix-M
     backend (PR #1980 → #2000) matches this convention exactly.

  2. **averaged crossings**: `chi_at_q0_via_hoefsmit_mpfr.py` calls
     `_chi_lambda_of_word_mpf` with `atom_braid_word_3A(Z, N)`'s
     full `(c, d, gen_0based)` triples — the d ≠ 0 entries weight
     crossings by per-color factors. Different physics, different
     character values.

This producer is **NOT a drop-in replacement** for the hoefsmit
producer — the chi values won't match (verified empirically: on
deuteron the two paths give χ^(6) = 1.56 vs 11.02 = q_0^23 at q_0 ≈
1.11). The two represent different braid encodings.

What this producer IS: a fast generator of per-λ chi caches in the
chi_q_via_gp convention, suitable for downstream consumers that
want the SAME chi values stored in the derived_chi_catalogue (or
that consume those catalogue cells at q_0).

## Output

`chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json` —
producer field is `"matrix-m-chi-q-via-gp"` for provenance.

## Performance

Per the matrix-M tier benchmarks (PR #1993, #2000):

- ⁴He aggregate is 1.34× faster than direct Rust `chi_q_via_gp`
- ⁴He λ=(12) is **56-68× faster** than Rust for dim-1 reps
- All dim-1 partitions scale flat in n

The direct Rust `chi_q_via_gp` path computes per-partition Rust
character values; this matrix-M producer does the same compute
on `μ_p`-block-restricted matrices (max size ≤ 4 for deuteron, ≤
~25 for ⁴He), independent of dim V_λ.

## NO f64 in compute path

`mpmath.mpf` at the canonical `set_compute_dps()` precision (default
50 dps from `_precision`). Substrate q_0 as
`mpmath.mpf(Q_50_DIGIT_STR)`. Same discipline as PR #1993/#2000.

## Δ_λ-gate

Wire-in only — reuses the matrix-M trace identity (PR #1980 →
#2000). No new ansatz, no fit, no calibration parameter.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402

from derived_chi_catalogue_matrix_m_mpfr import (  # noqa: E402
    precompute_block_tables_mpfr,
    chi_via_numerical_matrix_m_mpfr,
    chi_rust_at_q_mpf,
)
from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a  # noqa: E402


def _save_partial(out_path: Path, payload: dict) -> None:
    """Atomic incremental save (per the hoefsmit producer convention)."""
    tmp = out_path.with_suffix(out_path.suffix + ".partial")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    tmp.replace(out_path)


def _split_atom_braid(Z: int, N: int) -> tuple[
    int, list[tuple[int, int]], int, list[tuple[int, int]]
]:
    """Split `atom_braid_word_3A(Z, N)` at first bridge σ_3.

    Returns (n_strands, word_left, bridge_sign, word_right) — the
    same parabolic shape consumed by the matrix-M backend's
    `chi_via_numerical_matrix_m_mpfr`.
    """
    n_strands, word = _word_for_braid_word_3a(Z, N)
    word_left = [t for t in word if t[1] <= 2]
    bridge = [t for t in word if t[1] == 3]
    word_right = [t for t in word if t[1] >= 4]
    if not bridge:
        # A=1 case (single nucleon) — no σ_3 bridge. Caller falls back
        # to the hoefsmit producer for these (single-nucleon caches are
        # already cheap there).
        raise ValueError(
            f"atom_braid_word_3A({Z}, {N}) has no σ_3 bridge — single-"
            f"nucleon braid (A=1) is not parabolic. Use the hoefsmit "
            f"producer for this atom."
        )
    # The matrix-M trace identity (audit §5) requires exactly ONE σ_3
    # bridge — the parabolic split at k_split = 3 isolates the proton
    # block from everything beyond. Multiple σ_3 crossings would mix
    # the blocks and invalidate the single-block formula.
    if len(bridge) != 1:
        raise ValueError(
            f"atom_braid_word_3A({Z}, {N}) has {len(bridge)} crossings "
            f"at the σ_3 bridge ({bridge}); the matrix-M trace identity "
            f"requires exactly one bridge crossing."
        )
    bridge_sign = bridge[0][0]
    return n_strands, word_left, bridge_sign, word_right


def build_chi_cache_at_q0_matrix_m(
    atom_name: str, Z: int, N: int, q_str: str, *, dps: int = 50,
    max_dim: int | None = None,
) -> dict:
    """Per-λ χ^λ(β_atomic(Z, N); q_0) via the matrix-M mpfr backend.

    Iterates partitions of n = 3(Z+N), uses the pre-cached block
    tables per shape, saves incrementally. Format mirrors the
    hoefsmit producer so downstream consumers swap in transparently.

    LOSSLESS BY DEFAULT (`max_dim=None`): EVERY partition λ ⊢ n is
    computed, so `tr_M_at_q0 = Σ_λ y_λ χ^λ` is the COMPLETE trace at
    1-ppQ precision. Required by the precision discipline — there is
    NO exact-χ selection rule (every λ has a nonzero character at the
    generic full-crossing atom braid), so dropping any partition is a
    truncation of unknown size, NOT a free omission (owner directive
    2026-06-10; see
    `docs/audits/2026-06-10-binding-active-set-compute-optimization.md`).

    `max_dim` (opt-in, EXPLORATORY only): when set to an int, partitions
    with dim V_λ > max_dim are SKIPPED with a placeholder entry. This
    makes `tr_M_at_q0` a TRUNCATED value — the payload is then flagged
    `tr_M_partial: true` with `n_skipped_max_dim`, so no consumer
    mistakes it for the complete 1-ppQ trace. Use only for fast smoke
    tests where ~1e-3 error is acceptable; never for production binding
    / Δ_λ.

    Wall-clock note: the cost is the full dim×dim seminormal build in
    `precompute_block_tables_mpfr` (pure-Python mpmath, ~0.1 s/dim²·
    word_length); the block-restricted CALL is cheap (≤~40 indep. of
    dim V_λ). The lossless O(reduced-block) path that never forms the
    dim×dim matrices is the #2062 Tier-3 follow-up; until it lands the
    lossless default eats the dim×dim build cost (minutes for n≥9).
    """
    n = 3 * (Z + N)
    if Z + N < 2:
        raise ValueError(
            f"atom A={Z+N} < 2: matrix-M producer requires a σ_3 bridge; "
            f"use chi_at_q0_via_hoefsmit_mpfr for single-nucleon atoms."
        )
    n_strands, word_left, bridge_sign, word_right = _split_atom_braid(Z, N)
    assert n_strands == n, f"strand count mismatch: {n_strands} vs {n}"

    q = mp.mpf(q_str)
    # Filename + payload keys parameterised by dps so --dps=70 doesn't
    # collide with the 50dps cache.
    out_path = HERE / f"chi-{atom_name}-h{n}-at-q0-{dps}dps-matrix-m.witness.json"
    # Reuse existing cache if present (incremental resume).
    already: dict[tuple, dict] = {}
    if out_path.exists():
        try:
            prior = json.loads(out_path.read_text())
            for entry in prior.get("by_partition", []):
                key = tuple(entry["partition"])
                already[key] = entry
        except (json.JSONDecodeError, KeyError):
            pass

    y_table = _load_y_lambda(n, None)
    shapes = list(parts_of(n))
    per_partition: list[dict] = []
    running_total = mp.mpf(0)
    t0 = time.time()

    from murnaghan_nakayama import dim_specht
    n_skipped = 0
    for shape in shapes:
        shape_t = tuple(shape)
        if shape_t in already:
            entry = already[shape_t]
            was_skipped = entry.get("chi_lambda") == "skipped-max-dim"
            if not was_skipped:
                # Real cached value — always reuse (lossless).
                per_partition.append(entry)
                running_total += mp.mpf(entry["contribution"])
                continue
            # Cached entry is a skip placeholder. Reuse it ONLY if this
            # run would also skip it (explicit cap still exceeded);
            # otherwise fall through and (re)compute it losslessly.
            if max_dim is not None and entry.get("dim", 0) > max_dim:
                n_skipped += 1
                per_partition.append(entry)
                continue
        # Lossless default (max_dim=None): never skip — compute every λ.
        # Explicit cap (exploratory): skip high-dim λ with a placeholder
        # and flag the trace partial. Cheap O(n) hook-length dim check
        # up-front avoids building the seminormal matrices when skipping.
        if max_dim is not None and dim_specht(shape_t) > max_dim:
            n_skipped += 1
            per_partition.append({
                "partition": list(shape_t),
                "dim": dim_specht(shape_t),
                "y_lambda": "skipped-max-dim",
                "chi_lambda": "skipped-max-dim",
                "contribution": "0",
                "compute_time_sec": 0.0,
            })
            continue
        # y_lam check BEFORE the expensive block-table precompute and
        # matrix-M evaluation (per Gemini review on PR #2004).
        y_lam = y_table.get(shape_t)
        if y_lam is None:
            continue

        t_part = time.time()
        cache = precompute_block_tables_mpfr(shape_t, 3, q)
        chi = chi_via_numerical_matrix_m_mpfr(
            shape_t, word_left, bridge_sign, word_right, cache,
        )
        # Pull dim from the cache's block sizes.
        dim = sum(b["size"] for b in cache["blocks"].values())
        contrib = y_lam * chi
        running_total += contrib

        entry = {
            "partition": list(shape_t),
            "dim": dim,
            "y_lambda": str(y_lam),
            "chi_lambda": str(chi),
            "contribution": str(contrib),
            "compute_time_sec": round(time.time() - t_part, 3),
        }
        per_partition.append(entry)

        def _payload(*, resume_partial: bool) -> dict:
            """Build the cache payload from the current running state.
            `resume_partial` flags an in-progress incremental save (not
            all shapes visited yet); `tr_M_partial` flags the DISTINCT
            condition that the trace omits skipped high-dim λ (explicit
            `max_dim` cap → truncated, NOT 1-ppQ)."""
            return {
                "computation": f"chi-{atom_name}-h{n}-at-q0-{dps}dps-matrix-m",
                "description": (
                    f"Numerical χ^λ_q(β_atomic({Z}, {N})) = {atom_name} per "
                    f"partition λ ⊢ {n}, evaluated at q = q_0 at {dps} dps "
                    f"via the matrix-M block-restricted mpfr backend (PR "
                    f"#1993). Convention: sign-only crossings — matches "
                    f"`chi_q_via_gp` and the derived_chi_catalogue cells. "
                    f"NOT a drop-in for the hoefsmit averaged-crossing "
                    f"producer (different physics). Built incrementally. "
                    f"Lossless (every λ) unless max_dim is set."
                ),
                "producer": "matrix-m-chi-q-via-gp",
                "convention": "sign-only-crossings",
                f"q_0_{dps}dps": str(q),
                "dps": dps,
                "n_strands": n,
                "atom": atom_name,
                "Z": Z, "N": N,
                "n_partitions": len(per_partition),
                "n_partitions_total": len(shapes),
                "max_dim": max_dim,
                "n_skipped_max_dim": n_skipped,
                "tr_M_partial": n_skipped > 0,
                "partial": resume_partial,
                "compute_time_sec_so_far": round(time.time() - t0, 2),
                "tr_M_at_q0": str(running_total),
                "by_partition": per_partition,
            }

        _save_partial(out_path,
                      _payload(resume_partial=len(per_partition) < len(shapes)))
        print(f"    λ={shape_t!s:25} dim={dim:>3}  "
              f"+{entry['compute_time_sec']:>6.3f}s  "
              f"({len(per_partition)}/{len(shapes)})", flush=True)

    elapsed = time.time() - t0
    # Final save: guarantees trailing skip placeholders + the final
    # n_skipped / tr_M_partial flags land in the cache even when the last
    # partition was skipped (no per-compute save fired). Lossless default
    # ⇒ no skips ⇒ this persists the complete trace.
    final = {
        "computation": f"chi-{atom_name}-h{n}-at-q0-{dps}dps-matrix-m",
        "description": (
            f"Numerical χ^λ_q(β_atomic({Z}, {N})) = {atom_name} per "
            f"partition λ ⊢ {n} at q_0, {dps} dps, matrix-M mpfr backend. "
            f"Lossless (every λ) unless max_dim is set."
        ),
        "producer": "matrix-m-chi-q-via-gp",
        "convention": "sign-only-crossings",
        f"q_0_{dps}dps": str(q),
        "dps": dps,
        "n_strands": n,
        "atom": atom_name,
        "Z": Z, "N": N,
        "n_partitions": len(per_partition),
        "n_partitions_total": len(shapes),
        "max_dim": max_dim,
        "n_skipped_max_dim": n_skipped,
        "tr_M_partial": n_skipped > 0,
        "partial": False,
        "compute_time_sec": round(elapsed, 2),
        "tr_M_at_q0": str(running_total),
        "by_partition": per_partition,
    }
    _save_partial(out_path, final)
    return {
        "atom": atom_name,
        "Z": Z, "N": N,
        "n_strands": n,
        "n_partitions": len(per_partition),
        "n_partitions_total": len(shapes),
        "n_skipped_max_dim": n_skipped,
        "tr_M_partial": n_skipped > 0,
        "tr_M_at_q0": str(running_total),
        "compute_time_sec": round(elapsed, 2),
        "out_path": str(out_path),
    }


def save_witness(record: dict, start_time: float) -> Path:
    """Emit the provenance witness for `record`. `start_time` is the
    `time.monotonic()` captured BEFORE the compute began — passed to
    WitnessBuilder so the emitted `durationMs` reflects the actual
    matrix-M compute wall, not just the WitnessBuilder construct+save
    time (which is microseconds and meaningless on its own)."""
    wb = WitnessBuilder(
        f"chi-at-q0-matrix-m-{record['atom']}",
        engine="python",
        start_time=start_time,
    )
    wb.set_description(
        f"Per-λ χ^λ(β_atomic({record['Z']}, {record['N']}); q_0) cache "
        f"for {record['atom']} via the matrix-M mpfr backend. Format "
        f"matches `chi_at_q0_via_hoefsmit_mpfr.py` so downstream "
        f"consumers swap transparently. NO f64 in compute path."
    )
    wb.add_data("atom", record["atom"])
    wb.add_data("lean_uniqueness_ref", lean_uniqueness_ref(record["atom"]))
    wb.add_data("Z", record["Z"])
    wb.add_data("N", record["N"])
    wb.add_data("n_strands", record["n_strands"])
    wb.add_data("n_partitions", record["n_partitions"])
    wb.add_data("tr_M_at_q0", record["tr_M_at_q0"])
    wb.add_data("compute_time_sec", record["compute_time_sec"])
    wb.add_data("cache_path", record["out_path"])
    return wb.save()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "atoms", nargs="*",
        help="Atoms to build (default: deuteron — single-isotope smoke "
             "test). One of: " + ", ".join(ATOMS),
    )
    parser.add_argument(
        "--dps", type=int, default=50,
        help="Working mpmath precision in decimal places. The substrate "
             "constant Q_50_DIGIT_STR has only 50 digits, so dps > 50 "
             "doesn't increase the substrate accuracy; you would also "
             "need a higher-precision substrate source. dps < 50 is "
             "rejected (the catalogue / matrix-M tolerance bound is "
             "10^-45 at dps=50; lower would not be safe).",
    )
    parser.add_argument(
        "--max-dim", type=int, default=None,
        help="EXPLORATORY truncation: skip partitions with dim V_λ > this. "
             "DEFAULT None = LOSSLESS (compute every λ — the complete "
             "1-ppQ trace; required for production binding / Δ_λ). Set an "
             "int ONLY for fast smoke tests; the resulting tr_M is then "
             "TRUNCATED (flagged tr_M_partial in the cache) because there "
             "is no exact-χ selection rule — every λ contributes.",
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error(
            f"--dps {args.dps} < 50: the substrate Q_50_DIGIT_STR has 50 "
            f"digits and the matrix-M tolerance is 10^-(dps-5). dps must "
            f"be ≥ 50 for safe agreement with the catalogue."
        )

    if not args.atoms:
        # Default to deuteron only — fastest comparison vs hoefsmit
        # producer, finishes in seconds.
        atoms = ["deuteron"]
    else:
        atoms = [ATOM_ALIASES.get(a, a) for a in args.atoms]

    mp.mp.dps = args.dps
    q_str = Q_50_DIGIT_STR
    print("=" * 80)
    print(" Building numerical χ^λ caches at q_0 via matrix-M mpfr backend")
    print(f" q_0 = {Q_50_DIGIT_STR}")
    print("=" * 80)
    print(f"  {'atom':>10}  {'n':>3}  {'n_parts':>10}  "
          f"{'tr_M(q_0)':>22}  {'time':>10}")
    print("  " + "-" * 70)

    last_record = None
    q_mpf = mp.mpf(q_str)
    for atom_name in atoms:
        if atom_name not in ATOMS:
            print(f"  {atom_name}: not in ATOMS, skip")
            continue
        Z, N = ATOMS[atom_name]
        if Z + N < 2:
            print(f"  {atom_name}: A=1 single nucleon, use hoefsmit producer")
            continue
        atom_start = time.monotonic()
        try:
            record = build_chi_cache_at_q0_matrix_m(
                atom_name, Z, N, q_str, dps=args.dps,
                max_dim=args.max_dim,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"  {atom_name:>10}  ERROR  {type(exc).__name__}: {exc}")
            continue
        save_witness(record, start_time=atom_start)
        n_parts = record["n_partitions"]
        tr_m_short = record["tr_M_at_q0"][:22]
        print(f"  {atom_name:>10}  {record['n_strands']:>3}  "
              f"{n_parts:>10}  {tr_m_short:>22}  "
              f"{record['compute_time_sec']:>9.2f}s")
        last_record = record

        # Cross-validate against Rust chi_q_via_gp at q_0 (the
        # canonical sign-only path my matrix-M matches).
        n_strands, word = _word_for_braid_word_3a(Z, N)
        cache_data = json.loads(
            (HERE / f"chi-{atom_name}-h{n_strands}-at-q0-{args.dps}dps-matrix-m.witness.json").read_text()
        )
        tol = mp.mpf(10) ** -(args.dps - 5)
        n_match = 0
        n_total = 0
        n_skipped = 0
        for entry in cache_data["by_partition"]:
            if entry["chi_lambda"] == "skipped-max-dim":
                n_skipped += 1
                continue
            shape = tuple(entry["partition"])
            chi_mpf = mp.mpf(entry["chi_lambda"])
            chi_rust = chi_rust_at_q_mpf(shape, n_strands, word, q_mpf)
            n_total += 1
            if abs(chi_mpf - chi_rust) < tol:
                n_match += 1
        cap_note = (f"dim > {args.max_dim}" if args.max_dim is not None
                    else "lossless: none")
        print(f"  {'':>10}     cross-check vs chi_q_via_gp at q_0: "
              f"{n_match}/{n_total} match (tol 1e-{args.dps-5}), "
              f"{n_skipped} skipped ({cap_note})")

    return 0 if last_record is not None else 1


if __name__ == "__main__":
    sys.exit(main())
