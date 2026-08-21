#!/usr/bin/env python3
"""Diagonal-gauge prune: can b_m = g_m * y_m map the C1 kernel into GGM eq 49?

Workplan step 3 of docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md.
Formalize-first: the consistency condition is DERIVED symbolically below (and
in docs/audits/2026-07-20-qlift-ggm-gauge-prune.md); this probe only verifies
the derived identity numerically. No scan, no fit, no AME data.

Kernels (three-term windows aligned at index m):
  C1 (proved q-lift, c(q)=1 exact per qlift_kernel_candidate_crosscheck_probe):
        [m+1]_q * b_{m+1} = b_m + c * b_{m-1}        (c = c(q), generic constant-in-m)
  C2 (GGM eq 49, arXiv:2012.00062 p.14):
        y_{m+1} - (2 - q^m) * y_m + y_{m-1} = 0.

DERIVATION (the formalize-first content).  Substitute b_m = g_m y_m (g_m != 0)
into monic C1 and divide by g_{m+1}:
    y_{m+1} - (g_m / (g_{m+1} [m+1]_q)) y_m - (c g_{m-1} / (g_{m+1} [m+1]_q)) y_{m-1} = 0.
Matching C2 coefficient-by-coefficient:
    (A)  g_m / g_{m+1} = [m+1]_q (2 - q^m)          (y_m coefficient)
    (B)  g_{m-1} / g_{m+1} = -[m+1]_q / c            (y_{m-1} coefficient)
One gauge freedom (the ratio sequence g_{m+1}/g_m), two constraints.  Chain
(A) at m and m-1 into (B):
    g_{m-1}/g_{m+1} = ([m]_q (2 - q^{m-1})) * ([m+1]_q (2 - q^m)) = -[m+1]_q / c
    =>  CONSISTENCY:  c * [m]_q * (2 - q^{m-1}) * (2 - q^m) = -1   for ALL m.
The LHS is non-constant in m (|[m]_q| is strictly monotone for real q > 0,
q != 1 padding aside; at q = 1 the LHS is c*m); the RHS is the constant -1.
Hence NO constant c(q) and NO gauge sequence g_m can satisfy both (A) and (B):
the system is over-determined and fails identically.  Index shifts
b_{m+s} = g_m y_m only replace [m]_q by [m+s]_q -- still non-constant in m.

KILL CRITERION (pre-stated): let C_m(q; c, s) = c*[m+s]_q*(2-q^{m-1})*(2-q^m) + 1.
If max_m |C_m| < 1e-40 for some (c, s) across all tested q, the diagonal gauge
SURVIVES and the derivation above is wrong.  Observed outcome (any |C_m| >> 0
with the derivation displayed) is a SCOPE-(b) STRUCTURAL EXCLUSION of
*diagonal* gauges only, justified by the derived algebraic identity (the
"proved invariant" per AGENTS.md section 'Before declaring refuted').
NOT excluded: non-diagonal 2x2 gauge transforms (vector (y_m, y_{m+1}) ->
A_m(q) * vector), Moebius transforms of solution ratios, inhomogeneous shifts
b_m = g_m y_m + h_m, and integral/summation (q-Borel-type) transforms mixing
all m.  Those remain live for workplan step 3's Stokes-matrix route.

Checks (mpmath, dps = 50, q in {0.9, 1.05, 1.10998}, m <= 15):
  P1  Consistency residual C_m(q; c=1, s=0), m = 1..15: report min/max |C_m|.
  P2  Direct construction: define g via (A) with g_0 = 1, y_m = b_m/g_m
      (b_m = I_q(m)/[m]_q!, the proved C1 solution); GGM eq-49 relative
      residual for m = 1..14.  By construction only the y_{m-1} coefficient
      can mismatch; residual != 0 measures the obstruction concretely.
  P3  No constant c(q) rescue: spread of S_m = [m]_q(2-q^{m-1})(2-q^m)
      across m (max - min); spread >> 0 => no constant can zero all C_m.
      Also index shifts s in {-2..2}: min over s of max_m |C_m(c=-1/S_1)|.

Run:  python3 -u computations/probes/qlift_ggm_diagonal_gauge_prune_probe.py \
          2>&1 | tee /tmp/qlift-gauge-prune.log
Emits: qlift_ggm_diagonal_gauge_prune_probe.witness.json (same directory).
"""

import json
import os
from datetime import datetime, timezone

from mpmath import mp, mpf

mp.dps = 50

TOL_KILL = mpf("1e-40")   # survival threshold (pre-stated kill criterion)
M_MAX = 15
Q_LIST = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]


# Path bridge — keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from witness_base import WitnessBuilder  # noqa: E402

import time as _time  # noqa: E402
_T0 = _time.monotonic()


def qint(k, q):
    """[k]_q = (1 - q^k)/(1 - q)."""
    return (1 - q ** k) / (1 - q)


def qfact(n, q):
    out = mpf(1)
    for k in range(1, n + 1):
        out *= qint(k, q)
    return out


def b_sequence(nmax, q):
    """Proved C1 solution: b_n = I_q(n)/[n]_q!, I_q(n+2)=I_q(n+1)+[n+1]_q I_q(n)."""
    I = [mpf(1), mpf(1)]
    for n in range(nmax - 1):
        I.append(I[n + 1] + qint(n + 1, q) * I[n])
    return [I[n] / qfact(n, q) for n in range(nmax + 1)]


def s_factor(m, q, s=0):
    """S_m = [m+s]_q (2 - q^{m-1})(2 - q^m); consistency C_m = c*S_m + 1."""
    return qint(m + s, q) * (2 - q ** (m - 1)) * (2 - q ** m)


# ---------------------------------------------------------------- P1
def p1_consistency():
    print("== P1: consistency residual C_m = [m]_q(2-q^(m-1))(2-q^m) + 1  (c=1, s=0) ==")
    rows = []
    survived = False
    for q in Q_LIST:
        vals = [abs(s_factor(m, q) + 1) for m in range(1, M_MAX + 1)]
        cmin, cmax = min(vals), max(vals)
        if cmax < TOL_KILL:
            survived = True
        print(f"  q = {mp.nstr(q, 8):<10} min|C_m| = {mp.nstr(cmin, 4):<12} "
              f"max|C_m| = {mp.nstr(cmax, 4):<12} "
              f"{'SURVIVES' if cmax < TOL_KILL else 'fails identically'}")
        rows.append({"q": mp.nstr(q, 8), "min_abs_C": mp.nstr(cmin, 4),
                     "max_abs_C": mp.nstr(cmax, 4),
                     "survives": bool(cmax < TOL_KILL)})
    verdict = ("SURVIVES (derivation wrong!)" if survived else
               "consistency condition fails identically: |C_m| = O(1..10^2) at "
               "every m <= 15, every q -- diagonal gauge over-determined")
    print(f"  => {verdict}\n")
    return {"rows": rows, "survived": survived, "verdict": verdict}


# ---------------------------------------------------------------- P2
def p2_direct_residual():
    print("== P2: direct residual -- gauge g from (A), y = b/g, GGM eq-49 residual ==")
    rows = []
    all_obstructed = True
    for q in Q_LIST:
        b = b_sequence(M_MAX + 2, q)
        # (A): g_{m+1} = g_m / ([m+1]_q (2 - q^m)), g_0 = 1
        g = [mpf(1)]
        for m in range(M_MAX + 1):
            g.append(g[m] / (qint(m + 1, q) * (2 - q ** m)))
        y = [b[m] / g[m] for m in range(M_MAX + 2)]
        worst = mpf(0)
        best = mpf("inf")
        for m in range(1, M_MAX):
            res = y[m + 1] - (2 - q ** m) * y[m] + y[m - 1]
            scale = max(abs(y[m + 1]), abs(y[m]), abs(y[m - 1]))
            rel = abs(res) / scale
            worst = max(worst, rel)
            best = min(best, rel)
        obstructed = best > TOL_KILL
        all_obstructed = all_obstructed and obstructed
        print(f"  q = {mp.nstr(q, 8):<10} eq-49 rel residual: min = "
              f"{mp.nstr(best, 4):<12} max = {mp.nstr(worst, 4):<12} "
              f"{'obstructed' if obstructed else 'MAPPED'}")
        rows.append({"q": mp.nstr(q, 8), "min_rel_residual": mp.nstr(best, 4),
                     "max_rel_residual": mp.nstr(worst, 4),
                     "obstructed": bool(obstructed)})
    print("  => the (A)-gauge fixes the y_m coefficient exactly; the y_{m-1} "
          "coefficient then\n     misses at every m -- concrete realization of "
          "the over-determination.\n")
    return {"rows": rows, "all_obstructed": all_obstructed,
            "verdict": ("obstructed at every m for every q" if all_obstructed
                        else "MAPPED somewhere (derivation wrong!)")}


# ---------------------------------------------------------------- P3
def p3_no_constant_c_no_shift():
    print("== P3: no constant c(q) and no index shift s rescues ==")
    rows = []
    any_rescue = False
    for q in Q_LIST:
        S = [s_factor(m, q) for m in range(1, M_MAX + 1)]
        spread = max(S) - min(S)
        # best constant c per shift s: c = -1/S_1 (zeroes m=1), then max residual
        shift_rows = []
        for s in range(-2, 3):
            Ss = [s_factor(m, q, s) for m in range(max(1, 1 - s), M_MAX + 1)]
            c_best = -1 / Ss[0]
            worst = max(abs(c_best * x + 1) for x in Ss)
            if worst < TOL_KILL:
                any_rescue = True
            shift_rows.append({"s": s, "c_best": mp.nstr(c_best, 6),
                               "max_abs_C": mp.nstr(worst, 4)})
        worst_over_s = min(mpf(r["max_abs_C"]) for r in shift_rows)
        print(f"  q = {mp.nstr(q, 8):<10} spread(S_m) = {mp.nstr(spread, 4):<12} "
              f"best-over-s max|C_m| = {mp.nstr(worst_over_s, 4)}")
        rows.append({"q": mp.nstr(q, 8), "spread_S": mp.nstr(spread, 4),
                     "shifts": shift_rows})
    verdict = ("RESCUED (derivation wrong!)" if any_rescue else
               "S_m non-constant in m at every q (spread >> 0); no constant "
               "c(q), no shift s in [-2,2] zeroes the residual")
    print(f"  => {verdict}\n")
    return {"rows": rows, "any_rescue": any_rescue, "verdict": verdict}


def main():
    p1 = p1_consistency()
    p2 = p2_direct_residual()
    p3 = p3_no_constant_c_no_shift()

    pruned = (not p1["survived"]) and p2["all_obstructed"] and (not p3["any_rescue"])
    verdict = (
        "SCOPE-(b) EXCLUSION of DIAGONAL gauges: the derived consistency "
        "condition c*[m+s]_q*(2-q^(m-1))*(2-q^m) = -1 (all m) fails "
        "identically -- one gauge freedom, two coefficient constraints, "
        "over-determined; verified |C_m| = O(1..10^2) at q in {0.9, 1.05, "
        "1.10998}, m <= 15, c and s free.  Invariant cited: the exact "
        "algebraic identity displayed in the module docstring / audit doc. "
        "NOT excluded (scope stated explicitly): non-diagonal 2x2 gauge "
        "transforms, Moebius-of-solution-ratio maps, inhomogeneous shifts "
        "b_m = g_m y_m + h_m, and q-Borel-type summation transforms mixing "
        "all m.  C1 and GGM eq-49 remain two genuinely distinct order-2 "
        "q-lifts of the same classical shadow."
        if pruned else
        "PROBE INCONSISTENT WITH DERIVATION -- re-examine the algebra before "
        "any durable claim.")
    print("VERDICT:", verdict)

    witness = {
        "description": "Diagonal-gauge prune: b_m = g_m*y_m from C1 kernel "
                       "[m+1]_q b_{m+1} = b_m + c b_{m-1} into GGM eq-49 "
                       "y_{m+1} - (2-q^m) y_m + y_{m-1} = 0 -- consistency "
                       "condition derived symbolically, verified numerically",
        # `computation` is RESERVED by WitnessBuilder.wrap_legacy, which
        # overwrites it with the witness stem ("filename already encodes
        # this"). That is true for a name and false for this field, which
        # is a METHOD description. Renamed so the text survives the wrap.
        "computation_method": "mpmath dps=50; P1 residual of derived consistency "
                       "identity; P2 direct (A)-gauge construction + eq-49 "
                       "residual on the proved C1 solution b_n = I_q(n)/[n]_q!; "
                       "P3 constant-c(q) and index-shift non-rescue",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {"dps": mp.dps, "tol_kill": "1e-40", "m_max": M_MAX,
                       "q_values": [mp.nstr(q, 8) for q in Q_LIST],
                       "shifts_tested": [-2, -1, 0, 1, 2]},
        "derivation": {
            "constraint_A": "g_m/g_{m+1} = [m+1]_q (2 - q^m)",
            "constraint_B": "g_{m-1}/g_{m+1} = -[m+1]_q / c",
            "consistency": "c * [m]_q * (2 - q^{m-1}) * (2 - q^m) = -1 for all m",
            "why_it_fails": "LHS non-constant in m (equals c*m at q=1, and "
                            "positive for real 0 < q^m < 2), RHS constant -1",
        },
        "results": {"p1_consistency": p1, "p2_direct_residual": p2,
                    "p3_no_constant_c_no_shift": p3, "pruned": pruned,
                    "verdict": verdict},
        "context": {
            "workplan": "docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md (step 3)",
            "audit_doc": "docs/audits/2026-07-20-qlift-ggm-gauge-prune.md",
            "prior_probe": "computations/probes/qlift_kernel_candidate_crosscheck_probe.py "
                           "(T2 scalar-gauge DISTINCT verdict; this probe upgrades "
                           "scalar -> arbitrary diagonal)",
            "ggm_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf pp.14-15 (eq 49, Thm 9 bar parity)",
            "discipline": "formalize-first (derivation before any scan); "
                          "scope-(a)/(b) vocabulary per AGENTS.md; no AME data; anti-fit",
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "qlift_ggm_diagonal_gauge_prune_probe",
        witness,
        script_path=__file__,
        engine="python+mpmath",
        start_time=_T0,
    ).save()
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
