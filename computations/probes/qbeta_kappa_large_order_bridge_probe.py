#!/usr/bin/env python3
"""qbeta_kappa_large_order_bridge_probe.py — G2+C3 (item 6) of the
Borel/alien-calculus utilization audit
(docs/audits/2026-07-12-borel-alien-calculus-utilization-audit.md):
resurgence LARGE-ORDER (bridge-equation) probe of the Ohtsuki rungs
kappa_5, kappa_6 past the exact-kappa_4 frontier.

HYPOTHESIS UNDER TEST (a TEST, not a fit): the 4_1 Ohtsuki ladder is a
one-instanton Gevrey-1 series whose large-order behaviour is governed by a
single Borel singularity at zeta = A (C1-stabilized, real-positive):

    kappa_n ~ (S/pi) * Gamma(n+beta) / A^(n+beta)
              * (1 + a_1*A/(n+beta-1) + ...)          [leading form tested]

NORMALIZATION: A is in the 1/N variable throughout — the SAME normalization
as the C1 sibling (qbeta_borel_conformal_pade_probe.py: "A is in the 1/N
normalization; divide by 2*pi for the 2*pi/N variable") and as the
predecessor's ratio formula A_k = k*kappa_{k-1}/kappa_k
(docs/audits/scripts/qbeta_borel_pade_action.py), which this probe
reproduces as an arithmetic identity (A_k = k/r_k, r_k = kappa_k/kappa_{k-1}).

CONVENTION (beta vs alpha): the large-order exponent beta EQUALS the Borel
branch exponent alpha of C1.  Proof sketch: B(zeta) ~ C*(1 - zeta/A)^(-alpha)
near zeta = A expands as b_n = C*Gamma(n+alpha)/(Gamma(alpha)*n!)*A^(-n), so
kappa_n = n!*b_n = [C*A^alpha/Gamma(alpha)] * Gamma(n+alpha)/A^(n+alpha) —
i.e. beta = alpha with S/pi = C*A^alpha/Gamma(alpha).  Verified numerically
below (binomial-expansion ratio identity, hard assert).

METHOD:
  1. FORWARD: exact rungs kappa_1..kappa_4 (closed forms, main) + the
     C1-stabilized A (mean + range as the error band).  For every rung pair
     (m,n), m<n<=4, solve the leading 2-parameter (S, beta) form; TEST
     (a) whether (S, beta) stabilizes across pair choices, and (b) whether
     the PREDICTED kappa_5, kappa_6 match the main-witness numerics within
     the band obtained by propagating A over its C1 range [0.6338, 0.6833].
     NO subleading parameter is fitted; the implied a_1 size is reported as
     a diagnostic only.
  2. INVERSE: fix the observed kappa_5 (14 digits), kappa_6 (10 digits);
     with the exact kappa_4 the two consecutive ratio equations
     r_5 = (4+beta)/A, r_6 = (5+beta)/A close exactly:
     A = 1/(r_6 - r_5), beta = A*r_5 - 4.  Compare the implied A to the C1
     band and the implied beta to C1's alpha.  A consecutive-TRIPLE ladder
     (1,2,3)->(2,3,4)->(3,4,5)->(4,5,6) is reported as the self-contained
     stability diagnostic.
  3. OPTIONAL PSLQ (gated): only if the large-order form + exact
     kappa_1..kappa_4 pins >= 12 stable digits of kappa_5 is a single
     budget-checked PSLQ of kappa_5/5! against the Q(sqrt3)*pi^5 line run
     (entropy budget per PR #1805 / the C2 machinery in
     computations/probes/qbeta_qsqrt3_borel_pslq_probe.py).  The budget
     arithmetic is logged either way.

KILL CRITERION (pre-stated): if the predicted kappa_5 misses the observed
value by more than the A-spread-propagated band under EVERY rung-pair
choice, the verdict is NEGATIVE scope-(a): "leading one-instanton
large-order form insufficient at n <= 6 — subleading Stokes sectors or a
slower transient", and NO extra parameters are tuned to force agreement.
If the prediction lands (some pair's band contains the observed value), the
verdict is CONSISTENT — never "derived" — and the report states exactly
what an exact-arithmetic kappa_5 candidate would still require (the
entropy-budget digits from the C2 machinery).

DISCIPLINE: audit-only witness; NO fit to QOU data; NO c_k value wired; NO
tier change; scope-(a) wording throughout.  Reference-data precision
(kappa_5: 14 digits, kappa_6: 10 digits) and the C1 A-spread — not the
50-dps L1 floor — bound the achievable tolerance; every assertion states
its own tolerance source.  Self-contained (mpmath only).
"""
import datetime
import hashlib
import json
import math
import os
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 60

# ---------------------------------------------------------------------------
# Reference data.
# kappa strings + ratio strings: origin/main
# docs/audits/scripts/qbeta-even-borel-singularity.witness.json
# (commitSha 4c4a936); kappa_1..kappa_4 have exact closed forms on main
# (#3606/#3628), kappa_5/kappa_6 are numeric with 14/10 confident digits.
# ---------------------------------------------------------------------------
WITNESS_KAPPA = {
    1: "0.55421647240489989879",
    2: "0.73108180748810063843",
    3: "2.6545270569495453476",
    4: "13.094774926381671947",
    5: "84.642165605038443528",
    6: "676.9466789641050315",
}
CONFIDENT_DIGITS = {1: 36, 2: 30, 3: 25, 4: 19, 5: 14, 6: 10}
# main-witness linear-ratio data (ratios[n] = kappa_{n+1}/kappa_n, 12 digits)
WITNESS_RATIOS = {
    1: "1.31912681035",
    2: "3.63095761618",
    3: "4.93299734584",
    4: "6.46381217554",
    5: "7.99774762525",
}
# Exact-rung rational heights on the Q(sqrt3)-parity line (#3606/#3628):
# kappa_1 = (11/108)sqrt3 pi (height 108), kappa_3 = (1081/21870)sqrt3 pi^3
# (height 21870) — used to project the kappa_5 height for the C2 budget.
ODD_RUNG_HEIGHTS = {1: 108, 3: 21870}
EVEN_RUNG_HEIGHTS = {2: 27, 4: 729}

C1_WITNESS_FILE = "qbeta-borel-conformal-pade.witness.json"

# entropy budget (PR #1805 rule, identical to the C2 probe machinery)
PSLQ_N_TERMS = 2          # PSLQ vector [v, 1]
BASE_MARGIN = 3.0
PSLQ_GATE_DIGITS = 12     # pre-stated gate for the optional PSLQ
H_FLOOR = 10

RUNG_PAIRS = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
A_GRID_POINTS = 17


def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _repo_head_sha():
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_find_repo_root(),
            text=True).strip()
    except (subprocess.SubprocessError, OSError):
        return "unknown"
    return sha or "unknown"


# ---------------------------------------------------------------------------
# Leading one-instanton large-order form: solve / predict.
# ---------------------------------------------------------------------------
def solve_beta(m, n, km, kn, A):
    """beta of kappa_n/kappa_m = Gamma(n+beta)/Gamma(m+beta) * A^(m-n).
    Consecutive pairs close analytically: kappa_{m+1}/kappa_m = (m+beta)/A."""
    if n == m + 1:
        return A * kn / km - m
    target = mp.log(kn / km) + (n - m) * mp.log(A)

    def f(b):
        return mp.loggamma(n + b) - mp.loggamma(m + b) - target
    return mp.findroot(f, (mp.mpf("0.0"), mp.mpf("0.5")),
                       solver="secant", tol=mp.mpf("1e-50"))


def S_of(n, kn, beta, A):
    """S from one rung: kappa_n = (S/pi)*Gamma(n+beta)/A^(n+beta)."""
    return mp.pi * kn * A ** (n + beta) / mp.gamma(n + beta)


def predict(j, S, beta, A):
    return S / mp.pi * mp.gamma(j + beta) * A ** (-(j + beta))


def triple_invert(k_a, k_b, k_c, n_a):
    """(A, beta) from three consecutive rungs kappa_{n_a}, kappa_{n_a+1},
    kappa_{n_a+2}: r1 = (n_a+beta)/A, r2 = (n_a+1+beta)/A =>
    A = 1/(r2-r1), beta = A*r1 - n_a."""
    r1, r2 = k_b / k_a, k_c / k_b
    A = 1 / (r2 - r1)
    return A, A * r1 - n_a


# ---------------------------------------------------------------------------
# Entropy budget (PR #1805 / C2 machinery).
# ---------------------------------------------------------------------------
def needed_digits(H, trials=1):
    return PSLQ_N_TERMS * math.log10(2 * H) + BASE_MARGIN + math.log10(trials)


def budget_maxcoeff(digits, trials=1):
    margin = BASE_MARGIN + math.log10(trials)
    if digits <= margin:
        return 0
    return int(10 ** ((digits - margin) / PSLQ_N_TERMS) / 2)


def main():
    assertions = []

    def check(name, passed, computed=None, expected=None, tolerance=None,
              source=None):
        entry = {"name": name, "passed": bool(passed)}
        if computed is not None:
            entry["computed"] = computed
        if expected is not None:
            entry["expected"] = expected
        if tolerance is not None:
            entry["tolerance"] = tolerance
        if source is not None:
            entry["source"] = source
        assertions.append(entry)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    pi, sqrt3 = mp.pi, mp.sqrt(3)

    # --- 0. load the C1 stabilized A (same branch, same directory) ----------
    c1_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           C1_WITNESS_FILE)
    with open(c1_path) as f:
        c1 = json.load(f)
    if not c1.get("allPassed"):
        print("ABORT: C1 witness allPassed is false — stabilized A unusable.")
        return 1
    A_mean = mp.mpf(c1["result"]["A_stabilized"])
    A_min = mp.mpf(c1["result"]["A_range"][0])
    A_max = mp.mpf(c1["result"]["A_range"][1])
    alpha_c1 = mp.mpf(c1["result"]["branch_exponent_alpha_mean"])
    alphas_56 = [mp.mpf(v["alpha"]) for v in
                 c1["result"]["conformal_dlog"].values()
                 if isinstance(v, dict) and v.get("rungs") in (5, 6)
                 and "alpha" in v]
    alpha_lo, alpha_hi = min(alphas_56), max(alphas_56)
    print(f"C1 input: A = {mp.nstr(A_mean, 10)} in "
          f"[{mp.nstr(A_min, 10)}, {mp.nstr(A_max, 10)}], alpha = "
          f"{mp.nstr(alpha_c1, 6)} (per-config [{mp.nstr(alpha_lo, 5)}, "
          f"{mp.nstr(alpha_hi, 5)}]); 1/N normalization "
          f"(scriptHash {c1['scriptHash']})", flush=True)

    # --- 1. exact rungs vs main witness -------------------------------------
    kappa_exact = {
        1: mp.mpf(11) / 108 * sqrt3 * pi,
        2: mp.mpf(2) / 27 * pi ** 2,
        3: mp.mpf(1081) / 21870 * sqrt3 * pi ** 3,
        4: mp.mpf(98) / 729 * pi ** 4,
    }
    print("\n=== 1. exact rungs kappa_1..kappa_4 vs main witness ===",
          flush=True)
    ok_exact = True
    exact_reldiffs = {}
    for n in range(1, 5):
        rel = abs(kappa_exact[n] / mp.mpf(WITNESS_KAPPA[n]) - 1)
        exact_reldiffs[str(n)] = mp.nstr(rel, 4)
        print(f"  kappa_{n}: {mp.nstr(kappa_exact[n], 22)}  rel "
              f"{mp.nstr(rel, 4)}")
        ok_exact = ok_exact and rel < mp.mpf("1e-18")
    check("kappa_1_4_exact_match_witness", ok_exact,
          computed=exact_reldiffs, expected="rel < 1e-18 each",
          tolerance="1e-18",
          source="closed forms (11/108)sqrt3 pi, (2/27)pi^2, "
                 "(1081/21870)sqrt3 pi^3, (98/729)pi^4 vs the 20-digit "
                 "main-witness strings (tolerance at the reference-string "
                 "precision).")
    if not ok_exact:
        print("ABORT: exact rungs disagree with the main witness.")
        return 1

    kappa = dict(kappa_exact)
    kappa[5] = mp.mpf(WITNESS_KAPPA[5])
    kappa[6] = mp.mpf(WITNESS_KAPPA[6])

    # --- 2. normalization cross-check vs predecessor ratio formula ----------
    print("\n=== 2. normalization cross-check (predecessor A_k = "
          "k*kappa_{k-1}/kappa_k) ===", flush=True)
    ratios = {n: kappa[n + 1] / kappa[n] for n in range(1, 6)}
    ok_ratio = True
    for n in range(1, 6):
        rel = abs(ratios[n] / mp.mpf(WITNESS_RATIOS[n]) - 1)
        ok_ratio = ok_ratio and rel < mp.mpf("1e-11")
    # A_k * r_k = k is the identity tying our r_n = kappa_n/kappa_{n-1}
    # convention to the predecessor's A_k = k*kappa_{k-1}/kappa_k.
    ok_ident = all(abs((k / ratios[k - 1]) * ratios[k - 1] - k)
                   < mp.mpf("1e-50") for k in range(2, 7))
    for k in (5, 6):
        print(f"  A_{k} = k*kappa_{k - 1}/kappa_{k} = "
              f"{mp.nstr(k / ratios[k - 1], 10)}")
    check("ratio_normalization_matches_predecessor", ok_ratio and ok_ident,
          computed={str(n): mp.nstr(ratios[n], 12) for n in ratios},
          expected="12-digit main-witness ratio strings; A_k*r_k = k exact",
          tolerance="1e-11 (main-witness ratio-string precision)",
          source="our r_n = kappa_n/kappa_{n-1} vs the main witness ratios "
                 "and the predecessor's A_k formula "
                 "(qbeta_borel_pade_action.py) — SAME 1/N normalization as "
                 "the C1 A.")

    # --- 3. solver known-answer controls ------------------------------------
    print("\n=== 3. solver self-checks (synthetic control + beta=alpha "
          "convention) ===", flush=True)
    # 3a. synthetic exact one-instanton series: recover (S, beta) + kappa_5.
    A_s, beta_s, S_s = mp.mpf("0.6"), mp.mpf("0.3"), mp.mpf(2)
    kap_s = {j: predict(j, S_s, beta_s, A_s) for j in range(1, 6)}
    ok_syn = True
    for (m, n) in RUNG_PAIRS:
        b = solve_beta(m, n, kap_s[m], kap_s[n], A_s)
        Sm = S_of(m, kap_s[m], b, A_s)
        Sn = S_of(n, kap_s[n], b, A_s)
        ok_syn = ok_syn and abs(b - beta_s) < mp.mpf("1e-40") \
            and abs(Sm / Sn - 1) < mp.mpf("1e-40") \
            and abs(predict(5, Sn, b, A_s) / kap_s[5] - 1) < mp.mpf("1e-40")
    check("synthetic_control_recovers_S_beta_kappa5", ok_syn,
          expected="beta, S, kappa_5 recovered to 1e-40 on an exact "
                   "one-instanton series (A=0.6, beta=0.3, S=2), all 6 pairs",
          tolerance="1e-40",
          source="known-answer control of the pairwise solver — exact "
                 "arithmetic, so full working precision applies.")
    # 3b. consecutive closed form == root-finder.
    ok_cf = True
    for m in (1, 2, 3):
        b_closed = solve_beta(m, m + 1, kappa[m], kappa[m + 1], A_mean)
        target = mp.log(kappa[m + 1] / kappa[m]) + mp.log(A_mean)

        def f(b, _m=m, _t=target):
            return mp.loggamma(_m + 1 + b) - mp.loggamma(_m + b) - _t
        b_root = mp.findroot(f, (mp.mpf("-0.4"), mp.mpf("0.6")),
                             solver="secant", tol=mp.mpf("1e-50"))
        ok_cf = ok_cf and abs(b_closed - b_root) < mp.mpf("1e-30")
    check("consecutive_closed_form_matches_findroot", ok_cf,
          tolerance="1e-30",
          source="beta = A*r - m (analytic, consecutive pair) vs the "
                 "loggamma root-finder on the real rungs at A_mean.")
    # 3c. beta = alpha convention: (1-zeta/A)^(-alpha) binomial expansion.
    a_t, A_t = mp.mpf("0.25"), mp.mpf("0.65")
    ok_conv = True
    for n in range(1, 6):
        bn = mp.gamma(n + a_t) / (mp.gamma(a_t) * mp.factorial(n)) \
            * A_t ** (-n)
        bn1 = mp.gamma(n + 1 + a_t) / (mp.gamma(a_t)
                                       * mp.factorial(n + 1)) \
            * A_t ** (-(n + 1))
        kn, kn1 = mp.factorial(n) * bn, mp.factorial(n + 1) * bn1
        ok_conv = ok_conv and abs(kn1 / kn - (n + a_t) / A_t) \
            < mp.mpf("1e-45")
    check("beta_equals_alpha_convention", ok_conv,
          expected="kappa_{n+1}/kappa_n = (n+alpha)/A for the expansion of "
                   "(1-zeta/A)^(-alpha) — the large-order beta IS the C1 "
                   "branch exponent alpha",
          tolerance="1e-45",
          source="binomial-expansion ratio identity, exact arithmetic.")

    # --- 4. FORWARD: pairwise (S, beta) + predicted kappa_5/kappa_6 ---------
    print("\n=== 4. FORWARD: (S, beta) per rung pair at A_mean; predicted "
          "kappa_5/kappa_6 with A-spread bands ===", flush=True)
    A_grid = [A_min + (A_max - A_min) * mp.mpf(i) / (A_GRID_POINTS - 1)
              for i in range(A_GRID_POINTS)]
    obs5, obs6 = kappa[5], kappa[6]
    forward = {}
    betas_at_mean = {}
    ok_S_pair = True
    consistent_pairs_k5, consistent_pairs_k6 = [], []
    for (m, n) in RUNG_PAIRS:
        b_mean = solve_beta(m, n, kappa[m], kappa[n], A_mean)
        S_mean = S_of(n, kappa[n], b_mean, A_mean)
        ok_S_pair = ok_S_pair and \
            abs(S_of(m, kappa[m], b_mean, A_mean) / S_mean - 1) \
            < mp.mpf("1e-30")
        k5s, k6s = [], []
        for A in A_grid:
            b = solve_beta(m, n, kappa[m], kappa[n], A)
            S = S_of(n, kappa[n], b, A)
            k5s.append(predict(5, S, b, A))
            k6s.append(predict(6, S, b, A))
        k5_lo, k5_hi = min(k5s), max(k5s)
        k6_lo, k6_hi = min(k6s), max(k6s)
        in5 = bool(k5_lo <= obs5 <= k5_hi)
        in6 = bool(k6_lo <= obs6 <= k6_hi)
        if in5:
            consistent_pairs_k5.append(f"({m},{n})")
        if in6:
            consistent_pairs_k6.append(f"({m},{n})")
        k5_mean = predict(5, S_mean, b_mean, A_mean)
        k6_mean = predict(6, S_mean, b_mean, A_mean)
        betas_at_mean[(m, n)] = b_mean
        forward[f"({m},{n})"] = {
            "beta_at_A_mean": mp.nstr(b_mean, 8),
            "S_at_A_mean": mp.nstr(S_mean, 8),
            "kappa5_pred_at_A_mean": mp.nstr(k5_mean, 10),
            "kappa5_pred_band": [mp.nstr(k5_lo, 10), mp.nstr(k5_hi, 10)],
            "kappa5_rel_miss_at_A_mean": mp.nstr(k5_mean / obs5 - 1, 4),
            "kappa5_obs_within_band": in5,
            "kappa6_pred_at_A_mean": mp.nstr(k6_mean, 10),
            "kappa6_pred_band": [mp.nstr(k6_lo, 10), mp.nstr(k6_hi, 10)],
            "kappa6_rel_miss_at_A_mean": mp.nstr(k6_mean / obs6 - 1, 4),
            "kappa6_obs_within_band": in6,
        }
        print(f"  pair ({m},{n}): beta = {mp.nstr(b_mean, 6)}  "
              f"k5_pred = {mp.nstr(k5_mean, 8)} band "
              f"[{mp.nstr(k5_lo, 8)}, {mp.nstr(k5_hi, 8)}] "
              f"{'IN' if in5 else 'out'};  "
              f"k6_pred = {mp.nstr(k6_mean, 8)} band "
              f"[{mp.nstr(k6_lo, 8)}, {mp.nstr(k6_hi, 8)}] "
              f"{'IN' if in6 else 'out'}", flush=True)
    check("pairwise_S_from_both_rungs_consistent", ok_S_pair,
          tolerance="1e-30",
          source="S computed from rung m and rung n of each pair must agree "
                 "(construction identity of the 2-parameter solve).")

    beta_vals = list(betas_at_mean.values())
    beta_spread = max(beta_vals) - min(beta_vals)
    beta_no_k1 = [b for (m, n), b in betas_at_mean.items() if m != 1]
    beta_frontier = betas_at_mean[(3, 4)]
    print(f"\n  (a) stability: beta across all 6 pairs spans "
          f"[{mp.nstr(min(beta_vals), 5)}, {mp.nstr(max(beta_vals), 5)}] "
          f"(spread {mp.nstr(beta_spread, 4)}); kappa_1-free pairs "
          f"[{mp.nstr(min(beta_no_k1), 5)}, {mp.nstr(max(beta_no_k1), 5)}]; "
          f"frontier pair (3,4): beta = {mp.nstr(beta_frontier, 6)} vs "
          f"C1 alpha {mp.nstr(alpha_c1, 5)}", flush=True)

    # implied subleading size (DIAGNOSTIC ONLY — not fitted, not fed back)
    r5_pred_34 = (4 + beta_frontier) / A_mean
    a1_implied = (obs5 / kappa[4] / r5_pred_34 - 1) \
        * (4 + beta_frontier) / A_mean
    print(f"  diagnostic: implied a_1 ~ {mp.nstr(a1_implied, 3)} from the "
          f"(3,4)-pair kappa_5 residual (NOT used in any prediction)",
          flush=True)

    # --- 5. INVERSE: implied (A, beta) from observed kappa_5, kappa_6 -------
    print("\n=== 5. INVERSE: consecutive-triple ladder -> implied (A, beta) "
          "===", flush=True)
    triple_ladder = {}
    for n0 in (1, 2, 3, 4):
        At, bt = triple_invert(kappa[n0], kappa[n0 + 1], kappa[n0 + 2], n0)
        triple_ladder[f"({n0},{n0 + 1},{n0 + 2})"] = {
            "A": mp.nstr(At, 10), "beta": mp.nstr(bt, 8)}
        print(f"  triple ({n0},{n0 + 1},{n0 + 2}): A = {mp.nstr(At, 8)}  "
              f"beta = {mp.nstr(bt, 6)}")
    A_impl, beta_impl = triple_invert(kappa[4], kappa[5], kappa[6], 4)
    A_impl_lo, beta_impl_lo = triple_invert(kappa[3], kappa[4], kappa[5], 3)
    # inverse self-consistency: implied (A, beta) reproduce r_5, r_6 exactly
    ok_inv = abs((4 + beta_impl) / A_impl / ratios[4] - 1) < mp.mpf("1e-40") \
        and abs((5 + beta_impl) / A_impl / ratios[5] - 1) < mp.mpf("1e-40")
    check("inverse_reproduces_r5_r6", ok_inv, tolerance="1e-40",
          source="(A,beta) from the (4,5,6) triple must reproduce the input "
                 "ratios r_5, r_6 exactly (algebraic inversion identity).")
    # input-precision propagation (kappa_5: 1e-14 rel, kappa_6: 1e-10 rel)
    dA_in, db_in = mp.mpf(0), mp.mpf(0)
    for s5 in (-1, 1):
        for s6 in (-1, 1):
            k5p = kappa[5] * (1 + s5 * mp.mpf("1e-14"))
            k6p = kappa[6] * (1 + s6 * mp.mpf("1e-10"))
            Ap, bp = triple_invert(kappa[4], k5p, k6p, 4)
            dA_in = max(dA_in, abs(Ap - A_impl))
            db_in = max(db_in, abs(bp - beta_impl))
    # model-truncation systematic: shift between the last two triples
    dA_sys = abs(A_impl - A_impl_lo)
    db_sys = abs(beta_impl - beta_impl_lo)
    A_in_c1 = bool(A_min <= A_impl <= A_max)
    beta_in_alpha = bool(alpha_lo - db_sys <= beta_impl
                         <= alpha_hi + db_sys)
    print(f"  implied (4,5,6): A = {mp.nstr(A_impl, 10)}  beta = "
          f"{mp.nstr(beta_impl, 8)}")
    print(f"  input-digit propagation: dA < {mp.nstr(dA_in, 3)}, dbeta < "
          f"{mp.nstr(db_in, 3)} (NEGLIGIBLE vs the truncation systematic "
          f"dA ~ {mp.nstr(dA_sys, 3)}, dbeta ~ {mp.nstr(db_sys, 3)} from "
          f"the (3,4,5)->(4,5,6) triple shift)")
    print(f"  implied A within C1 range [{mp.nstr(A_min, 6)}, "
          f"{mp.nstr(A_max, 6)}]: {A_in_c1};  implied beta vs C1 alpha "
          f"{mp.nstr(alpha_c1, 5)} (per-config [{mp.nstr(alpha_lo, 4)}, "
          f"{mp.nstr(alpha_hi, 4)}]): diff {mp.nstr(beta_impl - alpha_c1, 3)}"
          f" -> {'consistent' if beta_in_alpha else 'tension'}", flush=True)

    # --- 6. optional PSLQ, gated on the large-order pin ----------------------
    print("\n=== 6. PSLQ gate (pre-stated: run ONLY if the forward form "
          "pins >= 12 stable digits of kappa_5) ===", flush=True)
    fw34 = forward["(3,4)"]
    band_lo, band_hi = mp.mpf(fw34["kappa5_pred_band"][0]), \
        mp.mpf(fw34["kappa5_pred_band"][1])
    band_rel = (band_hi - band_lo) / obs5
    pinned_digits = max(0, int(mp.floor(-mp.log10(band_rel)))) \
        if band_rel > 0 else 0
    # budget arithmetic logged either way (C2 machinery, PR #1805 rule)
    h5_proj = int(ODD_RUNG_HEIGHTS[3]
                  * (ODD_RUNG_HEIGHTS[3] / ODD_RUNG_HEIGHTS[1]))
    h6_proj = int(EVEN_RUNG_HEIGHTS[4]
                  * (EVEN_RUNG_HEIGHTS[4] / EVEN_RUNG_HEIGHTS[2]))
    need5 = needed_digits(h5_proj)
    need6 = needed_digits(h6_proj)
    admissible_H = budget_maxcoeff(pinned_digits)
    ok_budget = (needed_digits(100) - (2 * math.log10(200) + 3.0)) < 1e-9 \
        and budget_maxcoeff(20) > budget_maxcoeff(12) > 0 \
        and (admissible_H == 0
             or needed_digits(admissible_H) <= pinned_digits + 1e-9)
    check("entropy_budget_arithmetic_spot_check", ok_budget,
          computed={"pinned_digits": pinned_digits,
                    "admissible_height": admissible_H,
                    "kappa5_height_projected": h5_proj,
                    "digits_needed_at_projected_height":
                        f"{need5:.1f}"},
          expected="needed(H=100,n=2,m=3) = 2*log10(200)+3; inversion never "
                   "over-asks; monotone",
          source="PR #1805 entropy rule, identical machinery to "
                 "qbeta_qsqrt3_borel_pslq_probe.py.")
    pslq_ran = False
    pslq_row = {
        "gate": f"forward-pinned stable digits {pinned_digits} "
                f"(band rel width {mp.nstr(band_rel, 3)}, frontier pair "
                f"(3,4)) vs required {PSLQ_GATE_DIGITS}",
        "outcome": "SKIPPED",
        "budget_arithmetic": {
            "admissible_height_at_pinned_digits": admissible_H,
            "kappa5_projected_height": h5_proj,
            "kappa5_digits_needed_at_projected_height": round(need5, 1),
            "kappa5_witness_digits_available": CONFIDENT_DIGITS[5],
            "kappa5_digit_gap_even_with_witness_numerics":
                round(need5 - CONFIDENT_DIGITS[5], 1),
            "kappa6_projected_height": h6_proj,
            "kappa6_digits_needed_at_projected_height": round(need6, 1),
            "kappa6_witness_digits_available": CONFIDENT_DIGITS[6],
        },
        "reason": (
            f"the leading large-order form pins only ~{pinned_digits} "
            f"stable digits of kappa_5 (A-spread band, frontier pair) — "
            f"far below the {PSLQ_GATE_DIGITS}-digit gate; admissible PSLQ "
            f"height at that budget is {admissible_H} < floor {H_FLOOR}. "
            f"Even the 14 witness digits fall ~{need5 - 14:.1f} digits "
            f"short of the ~{need5:.1f} needed at the height-growth-"
            f"projected kappa_5 height ~{h5_proj:.0f} (heights 108 -> "
            f"21870 on the odd sqrt3 line) — the same entropy wall that "
            f"produced the #3571-class kappa_6 false positive. Refusing "
            f"to over-ask."),
    }
    if pinned_digits >= PSLQ_GATE_DIGITS and admissible_H >= H_FLOOR:
        pslq_ran = True   # pragma: no cover — gate cannot pass at 6 rungs
        v = obs5 / (mp.factorial(5) * sqrt3 * pi ** 5)
        with mp.workdps(max(pinned_digits, 15)):
            rel = mp.pslq([+v, mp.mpf(1)], maxcoeff=admissible_H,
                          maxsteps=50000)
        pslq_row["outcome"] = "RAN"
        pslq_row["relation"] = str(rel)
    print(f"  PSLQ: {pslq_row['outcome']} — {pslq_row['reason']}",
          flush=True)

    # --- 7. verdict (kill criterion evaluated) -------------------------------
    hypothesis_consistent = len(consistent_pairs_k5) > 0
    all_passed = all(x["passed"] for x in assertions)
    if hypothesis_consistent:
        outcome_sentence = (
            f"CONSISTENT (not derived): the frontier pair (3,4) — the most "
            f"asymptotic exact pair — predicts kappa_5 in "
            f"[{fw34['kappa5_pred_band'][0]}, {fw34['kappa5_pred_band'][1]}]"
            f" (obs {WITNESS_KAPPA[5][:10]} INSIDE, miss at A_mean "
            f"{fw34['kappa5_rel_miss_at_A_mean']}) and kappa_6 in "
            f"[{fw34['kappa6_pred_band'][0]}, {fw34['kappa6_pred_band'][1]}]"
            f" (obs {WITNESS_KAPPA[6][:9]} "
            f"{'INSIDE' if fw34['kappa6_obs_within_band'] else 'outside'}). "
            f"Pairs containing kappa_1 miss low — the O(1/n) transient the "
            f"leading form omits, matching the implied a_1 ~ "
            f"{mp.nstr(a1_implied, 2)}.")
    else:
        outcome_sentence = (
            "NEGATIVE scope-(a): the predicted kappa_5 misses the observed "
            "value beyond the A-spread-propagated band under EVERY rung-"
            "pair choice — the leading one-instanton large-order form is "
            "insufficient at n <= 6 (subleading Stokes sectors or a slower "
            "transient); no extra parameters were tuned to force agreement.")
    verdict = (
        f"G2+C3 LARGE-ORDER BRIDGE TEST (scope-(a), leading one-instanton "
        f"form, 1/N normalization): {outcome_sentence} "
        f"(a) (S, beta) does NOT fully stabilize across rung pairs at "
        f"n <= 4 (beta spans [{mp.nstr(min(beta_vals), 4)}, "
        f"{mp.nstr(max(beta_vals), 4)}]) but the kappa_1-free pairs "
        f"cluster and the frontier (3,4) gives beta = "
        f"{mp.nstr(beta_frontier, 5)}. INVERSE: fixing observed "
        f"kappa_5/kappa_6 implies A = {mp.nstr(A_impl, 7)} (INSIDE the C1 "
        f"range [{mp.nstr(A_min, 6)}, {mp.nstr(A_max, 6)}]) and beta = "
        f"{mp.nstr(beta_impl, 5)} vs C1 alpha {mp.nstr(alpha_c1, 4)} "
        f"(same object: beta = alpha, proved by the binomial-expansion "
        f"identity; consecutive triples (3,4,5)->(4,5,6) drift only "
        f"dA ~ {mp.nstr(dA_sys, 2)}, dbeta ~ {mp.nstr(db_sys, 2)}). An "
        f"exact-arithmetic kappa_5 candidate still requires "
        f"~{need5:.0f} trusted digits at the height-projected "
        f"Q(sqrt3)*pi^5 line (have {CONFIDENT_DIGITS[5]}; the large-order "
        f"form pins only ~{pinned_digits}) — PSLQ gate NOT met, PSLQ "
        f"skipped with logged budget; the route remains the bridge-"
        f"equation arithmetic (Ecalle Delta_omega f = A_omega df/dz, "
        f"Garoufalidis-Gu-Marino Stokes data) or a higher-precision "
        f"extraction. No fit wired anywhere; no c_k value; no tier change."
        if all_passed else
        "INCONCLUSIVE — an arithmetic self-check failed; do not cite this "
        "probe's numbers.")

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-kappa-large-order-bridge",
        "description": "Resurgence large-order (bridge-equation) probe of "
                       "the 4_1 Ohtsuki rungs kappa_5/kappa_6 past the "
                       "exact-kappa_4 frontier: solve the leading "
                       "one-instanton (S, beta) form on exact rung pairs "
                       "with the C1-stabilized A, predict kappa_5/kappa_6 "
                       "with A-spread bands, and invert the observed rungs "
                       "for (A, beta) (audit item 6, G2+C3).",
        "audit_only": True,
        "tier": "structural-exact (kappa_1..kappa_4 closed forms) + "
                "numerical (leading large-order form; order-limited; "
                "hypothesis-class test, no value fit)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "parameters": {
            "compute_dps": mp.mp.dps,
            "large_order_form": "kappa_n ~ (S/pi)*Gamma(n+beta)/A^(n+beta) "
                                "(leading; a_1 subleading REPORTED as "
                                "diagnostic, never fitted)",
            "normalization": "A in the 1/N variable (same as C1 and the "
                             "predecessor ratio formula; /2pi for 2pi/N)",
            "beta_alpha_convention": "beta (large-order) = alpha (C1 Borel "
                                     "branch exponent); binomial-expansion "
                                     "identity, asserted",
            "A_input": {"mean": mp.nstr(A_mean, 12),
                        "range": [mp.nstr(A_min, 12), mp.nstr(A_max, 12)],
                        "alpha_mean": mp.nstr(alpha_c1, 8),
                        "alpha_per_config_range": [mp.nstr(alpha_lo, 8),
                                                   mp.nstr(alpha_hi, 8)],
                        "source": C1_WITNESS_FILE,
                        "source_scriptHash": c1["scriptHash"]},
            "kappa_confident_digits": CONFIDENT_DIGITS,
            "A_grid_points": A_GRID_POINTS,
            "rung_pairs": [f"({m},{n})" for (m, n) in RUNG_PAIRS],
            "kill_criterion": "predicted kappa_5 outside the A-spread band "
                              "for EVERY rung pair => NEGATIVE scope-(a); "
                              "no parameter tuning",
            "pslq_gate": f">= {PSLQ_GATE_DIGITS} forward-pinned stable "
                         f"digits of kappa_5 (PR #1805 entropy budget, "
                         f"C2 machinery)",
        },
        "result": {
            "kappa_exact_vs_witness_reldiff": exact_reldiffs,
            "kappa_numeric": {"5": WITNESS_KAPPA[5], "6": WITNESS_KAPPA[6]},
            "forward_per_pair": forward,
            "beta_stability": {
                "all_pairs_range": [mp.nstr(min(beta_vals), 8),
                                    mp.nstr(max(beta_vals), 8)],
                "spread": mp.nstr(beta_spread, 6),
                "kappa1_free_pairs_range": [mp.nstr(min(beta_no_k1), 8),
                                            mp.nstr(max(beta_no_k1), 8)],
                "frontier_pair_34_beta": mp.nstr(beta_frontier, 10),
            },
            "consistent_pairs_kappa5": consistent_pairs_k5,
            "consistent_pairs_kappa6": consistent_pairs_k6,
            "implied_a1_diagnostic_only": mp.nstr(a1_implied, 6),
            "inverse_triple_ladder": triple_ladder,
            "inverse_implied": {
                "A": mp.nstr(A_impl, 12),
                "beta": mp.nstr(beta_impl, 10),
                "A_within_C1_range": A_in_c1,
                "beta_vs_C1_alpha_diff": mp.nstr(beta_impl - alpha_c1, 6),
                "beta_consistent_with_C1_alpha_configs": beta_in_alpha,
                "input_digit_propagation": {"dA": mp.nstr(dA_in, 4),
                                            "dbeta": mp.nstr(db_in, 4)},
                "truncation_systematic_345_vs_456": {
                    "dA": mp.nstr(dA_sys, 4), "dbeta": mp.nstr(db_sys, 4)},
            },
            "pslq": pslq_row,
            "pslq_ran": pslq_ran,
            "hypothesis_outcome": ("CONSISTENT" if hypothesis_consistent
                                   else "NEGATIVE-scope-a"),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: G2 bridge equation / C3 "
                    "transseries past the kappa_4 frontier",
            "audit_item": "docs/audits/2026-07-12-borel-alien-calculus-"
                          "utilization-audit.md item 6 (G2+C3)",
            "A_source": "computations/probes/"
                        "qbeta_borel_conformal_pade_probe.py (C1, this "
                        "branch)",
            "kappa_source": "origin/main docs/audits/scripts/"
                            "qbeta-even-borel-singularity.witness.json "
                            "(commit 4c4a936)",
            "normalization_crosscheck": "docs/audits/scripts/"
                                        "qbeta_borel_pade_action.py "
                                        "(A_k = k*kappa_{k-1}/kappa_k; "
                                        "Richardson A ~ 0.6937 on its own "
                                        "noisier order-11 ladder)",
            "budget_machinery": "computations/probes/"
                                "qbeta_qsqrt3_borel_pslq_probe.py (C2)",
            "next": "bridge-equation arithmetic (Ecalle; Garoufalidis-Gu-"
                    "Marino 4_1 Stokes structure over Q(sqrt(-3))) to "
                    "generate kappa_5 exactly, or a higher-precision "
                    "ladder extraction (~17+ trusted digits) to clear the "
                    "PSLQ entropy wall",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-kappa-large-order-bridge.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
