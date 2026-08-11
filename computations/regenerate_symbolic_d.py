#!/usr/bin/env python3
"""Regenerate y-lambda-wenzl-bridge-symbolic-witness.json under Convention D.

Bean: qou-toi3

The existing witness was computed under Convention C (z = 1/(√q + 1/√q)),
giving expressions in ℚ(√q) — half-integer powers of q. Under Convention D
(z = q³/(q²+1)), X = Q² exactly, so all expressions are in ℚ(q) with
integer powers only. This makes sympy much faster (no sqrt canonicalization).

This script bypasses the cached witness entirely and computes fresh
symbolic y_λ for n = 2..12 using the module's existing D-convention
formulae. It then validates each expression against the numeric path
at q₀ to 30 digits.

Long-compute logging discipline applies (bean says ~6s at n=3, >60s at
n=6 under C; D should be faster but n=12 is still non-trivial).

Usage:
    python3 -u regenerate_symbolic_d.py 2>&1 | tee /tmp/regenerate_symbolic_d.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

# Import the module's core functions — NOT the cached wrappers.
# We want fresh computation, not cache lookups.
from y_lambda_wenzl_bridge import (
    _schur_self_unnormalized,
    _wenzl_norm_for_n,
    y_lambda_wenzl_bridge_numeric,
    partitions_of,
    classical_dim,
)
from q_parameter import Q_50_DIGIT_STR

HERE = Path(__file__).resolve().parent
WITNESS_PATH = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
SCRIPT_PATH = Path(__file__).resolve()


def compute_symbolic_y_lambda(partition: tuple) -> sp.Expr:
    """Compute y_λ symbolically under Convention D.

    Direct computation: sp.cancel(numerator / normalisation).
    No cache lookup, no convention gate.
    """
    num = _schur_self_unnormalized(partition)
    denom = _wenzl_norm_for_n(sum(partition))
    return sp.cancel(num / denom)


def validate_against_numeric(
    partition: tuple, expr: sp.Expr, q0_str: str, dps: int = 50
) -> tuple[bool, float]:
    """Check symbolic expression agrees with numeric at q₀."""
    q_pos = sp.Symbol("q", positive=True)
    with mp.workdps(dps):
        q0 = mp.mpf(q0_str)
        live = y_lambda_wenzl_bridge_numeric(list(partition), q0, dps=dps)
        cached_val = mp.mpf(
            str(sp.N(expr.subs(q_pos, sp.Float(q0_str, dps)), dps - 10))
        )
        scale = max(abs(live), abs(cached_val), mp.mpf("1e-30"))
        relerr = float(abs(live - cached_val) / scale)
        return relerr < 1e-20, relerr


def expose_polynomial(expr: sp.Expr, var: sp.Symbol, simplify: bool = False) -> str:
    """Convert to collected polynomial string for readability."""
    try:
        p = sp.Poly(expr, var)
        return str(p.as_expr())
    except (sp.PolynomialError, sp.GeneratorsNeeded):
        if simplify:
            return str(sp.simplify(expr))
        return str(expr)


def main():
    start_wall = time.monotonic()
    q = sp.Symbol("q", positive=True)

    print(f"Regenerating y-lambda-wenzl-bridge-symbolic-witness.json under D")
    print(f"  q₀ = {Q_50_DIGIT_STR[:20]}...")
    print(f"  Convention D: z = q³/(q²+1), X = Q² = q⁴")
    print(f"  Output: {WITNESS_PATH}")
    print()
    print(f"{'n':>3} {'parts':>5} {'time':>8}  {'sample'}")
    print("-" * 60)

    tables: dict[str, dict] = {}
    total_partitions = 0
    validation_failures = []

    for n in range(2, 13):
        parts = partitions_of(n)
        total_partitions += len(parts)
        t0 = time.monotonic()
        rows = []

        for i, p in enumerate(parts):
            pt = tuple(p)
            expr = compute_symbolic_y_lambda(pt)
            expr_str = sp.sstr(expr)

            # Validate against numeric
            ok, relerr = validate_against_numeric(pt, expr, Q_50_DIGIT_STR)
            if not ok:
                validation_failures.append((p, relerr))
                print(f"  WARNING: n={n} λ={p} validation FAIL relerr={relerr:.2e}")

            # Check no sqrt(q) appears (Convention D guarantee)
            if "sqrt" in expr_str.lower():
                print(f"  WARNING: n={n} λ={p} still has sqrt(q) — NOT Convention D!")

            rows.append({
                "partition": list(p),
                "y_lambda_symbolic": expr_str,
                "y_lambda_polynomial": expose_polynomial(expr, q),
            })

            # Progress for long computations
            elapsed = time.monotonic() - t0
            if elapsed > 5 and i < len(parts) - 1:
                pct = 100 * (i + 1) / len(parts)
                eta = elapsed / (i + 1) * (len(parts) - i - 1)
                print(f"    n={n} progress: {i+1}/{len(parts)} "
                      f"({pct:.0f}%) wall={elapsed:.1f}s ETA={eta:.1f}s",
                      flush=True)

        elapsed = time.monotonic() - t0
        sample = rows[0]["y_lambda_symbolic"]
        if len(sample) > 40:
            sample = sample[:37] + "..."
        print(f"{n:>3} {len(parts):>5} {elapsed:>7.2f}s  {sample}")

        tables[str(n)] = {
            "n": n,
            "num_partitions": len(parts),
            "weights": rows,
            "compute_time_sec": round(elapsed, 2),
        }

    # Compute script hash for provenance
    script_hash = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]

    # Get git commit
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()[:12]
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit = "unknown"

    # Assemble witness
    witness = {
        "computation": "y-lambda-wenzl-bridge-symbolic",
        "convention": "D",
        "convention_detail": (
            "z = q³/(q² + 1) = q²/[2]_q. Under D, X = Q² exactly "
            "(integer-level Wenzl SU_q(2) specialisation). All expressions "
            "are in ℚ(q) — no √q terms."
        ),
        "description": (
            "Symbolic closed-form y_λ for n = 2..12 via the Wenzl bridge: "
            "y_λ = s_{λ, X}(Q) / Σ_µ d_µ s_{µ, X}(Q) with Q = q² and "
            "X = Q² (convention D). Computed via sympy with exact q-rational "
            "expressions. Bypasses the O(p(n)³) linear-system solve. "
            "Regenerated from convention C → D per bean qou-toi3."
        ),
        "references": [
            "prop:y-lambda-closed-form-wenzl-bridge",
            "prop:explicit-alpha-k-h3",
            "prop:alpha-k-derivation-procedure",
            "thm:jones-markov-trace",
            "wenzl1988",
            "orellana1998",
            "chlouveraki2016",
        ],
        "tables_by_n": tables,
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": commit,
        "scriptFile": str(SCRIPT_PATH.relative_to(HERE)),
        "scriptHash": script_hash,
        "total_partitions": total_partitions,
        "validation": {
            "method": "numeric at q₀ to 50 dps",
            "q0_prefix": Q_50_DIGIT_STR[:20],
            "failures": len(validation_failures),
        },
    }

    with open(WITNESS_PATH, "w") as fp:
        json.dump(witness, fp, indent=2, default=str)

    wall = time.monotonic() - start_wall
    print()
    print(f"Done. {total_partitions} partitions across n=2..12.")
    print(f"Validation failures: {len(validation_failures)}")
    print(f"Wall time: {wall:.1f}s")
    print(f"Witness: {WITNESS_PATH}")


if __name__ == "__main__":
    main()
