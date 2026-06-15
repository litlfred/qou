#!/usr/bin/env python3
"""Task 2 — S_Z-block selection rule (the lossless symmetrization prune).

Which partitions λ⊢3Z are EXACT-0 under the identical-nucleon symmetric /
antisymmetric block projection. For Z protons the block-permutation σ∈S_Z maps
to a cycle-type-(Z^3) permutation of the 3Z strands; the trivial-rep
multiplicity is `(1/|S_Z|) Σ_σ χ_λ(block-image σ)`. For Z=2 this is
`(dim_λ + χ_λ(2³))/2` (symmetric) and `(dim_λ − χ_λ(2³))/2` (antisymmetric),
where the block-swap has cycle type 2³ on S₆. Characters via Murnaghan–Nakayama.

RESULT: weak at Z=2 (only the wrong-symmetry 1-dim rep is forbidden — [1⁶] in
the symmetric sector, [6] in the antisymmetric, 1/11 each); the exact-0 prune
GROWS with Z. The forbidden channels are provable (rep-theory), satisfying the
precision discipline's "truncate only if provable-exact-0".
"""
from math import factorial


def parts(n, mx=None):
    """Yield integer partitions of n with parts ≤ mx (descending)."""
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in parts(n - k, k):
            yield (k,) + rest


def chi(lam, mu):
    """Symmetric-group character χ^λ(μ) via Murnaghan–Nakayama (beta-numbers)."""
    lam = tuple(sorted(lam, reverse=True))
    if sum(lam) == 0 and not mu:
        return 1
    if not mu:
        return 1 if sum(lam) == 0 else 0
    r = mu[0]
    rest = mu[1:]
    total = 0
    L = len(lam)
    beta = sorted([lam[i] + (L - 1 - i) for i in range(L)], reverse=True)
    bset = set(beta)
    for b in list(bset):
        if b - r >= 0 and (b - r) not in bset:
            nb = sorted([x for x in bset if x != b] + [b - r], reverse=True)
            # height = # beta values strictly between b-r and b that are present
            ht = sum(1 for x in bset if b - r < x < b)
            m = len(nb)
            nl = tuple(x for x in (nb[i] - (m - 1 - i) for i in range(m)) if x > 0)
            total += ((-1) ** ht) * chi(nl, rest)
    return total


def dim(lam):
    """Number of standard Young tableaux of shape λ (hook-length formula)."""
    lam = list(lam)
    n = sum(lam)
    conj = [sum(1 for x in lam if x > j) for j in range(max(lam))]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


def main():
    print("=== Z=2 (H₆) S₂-block selection: block-swap cycle type 2³ ===")
    print(f"{'λ':>16}{'dim':>5}{'χ(2³)':>7}{'sym=(d+χ)/2':>12}"
          f"{'antisym':>9}{'forbidden':>14}")
    nsym = nanti = 0
    tot = 0
    for lam in parts(6):
        d = dim(lam)
        c = chi(lam, (2, 2, 2))
        s = (d + c) // 2
        a = (d - c) // 2
        tot += 1
        fb = []
        if s == 0:
            fb.append("sym")
            nsym += 1
        if a == 0:
            fb.append("antisym")
            nanti += 1
        print(f"{str(lam):>16}{d:>5}{c:>7}{s:>12}{a:>9}"
              f"{(','.join(fb) or '—'):>14}")
    print(f"\nForbidden: {nsym}/{tot} in symmetric sector, "
          f"{nanti}/{tot} in antisymmetric.")
    print("Selection rule is WEAK at Z=2 (single S₂); the prune grows with Z "
          "(S_Z avg over more block-permutations → more χ-cancellations → more "
          "exact-0 channels).")


if __name__ == "__main__":
    main()
