#!/usr/bin/env python3
r"""
hmin_closed_form_and_rev_sublinearity_probe.py — H_min in closed form; REV is SUB-LINEAR (qou-hok7)

Two results, and a correction to a published inference in the corpus.

## 1. `H_min(n)` has an exact closed form -- so `deg Z_n` does too

`zn_hook_length_closed_form_probe.py` derived `deg Z_n = n^2 - H_min(n)`, with
`H_min(n) := min_{lambda |- n} sum_c h(c)`.  Computing that by minimising over partitions costs
`p(n)`.  It is not necessary.  From `d2 H_min(n) = [n triangular]` (equivalent to the corpus's
`d2 deg = 2 - [n triangular]`) plus the two initial values `H_min(1) = 1`, `H_min(2) = 3`:

    H_min(n)  =  2n - 1  +  sum_{k >= 2, T_k <= n-1} (n - T_k),        T_k = k(k+1)/2      (H)

`H_min` is therefore computable in `O(sqrt n)` at any `n`, with no partition enumeration.

### Its asymptotics, derived

With `K = floor((sqrt(8n+1)-1)/2) ~ sqrt(2n)` triangular numbers below `n`,

    sum_{k<=K} (n - T_k)  =  K n  -  K(K+1)(K+2)/6  ->  sqrt2 n^{3/2} - (sqrt2/3) n^{3/2}
                          =  (2 sqrt2 / 3) n^{3/2}

so  `H_min(n) = (2 sqrt2/3) n^{3/2} + O(n)`  and  `deg Z_n = n^2 - (2 sqrt2/3) n^{3/2} + O(n)`.
At triangular `n = T_k` the minimiser is the staircase and `H_min = k(k+1)(2k+1)/6`, the square
pyramidal number -- an exact identity, checked below.

## 2. REV is SUB-LINEAR -- and therefore cannot carry an `n^{3/2}` signal

`rev_free_energy_over_shapes_probe.py` computes REV exactly as a free energy over shapes.  Extended
here, `REV_n / n` RISES to a maximum near n = 18 and then FALLS, while `REV_n / sqrt(n)` rises
throughout.  So `sqrt(n) << REV_n << n` on the measured range.

## 3. The correction

`deuteron_qborel_slope_derivation_probe.py` D5 concludes:

    "Splitting T2 = log Z_n - ln q_0 n(n-1) into its degree part and its REV part shows
     d2(degree part) = 0 to machine zero at n = 12, 18, 24, 27, 29 -- because none of those is
     triangular. ... The whole -0.165 n^{3/2} signal is therefore REV's."

The premise is right and the inference does not follow.  Exactly:

    T2  =  (n - H_min(n)) ln q_0  +  REV_n

`d2 H_min = [n triangular]`, so the degree part's SECOND DIFFERENCE is a sum of indicators
supported on the triangular numbers -- density `~ sqrt(2/n) -> 0`.  Sampling `d2` at non-triangular
`n` therefore returns zero **by construction**.  But summing that indicator twice gives
`H_min ~ (2 sqrt2/3) n^{3/2}`: the degree part carries the ENTIRE `n^{3/2}` trend, concentrated in
`d2` on a sparse set.  Sampling at generic `n` misses it; it does not show it is absent.

And REV cannot supply it: `REV >= 0` by construction (D2 in that probe), while the measured signal
is NEGATIVE, and REV is sub-linear so it has no `n^{3/2}` component of either sign.

Checks R1-R5 below establish (H), the pyramidal identity, the asymptotic constant, REV's
sub-linearity, and the exact `T2` split.  All comparisons on integers are exact.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

from zn_hook_length_closed_form_probe import (  # noqa: E402
    hooks,
    min_total_hook,
    partitions,
)


def H_min_closed(n: int) -> int:
    """(H): 2n - 1 + sum over triangular T_k <= n-1, k>=2, of (n - T_k).  Exact integer."""
    if n == 1:
        return 1
    tot = 2 * n - 1
    k = 2
    while True:
        Tk = k * (k + 1) // 2
        if Tk > n - 1:
            break
        tot += n - Tk
        k += 1
    return tot


def pyramidal(k: int) -> int:
    return k * (k + 1) * (2 * k + 1) // 6


def log_qint_table(nmax: int) -> list:
    """LOGQ[m] = log [m]_T for m = 0..nmax (LOGQ[0] unused)."""
    tab = [mp.mpf(0)] * (nmax + 1)
    for m in range(1, nmax + 1):
        tab[m] = mp.log((T ** m - 1) / (T - 1))
    return tab


def rev_at(n: int, logq: list) -> tuple:
    """REV_n by the shape free energy, using a precomputed log-q-integer table."""
    Hmin = H_min_closed(n)
    log_fact = mp.mpf(0)
    for i in range(1, n + 1):
        log_fact += logq[i]
    best = None
    Ls = []
    for lam in partitions(n):
        H = 0
        log_den = mp.mpf(0)
        conj = [0] * (lam[0] + 1)
        for j in range(lam[0]):
            conj[j] = sum(1 for p in lam if p > j)
        for i, row in enumerate(lam):
            for j in range(row):
                h = row - j + conj[j] - i - 1
                H += h
                log_den += logq[h]
        log_term = (H - n) * LNQ + log_fact - log_den
        R = log_term - (n * n - H) * LNQ
        L = R - (H - Hmin) * LNQ
        Ls.append(L)
        if best is None or L > best:
            best = L
    s = mp.mpf(0)
    for L in Ls:
        s += mp.e ** (L - best)
    return (best + mp.log(s), Hmin, len(Ls))


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)
        return bool(ok)

    print("=" * 78)
    print("H_min closed form, and REV sub-linearity   (qou-hok7)")
    print("=" * 78)

    # ---- R1: (H) against brute-force minimisation over partitions
    NB = 26
    bad = []
    for n in range(1, NB + 1):
        brute, _arg = min_total_hook(n)
        if H_min_closed(n) != brute:
            bad.append((n, H_min_closed(n), brute))
    check(
        "R1_Hmin_closed_form_matches_brute_force",
        not bad,
        f"(H) reproduces min_lambda sum_c h(c) exactly for every n=1..{NB} ({len(bad)} "
        f"disagreements), against a full minimisation over all partitions. Exact integers. "
        f"(H) costs O(sqrt n); the minimisation costs p(n).",
    )

    # ---- R2: pyramidal identity at triangular n
    bad2 = []
    for k in range(1, 40):
        n = k * (k + 1) // 2
        if H_min_closed(n) != pyramidal(k):
            bad2.append((k, n, H_min_closed(n), pyramidal(k)))
    check(
        "R2_Hmin_at_triangular_is_square_pyramidal",
        not bad2,
        f"H_min(T_k) = k(k+1)(2k+1)/6 for k=1..39 ({len(bad2)} failures) -- e.g. "
        f"k=6: n=21, H_min=91=pyramidal(6). The staircase (k,k-1,...,1) has total hook length "
        f"sum_{{i<=k}} i^2, which is why triangular n are exactly the exceptional points.",
    )

    # ---- R3: the asymptotic constant 2 sqrt2 / 3
    target = 2 * mp.sqrt(2) / 3
    ratios = []
    for n in [100, 1000, 10000, 100000, 1000000]:
        r = mp.mpf(H_min_closed(n)) / (mp.mpf(n) ** mp.mpf("1.5"))
        ratios.append((n, r))
    last = ratios[-1][1]
    check(
        "R3_Hmin_asymptotic_constant",
        abs(last - target) < mp.mpf("0.002"),
        f"H_min(n)/n^(3/2) -> 2*sqrt(2)/3 = {mp.nstr(target, 10)}; at n=10^6 the exact value of "
        f"(H) gives {mp.nstr(last, 10)} (|diff| = {mp.nstr(abs(last - target), 4)}). "
        f"Sequence: " + ", ".join(f"n={n}:{mp.nstr(r, 8)}" for n, r in ratios),
    )

    # ---- R4 / M1: REV sub-linearity, extended
    NMAX = 44
    logq = log_qint_table(NMAX + 1)
    print()
    print("-" * 78)
    print("REV extended (exact free energy over shapes; H_min from (H)):")
    print(f"  {'n':>3} {'REV':>12} {'REV/n':>11} {'REV/sqrt n':>11} {'H_min':>7} {'p(n)':>8}")
    table = []
    for n in list(range(4, 21, 2)) + [24, 28, 32, 36, 40, NMAX]:
        rev, Hmin, npart = rev_at(n, logq)
        row = {"n": n, "REV": mp.nstr(rev, 14), "REV_over_n": mp.nstr(rev / n, 10),
               "REV_over_sqrt_n": mp.nstr(rev / mp.sqrt(n), 10), "H_min": Hmin,
               "p_n": npart}
        table.append(row)
        print(f"  {n:>3} {mp.nstr(rev, 9):>12} {mp.nstr(rev/n, 8):>11} "
              f"{mp.nstr(rev/mp.sqrt(n), 8):>11} {Hmin:>7} {npart:>8}")

    ron = [(r["n"], mp.mpf(r["REV_over_n"])) for r in table]
    peak_n, peak_v = max(ron, key=lambda t: t[1])
    last_n, last_v = ron[-1]
    declining = last_v < peak_v
    ros = [(r["n"], mp.mpf(r["REV_over_sqrt_n"])) for r in table]
    rising = ros[-1][1] > ros[-2][1] > ros[-3][1]
    check(
        "R4_REV_is_sublinear",
        declining and rising,
        f"REV/n peaks at n={peak_n} ({mp.nstr(peak_v, 8)}) and falls to {mp.nstr(last_v, 8)} at "
        f"n={last_n}, while REV/sqrt(n) rises monotonically over the last three points "
        f"({', '.join(mp.nstr(v, 7) for _n, v in ros[-3:])}). So sqrt(n) << REV_n << n on the "
        f"measured range. MEASURED over n<={NMAX}, not proved for all n.",
    )

    # ---- R5: the exact T2 split, and what it implies about D5
    print()
    print("-" * 78)
    print("T2 = log Z_n - ln q0 * n(n-1)  =  (n - H_min) ln q0 + REV   [exact identity]")
    print(f"  {'n':>3} {'T2':>12} {'degree part':>13} {'REV part':>11} {'deg/T2':>9}")
    t2rows = []
    for r in table:
        n = r["n"]
        rev = mp.mpf(r["REV"])
        degpart = (mp.mpf(n) - mp.mpf(r["H_min"])) * LNQ
        t2 = degpart + rev
        frac = degpart / t2 if t2 != 0 else mp.mpf(0)
        t2rows.append({"n": n, "T2": mp.nstr(t2, 12), "degree_part": mp.nstr(degpart, 12),
                       "REV_part": mp.nstr(rev, 12)})
        print(f"  {n:>3} {mp.nstr(t2, 8):>12} {mp.nstr(degpart, 8):>13} "
              f"{mp.nstr(rev, 8):>11} {mp.nstr(frac, 6):>9}")

    # R5 tests the claim that actually matters: the n^{3/2} coefficient belongs to the degree
    # part and REV has none.  It deliberately does NOT compare their magnitudes at the largest
    # reachable n -- an earlier version of this probe did, asserted |degree| > |REV|, and FAILED,
    # because the two cross at almost exactly n = 44 (degree 24.21 vs REV 28.60).  "Grows faster"
    # and "is already bigger" are different claims and only the first one is true here.
    deg_ratio = []
    for n in [100, 1000, 10000, 100000, 1000000]:
        dp = (mp.mpf(n) - mp.mpf(H_min_closed(n))) * LNQ
        deg_ratio.append((n, dp / (mp.mpf(n) ** mp.mpf("1.5"))))
    target_coeff = -(2 * mp.sqrt(2) / 3) * LNQ
    deg_ok = abs(deg_ratio[-1][1] - target_coeff) < mp.mpf("0.0005")

    rev_ratio = [(r["n"], mp.mpf(r["REV"]) / (mp.mpf(r["n"]) ** mp.mpf("1.5"))) for r in table]
    rev_falling = rev_ratio[-1][1] < rev_ratio[-2][1] < rev_ratio[-3][1]

    print()
    print(f"  degree_part / n^(3/2) -> {mp.nstr(target_coeff, 10)} : "
          + ", ".join(f"n={n}:{mp.nstr(v, 8)}" for n, v in deg_ratio))
    print("  REV / n^(3/2) (falling toward 0): "
          + ", ".join(f"n={n}:{mp.nstr(v, 7)}" for n, v in rev_ratio[-4:]))

    check(
        "R5_the_n32_coefficient_belongs_to_the_degree_and_REV_has_none",
        deg_ok and rev_falling,
        f"degree_part/n^(3/2) converges to -(2sqrt2/3) ln q0 = {mp.nstr(target_coeff, 10)} "
        f"(at n=10^6, {mp.nstr(deg_ratio[-1][1], 10)}), computed from the closed form (H) with no "
        f"partition enumeration. Meanwhile REV/n^(3/2) FALLS over the last three points "
        f"({', '.join(mp.nstr(v, 6) for _n, v in rev_ratio[-3:])}), consistent with REV being "
        f"sub-linear (R4) and so having no n^(3/2) component. Since REV >= 0 by construction and "
        f"the measured residual is NEGATIVE, the n^(3/2) signal can only be the degree's. "
        f"This CORRECTS D5 of deuteron_qborel_slope_derivation_probe.py, which attributed it to "
        f"REV because d2(degree part) = 0 at the sampled non-triangular n -- true, but d2 of the "
        f"degree part is an indicator supported on the triangular numbers, so sampling at "
        f"generic n returns zero BY CONSTRUCTION rather than showing the degree contributes "
        f"nothing. NOTE the two parts cross near n=44 and REV is the LARGER there; the claim is "
        f"about the n^(3/2) coefficient, not about which term dominates at reachable n.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "hmin_closed_form_and_rev_sublinearity_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "H_min_closed_form": "H_min(n) = 2n - 1 + sum_{k>=2, T_k <= n-1} (n - T_k)",
        "H_min_asymptotic": "(2 sqrt2 / 3) n^{3/2} + O(n)",
        "deg_Z_closed_form": "deg Z_n = n^2 - H_min(n)",
        "corrects": ("D5 of deuteron_qborel_slope_derivation_probe.py: the n^{3/2} residual is "
                     "the DEGREE part, not REV"),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "rev_table": table,
        "t2_split": t2rows,
    }
    out = os.path.join(_COMPUTATIONS, "hmin-closed-form-rev-sublinearity.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")

    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
