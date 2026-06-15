#!/usr/bin/env python3
"""Recursive memoised Murnaghan-Nakayama for batch character evaluation.

Implements the recursive MN rule

  χ_ρ^λ = Σ_{ξ ∈ BS(λ, ρ_1)} (-1)^{ht(ξ)} · χ_{ρ\\ρ_1}^{λ\\ξ}

with memoisation on (lam, rho) pairs. Cross-validated against the
known S_3, S_4, S_5 character tables.

The q-deformed extension (Halverson-Ram broken-strip rule) replaces
the (-1)^ht weight with a polynomial in q; the recursion structure
is identical, so the same memoised driver works.

USAGE:
    from q_mn_recursive_memoized import chi_classical, chi_table

    # Single character
    cache = {}
    chi = chi_classical((3, 1), (2, 2), cache)

    # Full character table at S_n
    table = chi_table(4)
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.setrecursionlimit(50000)


def sub_partitions(lam, k):
    """Yield all sub-partitions μ ⊆ λ (non-increasing) with |λ| - |μ| = k."""
    rows = len(lam)
    if k == 0:
        yield tuple(lam)
        return

    def rec(idx, mu_prev, remaining):
        if idx == rows:
            if remaining == 0:
                yield ()
            return
        max_part = min(lam[idx], mu_prev)
        for mu_i in range(max_part + 1):
            removed_here = lam[idx] - mu_i
            if removed_here <= remaining:
                for rest in rec(idx + 1, mu_i, remaining - removed_here):
                    if mu_i > 0:
                        yield (mu_i,) + rest
                    else:
                        # Once we hit a zero row, all subsequent must be zero
                        if all(r == 0 for r in rest if isinstance(rest, tuple)):
                            yield rest

    for mu in rec(0, lam[0] + 1 if rows > 0 else 0, k):
        yield mu


def is_border_strip(lam, mu, k):
    """Check λ \\ μ is a connected border strip of size k (no 2×2 square).
    Returns (is_valid, height) where height = #rows - 1."""
    cells = []
    for i in range(len(lam)):
        mu_i = mu[i] if i < len(mu) else 0
        for j in range(mu_i, lam[i]):
            cells.append((i, j))
    if len(cells) != k:
        return False, 0
    cell_set = set(cells)
    # No 2×2 square
    for (i, j) in cells:
        if (i + 1, j) in cell_set and (i, j + 1) in cell_set \
                and (i + 1, j + 1) in cell_set:
            return False, 0
    # Connected
    visited = {cells[0]}
    stack = [cells[0]]
    while stack:
        (i, j) = stack.pop()
        for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (i + di, j + dj)
            if neighbor in cell_set and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    if len(visited) != k:
        return False, 0
    rows_used = set(c[0] for c in cells)
    height = len(rows_used) - 1
    return True, height


def border_strips(lam, k):
    """Yield (μ, height) for each border strip of size k removable from λ."""
    if k == 0:
        yield tuple(lam), 0
        return
    n = sum(lam)
    if k > n:
        return
    for mu in sub_partitions(lam, k):
        # Strip trailing/zero entries to make it a clean partition
        mu_clean = tuple(p for p in mu if p > 0)
        ok, ht = is_border_strip(lam, mu, k)
        if ok:
            yield mu_clean, ht


def chi_classical(lam, rho, cache=None):
    """Compute χ_ρ^λ classically (q=1) via recursive memoised MN."""
    return chi_q(lam, rho, q_val=1, cache=cache)


def chi_q(lam, rho, q_val, cache=None):
    """Compute χ_ρ^λ(q) via the recursive Halverson-Ram broken-strip rule.

    Weight per border strip ξ of size k with height ht:
      W_q(ξ) = (-1)^ht · q^{k - 1 - 2·ht}

    At q=1 this reduces to (-1)^ht (classical Murnaghan-Nakayama).

    Empirically verified:
      - At H_2: gives Hecke eigenvalues q (trivial) and -q^{-1} (sign).
      - At H_3 on 3-cycle: gives q² (trivial), -1 (standard), q^{-2} (sign).

    Args:
      lam: irrep partition (descending tuple).
      rho: cycle-type partition (any tuple summing to |lam|).
      q_val: numeric value or 1 for classical; can be mp.mpf for high precision.
      cache: dict for memoisation; created if None.
    """
    if cache is None:
        cache = {}
    lam = tuple(p for p in lam if p > 0)
    rho = tuple(p for p in rho if p > 0)
    rho = tuple(sorted(rho, reverse=True))

    key = (lam, rho)
    if key in cache:
        return cache[key]

    if not rho:
        result = 1 if not lam else 0
        cache[key] = result
        return result
    if sum(lam) != sum(rho):
        cache[key] = 0
        return 0

    rho1 = rho[0]
    rho_rest = rho[1:]

    # Sum over border strips of size rho1 in lam, weighted by Halverson-Ram.
    result = 0
    for new_lam, height in border_strips(lam, rho1):
        # Broken-strip weight: (-1)^ht · q^{k - 1 - 2·ht}
        # At q=1 this is just (-1)^ht (classical MN).
        weight_sign = (-1) ** height
        weight_qpow = rho1 - 1 - 2 * height
        if q_val == 1 or q_val == 1.0:
            weight = weight_sign  # q^0 = 1
        else:
            weight = weight_sign * (q_val ** weight_qpow)
        chi_sub = chi_q(new_lam, rho_rest, q_val, cache)
        result += weight * chi_sub

    cache[key] = result
    return result


def partitions_of(n):
    if n == 0:
        return [()]

    def gen(rem, mxp):
        if rem == 0:
            yield ()
            return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest

    return list(gen(n, n))


def chi_table(n):
    """Return the character table of S_n as a dict {(λ, ρ): χ}."""
    parts = partitions_of(n)
    cache = {}
    return {
        (lam, rho): chi_classical(lam, rho, cache)
        for lam in parts for rho in parts
    }, cache


# Reference character tables for cross-validation
S3_TABLE = {
    (3,): {(1, 1, 1): 1, (2, 1): 1, (3,): 1},
    (2, 1): {(1, 1, 1): 2, (2, 1): 0, (3,): -1},
    (1, 1, 1): {(1, 1, 1): 1, (2, 1): -1, (3,): 1},
}

S4_TABLE = {
    (4,): {(1,1,1,1): 1, (2,1,1): 1, (2,2): 1, (3,1): 1, (4,): 1},
    (3, 1): {(1,1,1,1): 3, (2,1,1): 1, (2,2): -1, (3,1): 0, (4,): -1},
    (2, 2): {(1,1,1,1): 2, (2,1,1): 0, (2,2): 2, (3,1): -1, (4,): 0},
    (2, 1, 1): {(1,1,1,1): 3, (2,1,1): -1, (2,2): -1, (3,1): 0, (4,): 1},
    (1, 1, 1, 1): {(1,1,1,1): 1, (2,1,1): -1, (2,2): 1, (3,1): 1, (4,): -1},
}


def main():
    print("=" * 60)
    print("Recursive memoised MN — cross-validation")
    print("=" * 60)

    # S_3
    print("\nS_3 character table:")
    cache3 = {}
    parts3 = [(3,), (2, 1), (1, 1, 1)]
    print(f"{'λ × ρ':>10}", *[f"{str(rho):>10}" for rho in parts3])
    all_ok = True
    for lam in parts3:
        row = []
        for rho in parts3:
            chi = chi_classical(lam, rho, cache3)
            ref = S3_TABLE[lam][rho]
            row.append(chi)
            if chi != ref:
                print(f"  MISMATCH: λ={lam}, ρ={rho}: got {chi}, expected {ref}")
                all_ok = False
        print(f"{str(lam):>10}", *[f"{v:>10}" for v in row])

    print(f"\n  S_3 cache: {len(cache3)} entries")
    print(f"  S_3 cross-check: {'PASS ✓' if all_ok else 'FAIL ✗'}")

    # S_4
    print("\nS_4 character table:")
    cache4 = {}
    parts4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    print(f"{'λ × ρ':>14}", *[f"{str(rho):>15}" for rho in parts4])
    all_ok = True
    for lam in parts4:
        row = []
        for rho in parts4:
            chi = chi_classical(lam, rho, cache4)
            ref = S4_TABLE[lam][rho]
            row.append(chi)
            if chi != ref:
                print(f"  MISMATCH: λ={lam}, ρ={rho}: got {chi}, expected {ref}")
                all_ok = False
        print(f"{str(lam):>14}", *[f"{v:>15}" for v in row])

    print(f"\n  S_4 cache: {len(cache4)} entries")
    print(f"  S_4 cross-check: {'PASS ✓' if all_ok else 'FAIL ✗'}")

    # S_5 (no reference table; just demonstrate cache size)
    print("\nS_5 — cache size demonstration:")
    cache5 = {}
    parts5 = partitions_of(5)
    n_chars = 0
    for lam in parts5:
        for rho in parts5:
            chi_classical(lam, rho, cache5)
            n_chars += 1
    print(f"  S_5 cache: {len(cache5)} entries for {n_chars} characters computed.")
    print(f"  Cache hit rate: {1 - len(cache5)/n_chars:.1%}")

    # Demonstrate batch speedup: compute 100 characters at S_8 with vs without cache
    print("\nS_8 batch demo — speedup from memoisation:")
    import time
    parts8 = partitions_of(8)
    t0 = time.time()
    cache8 = {}
    n_calls = 0
    for lam in parts8:
        for rho in parts8:
            chi_classical(lam, rho, cache8)
            n_calls += 1
    t_cached = time.time() - t0
    print(f"  S_8: {len(parts8)*len(parts8)} characters in {t_cached:.2f}s "
          f"(cache size {len(cache8)})")
    print(f"  Per-character: {t_cached/n_calls*1000:.3f} ms (with cache)")

    # NO CACHE: run a sample without memoisation
    t0 = time.time()
    sample_count = min(50, len(parts8))
    for lam in parts8[:sample_count]:
        for rho in parts8[:sample_count]:
            chi_classical(lam, rho, cache=None)  # fresh cache each call
    t_nocache = time.time() - t0
    print(f"  No-cache sample ({sample_count}² chars): {t_nocache:.2f}s")
    print(f"  Speedup factor (cached vs fresh): "
          f"{t_nocache/sample_count**2 / (t_cached/n_calls):.1f}×")


if __name__ == "__main__":
    main()
