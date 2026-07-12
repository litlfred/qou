#!/usr/bin/env python3
"""qbeta_qsqrt3_borel_pslq_probe.py — C2 of the Borel/alien-calculus
utilization audit (docs/audits/2026-07-12-borel-alien-calculus-utilization-audit.md):
re-run the ℚ(√−3) saddle-coefficient PSLQ on BOREL-TRANSFORMED coefficients.

PREDECESSOR (refuted, scope-(a)):
docs/audits/scripts/qbeta_action_qsqrt3_saddle_probe.py extracted the 4₁
Kashaev ladder coefficients c_m = [1/N^m](log J_N − (3/2)log N) at 220 dps
(K = 9, N = 300..1180 step 40, QR least squares) and PSLQ-tested c_m raw and
c_m·m!·(2π)^m under torsion normalizations 3^{a·m}.  Its own verdict names the
Borel-shaped blocker: c_m ~ m!/A^m factorial growth (A ≈ 0.688, the Borel
singularity of #3508), so the m!-RESCALED value explodes past PSLQ's entropy
reach, and high-m fit coefficients are precision-contaminated.

THIS PROBE (C2): the Borel transform b_m = c_m/m! is O(1/A^m) — bounded — so
the stated blocker is removed.  We (1) reproduce the predecessor's extraction
exactly (same dps, same ladder, same machinery), (2) verify b_m boundedness
numerically (ratio test) BEFORE any PSLQ, (3) PSLQ each b_m against a small
ℚ(√−3)-dictated basis with a per-coefficient entropy-budget check
(PR #1805 rule: trusted digits > n_terms·log10(2·height) + margin), refusing
to over-ask and logging skipped orders explicitly, and (4) cross-check every
hit at a SECOND, independent extraction (different K, different N window)
before any wording stronger than CANDIDATE.

BASIS JUSTIFICATION (4 trial forms per order; every element sourced):
  F1  b_m                       — the predecessor's raw test, Borel side.
  F2  b_m·3^{m/2}               — the predecessor's strongest torsion
                                  normalization (3 is the ramified prime of
                                  ℚ(√−3); √−3·√−3 = −3).
  F3  b_m/π^m                   — loop order m of the Kashaev asymptotic
                                  carries π^m; established a posteriori by the
                                  exact rungs κ₁..κ₄ (#3606/#3628 on main).
  F4  b_m/(√3^{m mod 2}·π^m)    — the Lean-certified √3-parity alternation of
                                  the rungs (#3628): odd m ∈ ℚ·√3·π^m, even
                                  m ∈ ℚ·π^m.  The ℚ(√−3)-dictated primary form.

CONTROLS: κ₁..κ₄ are exact on main (κ₁ = (11/108)√3π, κ₂ = (2/27)π²,
κ₃ = (1081/21870)√3π³, κ₄ = (98/729)π⁴).  Orders m ≤ 4 therefore act as
known-answer controls: F4 must recover p/(q·m!) IF the entropy budget covers
that height; the frontier is m ≥ 5 (κ₅/κ₆ "precision-limited, not structural").

HONEST KILL CRITERIA (pre-stated):
  • no relation within budget      ⇒ NEGATIVE scope-(a) for that order — the
    coefficient stays empirical at this extraction precision; NOT a structural
    exclusion (scope-(b) would need a proved invariant).
  • relation found                 ⇒ CANDIDATE only (never "identified"), and
    only after it reproduces from the second extraction; a hit that fails the
    cross-check is logged as an entropy false positive and rejected.
  • budget < floor                 ⇒ SKIPPED, logged explicitly (no silent cap).

DISCIPLINE: audit-only witness; NO fit to QOU data; NO c_k value wired; NO
tier change; scope-(a) wording throughout.  Self-contained (mpmath only).
"""
import datetime
import hashlib
import json
import math
import os
import subprocess
import time
from fractions import Fraction

import mpmath as mp

# ----------------------------------------------------------------------------
# Configuration — extraction A reproduces the predecessor EXACTLY.
# ----------------------------------------------------------------------------
mp.mp.dps = 220                     # predecessor dps

K_A, NS_A = 9, list(range(300, 1181, 40))     # predecessor ladder (23 points)
# Extraction B: independent truncation order AND N-window, for (i) empirical
# per-coefficient trust estimation and (ii) candidate cross-checking.
K_B, NS_B = 11, list(range(380, 1301, 40))    # 24 points, 13 basis columns

PSLQ_N_TERMS = 2          # PSLQ vector is [v, 1] — a 2-term relation
TRIALS_PER_ORDER = 4      # F1..F4 above; multiple-testing margin below
BASE_MARGIN = 3.0         # safety digits on top of the raw entropy bound
H_FLOOR = 10              # below this maxcoeff a PSLQ "hit" is meaningless
DIGITS_CAP = 40           # never claim more trusted digits than this

# Predecessor's committed c_m (12 sig digits), from
# docs/audits/scripts/qbeta-action-qsqrt3-saddle-probe.witness.json — the
# reproduction gate for extraction A.
PRED_C = ["0.554216472405", "0.731081807488", "2.65452705727",
          "13.0947746575", "84.6423214763", "676.883639216",
          "6460.95965922", "68021.3438891", "1208656.02861"]

# Exact rungs on main (#3606/#3628): m -> (p, q, eps) with
# c_m = (p/q)·√3^eps·π^m.  Known-answer controls for m ≤ 4.
KNOWN_RUNGS = {1: (11, 108, 1), 2: (2, 27, 0),
               3: (1081, 21870, 1), 4: (98, 729, 0)}

T0 = time.time()


def _elapsed():
    return time.time() - T0


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


# ----------------------------------------------------------------------------
# Predecessor machinery, reused verbatim.
# ----------------------------------------------------------------------------
def log_kashaev_4_1(N):
    """log of the 4₁ Kashaev invariant J_N (predecessor implementation)."""
    pi = mp.pi
    logterms = [mp.mpf(0)]
    logP = mp.mpf(0)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N))
        logterms.append(logP)
    m = max(logterms)
    return m + mp.log(mp.fsum(mp.exp(t - m) for t in logterms))


def extract_ladder(K, Ns, tag):
    """QR least-squares fit of log J_N − (3/2)log N against
    {N, 1, 1/N, ..., 1/N^K} (predecessor method).  Returns (slope, c[1..K])."""
    total = sum(Ns)
    done = 0
    rows = []
    for N in Ns:
        rows.append((N, log_kashaev_4_1(N) - mp.mpf(3) / 2 * mp.log(N)))
        done += N
        eta = _elapsed() / done * (total - done) if done else 0.0
        print(f"  [{tag}] N={N:5d} done  elapsed={_elapsed():7.1f}s  "
              f"ETA(this ladder)={eta:6.1f}s", flush=True)

    def basis(N):
        return [mp.mpf(N), mp.mpf(1)] + [1 / mp.mpf(N) ** k
                                         for k in range(1, K + 1)]
    coef = mp.qr_solve(mp.matrix([basis(N) for N, _ in rows]),
                       mp.matrix([g for _, g in rows]))[0]
    slope = coef[0]
    c = [coef[2 + k] for k in range(K)]   # c[k] is coeff of 1/N^{k+1}
    return slope, c


# ----------------------------------------------------------------------------
# Entropy budget (PR #1805 rule): trusted digits > n_terms·log10(2·height) + margin.
# ----------------------------------------------------------------------------
def needed_digits(H, trials=TRIALS_PER_ORDER):
    """Digits required to certify a 2-term relation of height H, with a
    multiple-testing surcharge log10(trials)."""
    return PSLQ_N_TERMS * math.log10(2 * H) + BASE_MARGIN + math.log10(trials)


def budget_maxcoeff(digits, trials=TRIALS_PER_ORDER):
    """Largest height H such that needed_digits(H) <= digits (inverse of the
    bound: H = 10^((digits − margin)/n)/2)."""
    margin = BASE_MARGIN + math.log10(trials)
    if digits <= margin:
        return 0
    return int(10 ** ((digits - margin) / PSLQ_N_TERMS) / 2)


def spot_check_entropy_arithmetic():
    """In-script arithmetic spot-checks of the budget formula (hard asserts)."""
    # Hand value: n=2, H=100, trials=1, margin=3 ⇒ 2·log10(200)+3 = 7.60206…
    v = PSLQ_N_TERMS * math.log10(2 * 100) + BASE_MARGIN
    assert abs(v - 7.6020599913) < 1e-6, "entropy-bound arithmetic broken"
    # Inverse consistency: needed(budget_maxcoeff(d)) <= d for representative d.
    for d in (10, 14, 18, 25):
        H = budget_maxcoeff(d)
        assert H == 0 or needed_digits(H) <= d + 1e-9, \
            f"budget inversion over-asks at digits={d}"
    # Monotonicity: more digits ⇒ larger admissible height.
    assert budget_maxcoeff(20) > budget_maxcoeff(12) > 0
    return True


def try_pslq(v_full, digits, hmax):
    """PSLQ [v, 1] at the TRUSTED precision only (never at full working dps —
    that would ask the fit for digits it does not have).  Returns Fraction or
    None."""
    wd = max(int(digits), 15)
    with mp.workdps(wd):
        vv = +v_full          # re-round to trusted precision
        r = mp.pslq([vv, mp.mpf(1)], maxcoeff=int(hmax), maxsteps=50000)
    if not r or r[0] == 0:
        return None
    return Fraction(-r[1], r[0])


def rel_err(v, frac):
    q = mp.mpf(frac.numerator) / mp.mpf(frac.denominator)
    return abs(v - q) / abs(v)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed),
                           **({"detail": detail} if detail else {})})
        print(f"  assert {name}: {'PASS' if passed else 'FAIL'}"
              + (f"  ({detail})" if detail else ""), flush=True)

    print(f"extraction A (predecessor-identical): dps={mp.mp.dps}, K={K_A}, "
          f"N={NS_A[0]}..{NS_A[-1]} step 40", flush=True)
    slope_A, c_A = extract_ladder(K_A, NS_A, "A")
    print(f"extraction B (independent): K={K_B}, N={NS_B[0]}..{NS_B[-1]} "
          f"step 40", flush=True)
    slope_B, c_B = extract_ladder(K_B, NS_B, "B")

    # --- Sanity: Vol(4₁) from the slope (predecessor check). ---------------
    Vol = 2 * mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3)))
    vol_rel = abs(2 * mp.pi * slope_A / Vol - 1)
    check("vol41_recovered", vol_rel < mp.mpf(10) ** (-15),
          f"rel err {mp.nstr(vol_rel, 3)}")

    # --- Reproduction gate: extraction A == predecessor witness. -----------
    rep_max = max(abs(c_A[k] / mp.mpf(PRED_C[k]) - 1) for k in range(K_A))
    check("predecessor_extraction_reproduced", rep_max < mp.mpf("1e-9"),
          f"max rel diff vs committed 12-digit c_m = {mp.nstr(rep_max, 3)}")

    # --- Per-coefficient empirical trust (A vs B agreement). ---------------
    trust = {}
    for k in range(K_A):
        m = k + 1
        d = abs(c_A[k] - c_B[k]) / abs(c_A[k])
        dg = DIGITS_CAP if d == 0 else min(DIGITS_CAP,
                                           int(mp.floor(-mp.log10(d))))
        trust[m] = max(dg, 0)
    print("  trusted digits per order (A-vs-B agreement): "
          + ", ".join(f"c_{m}:{trust[m]}" for m in sorted(trust)), flush=True)

    # --- Borel transform + boundedness (BEFORE any PSLQ). ------------------
    b_A = {m: c_A[m - 1] / mp.factorial(m) for m in range(1, K_A + 1)}
    b_B = {m: c_B[m - 1] / mp.factorial(m) for m in range(1, K_A + 1)}
    b_ratios = {m: float(b_A[m] / b_A[m - 1]) for m in range(2, K_A + 1)}
    c_ratios = {m: float(c_A[m - 1] / c_A[m - 2]) for m in range(2, K_A + 1)}
    # m = 9 is the last, most truncation-contaminated coefficient (the
    # predecessor's own c_9/c_8 ratio 17.8 is a fit artifact); the bounded-
    # ness assertion covers m ≤ 8 and m = 9 is reported alongside.
    bounded_max = max(b_ratios[m] for m in range(2, 9))
    check("borel_bm_bounded_ratio_test", bounded_max < 3.0,
          f"max |b_m/b_(m-1)| (m=2..8) = {bounded_max:.3f} "
          f"(expected → 1/A ≈ 1.44; factorial growth removed)")
    assert bounded_max < 3.0, "b_m not bounded — Borel premise fails, abort"
    a_est = 1.0 / (sum(b_ratios[m] for m in (6, 7, 8)) / 3.0)
    print(f"  ratio-test Borel radius estimate: A ≈ {a_est:.4f} "
          f"(predecessor large-order value ≈ 0.688–0.694)", flush=True)

    # --- Entropy-budget arithmetic spot-check (hard asserts). --------------
    check("entropy_budget_arithmetic_spot_check",
          spot_check_entropy_arithmetic(),
          "needed(H=100,n=2,T=1,m=3)=7.60206 ok; inversion+monotonicity ok")

    # --- Known-rung direct validation (controls, m ≤ 4). -------------------
    sqrt3, pi = mp.sqrt(3), mp.pi
    known_ok = True
    for m, (p, q, eps) in KNOWN_RUNGS.items():
        exact = mp.mpf(p) / q * sqrt3 ** eps * pi ** m
        r = abs(c_A[m - 1] - exact) / abs(exact)
        ok = r < mp.mpf(10) ** (-(max(trust[m] - 2, 4)))
        known_ok &= ok
        print(f"  control c_{m} vs exact rung ({p}/{q})·√3^{eps}·π^{m}: "
              f"rel diff {mp.nstr(r, 3)} -> {'ok' if ok else 'MISMATCH'}",
              flush=True)
    check("known_rungs_m1_m4_match_extraction", known_ok,
          "extraction agrees with #3606/#3628 exact κ₁..κ₄ at trust level")

    # --- Per-order PSLQ with per-coefficient entropy budget. ---------------
    def forms(m, b):
        return [
            ("F1 raw b_m", b),
            ("F2 b_m*3^(m/2)", b * mp.mpf(3) ** (mp.mpf(m) / 2)),
            ("F3 b_m/pi^m", b / pi ** m),
            ("F4 b_m/(sqrt3^(m%2)*pi^m)", b / (sqrt3 ** (m % 2) * pi ** m)),
        ]

    per_order = []
    budget_respected = True
    for m in range(1, K_A + 1):
        dg = trust[m]
        hmax = budget_maxcoeff(dg)
        row = {"order": m, "b_m": mp.nstr(b_A[m], 15),
               "trusted_digits": dg, "budget_maxcoeff": hmax}
        if hmax < H_FLOOR:
            row["outcome"] = "SKIPPED"
            row["reason"] = (f"entropy budget: {dg} trusted digits admit "
                             f"height ≤ {hmax} < floor {H_FLOOR} — refusing "
                             f"to over-ask (order logged, not silently capped)")
            print(f"  m={m}: SKIPPED — {row['reason']}", flush=True)
            per_order.append(row)
            continue
        # Structural budget guard: the maxcoeff we hand PSLQ must satisfy the
        # bound at this order's trust.
        budget_respected &= (needed_digits(hmax) <= dg + 1e-9)

        hit = None
        for fname, vfull in forms(m, b_A[m]):
            frac = try_pslq(vfull, dg, hmax)
            if frac is None:
                continue
            ra = rel_err(vfull, frac)
            if ra >= mp.mpf(10) ** (-(dg - 2)):
                continue      # PSLQ artifact, not a relation at trust level
            hit = (fname, frac, ra)
            break
        if hit is None:
            row["outcome"] = "NEGATIVE"
            row["scope"] = ("scope-(a): no ℚ(√−3)-basis relation within the "
                            f"entropy budget (H ≤ {hmax}) at {dg} trusted "
                            "digits — b_%d stays empirical at this extraction "
                            "precision; not a structural exclusion" % m)
            if m in KNOWN_RUNGS:
                p, q, _ = KNOWN_RUNGS[m]
                exp_frac = Fraction(p, q * math.factorial(m))
                h_known = max(abs(exp_frac.numerator), exp_frac.denominator)
                row["known_rung_height"] = h_known
                row["budget_explained"] = bool(needed_digits(h_known) > dg)
                row["note"] = (f"known rung κ_{m}/{m}! = {exp_frac} has "
                               f"height {h_known}, needing "
                               f"{needed_digits(h_known):.1f} digits > {dg} "
                               "trusted — the negative is budget-explained, "
                               "NOT a contradiction of #3606/#3628")
            print(f"  m={m}: NEGATIVE within budget H≤{hmax} @ {dg} digits"
                  + (f"  [{row['note']}]" if "note" in row else ""),
                  flush=True)
            per_order.append(row)
            continue

        fname, frac, ra = hit
        # Cross-check against the independent extraction B.
        vB = dict(forms(m, b_B[m]))[fname]
        rb = rel_err(vB, frac)
        xchk = rb < mp.mpf(10) ** (-(max(dg - 3, 4)))
        row["hit_form"] = fname
        row["hit_rational"] = f"{frac.numerator}/{frac.denominator}"
        row["rel_err_A"] = mp.nstr(ra, 3)
        row["rel_err_B"] = mp.nstr(rb, 3)
        row["crosscheck_passed"] = bool(xchk)
        if not xchk:
            row["outcome"] = "FALSE-POSITIVE-REJECTED"
            row["reason"] = ("relation does not reproduce from the second "
                             "extraction — #3571-class entropy false positive")
        elif m in KNOWN_RUNGS and (fname.startswith("F4") or
                                   (fname.startswith("F3") and m % 2 == 0)):
            # For even m, F3 = F4 (√3^0 = 1): a F3 hit is the parity form.
            p, q, eps = KNOWN_RUNGS[m]
            expected = Fraction(p, q * math.factorial(m))
            if frac == expected:
                row["outcome"] = "VALIDATED-CONTROL"
                row["reason"] = (f"recovers the known exact rung κ_{m}/{m}! = "
                                 f"{expected} (#3606/#3628) within budget")
            else:
                row["outcome"] = "FALSE-POSITIVE-REJECTED"
                row["reason"] = (f"cross-checked hit {frac} contradicts the "
                                 f"known exact rung {expected} — rejected")
        else:
            row["outcome"] = "CANDIDATE"
            row["reason"] = ("relation reproduces at a second, independent "
                             "extraction — CANDIDATE only, NOT identified; "
                             "confirmation requires the exact Ohtsuki saddle "
                             "recursion or a higher-precision extraction")
        print(f"  m={m}: {row['outcome']} — {fname} = "
              f"{row['hit_rational']} (relA {row['rel_err_A']}, "
              f"relB {row['rel_err_B']})", flush=True)
        per_order.append(row)

    check("entropy_budget_never_exceeded", budget_respected,
          "every PSLQ maxcoeff satisfied needed_digits(H) <= trusted digits")

    # --- Verdict. -----------------------------------------------------------
    outcomes = {r["order"]: r["outcome"] for r in per_order}
    n_ctrl = sum(1 for o in outcomes.values() if o == "VALIDATED-CONTROL")
    n_cand = sum(1 for o in outcomes.values() if o == "CANDIDATE")
    n_neg = sum(1 for o in outcomes.values() if o == "NEGATIVE")
    n_skip = sum(1 for o in outcomes.values() if o == "SKIPPED")
    n_fp = sum(1 for o in outcomes.values()
               if o == "FALSE-POSITIVE-REJECTED")
    verdict = (
        "C2 RESULT (Borel-transformed ℚ(√−3) PSLQ, scope-(a) wording): the "
        f"Borel transform b_m = c_m/m! is numerically bounded (max ratio "
        f"{bounded_max:.2f}, → 1/A), removing the predecessor's stated "
        f"entropy blocker. Under per-coefficient entropy budgets: "
        f"{n_ctrl} known-answer control(s) re-derived (m ≤ 4 exact rungs), "
        f"{n_cand} CANDIDATE(s) (reproduced at a second extraction; NOT "
        f"identified), {n_fp} entropy false positive(s) rejected, "
        f"{n_neg} NEGATIVE (no relation within budget — those b_m stay "
        f"empirical at this extraction precision; scope-(a), not a "
        f"structural exclusion), {n_skip} SKIPPED (budget below floor, "
        f"logged). No fit; no c_k value; no wiring; no tier change. The "
        f"exact route past the frontier remains the Ohtsuki state-integral "
        f"saddle recursion / bridge equation (audit §2.G2), not deeper PSLQ.")
    print("\nVERDICT:", verdict, flush=True)

    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-qsqrt3-borel-pslq",
        "description": "C2 (Borel/alien-calculus audit): re-run of the "
                       "refuted ℚ(√−3) saddle-coefficient PSLQ on "
                       "Borel-transformed b_m = c_m/m! (bounded, "
                       "PSLQ-tractable) with per-coefficient entropy "
                       "budgets and second-extraction cross-checks.",
        "auditOnly": True,
        "tier": "numerical (hypothesis-class test; no value fit)",
        "computedAt": datetime.datetime.now(
            datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "durationMs": int(_elapsed() * 1000),
        "precisionMetadata": {
            "extraction_dps": EXTRACT_DPS_ACTUAL,
            "extraction_A": {"K": K_A, "N_range": [NS_A[0], NS_A[-1], 40],
                             "note": "predecessor-identical"},
            "extraction_B": {"K": K_B, "N_range": [NS_B[0], NS_B[-1], 40],
                             "note": "independent window + truncation order"},
            "entropy_bound": "digits > n_terms*log10(2*height) + 3 + "
                             "log10(trials); n_terms=2, trials=4 (PR #1805)",
        },
        "assertions": assertions,
        "allPassed": all_passed,
        "data": {
            "c_m_extraction_A": [mp.nstr(x, 15) for x in c_A],
            "b_m": [mp.nstr(b_A[m], 15) for m in range(1, K_A + 1)],
            "c_ratios": {str(m): round(c_ratios[m], 3)
                         for m in sorted(c_ratios)},
            "b_ratios": {str(m): round(b_ratios[m], 4)
                         for m in sorted(b_ratios)},
            "borel_radius_ratio_estimate_A": round(a_est, 4),
            "trusted_digits": {str(m): trust[m] for m in sorted(trust)},
            "per_order": per_order,
            "verdict": verdict,
        },
        "scope_classification": {
            "negatives": "scope-(a) — no relation within the entropy budget "
                         "at this extraction precision; ingredient NOT "
                         "structurally excluded",
            "hits": "CANDIDATE at most — cross-checked at a second "
                    "extraction, still requires the exact Ohtsuki saddle "
                    "recursion for identification",
            "controls": "m<=4 known exact rungs (#3606/#3628) used as "
                        "known-answer controls",
        },
        "context": {
            "axis": "z->c_k f-map keystone: even-channel action, ℚ(√−3) "
                    "saddle — Borel transform side",
            "audit_item": "docs/audits/2026-07-12-borel-alien-calculus-"
                          "utilization-audit.md §1.C2",
            "predecessor": "docs/audits/scripts/"
                           "qbeta_action_qsqrt3_saddle_probe.py "
                           "(REFUTED scope-(a): m!-rescale entropy blocked)",
            "exact_rungs": "κ₁=(11/108)√3π, κ₂=(2/27)π², "
                           "κ₃=(1081/21870)√3π³, κ₄=(98/729)π⁴ "
                           "(#3606/#3628, main)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-qsqrt3-borel-pslq.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out, flush=True)
    return 0


EXTRACT_DPS_ACTUAL = mp.mp.dps

if __name__ == "__main__":
    raise SystemExit(main())
