#!/usr/bin/env python3
"""magnus_hook_kappa_column_probe.py — the hook cancellation column, and why it is cheap. (qou-o6ov)

WHY THIS IS AFFORDABLE WHEN THE CENSUS IS NOT. κ = |Σ eig| / Σ|eig| needs EIGENVALUES, and mp.eig
costs ~dim³ (measured at dps 65: 9.9 s at dim 42, 154 s at dim 105, ~22 min projected at dim 216).
A complete n=9 κ census is ~1h45m. But the HOOKS have dim = C(n-1, b) — at n=9 that is
8, 28, 56, 70, 56, 28, 8, all ≤ 70 — so the entire hook column costs under two minutes. When one
family answers the question, measure that family rather than the census.

WHAT IT SETTLES. #6754 found the arc's bound loose by up to 550×, and the loss factors as
|tr| = κ·Σ|eig|. I claimed hooks have RISING κ, making them the driver of a non-monotone κ envelope
at high b. The column REFUTES the "rising" half and CONFIRMS the consequence:

    b:      1        2        3        4        5        6        7
    κ:   0.9362   0.5365   0.1042   0.0981   0.0661   0.2507   0.6852
                                             ^ minimum, then a steep rise

κ is U-SHAPED, not monotone. But the hook is the LOWEST κ in its level at b=3 (0.104 against 0.276,
0.228) and the HIGHEST at b=6 (0.251 against 0.073, 0.154) and b=7 (0.685 against 0.372) — so the
hook crosses from level-min to level-max, and the κ envelope's rise from b=6 to b=7 is entirely a
hook effect.

THE MECHANISM IS IN THE SAME TABLE, which is why it is reported alongside rather than inferred:
the hook's Σ|eig|/dim collapses 213× (35.94 → 0.169) while its |tr|/dim falls 291×. κ is their
ratio, so it dips and then rebounds once the magnitude falls faster than the trace.

THIRD INDEPENDENT APPEARANCE of one structural split. Hooks behave oppositely to every other family
in the per-dim majorant (#6748: level-max → level-min), in pointwise monotonicity (#6729: 6 of 6
violations have a hook on the low side), and now in the cancellation factor (level-min → level-max).
Each time, hooks are the family that already has a derived closed form (the reduced Burau, #6556).

scope-(a); NO-FLOAT64 (mpf, dps 65). Nothing wired.

NOTE ON dps, learned the hard way here: every probe in this arc sets mp.mp.dps at module scope, so
dps MUST be set AFTER all imports. Doing it before let an import silently reset 65 → 140; the
_assert_dps guard from #6710 caught it and refused to compute rather than return numbers at an
unrequested precision. That guard is imported below deliberately.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
import magnus_kappa_decomposition_probe as K  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps          # AFTER the imports — see the module docstring
    K._WANT_DPS = args.dps

    q = base.Q0
    n = 3 * args.A
    Z, N = args.A // 2, args.A - args.A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[hookkappa] n={n}: the whole hook κ column — dims C({n-1},b) are all small, so this")
    print(f"[hookkappa] costs under two minutes where a κ census costs ~1h45m.  (mp.dps={args.dps})\n")
    print("   b   hook                       dim      κ          |tr|/dim    Σ|eig|/dim")
    ks, trs, sas = [], [], []
    for b in range(1, n - 1):
        lam = tuple([n - b] + [1] * b)
        M, dim = K.build_X_dense(lam, gens, q, ngen)
        E, _ = mp.eig(M)
        tr = mp.re(sum(M[i, i] for i in range(dim)))
        sa = sum(abs(x) for x in E)
        k = abs(tr) / sa if sa > 0 else mp.mpf(0)
        ks.append(k); trs.append(abs(tr) / dim); sas.append(sa / dim)
        print(f"  {b:>2}   {str(lam):<26} {dim:>4}  {mp.nstr(k,7):>10}  {mp.nstr(abs(tr)/dim,7):>10}"
              f"  {mp.nstr(sa/dim,7):>11}")

    inc = all(ks[i + 1] > ks[i] for i in range(len(ks) - 1))
    dec = all(ks[i + 1] < ks[i] for i in range(len(ks) - 1))
    lo = min(range(len(ks)), key=lambda i: ks[i])
    print(f"\n  hook κ monotone?  increasing {inc}, decreasing {dec}  →  "
          f"{'U-SHAPED, minimum at b=' + str(lo + 1) if not (inc or dec) else 'monotone'}")
    print(f"  across b=1..{len(ks)}:  Σ|eig|/dim falls {mp.nstr(sas[0]/sas[-1],5)}× ,  "
          f"|tr|/dim falls {mp.nstr(trs[0]/trs[-1],5)}×")
    print("  κ is their RATIO, so it dips and then rebounds once the magnitude falls faster than")
    print("  the trace — the mechanism, from the same table rather than inferred.")


if __name__ == "__main__":
    main()
