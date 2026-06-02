#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic y_λ
# polynomials live upstream in y-lambda-wenzl-bridge-symbolic-witness.json.
"""One-shot cache of y_λ(q_0) numeric values for n ∈ {2, ..., 12}.

The Wenzl-bridge symbolic y_λ(q) polynomials in
[`y-lambda-wenzl-bridge-symbolic-witness.json`](y-lambda-wenzl-bridge-symbolic-witness.json)
have raw lengths up to 45k characters per partition for n = 12,
making `evalf(50)` evaluation slow (~10 seconds per partition for
n = 12, so ~13 minutes for all 77 partitions of 12 in series).

This script does the symbolic → numeric evaluation **once**,
parallelised across CPU cores via `multiprocessing.Pool`, and
writes the 50-dps decimal strings to
`y-lambda-at-q0.witness.json` for fast downstream reuse by
`delta_lambda_empirical_tabulation.py` and any other ρ_K consumer.

Output: `y-lambda-at-q0.witness.json` keyed by n → list of
{partition, y_at_q0_50dps}.
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

mp.mp.dps = 60   # eval headroom; we serialise the leading 50 dps

from q_parameter import Q_MP  # noqa: E402

Q_MP_STR = str(Q_MP)


def _eval_one(args: tuple) -> dict:
    """Worker: evaluate one symbolic y_λ(q) at q = q_0 to 50 dps.

    Uses sympy.lambdify(modules='mpmath') for fast, correct
    numeric evaluation.  The plain `subs(q, ...).evalf()` path
    was broken because sympify creates a fresh `q` symbol whose
    assumptions differ from the explicit `positive=True` symbol;
    substitution silently fails to match across the assumption
    boundary, leaving the expression unevaluated.  lambdify
    bypasses that pitfall by binding the symbol via signature
    matching.
    """
    n, partition, y_sym_str = args
    mp.mp.dps = 60
    y_sym = sp.sympify(y_sym_str)
    free = list(y_sym.free_symbols)
    if not free:
        # Constant (e.g. y_λ ≡ 0 or scalar).
        val = complex(y_sym)
        return {"n": n, "partition": list(partition),
                "y_at_q0_50dps": str(mp.mpf(val.real))}
    # Use the free symbol from the sympified expression directly.
    q_sym = free[0]
    y_func = sp.lambdify(q_sym, y_sym, modules=["mpmath"])
    q0 = mp.mpf(Q_MP_STR)
    val = y_func(q0)
    # mpmath returns mpf for real, mpc for complex
    if hasattr(val, "imag") and abs(val.imag) > mp.mpf("1e-30"):
        # genuine complex residual; take real part
        re_val = val.real
    elif hasattr(val, "real"):
        re_val = val.real
    else:
        re_val = val
    # Per Copilot PR #619 review: trim to exactly 50 dps so the field
    # name ("y_at_q0_50dps") matches the stored precision (was ~60 dps).
    s = mp.nstr(re_val, 50, strip_zeros=False)
    return {"n": n, "partition": list(partition), "y_at_q0_50dps": s}


def main() -> int:
    # Construct WitnessBuilder up front to capture full durationMs
    # (Copilot PR #619 review).
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("y-lambda-at-q0", engine="mpmath")
         .set_description(
            "Numeric cache of y_λ(q_0) at 50 dps for n ∈ {2, ..., 12}, "
            "evaluated from y-lambda-wenzl-bridge-symbolic-witness.json "
            "in parallel via multiprocessing.Pool. Pre-computes the "
            "expensive symbolic-to-numeric step so downstream consumers "
            "(delta_lambda_empirical_tabulation.py and other ρ_K "
            "Wedderburn-weighted formulas) can load instantly. "
            "Output strings trimmed to exactly 50 dps via mp.nstr."
         )
         .set_content_block("prop:y-lambda-closed-form-wenzl-bridge"))

    print("=" * 96)
    print("  y_λ(q_0) numeric cache builder (parallel)")
    print("=" * 96)

    src = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    if not src.exists():
        print(f"  ERROR: missing source witness {src}")
        return 1
    d = json.loads(src.read_text())
    tab = d["tables_by_n"]

    # Build worker tasks: (n, partition_tuple, sym_str)
    tasks = []
    for n_str, entry in sorted(tab.items(), key=lambda kv: int(kv[0])):
        n = int(n_str)
        # Don't shadow the WitnessBuilder `w` defined above with the
        # loop variable (Copilot PR #619 review pre-emptively dodged).
        for wt in entry["weights"]:
            tasks.append((n, tuple(wt["partition"]), wt["y_lambda_symbolic"]))
    print(f"  Tasks: {len(tasks)} y_λ evaluations across n ∈ "
          f"{[int(k) for k in tab.keys()]}")
    nproc = max(1, cpu_count() - 1)
    print(f"  Parallel pool: {nproc} workers")

    with Pool(nproc) as pool:
        results = pool.map(_eval_one, tasks)

    # Group by n
    by_n: dict[int, list[dict]] = {}
    for r in results:
        by_n.setdefault(r["n"], []).append({
            "partition": r["partition"],
            "y_at_q0_50dps": r["y_at_q0_50dps"],
        })

    print(f"\n  Per-n summary:")
    for n in sorted(by_n.keys()):
        print(f"    n = {n:>2}: {len(by_n[n])} partitions cached")

    # Sanity-check a few values against existing per-atom witnesses.
    sanity = {}
    spot_files = {
        "deuteron": ("chi-deuteron-h6.witness.json", 6),
        "tritium": ("chi-tritium-h9.witness.json", 9),
        "helium-3": ("chi-helium-3-h9.witness.json", 9),
        "helium-4": ("chi-helium-4-h12-numeric.witness.json", 12),
    }
    for atom, (fname, n) in spot_files.items():
        path = HERE / fname
        if not path.exists():
            continue
        try:
            ad = json.loads(path.read_text())
            # 4He has per_partition with y_at_q0; others don't (chi only)
            ref = None
            if "per_partition" in ad:
                # take the first non-zero contribution
                for entry in ad["per_partition"]:
                    if abs(float(entry.get("y_at_q0", "0"))) > 1e-30:
                        ref = (tuple(entry["partition"]),
                               mp.mpf(entry["y_at_q0"]))
                        break
            if ref is None:
                continue
            ref_lam, ref_val = ref
            cached = next((r for r in by_n[n]
                          if tuple(r["partition"]) == ref_lam), None)
            if cached is None:
                continue
            cached_val = mp.mpf(cached["y_at_q0_50dps"])
            rel_err = abs(cached_val - ref_val) / abs(ref_val)
            sanity[atom] = {
                "lambda": list(ref_lam),
                "ref_y_at_q0": str(ref_val),
                "cached_y_at_q0": str(cached_val),
                "rel_err": str(rel_err),
                "agrees_to_1e_minus_15": float(rel_err) < 1e-15,
            }
            tag = "✓" if float(rel_err) < 1e-15 else "✗"
            print(f"    {tag} {atom} λ={list(ref_lam)}: rel_err = {mp.nstr(rel_err, 6)}")
        except Exception as exc:
            sanity[atom] = {"error": f"{type(exc).__name__}: {exc}"}

    # WitnessBuilder constructed at start of main(); now populate.
    w.parameters.update({
        "q_0": Q_MP_STR,
        "precision_dps": 50,
        "n_values": sorted(by_n.keys()),
        "n_total_partitions": len(tasks),
    })
    w.add_data("by_n", {str(n): by_n[n] for n in sorted(by_n.keys())})
    w.add_data("sanity_check", sanity)
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
