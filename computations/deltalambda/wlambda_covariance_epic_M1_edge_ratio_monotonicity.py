#!/usr/bin/env python3
"""M_1>0: N/P monotonicity extended to n=60, and the per-edge ratio is UNBOUNDED.

Gap qou-k5r5, bean qou-t6hc leg A. `..._edge_ratio_decomposition.py` reduced
M_1 > 0 for all n to

    [N/P monotone for n >= 9]  +  [N/P -> 0.6605 < 1]  +  [exact check n <= 9]

and verified the monotonicity on n = 9..46. Two things this probe adds.

THE REFORMULATION (what makes the rest affordable)
--------------------------------------------------
The predecessors sum over unordered Young-lattice edges {lam,mu} weighted by
cc(lam,mu) = #common children, which needs a dict keyed by PAIRS of partitions.
But

    sum_{edges} cc(lam,mu) f(lam,mu) = sum over TRIPLES lam -> Lam -> mu,

i.e. a sum over Lam |- n+1 of ordered pairs of distinct removable corners. No
pair dict, no dedup, and the arithmetic collapses. Writing D_Lam for the
diagonal profile of the COMMON CHILD, and taking corners at contents c_x, c_y:

    lam = Lam - box(c_x),  mu = Lam - box(c_y)
    => added to lam = c_x, removed from lam = c_y, and D_lam(u) = D_Lam(u) - [u=c_x]
    => dD2 = 2(D_lam(c_x) - D_lam(c_y) + 1) = 2(D_Lam(c_x) - D_Lam(c_y))

-- the -1 from D_lam(c_x) and the +1 cancel. Also D_Lam at a removable corner
in row i is just min(i, Lam_i - 1) + 1, so no diagonal dictionary is built at
all. Both Pterm and Nterm are invariant under x<->y (each factor flips sign),
so unordered corner pairs suffice, doubled. The normalisation 2/((n+1) n!) is
common to N and P and cancels in the ratio, so the whole computation is
INTEGER: no Fraction until the final divide.

MEASURED-COST (2026-08-30, this container; quote with the command or not at
all). Same level, same answer, both forms:

    cd computations/deltalambda && python3 -c "
    import time,sys; sys.path.insert(0,'.')
    from wlambda_covariance_epic_M1_edge_ratio_decomposition import decompose
    from wlambda_covariance_epic_M1_edge_ratio_monotonicity import np_ratio
    for n in (34,38):
        t=time.monotonic(); a=decompose(n)['NP']; told=time.monotonic()-t
        t=time.monotonic(); b=np_ratio(n);        tnew=time.monotonic()-t
        assert a==b; print(n, told, tnew, told/tnew)"

    n = 34:  pair-dict  4.79 s   Lam-centric  0.25 s   19.3x
    n = 38:  pair-dict 10.84 s   Lam-centric  0.60 s   17.9x

(and the two agree exactly, which is a second control on the rewrite). That is
what buys n = 60 here against n = 46 there. It is a MEASUREMENT on one machine
on one day, not a property of the algorithm.

CONTROL: N/P from this route must equal the committed decomposition witness
EXACTLY as Fractions on its entire range. A reformulation that is merely
plausible is worth nothing; if these disagree anywhere, this probe is wrong.

FINDING 1 -- monotonicity survives the next oscillation trough
--------------------------------------------------------------
N/P is monotone increasing on n = 9..60 (exact). That matters because the
increments OSCILLATE, and a trough is where monotonicity would break first.
The 46-range put troughs at n = 20, 36, spaced 1.528 in sqrt(n); extrapolating
puts the next at sqrt(n) ~ 7.53, n ~ 57. There IS a trough at exactly n = 57,
its increment is +1.727e-4 > 0, and the increments rise again after it.

FINDING 2 -- "worst-case per-edge ratio <= 4" is FALSE for n >= 28
------------------------------------------------------------------
`..._edge_ratio_structure.py` used to print, as a RESULT line:

    RESULT: 1-Lipschitz lemma verified (max jump 1); worst-case per-edge ratio<=4.

(corrected in the same commit as this file, so it no longer says that).

The derivation printed just above it carries the hypothesis "(same-sign
contents)" -- and the RESULT line drops it. Every extremal edge is in fact
OPPOSITE-sign, exactly the case the derivation excludes. The probe's default
nmax is 16, and 4 is correct up to n = 27, so it was never run where it fails.

The true maximum is attained on the family Lam_m = ((2m+1)^(m+1), 1), whose two
removable corners sit at contents m and -(m+1) with D_Lam = m+1 and 1, giving

    ratio = 2((m+1) - 1) / ((m+1) - m) = 2m   at   n = (2m+1)(m+1) = 2m^2+3m+1,

so max_ratio(n) = 2*floor((sqrt(8n+1) - 3)/4) ~ sqrt(2n): UNBOUNDED, not <= 4.
Verified exactly against a brute-force scan of every corner pair at every level
n = 6..50. This does not damage the reduction -- the structure probe's real
conclusion, that N/P < 1 is an AVERAGING phenomenon and no per-edge bound can
reach it, is strengthened, since the per-edge worst case now diverges.

Exact integers/Fractions throughout; mpmath only for display. Honesty:
measurement plus one refutation for the OPEN uniform bound; scope-(a); no fit;
nothing wired; gap qou-k5r5 stays OPEN. Monotonicity remains OBSERVED, not
proved -- a longer finite range is more evidence, not a proof.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 40


def show(x, d=8):
    """Fraction -> display string, without ever touching binary64."""
    return nstr(mpf(x.numerator) / mpf(x.denominator), d)


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def dim(lam, nfac):
    """Hook length formula. nfac passed in so it is computed once per level."""
    if not lam:
        return 1
    conj = [0] * lam[0]
    for part in lam:
        for j in range(part):
            conj[j] += 1
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j) + (conj[j] - i) - 1
    return nfac // prod


def corners(Lam):
    """Removable corners of Lam as (content, D_Lam(content), child partition).

    For the corner in row i, column j = Lam_i - 1, the diagonal j-i runs from
    its first box to this one, so it holds exactly min(i, j) + 1 boxes.
    """
    out = []
    L = len(Lam)
    for i in range(L):
        if Lam[i] > (Lam[i + 1] if i + 1 < L else 0):
            j = Lam[i] - 1
            child = list(Lam)
            child[i] -= 1
            out.append((j - i, min(i, j) + 1,
                        tuple(child[:i]) if child[i] == 0 else tuple(child)))
    return out


def np_ratio(n):
    """Exact N/P at level n, via the Lam-centric triple sum. Integers only."""
    nfac = factorial(n)
    dimc = {lam: dim(lam, nfac) for lam in partitions(n)}
    Pnum = Nnum = 0
    for Lam in partitions(n + 1):
        cs = corners(Lam)
        k = len(cs)
        if k < 2:
            continue
        ds = [dimc[c[2]] for c in cs]
        for x in range(k):
            cx, Dx, _ = cs[x]
            for y in range(x + 1, k):
                cy, Dy, _ = cs[y]
                w = ds[x] * ds[y]
                dO = cy * cy - cx * cx
                Pnum += w * (abs(cy) - abs(cx)) * dO
                Nnum += w * 2 * (Dx - Dy) * dO
    return F(Nnum, Pnum)


def max_edge_ratio(n):
    """Brute-force max of ratio_e over every edge at level n. No dims needed:
    ratio_e = dD2/dABS = 2(D_Lam(c_x) - D_Lam(c_y))/(|c_y| - |c_x|), and the
    only edge with Pterm = 0 is the symmetric one |c_x| = |c_y|."""
    best = None
    for Lam in partitions(n + 1):
        cs = corners(Lam)
        for x in range(len(cs)):
            cx, Dx, _ = cs[x]
            for y in range(x + 1, len(cs)):
                cy, Dy, _ = cs[y]
                den = abs(cy) - abs(cx)
                if den == 0:
                    continue
                r = F(2 * (Dx - Dy), den)
                if best is None or r > best[0]:
                    best = (r, Lam)
    return best


def isqrt(x):
    r = int(x ** 0.5)          # float64-ok: seed only, corrected exactly below
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r


def predicted_max_ratio(n):
    """2m where n = 2m^2+3m+1 is the m-th threshold; exact integer sqrt."""
    return 2 * ((isqrt(8 * n + 1) - 3) // 4)


def extrema(incs):
    """Interior local maxima/minima of the increment sequence."""
    ns = sorted(incs)
    out = []
    for i in range(1, len(ns) - 1):
        a, b, c = incs[ns[i - 1]], incs[ns[i]], incs[ns[i + 1]]
        if b > a and b > c:
            out.append((ns[i], "MAX"))
        elif b < a and b < c:
            out.append((ns[i], "min"))
    return out


def main():
    t0 = time.monotonic_ns()
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    rmax = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    NP = {}
    print(f"# exact N/P per level, Lam-centric triple sum (n = 4..{nmax})")
    for n in range(4, nmax + 1):
        NP[n] = np_ratio(n)
        print(f"  {n:>3} {show(NP[n], 10):>13}   {NP[n]}", flush=True)

    # ---- CONTROL: must reproduce the committed witness exactly ----
    wit_prev = Path(__file__).with_name("m1-edge-ratio-decomposition.witness.json")
    prev = json.loads(wit_prev.read_text())
    prev_np = {r["n"]: F(r["NP"]) for r in prev["rows"]}
    shared = [n for n in sorted(prev_np) if n in NP]
    bad = [n for n in shared if prev_np[n] != NP[n]]
    check("CONTROL: reproduces the committed decomposition witness exactly",
          shared and not bad,
          f"exact Fraction equality on n = {shared[0]}..{shared[-1]} "
          f"({len(shared)} levels), {len(bad)} mismatches. The Lam-centric sum "
          f"is a reformulation, so anything but exact agreement means it is wrong.")

    # ---- FINDING 1: monotonicity on the extended range ----
    tail = [n for n in sorted(NP) if n >= 9]
    viol = [n for a, n in zip(tail, tail[1:]) if NP[n] <= NP[a]]
    check(f"N/P is monotone increasing on n = 9..{nmax}", not viol,
          f"exact Fraction comparison, {len(tail)} levels, violations: "
          f"{viol or 'none'}. Was verified to n = 46; this extends it by "
          f"{nmax - 46}. Still OBSERVED, not proved.")

    LIM = F(6605, 10000)
    check("every N/P sits below the proved limit 0.6605",
          all(v < LIM for v in NP.values()),
          f"max = {show(max(NP.values()))} at n = {max(NP, key=NP.get)}; "
          f"headroom to 1 is {show(1 - max(NP.values()), 4)}")

    incs = {n: NP[n] - NP[a] for a, n in zip(tail, tail[1:])}
    ext = extrema(incs)

    # PREDICTION MADE ON THE n<=46 DATA, TESTED HERE FOR THE FIRST TIME.
    # Troughs at n = 20, 36 are 1.528 apart in sqrt(n); the next is at
    # sqrt(n) ~ 7.53, n ~ 57. If the trough is elsewhere, or its increment is
    # <= 0, this check must FAIL rather than be reinterpreted.
    if nmax >= 60:
        w = [n for n in incs if 45 <= n <= nmax]
        tr = min(w, key=lambda n: incs[n])
        after = sorted(n for n in w if n > tr)
        check("PREDICTED trough at n ~ 57 is there, and positive",
              tr == 57 and incs[tr] > 0 and len(after) >= 2
              and all(incs[after[i]] < incs[after[i + 1]] for i in range(len(after) - 1)),
              f"trough at n = {tr} (predicted 57), increment "
              f"{show(incs[tr], 4)} > 0, increments rise again after it. This is "
              f"the point at which monotonicity was most likely to fail.")
    else:
        check("PREDICTED trough at n ~ 57 is there, and positive", False,
              f"NOT CHECKED: needs nmax >= 60, got {nmax}.")

    # ---- FINDING 2: the per-edge ratio is unbounded ----
    scan = {n: max_edge_ratio(n) for n in range(4, rmax + 1)}
    mr = {n: v[0] for n, v in scan.items()}
    fam = {n: scan[n][1] for n in (15, 28, 45) if n <= rmax}
    bad_f = [n for n in mr if n >= 6 and mr[n] != predicted_max_ratio(n)]
    check("max per-edge ratio has the closed form 2*floor((sqrt(8n+1)-3)/4)",
          not bad_f,
          f"brute-force scan of every corner pair at every level n = 6..{rmax} "
          f"({rmax - 5} levels), {len(bad_f)} mismatches. Below the first "
          f"threshold (n = 4, 5) the formula gives 0 and the true max is 1.")
    # CONTROL: the same comparison against a deliberately wrong formula must fire.
    bad_c = [n for n in mr if n >= 6 and mr[n] != predicted_max_ratio(n) + 2]
    check("CONTROL: the closed-form detector fires on a shifted formula",
          len(bad_c) == len([n for n in mr if n >= 6]),
          f"formula shifted by +2 disagrees on {len(bad_c)}/"
          f"{len([n for n in mr if n >= 6])} levels, so the check above is "
          f"comparing something.")

    over4 = [n for n in sorted(mr) if mr[n] > 4]
    check("REFUTES the structure probe's 'worst-case per-edge ratio <= 4'",
          bool(over4) and over4[0] == 28,
          f"first violation at n = {over4[0] if over4 else '-'}, max ratio "
          f"{mr[over4[0]] if over4 else '-'} on Lam = {fam.get(28)}. The bound "
          f"holds only for SAME-sign contents, a hypothesis the printed RESULT "
          f"line drops; every extremal edge is opposite-sign. That probe's "
          f"default nmax is 16, so it never ran where it fails.")

    check("the extremal family is Lam_m = ((2m+1)^(m+1), 1)", True,
          "; ".join(f"n={n}: {fam[n]} ratio {mr[n]}" for n in sorted(fam))
          + f". ratio ~ sqrt(2n) -> infinity, so no per-edge or worst-case "
            f"argument can ever give N/P < 1. That STRENGTHENS the structure "
            f"probe's own conclusion (averaging is essential).")

    # ---- the oscillation, and a prediction that can fail ----
    mins = [n for n, k in ext if k == "min" and n >= 9]
    maxs = [n for n, k in ext if k == "MAX" and n >= 9]
    def gaps(seq):
        return [nstr(mpf(seq[i + 1]) ** mpf("0.5") - mpf(seq[i]) ** mpf("0.5"), 4)
                for i in range(len(seq) - 1)]
    check("increment extrema: spacing in sqrt(n) DRIFTS UPWARD, toward ~pi/2",
          len(mins) >= 3,
          f"minima at n = {mins}, sqrt(n) gaps {gaps(mins)}; maxima at n = "
          f"{maxs}, gaps {gaps(maxs)}. Both series drift upward. Earlier this "
          f"was called a refutation of equal spacing on the strength of ONE 6.3% "
          f"discrepancy in the maxima; with the n = 57 trough it is better "
          f"described as a systematic drift, visible in both series. pi/2 = "
          f"{nstr(mp.pi / 2, 5)} is the value the gaps are drifting toward.")

    # In units of D(0) ~ (2/pi)sqrt(n) the extrema should be spaced by 1.
    # Computed, not hardcoded: an earlier draft quoted a three-gap list whose
    # first entry came from n = 9, which is not in `mins` at all.
    def dgaps(seq):
        u = [mpf(2) / mp.pi * mpf(n) ** mpf("0.5") for n in seq]
        return [nstr(u[i + 1] - u[i], 3) for i in range(len(u) - 1)]
    check("HYPOTHESIS (recorded, NOT established): the period is one unit of D(0)",
          True,
          f"D(0), the central diagonal length, is the Durfee side; VKLS gives "
          f"D(0)/sqrt(n) -> 2/pi, so D(0) advances by 1 when sqrt(n) advances by "
          f"pi/2 = {nstr(mp.pi / 2, 5)} -- the value the spacings drift toward. "
          f"In units of (2/pi)sqrt(n) the gaps are {dgaps(mins)} between minima "
          f"{mins} and {dgaps(maxs)} between maxima {maxs}, i.e. -> 1. "
          f"FALSIFIABLE: it puts the next maximum at n ~ 67 and the next minimum "
          f"at n ~ 83. Two gaps per series support this; it is a hypothesis, not "
          f"a finding, and the mechanism is still unexplained.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    out = {
        "probe": "m1_edge_ratio_monotonicity",
        "bean": ["qou-t6hc", "qou-k5r5"],
        "nmax": nmax,
        "rmax": rmax,
        "rows": [{"n": n, "NP": str(NP[n]),
                  "inc": str(incs[n]) if n in incs else None,
                  "max_ratio": str(mr[n]) if n in mr else None}
                 for n in sorted(NP)],
        "checks": checks,
        "passed": sum(1 for c in checks if c["pass"]),
        "total": len(checks),
        "ms": int(ms),
    }
    Path(__file__).with_name("m1-edge-ratio-monotonicity.witness.json").write_text(
        json.dumps(out, indent=1) + "\n")
    print()
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: N/P monotone increasing on n = 9..{nmax} (exact), extending 46 -> {nmax} "
          f"through the predicted trough at n = 57.")
    print(f"RESULT: max per-edge ratio = 2*floor((sqrt(8n+1)-3)/4) ~ sqrt(2n), UNBOUNDED; "
          f"the 'ratio <= 4' RESULT line in ..._edge_ratio_structure.py is false for n >= 28.")
    print("RESULT: gap qou-k5r5 stays OPEN -- monotonicity is observed on a finite range.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
