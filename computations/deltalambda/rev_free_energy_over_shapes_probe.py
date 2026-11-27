#!/usr/bin/env python3
r"""
rev_free_energy_over_shapes_probe.py — REV as an EXACT free energy over Young shapes (qou-hok7)

`qou-hok7` leaves exactly one thing open: the asymptotics of

    REV_n  :=  log Z_n(q_0)  -  (deg Z_n) * ln q_0 .

Four routes to it are closed in the bean, and all four went through MOMENTS of the path-weight
distribution (palindromicity, extensivity, a 2nd-order cumulant expansion, a closed form for
Var(w)).  The bean's own suggested next attack is to go at the deficit spectrum `N_n(E)` directly,
"since REV_n = log sum_E N_n(E) x^E is a free energy".

`zn_hook_length_closed_form_probe.py` supplies the missing handle: the closed form

    Z_n(q)  =  q^{-n}  sum_{lambda |- n}  q^{H(lambda)}  [n]_{q^2}! / prod_c [h(c)]_{q^2}      (C2)

with `H(lambda) = sum_c h(c)` the total hook length, and `deg Z_n = n^2 - H_min(n)`  (C3).

## The decomposition this probe establishes

Write `term_lambda(q)` for the `lambda`-summand of (C2).  Its degree is exactly `n^2 - H(lambda)`,
and its coefficients are non-negative with `term_lambda(1) = f^lambda`.  Dividing (C2) by
`q_0^{deg Z_n}` term by term gives, with NO approximation,

    REV_n  =  log  sum_{lambda |- n}  exp(  R_lambda  -  (H(lambda) - H_min) * ln q_0  )        (F)

    R_lambda  :=  log term_lambda(q_0)  -  (n^2 - H(lambda)) * ln q_0 ,      0 <= R_lambda <= log f^lambda

So REV is a free energy over PARTITIONS, not over paths:

  * ENERGY   `(H(lambda) - H_min) * ln q_0` -- an exact integer excess hook length, penalising
             shapes away from the staircase-like minimiser, at "inverse temperature" `ln q_0`;
  * ENTROPY  `R_lambda` -- the per-shape reversed polynomial, bounded by `log f^lambda`.

The deficit spectrum `N_n(E)` of the bean is thereby IDENTIFIED: at leading order `E` is the
excess total hook length `H(lambda) - H_min`, whose distribution over `lambda |- n` is a purely
combinatorial object independent of `q_0`.

## What this probe checks / measures

  R1  (F) is exact: recomputing REV from the shape sum reproduces REV from the transfer operator.
  R2  the bounds `0 <= R_lambda <= log f^lambda` hold for every shape (so (F) really is a free
      energy with a bounded entropy term).
  R3  which of the two terms carries REV's growth -- reported as a measured split, not a fit.
  R4  the ENERGY-only free energy (set R_lambda = 0) and the ENTROPY-only one (set the energy to 0)
      are each computed, to show neither alone reproduces REV.
  M1  REV_n itself, extended to larger n than the corpus has reached, via (C2).

Arithmetic: mpmath at 60 dps throughout; the energies `H(lambda) - H_min` are exact integers.
No float64 anywhere.  R1/R2 are exact-in-the-limit checks with an explicit dps-scaled tolerance,
stated per check.
"""

from __future__ import annotations

import json
import os
import sys
import time
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
    closed_form_Z,
    conjugate,
    hooks,
    min_total_hook,
    partitions,
    transfer_Z,
)


def log_qint(m: int, t) -> "mp.mpf":
    """log [m]_t = log((t^m - 1)/(t - 1)), t > 1."""
    return mp.log((t ** m - 1) / (t - 1))


def hook_counts(lam: tuple) -> dict:
    d: dict = {}
    for h in hooks(lam):
        d[h] = d.get(h, 0) + 1
    return d


def f_lambda(lam: tuple, n: int) -> int:
    """Number of SYT of shape lambda, by the hook length formula (exact integer)."""
    num = 1
    for i in range(1, n + 1):
        num *= i
    den = 1
    for h in hooks(lam):
        den *= h
    assert num % den == 0
    return num // den


def shape_terms(n: int):
    """Yield (lam, H, R_lambda, energy) for every lambda |- n.

    R_lambda = log term_lambda(q0) - (n^2 - H) ln q0, computed from the q-integer product
    (no polynomial expansion needed).
    """
    Hmin, _ = min_total_hook(n)
    # log [n]_{t}! = sum_{i=1}^n log [i]_t
    log_fact = mp.mpf(0)
    for i in range(1, n + 1):
        log_fact += log_qint(i, T)
    for lam in partitions(n):
        hs = hooks(lam)
        H = sum(hs)
        log_den = mp.mpf(0)
        for h in hs:
            log_den += log_qint(h, T)
        # log term_lambda(q0) = (H - n) ln q0 + log_fact - log_den
        log_term = (H - n) * LNQ + log_fact - log_den
        R = log_term - (n * n - H) * LNQ
        energy = (H - Hmin) * LNQ
        yield (lam, H, R, energy)


def rev_from_shapes(n: int, *, use_R=True, use_energy=True):
    """log sum_lambda exp(R - energy), by logsumexp.  Also returns the dominant shape."""
    best = None
    vals = []
    for (lam, H, R, energy) in shape_terms(n):
        L = (R if use_R else mp.mpf(0)) - (energy if use_energy else mp.mpf(0))
        vals.append((L, lam))
        if best is None or L > best[0]:
            best = (L, lam)
    m = best[0]
    s = mp.mpf(0)
    for (L, _lam) in vals:
        s += mp.e ** (L - m)
    return (m + mp.log(s), best[1], len(vals))


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)
        return bool(ok)

    print("=" * 78)
    print("REV as an exact free energy over Young shapes   (qou-hok7)")
    print(f"q_0 = {mp.nstr(Q0, 20)}   ln q_0 = {mp.nstr(LNQ, 12)}   dps = {mp.dps}")
    print("=" * 78)

    # ---------- R1: (F) reproduces REV computed from the transfer operator
    N_CHK = 11
    Ztr = transfer_Z(N_CHK)
    tol = mp.mpf(10) ** (-(mp.dps - 15))
    worst = mp.mpf(0)
    rows = []
    for n in range(1, N_CHK + 1):
        poly = Ztr[n]
        d = len(poly) - 1
        zval = mp.mpf(0)
        for j, c in enumerate(poly):
            if c:
                zval += mp.mpf(int(c)) * Q0 ** j
        rev_tr = mp.log(zval) - mp.mpf(d) * LNQ
        rev_sh, dom, npart = rev_from_shapes(n)
        err = abs(rev_tr - rev_sh)
        worst = max(worst, err)
        rows.append({"n": n, "REV": mp.nstr(rev_tr, 12), "err": mp.nstr(err, 4),
                     "dominant_shape": list(dom), "n_partitions": npart})
    check(
        "R1_free_energy_identity_reproduces_REV",
        worst < tol,
        f"(F) reproduces REV from the exact transfer-operator polynomial for every n=1..{N_CHK}; "
        f"worst |difference| = {mp.nstr(worst, 4)} against a {mp.dps}-dps tolerance "
        f"{mp.nstr(tol, 4)}. The shape sum has p(n) terms where the operator has ~I(n) paths.",
    )

    # ---------- R2: the entropy term is bounded by log f^lambda
    bad2 = []
    checked2 = 0
    for n in range(1, 15):
        for (lam, H, R, energy) in shape_terms(n):
            checked2 += 1
            lo = -tol
            hi = mp.log(mp.mpf(f_lambda(lam, n))) + tol
            if not (R >= lo and R <= hi):
                bad2.append((n, lam, mp.nstr(R, 8)))
    check(
        "R2_entropy_term_bounded_by_log_dim",
        not bad2,
        f"0 <= R_lambda <= log f^lambda verified for all {checked2} shapes with n <= 14 "
        f"({len(bad2)} violations). This is what makes (F) a free energy with a bounded entropy: "
        f"R_lambda is the log of a reversed polynomial with non-negative coefficients summing "
        f"to f^lambda.",
    )

    # ---------- M1 / R3 / R4: the split, measured
    print()
    print("-" * 78)
    print("REV and its two parts (all exact-arithmetic evaluations, no fitting):")
    print(f"  {'n':>3} {'REV_n':>12} {'energy-only':>12} {'entropy-only':>13} "
          f"{'H_min':>6} {'dominant shape':>22}")
    split = []
    NMAX = 34
    t0 = time.time()
    for n in list(range(2, 13)) + [15, 18, 21, 24, 27, 30, NMAX]:
        rev, dom, npart = rev_from_shapes(n)
        e_only, _, _ = rev_from_shapes(n, use_R=False, use_energy=True)
        s_only, _, _ = rev_from_shapes(n, use_R=True, use_energy=False)
        Hmin, _arg = min_total_hook(n)
        print(f"  {n:>3} {mp.nstr(rev, 8):>12} {mp.nstr(e_only, 8):>12} "
              f"{mp.nstr(s_only, 8):>13} {Hmin:>6} {str(dom):>22}")
        split.append({"n": n, "REV": mp.nstr(rev, 14), "energy_only": mp.nstr(e_only, 14),
                      "entropy_only": mp.nstr(s_only, 14), "H_min": Hmin,
                      "dominant_shape": list(dom), "n_partitions": npart})
    elapsed = time.time() - t0
    print(f"  ({mp.nstr(mp.mpf(elapsed), 4)} s for the table)")

    rev_max = mp.mpf(split[-1]["REV"])
    e_max = mp.mpf(split[-1]["energy_only"])
    s_max = mp.mpf(split[-1]["entropy_only"])
    check(
        "R3_neither_part_alone_reproduces_REV",
        (abs(rev_max - e_max) > mp.mpf("0.01")) and (abs(rev_max - s_max) > mp.mpf("0.01")),
        f"at n={NMAX}: REV = {mp.nstr(rev_max, 10)}, energy-only = {mp.nstr(e_max, 10)}, "
        f"entropy-only = {mp.nstr(s_max, 10)}. Both differ from REV, so REV is a genuine "
        f"competition between excess hook length and shape multiplicity -- not either alone.",
    )

    # growth diagnostics -- MEASURED, explicitly not a derivation
    print()
    print("-" * 78)
    print("growth diagnostics for REV (MEASURED -- these do not derive the asymptotics):")
    print(f"  {'n':>3} {'REV':>11} {'REV/n':>10} {'REV/sqrt(n)':>12} {'REV/log I(n)':>13}")
    I = [1, 1]
    for m in range(2, NMAX + 1):
        I.append(I[m - 1] + (m - 1) * I[m - 2])
    growth = []
    for row in split:
        n = row["n"]
        rev = mp.mpf(row["REV"])
        g = {"n": n,
             "REV_over_n": mp.nstr(rev / n, 8),
             "REV_over_sqrt_n": mp.nstr(rev / mp.sqrt(n), 8),
             "REV_over_log_I": mp.nstr(rev / mp.log(mp.mpf(I[n])), 8)}
        growth.append(g)
        print(f"  {n:>3} {mp.nstr(rev, 8):>11} {g['REV_over_n']:>10} "
              f"{g['REV_over_sqrt_n']:>12} {g['REV_over_log_I']:>13}")

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "rev_free_energy_over_shapes_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "identity": ("REV_n = log sum_{lambda|-n} exp(R_lambda - (H(lambda)-H_min) ln q0), "
                     "R_lambda = log term_lambda(q0) - (n^2-H(lambda)) ln q0, "
                     "0 <= R_lambda <= log f^lambda"),
        "deficit_spectrum_identified_as": "excess total hook length H(lambda) - H_min(n)",
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "rev_table": split,
        "growth_diagnostics_MEASURED_not_derived": growth,
        "verification_rows": rows,
    }
    out = os.path.join(_COMPUTATIONS, "rev-free-energy-over-shapes.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")

    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
