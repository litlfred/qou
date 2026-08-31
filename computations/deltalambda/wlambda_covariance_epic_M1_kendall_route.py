#!/usr/bin/env python3
"""M_1>0: the pairwise route is a KENDALL statement, not a restatement of rho>0.

Gap qou-k5r5, bean qou-t6hc. Earlier probes reduced M_1 > 0 to

    discordant/concordant = [q/(1-q)] * [mean|d| ratio]  <  1

with q the probability that two iid Plancherel diagrams are DISCORDANT in
(sum h, sum c^2). This probe asks whether that is genuine progress or a
restatement of the correlation-sign question it came from.

THE TEST. For a centered bivariate normal with correlation rho, two iid draws
give a difference vector with the same correlation, and the classical quadrant
formula says exactly

    q_Gauss = 1/2 - arcsin(rho)/pi.

If the measured q tracked that, the pairwise route would be equivalent to
rho > 0 and would buy nothing -- the 138x margin would be an illusion. That was
the outcome to rule out, and it IS ruled out.

FINDING 1 (HYPOTHESIS FALSIFIED, FAVOURABLY): q is ~2.2x rarer than Gaussian
-----------------------------------------------------------------------------
Exact, n = 8..18, with rho_n computed exactly from the same enumeration:

    n = 15..18:  rho = 0.9127, 0.9146, 0.9163, 0.9184
                 q measured  = 0.0631, 0.0607, 0.0606, 0.0601
                 q Gaussian  = 0.1340, 0.1325, 0.1311, 0.1295
                 ratio       = 0.471,  0.458,  0.462,  0.464

The ratio settles at about 0.46, so discordance is roughly 2.2x rarer than a
Gaussian with the SAME correlation would give. The route therefore carries
structure beyond the Pearson correlation.

FINDING 2: what M_1 > 0 actually needs, and in which language
--------------------------------------------------------------
Since 1 - 2q is KENDALL'S TAU, "q < 1/2" is exactly tau > 0 -- a RANK statement,
invariant under monotone reparametrisation, and neither implied by nor implying
Pearson rho > 0. Measured tau = 1 - 2q = 0.880 at n = 18, against the
Gaussian-implied (2/pi) arcsin(rho) = 0.741: the rank dependence is STRONGER
than the linear dependence here.

And M_1 > 0 does not even need tau > 0 on its own. It needs

    [q/(1-q)] * [mean|d| ratio]  <  1,

and the mean ratio is separately measured at ~0.111 (stable, previous probe), so
it suffices that

    q  <  0.90        against a measured q ~ 0.060  --  a ~15x margin

on q ALONE. Two clean sufficient routes therefore exist: (q < 1/2 and mean ratio
<= 1), or (q < 0.90 and mean ratio <= 0.111).

NOT CLOSED. Both routes still require proving something about the joint law of
(sum h, sum c^2). What changed is the TARGET: a rank-based quantity with a 15x
margin, rather than the sign of a Pearson correlation with none.
"""
import json
import time
from fractions import Fraction as F
from math import factorial  # float64-ok: exact integer factorial, no float path
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 30


def qf(x):
    return mpf(x.numerator) / mpf(x.denominator)


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def dim(lam, nf):
    if not lam:
        return 1
    conj = [sum(1 for l in lam if l >= j + 1) for j in range(lam[0])]
    p = 1
    for i, l in enumerate(lam):
        for j in range(l):
            p *= (l - j - 1) + (conj[j] - i - 1) + 1
    return nf // p


def main():
    t0 = time.monotonic_ns()
    checks = []
    rows = []
    for n in range(8, 19):
        nf = factorial(n)
        P = []
        for lam in partitions(n):
            d = dim(lam, nf)
            h = sum(i + j + 1 for i, l in enumerate(lam) for j in range(l))
            c2 = sum((j - i) ** 2 for i, l in enumerate(lam) for j in range(l))
            P.append((F(d * d, nf), h, c2))
        EA = EB = EAA = EBB = EAB = F(0)
        for w, a, b in P:
            EA += w * a; EB += w * b
            EAA += w * a * a; EBB += w * b * b; EAB += w * a * b
        rho = qf(EAB - EA * EB) / (mp.sqrt(qf(EAA - EA * EA))
                                   * mp.sqrt(qf(EBB - EB * EB)))
        qm = F(0)
        for wa, fa, ga in P:
            for wb, fb, gb in P:
                if (fa - fb) * (ga - gb) < 0:
                    qm += wa * wb
        qmeas = qf(qm)
        qpred = mpf(1) / 2 - mp.asin(rho) / mp.pi
        rows.append({
            "n": n, "rho": nstr(rho, 8), "q_meas": nstr(qmeas, 6),
            "q_gauss": nstr(qpred, 6), "ratio": nstr(qmeas / qpred, 5),
            "tau": nstr(1 - 2 * qmeas, 6),
            "tau_gauss": nstr(2 * mp.asin(rho) / mp.pi, 6),
        })
    tail = rows[-4:]
    rats = [mpf(r["ratio"]) for r in tail]
    checks.append({
        "name": "FINDING 1 (HYPOTHESIS FALSIFIED, favourably): q is ~2.2x rarer than Gaussian",
        "pass": max(rats) < mpf(6) / 10 and max(rats) - min(rats) < mpf(5) / 100,
        "detail": (
            f"For a centered bivariate normal with correlation rho, two iid "
            f"draws give q_Gauss = 1/2 - arcsin(rho)/pi exactly. If measured q "
            f"tracked it, the pairwise route would merely RESTATE rho > 0 and "
            f"the 138x margin would be an illusion -- that was the outcome to "
            f"rule out. Exact over n = 15..18: rho = {[r['rho'] for r in tail]}, "
            f"q measured = {[r['q_meas'] for r in tail]}, q Gaussian = "
            f"{[r['q_gauss'] for r in tail]}, ratio = "
            f"{[r['ratio'] for r in tail]} -- settling near "
            f"{nstr(sum(rats) / len(rats), 4)}, spread "
            f"{nstr(max(rats) - min(rats), 3)}. Discordance is ~2.2x rarer than "
            f"a Gaussian with the SAME correlation, so the route carries "
            f"structure beyond the Pearson correlation."),
    })
    t18 = rows[-1]
    checks.append({
        "name": "FINDING 2: the target is Kendall's tau, with a ~15x margin on q alone",
        "pass": mpf(t18["tau"]) > mpf(t18["tau_gauss"]) and mpf(t18["q_meas"]) < mpf(9) / 10,
        "detail": (
            f"1 - 2q is KENDALL'S TAU, so 'q < 1/2' is exactly tau > 0 -- a RANK "
            f"statement, invariant under monotone reparametrisation, neither "
            f"implied by nor implying Pearson rho > 0. At n = 18: tau = "
            f"{t18['tau']} against the Gaussian-implied (2/pi) arcsin(rho) = "
            f"{t18['tau_gauss']}, so the rank dependence is STRONGER than the "
            f"linear one. And M_1 > 0 needs less than tau > 0: it needs "
            f"[q/(1-q)] * [mean ratio] < 1, and the mean ratio is separately "
            f"~0.111 (previous probe), so q < 0.90 suffices against a measured "
            f"q = {t18['q_meas']} -- a ~15x margin on q ALONE. Two sufficient "
            f"routes: (q < 1/2 and mean ratio <= 1), or (q < 0.90 and mean ratio "
            f"<= 0.111). NOT CLOSED -- both still need a statement about the "
            f"joint law; what changed is that the target is a rank quantity with "
            f"a margin, not a Pearson sign with none."),
    })
    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-kendall-route.witness.json").write_text(
        json.dumps({
            "probe": "m1_kendall_route", "bean": ["qou-t6hc", "qou-k5r5"],
            "rows": rows, "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: q is ~2.2x rarer than the Gaussian quadrant formula predicts, so")
    print("RESULT:   the pairwise route is NOT a restatement of rho > 0.")
    print("RESULT: the target is Kendall's tau > 0 -- a RANK statement -- and M_1 > 0")
    print("RESULT:   needs only q < 0.90 given the measured mean ratio, a ~15x margin.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
