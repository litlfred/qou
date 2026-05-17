#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical χ^λ at q = q_0, not symbolic.
"""Numerical per-irrep χ^λ_q(β_atomic) cache at q_0 (50 dps).

Optimization of the symbolic chi cache emitted by
`per_irrep_pole_atom.py` for callers that only need the canonical
|tr_M| at q_0 (e.g. `canonical_tr_m_via_chi_cache.py`,
`cross_check_trM_1ppb.py`'s third path). The symbolic cache
remains the source of truth for pole-order analysis
(`prop:per-nucleon-shift-additive-linearity` via q → u²
substitution); this script provides the **numerical-only**
counterpart, built **~100× faster** by skipping the symbolic poly
arithmetic.

The per-λ χ^λ values are extracted from the existing
[`tr_M_via_wenzl_bridge_mpfr`](./tr_m_wenzl_bridge_mpfr.py) call
with `return_breakdown=True`. That function already computes
χ^λ(β; q_0) in the Hoefsmit seminormal basis at 50 dps for every
λ ⊢ n; we just expose the per-λ table.

Per-atom timing (single-thread, mpmath @ 50 dps):
  - proton/neutron (H_3, 3 partitions): seconds
  - deuteron (H_6, 11 partitions): seconds
  - tritium / ³He (H_9, 30 partitions): minutes
  - ⁴He (H_12, 77 partitions): tens of minutes — feasible

Output: `chi-{atom}-h{n}-at-q0-50dps.witness.json` — separate from
the symbolic `chi-{atom}-h{n}.witness.json`. The `canonical_tr_m_via_chi_cache.py`
combiner prefers the numerical cache when present.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf,
    _chi_lambda_of_word_mpf,
    _load_y_lambda,
    tr_M_via_wenzl_bridge_mpfr,
)
from witness_base import WitnessBuilder  # noqa: E402


def _save_partial(out_path: Path, payload: dict) -> None:
    """Atomic incremental save — write to a temp file, then rename
    so an interrupt mid-write can't leave the witness corrupted.
    """
    tmp = out_path.with_suffix(out_path.suffix + ".partial")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    tmp.replace(out_path)


def build_chi_cache_at_q0(
    atom_name: str, Z: int, N: int, q_str: str, *, dps: int = 50,
    incremental: bool = True,
) -> dict:
    """Return per-λ χ^λ(β_atomic(Z, N); q_0) at 50 dps.

    When ``incremental=True`` (default), loops over partitions of n
    one at a time, building Hoefsmit seminormal matrices at q = q_0
    numerically and computing the per-partition χ. Each completed
    partition is **persisted to disk immediately** via
    `chi-{atom}-h{n}-at-q0-50dps.witness.json`, so a SIGTERM /
    timeout / OOM mid-loop preserves the work done so far.
    Re-running picks up where it left off.

    When ``incremental=False``, falls through to a single call to
    `tr_M_via_wenzl_bridge_mpfr(return_breakdown=True)` — faster for
    small atoms (no per-iteration JSON write overhead) but loses all
    work on interrupt. Used by tests and the cheap-atom default.
    """
    n = 3 * (Z + N)
    word = atom_braid_word_3A(Z, N)
    t0 = time.time()

    if not incremental:
        result = tr_M_via_wenzl_bridge_mpfr(
            word, n, q_str, dps=dps, return_breakdown=True,
        )
        elapsed = time.time() - t0
        return {
            "atom": atom_name,
            "Z": Z, "N": N,
            "n_strands": n,
            "n_partitions": result["n_partitions_used"],
            "compute_time_sec": round(elapsed, 2),
            "tr_M_at_q0": result["tr_M"],
            "by_partition": result["by_partition"],
        }

    # Incremental path — partition-by-partition with per-step save.
    out_path = HERE / f"chi-{atom_name}-h{n}-at-q0-50dps.witness.json"
    already: dict[tuple, dict] = {}
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        for entry in existing.get("by_partition", []):
            already[tuple(entry["partition"])] = entry
        if already:
            print(f"    resume: {len(already)} partition(s) already cached")

    with mp.workdps(dps):
        q = mp.mpf(q_str)
        y_table = _load_y_lambda(n, None)
        shapes = list(parts_of(n))
        per_partition: list[dict] = []
        running_total = mp.mpf(0)

        for shape in shapes:
            shape_t = tuple(shape)
            if shape_t in already:
                per_partition.append(already[shape_t])
                running_total += mp.mpf(already[shape_t]["contribution"])
                continue
            t_part = time.time()
            sigmas, dim = _build_seminormal_matrices_mpf(shape_t, q)
            if dim == 0:
                continue
            chi = _chi_lambda_of_word_mpf(sigmas, dim, word, q=q)
            y_lam = y_table.get(shape_t)
            if y_lam is None:
                continue
            contrib = y_lam * chi
            running_total += contrib
            entry = {
                "partition": list(shape_t),
                "dim": dim,
                "y_lambda": str(y_lam),
                "chi_lambda": str(chi),
                "contribution": str(contrib),
                "compute_time_sec": round(time.time() - t_part, 2),
            }
            per_partition.append(entry)
            # Incremental save (atomic rename — interrupt-safe).
            payload = {
                "computation": f"chi-{atom_name}-h{n}-at-q0-50dps",
                "description": (
                    f"Numerical χ^λ_q(β_atomic({Z}, {N})) = {atom_name} per "
                    f"partition λ ⊢ {n}, evaluated at q = q_0 at {dps} dps via "
                    f"the Hoefsmit seminormal basis. Built incrementally — "
                    f"each completed partition is persisted immediately, so "
                    f"a SIGTERM/timeout mid-loop preserves work done so far. "
                    f"Re-running picks up cached partitions and computes the "
                    f"remaining ones."
                ),
                "q_0_50dps": str(q),
                "dps": dps,
                "n_strands": n,
                "atom": atom_name,
                "Z": Z, "N": N,
                "n_partitions": len(per_partition),
                "n_partitions_total": len(shapes),
                "partial": len(per_partition) < len(shapes),
                "compute_time_sec_so_far": round(time.time() - t0, 2),
                "tr_M_at_q0": str(running_total),
                "by_partition": per_partition,
            }
            _save_partial(out_path, payload)
            print(f"    λ={shape_t!s:20} dim={dim:>3}  +{entry['compute_time_sec']:>5.1f}s  "
                  f"({len(per_partition)}/{len(shapes)})")

    elapsed = time.time() - t0
    return {
        "atom": atom_name,
        "Z": Z, "N": N,
        "n_strands": n,
        "n_partitions": len(per_partition),
        "compute_time_sec": round(elapsed, 2),
        "tr_M_at_q0": str(running_total),
        "by_partition": per_partition,
    }


def save_witness(record: dict) -> Path:
    """Persist the per-atom numerical cache as
    `chi-{atom}-h{n}-at-q0-50dps.witness.json`."""
    atom_name = record["atom"]
    n = record["n_strands"]
    out = HERE / f"chi-{atom_name}-h{n}-at-q0-50dps.witness.json"
    payload = {
        "computation": f"chi-{atom_name}-h{n}-at-q0-50dps",
        "description": (
            f"Numerical χ^λ_q(β_atomic({record['Z']}, {record['N']})) "
            f"= {atom_name} per partition λ ⊢ {n}, evaluated at q = q_0 "
            f"at 50 decimal places via the Hoefsmit seminormal basis. "
            f"Companion to the symbolic chi-{atom_name}-h{n}.witness.json "
            f"emitted by per_irrep_pole_atom.py; this numerical cache is "
            f"used by canonical_tr_m_via_chi_cache.py and the 3-way "
            f"1ppb cross-check (cross_check_trM_1ppb.py) when full "
            f"symbolic data is not yet available. ~100× faster to build "
            f"than the symbolic counterpart (no sympy poly arithmetic)."
        ),
        "q_0_50dps": str(mp.mpf(repr(Q_0_FLOAT))),
        "dps": 50,
        "n_strands": n,
        "atom": atom_name,
        "Z": record["Z"], "N": record["N"],
        "n_partitions": record["n_partitions"],
        "compute_time_sec": record["compute_time_sec"],
        "tr_M_at_q0": record["tr_M_at_q0"],
        "by_partition": record["by_partition"],
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "atoms", nargs="*",
        help="Atoms to build (default: tritium, helium-3 — the ones with "
             "partial symbolic caches). One of: " + ", ".join(ATOMS),
    )
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    if not args.atoms:
        atoms = ["tritium", "helium-3"]
    else:
        atoms = [ATOM_ALIASES.get(a, a) for a in args.atoms]

    mp.mp.dps = args.dps
    q_str = repr(Q_0_FLOAT)
    print("=" * 80)
    print(f" Building numerical χ^λ caches at q_0 (50 dps)")
    print(f" q_0 = {Q_0_FLOAT}")
    print("=" * 80)
    print(f"  {'atom':>9}  {'n':>3}  {'n_partitions':>14}  {'tr_M(q_0)':>22}  {'time':>10}")
    print("  " + "-" * 70)

    for atom_name in atoms:
        if atom_name not in ATOMS:
            print(f"  {atom_name}: not in ATOMS, skip")
            continue
        Z, N = ATOMS[atom_name]
        try:
            record = build_chi_cache_at_q0(atom_name, Z, N, q_str, dps=args.dps)
        except Exception as exc:  # noqa: BLE001
            print(f"  {atom_name:>9}  ERROR  {type(exc).__name__}: {exc}")
            continue
        out_path = save_witness(record)
        n_parts = record["n_partitions"]
        tr_m_short = record["tr_M_at_q0"][:22]
        print(f"  {atom_name:>9}  {record['n_strands']:>3}  "
              f"{n_parts:>14}  {tr_m_short:>22}  "
              f"{record['compute_time_sec']:>9.2f}s")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
