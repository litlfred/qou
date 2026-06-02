#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic χ^λ
# polynomials live upstream in chi-{atom}-h{n}.witness.json.
"""One-shot cache of χ^λ(β_K)(q_0) numeric values for the canonical atoms
{D, T, ³He, ⁴He}.

The chi-{atom}-h{n}.witness.json files (D / T / ³He) carry the
χ^λ(β_K) Hoefsmit-symbolic forms but no numeric q_0 evaluation — each
expression is up to 14k characters and `evalf(50)` can take 10s+
per partition serially.  The ⁴He witness already includes a
`per_partition` table with numeric `chi_q_at_q0`.

This script does the symbolic → numeric evaluation **once** for
D / T / ³He, parallelised across CPU cores, and writes the 50-dps
strings to `chi-lambda-at-q0.witness.json` for fast downstream
reuse by `delta_lambda_empirical_tabulation.py`.

Output: `chi-lambda-at-q0.witness.json` keyed by atom →
list of {partition, chi_q_at_q0_50dps}.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from multiprocessing import Pool, cpu_count
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 60

from q_parameter import Q_MP  # noqa: E402

Q_MP_STR = str(Q_MP)


ATOMS_TO_CACHE = {
    "deuteron":  {"witness": "chi-deuteron-h6.witness.json",
                  "n": 6, "Z": 1, "N": 1},
    "tritium":   {"witness": "chi-tritium-h9.witness.json",
                  "n": 9, "Z": 1, "N": 2},
    "helium-3":  {"witness": "chi-helium-3-h9.witness.json",
                  "n": 9, "Z": 2, "N": 1},
    # 4He already has numeric per_partition; skip
}


def _compute_and_eval(args: tuple) -> dict:
    """Worker: either lambdify-evaluate a cached symbolic χ^λ string,
    OR compute it from scratch via hoefsmit_symbolic.chi_lambda_symbolic
    given the canonical braid word, then lambdify-evaluate.

    Args: (atom, partition_tuple, sym_str_or_None, crossings_or_None).
    If sym_str is provided, just evaluate.  Otherwise compute symbolically
    first (slow path, parallelised across atoms × partitions).
    """
    atom, partition, sym_str, crossings = args
    mp.mp.dps = 60
    if sym_str is not None:
        chi_sym = sp.sympify(sym_str)
    else:
        # On-the-fly symbolic computation in worker.
        from hoefsmit_symbolic import chi_lambda_symbolic
        chi_sym = chi_lambda_symbolic(partition, crossings)
        sym_str = str(chi_sym)
    free = list(chi_sym.free_symbols)
    if not free:
        val = complex(chi_sym)
        return {"atom": atom, "partition": list(partition),
                "chi_q_at_q0_50dps": mp.nstr(mp.mpf(val.real), 50,
                                              strip_zeros=False),
                "newly_computed": sym_str if crossings is not None else None}
    q_sym = free[0]
    chi_func = sp.lambdify(q_sym, chi_sym, modules=["mpmath"])
    q0 = mp.mpf(Q_MP_STR)
    val = chi_func(q0)
    if hasattr(val, "imag") and abs(val.imag) > mp.mpf("1e-30"):
        re_val = val.real
    elif hasattr(val, "real"):
        re_val = val.real
    else:
        re_val = val
    # Per Copilot PR #619 review: trim to exactly 50 dps via mp.nstr
    # so the field name matches stored precision (was ~60 dps).
    s = mp.nstr(re_val, 50, strip_zeros=False)
    return {"atom": atom, "partition": list(partition),
            "chi_q_at_q0_50dps": s,
            "newly_computed": sym_str if crossings is not None else None}


def _gather_or_compute_chi(atom: str, info: dict) -> list[tuple]:
    """Return list of (atom, partition, sym_str_or_None, crossings_or_None).

    For partitions cached in the witness, sym_str is the symbolic form
    and crossings is None (workers just evaluate).  For missing
    partitions, sym_str is None and crossings is the canonical word
    (workers compute symbolically + evaluate, parallelised).
    """
    n = info["n"]
    Z = info["Z"]; N = info["N"]
    fname = info["witness"]
    path = HERE / fname
    cached_symbolic: dict[tuple, str] = {}
    if path.exists():
        d = json.loads(path.read_text())
        for entry in d.get("chi_lambda_symbolic", []):
            cached_symbolic[tuple(entry["partition"])] = entry["chi_q_symbolic"]
    print(f"  {atom} (n={n}): {len(cached_symbolic)} cached χ^λ in witness")

    from schur_weyl_symbolic import partitions_of
    all_partitions = [tuple(p) for p in partitions_of(n)]
    missing = [p for p in all_partitions if p not in cached_symbolic]
    print(f"    {len(missing)} missing — workers will compute symbolically")

    crossings = None
    if missing:
        from canonical_braid_crossings import atom_canonical_crossings
        crossings = atom_canonical_crossings(Z, N)

    return [(atom, p,
             cached_symbolic.get(p),
             None if p in cached_symbolic else crossings)
            for p in all_partitions]


def main() -> int:
    # Construct WitnessBuilder up front to capture full durationMs
    # (Copilot PR #619 review).
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("chi-lambda-at-q0", engine="mpmath")
         .set_description(
            "Numeric cache of χ^λ(β_K) at q_0 to 50 dps for atoms "
            "{D, T, ³He}, evaluated from chi-{atom}-h{n}.witness.json "
            "in parallel via multiprocessing.Pool. ⁴He is excluded — "
            "its chi-helium-4-h12-numeric.witness.json already carries a "
            "per_partition table with numeric chi_q_at_q0. "
            "Pre-computes the symbolic-to-numeric step for fast "
            "downstream reuse by delta_lambda_empirical_tabulation.py. "
            "Output strings trimmed to exactly 50 dps via mp.nstr."
         )
         .set_content_block("prop:hecke-branching-trace-decomposition"))

    print("=" * 96)
    print("  χ^λ(β_K)(q_0) numeric cache builder (parallel)")
    print("=" * 96)

    tasks = []
    n_lookup = {}
    for atom, info in ATOMS_TO_CACHE.items():
        n_lookup[atom] = info["n"]
        atom_tasks = _gather_or_compute_chi(atom, info)
        tasks.extend(atom_tasks)

    if not tasks:
        print(f"  ERROR: no chi witnesses or computable atoms")
        return 1

    nproc = max(1, cpu_count() - 1)
    print(f"\n  Parallel pool: {nproc} workers, {len(tasks)} tasks total")
    n_compute = sum(1 for t in tasks if t[2] is None)
    print(f"  ({n_compute} tasks need on-the-fly symbolic χ computation)")

    # Use imap_unordered with chunksize=1 to balance load across
    # workers (slow on-the-fly computes get spread evenly with
    # fast cached evaluations).
    with Pool(nproc) as pool:
        results = []
        for i, r in enumerate(pool.imap_unordered(_compute_and_eval, tasks,
                                                   chunksize=1)):
            results.append(r)
            if (i + 1) % 5 == 0:
                print(f"    progress: {i+1}/{len(tasks)} done")

    # Group by atom
    by_atom: dict[str, list[dict]] = {}
    for r in results:
        by_atom.setdefault(r["atom"], []).append({
            "partition": r["partition"],
            "chi_q_at_q0_50dps": r["chi_q_at_q0_50dps"],
        })

    print(f"\n  Per-atom summary:")
    for atom in sorted(by_atom.keys()):
        print(f"    {atom:<10}: {len(by_atom[atom])} χ^λ cached")

    # Sanity-check first row of each atom — re-evaluate via lambdify
    # (the same path used by _eval_one) to confirm consistency.
    sanity = {}
    for atom in by_atom:
        if not by_atom[atom]:
            continue
        ref_entry = by_atom[atom][0]
        path = HERE / ATOMS_TO_CACHE[atom]["witness"]
        if not path.exists():
            continue
        d = json.loads(path.read_text())
        sym = next((e["chi_q_symbolic"] for e in d["chi_lambda_symbolic"]
                    if tuple(e["partition"]) == tuple(ref_entry["partition"])),
                   None)
        if sym is None:
            continue  # Computed-on-the-fly partition; no witness ref to compare
        sym_expr = sp.sympify(sym)
        free = list(sym_expr.free_symbols)
        if not free:
            ref_mp = mp.mpf(str(complex(sym_expr).real))
        else:
            f = sp.lambdify(free[0], sym_expr, modules=["mpmath"])
            v = f(mp.mpf(Q_MP_STR))
            ref_mp = mp.mpf(str(v.real if hasattr(v, "real") else v))
        cached_mp = mp.mpf(ref_entry["chi_q_at_q0_50dps"])
        rel_err = abs(cached_mp - ref_mp) / abs(ref_mp) if abs(ref_mp) > 0 else mp.mpf(0)
        sanity[atom] = {
            "lambda": ref_entry["partition"],
            "ref_chi": str(ref_mp),
            "cached_chi": str(cached_mp),
            "rel_err": str(rel_err),
            "agrees": float(rel_err) < 1e-15,
        }
        tag = "✓" if float(rel_err) < 1e-15 else "✗"
        print(f"    {tag} {atom} λ={ref_entry['partition']}: rel_err = {mp.nstr(rel_err, 6)}")

    # WitnessBuilder constructed at start of main(); now populate.
    w.parameters.update({
        "q_0": Q_MP_STR,
        "precision_dps": 50,
        "atoms": list(by_atom.keys()),
        "n_per_atom": n_lookup,
        "n_total_chi": len(tasks),
    })
    w.add_data("by_atom", by_atom)
    w.add_data("sanity_check", sanity)
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
