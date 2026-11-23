#!/usr/bin/env python3
"""Pin the seminormal OFF-DIAGONAL convention before building anything on it.

The block-monotone window transfer (bean `qou-wdij`) needs the full 2x2
seminormal block of `sigma_g`, not just its diagonal. The existing corpus has
never needed the off-diagonal — `chi_monotone_transfer._alpha_beta`'s docstring
says so in as many words:

    "the off-diagonal seminormal convention never enters the diagonal of a
     polynomial in sigma_g"

which is exactly why a monotone word can be swept with a scalar per step. So the
convention is not recorded anywhere in this repository, and the window transfer's
failure mode is **a plausible wrong number, not an exception**. This probe
establishes it FIRST, on the smallest case where an interleaving exists at all,
against an oracle — rather than writing a transfer and debugging the convention
through it.

## The claim being tested

For `sigma_g` acting on the 2-dimensional span of the two standard tableaux that
differ by swapping entries `g+1` and `g+2`, with axial distance
`delta = c(g+2) - c(g+1)`:

    diagonal entries    D(delta)  and  D(-delta),   D(x) = h / (1 - q^(-2x))

Two constraints fix the rest without any freedom:

  * **trace.** `D(delta) + D(-delta) = h` EXACTLY. Put `x = q^(-2 delta)`; then
    `1/(1-x) + 1/(1-1/x) = 1/(1-x) - x/(1-x) = 1`. So the trace is `h` for every
    `delta`, which is `q + (-q^-1)` — the eigenvalue sum.
  * **determinant.** The eigenvalues are `q` and `-q^-1`, so `det = -1`.

Hence `B * B' = D(delta) * D(-delta) + 1`, and the SPLIT between `B` and `B'` is
a similarity choice. A character is a trace and is invariant under it, so this
probe asserts the *invariants* and then verifies that the cheapest split — the
seminormal/row form `B = 1`, `B' = D(delta) D(-delta) + 1`, which needs **no
square root and stays in the ring** — reproduces the oracle's characters.

That last point is the practical prize: the orthogonal (Young) form takes
`B = B' = sqrt(D D' + 1)` and would drag a square root into every window matrix.

## What is checked

1. `D(delta) + D(-delta) == h` symbolically-tight at 50 dps, over many `delta`.
2. `D(delta) * D(-delta) + 1 == B * B'` for the row-form split, i.e. `det = -1`.
3. Eigenvalues of the assembled 2x2 are exactly `{q, -q^-1}`.
4. `sigma_g` assembled this way satisfies the **Hecke relation**
   `(sigma - q)(sigma + q^-1) = 0` — the defining relation, not a consequence.
5. **Against the oracle**: characters built by multiplying these 2x2 blocks in
   word order reproduce `pyhecke_native`'s general-word kernel on the real
   `n = 3` atom words, both intra orders. This is the check that would catch a
   sign error the algebra above cannot see.

Check 5 is the load-bearing one; 1-4 are cheap invariants that localise a
failure if 5 goes red.

Arithmetic: mpmath at the 50-dps floor. No float64.
Exit 0 iff every check passes.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_general_word import chi_all_lambda_general  # noqa: E402
from chi_monotone_transfer import word_to_mpfr  # noqa: E402

TOL = mp.mpf("1e-45")

# SYT of the three partitions of 3, as chains of box contents in the order the
# boxes are added. Content of box (row r, col c) is c - r, 0-indexed.
#   (3)       one tableau: contents 0, 1, 2
#   (1,1,1)   one tableau: contents 0, -1, -2
#   (2,1)     two tableaux: 0, 1, -1  and  0, -1, 1
SYT3 = {
    (3,): [(0, 1, 2)],
    (1, 1, 1): [(0, -1, -2)],
    (2, 1): [(0, 1, -1), (0, -1, 1)],
}


def D(delta, q):
    """Diagonal seminormal entry at axial distance `delta`."""
    h = q - 1 / q
    return h / (1 - q ** (-2 * delta))


def sigma_block(delta, q):
    """The 2x2 seminormal block of `sigma` on {T, T'} at axial distance `delta`,
    in the ROW (seminormal) form: off-diagonals `1` and `D D' + 1`.

    Returns `mp.matrix` [[D(delta), B], [B', D(-delta)]].
    """
    d, dp = D(delta, q), D(-delta, q)
    return mp.matrix([[d, mp.mpf(1)], [d * dp + 1, dp]])


def sigma_on_syt(g, shape, q):
    """Matrix of `sigma_g` (0-indexed) in the seminormal basis of `shape`,
    indexed by `SYT3[shape]` order. Built from the axial distance between the
    boxes carrying entries g+1 and g+2 in each tableau."""
    tabs = SYT3[shape]
    n = len(tabs)
    M = mp.zeros(n, n)
    for i, t in enumerate(tabs):
        a, b = t[g], t[g + 1]          # contents of entries g+1 and g+2
        delta = b - a
        if abs(delta) == 1:
            # same row (delta = +1) -> q ; same column (delta = -1) -> -1/q.
            # The swapped tableau is not standard, so the block is 1x1.
            M[i, i] = q if delta == 1 else -1 / q
            continue
        swapped = t[:g] + (t[g + 1], t[g]) + t[g + 2:]
        j = tabs.index(swapped)
        blk = sigma_block(delta, q)
        M[i, i] = blk[0, 0]
        M[i, j] = blk[0, 1] if i < j else blk[1, 0]
    return M


def chi_via_blocks(word, q):
    """`{lambda: chi^lambda(word)}` at n = 3, by multiplying the seminormal
    matrices in WORD ORDER — the construction the window transfer will use."""
    out = {}
    for shape in SYT3:
        dim = len(SYT3[shape])
        acc = mp.eye(dim)
        for d_mp, g in word_to_mpfr(word, q):
            # each letter is (sigma_g + d), c = 1 for every atom-word crossing
            acc = acc * (sigma_on_syt(g, shape, q) + d_mp * mp.eye(dim))
        out[shape] = mp.fsum(acc[i, i] for i in range(dim))
    return out


def main() -> int:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    checks: list[tuple[str, bool]] = []

    # 1-3: the invariants that fix the block, over a range of axial distances.
    worst_tr = worst_det = mp.mpf(0)
    for delta in [d for d in range(-6, 7) if abs(d) >= 2]:
        d, dp = D(delta, q), D(-delta, q)
        worst_tr = max(worst_tr, abs(d + dp - h))
        blk = sigma_block(delta, q)
        det = blk[0, 0] * blk[1, 1] - blk[0, 1] * blk[1, 0]
        worst_det = max(worst_det, abs(det + 1))
    checks.append((f"trace D(d)+D(-d) = h for all |d|>=2 "
                   f"(max err {mp.nstr(worst_tr, 6)})", worst_tr < TOL))
    checks.append((f"det of the row-form block = -1 "
                   f"(max err {mp.nstr(worst_det, 6)})", worst_det < TOL))

    worst_eig = mp.mpf(0)
    for delta in (2, 3, -2, -4):
        blk = sigma_block(delta, q)
        got = sorted([complex(z).real for z in mp.eig(blk)[0]])
        want = sorted([float(-1 / q), float(q)])
        worst_eig = max(worst_eig, max(abs(a - b) for a, b in zip(got, want)))
    checks.append((f"eigenvalues are {{q, -1/q}} "
                   f"(max err {mp.nstr(worst_eig, 6)})", worst_eig < mp.mpf("1e-20")))

    # 4: the Hecke relation itself, on the assembled 2x2.
    worst_hecke = mp.mpf(0)
    for delta in (2, 3, -2, -5):
        s = sigma_block(delta, q)
        I = mp.eye(2)
        R = (s - q * I) * (s + (1 / q) * I)
        worst_hecke = max(worst_hecke, max(abs(R[i, j]) for i in range(2) for j in range(2)))
    checks.append((f"(sigma - q)(sigma + 1/q) = 0 "
                   f"(max |entry| {mp.nstr(worst_hecke, 6)})", worst_hecke < TOL))

    # 5: THE LOAD-BEARING CHECK — against the general-word kernel, on the real
    #    n = 3 atom words, both intra orders (grouped is monotone, borromean is
    #    the interleaving this whole construction exists for).
    for order in ("grouped", "borromean"):
        for (Z, N) in [(1, 0), (0, 1)]:
            word = atom_braid_word_3A(Z, N, intra_order=order)
            got = chi_via_blocks(word, q)
            ref = chi_all_lambda_general(word, 3, dps=50)
            worst = mp.mpf(0)
            for lam in set(got) | set(ref):
                worst = max(worst, abs(got.get(lam, mp.mpf(0))
                                       - ref.get(lam, mp.mpf(0))))
            checks.append((
                f"({Z},{N}) {order}: block product == kernel "
                f"(max|d chi| = {mp.nstr(worst, 6)})", worst < TOL))

    ok = sum(1 for _n, p in checks if p)
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
    print(f"\n{ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
