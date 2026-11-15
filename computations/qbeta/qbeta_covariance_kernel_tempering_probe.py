"""Tempering Plancherel: g'(0) -> -1/4, rho -> -0.170, and a quarantined coincidence retired.

Epic `qou-x631`. Since P(lam) = (f^lam)^2/k!, the tilt family Q_t ~ (f^lam)^{2+t}
of `qou-h4fe` is exactly TEMPERING of Plancherel:

    Q_t  ~  P^{1+t/2} ,   so   Q ~ P^{3/2} .

That is the cleanest statement of what the conjecture is about: sharpening the
Plancherel measure toward its mode makes E[Sigma_3] negative.

*** RESULT 1: g'(0) sits near -1/4 at k ~ 50 ***

    k :   16       24       32       40       44       48
  g'(0): -0.2318  -0.2379  -0.2427  -0.2462  -0.2469  -0.2483

*** CORRECTED 2026-09-07 (bean `qou-igjo`). This block previously read "Monotone
from below ... so this is convergence rather than drift", and the assertion below
tested -0.25 < g'(0). BOTH ARE WRONG, and only survived because this probe's grid
stops at k = 48. ***

`qbeta_covariance_kernel_class_basis_probe` identifies g'(0) with the Plancherel
Kerov-mode projection c_3 = Cov_P(log f, Sigma_3)/sd_P(Sigma_3) -- an exact
identity, since log Q_t ~ (1+t/2)(2 log f - log k!) -- and the two code paths
agree to every printed digit at all six k above. Computed there at larger k:

  - NOT MONOTONE. On a CONSECUTIVE grid, g'(0) rises at k = 33,34,35 and again at
    k = 44. It oscillates with quasi-period ~11 in k and amplitude ~3e-4 on a
    downward drift. The grid 16,24,32,40,44,48 lands only on descending phases,
    which is what manufactured the appearance of monotonicity.
  - NOT FROM BELOW. g'(0) = -0.250311 at k = 52 and -0.250614 at k = 56: it
    passes THROUGH -1/4 near k = 50 and continues.

So the argument that made -1/4 look like the limit -- a monotone approach from
below -- is withdrawn in both halves. -1/4 IS STILL RECORDED AS A TARGET TO CHECK
A DERIVATION AGAINST, NEVER AS A CRITERION TO SEARCH ON, but the honest reading is
now weaker: the data does not separate a limit of exactly -1/4 from one slightly
below it.

*** RESULT 2: rho tightens to -0.170, and that RETIRES an earlier coincidence ***

At the same k, rho = g(1) = -0.1732, -0.1691, -0.1714, -0.1733, -0.1666, -0.1694
-- oscillating with no trend, -0.170 +/- 0.004.

`qou-ujil` recorded a coincidence: the k^{3/2} coefficient looked like
sqrt(3)/(2 pi), equivalently rho -> -1/(2 pi) = -0.15915. It was quarantined
explicitly as "a target to check a future derivation against, never a criterion
to search on". THE CHECK NOW FAILS: -0.15915 is 6.8% from -0.170, outside the
tightened bar. Treat -1/(2 pi) as disfavoured.

That is the quarantine working as designed. Had the constant been fitted to
rather than recorded, three rounds of later work would have been aimed at the
wrong number.

*** RESULT 3: the correlation COEFFICIENT decays; only the product is O(1) ***

    k          :   12      16      20      24      28      32      36      40
    sd_P(log f):  0.492   0.533   0.568   0.611   0.635   0.667   0.689   0.712
    corr       : -0.450  -0.435  -0.404  -0.389  -0.374  -0.364  -0.352  -0.346

so sd_P(log f^lam) GROWS and the true correlation coefficient between log f^lam
and Sigma_3 DECAYS, their product g'(0) = corr * sd_P(log f) staying near -1/4.

This refines the language of `qou-ujil`, which called the effect "an O(1)
correlation". That is right in units of sd(Sigma_3) and wrong as a statement
about the correlation coefficient, which is o(1). A method that assumes log f^lam
has bounded fluctuations, or that the two observables stay comparably correlated,
is assuming something false.

Floats throughout; all Plancherel weights are formed as exp(2 log f - log k!) so
nothing overflows, and every reported quantity carries three significant figures.
"""
from __future__ import annotations

import json
import math  # float64-ok: exp/log/sqrt for tempered sums formed in log space; no assertion here is an equality and all carry >=3 significant figures
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.setrecursionlimit(10000)


def partitions(n: int, cap: int | None = None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dim(lam, nfact: int) -> int:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return nfact // prod


def falling(k: int, p: int) -> int:
    r = 1
    for i in range(p):
        r *= k - i
    return r


def stats(k: int):
    nf = 1
    for i in range(2, k + 1):
        nf *= i
    b = k * (k - 1) // 2
    lg = math.lgamma(k + 1)
    den = sL = sL2 = sS = sS2 = sLS = 0.0
    d3 = n3 = 0.0
    for lam in partitions(k):
        f = hook_dim(lam, nf)
        lf = math.log(f)
        s3 = 3 * (sum((j - i) ** 2 for i, r in enumerate(lam) for j in range(r)) - b)
        w = math.exp(2 * lf - lg)
        den += w; sL += w * lf; sL2 += w * lf * lf
        sS += w * s3; sS2 += w * s3 * s3; sLS += w * lf * s3
        w3 = math.exp(3 * lf - 1.5 * lg)
        d3 += w3; n3 += w3 * s3
    mL, mS = sL / den, sS / den
    vL, vS = sL2 / den - mL * mL, sS2 / den - mS * mS
    cov = sLS / den - mL * mS
    sd3 = math.sqrt(3 * falling(k, 3))
    return {"sd_logf": math.sqrt(vL), "gp0": cov / sd3,
            "corr": cov / (math.sqrt(vL) * math.sqrt(vS)), "rho": (n3 / d3) / sd3}


def main() -> int:
    t0 = time.monotonic()
    a, ok = [], True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    ks = (16, 24, 32, 40, 44, 48)
    S = {k: stats(k) for k in ks}
    print("=" * 78)
    print("TEMPERING Plancherel:  Q_t ~ P^{1+t/2},  Q ~ P^{3/2}")
    print("=" * 78)
    print(f"    {'k':>3} | {'sd_P(log f)':>12} | {'g_prime(0)':>11} | {'corr':>9} | {'rho=g(1)':>10}")
    for k in ks:
        s = S[k]
        print(f"    {k:>3} | {s['sd_logf']:>12.5f} | {s['gp0']:>+11.4f} | "
              f"{s['corr']:>+9.4f} | {s['rho']:>+10.4f}")

    gps = [S[k]["gp0"] for k in ks]
    diffs = [gps[i + 1] - gps[i] for i in range(len(gps) - 1)]
    ok &= chk("gprime0_differences_shrink_on_THIS_grid",
              bool(abs(diffs[-1]) < abs(diffs[0]) / 3), True,
              note=f"successive differences {[round(d,5) for d in diffs]}. This is a "
                   "property OF THIS COARSE GRID and is no longer read as convergence: "
                   "`qbeta_covariance_kernel_class_basis_probe` section 6 shows g'(0) "
                   "oscillates on a consecutive grid (quasi-period ~11, amplitude ~3e-4), "
                   "so shrinking differences here reflect where 16,24,32,40,44,48 happens "
                   "to sample the oscillation")
    ok &= chk("gprime0_in_band_over_this_range_only",
              bool(all(-0.25 < g < -0.22 for g in gps) and gps[-1] < gps[0]), True,
              note="RETRACTION (bean `qou-igjo`): this was named "
                   "`gprime0_approaches_quarter_from_below` and its -0.25 < g'(0) bound was "
                   "read as evidence that -1/4 is the limit. The bound holds only because "
                   "this grid stops at k = 48. g'(0) = -0.250311 at k = 52 and -0.250614 at "
                   "k = 56 -- it CROSSES -1/4. The assertion is kept, scoped to its own "
                   "range, and must not be quoted as an approach from below")

    rhos = [S[k]["rho"] for k in ks]
    lo, hi = min(rhos), max(rhos)
    ok &= chk("rho_is_stable_near_minus_0_170",
              bool(-0.176 < lo and hi < -0.164), True,
              note=f"observed [{lo:.4f}, {hi:.4f}], oscillating with no trend")

    inv2pi = -1.0 / (2 * math.pi)
    mean_rho = sum(rhos) / len(rhos)
    ok &= chk("earlier_coincidence_minus_one_over_two_pi_is_disfavoured",
              bool(abs(mean_rho - inv2pi) > 3 * (hi - lo) / 2), True,
              note=f"rho ~ {mean_rho:.4f} against -1/(2 pi) = {inv2pi:.4f}, a 6.8% "
                   "gap outside the tightened spread. qou-ujil quarantined this "
                   "constant as 'check against, never search on'. The check fails; "
                   "treat it as disfavoured. This is the quarantine working")

    sds = [S[k]["sd_logf"] for k in ks]
    corrs = [S[k]["corr"] for k in ks]
    ok &= chk("sd_logf_grows_while_correlation_coefficient_decays",
              bool(sds[-1] > sds[0] and abs(corrs[-1]) < abs(corrs[0])), True,
              note="only the PRODUCT is O(1). qou-ujil's phrase 'an O(1) "
                   "correlation' is right in units of sd(Sigma_3) and wrong about "
                   "the correlation coefficient, which is o(1)")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-tempering.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-tempering",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "Q ~ P^{3/2}; g'(0) near -1/4 at k~50 (CROSSES it by k=52, see qou-igjo); rho ~ -0.170; "
                                "-1/(2 pi) disfavoured"},
        # NO RAW float64 REACHES THIS WITNESS (drained 2026-09-07, bean `qou-igjo`,
        # from 25 fields). AGENTS.md: "none may enter a witness", ratcheted by
        # `witness_raw_float64_audit`; this file is not in the baseline, so any
        # raw float64 here is a NEW dirty witness. These are float64-grade by
        # construction (log of an exact integer), so they are emitted as decimal
        # STRINGS at the 6 dp the computation supports, rather than as doubles or
        # padded through fmt() to a width that would read as measured.
        "_grade": "decimal strings, float64-grade, 6 dp",
        "data": {str(k): {kk: f"{vv:.6f}" for kk, vv in S[k].items()} for k in ks},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_tempering_probe.py",
                       "elapsed_s": f"{time.monotonic() - t0:.3f}"},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
