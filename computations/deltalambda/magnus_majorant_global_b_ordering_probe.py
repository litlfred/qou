#!/usr/bin/env python3
"""magnus_majorant_global_b_ordering_probe.py — does the per-dim majorant decay with b(λ) across
ALL shapes, or only inside the two families that have handles? (qou-o6ov)

WHERE THIS SITS. The arc now has two reductions of the positive majorant tr_λ(X*X) = ‖M_λ‖_F²
(X = ρ·Ω₂^P): the HOOK column to the reduced Burau (a derived monotone bound), and the TWO-ROW
column to a difference of sector Frobenius norms of the fixed 4×4 Ř (exact, monotone). At n=9 those
are 2 of the 30 shapes' worth of structure; most λ are neither.

THE QUESTION THIS ANSWERS, and it is prior to finding a third handle: is
    tr_λ(X*X) / dim_λ    decreasing in b(λ) = n − λ₁    GLOBALLY, across all λ?
If YES the arc's target is a genuine global statement and a general handle is worth hunting. If NO
— if some higher-b shape outside the two families has a LARGER per-dim majorant than a lower-b one
— then the b-ordering is a family-level phenomenon, and no general bound of that shape can exist.
That is a cheap question with an expensive consequence either way, and it should be settled before
building a third reduction.

Prior evidence is CONJUGATE-PAIR only (#6556: 9/9 pairs, dim controlled). That establishes decay
between λ and λ', not a global ordering over all shapes — a pair test cannot see a violation
between two shapes that are not conjugate. This probe checks the global claim directly.

REPORTS: every λ (up to a dim cap) sorted by b, with tr_λ(X*X)/dim_λ, flagging every INVERSION
(a pair λ, μ with b(λ) < b(μ) but per-dim(λ) < per-dim(μ)). Inversions are listed individually, not
summarised — one real inversion refutes the global claim and must not be averaged away.
scope-(a); NO-FLOAT64 (mpf, dps 140). Nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402


def family(lam, n):
    if len(lam) == 1:
        return "trivial"
    if lam[0] == 1:
        return "sign"
    if all(p == 1 for p in lam[1:]):
        return "hook"
    if len(lam) <= 2:
        return "two-row"
    return "OTHER"


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[global] A={A} (n={n}); tr_λ(X*X)/dim_λ vs b(λ) over ALL λ, dim ≤ {max_dim}")
    print(f"[global] hook + two-row have handles; 'OTHER' has none — the question is whether the")
    print(f"[global] b-ordering is global or only intra-family.\n")
    print("    b   λ                  dim    family     tr_λ(X*X)/dim_λ")
    data, skipped = [], []
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            skipped.append((lam, d))
            continue
        X, Xstar, dim, _a = build(lam, gens, q, ngen)
        P = Xstar * X
        val = mp.re(sum(P[i, i] for i in range(dim)))
        data.append((sum(lam) - lam[0], lam, dim, family(lam, n), val / dim))
    for b, lam, d, fam, pd in sorted(data):
        print(f"  {b:>3}   {str(lam):<18} {d:>4}   {fam:<9}  {mp.nstr(pd, 8):>15}")

    # EXCLUDE the exact-zero endpoints. On a 1-dim rep every σ is a scalar, so Ω₂^P = Σ[σ,σ] = 0
    # identically and tr(X*X) = 0 (the manifest endpoint-zero of #6445). Those are not
    # counterexamples to a decay ordering, they are its degenerate extreme — and leaving them in
    # makes "0 < anything" register as an inversion against every other shape, which is noise.
    interior = [row for row in data if row[4] > 0]
    n_zero = len(data) - len(interior)

    # every inversion among the interior, listed
    inv = []
    for i in range(len(interior)):
        for j in range(len(interior)):
            bi, li, _di, fi, pi = interior[i]
            bj, lj, _dj, fj, pj = interior[j]
            if bi < bj and pi < pj:
                inv.append((li, fi, bi, pi, lj, fj, bj, pj))
    print()
    print(f"  ({n_zero} exact-zero endpoint shape(s) excluded — Ω₂^P vanishes identically on 1-dim reps)")

    # LEVEL SEPARATION: is max at level b strictly below min at level b-1? Stronger than
    # "no inversions" — it says the b-levels do not even interleave.
    lvl = {}
    for b, lam, d, fam, pd in interior:
        lvl.setdefault(b, []).append(pd)
    bs = sorted(lvl)
    print("\n   b    min per-dim      max per-dim     (shapes)   separated from b−1?")
    sep_all = True
    for idx, b in enumerate(bs):
        lo, hi = min(lvl[b]), max(lvl[b])
        if idx == 0:
            sep = "—"
        else:
            ok = hi < min(lvl[bs[idx - 1]])
            sep_all = sep_all and ok
            sep = "YES" if ok else "NO"
        print(f"  {b:>2}    {mp.nstr(lo,8):>12}    {mp.nstr(hi,8):>12}     {len(lvl[b]):>4}       {sep}")
    print(f"\n  LEVEL SEPARATION (max at b < min at b−1, every consecutive pair)?  "
          f"{'YES ✓' if sep_all and len(bs) > 1 else 'NO'}")

    # THE ENVELOPE. A decay BOUND needs only  max_{b(λ)=b} per-dim  to fall with b — it does NOT
    # need every high-b shape to sit below every lower-b shape. These are different claims and the
    # weaker one is the one a theorem would use, so it is reported separately rather than folded in.
    env = [max(lvl[b]) for b in bs]
    env_mono = all(env[i + 1] < env[i] for i in range(len(env) - 1))
    print(f"  ENVELOPE (max per-dim at each b) strictly decreasing?  "
          f"{'YES ✓' if env_mono and len(env) > 1 else 'NO'}")
    print("      " + " > ".join(mp.nstr(e, 6) for e in env)
          + ("   (b levels: " + ", ".join(str(b) for b in bs) + ")"))
    if skipped:
        print(f"  SKIPPED {len(skipped)} shape(s) over the dim cap (NOT evidence — just not run): "
              + ", ".join(f"{l}(dim {d})" for l, d in skipped) + "\n")
    if not inv:
        print(f"  NO INVERSIONS among the {len(interior)} interior shapes: tr_λ(X*X)/dim_λ is globally\n  decreasing in b(λ).")
        print("  ⇒ the b-ordering is GLOBAL, not intra-family — a general handle is worth hunting,")
        print("    and a general bound of this shape is not excluded.")
    else:
        print(f"  {len(inv)} INVERSION(S) among the {len(interior)} interior shapes — global claim REFUTED as stated:")
        for li, fi, bi, pi, lj, fj, bj, pj in inv:
            print(f"    b={bi} {li} [{fi}] per-dim {mp.nstr(pi,6)}  <  b={bj} {lj} [{fj}] per-dim {mp.nstr(pj,6)}")
        fams = {(fi, fj) for li, fi, bi, pi, lj, fj, bj, pj in inv}
        print(f"    families involved: {sorted(fams)}")
        print("  ⇒ per-dim majorant is NOT globally monotone in b. Any general bound must be in a")
        print("    weaker form (an envelope, or b together with another statistic) — report this")
        print("    rather than generalising the intra-family monotonicity.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=50)
    args = ap.parse_args()
    for A in args.A:
        analyze(A, args.max_dim)
        print()


if __name__ == "__main__":
    main()
