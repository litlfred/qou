#!/usr/bin/env python3
"""hecke_corner_block_blueprint — is the block-decomposed corner chain legal?

The Lean development proves the block itself as
`UGB.GrobnerShirshov.Hecke.CornerBlock.blockStep`. This is the check that ran
first, to fix the loop invariant before writing it.


The engine's driver always rewrites the deg-lex-largest redex, but a
`SingleStepReduction` in the Lean development only has to apply *some* rule of
the system at *some* position. So the chain a Lean proof follows need not be the
engine's — and at `a = b + 1` it is not, because the Bokut–Shiao step of block
`d` exposes a redex that deg-lex prefers over finishing block `d`'s transport.

This builds the block-decomposed chain directly from the invariant

    V:  R_d ++ D ++ descWord i_d j₂        →  R_{d+1} ++ D ++ descWord i_{d+1} j₂
    U:  Q_d ++ D ++ descWord i_d j₂ ++ [i] →  Q_{d+1} ++ D ++ descWord i_{d+1} j₂ ++ [i]

each block being one Bokut–Shiao step at top `d` followed by `d`
far-commutations carrying `σ_{i−d−1}` leftwards, and checks every consecutive
pair really is one rule of the system applied in one context — which is exactly
the obligation `monicStep` and `farComm_transport_left` discharge.
"""
from __future__ import annotations
import importlib.util, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))
_spec = importlib.util.spec_from_file_location("eng", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(eng)


def retune(n):
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


def legal_step(w, w2):
    """Is `w → w2` one rule of the system applied in one context?"""
    for name, rel, lm in eng.RULES:
        others = [x for x in rel if x != lm]
        for k in eng.infix_positions(w, lm):
            for o in others:
                if w[:k] + o + w[k + len(lm):] == w2:
                    return name
    return None


def block(prefix, suffix, d, i, j1, j2):
    """One block: Bokut-Shiao at top `d`, then `d` far-commutations."""
    dw = eng.desc_word
    Y = dw(i, i - (d - 1))                     # the run the new letter crosses
    x = i - (d + 1)
    Z = (i - d,) + dw(i - (d + 1), j1) + dw(i - (d + 1), j2)
    out = [prefix + Y + (x,) + Z + suffix]     # after the Bokut-Shiao step
    for k in range(len(Y) - 1, -1, -1):        # carry `x` left, one letter a time
        out.append(prefix + Y[:k] + (x,) + Y[k:] + Z + suffix)
    return out


def chain(i, a, b):
    dw = eng.desc_word
    j1, j2 = i - a, i - b
    D = dw(i, j1)
    Q = lambda d: dw(i - 1, i - d)
    R = [(i - 2,)]
    for d in range(b + 1):
        R.append(R[-1] + (i - (d + 1),))

    V = [D + (i - 1,) + dw(i, j2),
         (i,) + (i - 2, i - 1) + dw(i - 2, j1) + dw(i, j2),
         (i - 2,) + D + dw(i, j2)]
    for d in range(b + 1):
        V += block(R[d], (), d, i, j1, j2)
        assert V[-1] == R[d + 1] + D + dw(i - (d + 1), j2), \
            f"V block {d} does not land on the invariant"
    U = [Q(1) + D + dw(i - 1, j2) + (i,)]
    for d in range(1, b + 1):
        U += block(Q(d), (i,), d, i, j1, j2)
        assert U[-1] == Q(d + 1) + D + dw(i - (d + 1), j2) + (i,), \
            f"U block {d} does not land on the invariant"
    U.append(Q(b + 1) + (i - 1,) + D)          # B₁₀ at the tail
    U.append((i - 2,) + Q(b + 1) + D)          # the fixed-depth step onto W
    return V, U


def main():
    bad = tot = 0
    print(" b   a   i    V steps  U steps   total   b²+3b+5   illegal")
    for b in range(2, 8):
        for a in range(b + 1, b + 5):
            n = a + 4
            for i in (a, a + 1):
                if i >= n:
                    continue
                retune(n)
                V, U = chain(i, a, b)
                ill = []
                for seq, tag in ((V, "V"), (U, "U")):
                    for k in range(len(seq) - 1):
                        if legal_step(seq[k], seq[k + 1]) is None:
                            ill.append(f"{tag}{k}")
                if V[-1] != U[-1]:
                    ill.append("endpoints differ")
                tot += 1
                bad += bool(ill)
                nv, nu = len(V) - 1, len(U) - 1
                if ill or (nv + nu) != b * b + 3 * b + 5:
                    print(f"{b:>2} {a:>3} {i:>3} {nv:>10} {nu:>8} {nv+nu:>7} "
                          f"{b*b+3*b+5:>9}   {','.join(ill) or '-'}")
    print(f"\ncases: {tot}   with an illegal step or wrong length: {bad}")

    for b in range(2, 8):
        n, i, a = b + 6, b + 3, b + 2
        retune(n)
        V, U = chain(i, a, b)
        print(f"b={b}:  V {len(V)-1} steps (2 + {b+1} + {b*(b+1)//2}), "
              f"U {len(U)-1} steps ({b} + {b*(b+1)//2} + 2), "
              f"total {len(V)+len(U)-2} = {b*b+3*b+5}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
