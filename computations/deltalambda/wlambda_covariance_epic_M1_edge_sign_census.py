#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): P > N in LOCAL form -- is the edge contribution positive EDGE BY EDGE?
If it were, M_1 > 0 would follow for every n immediately and the gap would close. It is not, and
this measures exactly how much cancellation survives, which is what a finite-n argument must beat.

WHY THIS, NOW. The commits before it on this branch established that the exchangeable-pair identity
reaches P and N (and NOT V_A), and verified the identity itself exactly. That makes P > N the
recommended target, and P > N has a LOCAL form the margin route does not:

    M_1 = Cov(Sum h, W) = E_pi[(Sum h - Sum h*)(W - W*)] / (2(1 - beta_3)),   1 - beta_3 = 3/(n+1)

a weighted sum over single-box moves of the up-down chain. Two per-edge sign facts are recorded in
the corpus (2026-08-21, verified there to n <= 8 and n <= 13 respectively):

    Fact A   Delta(A) * Delta(W) >= 0  on every edge   =>  P >= 0
    Fact B   Delta(D) * Delta(W) <= 0  on every edge   =>  N >= 0

Both are re-verified here at every edge to n = 12, independently. The question they do NOT answer is
the one that decides the gap:

    Is  Delta(Sum h) * Delta(W) = Delta(A)*Delta(W) + Delta(D)*Delta(W)  >= 0  on every edge?

Facts A and B give a POSITIVE plus a NEGATIVE term, so their sum is of indefinite sign and nothing
about it follows from either. If it were non-negative edge-by-edge, M_1 > 0 would be immediate for
all n -- so the honest expectation is that it is not, and the useful output is the CENSUS: how many
edges go the wrong way, and how much of the total weight sits on them.

WHAT IS REPORTED. Over ordered pairs (lam, lam*) of the chain with lam != lam* (the diagonal
contributes 0 identically, since every Delta vanishes there):

    pos_mass  = sum of  pi(lam) J(lam,lam*) * DSh * DW  over edges where that term is > 0
    neg_mass  = |same, over edges where it is < 0|
    ratio     = pos_mass / neg_mass          -- the local form of P/N; > 1 iff M_1 > 0

and the edge counts behind them. The ratio's trend in n is the quantity a finite-n argument would
have to bound away from 1; the count tells you whether the negative edges are a thin exceptional set
(suggesting a pairing or injection argument) or a constant fraction (suggesting they are not).

SELF-CHECK, gating every number: the reconstructed M_1 = (pos_mass - neg_mass)/(2(1-beta_3)) is
compared EXACTLY against M_1 computed directly by summation over partitions. If they disagree the
census is describing something other than M_1 and nothing here may be quoted.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30
NMAX = 12


def _load_reach():
    """Import the chain helpers from the sibling reach probe by explicit file path (the _path_bridge
    bootstrap trap: this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_eigenfunction_reach.py"
    spec = importlib.util.spec_from_file_location("_m1_reach", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    reach = _load_reach()
    cl = reach._load_cl()

    print("# P > N in LOCAL form: is the edge contribution positive EDGE BY EDGE?")
    print("# exact Fractions throughout; mpmath only to display a ratio. NO float64.")
    print("#")
    print(f"#   {'n':>3} {'FactA':>6} {'FactB':>6} {'combined>=0':>12} {'#pos':>7} {'#neg':>7} "
          f"{'neg frac':>9} {'pos/neg mass':>13}")

    rows = []
    checks_ok = True
    for n in range(3, NMAX + 1):
        nfact = cl.fact(n)
        parts = [tuple(p) for p in cl.partitions(n)]
        dim = {p: reach.dim_partition(p, nfact) for p in parts}
        st = {p: reach.stats_of(p, n) for p in parts}
        pi = {p: F(dim[p] * dim[p], nfact) for p in parts}

        cover = {}
        for p in parts:
            for mu in reach.addable(p):
                cover.setdefault(mu, []).append(p)
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        factA = True
        factB = True
        factB_witness = None
        combined = True
        npos = nneg = 0
        pos_mass = F(0)
        neg_mass = F(0)
        for a in parts:
            for b, w in J[a].items():
                if a == b:
                    continue                      # every Delta vanishes; contributes 0 identically
                dA = st[a][0] - st[b][0]
                dD = st[a][1] - st[b][1]
                dW = st[a][2] - st[b][2]
                if dA * dW < 0:
                    factA = False
                if dD * dW > 0:
                    factB = False
                    if factB_witness is None:
                        factB_witness = (a, b, st[b][1], st[a][1], st[b][2], st[a][2])
                term = pi[a] * w * (dA + dD) * dW
                if term > 0:
                    npos += 1
                    pos_mass += term
                elif term < 0:
                    nneg += 1
                    neg_mass += -term
                    combined = False

        # --- SELF-CHECK: does this census actually reconstruct M_1?
        beta3 = F(n - 2, n + 1)
        M1_local = (pos_mass - neg_mass) / (2 * (1 - beta3))
        EH = sum(pi[p] * (st[p][0] + st[p][1]) for p in parts)
        EW = sum(pi[p] * st[p][2] for p in parts)
        M1_direct = sum(pi[p] * (st[p][0] + st[p][1]) * st[p][2] for p in parts) - EH * EW
        if M1_local != M1_direct:
            checks_ok = False

        negfrac = F(nneg, npos + nneg) if (npos + nneg) else F(0)
        ratio = (mp.mpf(pos_mass.numerator) / pos_mass.denominator /
                 (mp.mpf(neg_mass.numerator) / neg_mass.denominator)) if neg_mass else mp.inf
        rows.append((n, factA, factB, combined, npos, nneg, negfrac, ratio, M1_direct,
                     factB_witness))
        print(f"#   {n:>3} {'ok' if factA else 'FAIL':>6} {'ok' if factB else 'FAIL':>6} "
              f"{'YES' if combined else 'no':>12} {npos:>7} {nneg:>7} "
              f"{mp.nstr(mp.mpf(negfrac.numerator)/negfrac.denominator, 4):>9} "
              f"{mp.nstr(ratio, 6):>13}")
    print("#")

    print("# SELF-CHECK (gates every number above): the census reconstructs M_1 exactly?")
    print(f"#   (pos_mass - neg_mass)/(2(1-beta_3)) == Cov(Sum h, W) computed directly : "
          f"{'PASS' if checks_ok else 'FAIL'}")
    if not checks_ok:
        print("RESULT: SELF-CHECK FAILED -- the census is not describing M_1; no figure here may be "
              "quoted. qou-k5r5 OPEN.")
        print("EXIT: 0")
        return 0
    print("#")

    all_A = all(r[1] for r in rows)
    all_B = all(r[2] for r in rows)
    b_fail = [r[0] for r in rows if not r[2]]
    print("# THE TWO CORPUS FACTS, re-verified independently at EVERY edge:")
    print(f"#   Fact A  Delta(A)*Delta(W) >= 0 on every edge, n <= {NMAX} : "
          f"{'HOLDS' if all_A else 'FAILS'}  (corpus verified n <= 8; extended here)")
    print(f"#   Fact B  Delta(D)*Delta(W) <= 0 on every edge, n <= {NMAX} : "
          f"{'HOLDS' if all_B else 'FAILS'}")
    if not all_B:
        w = next(r[9] for r in rows if not r[2])
        nb = b_fail[0]
        print(f"#")
        print(f"#   *** THIS CONTRADICTS THE CORPUS. docs/audits/2026-08-21-covariance-kernel-M1-")
        print(f"#   fulman-exchangeable-pair-reduction.md states Fact B holds 'on every single-box")
        print(f"#   edge ... verified n<=13'. It FAILS here, first at n = {nb}, on n = {b_fail}.")
        print(f"#   Explicit counterexample (hand-verified), n = {nb}:")
        print(f"#     lam* = {w[1]}  ->  lam = {w[0]}   (joined in the chain)")
        print(f"#     D : {w[2]} -> {w[3]}   W : {w[4]} -> {w[5]}   so dD*dW > 0, not <= 0.")
        print(f"#   WHY the stated reason fails: the audit argues 'moving a box to a diagonal of")
        print(f"#   larger |content| (nearer the edge, hence shorter) DECREASES Sum D^2'. That")
        print(f"#   tracks the EQUILIBRIUM SHAPE, not the actual diagonal lengths. Landing a box on")
        print(f"#   a diagonal of current length d raises its square by 2d+1 whatever the content")
        print(f"#   is; here the box leaves a length-1 diagonal (1 -> 0) and lands on another")
        print(f"#   length-1 one (1 -> 4), for a net +2.")
        print(f"#   WHAT SURVIVES: N >= 0 itself is NOT refuted -- it is positive at every n in this")
        print(f"#   arc's own table (#6651). What fails is the PER-EDGE argument for it, so 'both")
        print(f"#   signs are manifest edge by edge' is true of P (Fact A) and NOT of N at n >= {nb}.")
        print(f"#   The reduction M_1 = P - N is an identity and is unaffected (verified exactly).")
    print("#")

    # QUANTIFIER, and this is the THIRD small-n degeneracy of this arc (after #6602's family-tested-
    # at-a-point and the reach probe's constant-statistic-counted-as-eigenfunction). At n = 3,4,5
    # there are simply no negative edges yet -- the chain is too small to exhibit one -- so an
    # `any(n)` over the whole table reports "a positive n exists" and says nothing. The meaningful
    # statement is where the property STARTS failing and whether it ever recovers.
    first_neg = next((r[0] for r in rows if not r[3]), None)
    recovers = [r[0] for r in rows if r[0] > (first_neg or 0) and r[3]]
    negfracs = [r[6] for r in rows if first_neg is not None and r[0] >= first_neg]
    ratios = [r[7] for r in rows if first_neg is not None and r[0] >= first_neg]
    print(f"# THE COMBINED SUM Delta(Sum h)*Delta(W):")
    print(f"#   edge-wise non-negative for n < {first_neg} (too few edges to exhibit one), then")
    print(f"#   NEVER again over n = {first_neg}..{NMAX}" +
          (f" -- recovers at n = {recovers}" if recovers else " (no recovery)"))
    print(f"#   negative-edge fraction over n >= 6 : "
          f"{mp.nstr(mp.mpf(min(negfracs).numerator)/min(negfracs).denominator,4)} .. "
          f"{mp.nstr(mp.mpf(max(negfracs).numerator)/max(negfracs).denominator,4)}")
    print(f"#   pos/neg MASS ratio over n >= 6      : {mp.nstr(min(ratios),6)} .. "
          f"{mp.nstr(max(ratios),6)}   (> 1 iff M_1 > 0)")
    print("#")

    if first_neg is not None and not recovers:
        verdict = (f"TWO findings. (1) Fact B is FALSE: Delta(D)*Delta(W) <= 0 does NOT hold on "
                   f"every edge, failing at n = {b_fail} against the corpus's 'verified n<=13' -- "
                   f"N >= 0 survives (it is positive at every n) but its PER-EDGE argument does "
                   f"not, so only P's sign is edge-wise manifest. (2) The combined term is "
                   f"edge-wise non-negative only for n < {first_neg} and never after, so M_1 > 0 "
                   f"does NOT follow from per-edge signs; what must be bounded is the pos/neg MASS "
                   f"ratio, measured in [{mp.nstr(min(ratios),5)}, {mp.nstr(max(ratios),5)}] over "
                   f"n >= {first_neg}, against the threshold 1")
    else:
        verdict = ("the combined term recovers edge-wise non-negativity at some n above its first "
                   "failure -- re-derive before acting, this contradicts the expectation")
    print(f"# VERDICT (computed, not predicted): {verdict}.")
    print("#")
    print("# WHAT THIS BUYS, and what it does not. It converts P > N into a statement about a")
    print("#   WEIGHTED EDGE SUM with a measured margin, on a set whose negative part is a")
    print("#   substantial fraction rather than a thin exceptional set -- which ARGUES AGAINST a")
    print("#   pairing/injection argument over the negative edges and FOR bounding the mass ratio")
    print("#   directly. That is a reading of the census, not a proof that pairing cannot work.")
    print(f"#   Window n <= {NMAX} against a requirement of n >= 79; nothing here is a bound.")
    print(f"RESULT: {verdict}. Self-check: census reconstructs M_1 exactly at every n. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
