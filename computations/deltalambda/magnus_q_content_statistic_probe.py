#!/usr/bin/env python3
"""magnus_q_content_statistic_probe.py — do the q-DEFORMED contents order the per-dim majorant,
where every q-independent statistic failed? (qou-o6ov)

THE DEFECT IN THE PREVIOUS SEARCH, named. #6587 tested seven candidate statistics against
tr_λ(X*X)/dim_λ and all seven died. They share a property I did not state at the time and which
makes the failure much less surprising: EVERY ONE OF THEM IS q-INDEPENDENT. b(λ)=n−λ₁, ℓ(λ),
n(λ)=Σ(i−1)λ_i, n(λ'), n(λ)−n(λ'), b+ℓ, dim_λ are all pure combinatorics of the Young diagram.
The quantity they were asked to order is not: tr_λ(X*X)/dim_λ is a normalized character of a fixed
positive element of H_n(q), and q enters at every step. A q-independent statistic can track it only
by accident.

THE STRUCTURALLY MOTIVATED CANDIDATES. χ_λ(z)/dim_λ for CENTRAL z is a symmetric function of the
Jucys–Murphy contents x_□ = q^{2(j−i)}, □ ∈ λ — that is the standard JM/central-character structure
of H_n(q). X*X is NOT central, so this is not a derivation and this probe does not claim it is; it
is the reason to look at q-content symmetric functions rather than at more diagram combinatorics.
They are also q-DEPENDENT and they separate λ from λ' (transposition sends c ↦ −c, i.e. x ↦ x⁻¹),
which #6556's conjugate-pair result says any working statistic must do.

CANDIDATES (all over cells □=(i,j) of λ, content c = j−i, 1-indexed):
    P₁  = Σ q^{2c}            the q-content power sum — the first JM symmetric function
    P₂  = Σ q^{4c}
    P₋₁ = Σ q^{-2c}           = P₁(λ')
    P₁−P₋₁                    the q-deformation of n(λ')−n(λ); the asymmetric combination
    P₁+P₋₁                    symmetric under λ↔λ' — included EXPECTING failure, because #6556 says
                              a symmetric statistic cannot order a pair that it cannot separate
    P₁/n                      per-cell normalization
    log-spread Σ|2c·ln q|     a q-scaled spread; the crudest of the set

THE CONTROL THAT MAKES THIS NON-CIRCULAR, and it is unusually clean: at q=1 every power sum above
collapses to |λ| = n EXACTLY, for every λ. So at q=1 these statistics carry zero information and
P₁−P₋₁ is identically 0. Whatever ordering they produce at q₀ is therefore a pure q-effect and is
disjoint from the seven q-independent candidates — it cannot be one of them wearing a new name.
The probe VERIFIES this collapse numerically rather than asserting it.

A pass here is a statistic that orders the measured sample — NOT a bound and NOT a proof. A failure
is worth as much: it says the per-dim majorant is not a function of the q-contents alone either, and
the envelope form is what survives.

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


def contents(lam):
    """Contents c(□) = j − i over the cells of λ (1-indexed rows/cols)."""
    return [j - i for i, p in enumerate(lam) for j in range(p)]


def q_stats(lam, q):
    """The q-content symmetric functions. At q=1 every power sum here equals |λ| exactly."""
    cs = contents(lam)
    p1 = sum(q ** (2 * c) for c in cs)
    p2 = sum(q ** (4 * c) for c in cs)
    pm1 = sum(q ** (-2 * c) for c in cs)
    n = len(cs)
    return {
        "P₁": p1,
        "P₂": p2,
        "P₋₁": pm1,
        "P₁−P₋₁": p1 - pm1,
        "P₁+P₋₁": p1 + pm1,
        "P₁/n": p1 / n,
        "Σ|2c·lnq|": sum(abs(2 * c * mp.log(q)) for c in cs),
    }


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    # THE CONTROL, verified not asserted: at q=1 the power sums are identically n.
    one = mp.mpf(1)
    worst_collapse = mp.mpf(0)
    for lam in base.partitions(n):
        st = q_stats(tuple(lam), one)
        worst_collapse = max(worst_collapse,
                             abs(st["P₁"] - n), abs(st["P₂"] - n), abs(st["P₋₁"] - n),
                             abs(st["P₁−P₋₁"]))
    collapsed = worst_collapse < mp.mpf(10) ** -100

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
            continue          # exact-zero endpoints: Ω₂^P vanishes identically on 1-dim reps
        rows.append((lam, dim, val / dim, q_stats(lam, q)))

    print(f"[qcontent] A={A} (n={n}); do the q-contents x_□ = q^{{2(j−i)}} order tr_λ(X*X)/dim_λ?  "
          f"{len(rows)} interior shapes, dim ≤ {max_dim}")
    print(f"[qcontent] q₀ = {mp.nstr(q, 12)};  every candidate below is q-DEPENDENT — that is the")
    print(f"[qcontent] point, since all seven of #6587's dead candidates were q-independent.")
    print(f"[qcontent] CONTROL: at q=1 the power sums collapse to n={n} for every λ?  "
          f"{'YES ✓' if collapsed else 'NO ✗'}  (worst |dev| = {mp.nstr(worst_collapse,3)})")
    print(f"[qcontent] ⇒ any ordering below is a pure q-effect, disjoint from the seven.\n")

    names = list(rows[0][3].keys())
    print("   λ                  dim   per-dim      " + "  ".join(f"{nm:>12}" for nm in names))
    for lam, dim, pd, st in sorted(rows, key=lambda r: -r[2]):
        print(f"  {str(lam):<18} {dim:>4}  {mp.nstr(pd,7):>10}   "
              + "  ".join(f"{mp.nstr(st[nm],7):>12}" for nm in names))

    print("\n   statistic            strictly monotone?     inversions   ties(differing per-dim)")
    winners = []
    for nm in names:
        inv = ties = 0
        for i in range(len(rows)):
            for j in range(len(rows)):
                si, sj = rows[i][3][nm], rows[j][3][nm]
                pi, pj = rows[i][2], rows[j][2]
                # monotone in EITHER direction: count violations of decreasing and of increasing,
                # and take the better — the sign of a statistic is a convention, not a claim.
                if si < sj and pi < pj:
                    inv += 1
                if si == sj and i < j and pi != pj:
                    ties += 1
        inv_up = 0
        for i in range(len(rows)):
            for j in range(len(rows)):
                si, sj = rows[i][3][nm], rows[j][3][nm]
                pi, pj = rows[i][2], rows[j][2]
                if si < sj and pi > pj:
                    inv_up += 1
        best = min(inv, inv_up)
        direction = "dec" if inv <= inv_up else "inc"
        ok = best == 0 and ties == 0
        if ok:
            winners.append((nm, direction))
        print(f"  {nm:<20} {('YES ✓ (' + direction + ')') if ok else 'NO':<22} "
              f"{best:>10}   {ties:>10}")

    if skipped:
        print(f"\n  SKIPPED {len(skipped)} shape(s) over the dim cap (NOT evidence — just not run): "
              + ", ".join(f"{l}({d})" for l, d in skipped))
    print()
    if winners:
        print(f"  ⇒ candidate(s) ordering this sample: {[w[0] for w in winners]}. The q=1 control")
        print("    above shows these carry no combinatorial content, so this is a genuine q-effect")
        print("    and not one of the seven dead statistics renamed. It is a statistic that ORDERS")
        print("    the measured sample — NOT a bound, NOT a proof, and it must be checked at another")
        print("    size before being carried into any claim.")
    else:
        print("  ⇒ NO q-content statistic orders the sample either. Combined with #6587's seven")
        print("    q-independent failures, the per-dim majorant is not a function of the q-contents")
        print("    alone. The envelope max_{b(λ)=b} remains the only surviving global form, and the")
        print("    next move is to bound IT rather than to hunt a ninth statistic.")


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
