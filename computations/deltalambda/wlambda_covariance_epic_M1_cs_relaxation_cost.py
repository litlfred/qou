#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): how much does the Cauchy-Schwarz relaxation COST? The (CS) margin route is a
relaxation of the corpus's sharper Fulman reduction, and nobody has measured the gap between them.

WHY THIS, NOW -- and it audits my own route choice rather than extending it. Two routes to M_1 > 0
coexist in this corpus and their relationship has never been quantified:

  FULMAN (2026-08-21, docs/audits/2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
    Split identity  Sum h = Sum_u D(u)^2 + Sum|c|,  i.e.  Sum h = D + A.
    With omega_3 = Sum c^2 - C(n,2) = W an exact eigenfunction of the up-down chain,
        M_1 = Cov(Sum h, W) = P - N,   P := Cov(A, W) >= 0,   N := -Cov(D, W) >= 0,
    both signs manifest EDGE BY EDGE. So M_1 > 0 is EXACTLY P > N. Necessary and sufficient.

  (CS) MARGIN (the route PRs #6500/#6528/#6576/#6602 have been sharpening)
    m = rho_P - sqrt(V_D/V_A) > 0,  rho_P = P/sqrt(V_A V_W).
    Multiply through by sqrt(V_A V_W): this is exactly  P > sqrt(V_D V_W).
    And Cauchy-Schwarz gives N = |Cov(D,W)| <= sqrt(V_D V_W). So the margin is the CS RELAXATION
    of P > N -- SUFFICIENT but not necessary, and it discards N's per-edge sign structure entirely.

THE COST IS ONE NUMBER, and it is measurable exactly:

    rho_D := N / sqrt(V_D V_W) = |Cov(D,W)| / sqrt(V_D V_W)  in [0, 1]

is precisely how tight CS is on this pair. rho_D -> 1 means CS is nearly free and the margin route
loses almost nothing; rho_D well below 1 means the margin route is throwing away a factor and effort
belongs on P > N instead. Reported alongside the directly comparable quantity

    surviving fraction = (P - sqrt(V_D V_W)) / (P - N) = (CS-relaxed margin) / (true margin M_1),

which says what fraction of the true positive margin the relaxation still certifies.

SELF-CHECK, and it validates the corpus's split identity rather than assuming it. Sum h is computed
independently (an explicit per-cell hook sum, not via D + A), and the probe asserts BOTH
    Sum h == D + A            at every partition, and
    Cov(Sum h, W) == P - N    at every n.
If either fails, the reduction this probe is pricing does not hold as stated and no number here
means anything -- so both are checked before any cost is reported.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 40


def _load_cl():
    """Import partitions()/fact() by explicit file path (not a bare name: the _path_bridge bootstrap
    trap -- this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_constant_C_landscape.py"
    spec = importlib.util.spec_from_file_location("_m1_cl", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def full_stats(lam, n, nfact):
    """(f^lambda, A, D, W, H) for one partition, all exact integers.

    A = Sum|c|;  D = Sum_u d_u^2;  W = Sum c^2 - C(n,2);  H = Sum_cells hook, computed
    INDEPENDENTLY per cell so that the split identity H == D + A is a test, not an assumption.
    """
    m = lam[0] if lam else 0
    conj = [0] * m
    for part in lam:
        for j in range(part):
            conj[j] += 1
    prod = 1
    absc = 0
    c2 = 0
    hooks = 0
    diag = {}
    for i, part in enumerate(lam):
        for j in range(part):
            h = (part - j - 1) + (conj[j] - i - 1) + 1
            prod *= h
            hooks += h
            u = j - i
            absc += abs(u)
            c2 += u * u
            diag[u] = diag.get(u, 0) + 1
    f = nfact // prod
    D = sum(v * v for v in diag.values())
    return f, absc, D, c2 - (n * (n - 1)) // 2, hooks


def main():
    mod = _load_cl()
    nmax = 40
    print(f"# cost of the Cauchy-Schwarz relaxation; dps={mp.mp.dps}; exact Fractions; NO float64")
    print("# Fulman:  M_1 = P - N,  P = Cov(A,W) >= 0,  N = -Cov(D,W) >= 0   (per-edge manifest)")
    print("# (CS)   :  the margin m > 0 is exactly  P > sqrt(V_D V_W) >= P > N   -- a RELAXATION")
    print("#")
    print(f"#   {'n':>3} {'P':>13} {'N':>13} {'M_1=P-N':>13} {'sqrt(VD*VW)':>13} "
          f"{'rho_D':>8} {'survives':>9}")

    rows = []
    split_ok = True
    reduction_ok = True
    for n in range(4, nmax + 1):
        nfact = mod.fact(n)
        ac = {k: F(0) for k in ("A", "D", "W", "H", "DD", "WW", "AW", "DW", "HW")}
        for lam in mod.partitions(n):
            f, A, D, W, H = full_stats(lam, n, nfact)
            if H != D + A:                       # the corpus's split identity, TESTED
                split_ok = False
            w = F(f * f, nfact)
            ac["A"] += w * A; ac["D"] += w * D; ac["W"] += w * W; ac["H"] += w * H
            ac["DD"] += w * D * D; ac["WW"] += w * W * W
            ac["AW"] += w * A * W; ac["DW"] += w * D * W; ac["HW"] += w * H * W
        P = ac["AW"] - ac["A"] * ac["W"]
        covDW = ac["DW"] - ac["D"] * ac["W"]
        N = -covDW
        M1 = ac["HW"] - ac["H"] * ac["W"]
        if M1 != P - N:                          # the Fulman reduction itself, TESTED
            reduction_ok = False
        VD = ac["DD"] - ac["D"] ** 2
        VW = ac["WW"] - ac["W"] ** 2
        r = lambda x: mp.mpf(x.numerator) / x.denominator
        cs = mp.sqrt(r(VD) * r(VW))
        rho_D = r(N) / cs if cs != 0 else mp.mpf('nan')
        relaxed = r(P) - cs
        survives = relaxed / r(M1) if M1 != 0 else mp.mpf('nan')
        rows.append((n, r(P), r(N), r(M1), cs, rho_D, survives))
        if n <= 8 or n % 4 == 0:
            print(f"#   {n:>3} {mp.nstr(r(P),6):>13} {mp.nstr(r(N),6):>13} {mp.nstr(r(M1),6):>13} "
                  f"{mp.nstr(cs,6):>13} {mp.nstr(rho_D,4):>8} {mp.nstr(survives,4):>9}")
    print("#")

    print("# SELF-CHECKS (both must pass or nothing below is meaningful):")
    print(f"#   split identity  Sum h == D + A  at every partition : {'PASS' if split_ok else 'FAIL'}")
    print(f"#   Fulman reduction  Cov(Sum h,W) == P - N  at every n : "
          f"{'PASS' if reduction_ok else 'FAIL'}")
    if not (split_ok and reduction_ok):
        print("RESULT: SELF-CHECK FAILED -- the reduction being priced does not hold as stated; no "
              "cost figure from this probe may be quoted. qou-k5r5 OPEN.")
        print("EXIT: 0")
        return 0
    print("#   Both pass, so the corpus's split identity and Fulman reduction are confirmed here")
    print("#   independently (Sum h computed per-cell, never as D + A).")
    print("#")

    tail = [x for x in rows if x[0] >= 16]
    rd = [x[5] for x in tail]
    sv = [x[6] for x in tail]
    print(f"# rho_D = N / sqrt(V_D V_W) over n >= 16 : min {mp.nstr(min(rd),5)}  "
          f"max {mp.nstr(max(rd),5)}")
    print(f"#   This IS the tightness of Cauchy-Schwarz on the (D, W) pair. 1 = CS free.")
    print(f"# surviving fraction (P - sqrt(V_D V_W))/(P - N) over n >= 16 : "
          f"min {mp.nstr(min(sv),5)}  max {mp.nstr(max(sv),5)}")
    print("#   = the share of the TRUE margin that the CS relaxation still certifies.")
    print("#")

    lo = min(sv)
    cost = 1 / lo if lo > 0 else mp.inf
    if lo <= 0:
        verdict = ("the CS relaxation goes NEGATIVE somewhere in n >= 16 -- it fails to certify "
                   "M_1 > 0 at those n even though M_1 > 0 there, so the margin route CANNOT close "
                   "the gap by itself and P > N is the only sufficient form")
    elif lo > mp.mpf('0.5'):
        verdict = (f"the CS relaxation is CHEAP: it keeps at least {mp.nstr(lo*100,4)}% of the true "
                   f"margin over n >= 16 (rho_D in [{mp.nstr(min(rd),4)}, {mp.nstr(max(rd),4)}]), so "
                   f"the (CS) margin route loses little and sharpening delta_A is well spent")
    else:
        verdict = (f"the CS relaxation is EXPENSIVE: it keeps only {mp.nstr(lo*100,4)}% of the true "
                   f"margin at worst over n >= 16 (a {mp.nstr(cost,4)}x loss; rho_D in "
                   f"[{mp.nstr(min(rd),4)}, {mp.nstr(max(rd),4)}]), so effort on the margin route is "
                   f"paying a large avoidable premium and P > N deserves the attention instead")
    print(f"# VERDICT (computed, not predicted): {verdict}.")
    print("#")
    print("# WHAT THIS DOES NOT DO. It prices the relaxation; it does not close either route. Both")
    print("#   still need a rigorous finite-n argument -- delta_A for the margin, P > N for Fulman.")
    print(f"#   Window n <= {nmax}; the requirement is n >= 79. Nothing here is a bound.")
    print(f"RESULT: {verdict}. rho_D over n>=16 in [{mp.nstr(min(rd),5)}, {mp.nstr(max(rd),5)}]; "
          f"surviving fraction in [{mp.nstr(lo,5)}, {mp.nstr(max(sv),5)}]. Split identity and Fulman "
          f"reduction both re-verified exactly. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
