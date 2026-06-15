#!/usr/bin/env python3
# polynomial_q_not_applicable: evaluates at q = q_0, numeric output.
"""Canonical |tr_M(β_atomic)| at q_0 via the chi-cache combiner.

Step 2 of [`docs/audits/2026-05-17-knot-fusion-step1-audit.md`](../../docs/audits/2026-05-17-knot-fusion-step1-audit.md)
from PR #681. The Step 1 audit found that the **operator-valued
Wenzl 1988 branching identity** for non-tensor canonical braids
already exists on main, along with parameterised compute pipeline
`per_irrep_pole_atom.py` and per-irrep χ caches
`chi-{atom}-h{n}.witness.json` for the proton, neutron, deuteron
(complete) and tritium / ³He / ⁴He (partial).

What was missing: a **Σ_λ y_λ(q_0) · χ^λ(β; q_0)** combiner that
turns those caches into canonical |tr_M(β_atomic)|. This script is
that ~50-line combiner.

## Recipe

For each atom (Z, N) with n = 3(Z + N):

  1. Load chi cache `chi-{atom}-h{n}.witness.json` — symbolic
     χ^λ_q(β_atomic(Z, N)) per partition λ ⊢ n.
  2. Substitute q = q_0 (mpmath 50 dps).
  3. Load y_λ(q_0) via `wedderburn_jones_markov.y_lambda_at(n, q_0)`
     — fast path through `y-lambda-at-q0.witness.json` (50 dps).
  4. Sum: `tr_M = Σ_λ y_λ · χ^λ`.
  5. Return |tr_M|.

This is the canonical |tr_M| consumed by:
  - the ρ_K overlay layer 4 in `atomic_mass_via_rho_k.py`
    (currently disabled pending this combiner — see #678 / #679)
  - cross-checks against Hoefsmit / markov_peel for D/T/³He
    (`cross_check_trM_wenzl_lr_1ppb.py`).

Output: `canonical-tr-m-via-chi-cache.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of  # noqa: E402
from q_parameter import Q as Q_0_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _load_numerical_chi_cache(atom_name: str, n: int) -> dict | None:
    """Load the numerical χ^λ@q_0 cache built by
    `chi_at_q0_via_hoefsmit_mpfr.py`, if present. Returns None when
    the numerical cache is absent (callers fall back to the symbolic
    path).
    """
    path = HERE / f"chi-{atom_name}-h{n}-at-q0-50dps.witness.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def _load_chi_cache(atom_name: str, n: int) -> tuple[dict[tuple, str], bool, int]:
    """Load symbolic χ^λ cache for `atom_name` at H_n.

    Returns (cache, partial, total_partitions). Caller decides how
    to handle partial caches.
    """
    path = HERE / f"chi-{atom_name}-h{n}.witness.json"
    if not path.exists():
        raise FileNotFoundError(
            f"chi cache not found: {path.name}. Run "
            f"`per_irrep_pole_atom.py {atom_name}` to build it."
        )
    d = json.loads(path.read_text())
    cached_str = {tuple(e["partition"]): e["chi_q_symbolic"]
                  for e in d.get("chi_lambda_symbolic", [])}
    partial = bool(d.get("partial", False)) or len(cached_str) < len(parts_of(n))
    return cached_str, partial, len(parts_of(n))


def canonical_tr_m(atom_name: str, Z: int, N: int) -> dict[str, object]:
    """Compute |tr_M(β_atomic(Z, N))| at q_0 via Σ_λ y_λ · χ^λ.

    Prefers the numerical χ^λ@q_0 cache (built by
    `chi_at_q0_via_hoefsmit_mpfr.py`) when present — it's
    pre-computed end-to-end as |tr_M(q_0)| = Σ y_λ · χ^λ at 50 dps,
    so the consumer just reads the value with the per-λ breakdown.
    Falls back to the symbolic chi cache (slower, partial-aware)
    when the numerical cache is missing.
    """
    # Normalize short aliases ("D" → "deuteron", "3He" → "helium-3", …)
    # to the canonical ATOMS key the chi caches are written under: the
    # producer (chi_at_q0_via_hoefsmit_mpfr.py) keys cache files by the
    # full name, so a short-alias caller would otherwise miss
    # (chi-D-h6 vs chi-deuteron-h6). Idempotent on canonical names.
    atom_name = ATOM_ALIASES.get(atom_name, atom_name)
    n = 3 * (Z + N)

    # Fast path: numerical χ^λ@q_0 cache (one mpf per partition, built by
    # chi_at_q0_via_hoefsmit_mpfr.py). The cache stores χ^λ only — NOT the
    # central weights y_λ, the per-λ contributions, or the summed tr_M — so
    # the consumer combines them here per the docstring recipe (steps 3-4):
    # load y_λ(q_0) and sum Σ_λ y_λ · χ^λ. This is faster than the symbolic
    # path below (the cached χ are already numeric — no sympify/subst) while
    # producing the identical return schema.
    numerical = _load_numerical_chi_cache(atom_name, n)
    if numerical is not None:
        q_0 = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised
        n_total = numerical.get("n_partitions_total", len(numerical["by_partition"]))
        n_used = numerical.get("n_partitions", len(numerical["by_partition"]))
        is_partial = bool(numerical.get("partial", False)) or n_used < n_total

        t0 = time.time()
        y_lams = y_lambda_at(n, q_0)
        t_y = time.time() - t0

        t0 = time.time()
        tr_m = mp.mpf(0)
        per_lambda = []
        for entry in numerical["by_partition"]:
            raw = entry["partition"]
            # The numerical cache serialises the partition as a JSON
            # string ("[6]"); the symbolic cache uses a list. Accept both.
            lam = tuple(json.loads(raw)) if isinstance(raw, str) else tuple(raw)
            if lam not in y_lams:
                continue
            chi_val = mp.mpf(entry["chi_lambda"])
            y_val = mp.mpf(str(y_lams[lam]))
            contrib = y_val * chi_val
            tr_m += contrib
            per_lambda.append({
                "partition": list(lam),
                "y_lambda_at_q0": str(y_val),
                "chi_lambda_at_q0": str(chi_val),
                "contribution": str(contrib),
            })
        t_sum = time.time() - t0

        return {
            "atom": atom_name,
            "Z": Z,
            "N": N,
            "n_strands": n,
            "partitions_total": n_total,
            "partitions_used": n_used,
            "partial_cache": is_partial,
            "source": "numerical_chi_cache",
            "q_0_50dps": str(q_0),
            "tr_M_q0": str(tr_m),
            "abs_tr_M_q0": str(abs(tr_m)),
            "y_lambda_load_time_sec": round(t_y, 3),
            "tr_m_sum_time_sec": round(t_sum, 3),
            "per_lambda": per_lambda,
        }

    # Slow path: symbolic chi cache (used when the numerical builder
    # has not run for this atom yet).
    q = sp.Symbol("q", positive=True)

    chi_cache, partial, n_total = _load_chi_cache(atom_name, n)
    n_used = len(chi_cache)

    t0 = time.time()
    q_0 = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised
    y_lams = y_lambda_at(n, q_0)
    t_y = time.time() - t0

    t0 = time.time()
    tr_m = mp.mpf(0)
    per_lambda = []
    q_0_sp = sp.Float(str(q_0), 50)
    for lam_str, chi_sym_str in chi_cache.items():
        lam = tuple(lam_str)
        if lam not in y_lams:
            continue
        chi_expr = sp.sympify(chi_sym_str)
        # Substitute every free symbol (the cache uses its own `q`
        # symbol identity) with the 50-dps q_0 value in a single
        # `.subs(dict)` call (faster than iterative; per Gemini
        # review on PR #682).
        chi_val_sp = chi_expr.subs(
            {sym: q_0_sp for sym in chi_expr.free_symbols}
        )
        chi_val = mp.mpf(str(sp.N(chi_val_sp, 50)))
        y_val = mp.mpf(str(y_lams[lam]))
        contrib = y_val * chi_val
        tr_m += contrib
        per_lambda.append({
            "partition": list(lam),
            "y_lambda_at_q0": str(y_val),
            "chi_lambda_at_q0": str(chi_val),
            "contribution": str(contrib),
        })
    t_sum = time.time() - t0

    return {
        "atom": atom_name,
        "Z": Z,
        "N": N,
        "n_strands": n,
        "partitions_total": n_total,
        "partitions_used": n_used,
        "partial_cache": partial,
        "source": "symbolic_chi_cache",
        "q_0_50dps": str(q_0),
        "tr_M_q0": str(tr_m),
        "abs_tr_M_q0": str(abs(tr_m)),
        "y_lambda_load_time_sec": round(t_y, 3),
        "tr_m_sum_time_sec": round(t_sum, 3),
        "per_lambda": per_lambda,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "atoms", nargs="*",
        help="Atom names or aliases (default: every atom with a complete "
             "or partial chi cache). One of: " + ", ".join(ATOMS),
    )
    parser.add_argument("--full-tables", action="store_true",
                        help="Print per-partition contribution tables.")
    args = parser.parse_args()

    start_time = time.monotonic()

    # Default: scan for any chi-*.witness.json that exists.
    if not args.atoms:
        atoms = []
        for atom_name, (Z, N) in ATOMS.items():
            n = 3 * (Z + N)
            if (HERE / f"chi-{atom_name}-h{n}.witness.json").exists():
                atoms.append(atom_name)
    else:
        atoms = [ATOM_ALIASES.get(a, a) for a in args.atoms]

    print("=" * 84)
    print(" Canonical |tr_M(β_atomic)| at q_0 via Σ_λ y_λ · χ^λ chi-cache combiner")
    print(f" q_0 = {Q_0_FLOAT}")
    print("=" * 84)
    print(f"  {'atom':>9} {'A':>3} {'n':>3} {'parts':>10} {'|tr_M|':>20} {'time':>7}")
    print("  " + "-" * 70)

    results = []
    for atom_name in atoms:
        if atom_name not in ATOMS:
            print(f"  skipping unknown atom: {atom_name}")
            continue
        Z, N = ATOMS[atom_name]
        t_atom = time.time()
        try:
            r = canonical_tr_m(atom_name, Z, N)
        except FileNotFoundError as e:
            print(f"  {atom_name:>9}  cache missing: {str(e)[:50]}")
            continue
        elapsed = time.time() - t_atom
        cov = f"{r['partitions_used']}/{r['partitions_total']}"
        if r["partial_cache"]:
            cov += "*"
        print(f"  {atom_name:>9} {Z+N:>3} {r['n_strands']:>3} "
              f"{cov:>10} {float(r['abs_tr_M_q0']):>20.12g} "
              f"{elapsed:>6.1f}s")
        if args.full_tables:
            for row in r["per_lambda"]:
                print(f"    λ={tuple(row['partition'])!s:>15}  "
                      f"y={float(row['y_lambda_at_q0']):+.6e}  "
                      f"χ={float(row['chi_lambda_at_q0']):+.6e}  "
                      f"y·χ={float(row['contribution']):+.6e}")
        results.append(r)

    print()

    builder = WitnessBuilder.wrap_legacy(
        "canonical-tr-m-via-chi-cache",
        {
            "description": (
                "Canonical |tr_M(β_atomic(Z, N))| at q_0 computed as "
                "Σ_λ y_λ(q_0) · χ^λ(β; q_0), the ~50-line combiner "
                "called out by `docs/audits/2026-05-17-knot-fusion-"
                "step1-audit.md` (PR #681). Consumes the symbolic "
                "χ^λ chi-cache from `per_irrep_pole_atom.py` and the "
                "50-dps `y_lambda_at(n, q_0)` table. Partial chi "
                "caches yield truncated traces (`partitions_used < "
                "partitions_total`); downstream consumers should check "
                "`partial_cache` before using the result for the 1ppb "
                "comparison."
            ),
            "parameters": {
                "q_0_50dps": Q_50_DIGIT_STR,
                "atoms_evaluated": [r["atom"] for r in results],
            },
            "results": results,
        },
        script_path=__file__,
        engine="mpmath",
        start_time=start_time,
    )
    out = builder.save()
    print(f"  Witness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
