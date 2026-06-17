#!/usr/bin/env python3
"""A-operator combiner at A≥5: the O(d²) cost wall + the contraction-only form.

formalize-first (before any Rust build): the diagonal-only / contraction-only
combiner cost is `Σ_{ξ⊢n_inner} d_ξ²·|W|` per atom. Since `Σ_{ξ⊢n} d_ξ² = n!`,
this is `n_inner!·|W|` — dominated by the single largest block `d_max²·|W|`. The
diagonal/contraction reorganisation (this branch) removes the `O(d²)` *memory*
wall but NOT the `O(d²)` *time*: a generic seminormal word-rep has no low-rank
diagonal, so the cost is irreducible without a rep-free method.

This probe (1) tabulates the wall across A=4..7 under three arithmetic backends
(mpmath 50 dps, a Rust mpfr constant-factor, float64), to show what Rust can and
cannot reach; and (2) verifies the streaming `combiner_value_streaming` against
`chi_young` at A=4 (exact, the contraction-only deliverable). No fit.
"""
from __future__ import annotations

import sys
from math import factorial
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parents[1]               # computations/
AOP = HERE / "a_operator"
for p in (str(HERE), str(AOP), str(HERE / "substrate")):
    sys.path.insert(0, p)

import a_operator_categorical as aoa            # noqa: E402
import a_operator_recursive as rec              # noqa: E402
import rho_xi_diagonal as rxd                   # noqa: E402
from young_seminormal import chi_young, seminormal_sigma  # noqa: E402
from lr_coefficients import partitions_of       # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

DPS = 50
mp.mp.dps = 60

# per-op wall-time models (s/op), calibrated to #2449's A=4 diag run (~0.5 µs/op
# at 50 dps mpmath); Rust mpfr ≈ 7× faster; float64 ≈ 100× faster but coarse.
T_MPMATH = 0.5e-6
T_RUST = 0.07e-6
T_FLOAT = 5e-9


def hook_dim(lam) -> int:
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def _fmt(seconds: float) -> str:
    if seconds < 90:
        return f"{seconds:.1f} s"
    if seconds < 5400:
        return f"{seconds / 60:.1f} min"
    if seconds < 1.5 * 86400:
        return f"{seconds / 3600:.1f} h"
    return f"{seconds / 86400:.1f} d"


def cost_table():
    print("=" * 92)
    print(" A-operator combiner cost wall  (diagonal/contraction-only: Σ_ξ d_ξ²·|W|, ξ⊢3A−3)")
    print("=" * 92)
    print(f" {'A':>2} {'n_in':>4} {'#ξ':>5} {'d_max':>8} {'Σd²=n!':>12} {'|W|':>4}"
          f" {'ops':>10} {'mpmath':>9} {'rust':>9} {'float64':>9}")
    print(" " + "-" * 90)
    zn = {4: (2, 2), 5: (3, 2), 6: (3, 3), 7: (4, 3)}
    for A in (4, 5, 6, 7):
        n_in = 3 * A - 3
        parts = partitions_of(n_in)
        dims = [hook_dim(p) for p in parts]
        d_max = max(dims)
        sumsq = factorial(n_in)                          # Σ_{ξ⊢n} d_ξ² = n!
        Z, N = zn[A]
        wlen = len(atom_braid_word_3A(Z, N))
        ops = 2 * wlen * sumsq                            # ≈2 nonzeros/row per gen
        print(f" {A:>2} {n_in:>4} {len(parts):>5} {d_max:>8} {sumsq:>12.3g} {wlen:>4}"
              f" {ops:>10.2e} {_fmt(ops*T_MPMATH):>9} {_fmt(ops*T_RUST):>9}"
              f" {_fmt(ops*T_FLOAT):>9}")
    print("\n READING: the cost is Σd²=n_inner! — dominated by d_max². Rust is a"
          " ~7× constant\n factor; it does NOT change the asymptotic, so the"
          " largest A=6 block stays days\n even in Rust at 50 dps. Only float64"
          " (coarse, ~1e-10) reaches A=6 in ~hours.\n")


def verify_streaming_a4():
    """combiner_value_streaming == chi_young at A=4 (exact contraction-only)."""
    q = aoa.q0_mp(DPS)
    q_str = mp.nstr(q, DPS)
    h = q - 1 / q

    def shim(lam, qs, dps):
        qq = mp.mpf(qs)
        n = sum(lam)
        mats = [seminormal_sigma(tuple(lam), i, qq) for i in range(1, n)]
        return mats, (mats[0].rows if mats else 1)

    aoa.exact_seminormal_matrices = shim                 # Rust wheel absent here

    def fac(br):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, g) for (s, g) in br]

    def dense_prod(mats, word):
        M = mp.eye(mats[0].rows)
        eye = mp.eye(mats[0].rows)
        for (c, d, g) in word:
            M = M * (c * mats[g] + d * eye)
        return M

    finner = fac([(1, 0), (1, 3), (-1, 5), (1, 7), (1, 1)])
    fblock = fac([(1, 0), (-1, 1)])
    RB = {nu: dense_prod(shim(nu, q_str, DPS)[0], fblock)
          for nu in partitions_of(3)}

    worst = mp.mpf(0)
    for lam in [(10, 2), (11, 1), (7, 5)]:
        full = finner + [(mp.mpf(1), -h / 2, 8)] + [(c, d, g + 9) for (c, d, g) in fblock]
        lhs = chi_young(lam, full, q)
        blocks_full = rec.interface_blocks(lam, 9, 3, q_str, -h / 2, DPS)
        blocks = {k: info["A"] for k, info in blocks_full.items()}
        rhs = rxd.combiner_value_streaming(blocks, RB, finner, q_str, DPS)
        worst = max(worst, abs(lhs - rhs))
    ok = worst < mp.mpf(10) ** -25
    print(" VERIFY (contraction-only streaming combiner vs chi_young, A=4):")
    print(f"   max|chi_young − streaming| = {mp.nstr(worst, 4)}"
          f"   {'OK — exact, O(d) memory' if ok else 'FAIL'}")
    return ok


def main() -> int:
    cost_table()
    ok = verify_streaming_a4()
    print("\n VERDICT: contraction-only streaming is exact + O(d) memory (the right"
          " A=6 form),\n but the O(d²·|W|) TIME wall is irreducible — Rust's constant"
          " factor cannot make\n the largest A=6 block tractable at 50 dps; a float64"
          " coarse cross-check is the\n only realistic A=6 route. No fit, nothing rewired.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
