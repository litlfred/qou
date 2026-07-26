#!/usr/bin/env python3
"""Numeric (numpy complex128) weight-block colored-Jones engine + δ→0
extrapolation — the fast root-of-unity magnitude tower for the Whitehead
factor, reaching N≈30–40 (vs the O(N⁹) engine's N≈14; mpmath is too slow).

Weight-block decomposition (Ř preserves total weight s=i₁+i₂+i₃ ⇒ ρ(β)
block-diagonal; trace needs only the diagonal) in float64, evaluated just
off the root at several δ and Neville-extrapolated to δ=0 (float64-clean,
no near-root cancellation; ~1e-4 relative — ample for the factor).

Validated below against whitehead_fast.closure_norm (full numpy engine).
Item #1 of the 1-3-2 plan.  Audit-only; no wiring.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_fast import r_check, generators  # noqa: E402

WH = [1, -2, 1, -2, 1]


def norm_weightblock(word, N, q):
    """Framing-corrected reduced colored Jones raw/[N] at q (complex128),
    3-strand, via total-weight block decomposition."""
    Rc, Rci = r_check(N, q)
    _, _, Kd = generators(N, q)

    blocks = {}
    for i1 in range(N):
        for i2 in range(N):
            for i3 in range(N):
                blocks.setdefault(i1 + i2 + i3, []).append((i1, i2, i3))

    total = 0j
    for states in blocks.values():
        d = len(states)
        idx = {st: a for a, st in enumerate(states)}
        rho = np.eye(d, dtype=complex)
        for g in word:
            a = abs(g) - 1
            blk = Rc if g > 0 else Rci
            G = np.zeros((d, d), dtype=complex)
            for st in states:
                col = idx[st]
                ia, ib = st[a], st[a + 1]
                c = ia + ib
                for ja in range(max(0, c - (N - 1)), min(N - 1, c) + 1):
                    jb = c - ja
                    ent = blk[ja * N + jb, ia * N + ib]
                    if ent != 0:
                        nst = list(st); nst[a] = ja; nst[a + 1] = jb
                        G[idx[tuple(nst)], col] = ent
            rho = G @ rho
        for st in states:
            w = 1.0 + 0j
            for ik in st:
                w *= Kd[ik]
            total += w * rho[idx[st], idx[st]]

    def qint(n):
        return (q**n - q**(-n)) / (q - q**(-1))
    val = total / qint(N)
    wr = sum(1 if g > 0 else -1 for g in word)
    return val * q ** (-wr * (N * N - 1) / 2)


def reduced_at_root(N, deltas=(0.024, 0.018, 0.012, 0.008, 0.004)):
    """|J_red(N)| at the exact root via Neville δ→0 extrapolation."""
    xs = list(deltas)
    ys = []
    for d in deltas:
        th = math.pi * (1 - d) / N
        ys.append(norm_weightblock(WH, N, complex(math.cos(th), math.sin(th))))
    n = len(xs)
    for k in range(1, n):
        for i in range(n - k):
            ys[i] = ((0 - xs[i + k]) * ys[i] - (0 - xs[i]) * ys[i + 1]) / (xs[i] - xs[i + k])
    return abs(ys[0])


if __name__ == "__main__":
    from whitehead_fast import closure_norm
    import time
    print("Numeric weight-block (numpy) — validation vs full closure_norm:")
    q = complex(math.cos(0.4), math.sin(0.4))
    ok = True
    for N in (2, 3, 4, 5, 6):
        a = norm_weightblock(WH, N, q)
        b = closure_norm(WH, 3, N, q) * q ** (-1 * (N * N - 1) / 2)   # framing (writhe +1)
        err = abs(a - b)
        ok = ok and err < 1e-9
        print(f"  N={N}: |Δ|={err:.1e}")
    print(f"  => {'VALIDATED' if ok else 'MISMATCH'}\n")
    if ok:
        for N in (14, 20, 26, 30):
            t = time.time(); v = reduced_at_root(N)
            print(f"  reduced_at_root N={N}: {v:.5f}  ({time.time()-t:.1f}s)")
