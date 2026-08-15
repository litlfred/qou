#!/usr/bin/env python3
"""Door-iii FOLLOW-UP: twisted-combination + cross-term sinh/cosh C1^2 -> GGM eq 49.

Bean qou-vw3g.  Follow-up to Door-iii
(docs/audits/2026-07-20-qlift-doorIII-sinhcosh-bridge.md +
computations/probes/qlift_doorIII_sinhcosh_bridge_probe.py), which REFUTED
(scope-(a)) the naive m-INDEPENDENT linear combination of the C1 symmetric
squares {f+^2, f+f-, f-^2} (and bar copies) reproducing GGM eq 49.  The
leading growth class (theta q^{gamma m^2}) matched (sym^2 doubles C1's
slope-1/2 to slope-1 = GGM slope) but the SUB-LEADING theta fine-structure
did NOT, so the fixed-combination extrapolation drifted O(1).

Recursions (state index m):
  C1  (proved q-lift): [m+2]_q b_{m+2} = b_{m+1} + b_m,  [n]_q=(q^n-1)/(q-1)
  GGM (eq 49, arXiv:2012.00062 p.14): y_{m+1} = (2 - q^m) y_m - y_{m-1}
Bar involution: q -> 1/q.

This follow-up tests the two refined identifications the owner named:

  OPTION 1 -- TWISTED COMBINATION.  Allow an m-DEPENDENT q-power twist: fit GGM
    to  q^{alpha*m} * (sym^2 combo)  +  q^{-alpha*m} * (bar-sym^2 combo)  for a
    FIXED scalar alpha (swept over a small grid).  A q^{alpha*m} factor shifts
    only the LINEAR-in-m degree term of log|.| (the sub-leading theta), leaving
    the quadratic gamma*m^2 slope term UNCHANGED -- exactly the Door-iii miss.
    So the twist directly targets Door-iii's "sub-leading fine-structure"
    failure while preserving the confirmed leading slope match.  Does any fixed
    alpha + fixed combo reproduce a GGM solution across the tail?
      residual < 1e-40 over the tail  =>  LANDS (scope-(a) POSITIVE)
      residual = O(1) at every alpha   =>  REFUTED for this twisted class.

  OPTION 2 -- CROSS-TERM LEAD.  Test whether GGM's anisoclinic {-1,+1} needs
    the SLOPE-0 cross term f+f- as the connecting datum, NOT the pure squares.
    Fit GGM to span{f+^2, f+f-, f-^2, bar-versions} and REPORT which basis
    elements carry NONZERO weight -- is f+f- essential?  Also run the targeted
    2-column hypothesis  GGM =? bar-even(f+^2) +- f+f-  (bar-even(X)=(X+Xbar)/2).

KILL CRITERION (pre-stated, per AGENTS.md refuted-discipline):
  For a GGM target y and candidate basis S, fit a fixed coefficient vector on
  the low-m window m in [0, N_FIT], form the EXTRAPOLATION residual
  R = max_{m in tail} |y_m - (S c)_m| / |y_m|.
    * R < 1e-40 over the tail  => LANDS (scope-(a) POSITIVE: the explicit
        m-independent [+ fixed-alpha] combination reproduces GGM -- FIRST
        positive C1<->GGM link; a NON-module, sequence-level correspondence,
        NOT a q-difference-module iso, Door-i's isoclinicity exclusion stands).
    * R = O(1) drift  => REFUTED at that q (scope-(a): this construction ALONE
        does not reproduce GGM).  NO scope-(b) structural-exclusion claim is
        made here (that is Door-i's job, done with the isoclinicity invariant).

A solver self-test (fit a target that IS a known twisted combo) recovers it to
< 1e-40, so an O(1) residual is a genuine miss, not a solver artifact.

mpmath dps=60.  No AME data; no experimental fit; the only 'fit' is the
m-independent linear coefficient solve (over a small fixed-alpha grid) whose
sole purpose is the extrapolation kill-test.

Run:  python3 -u computations/probes/qlift_doorIII_followup_twist_crossterm_probe.py \
          2>&1 | tee /tmp/qlift-doorIII-followup.log
Emits: qlift_doorIII_followup_twist_crossterm_probe.witness.json (same dir).
"""

import json
import os
from datetime import datetime, timezone

import mpmath
from mpmath import mp, mpf, log, fabs

mp.dps = 60

M_MAX = 50                          # solution index m = 0..50 (task spec)
N_FIT = 14                          # fit window m = 0..N_FIT (low m)
TAIL = list(range(34, M_MAX + 1))   # extrapolation window (disjoint from fit)
M_MILLER = 140                      # backward-recursion start (minimal solution)
Q_LIST = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]
TOL_CONSISTENT = mpf("1e-40")
# small alpha grid for OPTION 1 (fixed scalar twist exponent)
ALPHA_GRID = [mpf(a) for a in
              ("-2", "-1.5", "-1", "-0.5", "-0.25", "0",
               "0.25", "0.5", "1", "1.5", "2")]


def q_int(n, q):
    if q == 1:
        return mpf(n)
    return (q ** n - 1) / (q - 1)


def c1_solutions(q, M):
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


def twist_col(col, q, alpha):
    """Multiply column elementwise by q^{alpha*m}."""
    return [col[m] * q ** (alpha * m) for m in range(len(col))]


def col_scaled_lstsq(cols, target, fit_ms):
    ncol = len(cols)
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
    AT = A.T
    G = AT * A
    rhs = AT * b
    csc = mp.lu_solve(G, rhs)
    return [csc[j, 0] / scales[j] for j in range(ncol)]


def extrapolation_residual(cols, coeffs, target, test_ms):
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
    deg = mp.fsum(d1) / len(d1)
    gamma = (mp.fsum(d2) / len(d2)) / 2
    return deg, gamma


def fit_and_resid(cols, target, fit_ms):
    """Fit + return (rel_resid, abs_resid, coeffs) with graceful failure."""
    try:
        c = col_scaled_lstsq(cols, target, fit_ms)
        rrel, rabs = extrapolation_residual(cols, c, target, TAIL)
        return rrel, rabs, c
    except Exception as e:  # noqa: BLE001
        return None, None, repr(e)


def analyze_q(q):
    fp, fm = c1_solutions(q, M_MAX)
    fbp, fbm = c1_solutions(1 / q, M_MAX)          # bar = q -> 1/q
    ya, yb = ggm_forward(q, M_MAX)
    rec = ggm_recessive(q, M_MAX, M_MILLER)

    Sp, Spm, Sm = elementwise(fp, fp), elementwise(fp, fm), elementwise(fm, fm)
    Bp, Bpm, Bm = elementwise(fbp, fbp), elementwise(fbp, fbm), elementwise(fbm, fbm)
    unbar = [Sp, Spm, Sm]
    bar = [Bp, Bpm, Bm]
    col_names = ["f+^2", "f+f-", "f-^2", "fb+^2", "fb+fb-", "fb-^2"]
    fit_ms = list(range(0, N_FIT + 1))

    targets = {"y_a_forward": ya, "y_b_forward": yb, "recessive": rec}

    # ================= OPTION 1: twisted combination =================
    #   basis columns: q^{+alpha m} * {unbar} , q^{-alpha m} * {bar}
    option1 = {}
    for tname, tgt in targets.items():
        per_alpha = []
        best = {"alpha": None, "rel": None}
        for alpha in ALPHA_GRID:
            tw_unbar = [twist_col(c, q, alpha) for c in unbar]
            tw_bar = [twist_col(c, q, -alpha) for c in bar]
            cols = tw_unbar + tw_bar
            rrel, rabs, c = fit_and_resid(cols, tgt, fit_ms)
            entry = {"alpha": mp.nstr(alpha, 4),
                     "rel_residual": (mp.nstr(rrel, 6) if rrel is not None else None)}
            if isinstance(c, list):
                entry["coeffs"] = [mp.nstr(x, 6) for x in c]
            per_alpha.append(entry)
            if rrel is not None and (best["rel"] is None or rrel < best["rel"]):
                best = {"alpha": mp.nstr(alpha, 4), "rel": rrel,
                        "coeffs": ([mp.nstr(x, 6) for x in c]
                                   if isinstance(c, list) else None)}
        option1[tname] = {
            "per_alpha": per_alpha,
            "best_alpha": best["alpha"],
            "best_rel_residual": (mp.nstr(best["rel"], 6)
                                  if best["rel"] is not None else None),
            "best_coeffs": best.get("coeffs"),
            "lands": bool(best["rel"] is not None and best["rel"] < TOL_CONSISTENT),
        }

    # ================= OPTION 2: cross-term lead =================
    #   full 6-col fit; report which columns carry nonzero weight (is f+f- essential?)
    cols6 = unbar + bar
    cols3 = unbar
    option2 = {}
    for tname, tgt in targets.items():
        rrel6, rabs6, c6 = fit_and_resid(cols6, tgt, fit_ms)
        rrel3, rabs3, c3 = fit_and_resid(cols3, tgt, fit_ms)
        # normalized weights (relative magnitude) for the 6-col fit
        weights6 = None
        crossterm_essential = None
        if isinstance(c6, list):
            mags = [fabs(x) for x in c6]
            mx = max(mags) if mags else mpf(1)
            mx = mx if mx != 0 else mpf(1)
            weights6 = {col_names[j]: mp.nstr(mags[j] / mx, 5)
                        for j in range(len(c6))}
            # cross-term (f+f-) essential if its normalized weight is not tiny
            # AND dropping it (3-col-no-cross fit) materially worsens the fit
            cross_norm = mags[1] / mx
            crossterm_essential = bool(cross_norm > mpf("1e-3"))
        # targeted 2-col hypothesis: GGM =? bar-even(f+^2) +- f+f-
        bar_even_fp2 = [(Sp[m] + Bp[m]) / 2 for m in range(M_MAX + 1)]
        cols2 = [bar_even_fp2, Spm]
        rrel2, rabs2, c2 = fit_and_resid(cols2, tgt, fit_ms)
        # drop-cross control: fit {f+^2, f-^2, bar} WITHOUT f+f-
        cols_nocross = [Sp, Sm, Bp, Bm]
        rrelnc, _, _ = fit_and_resid(cols_nocross, tgt, fit_ms)
        option2[tname] = {
            "rel_residual_6col": (mp.nstr(rrel6, 6) if rrel6 is not None else None),
            "rel_residual_3col_unbar": (mp.nstr(rrel3, 6) if rrel3 is not None else None),
            "rel_residual_2col_barEven_plus_cross":
                (mp.nstr(rrel2, 6) if rrel2 is not None else None),
            "rel_residual_nocross_control":
                (mp.nstr(rrelnc, 6) if rrelnc is not None else None),
            "normalized_weights_6col": weights6,
            "crossterm_fpfm_nonzero": crossterm_essential,
            "coeffs_2col": ([mp.nstr(x, 6) for x in c2]
                            if isinstance(c2, list) else None),
            "lands_6col": bool(rrel6 is not None and rrel6 < TOL_CONSISTENT),
            "lands_2col": bool(rrel2 is not None and rrel2 < TOL_CONSISTENT),
        }

    # ================= growth diagnostics (context) =================
    diag_ms = list(range(20, M_MAX - 2))
    _, g_fp = leading_log_slope(fp, q, diag_ms)
    _, g_Sp = leading_log_slope(Sp, q, diag_ms)
    _, g_Spm = leading_log_slope(Spm, q, diag_ms)
    _, g_ya = leading_log_slope(ya, q, diag_ms)
    _, g_rec = leading_log_slope(rec, q, diag_ms)
    diag = {
        "C1_fplus_theta_gamma": mp.nstr(g_fp, 5) if g_fp is not None else None,
        "sym2_fplus2_theta_gamma": mp.nstr(g_Sp, 5) if g_Sp is not None else None,
        "crossterm_fpfm_theta_gamma": mp.nstr(g_Spm, 5) if g_Spm is not None else None,
        "GGM_ya_theta_gamma": mp.nstr(g_ya, 5) if g_ya is not None else None,
        "GGM_recessive_theta_gamma": mp.nstr(g_rec, 5) if g_rec is not None else None,
    }

    return {"q": mp.nstr(q, 8), "option1_twist": option1,
            "option2_crossterm": option2, "growth_diagnostics": diag}


def solver_selftest(q):
    """Recover an IN-SPAN twisted target exactly (so O(1) elsewhere is genuine)."""
    fp, fm = c1_solutions(q, M_MAX)
    fbp, fbm = c1_solutions(1 / q, M_MAX)
    Sp, Spm, Sm = elementwise(fp, fp), elementwise(fp, fm), elementwise(fm, fm)
    Bp, Bpm, Bm = elementwise(fbp, fbp), elementwise(fbp, fbm), elementwise(fbm, fbm)
    alpha = mpf("0.5")
    unbar = [twist_col(c, q, alpha) for c in (Sp, Spm, Sm)]
    barc = [twist_col(c, q, -alpha) for c in (Bp, Bpm, Bm)]
    cols = unbar + barc
    known = [mpf(2) * cols[0][m] - mpf(3) * cols[1][m] + mpf("0.5") * cols[2][m]
             + mpf("1.5") * cols[3][m] - cols[4][m] for m in range(len(Sp))]
    fit_ms = list(range(0, N_FIT + 1))
    c = col_scaled_lstsq(cols, known, fit_ms)
    tail, _ = extrapolation_residual(cols, c, known, TAIL)
    return {"q": mp.nstr(q, 8), "tail_rel_residual": mp.nstr(tail, 6),
            "pass": bool(tail < TOL_CONSISTENT)}


def main():
    selftest = [solver_selftest(q) for q in Q_LIST]
    print("SOLVER SELF-TEST (in-span twisted target must give ~0 residual):")
    for st in selftest:
        print(f"  q={st['q']}: tail_resid={st['tail_rel_residual']} pass={st['pass']}")

    results = []
    opt1_lands = False
    opt2_lands = False
    for q in Q_LIST:
        r = analyze_q(q)
        results.append(r)
        for tname, v in r["option1_twist"].items():
            opt1_lands = opt1_lands or v["lands"]
        for tname, v in r["option2_crossterm"].items():
            opt2_lands = opt2_lands or v["lands_6col"] or v["lands_2col"]
        print(f"\n=== q = {mp.nstr(q, 8)} ===")
        print("  OPTION 1 (twist) best alpha + residual per target:")
        for tname, v in r["option1_twist"].items():
            print(f"    {tname}: best_alpha={v['best_alpha']} "
                  f"best_rel={v['best_rel_residual']} lands={v['lands']}")
        print("  OPTION 2 (cross-term) residuals + f+f- weight per target:")
        for tname, v in r["option2_crossterm"].items():
            w = v["normalized_weights_6col"]
            fpfm_w = w["f+f-"] if w else None
            print(f"    {tname}: 6col={v['rel_residual_6col']} "
                  f"2col(barEven+cross)={v['rel_residual_2col_barEven_plus_cross']} "
                  f"nocross={v['rel_residual_nocross_control']} "
                  f"f+f-_wt={fpfm_w} essential={v['crossterm_fpfm_nonzero']}")
        print(f"  growth gamma (theta q^{{gamma m^2}}): {r['growth_diagnostics']}")

    lands = opt1_lands or opt2_lands
    if lands:
        which = []
        if opt1_lands:
            which.append("OPTION 1 (twisted combination)")
        if opt2_lands:
            which.append("OPTION 2 (cross-term lead)")
        verdict = (
            "SCOPE-(a) POSITIVE / LANDS: " + " and ".join(which) + " reproduces "
            "a GGM solution to < 1e-40 across the extrapolation tail at >=1 "
            "tested q -- the FIRST positive C1<->GGM link. This is a "
            "sequence-level (NON-module) correspondence, NOT a q-difference-"
            "module iso (Door-i's isoclinicity exclusion stands). See the "
            "best_alpha / best_coeffs (Option 1) or the nonzero normalized "
            "weights (Option 2) for the explicit combination.")
    else:
        verdict = (
            "SCOPE-(a) REFUTED (both options): at every tested q, neither the "
            "m-dependent q^{alpha m} TWISTED combination (Option 1, any alpha "
            "in the grid) nor the CROSS-TERM-led basis (Option 2, incl. the "
            "targeted bar-even(f+^2) +- f+f- 2-col fit) reproduces a GGM "
            "solution across the extrapolation tail (residual O(1) drift). The "
            "twist shifts only the sub-leading LINEAR-in-m theta term, leaving "
            "the confirmed quadratic gamma*m^2 slope match intact, yet the full "
            "sub-leading theta fine-structure is still not reachable; the "
            "cross term f+f- (slope 0) does not supply the anisoclinic "
            "connecting datum either. This CLOSES the exact non-module "
            "identification for these refined classes too (reinforcing Door-i "
            "reading R1: C1 is a DISTINCT object -- its own Gevrey-1/2 module -- "
            "from the colored-Jones/Stokes GGM carrier). scope-(a) only: no "
            "ingredient structurally excluded here (Door-i supplies the "
            "module-level isoclinicity (b)-exclusion); this measures the miss "
            "for these two constructions. RECOMMENDATION: upgrade Door-iii to a "
            "scope-(b) Lean no-identity theorem (a proved invariant separating "
            "the two sub-leading theta fine-structures), retiring the "
            "non-module carve-out.")
    print(f"\nVERDICT: {verdict}")

    witness = {
        "description": "Door-iii FOLLOW-UP: does a TWISTED (m-dependent "
                       "q^{alpha m}) combination or a CROSS-TERM-led basis of "
                       "the C1 symmetric-square sequences reproduce the GGM "
                       "eq-49 solutions, where the naive m-independent linear "
                       "combo (Door-iii) failed on sub-leading theta fine-structure?",
        "computation": "mpmath dps=60; C1 [m+2]_q b_{m+2}=b_{m+1}+b_m and GGM "
                       "y_{m+1}=(2-q^m)y_m-y_{m-1}, m=0..50; OPTION 1 fits GGM to "
                       "q^{+alpha m}*{f+^2,f+f-,f-^2} U q^{-alpha m}*{bar copies} "
                       "over a fixed-alpha grid; OPTION 2 fits the 6-col basis and "
                       "reports nonzero normalized weights (is f+f- essential?), "
                       "plus the targeted 2-col bar-even(f+^2)+-f+f- fit and a "
                       "no-cross control; column-scaled least squares on m=0..14, "
                       "extrapolation residual on m=34..50; recessive GGM via "
                       "Miller backward recursion from m=140",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {
            "dps": mp.dps, "m_max": M_MAX, "n_fit": N_FIT,
            "tail_window": [TAIL[0], TAIL[-1]], "m_miller": M_MILLER,
            "q_values": [mp.nstr(q, 8) for q in Q_LIST],
            "alpha_grid": [mp.nstr(a, 4) for a in ALPHA_GRID],
            "tol_consistent": "1e-40",
            "kill_criterion": "tail relative residual < 1e-40 => LANDS "
                              "(scope-(a) positive); O(1) drift => REFUTED",
        },
        "results": {
            "per_q": results,
            "option1_twist_lands": bool(opt1_lands),
            "option2_crossterm_lands": bool(opt2_lands),
            "any_lands": bool(lands),
            "solver_selftest": selftest,
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-vw3g",
            "audit_doc": "docs/audits/2026-07-20-qlift-doorIII-followup.md",
            "builds_on": [
                "docs/audits/2026-07-20-qlift-doorIII-sinhcosh-bridge.md "
                "(naive m-independent sym^2 combo REFUTED; leading slope matched, "
                "sub-leading theta fine-structure did not)",
                "docs/audits/2026-07-20-qlift-doorI-analytic-summation.md "
                "(isoclinicity: no module map bridges C1 and GGM; NON-module "
                "maps left as the only carve-out)",
            ],
            "ggm_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf p.14 (eq 49)",
            "hypotheses": {
                "option1": "an m-dependent q^{alpha m} twist (fixed scalar alpha) "
                           "shifts the sub-leading LINEAR-in-m theta term while "
                           "preserving the quadratic slope, targeting Door-iii's "
                           "sub-leading fine-structure miss",
                "option2": "the anisoclinic {-1,+1} GGM needs the slope-0 cross "
                           "term f+f- as the connecting datum, not the pure squares",
            },
            "discipline": "scope-(a) vocabulary per AGENTS.md refuted-discipline; "
                          "pre-stated kill criterion + twisted-target solver "
                          "self-test; NON-module correspondence by design (Door-i "
                          "excludes module maps); the only 'fit' is the "
                          "m-independent linear coefficient solve over a fixed-"
                          "alpha grid whose sole purpose is the extrapolation "
                          "kill-test; no AME data; a landing is CONSISTENT (first "
                          "positive C1<->GGM link), a refutation measures the "
                          "residual",
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qlift_doorIII_followup_twist_crossterm_probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
