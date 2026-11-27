#!/usr/bin/env python3
"""Level-selection rule k(A): which structural form does the data demand?

Follow-on to wlambda_jet_tower_connected_probe.py, which found the connected
standard-channel tower weight w_std(k) grows super-geometrically (extensive-
capable) and pinned the open piece to the LEVEL-SELECTION rule k(A) (= GAP-A-3).
This probe asks, SCALE-FREE and with NO ansatz search, which named structural
form k(A) the AME binding actually demands.

Method (fit-free; tests the FORM of k(A) only — sets NO absolute scale, closes
nothing):
  1. Tabulate the monotonic universal tower weight
        w_std(k) = Sigma_{lambda|-k} W_lambda * mult_(2,1)(lambda|H_3)
     for k = 3..KMAX (exact branching; skew cells <= 7 so count_syt_skew is exact).
  2. The connected picture says B(K) ~ (scale) * w_std(k(A)). RATIOS against the
     LIGHTEST nucleus (2H) cancel the scale:
        w_std(k_implied(A)) / w_std(k(2H)) = B_AME(A) / B_AME(2H).
     Invert the monotonic w_std table (log-linear interp) -> implied level per
     nucleus. One reference calibrates the scale; the rest are SHAPE predictions.
  3. Robust structural claim: because w_std grows super-geometrically while B is
     ~extensive (B ~ A saturation), k_implied(A) must be strongly SUB-LINEAR in A
     -> the naive k~A and k~bond-count candidates are FALSIFIED (a-scope). Report
     the best-fitting NAMED form (log A / log bonds) as an observation (all R^2),
     no search over a family.

Tests only the k(A) FORM. Sets no binding scale, wires nothing, lands no absolute
magnitude. No fit beyond the single reference-scale calibration.

Usage:
    python3 wlambda_level_selection_kA_probe.py

NORMALIZATION (2026-09-05, bean qou-uk8o). w_std(k) now uses the SELF-NORMALIZED
q-Plancherel weight d_q^2 / Sigma_mu d_q^2. The textbook d_q^2/[k]_q! is a
probability measure at q = 1 only; at q_0 it sums to c_k = 0.9874 .. 1.1782
over k = 3..10, so every level carried a different factor while this probe
inverts the whole table against B_AME ratios anchored at k = 3 -- a comparison
ACROSS k, where c_k does not cancel.

Both assertions still pass and the ordering of the four candidate forms is
unchanged; every R^2 moves up slightly:

    k ~ log(bond count)  0.8912 -> 0.8966
    k ~ log A            0.8633 -> 0.8695
    k ~ A (mass)         0.6721 -> 0.6807
    k ~ bond count       0.4853 -> 0.4939

k_implied span 3.00->8.52 becomes 3.00->8.61 (still x2.9 against A's x8).
"""
import datetime
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
from itertools import permutations

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.abspath(os.path.join(_HERE, ".."))
for _p in (_COMP, os.path.join(_COMP, "hecke"), os.path.join(_COMP, "substrate")):
    sys.path.insert(0, _p)

from hecke_characters import partitions_of, dim_q, qfac  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()
Q0_MP = Q_MP   # same proton pin as Q0_PROTON, at compute dps

KMAX = 10

# AME2020 binding energies B (MeV), light nuclei (well-known constants).
NUCLEI = [("2H", 2, 2.224), ("3H", 3, 8.482), ("3He", 3, 7.718),
          ("4He", 4, 28.296), ("6Li", 6, 31.994), ("7Li", 7, 39.245),
          ("9Be", 9, 58.165), ("12C", 12, 92.162), ("16O", 16, 127.619)]


def contains(lam, mu):
    for i in range(len(mu)):
        if i >= len(lam) or lam[i] < mu[i]:
            return False
    return True


def count_syt_skew(lam, mu):
    lam = list(lam)
    mu = list(mu) + [0] * (len(lam) - len(mu))
    cells = [(i, j) for i in range(len(lam)) for j in range(mu[i], lam[i])]
    n = len(cells)
    if n <= 1:
        return 1
    count = 0
    for perm in permutations(range(n)):
        filling = {cells[idx]: perm[idx] for idx in range(n)}
        ok = True
        for (i, j), val in filling.items():
            if (i, j + 1) in filling and filling[(i, j + 1)] < val:
                ok = False; break
            if (i + 1, j) in filling and filling[(i + 1, j)] < val:
                ok = False; break
        if ok:
            count += 1
    return count


def _q_int(m, q):
    """[m]_q = (q^m - q^-m)/(q - q^-1), balanced convention, in mpmath."""
    return (q ** m - q ** (-m)) / (q - 1 / q)


def _q_fact(m, q):
    r = mp.mpf(1)
    for j in range(1, m + 1):
        r *= _q_int(j, q)
    return r


def _dim_q(lam, q):
    """d_q(lambda) = [n]_q!/prod_cells [h]_q, in mpmath (local: the shared
    hecke_characters.dim_q returns a builtin float)."""
    num = _q_fact(sum(lam), q)
    den = mp.mpf(1)
    for r, row in enumerate(lam):
        for c in range(row):
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            den *= _q_int(arm + leg + 1, q)
    return num / den


def normalization_c(k):
    """c_k = Sigma_{lambda |- k} d_q(lambda)^2/[k]_q!, the amount by which the
    textbook q-Plancherel weight fails to be a probability measure at q_0.

    0.9874 / 0.9822 / 0.9822 / 0.9911 / 1.0124 / 1.0506 / 1.1109 / 1.1782 at
    k = 3..10 (docs/audits/2026-09-04-plancherel-convention-gap.md). It varies
    with k, so an unnormalized w_std(k) carries a DIFFERENT factor at every
    level -- and this probe inverts the whole k-table against B_AME ratios
    anchored at k = 3, which is a comparison ACROSS k. Bean qou-uk8o.
    """
    nfac = _q_fact(k, Q0_MP)
    return sum((_dim_q(lam, Q0_MP) ** 2 / nfac for lam in partitions_of(k)),
               mp.mpf(0))


def w_std_of_k(k, self_normalized=True):
    """Sigma_{lambda |- k, lambda >= (2,1)} W_lambda * mult_(2,1), with
    W_lambda self-normalized to a probability measure (pass False for the
    historical d_q^2/[k]_q! form)."""
    nfac = _q_fact(k, Q0_MP)
    denom = normalization_c(k) if self_normalized else mp.mpf(1)
    s = mp.mpf(0)
    for lam in partitions_of(k):
        if contains(lam, (2, 1)):
            s += (_dim_q(lam, Q0_MP) ** 2 / nfac / denom) * count_syt_skew(lam, (2, 1))
    return s


def invert_wstd(table, ks, target):
    if target <= 0:
        return None
    if target < table[0]:
        # log-linear extrapolation below k=3 using the first two points.
        # mp.log, not math.log: the table is mpf now and math.log would coerce
        # every entry through binary64.
        return ks[0] + (mp.log(target) - mp.log(table[0])) / \
            (mp.log(table[1]) - mp.log(table[0]))
    if target > table[-1]:
        return None
    for i in range(1, len(table)):
        if table[i] >= target:
            lo, hi = table[i - 1], table[i]
            frac = (mp.log(target) - mp.log(lo)) / (mp.log(hi) - mp.log(lo))
            return ks[i - 1] + frac
    return None


def pearson_r2(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    return (sxy ** 2) / (sxx * syy) if sxx and syy else 0.0


def main() -> int:
    assertions = []

    def rec(name, passed, detail):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}: {detail}")
        return passed

    ks = list(range(3, KMAX + 1))
    table = [w_std_of_k(k) for k in ks]
    print("w_std(k) (exact branching):")
    for k, w in zip(ks, table):
        print(f"  k={k:<3} w_std={float(w):.6f}  (c_k={float(normalization_c(k)):.6f})")
    ratios = [table[i] / table[i - 1] for i in range(1, len(table))]
    print(f"  successive ratios: {[round(float(r),3) for r in ratios]} (increasing "
          f"-> super-geometric)\n")

    refname, refA, refB = NUCLEI[0]           # 2H — lightest
    w_ref = table[0]                          # k(2H) := 3
    print(f"reference = {refname} (B={refB} MeV) calibrated to w_std(k=3)={float(w_ref):.4f}\n")
    print(f"{'nucleus':<8}{'A':<4}{'bonds':<7}{'B_AME':<9}{'k_implied':<11}"
          f"{'logA':<8}{'log(bonds)':<11}")
    rows = {}
    kimp, As, logAs, bonds, logbonds = [], [], [], [], []
    for name, A, B in NUCLEI:
        nb = A * (A - 1) // 2
        target = w_ref * B / refB
        ki = invert_wstd(table, ks, target)
        rows[name] = dict(A=A, bonds=nb, B=B,
                          k_implied=(fmt(ki) if ki is not None else None))
        s = f"{name:<8}{A:<4}{nb:<7}{B:<9}"
        if ki is not None:
            s += f"{float(ki):<11.4f}{math.log(A):<8.4f}{math.log(nb):<11.4f}"
            kimp.append(ki); As.append(A); logAs.append(math.log(A))
            bonds.append(nb); logbonds.append(math.log(nb))
        else:
            s += "(out of range)"
        print(s)

    r2 = {
        "k ~ A (mass)": pearson_r2(As, kimp),
        "k ~ bond count": pearson_r2(bonds, kimp),
        "k ~ log A": pearson_r2(logAs, kimp),
        "k ~ log(bond count)": pearson_r2(logbonds, kimp),
    }
    print("\nR^2 of k_implied(A) vs each NAMED structural candidate:")
    for form, val in sorted(r2.items(), key=lambda x: -x[1]):
        print(f"  {form:<22} R^2 = {val:.4f}")
    best = max(r2, key=r2.get)

    # Robust structural claim: k_implied is strongly SUB-LINEAR in A.
    A_span = max(As) / min(As)
    k_span = max(kimp) / min(kimp)
    sublinear = k_span < 0.5 * A_span
    all_ok = True
    all_ok &= rec("k_implied_strongly_sublinear_in_A",
                  sublinear,
                  f"A spans x{A_span:.1f} ({min(As)}->{max(As)}) while k_implied spans "
                  f"only x{k_span:.2f} ({min(kimp):.2f}->{max(kimp):.2f}) -> STRONGLY "
                  f"sub-linear; naive k~A and k~bond-count FALSIFIED (a-scope)")
    all_ok &= rec("log_forms_beat_linear",
                  (r2["k ~ log A"] > r2["k ~ A (mass)"]) and
                  (r2["k ~ log A"] > r2["k ~ bond count"]),
                  f"k~log A R^2={r2['k ~ log A']:.3f} beats k~A R^2="
                  f"{r2['k ~ A (mass)']:.3f} and k~bonds R^2={r2['k ~ bond count']:.3f} "
                  f"(best-fitting NAMED form: '{best}')")

    verdict = (f"k(A) FORM CONSTRAINED (scale-free, no closure): inverting the exact "
               f"tower weight w_std(k) against AME B(A) ratios (ref=2H), the implied "
               f"level k_implied(A) is STRONGLY SUB-LINEAR in A (A x{A_span:.0f}, k only "
               f"x{k_span:.1f}) — so the naive k~A and k~bond-count candidates are "
               f"FALSIFIED (a-scope). The best-fitting named form is '{best}' "
               f"(R^2={r2[best]:.3f}); k~log A (R^2={r2['k ~ log A']:.3f}) clearly beats "
               f"linear. NOTE log A and log(bond-count) are statistically "
               f"INDISTINGUISHABLE here (both ~0.87-0.89, near-collinear for these "
               f"nuclei) — the robust claim is LOG-TYPE, not log-A-vs-log-bonds. This is "
               f"the arithmetic consequence of w_std growing super-geometrically while B "
               f"is ~extensive: the jet level grows ~log(mass). GAP-A-3 is thereby "
               f"constrained to a LOG-TYPE k(A). Sets no scale, wires nothing, lands no "
               f"magnitude; the open piece is WHY k(A)~log from the drivers. Light nuclei "
               f"are below saturation so residual scatter (R^2~0.88, not ~1) is expected.")
    print(f"\nVERDICT: {verdict}")

    with open(os.path.abspath(__file__), "rb") as _f:
        src = _f.read()
    try:
        commit_sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=_HERE,
                                    capture_output=True, text=True, check=True).stdout.strip() or "unknown"
    except Exception:
        commit_sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "computation": "wlambda-level-selection-kA",
        "engine": "python",
        "engineVersion": platform.python_version(),
        "scriptFile": os.path.basename(__file__),
        "commitSha": commit_sha,
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "description": (
            "Scale-free k(A) form test: inverting exact w_std(k) against AME B(A) ratios "
            "(ref=2H), k_implied is strongly sub-linear in A -> falsifies naive k~A and "
            "k~bond-count; best-fitting named form is logarithmic. Constrains GAP-A-3 to "
            "a log-type rule; no scale, no wiring, no closure."
        ),
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "assertions": assertions,
        "allPassed": all_ok,
        "result": {"w_std_table": {str(k): fmt(w) for k, w in zip(ks, table)},
                   "normalization_c_k": {str(k): fmt(normalization_c(k)) for k in ks},
                   "weight_convention": (
                       "W_lambda = d_q^2 / Sigma_mu d_q^2 (SELF-NORMALIZED "
                       "q-Plancherel). The textbook d_q^2/[k]_q! is a "
                       "probability measure at q=1 only; at q_0 it sums to "
                       "c_k, recorded above, which varies with k -- and this "
                       "probe compares w_std ACROSS k, so c_k does not "
                       "cancel. Bean qou-uk8o; "
                       "docs/audits/2026-09-04-plancherel-convention-gap.md"),
                   "nuclei": rows, "R2_by_form": {k: fmt(v) for k, v in r2.items()},
                   "best_form": best,
                   "verdict": verdict},
        "context": {
            "builds_on": "wlambda_jet_tower_connected_probe.py (w_std super-geometric)",
            "open_object": "GAP-A-3 level selection k(A); constrains its FORM to log-type",
            "scope": "FORM of k(A) only; scale-free; no absolute magnitude; no fit search; no closure",
            "AME_source": "AME2020 binding energies (light nuclei)",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "wlambda-level-selection-kA.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
