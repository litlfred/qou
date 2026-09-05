#!/usr/bin/env python3
"""magnus_fs_transpose_prune_probe.py — the Féray–Śniady character bound cannot be tight here, by
a transpose-invariance argument. (qou-o6ov)

WHY THIS WAS THE NEXT ROUTE. Two bound routes are closed — the norm relaxation (#6754, loose to
550×) and the commutator reformulation (#6757, 2.0–2.6× LOOSER) — and the a-sum reduction of the
#6534 identity captures at most ~9× of the effect (#6798). A corpus-grep then found the classical
literature this arc had never consulted, including Féray–Śniady, "Asymptotics of characters of
symmetric groups related to Stanley character formula" (library/arxiv-math-0701051v4), whose
Theorem 1 bounds the NORMALIZED character directly:

    |χ̂_λ(π)|  ≤  [ a · max( r(λ)/n , c(λ)/n , |π|/n ) ]^{|π|},        χ̂_λ(e) = 1

That is exactly the per-shape quantity this arc measures, with no norm and no eigendecomposition —
the two things both closed routes depended on. It looked like the right object.

THE PRUNE, and it is structural rather than numerical. For a FIXED element the bound's only
λ-dependence is through max(r(λ), c(λ)). Transposing λ exchanges rows and columns, so

    max(r(λ'), c(λ'))  =  max(c(λ), r(λ))  =  max(r(λ), c(λ))                          (INVARIANCE)

i.e. the bound assigns λ and λ' the SAME value. But the measured |tr_λ|/dim_λ is strongly
transpose-ASYMMETRIC — #6556 first saw this on conjugate pairs, and the complete n=9 census makes it
exact. So the bound is necessarily loose by at least the conjugate-pair ratio on one member of every
pair, BEFORE any constant a is fitted.

Measured worst pair: (8,1) 29.0013 against (2,1⁷) 0.110202 — a factor 263.16. The existing chain's
slack is 2.04–550× (#6754), so FS in its stated form has a structural floor that is not better than
what the arc already has.

THE FIGURE, AND A NUMBER OF MINE IT CORRECTS. 263.16 is verified three independent ways at dps 65 —
the dense diagonal of `build_X_dense`, the column-wise sweep of `trace_and_frob`, and `Σ eig` — all
agreeing to 10 significant figures on both members of the pair. It supersedes a 291.4× I quoted from
a DRAFT of the hook-κ column probe, whose (8,1) read 33.648; that draft's output is identifiable by
its ASCII header (`kappa`, `S|eig|`) where the committed probe prints unicode. The 291.4 reached the
audit doc for #6779, which needs the correction — the U-shape and the mechanism there are unaffected,
since both depend on the column's SHAPE rather than its scale.

SCOPE — this is a scope-(b) structural exclusion, and the invariant is named. It excludes "the FS
bound AS STATED can be tight for this problem", by (INVARIANCE) together with measured
transpose-asymmetry. It does NOT exclude a q-deformation of FS carrying a transpose-ASYMMETRIC shape
parameter; that remains open and is precisely what such a deformation would have to supply. Nothing
here is a criticism of FS, which is a true theorem about a different regime (q=1, single permutation).

WHY IT IS WORTH RUNNING RATHER THAN ASSERTING. The invariance is a one-line fact, but "the measured
quantity is transpose-asymmetric" is a claim about this corpus at this q₀, and the ratio is the whole
strength of the prune. The probe verifies BOTH halves: that max(r,c) really is equal across every
conjugate pair, and what the asymmetry actually is.

scope-(b) with the invariant cited; NO-FLOAT64 (mpf, dps 65). Nothing wired.
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
import magnus_chain_end_to_end_probe as CE  # noqa: E402


def conj(lam):
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def max_rc(lam):
    """max(rows, cols) — the ONLY λ-dependence of the FS bound at a fixed element."""
    return max(len(lam), lam[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps            # AFTER imports (#6710 trap)
    CE._WANT_DPS = args.dps

    q = base.Q0
    n = 3 * args.A
    Z, N = args.A // 2, args.A - args.A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[fsprune] n={n}: FS Theorem 1 bounds |χ̂_λ(π)| by [a·max(r/n, c/n, |π|/n)]^|π|.")
    print(f"[fsprune] At a FIXED element its only λ-dependence is max(r(λ), c(λ)), which is")
    print(f"[fsprune] TRANSPOSE-INVARIANT. The measured quantity is not. Verifying both halves.\n")

    vals = {}
    for lam in base.partitions(n):
        lam = tuple(lam)
        tr, _frob, dim = CE.trace_and_frob(lam, gens, q, ngen)
        vals[lam] = (dim, abs(tr) / dim)

    print(f"  {'λ':<22}{'max(r,c)':>9}{'|tr|/dim':>12}   {'λ′':<22}{'max(r,c)':>9}"
          f"{'|tr|/dim':>12}{'ratio':>9}")
    seen, worst, inv_ok = set(), mp.mpf(0), True
    for lam in sorted(vals, key=lambda l: -vals[l][1]):
        c = conj(lam)
        if lam in seen or c == lam or c not in vals:
            continue
        seen.add(lam); seen.add(c)
        a, b = vals[lam][1], vals[c][1]
        inv_ok = inv_ok and (max_rc(lam) == max_rc(c))
        if min(a, b) > 0:
            r = max(a, b) / min(a, b)
            worst = max(worst, r)
            print(f"  {str(lam):<22}{max_rc(lam):>9}{mp.nstr(a,6):>12}   {str(c):<22}"
                  f"{max_rc(c):>9}{mp.nstr(b,6):>12}{mp.nstr(r,5):>9}")

    print(f"\n  (1) max(r,c) equal across EVERY conjugate pair?  {'YES ✓' if inv_ok else 'NO ✗'}")
    print(f"  (2) worst measured conjugate-pair ratio in |tr|/dim:  {mp.nstr(worst,6)}×")
    print(f"\n  ⇒ PRUNED, scope-(b): the FS bound AS STATED is transpose-invariant, so it is loose")
    print(f"    by ≥ {mp.nstr(worst,5)}× on one member of that pair, before any constant is fitted.")
    print("    The existing chain's slack is 2.04–550× (#6754), so FS's structural floor is not")
    print("    better than what the arc already has.")
    print("\n    NOT excluded: a q-deformation of FS carrying a transpose-ASYMMETRIC shape")
    print("    parameter. That stays open, and is exactly what such a deformation must supply.")
    print("    This is no criticism of FS — a true theorem about q=1 and a single permutation.")


if __name__ == "__main__":
    main()
