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
    """The q-content symmetric functions, plus the two q-INDEPENDENT controls.

    The controls are here so the comparison is WITHIN-SAMPLE. #6587 measured b(λ) on its own
    run with its own dim cap and its own counting rule; quoting its inversion count against a
    count produced here would be a cross-run comparison, and the two rules differ — this one
    also charges TIES, which b incurs heavily (it takes few values) and an injective statistic
    cannot. Both numbers must come from the same table or neither means anything.
    """
    cs = contents(lam)
    p1 = sum(q ** (2 * c) for c in cs)
    p2 = sum(q ** (4 * c) for c in cs)
    pm1 = sum(q ** (-2 * c) for c in cs)
    n = len(cs)
    nl = sum(i * p for i, p in enumerate(lam))
    cj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    nlp = sum(j * p for j, p in enumerate(cj))
    return {
        "P₁": p1,
        "P₂": p2,
        "P₋₁": pm1,
        "P₁−P₋₁": p1 - pm1,
        "P₁+P₋₁": p1 + pm1,
        "P₁/n": p1 / n,
        "Σ|2c·lnq|": sum(abs(2 * c * mp.log(q)) for c in cs),
        "b(λ) [ctl]": mp.mpf(-(sum(lam) - lam[0])),   # negated: all candidates read "decreasing"
        "n'−n [ctl]": mp.mpf(nlp - nl),
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

    npairs = len(rows) * (len(rows) - 1) // 2
    print(f"\n   statistic            strictly monotone?     inversions   ties(differing per-dim)"
          f"   [of {npairs} pairs]")
    winners, detail = [], {}
    for nm in names:
        inv = ties = inv_up = 0
        inv_pairs, inv_up_pairs, tie_pairs = [], [], []
        for i in range(len(rows)):
            for j in range(len(rows)):
                si, sj = rows[i][3][nm], rows[j][3][nm]
                pi, pj = rows[i][2], rows[j][2]
                # monotone in EITHER direction: count violations of decreasing and of increasing,
                # and take the better — the sign of a statistic is a convention, not a claim.
                if si < sj and pi < pj:
                    inv += 1
                    inv_pairs.append((rows[i], rows[j]))
                if si < sj and pi > pj:
                    inv_up += 1
                    inv_up_pairs.append((rows[i], rows[j]))
                if si == sj and i < j and pi != pj:
                    ties += 1
                    tie_pairs.append((rows[i], rows[j]))
        best = min(inv, inv_up)
        direction = "dec" if inv <= inv_up else "inc"
        detail[nm] = (best, direction, inv_pairs if inv <= inv_up else inv_up_pairs, tie_pairs)
        ok = best == 0 and ties == 0
        if ok:
            winners.append((nm, direction))
        print(f"  {nm:<20} {('YES ✓ (' + direction + ')') if ok else 'NO':<22} "
              f"{best:>10}   {ties:>10}")

    # NAME the surviving violations for the near-misses. A count of 1 is a specific pair of
    # shapes, and reporting it as a number hides the only thing that could be acted on.
    # Controls INCLUDED here. A control that near-misses as well as the candidate is the whole
    # result, and filtering it out of the detail would hide exactly that.
    near = [nm for nm in names if 0 < detail[nm][0] <= 2]
    blockers = {}
    for nm in near:
        best, direction, pairs, _t = detail[nm]
        print(f"\n  {nm} misses by {best} — the surviving violation(s), named:")
        for (li, _di, pi, sti), (lj, _dj, pj, stj) in pairs:
            blockers.setdefault(frozenset((li, lj)), []).append(nm)
            print(f"    {str(li):<20} {nm}={mp.nstr(sti[nm],7):>10}  per-dim={mp.nstr(pi,7)}")
            print(f"    {str(lj):<20} {nm}={mp.nstr(stj[nm],7):>10}  per-dim={mp.nstr(pj,7)}"
                  f"   ← same b-level? {sum(li)-li[0] == sum(lj)-lj[0]}")

    # IS IT ONE PAIR? "every near-miss fails on the same shapes" is a far sharper statement than
    # "several statistics have 1 inversion", and it is a different claim — so it is tested, not
    # read off the table by eye.
    if blockers:
        print("\n   the blocking pair(s), and which near-miss statistics each defeats:")
        for pr, who in sorted(blockers.items(), key=lambda kv: -len(kv[1])):
            a, b_ = sorted(pr, key=lambda t: -sum(t))
            print(f"    {str(a)} vs {str(b_)}  defeats {len(who)}: {who}")
        if len(blockers) == 1 and len(near) > 1:
            print(f"  ⇒ ALL {len(near)} near-miss statistics fail on the SAME single pair. The")
            print("    obstruction is one shape-degeneracy, not a diffuse failure of the whole")
            print("    statistic class — a materially different (and more tractable) situation.")

    # IS THE q-CANDIDATE INDEPENDENT EVIDENCE? P₁−P₋₁ = Σ(q^{2c} − q^{−2c}) = 2Σ sinh(2c·ln q),
    # whose leading term is 4·ln q·Σc = 4·ln q·(n(λ')−n(λ)) — i.e. it is the q-DEFORMATION of the
    # control, not a different idea. Two statistics agreeing means nothing if one is a deformation
    # of the other, so the honest test is whether they induce the SAME ORDERING on this sample. If
    # they do, the q-deformation bought nothing here and must not be reported as corroboration.
    if "P₁−P₋₁" in names and "n'−n [ctl]" in names:
        disagree = [(rows[i][0], rows[j][0])
                    for i in range(len(rows)) for j in range(i + 1, len(rows))
                    if ((rows[i][3]["P₁−P₋₁"] < rows[j][3]["P₁−P₋₁"])
                        != (rows[i][3]["n'−n [ctl]"] < rows[j][3]["n'−n [ctl]"]))]
        print(f"\n  INDEPENDENCE CHECK — P₁−P₋₁ is the q-deformation of the control n(λ')−n(λ)")
        print(f"  (leading order 4·ln q·Σc). Do they induce the SAME ordering on this sample?  "
              f"{'YES — ' + str(len(rows)) + ' shapes, 0 disagreements' if not disagree else 'NO, ' + str(len(disagree)) + ' pair(s) differ'}")
        if not disagree:
            print("  ⇒ the q-content near-miss is NOT independent evidence: it is the control")
            print("    wearing a q. Do not report the two as agreeing candidates.")
        else:
            print("    differing pair(s): " + ", ".join(f"{a} vs {b_}" for a, b_ in disagree[:5]))
    for nm in names:
        if nm.endswith("[ctl]") and detail[nm][3]:
            print(f"\n  {nm}: {len(detail[nm][3])} tie(s) with differing per-dim — a statistic taking "
                  f"few values\n    cannot order a sample strictly, which is why its inversion count "
                  f"alone flatters it.")

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
