#!/usr/bin/env python3
"""Weight-block acceleration of the (validated) mod-p R-matrix colored-Jones
engine, so the exact Whitehead-link tower reaches the N the recurrence hunt
needs — without any external/unvalidated formula.

The U_q(sl₂) braiding Ř is a weight intertwiner: on V^{⊗3} the total weight
w = 3(N−1) − 2(i₁+i₂+i₃) is preserved, so ρ(β) is block-diagonal in
s := i₁+i₂+i₃.  The Markov trace only needs the diagonal, so we build ρ(β)
block-by-block (largest block O(N²)-dim, not N³) — turning the O(N⁹) full
matmul into O(N⁶)-ish and lifting the ceiling from N≈14 to N≈25+.

Correctness gate (§anti-guessing): validated to reproduce the full engine
`colored_jones_modp` exactly, mod p, at small N.  Audit-only; no wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_diagonal_recurrence_hunt import (  # noqa: E402
    rmatrix, gauss_inv, minv, spow, PRIMES, BASES,
)


def colored_jones_weightblock(word, N, t, p):
    """Framing-corrected reduced colored Jones J(N) mod p for a 3-strand braid,
    via total-weight block decomposition.  q = t²."""
    Rc, Kd = rmatrix(N, t, p)          # N²×N² braiding, Kd = K diagonal
    Rci = gauss_inv(Rc, p)
    Kd = np.array(Kd, dtype=np.int64)

    # group the 3-strand basis by s = i1+i2+i3
    blocks = {}
    for i1 in range(N):
        for i2 in range(N):
            for i3 in range(N):
                blocks.setdefault(i1 + i2 + i3, []).append((i1, i2, i3))

    total = 0
    for s, states in blocks.items():
        d = len(states)
        idx = {st: a for a, st in enumerate(states)}
        rho = np.eye(d, dtype=np.int64)
        for g in word:
            a = abs(g) - 1                     # 0-indexed left strand of the pair
            blk = Rc if g > 0 else Rci
            G = np.zeros((d, d), dtype=np.int64)
            for st in states:
                col = idx[st]
                i = list(st)
                ia, ib = i[a], i[a + 1]
                c = ia + ib                    # Ř preserves the pair weight
                for ja in range(max(0, c - (N - 1)), min(N - 1, c) + 1):
                    jb = c - ja
                    ent = blk[ja * N + jb, ia * N + ib]
                    if ent:
                        nst = i.copy(); nst[a] = ja; nst[a + 1] = jb
                        G[idx[tuple(nst)], col] = ent
            rho = G @ rho % p
        # weighted diagonal trace on this block
        for st in states:
            mu = 1
            for ik in st:
                mu = mu * int(Kd[ik]) % p
            total = (total + mu * int(rho[idx[st], idx[st]])) % p

    # reduce: raw/[N], then framing q^{-w(N²-1)/2} = t^{-w(N²-1)}
    def qint(n):
        num = (spow(t, 2 * n, p) - spow(t, -2 * n, p)) % p
        den = (spow(t, 2, p) - spow(t, -2, p)) % p
        return num * minv(den, p) % p
    val = total * minv(qint(N), p) % p
    wr = sum(1 if g > 0 else -1 for g in word)
    return val * spow(t, -wr * (N * N - 1), p) % p


if __name__ == "__main__":
    from whitehead_diagonal_recurrence_hunt import colored_jones_modp
    import time
    p, t = PRIMES[0], BASES[0]
    WH = [1, -2, 1, -2, 1]
    print("Weight-block engine — validation vs full colored_jones_modp (Whitehead):")
    ok = True
    for N in (2, 3, 4, 5, 6):
        a = colored_jones_weightblock(WH, N, t, p)
        b = colored_jones_modp(WH, 3, N, t, p)
        m = a == b
        ok = ok and m
        print(f"  N={N}: weightblock={a}  full={b}  match={m}")
    print(f"  => {'VALIDATED' if ok else 'MISMATCH'}\n")
    if ok:
        print("  timing at higher N (full engine is infeasible here):")
        for N in (8, 10, 12, 14):
            t0 = time.time()
            v = colored_jones_weightblock(WH, N, t, p)
            print(f"    N={N}: J={v}  ({time.time()-t0:.1f}s)")
