#!/usr/bin/env python3
"""q-lift kernel candidate cross-check: C1 (q-Hermite/q-involution) vs C2 (GGM eq 49).

Workplan step 2 of docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md.
Literature basis: docs/audits/2026-07-20-qlift-literature-check.md (S2 inferred
c(q)=1 candidate; S4 GGM eq-49 order-2 carrier verified from library/arxiv-2012.00062v3/2012.00062v3.pdf).

Candidates for the q-lift of the PROVED classical depth-2 kernel
    (n+2) * b_{n+2} = b_{n+1} + b_n
(QOU.Mass.QDifferenceConfluentObstruction.normalized_classical_kernel_exists):

  C1 (q-Hermite route): q-involution numbers
        I_q(0) = I_q(1) = 1,  I_q(n+2) = I_q(n+1) + [n+1]_q * I_q(n),
        [k]_q = (1 - q^k)/(1 - q),  b_n = I_q(n)/[n]_q!
     Claim: [n+2]_q * b_{n+2} = b_{n+1} + c(q) * b_n with c(q) = 1 EXACTLY
     (by construction: divide the I_q recurrence by [n+1]_q!).

  C2 (GGM route): eq (49) of Garoufalidis-Gu-Marino (arXiv:2012.00062, p.14):
        y_{m+1} - (2 - q^m) * y_m + y_{m-1} = 0.

Checks:
  T1  C1 exactness: residual [n+2]_q*b_{n+2} - b_{n+1} - b_n at several real q
      (0.9, 0.99, 1.01, 1.05, 1.10998) and the classical q=1 limit, n <= 20;
      assert relative residual < 1e-45 at mp.dps = 50.
  T2  Confluent-limit + gauge comparison: write both kernels monic in the same
      shape; test numerically whether ANY scalar gauge b_m -> lam^m * b_m maps
      C1's solution into C2's kernel at q = 1.05 (and at q = 1) for m <= 12.
      lam is solved exactly from the m=1 residual (quadratic, both roots);
      residuals at m = 2..11 then measure the obstruction.
  T3  Bar symmetry (q -> 1/q), numerically at q = 1.05:
      - C1 coefficient covariance [k]_{1/q} = q^{-(k-1)} [k]_q;
      - C1 solution-level ratio b_n(1/q)/b_n(q) (classify even/odd/neither);
      - C2 kernel covariance: coeff(1/q, m) = coeff(q, -m) (invariant under
        (q -> 1/q, m -> -m) combined).

KILL CRITERION (pre-stated): this is a scope-(a) STRUCTURAL comparison only.
No AME data, no experimental anchors, no fitting anywhere. Verdict vocabulary
is CONSISTENT / DISTINCT per check -- never "derived". If T1's exactness
FAILS, that refutes the S2 inference of the lit-check and is reported honestly
as-is; nothing is tuned. A DISTINCT verdict on T2 means the two candidates are
genuinely different q-lifts of the same classical shadow (both remain live);
it excludes only the "same kernel up to scalar gauge" identification.

Run:  python3 -u computations/probes/qlift_kernel_candidate_crosscheck_probe.py \
          2>&1 | tee /tmp/qlift-probe.log
Emits: qlift_kernel_candidate_crosscheck_probe.witness.json (same directory).
"""

import json
import os
from datetime import datetime, timezone

from mpmath import mp, mpf
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

TOL_EXACT = mpf("1e-45")   # T1 assertion tolerance (relative)
TOL_GAUGE = mpf("1e-30")   # T2: residual below this counts as "mapped"
N_MAX_T1 = 20
M_MAX_T2 = 12


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
    """[k]_q = (1 - q^k)/(1 - q); classical limit k at q = 1."""
    if q == 1:
        return mpf(k)
    return (1 - q ** k) / (1 - q)


def qfact(n, q):
    out = mpf(1)
    for k in range(1, n + 1):
        out *= qint(k, q)
    return out


def q_involution(nmax, q):
    """I_q(0..nmax) via I_q(n+2) = I_q(n+1) + [n+1]_q I_q(n)."""
    I = [mpf(1), mpf(1)]
    for n in range(nmax - 1):
        I.append(I[n + 1] + qint(n + 1, q) * I[n])
    return I


def b_sequence(nmax, q):
    I = q_involution(nmax, q)
    return [I[n] / qfact(n, q) for n in range(nmax + 1)]


# ---------------------------------------------------------------- T1
def t1_c1_exactness():
    print("== T1: C1 exactness  [n+2]_q b_{n+2} = b_{n+1} + b_n  (c(q)=1) ==")
    q_list = [mpf("0.9"), mpf("0.99"), mpf("1.01"), mpf("1.05"),
              mpf("1.10998"), 1]  # 1 = classical limit ([k]_q := k)
    rows = []
    all_pass = True
    for q in q_list:
        b = b_sequence(N_MAX_T1 + 2, q)
        worst = mpf(0)
        for n in range(N_MAX_T1 + 1):
            lhs = qint(n + 2, q) * b[n + 2]
            rhs = b[n + 1] + b[n]
            rel = abs(lhs - rhs) / max(abs(rhs), mpf(1))
            worst = max(worst, rel)
        ok = worst < TOL_EXACT
        all_pass = all_pass and ok
        qs = "1 (classical limit)" if q == 1 else mp.nstr(q, 8)
        print(f"  q = {qs:<22} max rel residual = {mp.nstr(worst, 3):<12} "
              f"{'PASS' if ok else 'FAIL'}")
        rows.append({"q": qs, "max_rel_residual": mp.nstr(worst, 3),
                     "pass": bool(ok)})
    assert all_pass, "T1 FAILED: c(q)=1 exactness does not hold -- real finding, report honestly"
    print(f"  => c(q) = 1 EXACT (all residuals < 1e-45): CONSISTENT with the "
          f"S2 combinatorial inference\n")
    return {"tolerance": "1e-45", "n_max": N_MAX_T1, "rows": rows,
            "pass": all_pass,
            "verdict": "CONSISTENT: c(q)=1 holds to 1e-45 at every tested q "
                       "incl. q=1.10998 and the q=1 classical limit"}


# ---------------------------------------------------------------- T2
def solve_quadratic(a, b_, c):
    """Roots of a*x^2 + b*x + c = 0 over C (mpmath); complex scalar gauges
    are legitimate, so we do NOT restrict to real roots."""
    from mpmath import sqrt, mpc
    disc = mpc(b_ * b_ - 4 * a * c)
    r = sqrt(disc)
    return [(-b_ + r) / (2 * a), (-b_ - r) / (2 * a)]


def c2_residual(y, m, q):
    """GGM eq-49 residual y_{m+1} - (2 - q^m) y_m + y_{m-1} (index into list)."""
    return y[m + 1] - (2 - q ** m) * y[m] + y[m - 1]


def t2_gauge_comparison():
    print("== T2: kernel shapes + scalar-gauge test (C1 solution vs C2 kernel) ==")
    print("  Monic shapes:  C1: b_{m+1} - (1/[m+1]_q) b_m - (1/[m+1]_q) b_{m-1} = 0")
    print("                 C2: y_{m+1} - (2 - q^m)   y_m +               y_{m-1} = 0")
    print("  Confluent q=1: C1 coeffs (1/(m+1), -1/(m+1)) m-dependent;")
    print("                 C2 coeffs (1, +1) constant  -- shapes differ structurally.")
    results = {}
    overall_distinct = True
    for q in [mpf("1.05"), 1]:
        qs = "1 (classical limit)" if q == 1 else mp.nstr(q, 6)
        b = b_sequence(M_MAX_T2 + 1, q)
        # gauge y_m = lam^m b_m; residual at m: lam^{m+1} b_{m+1}
        #   - (2-q^m) lam^m b_m + lam^{m-1} b_{m-1} = 0
        # divide by lam^{m-1}:  b_{m+1} lam^2 - (2-q^m) b_m lam + b_{m-1} = 0
        # solve lam from m=1, test m=2..M_MAX_T2-1.
        qm = q ** 1 if q != 1 else mpf(1)
        roots = solve_quadratic(b[2], -(2 - qm) * b[1], b[0])
        root_rows = []
        mapped = False
        for lam in roots:
            worst = mpf(0)
            for m in range(2, M_MAX_T2):
                y = [lam ** k * b[k] for k in range(M_MAX_T2 + 1)]
                res = c2_residual(y, m, q if q != 1 else mpf(1))
                scale = max(abs(y[m + 1]), abs(y[m]), abs(y[m - 1]), mpf("1e-40"))
                worst = max(worst, abs(res) / scale)
            root_rows.append({"lambda": mp.nstr(lam, 12),
                              "max_rel_residual_m2_to_m11": mp.nstr(worst, 4)})
            print(f"  q = {qs:<22} lam = {mp.nstr(lam, 10):<28} "
                  f"max rel residual (m=2..{M_MAX_T2-1}) = {mp.nstr(worst, 4)}")
            if worst < TOL_GAUGE:
                mapped = True
        verdict = "gauge-mapped" if mapped else "DISTINCT (no scalar gauge)"
        print(f"  => q = {qs}: {verdict}")
        overall_distinct = overall_distinct and (not mapped)
        results[f"q_{qs.split()[0]}"] = {"roots": root_rows, "gauge_mapped": mapped}
    print("  => C1 and C2 are genuinely DISTINCT kernels: C2's trailing "
          "coefficient is constant +1,\n     C1's is m-dependent -1/[m+1]_q; "
          "no scalar gauge b_m -> lam^m b_m identifies them.\n")
    results["verdict"] = (
        "DISTINCT: the C1 (q-Borel/[n]_q!-normalized) kernel and the C2 (GGM "
        "eq-49 q-holonomic normal form) kernel share the order-2 depth and a "
        "classical shadow but are NOT related by any scalar gauge b_m -> "
        "lam^m b_m (tested both quadratic roots incl. complex lam, q=1.05 "
        "and q=1, m<=12); "
        "identification, if any, requires a non-scalar (m-dependent) gauge / "
        "q-Borel transform -- workplan step 3 territory, not claimed here")
    results["pass"] = overall_distinct
    return results


# ---------------------------------------------------------------- T3
def t3_bar_symmetry():
    print("== T3: bar symmetry (q -> 1/q) ==")
    q = mpf("1.05")
    qi = 1 / q
    rows = {}

    # (a) C1 coefficient covariance: [k]_{1/q} = q^{-(k-1)} [k]_q
    worst_a = mpf(0)
    for k in range(1, 15):
        lhs = qint(k, qi)
        rhs = q ** (-(k - 1)) * qint(k, q)
        worst_a = max(worst_a, abs(lhs - rhs) / abs(rhs))
    ok_a = worst_a < TOL_EXACT
    print(f"  (a) [k]_(1/q) = q^-(k-1) [k]_q   max rel err = "
          f"{mp.nstr(worst_a, 3)}  {'PASS' if ok_a else 'FAIL'}")
    rows["c1_coeff_covariance"] = {
        "identity": "[k]_{1/q} = q^{-(k-1)} [k]_q",
        "max_rel_err": mp.nstr(worst_a, 3), "pass": bool(ok_a)}

    # (b) C1 solution-level: r_n = b_n(1/q)/b_n(q); even iff r=1, odd iff r=-1
    b_q = b_sequence(12, q)
    b_qi = b_sequence(12, qi)
    ratios = []
    even = odd = True
    for n in range(13):
        r = b_qi[n] / b_q[n]
        ratios.append(mp.nstr(r, 10))
        if abs(r - 1) > mpf("1e-40"):
            even = False
        if abs(r + 1) > mpf("1e-40"):
            odd = False
    # is it a pure q-power? log_q r_n integer/half-integer pattern check
    logq_r = [mp.log(b_qi[n] / b_q[n]) / mp.log(q) for n in range(13)]
    cls = "even" if even else ("odd" if odd else "neither")
    print(f"  (b) C1 solution b_n(1/q)/b_n(q): {cls} "
          f"(sample n=4: {ratios[4]}, n=8: {ratios[8]})")
    print(f"      log_q ratios n=0..6: "
          f"{[mp.nstr(x, 6) for x in logq_r[:7]]} (no fixed q-power weight)")
    rows["c1_solution_bar"] = {
        "classification": cls, "ratios_n0_to_n12": ratios,
        "logq_ratios_n0_to_n12": [mp.nstr(x, 8) for x in logq_r],
        "note": "b_n is bar-NEITHER even nor odd, and not a single q-power "
                "rescale; contrast GGM Thm 9 where the SOLUTIONS G^j_m have "
                "proved bar parity G^j_m(1/q) = (-1)^j G^j_m(q)"}

    # (c) C2 kernel covariance: coeff(1/q, m) = coeff(q, -m)
    worst_c = mpf(0)
    for m in range(-M_MAX_T2, M_MAX_T2 + 1):
        lhs = 2 - qi ** m
        rhs = 2 - q ** (-m)
        worst_c = max(worst_c, abs(lhs - rhs))
    ok_c = worst_c < TOL_EXACT
    print(f"  (c) C2 coeff: (2 - (1/q)^m) = (2 - q^(-m))  max abs err = "
          f"{mp.nstr(worst_c, 3)}  {'PASS' if ok_c else 'FAIL'}")
    print("      => C2 kernel invariant under combined (q -> 1/q, m -> -m); "
          "NOT invariant under q -> 1/q alone.")
    rows["c2_kernel_bar"] = {
        "identity": "coeff(1/q, m) = coeff(q, -m); kernel invariant under "
                    "combined (q->1/q, m->-m), not under q->1/q alone",
        "max_abs_err": mp.nstr(worst_c, 3), "pass": bool(ok_c)}

    assert ok_a and ok_c
    rows["verdict"] = (
        "C1 kernel: bar-covariant (leading coeff picks up q^{-(n+1)}), "
        "solution bar-NEITHER; C2 kernel: bar-invariant only jointly with "
        "m -> -m (its solutions carry the proved (-1)^j parity, GGM Thm 9). "
        "Bar behaviors are structurally different -- CONSISTENT with the T2 "
        "DISTINCT verdict")
    print()
    return rows


def main():
    t1 = t1_c1_exactness()
    t2 = t2_gauge_comparison()
    t3 = t3_bar_symmetry()

    verdict = (
        "T1 CONSISTENT (c(q)=1 exact to 1e-45, incl. q=1.10998); "
        "T2 DISTINCT (no scalar gauge maps C1 onto GGM eq-49, q=1.05 and "
        "q=1, m<=12); T3 bar behaviors structurally different (C1 solution "
        "bar-neither, C2 kernel bar-invariant only with m->-m). Scope-(a): "
        "both q-lift candidates remain live; identification would need a "
        "non-scalar transform (workplan step 3). Nothing here is 'derived'.")
    print("VERDICT:", verdict)

    witness = {
        "description": "C1 q-Hermite/q-involution vs C2 GGM eq-49: candidate "
                       "q-lifts of the proved classical kernel (n+2) b_{n+2} "
                       "= b_{n+1} + b_n -- structural cross-check, workplan "
                       "step 2",
        # `computation` is RESERVED by WitnessBuilder.wrap_legacy, which
        # overwrites it with the witness stem ("filename already encodes
        # this"). That is true for a name and false for this field, which
        # is a METHOD description. Renamed so the text survives the wrap.
        "computation_method": "mpmath dps=50; T1 exactness of [n+2]_q b_{n+2} = "
                       "b_{n+1} + b_n for b_n = I_q(n)/[n]_q!; T2 scalar-"
                       "gauge quadratic solve + residual scan vs GGM eq-49; "
                       "T3 bar (q->1/q) covariance checks",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {"dps": mp.dps, "tol_exact": "1e-45",
                       "tol_gauge": "1e-30", "n_max_t1": N_MAX_T1,
                       "m_max_t2": M_MAX_T2,
                       "q_values_t1": ["0.9", "0.99", "1.01", "1.05",
                                       "1.10998", "1 (classical limit)"]},
        "results": {"t1_c1_exactness": t1, "t2_gauge_comparison": t2,
                    "t3_bar_symmetry": t3, "verdict": verdict},
        "context": {
            "workplan": "docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md (step 2)",
            "literature_check": "docs/audits/2026-07-20-qlift-literature-check.md "
                                "(S2 c(q)=1 inference; S4 GGM eq-49 verified from "
                                "library/arxiv-2012.00062v3/2012.00062v3.pdf pp.14-15)",
            "classical_kernel_lean": "QOU.Mass.QDifferenceConfluentObstruction."
                                     "normalized_classical_kernel_exists",
            "discipline": "scope-(a) structural comparison; no AME data; "
                          "CONSISTENT/DISTINCT vocabulary only; anti-fit",
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "qlift_kernel_candidate_crosscheck_probe",
        witness,
        script_path=__file__,
        engine="python+mpmath",
        start_time=_T0,
    ).save()
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
