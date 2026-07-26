#!/usr/bin/env python3
"""Numeric (mpmath) weight-block colored-Jones engine — the fast exact-value
tower for the Whitehead factor, reaching N≈30 (vs the O(N⁹) engine's N≈14).

Same weight-block decomposition as the (mod-p) whitehead_weightblock_engine,
but in mpmath complex arithmetic, evaluated just inside the root of unity so
the reduced form raw/[N] is finite.  The braiding Ř preserves total weight
s=i₁+i₂+i₃, so ρ(β) is block-diagonal; the Markov trace needs only the
diagonal → largest block O(N²), turning O(N⁹) into ~O(N⁶).

Validated (below) against whitehead_colored_jones.closure_invariant (full
O(N⁹) engine) at small N.  Item #1 of the 3-2-1 plan: firm up "factor 2".

Audit-only; no wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_colored_jones import r_check_braiding, qint  # noqa: E402

WH = [1, -2, 1, -2, 1]


def colored_jones_weightblock_mp(word, N, q, mu_power=1):
    """Framing-corrected reduced colored Jones J(N) at q (mpmath), 3-strand,
    via total-weight block decomposition."""
    Rc, Rci = r_check_braiding(N, q)
    Kd = [q ** (mp.mpf(N - 1 - 2 * i) * mu_power) for i in range(N)]

    blocks = {}
    for i1 in range(N):
        for i2 in range(N):
            for i3 in range(N):
                blocks.setdefault(i1 + i2 + i3, []).append((i1, i2, i3))

    total = mp.mpc(0)
    for s, states in blocks.items():
        d = len(states)
        idx = {st: a for a, st in enumerate(states)}
        rho = mp.eye(d)
        for g in word:
            a = abs(g) - 1
            blk = Rc if g > 0 else Rci
            G = mp.zeros(d, d)
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
            rho = G * rho
        for st in states:
            w = mp.mpc(1)
            for ik in st:
                w *= Kd[ik]
            total += w * rho[idx[st], idx[st]]

    val = total / qint(N, q)
    wr = sum(1 if g > 0 else -1 for g in word)
    return val * q ** (-wr * (N * N - 1) / 2)


def whitehead_reduced_at_root(N, delta=mp.mpf("1e-45")):
    """|J_red(N)| for the Whitehead at the exact root (near-root eval)."""
    q = mp.exp(mp.mpc(0, 1) * mp.pi * (1 - delta) / N)
    return abs(colored_jones_weightblock_mp(WH, N, q))


if __name__ == "__main__":
    mp.mp.dps = 50
    from whitehead_colored_jones import closure_invariant
    print("Numeric weight-block engine — validation vs full closure_invariant:")
    q = mp.exp(mp.mpc(0, 1) * mp.mpf("0.4"))
    ok = True
    for N in (2, 3, 4, 5):
        a = colored_jones_weightblock_mp(WH, N, q)
        b = closure_invariant(WH, 3, N, q, *r_check_braiding(N, q)) / qint(N, q)
        b = b * q ** (-1 * (N * N - 1) / 2)     # framing (writhe +1)
        err = abs(a - b)
        ok = ok and err < mp.mpf("1e-30")
        print(f"  N={N}: |Δ|={float(err):.1e}")
    print(f"  => {'VALIDATED' if ok else 'MISMATCH'}")
