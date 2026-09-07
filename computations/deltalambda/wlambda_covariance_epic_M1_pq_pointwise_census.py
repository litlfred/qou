#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): is Q < P POINTWISE nearly-true, or only in aggregate? Measured, per edge.

WHY THIS QUESTION AND WHY NOW. #6651 established that the edge-measure Cauchy-Schwarz gives a
sufficient condition for M_1 > 0 stated entirely in objects the exchangeable-pair identity reaches:

    P = Sum dmu * g^2                     dmu := pi(lam) J(lam,lam*) (|u|+|v|) >= 0
    Q = Sum dmu * (2 - 2 delta)^2         g = |u| - |v|,  delta = d_u - d_v
    Q < P  =>  N < P  =>  M_1 > 0

and that it HOLDS at every n <= 20 with P/Q in [2.231, 2.266]. The live target is therefore a
finite-n proof of Q < P. Before searching for one, settle which KIND of proof is even available,
because the two possibilities need completely different arguments:

  * POINTWISE — every edge (or all but a thin, characterisable set) satisfies g^2 >= (2-2delta)^2.
    Then Q < P follows from a per-edge inequality plus a bound on the exceptional set, and the
    whole thing is a local combinatorial statement about one partition and one box move.
  * AGGREGATE ONLY — the negative part is a substantial fraction of the mass, as it is for M_1
    itself (pos/neg ~ 50 over n >= 16, measured in #6651). Then no per-edge argument closes it and
    the proof must control the joint distribution of (g, delta) under Plancherel.

THE PER-EDGE TERM, in closed form. Delta(A) = g and Delta(D) = 2 delta - 2, so the integrand of
P - Q is a difference of two squares and factors with no case split:

    g^2 - (2 - 2 delta)^2 = (g - 2 + 2 delta)(g + 2 - 2 delta) = k * (2g - k),    k := g + 2 delta - 2

so an edge subtracts from P - Q exactly when k(2g - k) < 0. Note k = Delta(A) + Delta(D) = Delta(Sum h)
is the SAME k whose sign against g decides the M_1 census (#6651: negative iff g*k < 0). The two
criteria share k and are otherwise different: g*k < 0 against k*(2g-k) < 0. They are NOT nested in
either direction, and this probe reports both so the sets can be compared rather than assumed.

WHAT IS ALSO WORTH READING OFF, and it is the reason to normalise. Dividing by Z = Sum dmu makes
both sides second moments of the same measure:

    Q < P   <=>   E_nu[Delta(D)^2] < E_nu[Delta(A)^2],     dnu = dmu / Z

i.e. across an edge the DIAGONAL statistic D moves less, in mean square, than the absolute-content
statistic A. Stated that way the target is a comparison of two moments rather than an inequality
between two unnormalised sums, and the moments are comparable across n.

THE HEURISTIC BEING TESTED. Near the ENDS of the content range a corner sits on a short diagonal, so
|g| is large and delta small -- the edge contributes positively. Near the CENTRE both d_u and d_v are
large, but delta is their DIFFERENCE and may be small too. So the sign of the negative-mass
localisation is not obvious from the shape argument, and this probe measures it two ways: by |g|, and
by the mean content-magnitude |u|+|v| on the negative set against the positive set. A negative set
concentrated at small |u|+|v| would be the bulk; at large, the ends.

CONTROLS -- no verdict is quoted unless all four pass:
  (1) P rebuilt from the edges matches Cov(A,W) computed from the Plancherel measure with no edges
      at all -- an independent yardstick. Q has NO such yardstick (it is not a covariance against W),
      so control (2) is what covers its arithmetic; do not read (1) as validating Q;
  (2) Sum of the per-edge terms == P - Q exactly, at every n (the census reconstructs its own target);
  (3) the closed-form criterion k(2g-k) < 0 agrees with the measured sign at EVERY edge;
  (4) the per-edge term is invariant under edge reversal (g -> -g, delta -> 2 - delta), as the M_1
      term is -- so reverse-pairing cannot cancel this negative set either.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 40
NMAX = 20


def _load(stem):
    """Load a sibling probe by explicit file path (the _path_bridge bootstrap trap: this probe must
    run with PYTHONPATH unset)."""
    src = pathlib.Path(__file__).resolve().parent / f"{stem}.py"
    spec = importlib.util.spec_from_file_location(f"_m1_{stem}", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def show(fr, digits=6):
    """Display an exact Fraction without ever computing in float64."""
    return mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), digits)


def main():
    cs = _load("wlambda_covariance_epic_M1_edge_cauchy_schwarz")
    reach = _load("wlambda_covariance_epic_M1_eigenfunction_reach")
    cl = reach._load_cl()

    print("# is Q < P POINTWISE, or only in aggregate? exact Fractions/ints; mpmath only to display.")
    print("#")
    print("#   per-edge integrand of P - Q :  g^2 - (2-2delta)^2 = k(2g - k),  k = g + 2delta - 2")
    print("#   NEGATIVE edge for P-Q  <=>  k(2g - k) < 0     [distinct from M_1's  g*k < 0]")
    print("#   normalised:  Q < P  <=>  E_nu[Delta(D)^2] < E_nu[Delta(A)^2],  dnu = dmu / Z")
    print("#")
    print(f"#   {'n':>3} {'E[dA^2]':>10} {'E[dD^2]':>10} {'P/Q':>8} {'neg frac':>9} "
          f"{'P-Q p/n':>9} {'M_1 p/n':>9} {'<|u|+|v|>-':>10} {'<|u|+|v|>+':>10}")

    ctrl_pq_ok = True
    ctrl_recon_ok = True
    ctrl_crit_ok = True
    ctrl_rev_ok = True
    rows = []

    for n in range(4, NMAX + 1):
        nfact = cl.fact(n)
        parts = [tuple(p) for p in cl.partitions(n)]
        dim = {p: reach.dim_partition(p, nfact) for p in parts}
        pi = {p: F(dim[p] * dim[p], nfact) for p in parts}
        dl = {p: cs.diag_lengths(p) for p in parts}
        cells = {p: cs.cells(p) for p in parts}

        cover = {}
        for p in parts:
            for mu in reach.addable(p):
                cover.setdefault(mu, []).append(p)
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        sum_P = sum_Q = sum_T = Z = F(0)
        neg_mass = pos_mass = F(0)
        n_edge = n_neg = 0
        cmag_neg = cmag_pos = F(0)
        by_g = {}
        terms = {}
        # M_1's OWN census, on this same edge set and this same n-window, so the two ratios are
        # comparable as a measurement rather than against a differently-windowed prior figure.
        m1_neg = m1_pos = F(0)
        g0_mass = F(0)          # the g = 0 edges, which contribute EXACTLY 0 to M_1

        for a in parts:
            for b, jab in J[a].items():
                if a == b:
                    continue
                only_a = cells[a] - cells[b]
                only_b = cells[b] - cells[a]
                if len(only_a) != 1 or len(only_b) != 1:
                    ctrl_rev_ok = False           # not a single-box move: the chain is wrong
                    continue
                (ia, ja), = only_a
                (ib, jb), = only_b
                u, v = ja - ia, jb - ib
                g = abs(u) - abs(v)
                delta = dl[a].get(u, 0) - dl[a].get(v, 0)
                cmag = abs(u) + abs(v)
                dmu = pi[a] * jab * cmag

                dA, dD = g, 2 * delta - 2
                t = dmu * (dA * dA - dD * dD)

                sum_P += dmu * dA * dA
                sum_Q += dmu * dD * dD
                sum_T += t
                Z += dmu
                n_edge += 1
                terms[(a, b)] = (dmu, g, delta, t)

                # (3) the closed-form criterion, checked against the measured sign at every edge
                k = g + 2 * delta - 2
                if (k * (2 * g - k) < 0) != (t < 0):
                    ctrl_crit_ok = False

                if t < 0:
                    n_neg += 1
                    neg_mass += -t
                    cmag_neg += (-t) * cmag
                    ag = abs(g)
                    by_g[ag] = by_g.get(ag, F(0)) + (-t)
                    if g == 0:
                        g0_mass += -t
                else:
                    pos_mass += t
                    cmag_pos += t * cmag

                m1 = dmu * g * k
                if m1 < 0:
                    m1_neg += -m1
                else:
                    m1_pos += m1

        # (4) reversal: the P-Q term must be invariant, exactly as the M_1 term is.
        for (a, b), (dmu, g, delta, t) in terms.items():
            rev = terms.get((b, a))
            if rev is None or rev[0] != dmu or rev[1] != -g or rev[2] != 2 - delta or rev[3] != t:
                ctrl_rev_ok = False

        # (1) P must reproduce Cov(A,W) computed from the PLANCHEREL MEASURE with no edges at all.
        #     That is a genuinely independent yardstick: a different formula over a different index
        #     set. (Q has NO such yardstick -- it is not a covariance of anything against W, being
        #     Sum dmu Delta(D)^2 rather than Sum piJ Delta(D)Delta(W). Control (2) is what covers
        #     Q's arithmetic. Do not read control (1) as validating Q.)
        st = {p: reach.stats_of(p, n) for p in parts}
        EA_p = sum(pi[p] * st[p][0] for p in parts)
        EW_p = sum(pi[p] * st[p][2] for p in parts)
        cov_AW = sum(pi[p] * st[p][0] * st[p][2] for p in parts) - EA_p * EW_p
        if sum_P * F(n + 1, 6) != cov_AW:
            ctrl_pq_ok = False
        # (2) the census reconstructs its own target
        if sum_T != sum_P - sum_Q:
            ctrl_recon_ok = False

        EA = sum_P / Z
        ED = sum_Q / Z
        ratio = F(sum_P, 1) / sum_Q if sum_Q != 0 else None
        negfrac = F(n_neg, n_edge) if n_edge else F(0)
        posneg = F(pos_mass, 1) / neg_mass if neg_mass != 0 else None
        mean_cmag_neg = cmag_neg / neg_mass if neg_mass != 0 else None
        mean_cmag_pos = cmag_pos / pos_mass if pos_mass != 0 else None
        m1_posneg = F(m1_pos, 1) / m1_neg if m1_neg != 0 else None
        g0_share = g0_mass / neg_mass if neg_mass != 0 else None
        rows.append((n, EA, ED, ratio, negfrac, posneg, mean_cmag_neg, mean_cmag_pos, by_g,
                     neg_mass, n_neg, n_edge, m1_posneg, g0_share))

        print(f"#   {n:>3} {show(EA):>10} {show(ED):>10} "
              f"{show(ratio) if ratio is not None else '-':>8} "
              f"{show(negfrac):>9} "
              f"{show(posneg) if posneg is not None else 'inf':>9} "
              f"{show(m1_posneg) if m1_posneg is not None else 'inf':>9} "
              f"{show(mean_cmag_neg) if mean_cmag_neg is not None else '-':>10} "
              f"{show(mean_cmag_pos) if mean_cmag_pos is not None else '-':>10}")

    print("#")
    print("# CONTROLS (nothing below is meaningful unless all four pass):")
    print(f"#   (1) P rebuilt == P computed directly, every n            : "
          f"{'PASS' if ctrl_pq_ok else 'FAIL'}")
    print(f"#   (2) sum of per-edge terms == P - Q exactly, every n      : "
          f"{'PASS' if ctrl_recon_ok else 'FAIL'}")
    print(f"#   (3) criterion k(2g-k)<0 == measured sign, EVERY edge     : "
          f"{'PASS' if ctrl_crit_ok else 'FAIL'}")
    print(f"#   (4) term invariant under reversal, EVERY edge            : "
          f"{'PASS' if ctrl_rev_ok else 'FAIL'}")

    if not (ctrl_pq_ok and ctrl_recon_ok and ctrl_crit_ok and ctrl_rev_ok):
        print("#\n# A CONTROL FAILED. No verdict is quoted.")
        print("RESULT: controls failed -- no verdict. qou-k5r5 OPEN.")
        return

    late = [r for r in rows if r[0] >= 12]
    pn = [r[5] for r in late if r[5] is not None]
    nf = [r[4] for r in late]
    pn_min, pn_max = min(pn), max(pn)
    nf_min, nf_max = min(nf), max(nf)
    last = late[-1]

    # Is the answer POINTWISE or AGGREGATE? The discriminator is the negative MASS share, not the
    # edge count: a thin set carrying most of the mass would not be pointwise-closeable either.
    thin = nf_max < F(1, 100) and pn_min > 1000
    pointwise = all(r[10] == 0 for r in late)

    if pointwise:
        verdict = (
            f"Q < P is POINTWISE: no edge at any n in 12..{NMAX} has g^2 < (2-2delta)^2, so the "
            f"inequality needs no aggregate argument at all -- a per-edge proof closes it.")
    elif thin:
        verdict = (
            f"Q < P is NOT pointwise but the exceptional set is THIN: negative edges are at most "
            f"{show(nf_max)} of edges over n >= 12 and the pos/neg MASS ratio stays above "
            f"{show(pn_min)}. A per-edge inequality plus a bound on that set is a viable route.")
    else:
        m1pn = [r[12] for r in late if r[12] is not None]
        m1_min, m1_max = min(m1pn), max(m1pn)
        harder = pn_max < m1_min
        cmp_word = ("WORSE than M_1's own" if harder else
                    "the same order as M_1's own" if pn_min < m1_max else "better than M_1's own")
        verdict = (
            f"Q < P is AGGREGATE, not pointwise. Over n >= 12 the negative-edge fraction is "
            f"[{show(nf_min)}, {show(nf_max)}] and the pos/neg MASS ratio is "
            f"[{show(pn_min)}, {show(pn_max)}] -- {cmp_word} census measured HERE on the SAME "
            f"edge set and the SAME window, [{show(m1_min)}, {show(m1_max)}]. So the "
            f"Cauchy-Schwarz relaxation bought a CLEANER statement (two second moments of one "
            f"measure, both reachable) and NOT an easier one: it did not convert an aggregate "
            f"problem into a local one, and by this census it is if anything the harder of the "
            f"two to close edge-wise. A proof of Q < P still needs control of the joint "
            f"distribution of (g, delta) under Plancherel.")

    print("#")
    print(f"# VERDICT (computed, not predicted): {verdict}")
    print("#")
    cn, cp = last[6], last[7]
    where = ("the BULK (small content magnitude)" if cn is not None and cp is not None and cn < cp
             else "the ENDS (large content magnitude)" if cn is not None and cp is not None
             else "undetermined")
    if cn is not None and cp is not None:
        print(f"# WHERE THE NEGATIVE MASS SITS, at n = {last[0]}: mean |u|+|v| is {show(cn)} on the "
              f"negative set")
        print(f"#   against {show(cp)} on the positive set, so it concentrates toward {where}.")
        print(f"#   By |g|: " + ", ".join(
            f"|g|={k}: {show(v / last[9] * 100, 4)}%" for k, v in sorted(last[8].items())))
    if last[13] is not None and last[13] > 0:
        print("#")
        print("# A STRUCTURAL DIFFERENCE FROM THE M_1 CENSUS, and it is why the two negative sets")
        print("#   are not nested. At g = 0 the P-Q integrand is g^2 - (2-2delta)^2 = -(2-2delta)^2,")
        print("#   which is <= 0 for EVERY such edge and < 0 whenever delta != 1 -- whereas the M_1")
        print("#   integrand g*k vanishes identically at g = 0. So the |u| = |v| edges contribute")
        print(f"#   nothing to M_1 and carry {show(last[13] * 100, 4)}% of P-Q's negative mass at "
              f"n = {last[0]}.")
        print("#   That family is exactly characterised (no inequality to solve: g = 0, delta != 1),")
        print("#   so it is the one part of this negative set a local argument can already price.")
    print("#")
    print("# ESTABLISHED REGARDLESS: the P-Q per-edge term is invariant under edge reversal")
    print("#   (control 4, every edge), exactly as the M_1 term is. So the negative set for THIS")
    print("#   decomposition is also closed under reversal, and reverse-pairing cannot cancel it.")
    print("#   Same scope note as #6651: scope-(b) for that pairing, scope-(a) for pairing at large.")
    print("#")
    print(f"# Window n <= {NMAX} against a requirement of n >= 79. Nothing here is a bound, and")
    print("#   Q < P remains SUFFICIENT, never necessary -- its failure would say nothing about M_1.")
    print(f"RESULT: {verdict} Controls (1)(2)(3)(4) all PASS. qou-k5r5 OPEN.")


if __name__ == "__main__":
    main()
