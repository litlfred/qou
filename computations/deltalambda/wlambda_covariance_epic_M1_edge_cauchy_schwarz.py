#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): a SECOND Cauchy-Schwarz -- on the EDGE measure, not on the (D,W) pair -- and it
gives a sufficient condition stated entirely in objects the Fulman identity reaches. Then measured.

WHY A SECOND CS. #6651 priced the FIRST one: N <= sqrt(V_D V_W), the relaxation behind the (CS)
margin, keeps >= 78.6% of the true margin. But the SAME PR then showed that route's one remaining
object V_A is NOT reachable by the exchangeable-pair identity (A is an eigenfunction of the up-down
chain at no non-degenerate n <= 12), and #6627 showed it has no polynomial closed form either. So a
tight relaxation was aimed at an intractable object. This probe aims the relaxation somewhere else.

THE EDGE MEASURE. The Fulman identity writes both halves of M_1 = P - N as sums over the SAME edge
set with the SAME non-negative weight. With an edge moving a box out of content u (in lam) into
content v, d_u/d_v the diagonal lengths in lam, g = |u| - |v| and delta = d_u - d_v:

    Delta(A) = g,   Delta(W) = g(|u|+|v|),   Delta(D) = 2*delta - 2

    P = Sum_edges dmu * g^2                       dmu := pi(lam) J(lam,lam*) (|u|+|v|) >= 0
    N = Sum_edges dmu * g(2 - 2*delta)

(both divided by the common 2(1-beta_3) = 6/(n+1), which cancels out of every ratio below). P's
integrand is a SQUARE, which is exactly the corpus's Fact A. N's is not, which is exactly why Fact B
is false. Cauchy-Schwarz on this measure:

    N <= sqrt( Sum dmu g^2 ) * sqrt( Sum dmu (2-2*delta)^2 ) = sqrt( P * Q ),  Q := Sum dmu (2-2delta)^2

    ==>   Q < P   IMPLIES   N < P   IMPLIES   M_1 > 0.

That is a sufficient condition in TWO edge sums of the same shape over the same measure -- one
weighting the CONTENT gap g, the other the DIAGONAL gap 2(1-delta). Neither needs V_A, V_D, or any
object outside the identity's reach. Whether it is TRUE is the question this probe measures; it is
not assumed anywhere, and a failure is reported as a failure.

WHAT ELSE IS ESTABLISHED HERE -- the reversal symmetry, which closes one route.
The chain is reversible with w(lam,lam*) = f^lam f^lam* / (n+1)!, manifestly symmetric. Under
reversal the same edge is read from the other end, and:

    g  -> -g          (the contents swap roles)
    delta -> 2 - delta  (removing at u drops d_u by 1, adding at v raises d_v by 1)
    k := g + 2delta - 2  ->  -k

so the term g*k*(|u|+|v|) is INVARIANT and the weight is unchanged. Consequence: THE NEGATIVE EDGE
SET IS CLOSED UNDER REVERSAL. A negative edge's reverse is negative too, never positive. So the most
natural pairing/injection argument -- cancel each negative edge against its own reverse -- cannot
work, and this is a proof of that, not a reading of a census. It is checked at every edge below.

WHAT THIS DOES NOT DO. Q < P is SUFFICIENT, never necessary: it is a relaxation, and if it fails
that says nothing about M_1 > 0, which is measured positive throughout. Nothing here is a bound at
the n >= 79 the epic needs; the window is finite and a trend over it is not evidence.

CONTROLS. Every number is gated on reconstructing objects that are already known independently:
  (1) P and N rebuilt from the edge sums must equal Cov(A,W) and -Cov(D,W) computed directly from
      the Plancherel measure, exactly, at every n;
  (2) N <= sqrt(P*Q) must hold at every n -- it is Cauchy-Schwarz, so a violation is a bug in me;
  (3) the reversal identities g'=-g, delta'=2-delta, w'=w must hold at every edge.
If any control fails the probe says so and quotes no verdict.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 40
NMAX = 20


def _load_reach():
    """Chain helpers from the sibling reach probe, by explicit file path (the _path_bridge bootstrap
    trap: this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_eigenfunction_reach.py"
    spec = importlib.util.spec_from_file_location("_m1_reach", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cells(lam):
    return {(i, j) for i, part in enumerate(lam) for j in range(part)}


def diag_lengths(lam):
    d = {}
    for i, part in enumerate(lam):
        for j in range(part):
            d[j - i] = d.get(j - i, 0) + 1
    return d


def show(fr, digits=6):
    """Display an exact Fraction without ever computing in float64."""
    return mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), digits)


def main():
    reach = _load_reach()
    cl = reach._load_cl()

    print("# a SECOND Cauchy-Schwarz, on the EDGE measure. exact Fractions/ints throughout;")
    print("# mpmath only for square roots and display. NO float64.")
    print("#")
    print("#   P = Sum dmu g^2      N = Sum dmu g(2-2delta)      Q = Sum dmu (2-2delta)^2")
    print("#   dmu = pi(lam) J(lam,lam*) (|u|+|v|) >= 0 ;  g = |u|-|v| ;  delta = d_u - d_v")
    print("#   CS:  N <= sqrt(P Q).   So  Q < P  IMPLIES  M_1 > 0.  (sufficient, never necessary)")
    print("#")
    print(f"#   {'n':>3} {'P':>12} {'N':>12} {'Q':>12} {'P/Q':>9} {'N/sqrt(PQ)':>11} "
          f"{'surviving':>10} {'Q<P?':>5} {'rev ok':>7}")

    ctrl_pn_ok = True
    ctrl_cs_ok = True
    ctrl_rev_ok = True
    rows = []

    for n in range(4, NMAX + 1):
        nfact = cl.fact(n)
        parts = [tuple(p) for p in cl.partitions(n)]
        dim = {p: reach.dim_partition(p, nfact) for p in parts}
        st = {p: reach.stats_of(p, n) for p in parts}
        pi = {p: F(dim[p] * dim[p], nfact) for p in parts}
        dl = {p: diag_lengths(p) for p in parts}
        cs = {p: cells(p) for p in parts}

        cover = {}
        for p in parts:
            for mu in reach.addable(p):
                cover.setdefault(mu, []).append(p)
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        # --- direct Plancherel covariances, the independent yardstick for control (1) ---
        EA = sum(pi[p] * st[p][0] for p in parts)
        ED = sum(pi[p] * st[p][1] for p in parts)
        EW = sum(pi[p] * st[p][2] for p in parts)
        cov_AW = sum(pi[p] * st[p][0] * st[p][2] for p in parts) - EA * EW
        cov_DW = sum(pi[p] * st[p][1] * st[p][2] for p in parts) - ED * EW

        # --- the three edge sums ---
        sum_P = sum_N = sum_Q = F(0)
        edge_terms = {}
        for a in parts:
            for b, jab in J[a].items():
                if a == b:
                    continue
                only_a = cs[a] - cs[b]
                only_b = cs[b] - cs[a]
                if len(only_a) != 1 or len(only_b) != 1:
                    ctrl_rev_ok = False           # not a single-box move: the chain is wrong
                    continue
                (ia, ja), = only_a
                (ib, jb), = only_b
                u = ja - ia
                v = jb - ib
                d_u = dl[a].get(u, 0)
                d_v = dl[a].get(v, 0)
                g = abs(u) - abs(v)
                delta = d_u - d_v

                w = pi[a] * jab
                dmu = w * (abs(u) + abs(v))
                sum_P += dmu * g * g
                sum_Q += dmu * (2 - 2 * delta) ** 2
                sum_N += dmu * g * (2 - 2 * delta)
                edge_terms[(a, b)] = (w, g, delta, g * (g + 2 * delta - 2))

        # (3) reversal: same weight, g -> -g, delta -> 2 - delta, term invariant.
        for (a, b), (w, g, delta, term) in edge_terms.items():
            rev = edge_terms.get((b, a))
            if rev is None:
                ctrl_rev_ok = False
                continue
            w2, g2, delta2, term2 = rev
            if w2 != w or g2 != -g or delta2 != 2 - delta or term2 != term:
                ctrl_rev_ok = False

        # the identity's divisor, common to both halves: 2(1-beta_3) = 6/(n+1)
        scale = F(n + 1, 6)
        P = sum_P * scale
        N = sum_N * scale
        Q = sum_Q * scale

        # (1) P and N must reproduce the directly-computed covariances exactly
        if P != cov_AW or N != -cov_DW:
            ctrl_pn_ok = False

        # (2) Cauchy-Schwarz itself. Compare squares so the check stays exact.
        if N > 0 and N * N > P * Q:
            ctrl_cs_ok = False

        ratio_PQ = F(P, 1) / Q if Q != 0 else None
        mP = mp.mpf(P.numerator) / mp.mpf(P.denominator)
        mN = mp.mpf(N.numerator) / mp.mpf(N.denominator)
        mQ = mp.mpf(Q.numerator) / mp.mpf(Q.denominator)
        tight = mN / mp.sqrt(mP * mQ) if P > 0 and Q > 0 else None
        # surviving = the share of the TRUE margin P - N that the relaxation still certifies.
        # Directly comparable to #6651's [0.786, 0.852] for the FIRST (D,W) Cauchy-Schwarz.
        surv = (mP - mp.sqrt(mP * mQ)) / (mP - mN) if P > N and P > 0 and Q > 0 else None
        rows.append((n, P, N, Q, ratio_PQ, tight, surv))
        print(f"#   {n:>3} {show(P):>12} {show(N):>12} {show(Q):>12} "
              f"{show(ratio_PQ) if ratio_PQ is not None else '-':>9} "
              f"{mp.nstr(tight, 6) if tight is not None else '-':>11} "
              f"{mp.nstr(surv, 6) if surv is not None else '-':>10} "
              f"{'YES' if ratio_PQ is not None and ratio_PQ > 1 else 'no':>5} "
              f"{'ok' if ctrl_rev_ok else 'FAIL':>7}")

    print("#")
    print("# CONTROLS (nothing below is meaningful unless all three pass):")
    print(f"#   (1) P == Cov(A,W) and N == -Cov(D,W) exactly, every n : "
          f"{'PASS' if ctrl_pn_ok else 'FAIL'}")
    print(f"#   (2) N <= sqrt(P Q) at every n (it is CS -- a FAIL is a bug in me) : "
          f"{'PASS' if ctrl_cs_ok else 'FAIL'}")
    print(f"#   (3) reversal: w'=w, g'=-g, delta'=2-delta, term invariant, every edge : "
          f"{'PASS' if ctrl_rev_ok else 'FAIL'}")

    controls_ok = ctrl_pn_ok and ctrl_cs_ok and ctrl_rev_ok
    if not controls_ok:
        print("#")
        print("# A CONTROL FAILED. No verdict is quoted; the derivation above is unverified.")
        print("RESULT: controls failed -- no verdict. qou-k5r5 OPEN.")
        return

    # --- the verdict, computed ---
    late = [r for r in rows if r[0] >= 12]
    holds_all = all(r[4] is not None and r[4] > 1 for r in rows)
    holds_late = all(r[4] is not None and r[4] > 1 for r in late)
    pq = [r[4] for r in late if r[4] is not None]
    pq_min, pq_max = min(pq), max(pq)
    tights = [r[5] for r in late if r[5] is not None]
    t_min, t_max = min(tights), max(tights)
    survs = [r[6] for r in late if r[6] is not None]
    s_min, s_max = min(survs), max(survs)

    # SHAPE, not an endpoint comparison. Comparing pq[-1] to pq[0] called this column "falling"
    # when it in fact turns and rises for the whole second half -- and which of those is true is
    # the difference between "may cross 1" and "moving away from 1". Classify by the argmin/argmax.
    imin, imax = pq.index(pq_min), pq.index(pq_max)
    last = len(pq) - 1
    if imin == 0 and imax == last:
        shape = "rising monotonically across the window"
    elif imax == 0 and imin == last:
        shape = "falling monotonically across the window"
    elif 0 < imin < last:
        shape = (f"U-SHAPED: it falls to a minimum {show(pq_min)} at n = {late[imin][0]} and RISES "
                 f"for the rest of the window (n = {late[imin][0]}..{late[last][0]}), so the "
                 f"endpoint comparison alone would call it falling and be wrong about the tail")
    elif 0 < imax < last:
        shape = (f"peaked: it rises to {show(pq_max)} at n = {late[imax][0]} then falls")
    else:
        shape = "not monotone in either direction"

    print("#")
    print(f"# P/Q over n >= 12 : min {show(pq_min)}  max {show(pq_max)}")
    print(f"#   shape: {shape}")
    print(f"# N/sqrt(PQ) over n >= 12 (how tight THIS CS is) : "
          f"min {mp.nstr(t_min, 6)}  max {mp.nstr(t_max, 6)}")
    print(f"# surviving margin (P - sqrt(PQ))/(P - N) over n >= 12 : "
          f"min {mp.nstr(s_min, 6)}  max {mp.nstr(s_max, 6)}")
    print(f"#   COMPARE #6651's FIRST Cauchy-Schwarz, on the (D,W) pair: surviving [0.786, 0.852].")
    print(f"#   So the two relaxations cost about the SAME -- but this one lands on P and Q, both")
    print(f"#   inside the identity's reach, while that one lands on V_A, which is not.")

    if holds_all:
        verdict = (
            f"the edge-measure CS sufficient condition Q < P HOLDS at every n in 4..{NMAX} "
            f"(P/Q in [{show(pq_min)}, {show(pq_max)}] over n >= 12; {shape}). Q < P implies "
            f"N < P implies M_1 > 0, and BOTH sums are over the same edge measure with the same "
            f"shape -- so this route needs neither V_A nor V_D, the two objects #6651 showed the "
            f"exchangeable-pair identity does not reach. That makes Q < P a candidate target a "
            f"finite-n argument can actually attack.")
    elif holds_late:
        verdict = (
            f"the edge-measure CS condition Q < P FAILS at small n but HOLDS from some n on "
            f"(P/Q in [{show(pq_min)}, {show(pq_max)}] over n >= 12; {shape}). Sufficient only "
            f"where it holds; the small-n failures are not evidence against M_1 > 0, which is "
            f"positive throughout.")
    else:
        verdict = (
            f"the edge-measure CS condition Q < P FAILS -- P/Q in [{show(pq_min)}, {show(pq_max)}] "
            f"over n >= 12; {shape} -- i.e. Q is the LARGER sum. So this relaxation is too lossy to "
            f"certify M_1 > 0, even though M_1 > 0 holds throughout. That is a scope-(a) negative "
            f"about the RELAXATION, not about M_1: the diagonal-gap sum 2(1-delta) carries more "
            f"weight than the content-gap sum g, and the cross term N recovers the margin only "
            f"because the two are CORRELATED -- which is exactly what CS throws away.")

    print("#")
    print(f"# VERDICT (computed, not predicted): {verdict}")
    print("#")
    print("# ESTABLISHED REGARDLESS, and it closes a route: the negative edge set is CLOSED UNDER")
    print("#   REVERSAL (control 3, every edge). g -> -g and delta -> 2-delta leave the term")
    print("#   g(g+2delta-2) and the weight both invariant, so a negative edge's reverse is negative")
    print("#   too. Cancelling each negative edge against its own reverse -- the most natural")
    print("#   pairing argument, and the one #6651's census could only argue against -- CANNOT work.")
    print("#   That is scope-(b) for THAT pairing (a proved invariant forbids it), and scope-(a)")
    print("#   for pairing in general: a different injection is untested here.")
    print("#")
    print(f"# Window n <= {NMAX} against a requirement of n >= 79. Nothing here is a bound.")
    print(f"RESULT: {verdict} Negative edges proved closed under reversal. Controls (1)(2)(3) all "
          f"PASS. qou-k5r5 OPEN.")


if __name__ == "__main__":
    main()
