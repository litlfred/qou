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
    "deuteron":  ("chi-deuteron-h6.witness.json", 6),
    "tritium":   ("chi-tritium-h9.witness.json", 9),
    "helium-3":  ("chi-helium-3-h9.witness.json", 9),
    # 4He already has numeric per_partition; skip
}


def _eval_one(args: tuple) -> dict:
    atom, partition, chi_sym_str = args
    mp.mp.dps = 60
    q = sp.symbols("q", positive=True)
    chi_sym = sp.sympify(chi_sym_str)
    val = chi_sym.subs(q, sp.sympify(Q_MP_STR)).evalf(50)
    if hasattr(val, "as_real_imag"):
        re_val, _ = val.as_real_imag()
        s = str(re_val)
    else:
        s = str(val)
    try:
        _ = mp.mpf(s)
    except (ValueError, TypeError):
        s = str(complex(val).real)
    return {"atom": atom, "partition": list(partition),
            "chi_q_at_q0_50dps": s}


def main() -> int:
    print("=" * 96)
    print("  χ^λ(β_K)(q_0) numeric cache builder (parallel)")
    print("=" * 96)

    tasks = []
    n_lookup = {}
    for atom, (fname, n) in ATOMS_TO_CACHE.items():
        path = HERE / fname
        if not path.exists():
            print(f"  WARN: missing {fname}; skipping {atom}")
            continue
        d = json.loads(path.read_text())
        chi_table = d.get("chi_lambda_symbolic", [])
        n_lookup[atom] = n
        for entry in chi_table:
            tasks.append((atom, tuple(entry["partition"]),
                         entry["chi_q_symbolic"]))
        print(f"  {atom} (n={n}): {len(chi_table)} χ^λ to evaluate")

    if not tasks:
        print(f"  ERROR: no chi witnesses found")
        return 1

    nproc = max(1, cpu_count() - 1)
    print(f"\n  Parallel pool: {nproc} workers, {len(tasks)} tasks total")

    with Pool(nproc) as pool:
        results = pool.map(_eval_one, tasks)

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

    # Sanity-check first row of each atom against full evaluator
    sanity = {}
    q = sp.symbols("q", positive=True)
    for atom in by_atom:
        if not by_atom[atom]:
            continue
        ref_entry = by_atom[atom][0]
        # Re-evaluate from source to confirm
        path = HERE / ATOMS_TO_CACHE[atom][0]
        d = json.loads(path.read_text())
        sym = next((e["chi_q_symbolic"] for e in d["chi_lambda_symbolic"]
                    if tuple(e["partition"]) == tuple(ref_entry["partition"])),
                   None)
        if sym is None:
            continue
        val = sp.sympify(sym).subs(q, sp.sympify(Q_MP_STR)).evalf(50)
        if hasattr(val, "as_real_imag"):
            re_val, _ = val.as_real_imag()
        else:
            re_val = val
        ref_mp = mp.mpf(str(re_val))
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

    from witness_base import WitnessBuilder
    w = (WitnessBuilder("chi-lambda-at-q0", engine="mpmath")
         .set_description(
            "Numeric cache of χ^λ(β_K) at q_0 to 50 dps for atoms "
            "{D, T, ³He}, evaluated from chi-{atom}-h{n}.witness.json "
            "in parallel via multiprocessing.Pool. ⁴He is excluded — "
            "its chi-helium-4-h12.witness.json already carries a "
            "per_partition table with numeric chi_q_at_q0. "
            "Pre-computes the symbolic-to-numeric step for fast "
            "downstream reuse by delta_lambda_empirical_tabulation.py."
         )
         .set_content_block("prop:hecke-branching-trace-decomposition"))
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
