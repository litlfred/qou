#!/usr/bin/env python3
"""M_1>0: can CONCENTRATION of A_sigma close the area input? Measured: no.

Gap qou-k5r5, bean qou-t6hc. This probe answers the literature question that
wlambda_covariance_epic_M1_area_symmetry.py ended on. That probe showed the
7.54% budget margin rests entirely on `A_sigma -> n/2`, that under plain
Plancherel `E[A_+] = (n - E[D0])/2` is an EXACT symmetry at every n, that the
symmetry does NOT transfer to the omega-weighted edge measure, and closed with:

    "the remaining input is CONCENTRATION of one smooth functional of a
     Plancherel diagram about a mean fixed by an exact symmetry -- a much
     narrower literature question, and the one to ask."

It has now been asked. The tool class is Pemantle-Peres, Concentration of
Lipschitz functionals of determinantal and other strong Rayleigh measures,
Combin. Probab. Comput. 23:1 (2014) 140-160 -- ingested as
library/arxiv-1108.0687v3. It is the right class: the Plancherel Maya
configuration {lam_i - i} is determinantal (discrete Bessel kernel), and
determinantal implies strong Rayleigh (Borcea-Branden-Liggett, ingested as
library/arxiv-0707.2340v2 = the JAMS version S0894-0347-08-00618-8).

THE ANSWER IS NO, for a reason that is not a defect of the tool.

FINDING 1: the margin is EXACTLY ONE STANDARD DEVIATION
-------------------------------------------------------
Both sides of the question are (1/pi) sqrt(n):

    n/2 - E[A_+]  =  E[D0]/2  ->  (1/pi) sqrt(n)     [exact symmetry + VKLS]
    sd(A_+)                   ->  (1/pi) sqrt(n)     [measured, AND derived
                                                      from Kerov -- FINDING 4]

so gap/sd -> 1. Measured flat at 1.00 across n = 100..3200 -- a 32x range. A
concentration inequality that has to cover one sigma cannot conclude anything:
a 1-sigma event has probability ~0.16, not o(1). The question sits exactly at
the edge of the Gaussian window, and no amount of sharpening the inequality
moves it, because the obstruction is the WIDTH OF THE DISTRIBUTION, not the
quality of the bound.

FINDING 2: it is asymptotic, not an identity
--------------------------------------------
gap/sd is NOT exact at finite n. Over n = 2..18 by exact rational enumeration it
oscillates 0.866 -> 1.084 -> 0.963 -> 1.029, crossing 1 four times. So there is
no finite-n identity to prove; the coincidence is a limit statement, and both
constants are the same VKLS/Kerov 1/pi.

FINDING 3: the off-the-shelf bound is off by n^(1/4), computed
--------------------------------------------------------------
Even granting everything, Pemantle-Peres Theorem 3.5 (determinantal, EN = mu):

    P(f - Ef >= a) <= 3 exp( -a^2 / (16 (a + 2 mu)) )     f Lipschitz-1

and A_+ is NOT Lipschitz-1 in the total-variation metric their Lipschitz
condition uses. Moving one particle from site 1 to the edge of the support
changes A_+ by that site's coordinate, so its Lipschitz constant is the maximum
content, c ~ 2 sqrt(n) (VKLS: lambda_1/sqrt(n) -> 2). Rescaling f -> f/c, the
bound is non-trivial only once a >= c sqrt(32 mu), with mu = E[D0] ~ (2/pi)
sqrt(n) particles on the positive side. That threshold is ~9 n^(3/4), against an
available gap of (1/pi) sqrt(n): short by a factor ~28 n^(1/4), tabulated below.

Note WHICH way this cuts. Pemantle-Peres is not weak here -- D(c) itself, the
per-diagonal profile the telescoping route uses, IS Lipschitz-1 in that metric
(it is a particle count), so the same theorem gives it concentration at scale
n^(1/4). The failure is specific to A_+, which is a linear statistic with
UNBOUNDED coefficients: A_+ = sum over occupied positive sites x of x.

FINDING 4: the physics side derives the constant, and it is Kerov
-----------------------------------------------------------------
The 1/pi is not a numerical coincidence. Kerov's CLT for Plancherel
fluctuations -- Ivanov-Olshanski, quoted as eq. (3.20)-(3.21) of
library/arxiv-1909.06797v5 (Quantum Mechanics of Plancherel Growth) -- says the
rescaled profile is

    nu_hat(u) ~ Omega(u) + (2/sqrt n) Delta(u),
    Delta(2 cos t) = (1/pi) sum_{m>=2} (alpha_m / sqrt m) sin(m t)

with alpha_m iid standard Gaussians. Since the number of cells on diagonal c is
d(c) = (L(c) - |c|)/2, the signed area is a linear statistic of the profile:

    A_+ - A_-  =  (n/2) INT sgn(u) (nu_hat(u) - |u|) du  =  sqrt(n) * I

and Omega is even, so only the fluctuation survives. Substituting u = 2 cos t,

    I = (2/pi) sum_m (alpha_m / sqrt m) c_m,
    c_m = INT_0^pi sgn(cos t) sin(m t) sin t dt = 0 (m odd),
                                               = -2 (-1)^(m/2) m/(m^2-1) (m even)

whence Var(I) = (16/pi^2) sum_{m even} m/(m^2-1)^2 = (16/pi^2)(1/4) = 4/pi^2:

    sd(A_+ - A_-) -> (2/pi) sqrt(n),   so   sd(A_+) -> (1/pi) sqrt(n)

(D0 contributes at lower order -- it IS Lipschitz-1, so by FINDING 3's own
theorem it concentrates at scale n^(1/4) = o(sqrt n)). Checked below against the
measurement and with a quadrature control on c_m.

So gap/sd -> 1 is a coincidence between two DIFFERENT constants that are both
2/pi: the gap is the Durfee constant E[D0]/sqrt(n) -> 2/pi, the width is the
Kerov constant sd(A_+ - A_-)/sqrt(n) -> 2/pi. Nothing in the derivation
suggests the equality is forced, and at finite n it fails (FINDING 2) -- but it
is exact in the limit, which is where the budget is tightest.

WHAT THIS CHANGES. `A_sigma -> n/2` is not reachable by concentration and should
stop being described as a literature question. Two routes survive: (i) the
favourable direction -- E_omega[A_sigma]/(n/2) converges to 1 FROM BELOW
(measured 0.30 -> 0.96 over n = 6..400 in the area-symmetry probe), and a
smaller A gives a TIGHTER bound sqrt(a^2 + 2A) - a, so the 7.54% is conservative
at every finite n; making that rigorous needs a one-sided finite-n inequality,
not concentration; or (ii) an exact computation of the constant, since the
question is a comparison of two quantities that agree to leading order and
differ in the subleading term.
"""
import json
import random
import time
from bisect import bisect_right
from fractions import Fraction as F
from math import factorial  # float64-ok: exact integer factorial, no float path
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 30


def qf(x):
    """Fraction -> mpf without touching binary64."""
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
    """Hook length formula."""
    if not lam:
        return 1
    conj = [sum(1 for l in lam if l >= j + 1) for j in range(lam[0])]
    p = 1
    for i, l in enumerate(lam):
        for j in range(l):
            p *= (l - j - 1) + (conj[j] - i - 1) + 1
    return nf // p


def rsk_shape(N, rnd):
    """Shape of the RSK insertion tableau of a uniform permutation of [N] --
    exactly Plancherel(N)-distributed. Uniform integer choices only."""
    perm = list(range(N))
    for i in range(N - 1, 0, -1):
        j = rnd.randrange(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    rows = []
    for x in perm:
        for row in rows:
            k = bisect_right(row, x)
            if k == len(row):
                row.append(x)
                x = None
                break
            row[k], x = x, row[k]
        if x is not None:
            rows.append([x])
    return tuple(len(r) for r in rows)


def split(lam):
    """(A_+, A_-, D0): cells of content > 0, < 0, and = 0."""
    ap = sum(max(0, l - (i + 1)) for i, l in enumerate(lam))
    d0 = sum(1 for i, l in enumerate(lam) if l >= i + 1)
    return ap, sum(lam) - ap - d0, d0


def exact_moments(n):
    """E[A_+], Var(A_+), E[D0] as exact rationals under Plancherel(n)."""
    nf = factorial(n)
    ea = ea2 = ed = tot = F(0)
    for lam in partitions(n):
        d = dim(lam, nf)
        w = F(d * d, nf)
        ap, _, d0 = split(lam)
        ea += w * ap
        ea2 += w * ap * ap
        ed += w * d0
        tot += w
    assert tot == 1, tot
    return ea, ea2 - ea * ea, ed


def sampled_moments(n, nsamp, seed):
    rnd = random.Random(seed)
    s = s2 = sd0 = 0
    for _ in range(nsamp):
        lam = rsk_shape(n, rnd)
        ap, _, d0 = split(lam)
        s += ap
        s2 += ap * ap
        sd0 += d0
    ea = F(s, nsamp)
    return ea, F(s2, nsamp) - ea * ea, F(sd0, nsamp)


def pp_threshold(n):
    """Pemantle-Peres Thm 3.5 deviation threshold for A_+, vs the gap.

    f Lipschitz-1: P(f-Ef>=a) <= 3 exp(-a^2/(16(a+2mu))). A_+ has TV-Lipschitz
    constant c = max content ~ 2 sqrt(n); rescaling f->f/c makes the bound
    non-trivial only for a >= c sqrt(32 mu), mu = E[D0] ~ (2/pi) sqrt(n)."""
    rn = mp.sqrt(mpf(n))
    c = 2 * rn                       # VKLS: lambda_1 / sqrt(n) -> 2
    mu = (2 / mp.pi) * rn            # VKLS: D(0) / sqrt(n) -> 2/pi
    return c * mp.sqrt(32 * mu), rn / mp.pi


def main():
    t0 = time.monotonic_ns()
    checks = []

    # ---- exact: is gap/sd an identity? -------------------------------------
    exact_rows = []
    for n in range(2, 19):
        ea, var, ed = exact_moments(n)
        sd = mp.sqrt(qf(var))
        gap = qf(ed) / 2
        exact_rows.append({
            "n": n, "E_Ap": str(ea), "E_D0": str(ed),
            "sd": nstr(sd, 8), "gap": nstr(gap, 8),
            "ratio": nstr(gap / sd, 6) if sd > 0 else None,
            "is_identity": bool(var * 4 == ed * ed),
        })
    ident = [r["n"] for r in exact_rows if r["is_identity"]]
    ratios = [mpf(r["ratio"]) for r in exact_rows if r["ratio"] is not None]
    crossings = sum(1 for i in range(len(ratios) - 1)
                    if (ratios[i] - 1) * (ratios[i + 1] - 1) < 0)
    checks.append({
        "name": "gap/sd is NOT a finite-n identity",
        "pass": ident == [2] and crossings >= 3,
        "detail": (
            f"Var(A_+) = (E[D0]/2)^2 as exact rationals only at n = {ident} "
            f"(n = 2 has a single partition pair and is degenerate). Over "
            f"n = 2..18 the ratio runs "
            f"{[nstr(r, 4) for r in ratios[:4]]} ... {[nstr(r, 4) for r in ratios[-4:]]}, "
            f"crossing 1 {crossings} times. So there is no identity to prove: "
            f"the coincidence in FINDING 1 is asymptotic, and both constants "
            f"are 1/pi."),
    })

    # ---- control: the anchor the whole comparison rests on ------------------
    bad = [r["n"] for r in exact_rows
           if F(r["E_Ap"]) != (F(r["n"]) - F(r["E_D0"])) / 2]
    checks.append({
        "name": "CONTROL: E[A_+] = (n - E[D0])/2 exactly",
        "pass": not bad,
        "detail": (
            f"Exact rational equality at every n = 2..18 (violations: {bad}). "
            f"This is the conjugation symmetry, and it is what fixes the gap "
            f"n/2 - E[A_+] = E[D0]/2 that FINDING 1 compares sd(A_+) against. "
            f"Formalised sorry-free as QOU.BraidKnot.M1EdgeCalculus."
            f"areaUpper_transpose together with "
            f"areaUpper_add_areaLower_add_diagLen_zero. Re-checked here because "
            f"an error in it would silently move the target, and the c = 0 "
            f"diagonal has caused three separate bookkeeping errors in this "
            f"cluster."),
    })

    # ---- sampled: the two constants ---------------------------------------
    plan = [(100, 4000), (200, 3000), (400, 2400), (800, 1800),
            (1600, 1200), (3200, 800)]
    seeds = (101, 202, 303)
    samp_rows = []
    for n, ns in plan:
        per = [sampled_moments(n, ns, s) for s in seeds]
        sds = [mp.sqrt(qf(v)) for _, v, _ in per]
        gaps = [qf(d) / 2 for _, _, d in per]
        rn = mp.sqrt(mpf(n))
        rat = [g / s for g, s in zip(gaps, sds)]
        sdm = sum(sds) / len(sds) / rn
        # se of a sample sd is s/sqrt(2(ns-1)); 3 independent seeds -> /sqrt(3)
        se = sdm / mp.sqrt(2 * (ns - 1) * len(seeds))
        samp_rows.append({
            "n": n, "nsamp": ns, "seeds": list(seeds),
            "sd_over_sqrtn": [nstr(s / rn, 6) for s in sds],
            "sd_mean": nstr(sdm, 6), "sd_se": nstr(se, 3),
            "sd_zscore": nstr((sdm - 1 / mp.pi) / se, 4),
            "gap_over_sqrtn": [nstr(g / rn, 6) for g in gaps],
            "ratio": [nstr(r, 6) for r in rat],
            "ratio_mean": nstr(sum(rat) / len(rat), 6),
            "ratio_spread": nstr(max(rat) - min(rat), 4),
        })
    inv_pi = 1 / mp.pi
    sd_all = [mpf(v) for r in samp_rows for v in r["sd_over_sqrtn"]]
    gp_all = [mpf(v) for r in samp_rows for v in r["gap_over_sqrtn"]]
    rat_all = [mpf(r["ratio_mean"]) for r in samp_rows]
    worst_sd = max(abs(v - inv_pi) for v in sd_all)
    zs = [abs(mpf(r["sd_zscore"])) for r in samp_rows]
    worst_gp = max(abs(v - inv_pi) for v in gp_all)
    worst_rat = max(abs(r - 1) for r in rat_all)
    spread = max(mpf(r["ratio_spread"]) for r in samp_rows)
    checks.append({
        "name": "sd(A_+)/sqrt(n) -> 1/pi, against the propagated error",
        "pass": max(zs) < 3,
        "detail": (
            f"Seed-pooled sd(A_+)/sqrt(n) over n = 100..3200: "
            f"{[r['sd_mean'] for r in samp_rows]} against 1/pi = "
            f"{nstr(inv_pi, 6)}; standard errors {[r['sd_se'] for r in samp_rows]} "
            f"(se of a sample sd is s/sqrt(2(ns-1)), pooled over "
            f"{len(seeds)} seeds), giving z-scores "
            f"{[r['sd_zscore'] for r in samp_rows]}, all under 3. Largest raw "
            f"departure is {nstr(worst_sd, 3)}, which is WITHIN the error bar "
            f"and not evidence of a trend -- the earlier version of this check "
            f"used a hardcoded 0.03 tolerance and tripped on exactly that "
            f"noise. Flat in n, so the fluctuation exponent is 1/2, not 1/4."),
    })
    checks.append({
        "name": "E[D0]/(2 sqrt(n)) -> 1/pi, measured",
        "pass": worst_gp < mpf(2) / 100,
        "detail": (
            f"The gap, independently accumulated: "
            f"{[r['gap_over_sqrtn'][0] for r in samp_rows]}; worst deviation "
            f"from 1/pi is {nstr(worst_gp, 3)}. This one is the known VKLS "
            f"constant D(0)/sqrt(n) -> 2/pi, so it is a check on the sampler "
            f"as much as on the claim."),
    })
    checks.append({
        "name": "FINDING 1: gap/sd = 1 -- the margin is exactly one sigma",
        "pass": worst_rat < mpf(8) / 100,
        "detail": (
            f"Seed-mean ratio over n = 100..3200 (a 32x range): "
            f"{[r['ratio_mean'] for r in samp_rows]}; worst departure from 1 is "
            f"{nstr(worst_rat, 3)}, largest seed spread at fixed n is "
            f"{nstr(spread, 3)} -- so the departures are within sampling noise "
            f"and there is no trend. THE CONSEQUENCE: a concentration "
            f"inequality asked to rule out A_+ >= n/2 must cover one standard "
            f"deviation, and a 1-sigma event has probability ~0.16. No "
            f"sharpening of the inequality helps, because the obstruction is "
            f"the width of the distribution."),
    })

    # ---- the off-the-shelf arithmetic --------------------------------------
    pp_rows = []
    for n in (100, 10 ** 4, 10 ** 6, 10 ** 8):
        thr, gap = pp_threshold(n)
        pp_rows.append({"n": n, "pp_threshold": nstr(thr, 6),
                        "gap": nstr(gap, 6), "shortfall": nstr(thr / gap, 5)})
    shortfalls = [mpf(r["shortfall"]) for r in pp_rows]
    growing = all(shortfalls[i] < shortfalls[i + 1]
                  for i in range(len(shortfalls) - 1))
    checks.append({
        "name": "FINDING 3: Pemantle-Peres is short by a growing n^(1/4)",
        "pass": growing and shortfalls[0] > 1,
        "detail": (
            f"Thm 3.5 needs a >= c sqrt(32 mu) with c ~ 2 sqrt(n) the "
            f"TV-Lipschitz constant of A_+ and mu ~ (2/pi) sqrt(n); the gap is "
            f"(1/pi) sqrt(n). Shortfall thr/gap at n = "
            f"{[r['n'] for r in pp_rows]}: "
            f"{[r['shortfall'] for r in pp_rows]} -- growing like n^(1/4), "
            f"never below {nstr(min(shortfalls), 4)}. NOT a weakness of the "
            f"theorem: D(c) IS Lipschitz-1 in that metric (a particle count), "
            f"so the same theorem concentrates the per-diagonal profile at "
            f"scale n^(1/4). A_+ fails it because it is a linear statistic "
            f"with unbounded coefficients."),
    })

    # ---- FINDING 4: derive 1/pi from Kerov's CLT ---------------------------
    S = F(0)
    for m in range(2, 100001, 2):
        S += F(m, (m * m - 1) ** 2)
    var_I = (16 / mp.pi ** 2) * qf(S)
    sd_pred = mp.sqrt(var_I) / 2          # sd(A_+)/sqrt(n) = sd(A_+-A_-)/2
    quad_err = mpf(0)
    for m in (2, 3, 4, 5, 6, 7):
        q = mp.quad(lambda t, m=m: mp.sign(mp.cos(t)) * mp.sin(m * t) * mp.sin(t),
                    [0, mp.pi / 2, mp.pi])
        cf = (mpf(0) if m % 2
              else -2 * mpf((-1) ** (m // 2)) * mpf(m) / (m * m - 1))
        quad_err = max(quad_err, abs(q - cf))
    sd_meas = mpf(samp_rows[-2]["sd_mean"])   # n = 1600
    kerov = {
        "S": nstr(qf(S), 14), "S_exact_target": "1/4",
        "var_I": nstr(var_I, 12), "sd_pred_over_sqrtn": nstr(sd_pred, 12),
        "inv_pi": nstr(inv_pi, 12), "quad_control_max_err": nstr(quad_err, 4),
        "sd_measured_n1600": nstr(sd_meas, 8),
    }
    checks.append({
        "name": "FINDING 4: Kerov's CLT DERIVES sd(A_+) -> (1/pi) sqrt(n)",
        "pass": (abs(sd_pred - inv_pi) < mpf(1) / 10 ** 9
                 and quad_err < mpf(1) / 10 ** 20
                 and abs(qf(S) - mpf(1) / 4) < mpf(1) / 10 ** 9),
        "detail": (
            f"From Delta(2 cos t) = (1/pi) sum alpha_m sin(m t)/sqrt(m): "
            f"Var(I) = (16/pi^2) S with S = sum_(m even) m/(m^2-1)^2 = "
            f"{kerov['S']} (= 1/4), so sd(A_+)/sqrt(n) -> "
            f"{kerov['sd_pred_over_sqrtn']} against 1/pi = {kerov['inv_pi']}. "
            f"Measured at n = 1600: {kerov['sd_measured_n1600']}. CONTROL: the "
            f"closed form for c_m checked against direct quadrature at "
            f"m = 2..7, max error {kerov['quad_control_max_err']} -- the odd m "
            f"vanish as the parity argument requires, which is what would break "
            f"first if the substitution u = 2 cos t were wrong. This makes the "
            f"1-sigma margin a DERIVED coincidence between two constants that "
            f"are both 2/pi, not a numerical accident."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-area-fluctuation-scale.witness.json").write_text(
        json.dumps({
            "probe": "m1_area_fluctuation_scale",
            "bean": ["qou-t6hc", "qou-k5r5"],
            "library": ["arxiv-1108.0687v3", "arxiv-0707.2340v2"],
            "exact": exact_rows, "sampled": samp_rows, "pemantle_peres": pp_rows,
            "kerov": kerov,
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")

    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: n/2 - E[A_+] and sd(A_+) are BOTH (1/pi) sqrt(n) -- the margin")
    print("RESULT:   is exactly one standard deviation. Concentration cannot close it.")
    print("RESULT: both constants are 2/pi -- the Durfee one and the Kerov one --")
    print("RESULT:   so the coincidence is derived, not numerical.")
    print("RESULT: 'A_sigma -> n/2' should stop being called a literature question.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
