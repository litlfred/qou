#!/usr/bin/env python3
"""
Wedderburn-strata witness for H_n(R, q): for each n ∈ {3, 4, 5, 6, 9, 12},
enumerate partitions of n, compute their depth = height - 1, classical
hook-length dimension, q-deformed dimension at q_0, signed content
(chirality marker), and the canonical Plancherel weight
w_λ = (dim_classical)²/n! (q-independent — sums to exactly 1).
The q-deformed alternative dim_q²/[n]_q! is recorded as
`q_deformed_weight` but does NOT sum to 1 at finite q ≠ 1.

Output: wedderburn-strata-witness.json — used by sibling branches
verify-mass-computation-k0DaZ and phase-b-heavy-rust-character-kernel
to validate ⁴He binding-energy predictions and atomic chirality residues
without re-deriving the Wedderburn structure.

References:
- Ch. Braids and Knots, §Plancherel boundedness, §Mass formula
- prop:plancherel-weight-boundedness
- prop:unified-curvature-rank-mass-formula
- prop:plancherel-term-7-formulation
"""

import json
from pathlib import Path
from fractions import Fraction


def partitions_of(n):
    """All partitions of n as weakly decreasing tuples (largest first)."""
    if n == 0:
        return [()]
    result = []

    def rec(remaining, max_part, prefix):
        if remaining == 0:
            result.append(tuple(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            rec(remaining - k, k, prefix + [k])

    rec(n, n, [])
    return result


def hook_lengths(partition):
    """Hook length of every cell (row, col) in the Young diagram."""
    rows = len(partition)
    if rows == 0:
        return {}
    cols = max(partition)
    transpose = [
        sum(1 for r in range(rows) if r < len(partition) and partition[r] > c)
        for c in range(cols)
    ]
    hooks = {}
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            arm = row_len - j - 1
            leg = transpose[j] - i - 1
            hooks[(i, j)] = arm + leg + 1
    return hooks


def classical_dim(partition, n):
    """Classical dim V_λ = n! / Π h_x via hook-length formula."""
    hooks = hook_lengths(partition)
    prod = 1
    for h in hooks.values():
        prod *= h
    factorial = 1
    for k in range(2, n + 1):
        factorial *= k
    return factorial // prod


def q_integer(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1}) evaluated at numeric q."""
    if k == 0:
        return 0.0
    return (q ** k - q ** (-k)) / (q - 1.0 / q)


def q_factorial(n, q):
    prod = 1.0
    for k in range(1, n + 1):
        prod *= q_integer(k, q)
    return prod


def q_dim(partition, q):
    """q-dim V_λ = [n]_q! / Π [h_x]_q."""
    n = sum(partition)
    qfact = q_factorial(n, q)
    hooks = hook_lengths(partition)
    prod = 1.0
    for h in hooks.values():
        prod *= q_integer(h, q)
    return qfact / prod


def signed_content(partition):
    """Σ_{cells (i,j)} (j - i): chirality marker (zero ⇒ chirality cell)."""
    s = 0
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            s += j - i
    return s


def depth(partition):
    """Curvature rank = height - 1."""
    return max(0, len(partition) - 1)


def stratify(n, q0):
    """Compute the full Wedderburn-strata table for H_n(R, q) at q_0."""
    parts = partitions_of(n)
    qfact = q_factorial(n, q0)
    rows = []
    for p in parts:
        d_cl = classical_dim(p, n)
        d_q = q_dim(p, q0)
        sc = signed_content(p)
        w = d_q * d_q / qfact
        # Canonical Plancherel measure on Hecke irreps uses classical dim
        # f_λ (q-independent): w_λ = f_λ² / n!, exactly sums to 1.
        # The q-deformed alternative w_q = dim_q² / [n]_q! is recorded
        # alongside but does NOT sum to 1 at q ≠ 1.
        n_factorial = 1
        for k in range(2, n + 1):
            n_factorial *= k
        w_classical = (d_cl * d_cl) / n_factorial
        rows.append({
            "partition": list(p),
            "height": len(p),
            "depth": depth(p),
            "dim_classical": d_cl,
            "dim_q_at_q0": d_q,
            "signed_content": sc,
            "is_chirality_cell": sc == 0,
            "plancherel_weight": w_classical,
            "q_deformed_weight": w,
        })
    # Group by depth
    strata = {}
    for r in rows:
        strata.setdefault(r["depth"], []).append(r)
    # Sanity: weights should sum to 1
    weight_sum = sum(r["plancherel_weight"] for r in rows)
    return {
        "n": n,
        "q_0": q0,
        "num_partitions": len(parts),
        "strata_by_depth": {str(k): v for k, v in sorted(strata.items())},
        "weight_sum_check": weight_sum,
        "strata_weight_sums": {
            str(k): sum(r["plancherel_weight"] for r in v)
            for k, v in sorted(strata.items())
        },
    }


def main():
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from q_parameter import Q as q0
    out = {
        "description": (
            f"Wedderburn-strata enumeration for H_n(R, q) at q = q_0 ≈ {q0:.6f}. "
            "For each n, lists every partition λ ⊢ n with depth, classical "
            "and q-deformed dimensions, signed content (chirality marker), "
            "the canonical Plancherel weight w_λ = (dim_classical)²/n! "
            "(q-independent, sums to exactly 1), and the q-deformed "
            "alternative dim_q²/[n]_q! recorded as `q_deformed_weight` "
            "(does NOT sum to 1 at finite q ≠ 1). "
            "Strata are grouped by curvature-rank depth = height(λ) - 1."
        ),
        "references": [
            "prop:plancherel-weight-boundedness",
            "prop:unified-curvature-rank-mass-formula",
            "prop:plancherel-term-7-formulation",
            "rem:mass-formula-wedderburn-enumeration",
        ],
        "tables": {
            str(n): stratify(n, q0) for n in [3, 4, 5, 6, 9, 12]
        },
    }
    out_path = (
        Path(__file__).parent / "wedderburn-strata-witness.json"
    )
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"Wrote {out_path}")
    for n_str, table in out["tables"].items():
        print(
            f"  n = {n_str:>2}: "
            f"{table['num_partitions']:>4} partitions, "
            f"weight_sum_check = {table['weight_sum_check']:.6f}"
        )


if __name__ == "__main__":
    main()
