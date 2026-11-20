#!/usr/bin/env python3
"""threerow_qcross_trend_probe.py — the q_cross trend question is CONVENTION-C.

RETIRED AS A LIVE PROBE, 2026-08-25 (bean `qou-qdtk`).  It no longer asks whether
`q_cross(n)` is a structured sequence; it records why that question cannot be asked
under convention D, and asserts what is measurably true instead.  The convention-C
findings are preserved below, not deleted.

WHAT IT USED TO ASK (convention C, coherent THERE)
--------------------------------------------------
With `F_K(q) = Sum_{lam|-3A, l(lam)>=3} y_lam * chi^lam(beta_K) * Delta_lam` and its
character-free companion `G_n(q) = Sum_{lam|-n, l(lam)>=3} y_lam * Delta_lam`: is the
crossing sequence `q_cross(n)` structured, and is `q0`'s position in it derived or
coincidental?  Its three background facts:

  BG-1  dual-Cauchy normaliser `Z(q) = ((1-Q^r)/(1-Q))^n`, so `sgn G_n = sgn S_n`.
  BG-2  `Q^r = u^3/D(u)` with `D(u) = -u^6-u^4+u^3+u^2+1` has a real root
        `u* = 1.13068544546...`, i.e. `q* = 1.27844957658...`.  Below `q*` the level
        `r = log(Q^r)/log(Q)` is real, above it complex -- the "real-level branch".
  BG-3  the level-integer ladder `q_k` solving `r(q_k) = k`, root of
        `Sum_{j<k} u^{4j+3} = u^{4k} + u^{4k+2}`, accumulating at `q*`.

THE DEFECT THAT RETIRES IT -- A CONVENTION STRADDLE INSIDE ONE COMPUTATION
--------------------------------------------------------------------------
`_D_wenzl`, `U_STAR`, `Q_STAR`, the sweep bound `Q_HI` and the ladder `q_level(k)`
were **convention C, hardcoded in this file**.  `level_r()` called the corpus's
`_wenzl_constants`, which is **convention D**.  One computation, two conventions.
Measured side by side at `q0`:

    Q^r from the corpus (LIVE, D)          1.517953249818345896  = Q^2  => r = 2.0
    Q^r = u^3/D(u)  (this file's own text) 1.720251751213844854        => r = 2.5995

What that made it print as *results*:

  * `level r(1.45) = 2.0  <- COMPLEX => OFF-BRANCH` -- prints `2.0` and calls it
    complex.  Under D, `Q^r = Q^2` is entire: no pole, no `q*`, and the real-level
    branch is all of `q > 0`.
  * the ladder printed `r = 2.0` at **every** rung `q_2 ... q_10`, though each rung is
    *defined* by `r(q_k) = k`: the rungs are C, the `r` beside them is D.
  * `=> q0 in (q_2, q_3);  r(q0) = 2.0 not in Z` -- **false as printed**.  Under C the
    real claim was `r = 2.5995 not in Z`; under D it inverts.
  * the `vanishing law at r=3` line reported `|s_lam| = 0` for `(3,2,1)` and `(4,1,1)`,
    which have `l = 3`, not `> 3` -- under D the whole `l >= 3` stratum is zero, so the
    test could no longer distinguish its own claim.
  * section 1 printed an **identical** crossing list for `n = 3 .. 23`, except
    single-`n` anomalies (`n=11` gained `1.096597`, `n=18` gained `1.114696` --
    different values).  An `n`-dependent object does not give an `n`-independent
    answer; a bisect-on-sign-change over round-off does, and two different spurious
    crossings at two different `n` is what round-off looks like.
  * section 2 printed `F(q0) = +0.00000e+00` for D, T and 3He.

Under D the headline object is a **structural zero**: `y_lam = 0` for every
`l(lam) >= 3` (`schurPrincipal_eq_zero_iff`, with `wenzlLevel_conventionD` pinning
`r = 2`), so `G_n = 0` and `F_K = 0` on that stratum.  All three questions --
monotone? derivable? is `q0` special? -- are questions about the crossings of the
zero function.

WHAT SURVIVES
-------------
BG-1 does.  The dual-Cauchy normaliser identity is convention-independent, and under
D it reads `Z = ((1-Q^2)/(1-Q))^n = (1+Q)^n`.  It is re-verified here.

BG-2 and BG-3 do not: with `Q^r = Q^2` there is no pole to bound a branch and no
ladder to climb, `r` being the constant 2.  `r(q) = k` is unsatisfiable for `k != 2`
and vacuous for `k = 2`.

SCOPE.  Scope-(a), and about THIS PROBE.  The `Q^r = u^3/D(u)` family is a legitimate
object and is not refuted here -- the finding is that this file is not computing it.
Convention C was excised by owner ruling (2026-08-15), so re-pinning the arithmetic to
C and registering an off-canon comparison -- the alternative disposition -- is not
taken: the question it would ask concerns a stratum that carries no weight in the
canonical convention.

WHAT THIS PROBE NOW ASSERTS (all measured under D, at the proton anchor)
------------------------------------------------------------------------
  * `wenzl_level_is_constant_two`          -- `Q^r = Q^2` exactly, so `r` is 2
  * `no_pole_on_positive_reals`            -- including AT C's pole `q*`, where the
                                              live level function is regular
  * `three_row_stratum_is_structural_zero` -- against an explicit noise floor, never
                                              an equality test
  * `reported_crossings_are_n_independent` -- the positive discriminator: an
                                              n-dependent object cannot do this
  * `dual_cauchy_identity_holds`           -- BG-1, the background fact that survives

Measurement only.  Nothing is fitted and nothing is wired.
"""
from __future__ import annotations

import math
import os
import sys
import warnings
from pathlib import Path

for _extra in ("/home/user/qou/computations", "/home/user/qou/computations/substrate",
               "/home/user/qou/computations/hecke", "/home/user/qou/computations/deltalambda"):
    if _extra not in sys.path:
        sys.path.append(_extra)
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    partitions_of, _f_lambda, schur_principal_mpmath, _wenzl_constants,
)
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

Q0 = Q_MP          # EXPERIMENTAL PROTON ANCHOR
N_MIN, N_MAX = 3, 12
OUTDIR = Path(os.environ.get("QOU_OUTDIR", str(Path(__file__).resolve().parent)))


def _D_wenzl_conventionC(u):
    """C's D(u) = -u^6-u^4+u^3+u^2+1; C had Q^r = u^3/D(u), with a pole at D(u) = 0.

    Kept ONLY to demonstrate that the live level function is regular where C had its
    pole.  It bounds no sweep and enters no result.
    """
    return -u ** 6 - u ** 4 + u ** 3 + u ** 2 + 1


U_STAR_C = mp.findroot(_D_wenzl_conventionC, mp.mpf("1.13"))
Q_STAR_C = U_STAR_C ** 2

C_FRAME_RECORD = {
    "convention": "C",
    "computed_at": "2026-08-09T18:11:26Z",
    "level_at_q0": "2.5995",
    "q_star_real_level_branch_end": "1.27844957657969...",
    "assertions_as_committed": {
        "q_cross_sequence_monotone": False,
        "crossings_exist_for_all_n": False,
        "q0_position_informative": False,
        "dual_cauchy_identity_holds": True,
        "q0_on_real_level_branch": True,
    },
    "note": "Correct for convention C. Under D `q0_on_real_level_branch` asserts a "
            "structure that does not exist -- there is no pole, so no branch to be on "
            "or off. The three False results remain False under D but for an entirely "
            "different reason: the object is identically zero, so there are no "
            "crossings at all. Green, but vacuous. Do not read these as live.",
}


def delta_lambda(lam) -> int:
    """Delta_lam = (-1)^{n(lam)} * dim V_lam (PROVED value-only)."""
    conj = tuple(sum(1 for p in lam if p > i) for i in range(lam[0])) if lam else ()
    sgn = math.prod((-1) ** (p * (p - 1) // 2) for p in conj)
    return sgn * _f_lambda(lam)


def y_lambda_all(n, q):
    """y_lam = s_lam / Z with the live (convention-D) Wenzl constants."""
    Q, QR = _wenzl_constants(q)
    Z = ((1 - QR) / (1 - Q)) ** n
    return {lam: schur_principal_mpmath(lam, q) / Z for lam in partitions_of(n)}


def main() -> int:
    Q, QR = _wenzl_constants(Q0)
    print("=" * 90)
    print(" the q_cross(n) trend question is CONVENTION-C -- retirement record")
    print("=" * 90)
    print(f" q0 (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")
    print(f" Q = q0^2 = {mp.nstr(Q, 20)}    Q^r (LIVE) = {mp.nstr(QR, 20)}")

    qs = [mp.mpf("1.000001"), mp.mpf("1.05"), Q0, mp.mpf("1.2"),
          Q_STAR_C, mp.mpf("1.45"), mp.mpf("2.0"), mp.mpf("5.0")]
    print(f"\n {'q':>20} {'Q^r':>22} {'Q^2':>22} {'r = logQ^r/logQ':>18}")
    print(" " + "-" * 86)
    level_const, entire = True, True
    for q in qs:
        Qq, QRq = _wenzl_constants(q)
        r = mp.log(QRq) / mp.log(Qq)
        if abs(QRq - Qq ** 2) > mp.mpf("1e-45"):
            entire = False
        if abs(r - 2) > mp.mpf("1e-40"):
            level_const = False
        tag = "  <- C's pole q*" if q == Q_STAR_C else ""
        print(f" {mp.nstr(q, 14):>20} {mp.nstr(QRq, 16):>22} {mp.nstr(Qq ** 2, 16):>22}"
              f" {mp.nstr(r, 12):>18}{tag}")
    print(f"\n Q^r == Q^2 at every sample (entire, no pole): {entire}")
    print(f" r is the constant 2 at every sample (no ladder): {level_const}")
    print(f" C's pole sat at q* = {mp.nstr(Q_STAR_C, 18)}; the live level function is"
          " regular there.")

    print(f"\n {'n':>3} {'parts':>6} {'l>=3':>5} {'max|G contrib|':>18}"
          f" {'noise floor':>14}  {'structural zero':>15}")
    print(" " + "-" * 72)
    all_zero, rows = True, []
    for n in range(N_MIN, N_MAX + 1):
        Y = y_lambda_all(n, Q0)
        ge3 = [l for l in Y if len(l) >= 3]
        # Same floor as computations/audits/ylambda_threerow_frame_audit.py: the
        # vanishing is a polynomial identity REACHED BY CANCELLATION, so an equality
        # test answers a question about the arithmetic, not the mathematics.
        floor = max((abs(v) for v in Y.values()), default=mp.mpf(0)) \
            * mp.mpf(10) ** (-(mp.mp.dps - 8))
        mx = max((abs(Y[l] * delta_lambda(l)) for l in ge3), default=mp.mpf(0))
        zero = mx < floor
        all_zero = all_zero and zero
        print(f" {n:>3} {len(Y):>6} {len(ge3):>5} {mp.nstr(mx, 6):>18}"
              f" {mp.nstr(floor, 6):>14}  {str(zero):>15}")
        rows.append({"n": n, "partitions": len(Y), "ell_ge_3": len(ge3),
                     "max_abs_G_contribution": mp.nstr(mx, 12),
                     "noise_floor": mp.nstr(floor, 6),
                     "is_structural_zero": bool(zero)})

    print("\n scanning the old sweep's grid for sign changes of G_n ...")
    grid = [mp.mpf("1") + (Q_STAR_C - 1) * mp.mpf(i) / 220 for i in range(1, 221)]
    cross_sets = {}
    for n in range(N_MIN, min(N_MAX, 10) + 1):
        prev_sign, crossings = None, []
        for q in grid:
            Y = y_lambda_all(n, q)
            G = sum((Y[l] * delta_lambda(l) for l in Y if len(l) >= 3), mp.mpf(0))
            s = 1 if G > 0 else (-1 if G < 0 else 0)
            if prev_sign is not None and s != 0 and prev_sign != 0 and s != prev_sign:
                crossings.append(mp.nstr(q, 8))
            if s != 0:
                prev_sign = s
        cross_sets[n] = tuple(crossings)
        print(f"  n={n:>3}  {len(crossings):>3} sign changes")
    distinct = set(cross_sets.values())
    n_independent = len(distinct) == 1
    print(f"\n distinct crossing sets across n = {N_MIN}..{min(N_MAX, 10)}: "
          f"{len(distinct)}  => n-independent: {n_independent}")
    print(" (an n-dependent object cannot give an n-independent crossing set;"
          " these are round-off sign flips)")

    cauchy_err = mp.mpf(0)
    for n in range(N_MIN, N_MAX + 1):
        Z_closed = ((1 - QR) / (1 - Q)) ** n
        Z_sum = sum((_f_lambda(l) * schur_principal_mpmath(l, Q0)
                     for l in partitions_of(n)), mp.mpf(0))
        cauchy_err = max(cauchy_err, abs(Z_sum - Z_closed) / abs(Z_closed))
    cauchy_ok = cauchy_err < mp.mpf("1e-35")
    print(f"\n BG-1 dual-Cauchy  Sum_mu f^mu s_mu = ((1-Q^r)/(1-Q))^n :"
          f" max rel err {mp.nstr(cauchy_err, 6)}  => holds: {cauchy_ok}")
    print(" under D this reads Z = (1+Q)^n, since Q^r = Q^2.")

    print("\n" + "=" * 90)
    print(" The three questions this probe asked -- is q_cross(n) monotone, is it")
    print(" derivable, is q0's position special -- are questions about the crossings")
    print(" of the zero function. They do not have convention-D answers; they")
    print(" dissolve. BG-1 survives; BG-2 and BG-3 do not exist under D.")
    print("=" * 90)

    w = WitnessBuilder("threerow-qcross-trend", engine="mpmath50", output_dir=OUTDIR)
    w.add_assertion("wenzl_level_is_constant_two", 1 if level_const else 0, 1)
    w.add_assertion("no_pole_on_positive_reals", 1 if entire else 0, 1)
    w.add_assertion("three_row_stratum_is_structural_zero", 1 if all_zero else 0, 1)
    w.add_assertion("reported_crossings_are_n_independent", 1 if n_independent else 0, 1)
    w.add_assertion("dual_cauchy_identity_holds", 1 if cauchy_ok else 0, 1)
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("Q", mp.nstr(Q, 30))
    w.add_parameter("QR_live", mp.nstr(QR, 30))
    w.add_parameter("wenzl_level_r", "2 (convention D)")
    w.add_parameter("q_star_conventionC_pole", mp.nstr(Q_STAR_C, 30))
    w.add_data("by_n", rows)
    w.add_data("convention_c_record", C_FRAME_RECORD)
    w.add_caveat(
        "RETIRED AS A LIVE PROBE. This witness no longer reports a q_cross trend. Under "
        "convention D the l(lam) >= 3 stratum is a structural zero, so G_n and F_K "
        "vanish identically there and the crossings the previous sweep reported were "
        "round-off sign flips -- demonstrated by their being IDENTICAL across n, which "
        "an n-dependent object cannot be."
    )
    w.add_caveat(
        "The superseded witness asserted `q0_on_real_level_branch: True`. Under D there "
        "is no pole, hence no branch to be on or off, so that assertion named a "
        "structure that does not exist. Its three False results stay False under D but "
        "for a different reason -- no crossings at all, rather than an unstructured "
        "sequence of them. Green, but vacuous."
    )
    w.add_caveat(
        "Scope-(a), about this probe. The Q^r = u^3/D(u) family is a legitimate object "
        "and is NOT refuted; the finding is that this file was not computing it -- its "
        "branch geometry was convention C hardcoded while its level function read "
        "convention D from the corpus. Re-pinning to C and registering an off-canon "
        "comparison was the alternative disposition, not taken: C is excised by owner "
        "ruling (2026-08-15) and the question concerns a stratum carrying no weight in "
        "the canonical convention."
    )
    w.set_description(
        "Records why the q_cross(n) trend question is convention-C-only. The probe "
        "straddled two conventions inside one computation: _D_wenzl / U_STAR / Q_STAR "
        "and the level-integer ladder were convention C hardcoded in the file, while "
        "level_r() read the corpus's convention-D _wenzl_constants. Under D, Q^r = Q^2 "
        "exactly, so the level is the constant 2, there is no pole (the live function "
        "is regular at C's q*), no real-level branch and no ladder; and the l(lam) >= 3 "
        "stratum is a structural zero, so the crossings previously reported were "
        "round-off, shown by their n-independence. BG-1, the dual-Cauchy normaliser "
        "identity, is convention-independent and is re-verified. Supersedes the "
        "2026-08-09 C-frame witness."
    )
    w.save()

    ok = level_const and entire and all_zero and n_independent and cauchy_ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
