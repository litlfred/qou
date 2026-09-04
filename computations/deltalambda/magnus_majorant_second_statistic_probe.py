#!/usr/bin/env python3
"""magnus_majorant_second_statistic_probe.py — which statistic orders the per-dim majorant, given
that b(λ) alone does not? (qou-o6ov)

THE CONSTRAINT. Pointwise monotonicity in b(λ) = n − λ₁ is REFUTED: at A=3 the hook (3,1⁶) at b=6
has per-dim majorant 14.32, BELOW the b=7 shapes (2,2,2,2,1) 31.56 and (2,2,2,1,1,1) 24.97. Only
the ENVELOPE max_{b(λ)=b} survives. So a general bound needs a second statistic — or a different
one entirely.

WHAT THE INVERSIONS SAY IT MUST DO. Within a single b-level the spread is large (15× at b=6, 72×
at b=7) and the shapes with MORE rows sit LOWER. So the ordering statistic must separate λ from
its transpose — it cannot be symmetric under λ ↔ λ'. That rules out b(λ)+b(λ') and max(b,b') a
priori, and it is consistent with #6556's conjugate-pair result (λ and λ' have very different
per-dim values while sharing every symmetric statistic).

CANDIDATES TESTED (each: is per-dim strictly decreasing when shapes are sorted by it?):
    b(λ) = n − λ₁                the current one — expected to FAIL, included as the control
    ℓ(λ) = number of rows = λ'₁
    n(λ) = Σ (i−1)·λ_i           the theoretically motivated one: the corpus's own
                                 Δ_λ = (−1)^{n(λ)}·dim V_λ is graded by exactly this
    n(λ') = Σ (j−1)·λ'_j
    n(λ) − n(λ')                 the asymmetric combination
    b + ℓ                        naive; I expect it to fail and it is included so the failure is
                                 on the record rather than in my head
    dim_λ                        a null control — if per-dim sorted by dim were monotone, the
                                 "decay" would be a dimension artifact and not about λ's shape
A candidate PASSES only if it is strictly monotone with NO inversions. Ties are reported, not
silently accepted: two shapes sharing a statistic value but differing in per-dim means that
statistic cannot order them, which is itself a refutation of a strict claim.

This probe does NOT propose a bound. It narrows which statistic a bound could use, and records
which candidates are dead. scope-(a); NO-FLOAT64 (mpf, dps 140). Nothing wired.
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
from magnus_conjugate_pair_cancellation_probe import conjugate  # noqa: E402


def n_stat(lam):
    """n(λ) = Σ (i−1)·λ_i."""
    return sum(i * p for i, p in enumerate(lam))


def stats(lam, n):
    cj = conjugate(lam)
    b = sum(lam) - lam[0]
    ell = len(lam)
    nl, nlp = n_stat(lam), n_stat(cj)
    return {
        "b(λ)": b,
        "ℓ(λ)": ell,
        "n(λ)": nl,
        "n(λ')": nlp,
        "n(λ)−n(λ')": nl - nlp,
        "b+ℓ": b + ell,
    }


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    rows, skipped = [], []
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            skipped.append((lam, d))
            continue
        X, Xstar, dim, _a = build(lam, gens, q, ngen)
        P = Xstar * X
        val = mp.re(sum(P[i, i] for i in range(dim)))
        if val <= 0:
            continue                      # exact-zero endpoints: the degenerate extreme
        rows.append((lam, dim, val / dim, stats(lam, n)))

    print(f"[stat] A={A} (n={n}); which statistic orders tr_λ(X*X)/dim_λ?  "
          f"{len(rows)} interior shapes, dim ≤ {max_dim}")
    print(f"[stat] b(λ) is the control and is expected to FAIL (pointwise refuted).\n")
    names = list(rows[0][3].keys()) + ["dim_λ (null control)"]
    print("   λ                  dim   per-dim      " + "  ".join(f"{nm:>11}" for nm in names[:-1]))
    for lam, dim, pd, st in sorted(rows, key=lambda r: -r[2]):
        print(f"  {str(lam):<18} {dim:>4}  {mp.nstr(pd,7):>10}   "
              + "  ".join(f"{st[nm]:>11}" for nm in names[:-1]))

    print("\n   statistic            strictly decreasing?   inversions   ties(differing per-dim)")
    verdicts = {}
    for nm in names:
        key = (lambda r, nm=nm: r[1]) if nm.startswith("dim") else (lambda r, nm=nm: r[3][nm])
        inv = ties = 0
        for i in range(len(rows)):
            for j in range(len(rows)):
                si, sj = key(rows[i]), key(rows[j])
                pi, pj = rows[i][2], rows[j][2]
                if si < sj and pi < pj:
                    inv += 1
                if si == sj and i < j and pi != pj:
                    ties += 1
        ok = inv == 0 and ties == 0
        verdicts[nm] = ok
        print(f"  {nm:<20} {'YES ✓' if ok else 'NO':<22} {inv:>10}   {ties:>10}")

    if skipped:
        print(f"\n  SKIPPED {len(skipped)} shape(s) over the dim cap (NOT evidence — just not run): "
              + ", ".join(f"{l}({d})" for l, d in skipped))
    winners = [nm for nm, ok in verdicts.items() if ok and not nm.startswith("dim")]
    print()
    if verdicts.get("dim_λ (null control)"):
        print("  ⚠ THE NULL CONTROL PASSED: per-dim is ordered by dim_λ itself on this sample, so any")
        print("    'winner' here may be a dimension artifact rather than a fact about λ's shape.")
    if winners:
        print(f"  ⇒ candidate ordering statistic(s): {winners}. NOT a bound and NOT a proof — a")
        print("    statistic that orders the measured sample. It must be checked at another size")
        print("    before being carried into any claim.")
    else:
        print("  ⇒ NO single candidate orders the sample. The per-dim majorant is not a function of")
        print("    any of these statistics alone; a general bound needs either a genuinely different")
        print("    invariant or the envelope form (which does hold). Reporting the dead ends.")


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
