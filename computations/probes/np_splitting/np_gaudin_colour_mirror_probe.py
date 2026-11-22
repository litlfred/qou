#!/usr/bin/env python3
"""Colour dressing of the strand braid: does it move the p/n readout? Generic q, exact.

Two colour routes for a strand braid on colour singlets (thread on PR #9107, ColourSingletSignTwist):
  tensor route, raw letter  X = -q^-1 * b    (owner ruling: the bond letter is b = -q X)
  gl6 coideal route         s = -b^-1        (the Hecke mirror)
The raw tensor letter rescales every letter by the same scalar, so each sector trace of a fixed
word picks up the same factor (-q^-1)^L and every ratio T_X / T_1 is unchanged; nothing to compute.
The mirror is not a scalar; this probe recomputes the q-Casimir (G-q) and KZ-monodromy (M)
readouts with b -> -b^-1 in Z[q, q^-1]. No floats.
"""
import sys
sys.path.insert(0, ".")
from np_gaudin_generic_q_probe import P, LP, q, scaled_casimir


def main():
    S = P.setup(q)
    S = {k: ([[LP.of(x) for x in r] for r in v] if isinstance(v, list) else v) for k, v in S.items()}
    Rt, Ri = S["Rt"], S["Ri"]
    S["Rt"] = [[-x for x in r] for r in Ri]   # mirror: b -> -b^-1
    S["Ri"] = [[-x for x in r] for r in Rt]
    A, B, AB = [0, 1, 2], [3, 4, 5], list(range(6))
    V = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
    base = P.word(S, V)
    Kd = {s: q ** (2 * sum(1 for x in P.bits(s) if x == 0) - P.N) for s in range(P.D)}
    X = P.add(scaled_casimir(S, AB), scaled_casimir(S, A), scaled_casimir(S, B), coeffs=[1, -1, -1])
    beta = P.word(S, [(2, False), (1, False), (0, False), (3, False), (2, False), (1, False), (4, False), (3, False), (2, False)])
    T1 = P.readout(S, base, Kd, P.eye())
    TX = P.readout(S, base, Kd, X)
    TM = P.readout(S, base, Kd, P.mul(beta, beta))
    pp, nn = (1, 1), (0, 0)
    print("mirror core, G-q: pp = nn identically in q:", TX[pp] * T1[nn] - TX[nn] * T1[pp] == 0)
    print("mirror core, M:   pp = nn identically in q:", TM[pp] * T1[nn] - TM[nn] * T1[pp] == 0)


if __name__ == "__main__":
    main()
