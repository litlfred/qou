#!/usr/bin/env python3
"""
High-precision (MPFR) Jones–Markov y_λ witness via Rust kernel.

Bridges to `pyhecke_native.chi_lambda_braid_mpfr` for arbitrary-
precision Hoefsmit characters, then assembles and solves the
linear system in `mpmath` at the requested precision.

Same linear-system structure as `y_lambda_jones_markov_witness.py`
(at f64 precision in pure Python), but with all arithmetic at
MPFR precision throughout.  Used to verify the f64 witness and to
provide higher-precision values for downstream binding-energy
computations targeting the ppb-class precision in PR #427.

Default: 50 dps (≈ 167 bits), which is well in excess of the f64
witness precision and matches the Rust kernel's default MPFR
default.

References:
- prop:alpha-k-derivation-procedure
- pyhecke_native.chi_lambda_braid_mpfr (tools/pyhecke-native)

Performance ceiling:
- n=3..11 at 50 dps complete in ~10 min total.
- n=12 at 50 dps does not complete in 45 min wall-clock.
- n=12 at 25 dps does not complete in 25 min wall-clock either.
  Bottleneck: 462x462 sparse Hoefsmit MPFR matmul for partition (4,4,4).
  Tractable n=12 high-precision would require block-sparse MPFR plus
  rayon parallelism over partitions in the Rust kernel.
  For now: f64 witness in y-lambda-jones-markov-witness.json
  (already in main) covers n=12 at 64-bit precision.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import pyhecke_native as ph

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT


def cycle_type_word(mu: tuple[int, ...]) -> list[tuple[int, int]]:
    """Reduced word as (sign=+1, generator_index) list realising
    cycle type μ on n = sum(μ) strands."""
    word: list[tuple[int, int]] = []
    s = 0
    for m in mu:
        for j in range(m - 1):
            word.append((1, s + j + 1))
        s += m
    return word


def solve_y_lambda_mpfr(n: int, q_str: str, dps: int) -> dict:
    """Compute y_λ at H_n(R, q) at MPFR precision."""
    mp.mp.dps = dps
    parts = list(ph.partitions_of(n))
    p_n = len(parts)
    z = mp.mpf(1) / (mp.mpf(q_str) ** mp.mpf("0.5") + mp.mpf(q_str) ** mp.mpf("-0.5"))

    A = mp.matrix(p_n, p_n)
    b = mp.matrix(p_n, 1)
    for i, mu in enumerate(parts):
        word = cycle_type_word(tuple(mu))
        b[i, 0] = z ** (n - len(mu))
        for j, lam in enumerate(parts):
            chi_str = ph.chi_lambda_braid_mpfr(list(lam), word, q_str, dps)
            A[i, j] = mp.mpf(chi_str)

    y = mp.lu_solve(A, b)

    # Compute residual A·y - b
    Ay = A * y
    residual = max(abs(Ay[i, 0] - b[i, 0]) for i in range(p_n))

    return {
        "n": n,
        "num_partitions": p_n,
        "q": q_str,
        "z": str(z),
        "dps": dps,
        "weights": [
            {
                "partition": list(lam),
                "depth": max(0, len(lam) - 1),
                "y_lambda": str(y[j, 0]),
            }
            for j, lam in enumerate(parts)
        ],
        "diagnostics": {
            "linear_system_residual_str": str(residual),
        },
    }


def cross_check_against_f64(n: int, mpfr_y: list[str]) -> dict:
    """Compare MPFR result to existing f64 witness."""
    f64_path = (
        Path(__file__).parent / "y-lambda-jones-markov-witness.json"
    )
    if not f64_path.exists():
        return {"f64_witness_missing": True}
    f64 = json.loads(f64_path.read_text())
    table = f64["tables_by_n"].get(str(n))
    if table is None:
        return {"no_f64_witness_for_n": n}
    diffs = []
    for j, weight_entry in enumerate(table["weights"]):
        y_f64 = mp.mpf(str(weight_entry["y_lambda"]))
        y_mpfr = mp.mpf(mpfr_y[j])
        diffs.append(abs(y_mpfr - y_f64))
    return {
        "max_abs_diff_f64_vs_mpfr": str(max(diffs)),
        "all_within_1e-12": all(d < mp.mpf("1e-12") for d in diffs),
    }


def main(ns: list[int], dps: int = 50) -> None:
    out_path = Path(__file__).parent / "y-lambda-mpfr-witness.json"
    if out_path.exists():
        out: dict = json.loads(out_path.read_text())
    else:
        out = {"tables_by_n": {}}
    out["description"] = (
        "High-precision (MPFR) Jones–Markov y_λ at H_n(R, q) via "
        "pyhecke_native.chi_lambda_braid_mpfr + mpmath linear solve.  "
        "Default 50 dps; arbitrary precision via the dps argument.  "
        "Cross-validates the f64 witness in y-lambda-jones-markov-"
        "witness.json and provides higher-precision values for "
        "ppb-class binding-energy computations."
    )
    out["references"] = [
        "prop:alpha-k-derivation-procedure",
        "tools/pyhecke-native (Rust kernel)",
    ]
    out["computedAt"] = datetime.now(timezone.utc).isoformat()
    out.setdefault("tables_by_n", {})
    out["dps"] = dps

    preserved = sorted(
        (k for k in out["tables_by_n"] if int(k) not in ns),
        key=int,
    )
    if preserved:
        print(f"Preserving existing entries for n in {preserved}\n")

    q_str = str(Q0_FLOAT)
    for n in ns:
        print(f"Solving y_λ at H_{n}(R, q) (n={n}) at {dps} dps...", flush=True)
        result = solve_y_lambda_mpfr(n, q_str, dps)
        result["cross_check_vs_f64"] = cross_check_against_f64(
            n, [w["y_lambda"] for w in result["weights"]]
        )
        out["tables_by_n"][str(n)] = result
        # Incremental save so progress isn't lost on SIGTERM/timeout.
        out_path.write_text(json.dumps(out, indent=2))
        diag = result["cross_check_vs_f64"]
        within = diag.get("all_within_1e-12")
        print(
            f"  saved n={n}; residual: {result['diagnostics']['linear_system_residual_str'][:30]}...  "
            f"f64 cross-check within 1e-12: {within}",
            flush=True,
        )

    print(f"\nFinal state already saved incrementally to {out_path}")


if __name__ == "__main__":
    if sys.argv[1:] and sys.argv[1] == "--dps":
        dps = int(sys.argv[2])
        ns = [int(a) for a in sys.argv[3:]]
    else:
        dps = 50
        ns = [int(a) for a in sys.argv[1:]]
    if not ns:
        # Default: small-n verification + the higher-n cases that benefit
        # most from MPFR precision (n=11, 12 had cond ~7980 in f64).
        ns = [3, 4, 5, 11, 12]
    main(ns, dps)
