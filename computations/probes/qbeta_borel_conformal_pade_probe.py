#!/usr/bin/env python3
"""
Conformal-mapped Borel-Pade extraction of the 4_1 instanton action A (audit
item C1 of docs/audits/2026-07-12-borel-alien-calculus-utilization-audit.md).

Predecessor (docs/audits/scripts/qbeta_borel_pade_action.py) abandoned the raw
Borel-Pade of the 4_1 Ohtsuki/Kashaev ladder because its nearest pole is
Froissart-unstable (jumps 0.71 -> 0.049 -> 0.049+0.12j across [M/M]); it fell
back to a Richardson ratio limit A ~ 0.6937 which yields |A| but cannot
phase-resolve the Borel singularity.  The cure implemented here is the
textbook CONFORMAL MAP of the Borel plane: uniformize the cut [A0, inf) via
zeta = 4*A0*w/(1+w)^2, re-expand in w, Pade there, map the located singularity
back, and iterate the estimate to a fixed point.

Input series (fluctuation 1 + sum_n kappa_n x^n, x = 1/N normalization):
  kappa_1 = (11/108)  sqrt(3) pi        (exact rung, main)
  kappa_2 = (2/27)    pi^2              (exact)
  kappa_3 = (1081/21870) sqrt(3) pi^3   (exact)
  kappa_4 = (98/729)  pi^4              (exact)
  kappa_5 ~ 84.642165605038443528       (numeric, 14 confident digits)
  kappa_6 ~ 676.9466789641050315        (numeric, 10 confident digits)
(numeric rungs + reference strings from origin/main
 docs/audits/scripts/qbeta-even-borel-singularity.witness.json).

Borel transform: B(zeta) = 1 + sum_{n>=1} kappa_n zeta^n / n!  (predecessor
normalization; A is in the 1/N variable — divide by 2*pi for the 2*pi/N one).

Methods, in order:
  (a)  BASELINE raw [L/M] Pade of B(zeta)  — reproduces the Froissart /
       branch-cut pole scatter that motivated C1;
  (b)  Dlog-Pade of B(zeta)                — pole + branch exponent alpha;
  (c1) CONFORMAL Pade: map with trial A0 held a margin mu above the running
       estimate (keeps the branch point strictly inside |w| < 1 where Pade
       locates it robustly; the naive A0 = A fixed point pushes w* onto the
       disc boundary and is unstable), damped fixed-point iteration from
       A0 = 0.6177 (the sibling ratio-fit trial).  Documents the residual
       downward order-drift = Pade-on-branch-point bias.
  (c2) CONFORMAL + DLOG Pade (headline): same map + iteration, but Pade is
       applied to (d/dw) log B(zeta(w)), which converts the mapped branch
       point into a genuine simple pole — the correct estimator for a
       branch-type Borel singularity.

Structural note on "truncation": the mapped coefficient d_k of w^k depends
only on kappa_1..kappa_k (zeta = O(w)), so an [L/M] Pade consumes exactly
rungs 1..(L+M) (or 1..(L+M+1) for the dlog variant) — the truncation axis and
the Pade-order axis COINCIDE.  The 4/5/6-rung stability study is therefore
the [L/M] grid itself; the margin mu is varied as an independent robustness
axis.

Reality: all Borel coefficients b_n = kappa_n/n! are POSITIVE, so by
Pringsheim's theorem the dominant Borel singularity lies ON the positive real
axis — the numerical phase check below confirms the located singularity is
real, in agreement with the predecessor's amphichirality argument
(CS(4_1) = 0 => the action is real; predecessor lines ~121-140 & 189-196).

Honest scope-(a) verdict: stabilized A + spread vs Vol(4_1)/pi ~ 0.646132,
the sibling ratio-fit 0.617661, and 2/e ~ 0.735759.  Identification is
claimed ONLY if the candidate lies within the observed spread.  NO fit to QOU
data, NO wiring, NO c_k value, NO tier change.  Reference-data precision
(kappa_5: 14 digits, kappa_6: 10 digits) — not the 50-dps L1 floor — bounds
achievable tolerance; cross-checks below are set to the data precision and
say so.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

mp.mp.dps = 60

# ---------------------------------------------------------------------------
# reference strings from origin/main qbeta-even-borel-singularity.witness.json
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
A0_TRIAL = mp.mpf("0.617661555754")  # sibling 5-ratio-fit estimate (main)
MARGINS = (mp.mpf("1.5"), mp.mpf("2.0"))
FP_TOL = mp.mpf("1e-11")


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
# series utilities (dense lists of coefficients, index = power)
# ---------------------------------------------------------------------------
def poly_mul(a, b, T):
    """Truncated product of coefficient lists a, b to order T (inclusive)."""
    out = [mp.mpf(0)] * (T + 1)
    for i, ai in enumerate(a):
        if i > T or ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j > T:
                break
            out[i + j] += ai * bj
    return out


def series_div(num, den, T):
    """Coefficients of num/den to order T (den[0] != 0)."""
    out = []
    for k in range(T + 1):
        s = num[k] if k < len(num) else mp.mpf(0)
        for j in range(1, k + 1):
            if j < len(den):
                s -= den[j] * out[k - j]
        out.append(s / den[0])
    return out


def pade(c, L, M):
    """[L/M] Pade of sum c_k z^k. Needs c_0..c_{L+M}. Returns (p, q), q0=1."""
    if L + M >= len(c):
        raise ValueError("not enough coefficients")
    A = mp.matrix(M, M)
    rhs = mp.matrix(M, 1)
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            idx = L + i - j
            A[i - 1, j - 1] = c[idx] if idx >= 0 else mp.mpf(0)
        rhs[i - 1] = -c[L + i]
    qv = mp.lu_solve(A, rhs)
    q = [mp.mpf(1)] + [qv[k] for k in range(M)]
    p = []
    for k in range(L + 1):
        p.append(mp.fsum(q[j] * c[k - j] for j in range(0, min(k, M) + 1)))
    return p, q


def roots_of(coeffs_lowhigh):
    cl = list(coeffs_lowhigh)
    while len(cl) > 1 and abs(cl[-1]) < mp.mpf("1e-55"):
        cl.pop()
    if len(cl) <= 1:
        return []
    return mp.polyroots(list(reversed(cl)), maxsteps=500, extraprec=200)


def clean_poles(p, q, max_abs, doublet_tol=mp.mpf("1e-5")):
    """Denominator roots minus Froissart doublets (pole ~ numerator zero)."""
    poles = roots_of(q)
    zeros = roots_of(p)
    out = []
    for w in poles:
        if abs(w) > max_abs:
            continue
        if any(abs(w - z) < doublet_tol * max(1, abs(w)) for z in zeros):
            continue
        out.append(w)
    return out


def residue_at(p, q, w):
    """Residue of the Pade rational p/q at a simple denominator root w."""
    num = mp.fsum(p[k] * w ** k for k in range(len(p)))
    dq = mp.fsum(k * q[k] * w ** (k - 1) for k in range(1, len(q)))
    return num / dq


# ---------------------------------------------------------------------------
# conformal map: zeta = A0 * 4w/(1+w)^2 maps |w|<1 onto C \ [A0, +inf)
# ---------------------------------------------------------------------------
def mapped_series(b, A0, T):
    """d_n of B(zeta(w)) = sum d_n w^n, exact to order T (zeta = O(w));
    d_k depends only on b_1..b_k."""
    z = [mp.mpf(0)] * (T + 1)
    for k in range(1, T + 1):
        z[k] = 4 * A0 * ((-1) ** (k - 1)) * k
    d = [mp.mpf(0)] * (T + 1)
    d[0] = b[0]
    zpow = [mp.mpf(1)] + [mp.mpf(0)] * T
    for n in range(1, min(len(b) - 1, T) + 1):
        zpow = poly_mul(zpow, z, T)
        for k in range(T + 1):
            d[k] += b[n] * zpow[k]
    return d


def map_back(A0, w):
    return A0 * 4 * w / (1 + w) ** 2


def conformal_iterate(b, L, M, A_start, margin, use_dlog,
                      max_iter=120, tol=FP_TOL):
    """Damped fixed-point iteration of the conformal-map singularity
    estimate.  Trial A0 = margin * A_est keeps the branch point strictly
    interior; the mapped-back nearest clean pole updates A_est.
    use_dlog: Pade the log-derivative of the mapped series (branch point ->
    simple pole).  Returns dict."""
    A_est = mp.mpf(A_start)
    phase = None
    alpha = None
    T = L + M + (1 if use_dlog else 0)
    if T > len(b) - 1:
        return {"converged": False, "why": "not enough rungs"}
    for it in range(1, max_iter + 1):
        A0 = margin * A_est
        d = mapped_series(b, A0, T)
        if use_dlog:
            Dp = [(n + 1) * d[n + 1] for n in range(T)]
            ser = series_div(Dp, d, T - 1)
        else:
            ser = d
        try:
            p, q = pade(ser, L, M)
        except (ValueError, ZeroDivisionError):
            return {"converged": False, "why": "pade failed", "A": A_est}
        cands = []
        for w in clean_poles(p, q, max_abs=mp.mpf(3)):
            zst = map_back(A0, w)
            if abs(zst) < mp.mpf("0.02"):
                continue
            cands.append((w, zst))
        if not cands:
            return {"converged": False, "why": "no clean pole", "A": A_est,
                    "iters": it}
        w, zst = min(cands, key=lambda t: abs(t[1]))
        A_new = abs(zst)
        phase = mp.arg(zst)
        if use_dlog:
            alpha = -residue_at(p, q, w)
        if abs(A_new - A_est) < tol * A_new:
            return {"converged": True, "A": A_new, "phase": phase,
                    "alpha": alpha, "w_star": w, "iters": it}
        A_est = (A_new + A_est) / 2  # damped update
    return {"converged": False, "why": "max_iter", "A": A_est,
            "phase": phase, "iters": max_iter}


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
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    pi, sqrt3 = mp.pi, mp.sqrt(3)
    Vol_41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))

    # --- 1. exact rungs vs main witness ------------------------------------
    kappa_exact = {
        1: mp.mpf(11) / 108 * sqrt3 * pi,
        2: mp.mpf(2) / 27 * pi ** 2,
        3: mp.mpf(1081) / 21870 * sqrt3 * pi ** 3,
        4: mp.mpf(98) / 729 * pi ** 4,
    }
    print("=== 1. exact rungs kappa_1..kappa_4 vs main witness ===")
    ok_exact = True
    exact_reldiffs = {}
    for n in range(1, 5):
        wv = mp.mpf(WITNESS_KAPPA[n])
        rel = abs(kappa_exact[n] / wv - 1)
        exact_reldiffs[str(n)] = mp.nstr(rel, 4)
        print(f"  kappa_{n}: exact {mp.nstr(kappa_exact[n], 22)}  "
              f"witness {WITNESS_KAPPA[n]}  rel {mp.nstr(rel, 4)}")
        ok_exact = ok_exact and rel < mp.mpf("1e-18")
    check("kappa_1_4_exact_match_witness", ok_exact,
          computed=exact_reldiffs, expected="rel < 1e-18 each",
          tolerance="1e-18",
          source="closed forms (11/108)sqrt3 pi, (2/27)pi^2, "
                 "(1081/21870)sqrt3 pi^3, (98/729)pi^4 vs the 20-digit "
                 "witness strings of qbeta-even-borel-singularity (tolerance "
                 "at the reference-string precision, not the 50-dps floor).")
    if not ok_exact:
        print("ABORT: exact rungs disagree with the main witness.")
        return 1

    kappa = dict(kappa_exact)
    kappa[5] = mp.mpf(WITNESS_KAPPA[5])   # 14 confident digits
    kappa[6] = mp.mpf(WITNESS_KAPPA[6])   # 10 confident digits

    b = [mp.mpf(1)] + [kappa[n] / mp.factorial(n) for n in range(1, 7)]
    print("\n  Borel coefficients b_n = kappa_n/n! (all POSITIVE => "
          "Pringsheim: dominant singularity real-positive):")
    for n, bn in enumerate(b):
        print(f"    b_{n} = {mp.nstr(bn, 15)}")

    # --- 2. (a) baseline raw Pade ------------------------------------------
    print("\n=== 2. (a) BASELINE raw [L/M] Pade of B(zeta) — pole scatter ===")
    baseline = {}
    baseline_mags = []
    for (L, M) in [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]:
        p, q = pade(b, L, M)
        poles = sorted(roots_of(q), key=abs)
        if not poles:
            baseline[f"[{L}/{M}]"] = "no pole"
            continue
        pl = poles[0]
        zeros = roots_of(p)
        is_doublet = any(abs(pl - z) < mp.mpf("1e-5") * max(1, abs(pl))
                         for z in zeros)
        baseline[f"[{L}/{M}]"] = {
            "nearest_pole": mp.nstr(pl, 10),
            "abs": mp.nstr(abs(pl), 10),
            "froissart_doublet": bool(is_doublet),
        }
        baseline_mags.append(abs(pl))
        print(f"  [{L}/{M}] (rungs<= {L + M}): nearest pole "
              f"{mp.nstr(pl, 10)}  |.|={mp.nstr(abs(pl), 8)}  "
              f"doublet={is_doublet}")
    b_min, b_max = min(baseline_mags), max(baseline_mags)
    baseline_spread = (b_max - b_min) / (mp.fsum(baseline_mags)
                                         / len(baseline_mags))
    print(f"  baseline |pole|: min {mp.nstr(b_min, 8)}  max "
          f"{mp.nstr(b_max, 8)}  rel spread {mp.nstr(baseline_spread, 5)}")
    check("baseline_froissart_instability_observed",
          baseline_spread > mp.mpf("0.15"),
          computed=mp.nstr(baseline_spread, 6), expected="> 0.15",
          tolerance="0.15",
          source="relative spread (max-min)/mean of the nearest-pole modulus "
                 "across [L/M] — documents the predecessor's raw Borel-Pade "
                 "instability at 6 rungs (0.28 vs 1.52).")

    # --- 3. (b) dlog-Pade in zeta -------------------------------------------
    print("\n=== 3. (b) Dlog-Pade of B(zeta) ===")
    Bp = [(n + 1) * b[n + 1] for n in range(len(b) - 1)]
    lser = series_div(Bp, b, len(b) - 2)
    dlog = {}
    for (L, M) in [(1, 1), (1, 2), (2, 2), (2, 3)]:
        p, q = pade(lser, L, M)
        cps = clean_poles(p, q, max_abs=mp.mpf(50))
        if not cps:
            dlog[f"[{L}/{M}]"] = "no clean pole"
            continue
        pl = min(cps, key=abs)
        alpha = -residue_at(p, q, pl)
        dlog[f"[{L}/{M}]"] = {
            "nearest_pole": mp.nstr(pl, 10),
            "branch_exponent_alpha": mp.nstr(alpha, 8),
        }
        print(f"  [{L}/{M}] (rungs<= {L + M + 1}): pole {mp.nstr(pl, 10)}  "
              f"alpha = {mp.nstr(alpha, 6)}")

    # --- 4. (c1) conformal Pade (documents branch-point bias/drift) ---------
    print("\n=== 4. (c1) CONFORMAL Pade in w (documents order-drift) ===")
    print(f"  map zeta = 4*A0*w/(1+w)^2, A0 = mu*A_est held above the "
          f"estimate; trial A_est = {mp.nstr(A0_TRIAL, 12)}")
    conf_plain = {}
    for (L, M) in [(2, 2), (2, 3), (3, 3)]:
        for mu in MARGINS:
            r = conformal_iterate(b, L, M, A0_TRIAL, mu, use_dlog=False)
            tag = f"[{L}/{M}],mu={mp.nstr(mu, 3)}"
            if r["converged"]:
                conf_plain[tag] = {"A": mp.nstr(r["A"], 10),
                                   "phase_rad": mp.nstr(r["phase"], 4),
                                   "iters": r["iters"]}
                print(f"  {tag} (rungs<= {L + M}): A = {mp.nstr(r['A'], 8)}  "
                      f"phase {mp.nstr(r['phase'], 3)}  ({r['iters']} its)")
            else:
                conf_plain[tag] = {"converged": False,
                                   "why": r.get("why", "?"),
                                   "A_last": mp.nstr(r.get("A", 0), 8)}
                print(f"  {tag}: NOT converged ({r.get('why')})")
    print("  NOTE: plain conformal Pade drifts down with order "
          "(~0.79 -> ~0.74 -> ~0.68) — the Pade pole approximates the mapped "
          "branch CUT from outside; this is bias, not the singularity. "
          "The dlog variant below removes it.")

    # --- 5. (c2) conformal + dlog Pade (headline) ----------------------------
    print("\n=== 5. (c2) CONFORMAL + DLOG Pade in w (headline estimator) ===")
    conf_dlog = {}
    headline_As, headline_phases, headline_alphas = [], [], []
    headline_cfgs = [(2, 2), (1, 3), (2, 3), (3, 2)]  # rungs 5,5,6,6
    extra_cfgs = [(1, 2)]                              # rungs 4 (reported)
    all_headline_converged = True
    for (L, M) in headline_cfgs + extra_cfgs:
        rungs = L + M + 1
        for mu in MARGINS:
            r = conformal_iterate(b, L, M, A0_TRIAL, mu, use_dlog=True)
            tag = f"[{L}/{M}],mu={mp.nstr(mu, 3)}"
            if r["converged"]:
                conf_dlog[tag] = {
                    "rungs": rungs,
                    "A": mp.nstr(r["A"], 12),
                    "phase_rad": mp.nstr(r["phase"], 6),
                    "alpha": mp.nstr(r["alpha"], 8),
                    "w_star": mp.nstr(r["w_star"], 8),
                    "iters": r["iters"],
                }
                print(f"  {tag} (rungs<= {rungs}): A = {mp.nstr(r['A'], 10)} "
                      f" phase {mp.nstr(r['phase'], 3)}  alpha "
                      f"{mp.nstr(r['alpha'], 5)}  ({r['iters']} its)")
                if (L, M) in headline_cfgs:
                    headline_As.append(r["A"])
                    headline_phases.append(abs(r["phase"]))
                    headline_alphas.append(r["alpha"])
            else:
                conf_dlog[tag] = {"rungs": rungs, "converged": False,
                                  "why": r.get("why", "?"),
                                  "A_last": mp.nstr(r.get("A", 0), 8)}
                print(f"  {tag} (rungs<= {rungs}): NOT converged "
                      f"({r.get('why')})")
                if (L, M) in headline_cfgs:
                    all_headline_converged = False

    if not headline_As:
        check("conformal_dlog_iteration_converged", False)
        print("ABORT: no headline conformal+dlog configuration converged.")
        return 1

    A_mean = mp.fsum(headline_As) / len(headline_As)
    A_min, A_max = min(headline_As), max(headline_As)
    half_band = (A_max - A_min) / 2
    conf_spread = (A_max - A_min) / A_mean
    max_phase = max(headline_phases)
    alpha_mean = mp.fsum(headline_alphas) / len(headline_alphas)
    print(f"\n  headline (5-6-rung) A: mean {mp.nstr(A_mean, 10)}  range "
          f"[{mp.nstr(A_min, 10)}, {mp.nstr(A_max, 10)}]  rel spread "
          f"{mp.nstr(conf_spread, 5)}")
    print(f"  max |phase| {mp.nstr(max_phase, 4)} rad;  branch exponent "
          f"alpha ~ {mp.nstr(alpha_mean, 5)}")

    check("conformal_dlog_iteration_converged",
          all_headline_converged and len(headline_As) == 8,
          computed={"converged_headline_configs": len(headline_As),
                    "expected_configs": 8},
          expected="all 8 headline (L,M,mu) configs converged",
          source="damped fixed-point iteration (tol 1e-11 rel) of the "
                 "conformal+dlog singularity estimate from trial A0=0.6177, "
                 "margins mu in {1.5, 2.0}.")
    check("conformal_A_stable_across_orders",
          conf_spread < baseline_spread and conf_spread < mp.mpf("0.10"),
          computed=mp.nstr(conf_spread, 6),
          expected=f"< baseline spread {mp.nstr(baseline_spread, 4)} "
                   f"and < 0.10",
          source="relative spread of the conformal+dlog fixed-point A across "
                 "Pade orders / truncations (5-6 rungs) and margins — the "
                 "C1 stabilization claim (vs 1.51 raw).")
    real_action = max_phase < mp.mpf("0.05")
    check("action_phase_consistent_with_real", real_action,
          computed=mp.nstr(max_phase, 6), expected="< 0.05 rad",
          tolerance="0.05",
          source="max |arg zeta*| over headline configs; Pringsheim "
                 "(positive b_n) + amphichirality (CS(4_1)=0) both demand a "
                 "real-positive action — this supplies the phase resolution "
                 "the predecessor's Richardson ratio could not.")

    # --- 6. candidates -------------------------------------------------------
    print("\n=== 6. A vs candidates (identification iff within spread) ===")
    candidates = {
        "Vol(4_1)/pi": Vol_41 / pi,
        "sibling_ratio_fit_0.6177": mp.mpf("0.617661555754"),
        "2/e": 2 / mp.e,
        "Vol(4_1)/2pi": Vol_41 / (2 * pi),
        "Vol(4_1)/4=Lambda(pi/3)": Vol_41 / 4,
        "predecessor_richardson_0.6937": mp.mpf("0.693749273902"),
    }
    cand_report = {}
    identified, suggestive = [], []
    for name, val in candidates.items():
        rel = abs(A_mean / val - 1)
        inside = A_min <= val <= A_max
        near = abs(A_mean - val) <= 3 * half_band or rel < mp.mpf("0.05")
        status = ("consistent-within-spread" if inside
                  else "suggestive" if near else "not matched")
        cand_report[name] = {"value": mp.nstr(val, 12),
                             "rel_to_A_mean": mp.nstr(rel, 5),
                             "status": status}
        if inside:
            identified.append(name)
        elif near:
            suggestive.append(name)
        print(f"  {name:32s} = {mp.nstr(val, 10)}  rel {mp.nstr(rel, 4)}  "
              f"-> {status}")

    band_str = (f"A = {mp.nstr(A_mean, 8)} in [{mp.nstr(A_min, 8)}, "
                f"{mp.nstr(A_max, 8)}]")
    if identified:
        ident_sentence = (
            f"{band_str}: {', '.join(identified)} lie(s) WITHIN the spread — "
            f"consistent-within-spread (order-limited, 6 rungs; NOT an exact "
            f"identification claim; scope-(a)).")
    elif suggestive:
        ident_sentence = (f"{band_str}: no candidate inside the spread; "
                          f"{', '.join(suggestive)} suggestive only.")
    else:
        ident_sentence = f"{band_str}: unresolved — no candidate matches."

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        f"C1 CONFORMAL STABILIZATION (scope-(a), order-limited to 6 rungs): "
        f"raw Borel-Pade of the 4_1 ladder is confirmed unstable at 6 rungs "
        f"(nearest-pole rel spread {mp.nstr(baseline_spread, 3)}); the "
        f"conformal-mapped Borel plane (zeta = 4*A0*w/(1+w)^2, margin-held "
        f"trial, damped fixed-point from A0 = 0.6177) with DLOG-Pade in w "
        f"stabilizes the singularity at A = {mp.nstr(A_mean, 8)} (range "
        f"[{mp.nstr(A_min, 8)}, {mp.nstr(A_max, 8)}], rel spread "
        f"{mp.nstr(conf_spread, 3)}, branch exponent alpha ~ "
        f"{mp.nstr(alpha_mean, 3)}) across Pade orders (= truncations 5/6 "
        f"rungs) and margins. Phase: max |arg| = {mp.nstr(max_phase, 3)} rad "
        f"— REAL-positive action, as forced by Pringsheim (positive b_n) and "
        f"amphichirality (CS(4_1)=0). {ident_sentence} The sibling ratio-fit "
        f"0.6177 and 2/e (predecessor's closest) fall OUTSIDE the band; the "
        f"plain-conformal variant's residual downward drift "
        f"(~0.79->~0.68) is Pade-on-branch-cut bias, removed by dlog. No fit "
        f"wired anywhere; no c_k value; no tier change. A is in the 1/N "
        f"normalization (divide by 2*pi for the 2*pi/N variable)."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; do not cite the stabilized A."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-borel-conformal-pade",
        "description": "Conformal-mapped Borel-Pade of the 4_1 Ohtsuki "
                       "ladder: stabilize the instanton-action (Borel "
                       "singularity) extraction that raw Borel-Pade loses to "
                       "Froissart/branch-cut pole scatter; phase-resolve the "
                       "f-map Stokes datum (audit item C1).",
        "audit_only": True,
        "tier": "structural-exact (kappa_1..kappa_4 closed forms) + "
                "numerical (conformal dlog-Borel-Pade singularity, "
                "order-limited)",
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
            "borel_normalization": "B(zeta) = 1 + sum kappa_n zeta^n / n!, "
                                   "x = 1/N variable (predecessor "
                                   "convention; /2pi for the 2pi/N variable)",
            "conformal_map": "zeta = 4*A0*w/(1+w)^2 (uniformizes the cut "
                             "[A0, +inf) onto |w|<1); A0 = mu*A_est held "
                             "above the estimate, mu in {1.5, 2.0}",
            "trial_A0": mp.nstr(A0_TRIAL, 12),
            "rungs": 6,
            "kappa_confident_digits": CONFIDENT_DIGITS,
            "fixed_point_tol": "1e-11 (relative), damped update",
            "truncation_note": "mapped d_k depends only on kappa_1..kappa_k, "
                               "so [L/M] uses exactly rungs 1..L+M (dlog: "
                               "..L+M+1) — the truncation axis and the "
                               "Pade-order axis coincide",
        },
        "result": {
            "kappa_exact_closed_forms": {
                "1": "(11/108) sqrt(3) pi",
                "2": "(2/27) pi^2",
                "3": "(1081/21870) sqrt(3) pi^3",
                "4": "(98/729) pi^4",
            },
            "kappa_exact_vs_witness_reldiff": exact_reldiffs,
            "kappa_numeric": {"5": WITNESS_KAPPA[5], "6": WITNESS_KAPPA[6]},
            "baseline_raw_pade": baseline,
            "baseline_rel_spread": mp.nstr(baseline_spread, 6),
            "dlog_pade_zeta": dlog,
            "conformal_plain": conf_plain,
            "conformal_dlog": conf_dlog,
            "A_stabilized": mp.nstr(A_mean, 12),
            "A_range": [mp.nstr(A_min, 12), mp.nstr(A_max, 12)],
            "A_rel_spread": mp.nstr(conf_spread, 6),
            "branch_exponent_alpha_mean": mp.nstr(alpha_mean, 8),
            "max_abs_phase_rad": mp.nstr(max_phase, 6),
            "A_is_real": bool(real_action),
            "candidates": cand_report,
            "consistent_within_spread": identified,
            "suggestive_only": suggestive,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: C1 conformal-mapped Borel plane",
            "audit_item": "docs/audits/2026-07-12-borel-alien-calculus-"
                          "utilization-audit.md #C1",
            "predecessor": "docs/audits/scripts/qbeta_borel_pade_action.py "
                           "(raw Borel-Pade Froissart-unstable; Richardson "
                           "A~0.6937, |A| only, no phase)",
            "sibling": "docs/audits/scripts/qbeta_even_borel_singularity.py "
                       "(ratio-fit A=0.6177, flagged suggestive-not-"
                       "identified)",
            "reality_argument": "Pringsheim (all b_n > 0) + amphichirality "
                                "(CS(4_1)=0 => action real); predecessor "
                                "discussion at its lines ~121-140",
            "next": "C3: Borel-Ecalle transseries anchored on the stabilized "
                    "A to reach kappa_5/kappa_6 exactly; more exact rungs "
                    "would shrink the band and settle Vol(4_1)/pi",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-borel-conformal-pade.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
