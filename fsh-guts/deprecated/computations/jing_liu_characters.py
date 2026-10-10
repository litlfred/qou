#!/usr/bin/env python3
"""
Closed-form Iwahori-Hecke characters χ^λ_μ(q) for hooks and two-row λ.

Implements Theorems 2.9 and 2.11 of

    Jing & Liu, "On irreducible characters of the Iwahori-Hecke
    algebra in type A", arXiv:2104.06067v1 (13 Apr 2021).

The paper works in the convention

    T_i^2 = (q_J − 1) T_i + q_J              (eigenvalues q_J, −1)           (1.3)

while our pipeline uses the Hoefsmit symmetric convention

    T_i^2 = (q_H − q_H^{−1}) T_i + 1         (eigenvalues q_H, −q_H^{−1})

These are related by T_J = q_H · T_H at q_J = q_H^2.  Hence for a
reduced word w of length ℓ(w) (e.g. the minimal-length cycle-type
representative w_μ with ℓ(w_μ) = n − l(μ)),

    χ^λ_μ(T_w^J; q_J)  =  q_H^{ℓ(w)}  ·  χ^λ_μ(T_w^H; q_H)
                      =  q_H^{n − l(μ)} · χ^λ_μ(T_w^H; q_H)   (cycle rep)

so Hoefsmit-convention values are recovered by

    χ^λ_{μ, H}(q_H)  =  q_H^{−(n − l(μ))}  ·  χ^λ_{μ, J}(q_H^2).

The closed forms below apply for λ a hook (k, 1^{n-k}) or a two-row
partition (k, n-k) with k ≥ n-k.  For general λ, use the recursive
Murnaghan-Nakayama (not implemented here) or the seminormal
matrix-trace path in hecke_characters.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


@lru_cache(maxsize=None)
def _a_coefficients(mu: tuple[int, ...], q_J: float) -> tuple[float, ...]:
    """Coefficients a_j(μ; q) from Jing-Liu Eq (2.29):

        (1 − q^{-1} v)^r · Π_{i=1}^r (1 + v + … + v^{μ_i − 1})
          = Σ_{j=0}^{|μ|} a_j(μ; q) v^j

    where r = l(μ) and |μ| = Σ μ_i.  Returns tuple (a_0, a_1, …, a_n).
    """
    mu = tuple(x for x in mu if x > 0)
    r = len(mu)
    n = sum(mu)
    # Polynomial in v with coefficients indexed 0..n (only up to degree n matters)
    poly = [0.0] * (n + 1)
    poly[0] = 1.0
    # Multiply by each (1 + v + ... + v^{μ_i-1})
    for mi in mu:
        new = [0.0] * (n + 1)
        for j, c in enumerate(poly):
            if c == 0.0:
                continue
            for s in range(mi):
                if j + s <= n:
                    new[j + s] += c
        poly = new
    # Multiply by (1 - q^{-1} v)^r using binomial expansion
    qi = 1.0 / q_J
    if r > 0:
        # Expand (1 - qi v)^r = Σ_{k=0}^r C(r,k) (-qi)^k v^k
        from math import comb
        binom = [comb(r, k) * (-qi) ** k for k in range(r + 1)]
        new = [0.0] * (n + 1)
        for j, c in enumerate(poly):
            if c == 0.0:
                continue
            for k, bk in enumerate(binom):
                if j + k <= n:
                    new[j + k] += c * bk
        poly = new
    return tuple(poly)


@lru_cache(maxsize=None)
def _b_coefficients(mu: tuple[int, ...], q_J: float) -> tuple[float, ...]:
    """Coefficients b_j(μ; q) from Jing-Liu Eq (2.30):

        Π_{i=1}^r [ q^{-1} + v^{μ_i} + (1 − q^{-1})(1 + v + … + v^{μ_i − 1}) ]
          = Σ_{j=0}^{|μ|} b_j(μ; q) v^j
    """
    mu = tuple(x for x in mu if x > 0)
    n = sum(mu)
    qi = 1.0 / q_J
    poly = [0.0] * (n + 1)
    poly[0] = 1.0
    for mi in mu:
        # Build factor = qi + v^{mi} + (1 - qi)(1 + v + ... + v^{mi-1})
        factor = [0.0] * (n + 1)
        factor[0] = qi
        if mi <= n:
            factor[mi] += 1.0
        coef = 1.0 - qi
        for s in range(mi):
            factor[s] += coef
        # Multiply poly * factor, truncate to degree n
        new = [0.0] * (n + 1)
        for j, a in enumerate(poly):
            if a == 0.0:
                continue
            for k, b in enumerate(factor):
                if b == 0.0:
                    continue
                if j + k <= n:
                    new[j + k] += a * b
        poly = new
    return tuple(poly)


def chi_hook_jing(lam: tuple[int, ...], mu: tuple[int, ...],
                    q_J: float) -> float:
    """χ^{(k, 1^{n-k})}_μ(q_J) via Jing-Liu Eq (2.31).

    Requires λ = (k, 1, 1, …, 1) with one row of length k and (n-k)
    rows of length 1.  Raises ValueError if λ is not a hook.

    Returns in the JING convention (T² = (q-1)T + q).
    """
    lam = tuple(x for x in lam if x > 0)
    mu = tuple(x for x in mu if x > 0)
    n = sum(lam)
    if sum(mu) != n:
        raise ValueError(
            f"Partition weights differ: |λ|={n} |μ|={sum(mu)}")
    if not lam:
        return 1.0
    k = lam[0]
    # λ is a hook iff parts are (k, 1, 1, ..., 1)
    if any(p != 1 for p in lam[1:]):
        raise ValueError(f"λ={lam} is not a hook")
    l_mu = len(mu)
    a = _a_coefficients(mu, q_J)
    total = 0.0
    for i in range(k, n + 1):
        total += a[i] * q_J ** i
    sign = (-1) ** (n - k + l_mu)
    return sign * total


def chi_two_row_jing(lam: tuple[int, ...], mu: tuple[int, ...],
                      q_J: float) -> float:
    """χ^{(k, n-k)}_μ(q_J) via Jing-Liu Eq (2.32).

    Requires λ = (k, n-k) with k ≥ n-k ≥ 0, i.e. a two-row shape
    (possibly single row if n-k = 0).  Returns JING convention.
    """
    lam = tuple(x for x in lam if x > 0)
    mu = tuple(x for x in mu if x > 0)
    n = sum(lam)
    if sum(mu) != n:
        raise ValueError(
            f"Partition weights differ: |λ|={n} |μ|={sum(mu)}")
    if not lam:
        return 1.0
    if len(lam) > 2:
        raise ValueError(f"λ={lam} has more than 2 rows")
    k = lam[0]
    rest = lam[1] if len(lam) == 2 else 0
    if k < rest:
        raise ValueError(f"λ={lam} must have k ≥ n-k")
    l_mu = len(mu)
    b = _b_coefficients(mu, q_J)
    b_k = b[k] if k < len(b) else 0.0
    b_kp1 = b[k + 1] if k + 1 < len(b) else 0.0
    return q_J ** (n - l_mu) * (b_k - b_kp1)


# ── Hoefsmit-convention bridge ──────────────────────────────

def hoefsmit_from_jing(chi_J: float, n: int, l_mu: int,
                         q_H: float) -> float:
    """Convert a Jing-convention character value at q_J = q_H^2 (on
    a minimal-length cycle-type representative word) to Hoefsmit:

        χ^λ_{μ, H}(q_H) = q_H^{-(n - l(μ))} · χ^λ_{μ, J}(q_H^2).
    """
    return q_H ** (-(n - l_mu)) * chi_J


def chi_hook_hoefsmit(lam: tuple[int, ...], mu: tuple[int, ...],
                        q_H: float) -> float:
    """Hoefsmit-convention hook character, via Jing-Liu + bridge."""
    n = sum(lam)
    chi_J = chi_hook_jing(lam, mu, q_H * q_H)
    return hoefsmit_from_jing(chi_J, n, len(tuple(x for x in mu if x > 0)),
                                 q_H)


def chi_two_row_hoefsmit(lam: tuple[int, ...], mu: tuple[int, ...],
                           q_H: float) -> float:
    """Hoefsmit-convention two-row character, via Jing-Liu + bridge."""
    n = sum(lam)
    chi_J = chi_two_row_jing(lam, mu, q_H * q_H)
    return hoefsmit_from_jing(chi_J, n, len(tuple(x for x in mu if x > 0)),
                                 q_H)


# ── CLI: verify against seminormal ─────────────────────────

if __name__ == "__main__":
    import numpy as np
    from q_parameter import Q as Q0
    from hecke_characters import partitions_of, build_seminormal_matrices

    def _min_cycle_word(mu: tuple[int, ...]) -> tuple[int, ...]:
        word = []
        offset = 0
        for part in mu:
            for t in range(part - 1):
                word.append(offset + t)
            offset += part
        return tuple(word)

    def _chi_direct(lam, mu):
        sigmas, d, _ = build_seminormal_matrices(lam)
        if d == 0:
            return 0.0
        w = _min_cycle_word(mu)
        prod = np.eye(d)
        for g in w:
            prod = prod @ sigmas[g]
        return float(np.trace(prod))

    print("=" * 80)
    print("Jing-Liu hook/two-row closed form vs Hoefsmit seminormal")
    print(f"q_H = {Q0:.6f}  (→ q_J = {Q0*Q0:.6f})")
    print("=" * 80)
    max_hook = 0.0
    max_two = 0.0
    n_hook = 0
    n_two = 0
    failures = []
    for n in [2, 3, 4, 5, 6, 7, 8]:
        for mu in partitions_of(n):
            mu = tuple(mu)
            # Hooks: (k, 1^{n-k}) for 1 ≤ k ≤ n
            for k in range(1, n + 1):
                lam = (k,) + (1,) * (n - k)
                lam = tuple(x for x in lam if x > 0)
                chi_d = _chi_direct(lam, mu)
                chi_f = chi_hook_hoefsmit(lam, mu, Q0)
                diff = abs(chi_d - chi_f)
                max_hook = max(max_hook, diff)
                n_hook += 1
                if diff > 1e-9:
                    failures.append(
                        ('hook', n, lam, mu, chi_d, chi_f, diff))
            # Two-row: (k, n-k) for k ≥ n-k ≥ 0
            for k in range(max(1, (n + 1) // 2), n + 1):
                nk = n - k
                lam = (k, nk) if nk > 0 else (k,)
                chi_d = _chi_direct(lam, mu)
                chi_f = chi_two_row_hoefsmit(lam, mu, Q0)
                diff = abs(chi_d - chi_f)
                max_two = max(max_two, diff)
                n_two += 1
                if diff > 1e-9:
                    failures.append(
                        ('two-row', n, lam, mu, chi_d, chi_f, diff))
    print(f"\nHook cases:    {n_hook}  max |Δ| = {max_hook:.3e}")
    print(f"Two-row cases: {n_two}  max |Δ| = {max_two:.3e}")
    if failures:
        print(f"\n✗ {len(failures)} failures:")
        for (kind, n, lam, mu, d, f, df) in failures[:10]:
            print(f"  {kind} n={n} λ={lam} μ={mu}: "
                  f"direct={d:+.6f} jing-liu={f:+.6f} Δ={df:.3e}")
    else:
        print("\n✓ All hook + two-row values agree with seminormal to 1e-9")
