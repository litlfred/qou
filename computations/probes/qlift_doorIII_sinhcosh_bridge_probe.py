#!/usr/bin/env python3
"""Door-iii: sinh/cosh (bar-even/odd) NON-MODULE bridge C1^2 -> GGM eq 49.

Bean qou-ceg6.  Follow-up to the five-route gauge-gap synthesis
(docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md) + Door-i analytic
summation (docs/audits/2026-07-20-qlift-doorI-analytic-summation.md), which
proved -- with a permanent invariant (ISOCLINICITY) -- that C1 and GGM are
inequivalent q-difference MODULES under every meromorphic gauge, formal
q-Borel weight, analytic q-summation, and ramified pullback.  Door-i
explicitly left ONE carve-out live: NON-module maps (sequence-level
identifications not induced by a q-difference morphism).  This probe attacks
exactly that carve-out with the owner's insight:

  HYPOTHESIS.  GGM's two solutions are the bar-EVEN (cosh) and bar-ODD (sinh)
  combinations of the SYMMETRIC SQUARES of the C1 solutions.  Schematically
  GGM_solution ~ {f.g} with f,g in the 2-dim C1 space (products of slope-1/2
  -> slope-1), split into bar-even/bar-odd (q -> 1/q) pieces.  Slope
  arithmetic sanity (pre-checked): GGM slope-1 solutions grow q^{m^2/2};
  C1 slope-1/2 solutions grow q^{+-m^2/4}; 2*(1/2) = 1.

Recursions (state index m):
  C1  (proved q-lift): [m+2]_q b_{m+2} = b_{m+1} + b_m,  [n]_q=(q^n-1)/(q-1)
  GGM (eq 49, arXiv:2012.00062 p.14): y_{m+1} = (2 - q^m) y_m - y_{m-1}

Bar involution: q -> 1/q (bar-even = invariant, bar-odd = anti-invariant).
"C1 solutions bar-conjugate" = the same recursion re-run at parameter 1/q.

This is a NON-MODULE correspondence by design (Door-i proved no module map
exists).  So 'CONSISTENT' does NOT mean a module iso -- it means an EXPLICIT,
m-INDEPENDENT, q-dependent linear combination of the sym^2 (and bar-sym^2)
sequences reproduces each GGM solution to machine precision, and keeps doing
so far outside the fit window.  That would be the FIRST positive C1<->GGM
link and would re-frame the whole gauge gap (Door-i's carve-out realized).

KILL CRITERION (pre-stated, per AGENTS.md refuted-discipline):
  For a GGM solution y and candidate basis S (columns = sym^2 / bar-sym^2
  sequences), fit a fixed coefficient vector c on a low-m window, then form
  the EXTRAPOLATION residual  R = max_{m in tail} |y_m - (S c)_m| / |y_m|.
    * R < 1e-40  over the tail  =>  CONSISTENT bridge (scope-(a) POSITIVE:
        the explicit combination reproduces GGM at these q).
    * R = O(1)  (drift, no fixed combo extrapolates)  =>  REFUTED at these q
        (scope-(a): this sym^2/bar-even-odd construction, ALONE, does not
        reproduce GGM's forward solutions).  Report the leading behaviour of
        the true residual honestly.
  NO scope-(b) structural-exclusion claim is made here (that is Door-i's job,
  already done with the isoclinicity invariant); this probe only measures
  whether the specific non-module combination lands.

Two complementary tests:
  TEST A -- FORWARD GGM (task step 2).  6-column basis {f+^2, f+f-, f-^2}
    (unbarred, forward C1 sym^2) U {fb+^2, fb+fb-, fb-^2} (bar, C1 at 1/q).
    Least-squares fit each forward GGM solution (y_a IC (1,0), y_b IC (0,1))
    on m in [0, N_FIT], extrapolate to the tail.  The fitted coefficient
    vector is split into its bar-even (unbarred==barred coeff) and bar-odd
    parts and reported.
  TEST B -- RECESSIVE GGM via Miller / backward recursion (task step 3, the
    slope-matched clean framing).  GGM's minimal (forward-decaying) solution
    -- the slope that MATCHES the forward-decaying C1 sym^2 products -- is
    extracted by backward recursion from m = M_MILLER, then tested against the
    3-column unbarred sym^2 basis {f+^2, f+f-, f-^2} alone.  This is where a
    genuine cosh/sinh landing would live: y_rec =? a f+^2 + b f+f- + c f-^2.
    We also form cosh=(g+gbar)/2, sinh=(g-gbar)/2 for the fitted g and report
    which (if any) equals a GGM solution.

mpmath dps=60.  No AME data; no experimental fit; the only 'fit' is the
pre-stated m-independent linear coefficient solve whose whole purpose is the
extrapolation kill-test above.

Run:  python3 -u computations/probes/qlift_doorIII_sinhcosh_bridge_probe.py \
          2>&1 | tee /tmp/qlift-doorIII.log
Emits: qlift_doorIII_sinhcosh_bridge_probe.witness.json (same directory).
"""

import json
import os
from datetime import datetime, timezone

import mpmath
from mpmath import mp, mpf, log, fabs

mp.dps = 60

M_MAX = 50                       # solution index m = 0..50 (task spec)
N_FIT = 14                       # fit window m = 0..N_FIT (low m)
TAIL = list(range(34, M_MAX + 1))  # extrapolation window (disjoint from fit)
M_MILLER = 140                   # backward-recursion start for the minimal solution
Q_LIST = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]
TOL_CONSISTENT = mpf("1e-40")


def q_int(n, q):
    """q-integer [n]_q = (q^n - 1)/(q - 1); [n]_1 = n."""
    if q == 1:
        return mpf(n)
    return (q ** n - 1) / (q - 1)


def c1_solutions(q, M):
    """Two independent C1 solutions from IC (1,0) and (0,1). Returns (fp, fm)."""
    fp = [mpf(0)] * (M + 1)
    fm = [mpf(0)] * (M + 1)
    fp[0], fp[1] = mpf(1), mpf(0)
    fm[0], fm[1] = mpf(0), mpf(1)
    for m in range(0, M - 1):
        d = q_int(m + 2, q)
        fp[m + 2] = (fp[m + 1] + fp[m]) / d
        fm[m + 2] = (fm[m + 1] + fm[m]) / d
    return fp, fm


def ggm_forward(q, M):
    """Two independent forward GGM solutions from IC (1,0) and (0,1)."""
    ya = [mpf(0)] * (M + 1)
    yb = [mpf(0)] * (M + 1)
    ya[0], ya[1] = mpf(1), mpf(0)
    yb[0], yb[1] = mpf(0), mpf(1)
    for m in range(1, M):
        c = 2 - q ** m
        ya[m + 1] = c * ya[m] - ya[m - 1]
        yb[m + 1] = c * yb[m] - yb[m - 1]
    return ya, yb


def ggm_recessive(q, M, M_start):
    """GGM minimal (forward-decaying) solution via backward recursion (Miller).
    Backward: y_{m-1} = (2 - q^m) y_m - y_{m+1}. Seed y_{M_start+1}=0, y_{M_start}=1;
    backward recursion amplifies -> converges to the forward-minimal solution.
    Returns list y[0..M] normalized so that the largest |y_m| on [0,M] is 1."""
    y = [mpf(0)] * (M_start + 2)
    y[M_start + 1] = mpf(0)
    y[M_start] = mpf(1)
    for m in range(M_start, 0, -1):
        y[m - 1] = (2 - q ** m) * y[m] - y[m + 1]
    seg = [y[m] for m in range(0, M + 1)]
    scale = max((fabs(v) for v in seg), default=mpf(1))
    if scale == 0:
        scale = mpf(1)
    return [v / scale for v in seg]


def elementwise(a, b):
    return [a[i] * b[i] for i in range(len(a))]


def col_scaled_lstsq(cols, target, fit_ms):
    """Least-squares solve  min || S c - t ||  over rows fit_ms, with per-column
    scaling for conditioning. cols: list of full sequences; returns coeff vector
    c (in ORIGINAL, unscaled column units)."""
    ncol = len(cols)
    # scale each column by max |value| over the fit window (avoid 0)
    scales = []
    for col in cols:
        s = max((fabs(col[m]) for m in fit_ms), default=mpf(1))
        scales.append(s if s != 0 else mpf(1))
    A = mpmath.matrix(len(fit_ms), ncol)
    b = mpmath.matrix(len(fit_ms), 1)
    for i, m in enumerate(fit_ms):
        for j in range(ncol):
            A[i, j] = cols[j][m] / scales[j]
        b[i, 0] = target[m]
    # normal equations (mpmath dps=60 tolerates the conditioning at this size)
    AT = A.T
    G = AT * A
    rhs = AT * b
    csc = mp.lu_solve(G, rhs)
    return [csc[j, 0] / scales[j] for j in range(ncol)]


def extrapolation_residual(cols, coeffs, target, test_ms):
    """max relative residual |target_m - sum_j coeffs_j cols_j[m]| / |target_m|."""
    worst = mpf(0)
    worst_abs = mpf(0)
    for m in test_ms:
        pred = mpf(0)
        for j, col in enumerate(cols):
            pred += coeffs[j] * col[m]
        num = fabs(target[m] - pred)
        den = fabs(target[m])
        rel = num / den if den != 0 else num
        if rel > worst:
            worst = rel
        if num > worst_abs:
            worst_abs = num
    return worst, worst_abs


def leading_log_slope(seq, q, ms):
    """Estimate second difference of log|seq| / log q over ms -> theta exponent
    (q^{gamma m^2}); and first difference / log q -> effective degree."""
    L = {}
    for m in ms:
        v = fabs(seq[m])
        L[m] = log(v) / log(q) if v != 0 else None
    ms_ok = [m for m in ms if L[m] is not None and (m + 1) in L
             and (m + 2) in L and L[m + 1] is not None and L[m + 2] is not None]
    if not ms_ok:
        return None, None
    d1 = [(L[m + 1] - L[m]) for m in ms_ok]
    d2 = [(L[m + 2] - 2 * L[m + 1] + L[m]) for m in ms_ok]
    deg = sum(d1) / len(d1)
    gamma = (sum(d2) / len(d2)) / 2
    return deg, gamma


def analyze_q(q):
    fp, fm = c1_solutions(q, M_MAX)
    fbp, fbm = c1_solutions(1 / q, M_MAX)     # bar = q -> 1/q
    ya, yb = ggm_forward(q, M_MAX)

    # sym^2 candidates
    Sp = elementwise(fp, fp)          # f+^2
    Spm = elementwise(fp, fm)         # f+ f-
    Sm = elementwise(fm, fm)          # f-^2
    Bp = elementwise(fbp, fbp)        # fb+^2
    Bpm = elementwise(fbp, fbm)       # fb+ fb-
    Bm = elementwise(fbm, fbm)        # fb-^2
    cols6 = [Sp, Spm, Sm, Bp, Bpm, Bm]
    cols3 = [Sp, Spm, Sm]

    fit_ms = list(range(0, N_FIT + 1))

    # ---- TEST A: forward GGM solutions vs 6-column sym^2 U bar-sym^2 ----
    testA = {}
    for name, tgt in (("y_a", ya), ("y_b", yb)):
        try:
            c = col_scaled_lstsq(cols6, tgt, fit_ms)
            rrel, rabs = extrapolation_residual(cols6, c, tgt, TAIL)
            # bar-even / bar-odd split of the fitted coefficients
            even = [(c[0] + c[3]) / 2, (c[1] + c[4]) / 2, (c[2] + c[5]) / 2]
            odd = [(c[0] - c[3]) / 2, (c[1] - c[4]) / 2, (c[2] - c[5]) / 2]
            consistent = rrel < TOL_CONSISTENT
            testA[name] = {
                "coeffs": [mp.nstr(x, 8) for x in c],
                "bar_even": [mp.nstr(x, 8) for x in even],
                "bar_odd": [mp.nstr(x, 8) for x in odd],
                "tail_rel_residual": mp.nstr(rrel, 6),
                "tail_abs_residual": mp.nstr(rabs, 6),
                "consistent": bool(consistent),
            }
        except Exception as e:  # noqa: BLE001
            testA[name] = {"error": repr(e)}

    # ---- TEST B: recessive GGM (Miller) vs 3-column unbarred sym^2 ----
    rec = ggm_recessive(q, M_MAX, M_MILLER)
    # sanity: recessive solution satisfies the GGM recursion internally
    rec_res = mpf(0)
    for m in range(1, M_MAX - 1):
        lhs = rec[m + 1] - (2 - q ** m) * rec[m] + rec[m - 1]
        sc = max(fabs(rec[m + 1]), fabs(rec[m]), fabs(rec[m - 1]), mpf(1))
        rec_res = max(rec_res, fabs(lhs) / sc)
    testB = {"recessive_recursion_residual": mp.nstr(rec_res, 6)}
    try:
        c3 = col_scaled_lstsq(cols3, rec, fit_ms)
        rrel3, rabs3 = extrapolation_residual(cols3, c3, rec, TAIL)
        consistent3 = rrel3 < TOL_CONSISTENT
        # also try 6-col on recessive
        c6r = col_scaled_lstsq(cols6, rec, fit_ms)
        rrel6, rabs6 = extrapolation_residual(cols6, c6r, rec, TAIL)
        testB.update({
            "coeffs_sym2_3": [mp.nstr(x, 8) for x in c3],
            "tail_rel_residual_3col": mp.nstr(rrel3, 6),
            "tail_rel_residual_6col": mp.nstr(rrel6, 6),
            "consistent_3col": bool(consistent3),
            "consistent_6col": bool(rrel6 < TOL_CONSISTENT),
        })
    except Exception as e:  # noqa: BLE001
        testB["error"] = repr(e)

    # ---- growth-class diagnostics (context, not a pass/fail) ----
    diag_ms = list(range(20, M_MAX - 2))
    deg_fp, g_fp = leading_log_slope(fp, q, diag_ms)
    deg_Sp, g_Sp = leading_log_slope(Sp, q, diag_ms)
    deg_ya, g_ya = leading_log_slope(ya, q, diag_ms)
    deg_rec, g_rec = leading_log_slope(rec, q, diag_ms)
    diag = {
        "C1_fplus_theta_gamma": mp.nstr(g_fp, 5) if g_fp is not None else None,
        "sym2_fplus2_theta_gamma": mp.nstr(g_Sp, 5) if g_Sp is not None else None,
        "GGM_ya_theta_gamma": mp.nstr(g_ya, 5) if g_ya is not None else None,
        "GGM_recessive_theta_gamma": mp.nstr(g_rec, 5) if g_rec is not None else None,
    }

    return {"q": mp.nstr(q, 8), "test_A_forward": testA,
            "test_B_recessive": testB, "growth_diagnostics": diag}


def solver_selftest(q):
    """Prove the least-squares solver recovers an IN-SPAN target exactly, so a
    residual of O(1) elsewhere is a genuine refutation, not a solver artifact."""
    fp, fm = c1_solutions(q, M_MAX)
    Sp, Spm, Sm = elementwise(fp, fp), elementwise(fp, fm), elementwise(fm, fm)
    cols = [Sp, Spm, Sm]
    known = [mpf(2) * Sp[m] - mpf(3) * Spm[m] + mpf("0.5") * Sm[m]
             for m in range(len(Sp))]
    fit_ms = list(range(0, N_FIT + 1))
    c = col_scaled_lstsq(cols, known, fit_ms)
    tail, _ = extrapolation_residual(cols, c, known, TAIL)
    return {"q": mp.nstr(q, 8), "recovered_coeffs": [mp.nstr(x, 8) for x in c],
            "tail_rel_residual": mp.nstr(tail, 6),
            "pass": bool(tail < TOL_CONSISTENT)}


def main():
    results = []
    any_consistent = False
    selftest = [solver_selftest(q) for q in Q_LIST]
    print("SOLVER SELF-TEST (in-span target must give ~0 residual):")
    for st in selftest:
        print(f"  q={st['q']}: tail_resid={st['tail_rel_residual']} pass={st['pass']}")
    for q in Q_LIST:
        r = analyze_q(q)
        results.append(r)
        ca = any(v.get("consistent") for v in r["test_A_forward"].values()
                 if isinstance(v, dict))
        cb = r["test_B_recessive"].get("consistent_3col") or \
            r["test_B_recessive"].get("consistent_6col")
        any_consistent = any_consistent or ca or cb
        print(f"\n=== q = {mp.nstr(q, 8)} ===")
        for name, v in r["test_A_forward"].items():
            print(f"  TEST A {name}: rel_resid={v.get('tail_rel_residual')} "
                  f"consistent={v.get('consistent')}")
        tb = r["test_B_recessive"]
        print(f"  TEST B recessive: 3col rel={tb.get('tail_rel_residual_3col')} "
              f"6col rel={tb.get('tail_rel_residual_6col')} "
              f"consistent3={tb.get('consistent_3col')} "
              f"consistent6={tb.get('consistent_6col')}")
        print(f"  growth gamma (theta q^{{gamma m^2}}): {r['growth_diagnostics']}")

    if any_consistent:
        verdict = (
            "SCOPE-(a) POSITIVE: at >=1 tested q an EXPLICIT m-independent "
            "linear combination of the C1 sym^2 (/bar-sym^2) sequences "
            "reproduces a GGM solution to < 1e-40 across the extrapolation "
            "tail -- the sinh/cosh bar-even/odd NON-module bridge C1^2 -> GGM "
            "LANDS (Door-i's non-module carve-out realized). This is the first "
            "positive C1<->GGM link; it is a sequence-level (non-module) "
            "correspondence, NOT a q-difference-module iso (Door-i's "
            "isoclinicity exclusion stands).")
    else:
        verdict = (
            "SCOPE-(a) REFUTED: at every tested q NO fixed (m-independent) "
            "linear combination of the C1 sym^2 or bar-sym^2 sequences "
            "reproduces the GGM solutions across the extrapolation tail "
            "(residual O(1) drift). The specific sinh/cosh bar-even/odd "
            "sym^2 construction, ALONE, does not reproduce GGM; the growth "
            "diagnostics record the leading-order mismatch (see "
            "growth_diagnostics per q). This does NOT exclude other "
            "non-module identifications -- it measures the size of the miss "
            "for THIS construction only. No scope-(b) claim (Door-i already "
            "supplies the module-level isoclinicity exclusion).")
    print(f"\nVERDICT: {verdict}")

    witness = {
        "description": "Door-iii sinh/cosh (bar-even/odd) NON-module bridge "
                       "C1^2 -> GGM eq-49: does a fixed m-independent linear "
                       "combination of the C1 symmetric-square sequences "
                       "{f+^2,f+f-,f-^2} and their bar-conjugates (q->1/q) "
                       "reproduce the GGM solutions?",
        "computation": "mpmath dps=60; C1 [m+2]_q b_{m+2}=b_{m+1}+b_m and GGM "
                       "y_{m+1}=(2-q^m)y_m-y_{m-1}, m=0..50; two independent C1 "
                       "solutions squared into a rank-3 sym^2 basis + bar (1/q) "
                       "copy -> 6-col basis; column-scaled least-squares fit on "
                       "m=0..14, extrapolation residual on m=34..50; TEST B "
                       "extracts GGM's minimal (forward-decaying) solution by "
                       "Miller backward recursion from m=140 and tests it "
                       "against the 3-col unbarred sym^2 basis (slope-matched)",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {
            "dps": mp.dps, "m_max": M_MAX, "n_fit": N_FIT,
            "tail_window": [TAIL[0], TAIL[-1]], "m_miller": M_MILLER,
            "q_values": [mp.nstr(q, 8) for q in Q_LIST],
            "tol_consistent": "1e-40",
            "kill_criterion": "tail relative residual < 1e-40 => CONSISTENT "
                              "(bridge lands); O(1) drift => REFUTED at that q",
        },
        "results": {"per_q": results, "any_consistent": bool(any_consistent),
                    "solver_selftest": selftest, "verdict": verdict},
        "context": {
            "bean": "qou-ceg6",
            "audit_doc": "docs/audits/2026-07-20-qlift-doorIII-sinhcosh-bridge.md",
            "builds_on": [
                "docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md "
                "(five routes: C1 != GGM as q-difference modules)",
                "docs/audits/2026-07-20-qlift-doorI-analytic-summation.md "
                "(isoclinicity: no module map bridges them; NON-module maps "
                "explicitly left as the only carve-out)",
            ],
            "ggm_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf p.14 (eq 49)",
            "hypothesis": "GGM solutions are the bar-even (cosh) / bar-odd "
                          "(sinh) combinations of the SQUARES of C1 solutions "
                          "(slope-1/2 products -> slope-1); 2*(1/2)=1",
            "discipline": "scope-(a) vocabulary per AGENTS.md refuted-discipline; "
                          "pre-stated kill criterion; NON-module correspondence "
                          "by design (Door-i excludes module maps); the only "
                          "'fit' is the m-independent linear coefficient solve "
                          "whose sole purpose is the extrapolation kill-test; "
                          "no AME data",
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qlift_doorIII_sinhcosh_bridge_probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
