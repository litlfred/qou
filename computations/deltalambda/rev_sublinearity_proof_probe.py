#!/usr/bin/env python3
r"""
rev_sublinearity_proof_probe.py — REV = Omega(sqrt n) PROVED; the upper bound FAILED (qou-hok7)

🛑 READ THE TITLE AS WRITTEN.  This file set out to prove REV sub-linear and got HALF of it: the
lower bound is proved, the upper bound is not, because the lemma the upper bound rested on is
false.  An earlier version of this line read "REV is PROVED sub-linear: Omega(sqrt n) <= REV <=
O(n^{3/4})" while the body below already documented the refutation -- i.e. the heading contradicted
its own contents, which is precisely the defect that makes a skimming reader quote a withdrawn
result.  The file name is left unchanged so the probe's identity is stable; the name is now
aspirational, not descriptive.

`qou-hok7`'s one remaining open piece is REV's asymptotics.  The previous tranche
(`hmin_closed_form_and_rev_sublinearity_probe.py`) MEASURED sub-linearity over n <= 44 and said so.
This probe makes `R_lambda` explicit, which proves the LOWER bound and supplies a sharp conjectured
constant -- and leaves sub-linearity itself exactly as it found it: measured, not proved.

## The key identity (exact)

Write `t = q_0^2` and `[m]_t = (t^m - 1)/(t - 1) = t^{m-1} * sigma_m` with
`sigma_m := (1 - t^{-m})/(1 - t^{-1})`, increasing from `sigma_1 = 1` to `sigma_inf`.  Put

    eps_m  :=  log sigma_inf - log sigma_m  =  -log(1 - t^{-m})  =  -log(1 - q_0^{-2m})  >  0 ,

which DECAYS GEOMETRICALLY (ratio `q_0^{-2} = 0.8117`), so `C := sum_{m>=1} eps_m` converges.
Substituting into the closed form `term_lambda(q) = q^{H-n} [n]_{q^2}!/prod_c [h(c)]_{q^2}`, every
power of `t` cancels against `deg = n^2 - H` and

    R_lambda  =  sum_{c in lambda} eps_{h(c)}  -  sum_{i=1}^{n} eps_i .                      (E)

So `R_lambda` depends on `lambda` ONLY through its hook multiset, and needs no polynomial algebra.

## Two lemmas

  L1 (one per row).  Hook lengths strictly decrease along a row, so each row holds at most one cell
      of any given hook length:  `N_m(lambda) <= min(ell(lambda), lambda_1) =: r(lambda)`
      (the column bound is the conjugate statement).  Hence by (E),
          R_lambda  <=  C * r(lambda) .
  L2 (ATTEMPTED, and REFUTED -- see below).  "If `r(lambda) = r` then `H(lambda) >= 3r^2-3r+1`."

## 🛑 THE UPPER BOUND IS NOT PROVED.  L2 IS FALSE, AND IT WAS MINE.

The first version of this probe claimed to prove `REV = O(n^{3/4})` via L2, whose derivation ran:
row 1 and column 1 each have `>= r` cells, so `h(1,j) >= 2r-j` and `h(i,1) >= 2r-i`, and summing
both arms gives `H >= 3r^2-3r+1`.

**The step `h(1,j) >= 2r-j` assumes column `j` has `>= r` cells for every `j <= r`.  Only column 1
does.**  R3 below now runs the bound as a REFUTATION test and finds **1168 counterexamples at
n <= 22 alone**.  The sharpest is the hook shape `lambda = (11, 1^10)`, where
`r = min(ell, lambda_1) = 11` but `lambda'_2 = 1`, so `h(1,2) = 10`, not the `>= 20` the argument
needs; `H = 131` against a claimed bound of `331`.

Everything downstream of L2 goes with it: the `r > M` shapes are NOT shown to be energy-killed,
so `REV = O(n^{3/4})` is **withdrawn**.  R7 below records the collapse rather than the bound.

Note the failure mode.  A hook shape is "thick" by the `min(ell, lambda_1)` measure and
"thin" by every measure that matters for hook lengths -- `r` is simply the wrong statistic to
couple `R_lambda` to `H(lambda)`.  Bound R4 (`R_lambda <= C*r`) survives, being a consequence of
L1 alone, but it is far too loose to be useful here: on that same hook shape it gives
`R <= 67.9` where the truth is `R ~ C = 6.17`.

## What IS proved

  LOWER.  At triangular `n = T_k` the staircase `delta_k` attains `H_min`, so its energy is ZERO
  and `REV_n >= R_{delta_k}`.  The staircase's hooks are exactly the odd numbers with
  `N_{2j-1}(delta_k) = k - j + 1`, so
      R_{delta_k}  =  sum_{j=1}^{k} (k-j+1) eps_{2j-1}  -  sum_{i<=n} eps_i  ->  A*k,
      A := sum_{j>=1} eps_{2j-1},   k = sqrt(2n) .
  Hence `REV_n >= (A*sqrt2 - o(1)) sqrt(n)`, i.e. **REV = Omega(sqrt n)** -- proved, and this one
  does not depend on L2.

## Status of the open question

PROVED here: identity (E), L1, and `REV = Omega(sqrt n)`.
NOT PROVED: any upper bound at all.  Sub-linearity therefore remains **MEASURED** (n <= 44,
`hmin_closed_form_and_rev_sublinearity_probe.py`), exactly as it was before this probe -- the
attempted proof failed and is recorded as a failure, not quietly weakened.
CONJECTURED: `REV_n ~ A*sqrt(2n)`, i.e. `REV/sqrt(n) -> A*sqrt2`.  The staircase lower bound
approaches that constant from below, so the conjecture is that the lower bound is TIGHT.

What a repair would need: a statistic `s(lambda)` that (i) bounds `sum_m eps_m N_m(lambda)` from
above and (ii) is genuinely forced up by `H(lambda) - H_min`.  `r = min(ell, lambda_1)` has
property (i) and demonstrably NOT (ii).
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
    conjugate,
    hooks,
    partitions,
)
from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402


def eps(m: int):
    return -mp.log(1 - T ** (-m))


def eps_table(nmax: int) -> list:
    return [mp.mpf(0)] + [eps(m) for m in range(1, nmax + 1)]


def R_direct(lam: tuple, n: int, logq: list):
    """R_lambda from the q-integer definition (the route the previous probe used)."""
    hs = hooks(lam)
    H = sum(hs)
    log_fact = sum(logq[i] for i in range(1, n + 1))
    log_den = sum(logq[h] for h in hs)
    log_term = (H - n) * LNQ + log_fact - log_den
    return log_term - (n * n - H) * LNQ


def R_eps(lam: tuple, n: int, et: list):
    """R_lambda from identity (E): sum_c eps_{h(c)} - sum_{i<=n} eps_i."""
    return sum(et[h] for h in hooks(lam)) - sum(et[i] for i in range(1, n + 1))


def staircase(k: int) -> tuple:
    return tuple(range(k, 0, -1))


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)
        return bool(ok)

    print("=" * 78)
    print("REV: Omega(sqrt n) PROVED; upper bound WITHDRAWN (my lemma L2 was false)   (qou-hok7)")
    print("=" * 78)

    NB = 22
    et = eps_table(4 * NB + 400)
    logq = [mp.mpf(0)] + [mp.log((T ** m - 1) / (T - 1)) for m in range(1, NB + 1)]
    C = sum(et[m] for m in range(1, 400))
    A = sum(et[2 * j - 1] for j in range(1, 200))
    print(f"  eps_m = -log(1 - q0^(-2m));  C = sum eps_m = {mp.nstr(C, 10)};  "
          f"A = sum eps_odd = {mp.nstr(A, 10)}")
    print(f"  predicted REV/sqrt(n) limit if the lower bound is tight: "
          f"A*sqrt2 = {mp.nstr(A * mp.sqrt(2), 10)}")
    print()

    # ---- R1: identity (E)
    tol = mp.mpf(10) ** (-(mp.dps - 15))
    worst = mp.mpf(0)
    cnt = 0
    for n in range(1, NB + 1):
        for lam in partitions(n):
            cnt += 1
            d = abs(R_direct(lam, n, logq) - R_eps(lam, n, et))
            worst = max(worst, d)
    check(
        "R1_identity_E_R_lambda_is_a_hook_multiset_sum",
        worst < tol,
        f"R_lambda = sum_c eps_h(c) - sum_{{i<=n}} eps_i verified against the q-integer definition "
        f"for all {cnt} partitions with n <= {NB}; worst |difference| {mp.nstr(worst, 4)} vs "
        f"tolerance {mp.nstr(tol, 4)}. R_lambda therefore depends on lambda only through its hook "
        f"MULTISET -- no polynomial algebra, no transfer operator.",
    )

    # ---- R2 (L1): at most one cell per row with a given hook length
    bad2 = []
    for n in range(1, NB + 1):
        for lam in partitions(n):
            conj = conjugate(lam)
            r = min(len(lam), lam[0])
            cnts: dict = {}
            for i, row in enumerate(lam):
                seen = set()
                for j in range(row):
                    h = row - j + conj[j] - i - 1
                    if h in seen:
                        bad2.append((lam, "row repeat", h))
                    seen.add(h)
                    cnts[h] = cnts.get(h, 0) + 1
            for h, c in cnts.items():
                if c > r:
                    bad2.append((lam, h, c, r))
    check(
        "R2_L1_hook_multiplicity_bounded_by_min_rows_cols",
        not bad2,
        f"N_m(lambda) <= min(ell, lambda_1) for every hook length m and every partition with "
        f"n <= {NB} ({len(bad2)} violations), and hook lengths never repeat within a row. "
        f"Consequence via (E): R_lambda <= C * r(lambda) with C = {mp.nstr(C, 8)}.",
    )

    # ---- R3: L2 is FALSE.  This check now CONFIRMS THE REFUTATION of my own lemma.
    bad3 = []
    worst_slack = None
    for n in range(1, NB + 1):
        for lam in partitions(n):
            r = min(len(lam), lam[0])
            H = sum(hooks(lam))
            bound = 3 * r * r - 3 * r + 1
            if H < bound:
                bad3.append((lam, H, bound))
            slack = H - bound
            if worst_slack is None or slack < worst_slack[0]:
                worst_slack = (slack, lam, H, bound)
    # the hook shape is the canonical counterexample; assert it explicitly so a future edit
    # cannot silently "fix" this check back into a claimed lemma
    hook_shape = (11,) + (1,) * 10
    hs_r = min(len(hook_shape), hook_shape[0])
    hs_H = sum(hooks(hook_shape))
    hs_bound = 3 * hs_r * hs_r - 3 * hs_r + 1
    check(
        "R3_L2_is_REFUTED_thickness_does_not_force_hook_length",
        len(bad3) > 0 and hs_H < hs_bound,
        f"the lemma 'H >= 3r^2-3r+1 with r = min(ell, lambda_1)' -- which an earlier version of "
        f"this probe used to claim REV = O(n^(3/4)) -- is FALSE, with {len(bad3)} counterexamples "
        f"at n <= {NB} alone. Canonical counterexample, the hook shape lambda=(11,1^10): r={hs_r}, "
        f"H={hs_H}, claimed bound {hs_bound}. The bad step was h(1,j) >= 2r-j, which needs column "
        f"j to have >= r cells for all j <= r; only column 1 does (lambda'_2 = 1 here, so "
        f"h(1,2) = 10, not >= 20). Worst slack over the range: lambda={worst_slack[1]}, H="
        f"{worst_slack[2]} vs bound {worst_slack[3]} ({worst_slack[0]}). The upper bound on REV "
        f"is WITHDRAWN; this check passes by confirming the refutation, not the lemma.",
    )

    # ---- R4: R_lambda <= C * r(lambda)
    bad4 = []
    for n in range(1, NB + 1):
        for lam in partitions(n):
            r = min(len(lam), lam[0])
            if R_eps(lam, n, et) > C * r + tol:
                bad4.append((lam, mp.nstr(R_eps(lam, n, et), 8), mp.nstr(C * r, 8)))
    check(
        "R4_R_lambda_bounded_by_C_times_r",
        not bad4,
        f"R_lambda <= C*r(lambda) for every partition with n <= {NB} ({len(bad4)} violations), "
        f"the direct consequence of (E) + L1.",
    )

    # ---- R5: staircase hooks are exactly the odd numbers, with the stated multiplicities
    bad5 = []
    for k in range(1, 30):
        lam = staircase(k)
        hs = sorted(hooks(lam))
        if any(h % 2 == 0 for h in hs):
            bad5.append((k, "even hook"))
        for j in range(1, k + 1):
            want = k - j + 1
            got = sum(1 for h in hs if h == 2 * j - 1)
            if got != want:
                bad5.append((k, 2 * j - 1, got, want))
    check(
        "R5_staircase_hooks_are_odd_with_multiplicity_k_minus_j_plus_1",
        not bad5,
        f"for the staircase delta_k (k=1..29) every hook length is ODD and "
        f"N_{{2j-1}}(delta_k) = k-j+1 exactly ({len(bad5)} violations). Hence "
        f"R_{{delta_k}} = sum_j (k-j+1) eps_{{2j-1}} - sum_{{i<=n}} eps_i -> A*k, A = "
        f"{mp.nstr(A, 8)}.",
    )

    # ---- R6: the lower bound, evaluated at triangular n
    print()
    print("-" * 78)
    print("LOWER BOUND at triangular n = T_k (staircase has ZERO energy, so REV >= R_delta_k):")
    print(f"  {'k':>3} {'n=T_k':>7} {'R_delta_k':>12} {'A*k':>10} {'R/sqrt(n)':>11} "
          f"{'A*sqrt2':>9}")
    lb = []
    for k in range(2, 30):
        n = k * (k + 1) // 2
        etl = eps_table(4 * n + 400)
        lam = staircase(k)
        R = sum(etl[h] for h in hooks(lam)) - sum(etl[i] for i in range(1, n + 1))
        row = {"k": k, "n": n, "R_staircase": mp.nstr(R, 12),
               "A_times_k": mp.nstr(A * k, 12),
               "R_over_sqrt_n": mp.nstr(R / mp.sqrt(n), 10)}
        lb.append(row)
        if k in (2, 3, 5, 8, 12, 17, 23, 29):
            print(f"  {k:>3} {n:>7} {mp.nstr(R, 8):>12} {mp.nstr(A*k, 8):>10} "
                  f"{mp.nstr(R/mp.sqrt(n), 8):>11} {mp.nstr(A*mp.sqrt(2), 7):>9}")
    ratio_last = mp.mpf(lb[-1]["R_over_sqrt_n"])
    target = A * mp.sqrt(2)
    rising = all(mp.mpf(lb[i]["R_over_sqrt_n"]) >= mp.mpf(lb[i - 1]["R_over_sqrt_n"]) - mp.mpf("1e-9")
                 for i in range(len(lb) - 6, len(lb)))
    check(
        "R6_lower_bound_REV_is_Omega_sqrt_n",
        rising and ratio_last > mp.mpf("0.75") * target,
        f"R_{{delta_k}}/sqrt(n) rises to {mp.nstr(ratio_last, 8)} at k=29 (n=435), against the "
        f"asymptote A*sqrt2 = {mp.nstr(target, 8)}. Since the staircase has ZERO energy at "
        f"triangular n, REV_n >= R_{{delta_k}}, so REV = Omega(sqrt n) -- PROVED, not measured. "
        f"(The approach to A*sqrt2 is from below because the -sum_i eps_i term is an O(1) deficit.)",
    )

    # ---- R7: the upper-bound chain, checked numerically at the chosen M
    # ---- R7: the upper bound is WITHDRAWN.  Show that the loose bound R4 cannot substitute.
    print()
    print("-" * 78)
    print("UPPER BOUND: WITHDRAWN (L2 refuted).  How loose R4 is on the counterexample:")
    ub = []
    hook_R = R_eps(hook_shape, sum(hook_shape), et)
    hook_bound = C * hs_r
    print(f"  lambda=(11,1^10):  R_lambda = {mp.nstr(hook_R, 8)}   "
          f"R4 bound C*r = {mp.nstr(hook_bound, 8)}   ratio {mp.nstr(hook_bound/hook_R, 6)}x loose")
    for n in [100, 1000, 10000, 100000, 1000000]:
        hm = mp.mpf(H_min_closed(n))
        ub.append({"n": n, "H_min": str(H_min_closed(n)),
                   "C_times_n_the_only_surviving_R_bound": mp.nstr(C * n, 10),
                   "note": "no upper bound on REV established"})
    check(
        "R7_upper_bound_WITHDRAWN_not_established",
        True,
        f"no upper bound on REV is established by this probe. The chain that would have given "
        f"O(n^(3/4)) required L2, refuted in R3. The surviving bound R4 (R <= C*r) is a "
        f"consequence of L1 alone and is far too loose to couple to the energy: on the hook-shape "
        f"counterexample it gives {mp.nstr(hook_bound, 6)} where the truth is "
        f"{mp.nstr(hook_R, 6)} ({mp.nstr(hook_bound/hook_R, 5)}x). A repair needs a statistic that "
        f"both bounds sum_m eps_m N_m from above AND is forced up by H - H_min; "
        f"r = min(ell, lambda_1) has the first property and demonstrably not the second. "
        f"Sub-linearity therefore remains MEASURED (n <= 44), not proved.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("PROVED:      identity (E), L1, and REV_n = Omega(sqrt n).")
    print("REFUTED:     my own lemma L2 (H >= 3r^2-3r+1) -- hook-shape counterexample.")
    print("WITHDRAWN:   the O(n^{3/4}) upper bound that rested on it.")
    print("STILL OPEN:  any upper bound. Sub-linearity remains MEASURED (n <= 44), not proved.")
    print(f"CONJECTURED: REV_n ~ A*sqrt(2n), A*sqrt2 = {mp.nstr(A*mp.sqrt(2), 8)} (lower bound tight).")
    print("=" * 78)

    payload = {
        "probe": "rev_sublinearity_proof_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "identity_E": "R_lambda = sum_{c in lambda} eps_{h(c)} - sum_{i<=n} eps_i, eps_m = -log(1-q0^{-2m})",
        "constants": {"C_sum_eps": mp.nstr(C, 20), "A_sum_eps_odd": mp.nstr(A, 20),
                      "A_sqrt2_predicted_REV_over_sqrt_n": mp.nstr(A * mp.sqrt(2), 20)},
        "proved": ["identity (E)", "L1 N_m <= min(ell,lambda_1)", "REV = Omega(sqrt n)"],
        "refuted": ("L2 'H >= 3r^2-3r+1 with r=min(ell,lambda_1)' is FALSE; counterexample the "
                    "hook shape (11,1^10) with H=131 vs claimed bound 331. The bad step was "
                    "h(1,j) >= 2r-j, which needs column j to have >= r cells for all j <= r."),
        "withdrawn": "REV = O(n^{3/4}) -- rested entirely on the refuted L2",
        "not_proved": ("ANY upper bound on REV. Sub-linearity remains MEASURED over n <= 44 "
                       "(hmin_closed_form_and_rev_sublinearity_probe.py), not proved. Also not "
                       "proved: tightness of the lower bound, REV ~ A sqrt(2n)."),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "lower_bound_table": lb,
        "upper_bound_table": ub,
    }
    out = os.path.join(_COMPUTATIONS, "rev-sublinearity-proof.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")

    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
