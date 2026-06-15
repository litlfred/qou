#!/usr/bin/env python3
"""
P2.2b-MN — Closed-form character for length-≤-2 partitions.

The bottleneck in ¹²C Schur-Weyl is `mn_character(λ, ρ)` for
length-≤-2 partition λ on a 36-strand cycle type ρ. The
Murnaghan-Nakayama recursion peels cycles one at a time and
transits through length-3+ intermediate partitions, exploding
combinatorially.

For length-≤-2 partitions there is a closed form via the
Frobenius character formula:

    χ^{(a,b)}(ρ) = [x_1^{a+1} x_2^b] · (x_1 - x_2) · Π_j (x_1^{ρ_j} + x_2^{ρ_j})

Expanding:
    χ^{(a,b)}(ρ) = #{S ⊂ {1..k} : Σ_{j∈S} ρ_j = a}
                 - #{S : Σ_{j∈S} ρ_j = a + 1}

Subset-sum counting via dynamic programming runs in O(k · n).

For length-1 λ = (n,): χ^{(n)}(ρ) = 1 (trivial character).

This module exposes a fast path that bypasses the MN recursion
for length-≤-2 partitions. Validation: matches `mn_character` on
all length-≤-2 partitions for n ≤ 8.

References:
  [macdonald1979] Symmetric Functions and Hall Polynomials, Ch I §7.
"""
from collections import defaultdict


def subset_sum_counts(parts: tuple[int, ...]) -> dict[int, int]:
    """Return a dict {s: count} where count = #subsets of parts summing to s.

    O(k · total_sum) DP.
    """
    counts: dict[int, int] = {0: 1}
    for p in parts:
        new = dict(counts)  # subsets that don't include p
        for s, c in counts.items():
            new[s + p] = new.get(s + p, 0) + c
        counts = new
    return counts


def chi_length_one(n: int, cycle_type: tuple[int, ...]) -> int:
    """χ^{(n)}(ρ) = 1 (trivial character on the symmetric group)."""
    if sum(cycle_type) != n:
        return 0
    return 1


def chi_length_two(a: int, b: int, cycle_type: tuple[int, ...]) -> int:
    """χ^{(a,b)}(ρ) via subset-sum (Frobenius formula)."""
    n = a + b
    if sum(cycle_type) != n:
        return 0
    if a < b:
        a, b = b, a  # canonicalise
    if b == 0:
        return chi_length_one(n, cycle_type)
    counts = subset_sum_counts(cycle_type)
    pos = counts.get(a, 0)
    neg = counts.get(a + 1, 0)
    return pos - neg


def chi_length_le_two(partition: tuple[int, ...],
                       cycle_type: tuple[int, ...]) -> int:
    """χ^λ(ρ) for length-≤-2 λ via closed form (no MN recursion)."""
    if len(partition) > 2:
        raise ValueError(f"chi_length_le_two requires length ≤ 2; got {partition}")
    if len(partition) == 0:
        return 1 if sum(cycle_type) == 0 else 0
    if len(partition) == 1:
        return chi_length_one(partition[0], cycle_type)
    return chi_length_two(partition[0], partition[1], cycle_type)


# ── Validation against MN ──────────────────────────────────────

def _validate():
    """Check chi_length_le_two against mn_character on small cases."""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from murnaghan_nakayama import mn_character, partitions_of

    print("Validating chi_length_le_two against mn_character...")
    failures = 0
    total = 0
    for n in range(1, 9):
        # All length-≤-2 partitions of n
        length_le_2 = [p for p in partitions_of(n) if len(p) <= 2]
        # All cycle types of size n (= partitions of n)
        for cyc in partitions_of(n):
            for lam in length_le_2:
                fast = chi_length_le_two(lam, cyc)
                slow = mn_character(lam, cyc)
                total += 1
                if fast != slow:
                    failures += 1
                    print(f"  FAIL: λ={lam}, ρ={cyc}: fast={fast}, slow={slow}")
    print(f"  {total} cases checked; {failures} failures.")
    return failures == 0


if __name__ == "__main__":
    ok = _validate()
    print()
    if ok:
        print("✅ All cases match.")
    else:
        print("🔴 Mismatches found.")

    # Performance check
    import time
    print("\nPerformance check at A=12 (cycle type for ¹²C atomic braid):")
    from murnaghan_nakayama import (
        atomic_braid_word,
        permutation_from_braid_word,
        cycle_type_of_permutation,
    )
    Z, N = 6, 6
    A = Z + N
    n_strands = 3 * A
    word = atomic_braid_word(Z, N, include_inter=True)
    perm = permutation_from_braid_word(word, n_strands)
    cyc = cycle_type_of_permutation(perm)
    print(f"  cycle type: {cyc}")

    # Time the closed-form on all length-≤-2 partitions of 36
    length_le_2 = []
    for b in range(0, n_strands // 2 + 1):
        a = n_strands - b
        if a >= b and (b == 0 or a >= b):
            length_le_2.append((a,) if b == 0 else (a, b))
    print(f"  {len(length_le_2)} length-≤-2 partitions of {n_strands}")

    t0 = time.time()
    chars = []
    for lam in length_le_2:
        chi = chi_length_le_two(lam, cyc)
        chars.append((lam, chi))
    t1 = time.time()
    print(f"  closed-form total time: {t1 - t0:.4f}s")

    # Show non-zero characters
    print(f"  non-zero characters:")
    for lam, chi in chars:
        if chi != 0:
            print(f"    λ = {lam!s:<14}  χ = {chi}")
