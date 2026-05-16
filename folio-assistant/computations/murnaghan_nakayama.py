#!/usr/bin/env python3
"""
Murnaghan–Nakayama rule for symmetric-group characters χ^λ(σ).

Classical form (q = 1 limit of the Hecke algebra character):

    χ^λ(σ) = Σ_{ν ≺ λ, λ/ν ribbon of size m_1}
               (-1)^{height(λ/ν)} · χ^ν(σ')

where σ has cycle type (m_1, m_2, …) and σ' has cycle type
(m_2, …) (the first cycle removed).

Base case: χ^λ((1^n)) = f^λ (number of standard Young tableaux,
dimension of the Specht module) — computed here via the hook
length formula.

Ribbons (rim-hooks) are connected skew shapes λ/ν of size m
contained in the rim of λ such that λ/ν contains no 2×2 square.

This is the q=1 classical character; the q-deformed Hecke
character χ^λ_q(T_w) adds (q - 1)-ribbon-weight corrections.
That refinement is a separate module.

References:
  [james-kerber1981] The Representation Theory of the Symmetric Group.
  [macdonald1979] Symmetric Functions and Hall Polynomials, Ch I §7.
"""
import math
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from partition_utils import hook_lengths  # noqa: E402


def partitions_of(n):
    """Generate all partitions of n as decreasing tuples."""
    def _gen(n, max_part):
        if n == 0:
            yield ()
            return
        for k in range(min(n, max_part), 0, -1):
            for tail in _gen(n - k, k):
                yield (k,) + tail
    return list(_gen(n, n))


def dim_specht(partition):
    """f^λ = n! / Π hook lengths (hook-length formula).

    Also exported as ``d_lambda`` for callers using that convention; both
    names refer to the same hook-length count of standard Young tableaux.
    """
    n = sum(partition)
    hooks = hook_lengths(partition)
    prod = 1
    for h in hooks:
        prod *= h
    return math.factorial(n) // prod


# Alias used by some callers (e.g. ρ_K race scripts that follow
# representation-theory naming d_λ rather than f^λ).
d_lambda = dim_specht


def dim_q_lambda(partition, q):
    """Quantum dimension of the irrep λ via the q-hook-length formula.

        dim_q(λ) = [n]_q! / Π_{x ∈ λ} [h(x)]_q

    where [k]_q = (q^k − q^{−k}) / (q − q^{−1}) is the symmetric q-integer.
    Numeric mpmath / float consumer (use the symbolic ``q_dim_sym`` in the
    Frobenius co-Casimir script for sympy expressions).

    Returns a positive value at q > 1; same type as the input q (mpmath
    mpf or Python float). Shared helper for the ρ_K race scripts that
    use Plancherel weights `1/dim_q(λ)` as LP cost vectors.
    """
    def qint(k):
        if k == 0:
            return q * 0  # type-preserving zero
        return (q ** k - q ** (-k)) / (q - q ** (-1))
    n = sum(partition)
    num = qint(1)
    for k in range(2, n + 1):
        num = num * qint(k)
    den = qint(1)
    for h in hook_lengths(partition):
        if h == 1:
            continue  # qint(1) = 1 — multiplicative identity
        den = den * qint(h)
    return num / den


def rim_hooks_of_size(partition, m):
    """Generate all skew shapes λ/ν that are ribbons (rim-hooks) of
    size m, as (mu, height) pairs where mu is the shape of ν and
    height is the number of rows the ribbon occupies minus 1.

    Algorithm: walk the outer rim of λ, marking all connected
    paths of length m along it that don't form a 2×2 block.

    For a ribbon of length m starting at rim cell (i, λ_i - 1) and
    proceeding down-left along the rim, the removed shape has
    height = (rows spanned) - 1.
    """
    rows = list(partition)
    n_rows = len(rows)
    if n_rows == 0:
        return
    # Outer rim cells, in the order: top-right → bottom-left
    # For each outer cell (i, j), the cell is on the rim iff
    # (i == 0 or j == rows[i-1]) and j == rows[i] - 1.
    rim = []
    for i in range(n_rows):
        j = rows[i] - 1
        # Top rim includes (i, j) for j above the next row's end
        start_j = rows[i + 1] if i + 1 < n_rows else 0
        for jj in range(j, start_j - 1, -1):
            rim.append((i, jj))
    # A rim-hook of size m is any m consecutive cells in the rim
    # sequence; the result must be a valid skew shape (which it is
    # by construction of the rim walk).
    for start in range(len(rim) - m + 1):
        ribbon = rim[start:start + m]
        # Check continuity: consecutive cells must share an edge.
        ok = True
        for k in range(1, m):
            dx = abs(ribbon[k][0] - ribbon[k - 1][0])
            dy = abs(ribbon[k][1] - ribbon[k - 1][1])
            if dx + dy != 1:
                ok = False
                break
        if not ok:
            continue
        # Compute mu = partition with ribbon removed.
        new_rows = list(rows)
        for (i, j) in ribbon:
            if new_rows[i] > j:
                new_rows[i] = j  # truncate row i at column j
        # Drop trailing zeros
        while new_rows and new_rows[-1] == 0:
            new_rows.pop()
        mu = tuple(new_rows)
        # Validate: mu must be a non-increasing sequence (valid partition)
        if any(mu[i] < mu[i + 1] for i in range(len(mu) - 1)):
            continue
        # Height of ribbon = number of distinct rows it touches - 1
        rows_used = set(i for (i, _) in ribbon)
        height = len(rows_used) - 1
        yield mu, height


@lru_cache(maxsize=None)
def mn_character(partition, cycle_type):
    """χ^λ(σ) via Murnaghan–Nakayama recursion.

    partition, cycle_type are tuples of positive integers in
    nonincreasing order.
    """
    # Canonicalise cycle_type: sort decreasing
    cycle_type = tuple(sorted(cycle_type, reverse=True))
    if sum(partition) != sum(cycle_type):
        return 0
    n = sum(partition)
    # Base case: identity permutation (cycle type (1, 1, ..., 1))
    if cycle_type == (1,) * n:
        return dim_specht(partition)
    # Recursion: peel off the largest cycle m_1
    m = cycle_type[0]
    rest = cycle_type[1:]
    total = 0
    for mu, height in rim_hooks_of_size(partition, m):
        total += (-1) ** height * mn_character(mu, rest)
    return total


def permutation_from_braid_word(word, n_strands):
    """Project a braid word (list of (generator_index, sign)) to a
    permutation in S_{n_strands}.

    Each crossing σ_i^{±1} acts as the transposition (i, i+1);
    signs are irrelevant at the S_n level.
    """
    perm = list(range(n_strands))
    for gen_idx, _sign in word:
        perm[gen_idx], perm[gen_idx + 1] = perm[gen_idx + 1], perm[gen_idx]
    return tuple(perm)


def cycle_type_of_permutation(perm):
    """Cycle type of a permutation as a decreasing tuple."""
    n = len(perm)
    seen = [False] * n
    cycles = []
    for i in range(n):
        if seen[i]:
            continue
        cycle_len = 0
        j = i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            cycle_len += 1
        cycles.append(cycle_len)
    return tuple(sorted(cycles, reverse=True))


def atomic_braid_word(Z, N, include_inter=True,
                      m_pp=1, m_pn=1, m_nn=1):
    """Derive the atomic-braid word from proton_cross + neutron_cross
    + inter-nucleon multiplicities.

    Returns list of (gen_index, sign).  Each nucleon contributes
    its intra-nucleon crossings at positions 3k and 3k+1; inter-
    nucleon pairs at position 3k+2.

    Sign convention for the S_n projection: signs don't matter
    (positive, negative, averaged all give the same transposition).
    """
    from mass_endomorphism import proton_cross, neutron_cross
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    word = []
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        for _ in src.get(0, []):
            word.append((3 * k, +1))
        for _ in src.get(1, []):
            word.append((3 * k + 1, +1))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                mult = m_pp
            elif pair == ('n', 'n'):
                mult = m_nn
            else:
                mult = m_pn
            for _ in range(mult):
                word.append((3 * k + 2, +1))
    return word


def character_on_atomic_braid(partition, Z, N, include_inter=True,
                                m_pp=1, m_pn=1, m_nn=1):
    """χ^λ(π(𝒜)) — classical S_{3A} character on the atomic-braid
    permutation.

    P2.1 wiring: threads m_pp/m_pn/m_nn through to atomic_braid_word
    so that dressed-quark mass differentiation reaches the SW
    character. Note: at A=1 (single nucleon) the multiplicities have
    no effect (no inter-nucleon pairs); at A≥2 they differentiate
    proton-rich vs neutron-rich atoms via the inter-nucleon crossing
    structure. The q=1 limit of the Hecke character is still implicit
    (full q-deformed Hecke character requires q-ribbon-tableau
    weights — separate module).
    """
    n_strands = 3 * (Z + N)
    word = atomic_braid_word(Z, N, include_inter, m_pp, m_pn, m_nn)
    perm = permutation_from_braid_word(word, n_strands)
    cyc = cycle_type_of_permutation(perm)
    return mn_character(partition, cyc), cyc


# ─── Self-test ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("MURNAGHAN–NAKAYAMA — classical χ^λ on atomic-braid permutations")
    print("=" * 76)

    # Sanity: χ^λ((1^n)) = f^λ (hook-length formula)
    print("\nDimensions via MN for n = 4:")
    for lam in partitions_of(4):
        mn_val = mn_character(lam, (1, 1, 1, 1))
        direct = dim_specht(lam)
        tag = "OK" if mn_val == direct else "FAIL"
        print(f"  λ = {lam!s:<16}  f^λ = {direct:>3}  "
              f"χ^λ(id) via MN = {mn_val:>3}  [{tag}]")

    # n-cycle character: χ^(n-k, 1^k)((n)) = (-1)^k
    print("\nχ^λ(n-cycle) for n = 5 (expect ±1 on hook λ, else 0):")
    for lam in partitions_of(5):
        val = mn_character(lam, (5,))
        print(f"  λ = {lam!s:<18}  χ^λ((5)) = {val}")

    # Atomic-braid characters
    print("\nATOMIC-BRAID CYCLE TYPES AND DOMINANT CHARACTERS")
    print("-" * 60)
    for Z, N in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2),
                  (3, 3)]:
        A = Z + N
        n_strands = 3 * A
        word = atomic_braid_word(Z, N, include_inter=True)
        perm = permutation_from_braid_word(word, n_strands)
        cyc = cycle_type_of_permutation(perm)
        print(f"\n  atom = ({Z}p, {N}n), A = {A}, braid length "
              f"= {len(word)}, cycle type = {cyc}")
        # Show top-5 partitions by |χ^λ(cycle)|
        lam_chars = []
        for lam in partitions_of(n_strands):
            chi = mn_character(lam, cyc)
            if chi != 0:
                lam_chars.append((lam, chi))
        lam_chars.sort(key=lambda p: -abs(p[1]))
        print(f"  Top-5 partitions with nonzero χ^λ:")
        for lam, chi in lam_chars[:5]:
            print(f"    λ = {lam!s:<26}  χ^λ = {chi:>+6d}")
        print(f"  Total nonzero partitions: {len(lam_chars)} "
              f"/ {len(partitions_of(n_strands))}")
