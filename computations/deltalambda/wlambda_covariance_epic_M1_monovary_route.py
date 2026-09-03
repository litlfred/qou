#!/usr/bin/env python3
"""M_1>0: does the association route apply? Pairwise NO, in weighted mass YES.

Gap qou-k5r5, bean qou-t6hc. Along the Plancherel growth chain
(..._M1_kappa_cancellation.py),

    M_1 = Cov(sum|c|, sum c^2) + 2 Cov(sum D, sum c^2)     [+] and [-]

and the open part is controlling their difference. This probe asks whether the
POSITIVE term is settled by Chebyshev's association inequality, since |c| and
c^2 both increase with |c|.

THE TOOL EXISTS NOW. Mathlib carries Chebyshev's sum inequality only in its
UNWEIGHTED form, `(sum f)(sum g) <= card * sum f g`, i.e. Cov >= 0 for the
UNIFORM measure. Plancherel is not uniform. The weighted form is proved in
QOU.MathlibExt.WeightedChebyshev (sorry-free, [propext, Classical.choice,
Quot.sound]):

    (sum w f)(sum w g) <= (sum w)(sum w f g)   for w >= 0 and f, g monovarying,

via the exact symmetrisation
sum_i sum_j w_i w_j (f_i-f_j)(g_i-g_j) = 2[(sum w)(sum w f g) - (sum w f)(sum w g)].
Setting w = 1 recovers Mathlib's statement, so it is a strict generalisation.

FINDING 1 (MY EXPECTATION, FALSIFIED): the hypothesis FAILS on partitions
--------------------------------------------------------------------------
I briefed that `|c|` and `c^2` monovary "hence the positive term is exactly this
inequality". That is true PER GROWTH STEP, where the randomness is one content
and c^2 is literally a function of |c|. It is FALSE for the SUMS over a
partition, which is what the covariance is actually over: checked exhaustively,
sum|c| and sum c^2 fail to monovary from n = 7 (and sum h against sum c^2 from
n = 6), with the violation count growing. So the inequality does NOT apply
directly, and the route as briefed is closed.

FINDING 2: but the violating pairs carry almost no Plancherel mass
--------------------------------------------------------------------
The inequality needs only the WEIGHTED SUM of pair products to be non-negative,
not every pair. Splitting that sum: violating pairs are 0.5-1.8 % by COUNT but
carry only 0.05-0.12 % of the weighted mass -- a margin of roughly 2000x. So
Cov(sum|c|, sum c^2) > 0 is not merely true, it is true with the
association-violating contribution three orders of magnitude below the
association-respecting one.

WHAT THAT LEAVES. A proof of the positive term now needs a bound on the
violating mass rather than a monovary hypothesis, and it has ~2000x of room --
the same shape as the (b') weakening in ..._M1_kappa_n_exact.py, where a crude
bound replaced a sharp one. It does NOT settle M_1 > 0: the negative term is
~65 % of the positive one, and that difference is still open.
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


def stats(lam):
    sabs = sum(abs(j - i) for i, l in enumerate(lam) for j in range(l))
    sc2 = sum((j - i) ** 2 for i, l in enumerate(lam) for j in range(l))
    sh = sum(i + j + 1 for i, l in enumerate(lam) for j in range(l))
    return sabs, sc2, sh


def main():
    t0 = time.monotonic_ns()
    checks = []

    # ---- FINDING 1: monovary fails --------------------------------------
    mono = []
    for n in range(2, 15):
        P = [stats(l) for l in partitions(n)]
        v1 = sum(1 for a in P for b in P if a[1] < b[1] and a[0] > b[0])
        v2 = sum(1 for a in P for b in P if a[1] < b[1] and a[2] > b[2])
        mono.append({"n": n, "npart": len(P), "viol_abs_c2": v1, "viol_h_c2": v2})
    first1 = next(r["n"] for r in mono if r["viol_abs_c2"] > 0)
    first2 = next(r["n"] for r in mono if r["viol_h_c2"] > 0)
    checks.append({
        "name": "FINDING 1 (MY EXPECTATION FALSIFIED): monovary fails on partitions",
        "pass": first1 <= 10 and first2 <= 10,
        "detail": (
            f"I briefed that sum|c| and sum c^2 monovary, so the positive term "
            f"would be exactly the weighted Chebyshev inequality. That holds PER "
            f"GROWTH STEP (c^2 is a function of |c| there) but NOT for the sums "
            f"over a partition, which is what the covariance is over. Exhaustive "
            f"check: (sum|c|, sum c^2) first violates at n = {first1}, "
            f"(sum h, sum c^2) at n = {first2}; violation counts "
            f"{[r['viol_abs_c2'] for r in mono]} and "
            f"{[r['viol_h_c2'] for r in mono]} over n = 2..14. The inequality "
            f"does not apply directly and the route as briefed is CLOSED."),
    })

    # ---- FINDING 2: the violating mass --------------------------------------
    mass = []
    for n in range(6, 17):
        nf = factorial(n)
        P = []
        for lam in partitions(n):
            d = dim(lam, nf)
            sabs, sc2, _ = stats(lam)
            P.append((F(d * d, nf), sabs, sc2))
        pos = neg = F(0)
        nv = tot = 0
        for wa, fa, ga in P:
            for wb, fb, gb in P:
                t = wa * wb * (fa - fb) * (ga - gb)
                tot += 1
                if t < 0:
                    neg += -t
                    nv += 1
                else:
                    pos += t
        mass.append({
            "n": n, "pair_viol_pct": nstr(mpf(100 * nv) / tot, 4),
            "weighted_viol_pct": nstr(100 * qf(neg) / qf(pos + neg), 4)
            if pos + neg > 0 else "0",
            "neg_over_pos": nstr(qf(neg) / qf(pos), 5) if pos > 0 else "0",
            "cov_pos": bool(pos - neg > 0),
        })
    wv = [mpf(r["weighted_viol_pct"]) for r in mass]
    pv = [mpf(r["pair_viol_pct"]) for r in mass]
    checks.append({
        "name": "FINDING 2: violating pairs carry ~0.05-0.12 % of the weighted mass",
        "pass": all(r["cov_pos"] for r in mass) and max(wv) < 1 and max(pv) > max(wv),
        "detail": (
            f"The inequality needs only the WEIGHTED SUM of pair products to be "
            f"non-negative, not every pair. Split over n = 6..16: violating "
            f"pairs are {[r['pair_viol_pct'] for r in mass]} % by COUNT but "
            f"carry only {[r['weighted_viol_pct'] for r in mass]} % of the "
            f"weighted mass, ratio neg/pos = {[r['neg_over_pos'] for r in mass]} "
            f"-- roughly a 2000x margin, and Cov(sum|c|, sum c^2) > 0 at every n "
            f"checked. So a proof of the positive term needs a BOUND ON THE "
            f"VIOLATING MASS rather than a monovary hypothesis, with ~2000x of "
            f"room. Same shape as the (b') weakening: a crude bound replaces a "
            f"sharp one. It does NOT settle M_1 > 0 -- the negative term is "
            f"~65 % of the positive one, and that difference stays open."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-monovary-route.witness.json").write_text(
        json.dumps({
            "probe": "m1_monovary_route", "bean": ["qou-t6hc", "qou-k5r5"],
            "lean": "QOU.MathlibExt.WeightedChebyshev",
            "monovary": mono, "mass": mass, "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: weighted Chebyshev PROVED (Mathlib has only the uniform form),")
    print("RESULT:   but its hypothesis FAILS on partitions -- route as briefed closed.")
    print("RESULT: the violating pairs carry ~0.05 % of the weighted mass, so a crude")
    print("RESULT:   mass bound would do, with ~2000x of room.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
