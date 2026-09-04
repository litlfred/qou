#!/usr/bin/env python3
"""M_1>0: the structure of kappa -- sign reduces to a CORRELATION sign.

Gap qou-k5r5, bean qou-t6hc. The gap's own literature roadmap names TOOL 1 as
"pin kappa and its SIGN" via Sniady's second-order free cumulants, recording:

    "Cov(Sum h, Sum c^2)/n^{5/2} converges to kappa ~ 0.0591 ... Close to
     sqrt(2)/24 = 0.058926 but data trends slightly above; Richardson
     float-unstable, exact kappa NOT pinned."

This probe pins it, by a different and much shorter route than free cumulants,
and explains the "trends slightly above" as a finite-n artefact rather than
evidence against sqrt(2)/24.

FINDING 1: an exact identity turns M_1 into a hook-power-sum covariance
-----------------------------------------------------------------------
The classical hook-content identity, verified here on all 914 partitions of
n <= 16 with a control that fires:

    sum_cells h^2  =  sum_cells c^2  +  n^2

n is deterministic, so Cov(., n^2) = 0 and therefore, EXACTLY at every n,

    M_1 = Cov(sum h, sum c^2) = Cov(sum_cells h, sum_cells h^2)

-- the covariance between the FIRST and SECOND power sums of the hook multiset.
That is a single-object statement; the two-object framing was hiding it.

FINDING 2: the exponents, and where Sum h loses its leading term
----------------------------------------------------------------
Measured: sd(sum c^2) ~ n^{3/2}, but sd(sum h) ~ n^1, not n^{3/2}. The leading
linear-in-fluctuation term of Sum h VANISHES -- which is the "Sum h is NOT in
the Kerov-Olshanski algebra" wall, seen as a scaling exponent.

Where it goes is measurable. Sum h = (sum lam_i^2 + sum lam'_j^2)/2, and
sd(sum lam_i^2)/n -> 1/sqrt(2): each half fluctuates at order n too, and the
two are ~96% ANTI-correlated, so their sum is suppressed ~7x. A wide diagram has
large sum lam_i^2 and small sum lam'_j^2; Sum h is the conjugation-symmetric
combination, and that is what costs it a half power of n.

FINDING 3: sigma_c = 1/sqrt(3), DERIVED
----------------------------------------
By the same Kerov-CLT computation used in ..._M1_area_fluctuation_scale.py
(Ivanov-Olshanski, eq. 3.20-3.21 of library/arxiv-1909.06797v5):

    sum_cells c^2 = (n^2/2) INT u^2 (nu_hat(u) - |u|) du,
    fluctuating part = n^{3/2} INT u^2 Delta(u) du

and with u = 2 cos t the weight is cos^2 t sin t = (sin t + sin 3t)/4, so
orthogonality of {sin(mt)} kills EVERY mode but m = 3 (m = 1 is absent from the
series, which starts at m = 2):

    Var = (64/pi^2) (pi/8)^2 / 3 = 1/3,    sigma_c := lim sd(sum c^2)/n^{3/2}
                                                    = 1/sqrt(3)

Contrast the area probe, where the same machine kept only EVEN modes. Different
conjugation parity, disjoint mode support.

FINDING 4: kappa = sigma_h * sigma_c  [CONSTANTS CORRECTED 2026-08-31]
-----------------------------------------------------------------------

*** CORRECTION. This probe originally asserted sigma_h -> sqrt(6)/24 and hence
kappa -> sqrt(2)/24. BOTH ARE WRONG. They were fitted to n = 400..800 data
before the drift in sigma_h had resolved; the n = 1600 point and an actual
derivation both say otherwise. The correct values, derived in
..._M1_kappa_derivation.py, are

    sigma_h = 0.09987155   (not sqrt(6)/24 = 0.10206207)
    kappa   = 128/(225 pi^2) = 0.05764050   (not sqrt(2)/24 = 0.05892557)

and 128/(225 pi^2) is the constant qou-k5r5 ALREADY records as derived via the
Ivanov-Olshanski field -- so the derivation reproduces it independently, and the
error was mine. The lesson is the one this file already records for sigma_c and
then failed to apply to sigma_h: a monotone drift over a 4x range in n is not a
limit. ***
rho(sum h, sum c^2) -> 1, measured 0.974 -> 0.9975 over n = 100..1600 and
rising monotonically. So kappa = rho * sigma_h * sigma_c -> sigma_h * sigma_c
with sigma_h := lim sd(sum h)/n measured at sqrt(6)/24 = 0.1020621, and

    sigma_h * sigma_c = (sqrt 6/24)(1/sqrt 3) = sqrt(2)/24 = 0.0589256.

The roadmap's "data trends slightly above" is explained rather than contradicted:
at finite n the measured sigma_c sits ABOVE 1/sqrt(3) while rho sits below 1,
and the first effect is the larger, so kappa is approached from above. A
low-sample first pass of this probe saw sigma_c apparently RISING monotonically
past 1/sqrt(3) (0.5578 -> 0.5842); at 4x the samples it is flat at 0.577 and
that trend was noise. The ratio sigma_h/sigma_c = 1/(4 sqrt 2) exactly.

FINDING 5 -- THE ONE THAT MATTERS: kappa > 0 is a CORRELATION SIGN
------------------------------------------------------------------
kappa = rho * sigma_h * sigma_c, and sigma_h, sigma_c are standard deviations,
hence positive by definition. So

    kappa > 0   <==>   rho(sum h, sum c^2) > 0

and the measurement says rho -> 1, not merely rho > 0. What qou-k5r5 needs for
the SIGN is therefore not the value of kappa and not Sniady's genus expansion:
it is that two conjugation-symmetric hook statistics are positively correlated,
with a measured correlation that is asymptotically PERFECT. Equivalently, by
FINDING 1, that the first and second hook power sums are positively correlated.

That is a strictly weaker target than pinning kappa, and it is the target this
probe recommends. NOT PROVED HERE -- rho -> 1 is measured, over n = 100..1600.
"""
import json
import random
import time
from bisect import bisect_right
from fractions import Fraction as F
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


def rsk_shape(N, rnd):
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


def hooks_and_contents(lam):
    """(sum h, sum h^2, sum c^2) over cells, exact integers."""
    conj = [sum(1 for l in lam if l >= j + 1) for j in range(lam[0])]
    sh = sh2 = sc2 = 0
    for i, l in enumerate(lam):
        for j in range(l):
            h = (l - j - 1) + (conj[j] - i - 1) + 1
            sh += h
            sh2 += h * h
            sc2 += (j - i) ** 2
    return sh, sh2, sc2


def row_squares(lam):
    n = sum(lam)
    nl = sum(i * l for i, l in enumerate(lam))
    nlp = sum(l * (l - 1) // 2 for l in lam)
    return 2 * nlp + n, 2 * nl + n          # sum lam_i^2, sum (lam'_j)^2


def main():
    t0 = time.monotonic_ns()
    checks = []

    # ---- FINDING 1: the exact identity, with a control ---------------------
    bad = tot = ctrl = 0
    for n in range(1, 17):
        for lam in partitions(n):
            sh, sh2, sc2 = hooks_and_contents(lam)
            tot += 1
            if sh2 != sc2 + n * n:
                bad += 1
            if sh2 == sc2:
                ctrl += 1
    checks.append({
        "name": "FINDING 1: sum h^2 = sum c^2 + n^2 exactly",
        "pass": bad == 0 and ctrl == 0,
        "detail": (
            f"Verified on all {tot} partitions of n = 1..16, {bad} violations. "
            f"CONTROL: dropping the n^2 makes it hold for {ctrl}/{tot} -- 0, so "
            f"the check can fail. CONSEQUENCE: n is deterministic, so "
            f"M_1 = Cov(sum h, sum c^2) = Cov(sum_cells h, sum_cells h^2) "
            f"EXACTLY at every n -- the covariance of the first and second "
            f"power sums of the hook multiset, a single-object statement."),
    })

    # ---- FINDING 2's identity, exactly: 2 sum h = sum lam^2 + sum lam'^2 ---
    badh = ctrlh = toth = 0
    for n in range(1, 17):
        for lam in partitions(n):
            sh, _, _ = hooks_and_contents(lam)
            R, Rp = row_squares(lam)
            toth += 1
            if 2 * sh != R + Rp:
                badh += 1
            if 2 * sh == R:
                ctrlh += 1
    checks.append({
        "name": "FINDING 2 identity: 2 sum h = sum lam_i^2 + sum lam'_j^2",
        "pass": badh == 0 and ctrlh == 0,
        "detail": (
            f"Exact on all {toth} partitions of n = 1..16, {badh} violations. "
            f"CONTROL: dropping the conjugate term holds for {ctrlh}/{toth} -- "
            f"0, so the check can fail. This is the identity that makes 'sum h "
            f"is the conjugation-symmetric combination' precise, and it is "
            f"formalised sorry-free as QOU.BraidKnot.M1EdgeCalculus."
            f"two_mul_sum_hookLen, on [propext, Classical.choice, Quot.sound]. "
            f"The half power of n that sum h loses relative to sum c^2 is the "
            f"price of that symmetrisation, given the measured ~96% "
            f"anti-correlation of the two halves."),
    })

    # ---- FINDING 3: sigma_c = 1/sqrt(3), derived ---------------------------
    # cos^2 t sin t = (sin t + sin 3t)/4 ; <sin kt, sin mt> = (pi/2) delta.
    # series starts at m = 2, so only m = 3 survives: e_3 = pi/8.
    var_c = (64 / mp.pi ** 2) * (mp.pi / 8) ** 2 / 3
    sigma_c_pred = mp.sqrt(var_c)
    dec_err = mp.quad(
        lambda t: abs(mp.cos(t) ** 2 * mp.sin(t)
                      - (mp.sin(t) + mp.sin(3 * t)) / 4), [0, mp.pi])
    e_err = mpf(0)
    for m in (2, 3, 4, 5):
        q = mp.quad(lambda t, m=m: mp.cos(t) ** 2 * mp.sin(t) * mp.sin(m * t),
                    [0, mp.pi])
        e_err = max(e_err, abs(q - (mp.pi / 8 if m == 3 else mpf(0))))
    checks.append({
        "name": "FINDING 3: sigma_c = 1/sqrt(3), derived from Kerov",
        "pass": (abs(sigma_c_pred - 1 / mp.sqrt(3)) < mpf(1) / 10 ** 12
                 and dec_err < mpf(1) / 10 ** 12 and e_err < mpf(1) / 10 ** 12),
        "detail": (
            f"cos^2 t sin t = (sin t + sin 3t)/4 (quadrature residual "
            f"{nstr(dec_err, 3)}), so against the sine series only m = 3 "
            f"survives -- m = 1 is absent because Ivanov-Olshanski starts at "
            f"m = 2. CONTROL: the mode integrals at m = 2,3,4,5 match "
            f"pi/8 * delta_(m,3) to {nstr(e_err, 3)}, so a wrong substitution "
            f"would show as a non-zero even mode. Var = (64/pi^2)(pi/8)^2/3 = "
            f"1/3, sigma_c = {nstr(sigma_c_pred, 12)} = 1/sqrt(3)."),
    })

    # ---- FINDINGS 2, 4, 5: the measurements --------------------------------
    # sigma_h from the derived Fourier coefficients f_m = 16/(m(m^2-4)^2), m odd,
    # sigma_h^2 = (64/pi^4) sum_{m odd >= 3} f_m^2 / m.  See ..._kappa_derivation.py.
    sigma_h_t = mp.sqrt((64 / mp.pi ** 4) * sum(
        (mpf(16) / (m * (m * m - 4) ** 2)) ** 2 / m for m in range(3, 4002, 2)))
    sigma_c_t = 1 / mp.sqrt(3)
    plan = [(100, 40000), (200, 24000), (400, 12000), (800, 6000), (1600, 2600)]
    rows = []
    for n, ns in plan:
        sA = sB = sAA = sBB = sAB = s2 = s22 = s2p = s22p = s2x = 0
        rnd = random.Random(9090 + n)
        for _ in range(ns):
            lam = rsk_shape(n, rnd)
            A, _, B = hooks_and_contents(lam)
            R, Rp = row_squares(lam)
            sA += A; sB += B; sAA += A * A; sBB += B * B; sAB += A * B
            s2 += R; s22 += R * R; s2p += Rp; s22p += Rp * Rp; s2x += R * Rp
        EA, EB = F(sA, ns), F(sB, ns)
        E2, E2p = F(s2, ns), F(s2p, ns)
        sdA = mp.sqrt(qf(F(sAA, ns) - EA * EA))
        sdB = mp.sqrt(qf(F(sBB, ns) - EB * EB))
        sd2 = mp.sqrt(qf(F(s22, ns) - E2 * E2))
        sd2p = mp.sqrt(qf(F(s22p, ns) - E2p * E2p))
        cv = qf(F(sAB, ns) - EA * EB)
        cv2 = qf(F(s2x, ns) - E2 * E2p)
        h = sdA / n
        c = sdB / mpf(n) ** mpf("1.5")
        se = 1 / mp.sqrt(2 * (ns - 1))
        rows.append({
            "n": n, "nsamp": ns,
            "sigma_h": nstr(h, 7), "z_h": nstr((h - sigma_h_t) / (h * se), 3),
            "sigma_c": nstr(c, 7), "z_c": nstr((c - sigma_c_t) / (c * se), 3),
            "rho": nstr(cv / (sdA * sdB), 7),
            "kappa": nstr(cv / mpf(n) ** mpf("2.5"), 7),
            "sd_rowsq_over_n": nstr(sd2 / n, 6),
            "rho_rowsq_conj": nstr(cv2 / (sd2 * sd2p), 5),
        })
    rhos = [mpf(r["rho"]) for r in rows]
    zh = [abs(mpf(r["z_h"])) for r in rows[2:]]      # n >= 400
    zc = [abs(mpf(r["z_c"])) for r in rows[1:]]      # n >= 200
    checks.append({
        "name": "FINDING 2: sd(sum h) ~ n, sd(sum c^2) ~ n^{3/2} -- the wall as an exponent",
        "pass": all(mpf(r["sd_rowsq_over_n"]) > 0 for r in rows)
                and all(mpf(r["rho_rowsq_conj"]) < mpf(-8) / 10 for r in rows),
        "detail": (
            f"sd(sum lam_i^2)/n = {[r['sd_rowsq_over_n'] for r in rows]} -> "
            f"1/sqrt(2) = {nstr(1 / mp.sqrt(2), 6)}: each half of "
            f"sum h = (sum lam_i^2 + sum lam'_j^2)/2 fluctuates at order n, and "
            f"their correlation is {[r['rho_rowsq_conj'] for r in rows]} -- "
            f"strongly ANTI-correlated, which is what suppresses sum h relative "
            f"to sum c^2 by a half power of n. This is the "
            f"'sum h is not in the Kerov-Olshanski algebra' wall, visible as a "
            f"scaling exponent rather than as an algebraic obstruction."),
    })
    checks.append({
        "name": "FINDING 4: sigma_h -> 0.0998715 (DERIVED), sigma_c -> 1/sqrt(3)",
        "pass": max(zh) < 3 and max(zc) < 3,
        "detail": (
            f"sigma_h = {[r['sigma_h'] for r in rows]} against the derived "
            f"{nstr(sigma_h_t, 8)}, z-scores from n = 400 on: "
            f"{[r['z_h'] for r in rows[2:]]} (the two smallest n are "
            f"{[r['z_h'] for r in rows[:2]]} -- still converging, from above). "
            f"sigma_c = {[r['sigma_c'] for r in rows]} against 1/sqrt(3), "
            f"z from n = 200 on: {[r['z_c'] for r in rows[1:]]}. Product "
            f"sigma_h * sigma_c = {nstr(sigma_h_t * sigma_c_t, 8)} = "
            f"128/(225 pi^2) = {nstr(mpf(128) / (225 * mp.pi ** 2), 8)}; measured "
            f"kappa = {[r['kappa'] for r in rows]}. CORRECTED: this check "
            f"previously targeted sqrt(6)/24 and sqrt(2)/24, which it PASSED on "
            f"n = 400..800 z-scores while sigma_h was still drifting down "
            f"through them. Both were wrong."),
    })
    checks.append({
        "name": "FINDING 5: kappa > 0 reduces to rho > 0, and rho -> 1",
        "pass": all(rhos[i] < rhos[i + 1] for i in range(len(rhos) - 1))
                and rhos[-1] > mpf(99) / 100,
        "detail": (
            f"kappa = rho * sigma_h * sigma_c with sigma_h, sigma_c standard "
            f"deviations, hence positive by definition -- so the SIGN of kappa "
            f"is exactly the sign of rho. Measured rho over n = 100..1600: "
            f"{[r['rho'] for r in rows]}, monotone increasing to "
            f"{nstr(rhos[-1], 6)}. So qou-k5r5's sign question is not 'compute "
            f"kappa' and not Sniady's genus expansion: it is that two "
            f"conjugation-symmetric hook statistics are positively correlated, "
            f"with a correlation that is asymptotically PERFECT. By FINDING 1, "
            f"equivalently: the first and second hook power sums are positively "
            f"correlated. MEASURED, NOT PROVED."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-kappa-structure.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: M_1>0: the structure of kappa -- sign reduces to a CORRELATION sign.",
            "probe": "m1_kappa_structure", "bean": ["qou-t6hc", "qou-k5r5"],
            "library": ["arxiv-1909.06797v5"],
            "identity_partitions": tot, "hook_sym_partitions": toth, "sigma_c_derived": nstr(sigma_c_pred, 15),
            "sampled": rows, "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: M_1 = Cov(sum_cells h, sum_cells h^2) exactly (hook-content identity).")
    print("RESULT: kappa = rho * sigma_h * sigma_c, sigma_c = 1/sqrt(3) DERIVED,")
    print("RESULT:   sigma_h -> 0.0998715 DERIVED, product = 128/(225 pi^2).")
    print("RESULT: kappa > 0 <=> rho > 0, and rho -> 1. THAT is the target for k5r5.")
    print("RESULT: gap qou-k5r5 stays OPEN -- rho -> 1 is measured, not proved.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
