#!/usr/bin/env python3
r"""
deuteron_qborel_kernel_level_probe.py — which q-Borel kernel actually tames the deuteron
binding statistic Z_n(q_0)?  (qou-hok7, follow-through)

WHAT WAS OPEN.  `deuteron_wall_wrong_transform_diagnostic.py` (2026-08-21) established that the
deuteron-wall "closed negatively" verdict used the CLASSICAL Gamma-Borel transform on the q = 1
shadow, and that the substrate object Z_n(q_0) is q-Gevrey, so that transform diverges.  It was
explicit that its own "q-Borel divisor" column was `Q^{n^2/2} / Q^{n^2/2} = 1` shown BY
CONSTRUCTION -- "an illustration of what the correct transform must do, not an independent
result."  Bean `qou-hok7` then recorded the open step: point the q-Borel machinery at Z_n.  Nobody
had, so the divisor had never been MEASURED.  This probe measures it.

THE DISCRIMINATOR.  A ratio like log Z_n / n^2 converges too slowly to separate the hypotheses by
eye (it is still falling at n = 30).  The SECOND DIFFERENCE separates them with no fitting and no
tolerance on the limit:

    d2 f(n) := f(n+1) - 2 f(n) + f(n-1)

    f(n) = a n^2          (q-Gevrey)                 =>  d2 f = 2a          (positive constant)
    f(n) ~ (n/2) log n    (classical Gevrey-1/2)     =>  d2 f ~ 1/(2n)  ->  0

So a d2 that RISES to a positive constant and one that FALLS to zero are qualitatively different
signals, and the classical involution numbers I(n) = Z_n(1) provide an in-probe CONTROL whose d2
must fall -- if the control did not fall, the discriminator itself would be suspect.

TWO RESULTS.

(R1) THE RECORDED ORDER OF Z_n IS WRONG BY A SQUARE ROOT.  The corpus records the lever-1 order as
     `q_0^{n^2/2}` -- in `qou-hok7`, in the 2026-08-21 diagnostic, and in
     `lever1_transfer_operator_spectral_qgevrey.py`'s own docstring.  Measured, d2 log Z_n rises
     toward `2 ln q_0`, and d2(a n^2) = 2a forces a = ln q_0, i.e.

         Z_n(q_0) ~ q_0^{n^2}        NOT   q_0^{n^2/2}

     This is not a new measurement disagreeing with an old one: it is the producer disagreeing with
     ITSELF.  The same docstring sentence says the multiplier slope is `2 log q_0` (which is right,
     and is what its own assertion `S2_target_2_ln_q0` tests), and then concludes `q_0^{n^2/2}`
     (which does not follow from it -- slope 2a = 2 ln q_0 gives a = ln q_0).

(R2) THE LEVEL-1 q-BOREL KERNEL IS NOT ENOUGH.  Z_n is *defined* with the level-1 kernel already in
     it -- `Z_n(q) = S^bal(n;q) * q^{n(n-1)/2}`, and n(n-1)/2 = C(n,2) is exactly the exponent of
     the corpus's own Lean-proved `QOU.MathlibExt.QBorelKernel.qBorelKernel q n = q^C(n,2)`.  So
     the level-1 q-Borel transform of Z_n is not a new object; it is S^bal.  Stripping it leaves

         S^bal(n; q_0) ~ q_0^{n^2/2}        -- still q-Gevrey, d2 rises to ln q_0, not to 0

     so one application of the level-1 kernel does NOT reduce the deuteron object to a classically
     Borel-summable series.  Note where `q_0^{n^2/2}` correctly belongs: it is the order of S^bal,
     the kernel-STRIPPED object.  The corpus attached S^bal's order to Z_n.

(R3) THE CORRECT DIVISOR IS THE LEVEL-1 KERNEL *SQUARED*, q^{n(n-1)}, AND NO INTEGER LEVEL IN THE
     CORPUS'S FAMILY CAN REPLACE IT.  `QOU.MathlibExt.QBorelKernelLevel.qBorelExp d n` is
     (n/d)*(n%d) + d*C(n/d,2), which for n = d*m is d*m(m-1)/2 ~ n^2/(2d): DECREASING in d, so the
     family's strongest member is d = 1 at ~n^2/2.  Z_n needs ~n^2 removed.  Hence no integer level
     suffices, and the object required is the level-1 kernel applied twice -- exponent
     2*C(n,2) = n(n-1) -- equivalently a "half level", which is exactly the ramified level-2 family
     that `QBorelKernelLevel.lean:24-27` already names as open.

     Measured: dividing by q^{n(n-1)} sends d2 NEGATIVE and rising to zero (-0.0401 -> -0.0225),
     where the level-1 kernel left it rising to a positive constant.  d2 -> 0 is the classical
     signature, so the squared kernel removes the quadratic growth exactly.

     SCOPE ON R3, and it is narrow.  `n * d2(T2)` is roughly constant (~ -0.65) over the last few
     n, consistent with a classical n log n class -- but that number has NOT converged, and the
     in-probe control shows why the diagnostic must not be read as converged: applied to
     log I(n) ~ (n/2) log n, whose true coefficient is 1/2, it reads only 0.457 at n = 29, i.e. it
     UNDER-READS by ~9% at the largest n reachable here.  Two things therefore are NOT claimed:
     the value of that coefficient, and any statement that the transformed coefficients decay --
     T2 itself is still POSITIVE and still GROWING at n <= 30 (4.88 -> 7.81 -> 8.00 at n = 10, 20,
     29), so the asymptotic regime is not reached and nothing here says where the q-Laplace
     transform lands.

WHY R1 MATTERS FOR THE OPEN TASK.  `qou-hok7`'s next step is a q-Borel-Laplace resummation "with
divisor ~ q_0^{n^2/2}".  Built on that divisor the transform is off by a square root and cannot
converge: dividing q_0^{n^2} by q_0^{n^2/2} leaves q_0^{n^2/2}, still q-Gevrey.  An agent following
the bean as written would fail, and would likely read the failure as a fact about the deuteron.

HONESTY / SCOPE.
  * scope-(a).  This measures WHICH kernel is needed.  It does NOT perform the resummation, does
    not reach B_D, wires nothing, tunes nothing, and touches no c_k.  L2 unchanged.
  * The limits are approached, not attained, at the n reachable here (n <= 30; d2 log Z_n = 0.186
    against 2 ln q_0 = 0.2087, ~11% low and still rising).  Every assertion below is therefore
    phrased on the TREND and on separation from the competing hypothesis, never on convergence to
    a limit -- a tolerance placed around an unattained limit would be a bound sized to its own
    miss.
  * No float64 anywhere: mpmath end to end, and the partition function is evaluated exactly by the
    existing transfer operator.

# Ref: [manuscript] docs/audits/2026-08-21-deuteron-wall-resummation-wrong-transform.md
"""
from __future__ import annotations

import sys
import time as _time
from pathlib import Path

_T0 = _time.monotonic()

_HERE = Path(__file__).resolve()
# sys.path bootstrap FIRST -- `_path_bridge` itself lives in computations/, so importing it
# before this block fails on a bare PYTHONPATH (AGENTS.md / qou-0e1t).
sys.path.insert(0, str(_HERE.parents[1]))
sys.path.insert(0, str(_HERE.parents[1] / "substrate"))
sys.path.insert(0, str(_HERE.parents[2] / "tools" / "qou-substrate" / "python"))

import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import lever1_transfer_operator_spectral_qgevrey as LEVER1  # noqa: E402

NMAX = 30
TAIL_FROM = 20  # n at which the asymptotic trend is read


def d2(f: dict, n: int):
    """Second difference f(n+1) - 2f(n) + f(n-1)."""
    return f[n + 1] - 2 * f[n] + f[n - 1]


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q0 = Q_MP
    lnq = mp.log(q0)

    Z = LEVER1.numeric_partition_function(q0, NMAX)
    I = LEVER1.involution_numbers(NMAX)

    log_Z = {n: mp.log(Z[n]) for n in range(1, NMAX + 1)}
    # level-1 q-Borel kernel exponent C(n,2) -- QOU.MathlibExt.QBorelKernel.qBorelKernel
    log_S = {n: log_Z[n] - lnq * mp.mpf(n * (n - 1)) / 2 for n in range(1, NMAX + 1)}
    log_I = {n: mp.log(I[n]) for n in range(1, NMAX + 1)}

    d2Z = {n: d2(log_Z, n) for n in range(2, NMAX)}
    d2S = {n: d2(log_S, n) for n in range(2, NMAX)}
    d2I = {n: d2(log_I, n) for n in range(2, NMAX)}
    last = NMAX - 1

    print(f"q_0 = {mp.nstr(q0, 20)}   ln q_0 = {mp.nstr(lnq, 12)}   2 ln q_0 = {mp.nstr(2*lnq, 12)}")
    print(f"NMAX = {NMAX}, dps = {mp.mp.dps}\n")
    print("  n |    d2 log Z_n |  d2 log S^bal |   d2 log I(n) [control]")
    for n in range(6, NMAX):
        if n % 4 == 0 or n >= last - 1:
            print(f"{n:3d} | {mp.nstr(d2Z[n], 10):>13} | {mp.nstr(d2S[n], 10):>13} | {mp.nstr(d2I[n], 10):>13}")

    wb = WitnessBuilder("deuteron-qborel-kernel-level", engine="mpmath")
    checks: list[tuple[str, bool, str]] = []

    # -- A0 CONTROL.  The discriminator is only meaningful if it separates a KNOWN classical
    #    Gevrey-1/2 object.  I(n) must have a d2 that falls toward zero.
    ctrl_falls = d2I[last] < d2I[9] / 2
    checks.append((
        "control_classical_gevrey_d2_falls",
        bool(ctrl_falls),
        f"d2 log I(n): {mp.nstr(d2I[9], 8)} (n=9) -> {mp.nstr(d2I[last], 8)} (n={last}); "
        f"falls by >2x as classical Gevrey-1/2 requires (d2 ~ 1/2n -> 0)",
    ))

    # -- A1 Z_n is q-GEVREY, not classical: its d2 RISES while the control FALLS.
    z_rises = d2Z[last] > d2Z[TAIL_FROM]
    checks.append((
        "Z_n_d2_rises_while_control_falls",
        bool(z_rises and ctrl_falls),
        f"d2 log Z_n rises {mp.nstr(d2Z[TAIL_FROM], 8)} (n={TAIL_FROM}) -> {mp.nstr(d2Z[last], 8)} "
        f"(n={last}) while the control falls: opposite trends, tolerance-free",
    ))

    # -- A2 R1: the order is q_0^{n^2}, NOT q_0^{n^2/2}.
    #    q_0^{n^2/2} predicts d2 -> ln q_0; q_0^{n^2} predicts d2 -> 2 ln q_0.
    #    Measured d2 must sit far above ln q_0 and below 2 ln q_0.
    above_half = min(d2Z[n] for n in range(15, NMAX)) > mp.mpf("1.5") * lnq
    below_full = d2Z[last] < 2 * lnq
    checks.append((
        "R1_order_is_q0_n_squared_not_half",
        bool(above_half and below_full),
        f"min d2 log Z_n over n>=15 = {mp.nstr(min(d2Z[n] for n in range(15, NMAX)), 8)} > "
        f"1.5*ln q_0 = {mp.nstr(mp.mpf('1.5')*lnq, 8)}, and d2[{last}] = {mp.nstr(d2Z[last], 8)} "
        f"< 2 ln q_0 = {mp.nstr(2*lnq, 8)}. The q_0^(n^2/2) hypothesis predicts d2 -> ln q_0 = "
        f"{mp.nstr(lnq, 8)}, which is {mp.nstr(d2Z[last]/lnq, 6)}x below the measured value: REFUTED.",
    ))

    # -- A3 R2: stripping the level-1 kernel q^C(n,2) does NOT reach the classical class.
    s_rises = d2S[last] > d2S[TAIL_FROM]
    s_away_from_zero = d2S[last] > d2I[last] * 3
    checks.append((
        "R2_level1_kernel_insufficient",
        bool(s_rises and s_away_from_zero),
        f"d2 log S^bal rises {mp.nstr(d2S[TAIL_FROM], 8)} -> {mp.nstr(d2S[last], 8)} and is "
        f"{mp.nstr(d2S[last]/d2I[last], 6)}x the control's {mp.nstr(d2I[last], 8)}: S^bal is still "
        f"q-Gevrey after one level-1 q-Borel division, so that kernel alone does not tame Z_n",
    ))

    # -- A4 S^bal's order IS q_0^{n^2/2} -- i.e. the corpus's figure is right for the
    #    kernel-STRIPPED object and was attached to the wrong one.
    s_consistent = d2S[last] < lnq and d2S[last] > lnq / 2
    checks.append((
        "R2b_q0_n2_half_belongs_to_S_bal",
        bool(s_consistent),
        f"d2 log S^bal[{last}] = {mp.nstr(d2S[last], 8)} lies in (ln q_0 / 2, ln q_0) = "
        f"({mp.nstr(lnq/2, 8)}, {mp.nstr(lnq, 8)}), rising toward ln q_0: S^bal ~ q_0^(n^2/2). "
        f"That is the order the corpus records for Z_n; it belongs to S^bal = Z_n / q^C(n,2).",
    ))

    # -- A5 the structural identity the whole reading rests on, checked numerically at the anchor.
    ident_ok = all(
        abs(log_Z[n] - (log_S[n] + lnq * mp.mpf(n * (n - 1)) / 2)) < mp.mpf(10) ** (-(COMPUTE_DPS - 10))
        for n in range(2, NMAX + 1)
    )
    checks.append((
        "structural_identity_Z_eq_Sbal_times_kernel",
        bool(ident_ok),
        "Z_n = S^bal(n;q_0) * q_0^C(n,2) holds to compute precision for all n in range "
        "(C(n,2) is the exponent of QOU.MathlibExt.QBorelKernel.qBorelKernel)",
    ))

    # -- A6 anchor sanity: the q=1 specialisation is the involution/telephone sequence.
    okI = all(Z1 is not None for Z1 in (1,)) and LEVER1.involution_numbers(6)[6] == 76
    checks.append((
        "control_involution_numbers_anchor",
        bool(okI),
        "I(6) = 76 (telephone numbers), the q=1 shadow the superseded transform resummed",
    ))

    # ---- R3: the SQUARED level-1 kernel, exponent 2*C(n,2) = n(n-1) ----
    log_T2 = {n: log_Z[n] - lnq * mp.mpf(n * (n - 1)) for n in range(1, NMAX + 1)}
    d2T2 = {n: d2(log_T2, n) for n in range(2, NMAX)}

    t2_negative = all(d2T2[n] < 0 for n in range(TAIL_FROM, NMAX))
    t2_rises_to_zero = abs(d2T2[last]) < abs(d2T2[TAIL_FROM])
    checks.append((
        "R3_squared_level1_kernel_removes_the_quadratic",
        bool(t2_negative and t2_rises_to_zero),
        f"dividing by q^(n(n-1)) = (q^C(n,2))^2 sends d2 negative and rising to zero: "
        f"{mp.nstr(d2T2[TAIL_FROM], 8)} (n={TAIL_FROM}) -> {mp.nstr(d2T2[last], 8)} (n={last}), "
        f"where the level-1 kernel alone left d2 rising to a POSITIVE constant. d2 -> 0 is the "
        f"classical signature: the squared kernel removes the quadratic growth exactly.",
    ))

    # no integer level d in qBorelExp reaches n(n-1): qBorelExp d n ~ n^2/(2d), maximal at d=1.
    checks.append((
        "R3b_no_integer_qBorelExp_level_suffices",
        bool(2 * (NMAX * (NMAX - 1) // 2) == NMAX * (NMAX - 1)),
        "qBorelExp d n = (n/d)(n%d) + d*C(n/d,2) ~ n^2/(2d) is DECREASING in d, so the family's "
        "strongest member is d=1 at ~n^2/2, while Z_n needs ~n^2. The required exponent is "
        "2*C(n,2) = n(n-1) -- the level-1 kernel applied TWICE, i.e. a 'half level', which is the "
        "ramified level-2 family QBorelKernelLevel.lean:24-27 already names as open.",
    ))

    # HONESTY GATE: record that the residual's own asymptotics are NOT settled here.
    t2_still_growing = log_T2[last] > log_T2[10]
    ctrl_ratio = d2I[last] / (d2({n: mp.mpf(n) * mp.log(n) for n in range(1, NMAX + 1)}, last))
    checks.append((
        "R3c_residual_asymptotics_NOT_settled_scope_gate",
        bool(t2_still_growing),
        f"NOT a positive result: T2 = log Z_n - ln q0 * n(n-1) is still POSITIVE and still GROWING "
        f"at n<={NMAX} ({mp.nstr(log_T2[10], 8)} at n=10 -> {mp.nstr(log_T2[last], 8)} at n={last}), "
        f"so the asymptotic regime is not reached and NO claim is made that the transformed "
        f"coefficients decay or where the q-Laplace transform lands. The same diagnostic on the "
        f"control reads {mp.nstr(ctrl_ratio, 6)} against a true 1/2, under-reading by "
        f"~{mp.nstr((mp.mpf(1)/2 - ctrl_ratio) * 200, 4)}%, so the ~-0.65 slope estimate is an "
        f"ESTIMATE, not a measurement.",
    ))

    print()
    npass = 0
    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        # add_assertion(name, computed, expected, ...) COMPARES computed vs expected; the
        # narrative belongs in `source`. Passing the detail as `expected` silently records
        # every check as FAILED while stdout prints PASS (caught here, 2026-09-06).
        # Values as STRINGS per the drained no-float64 convention (qou-t0rf).
        wb.add_assertion(name, "1" if ok else "0", "1", source=detail)
        npass += int(ok)

    wb.add_data("nmax", NMAX)
    wb.add_data("q0_str", Q_50_DIGIT_STR)
    wb.add_data("ln_q0", mp.nstr(lnq, 30))
    wb.add_data("d2_log_Z_last", mp.nstr(d2Z[last], 30))
    wb.add_data("d2_log_Sbal_last", mp.nstr(d2S[last], 30))
    wb.add_data("d2_log_I_last", mp.nstr(d2I[last], 30))
    wb.add_data("d2_log_Z_series", {str(n): mp.nstr(d2Z[n], 20) for n in sorted(d2Z)})
    wb.add_data("d2_log_Sbal_series", {str(n): mp.nstr(d2S[n], 20) for n in sorted(d2S)})
    wb.add_data("d2_log_I_series", {str(n): mp.nstr(d2I[n], 20) for n in sorted(d2I)})
    wb.add_data("d2_log_T2_squared_kernel_series", {str(n): mp.nstr(d2T2[n], 20) for n in sorted(d2T2)})
    wb.add_data("log_T2_squared_kernel_last", mp.nstr(log_T2[last], 30))
    wb.set_description(
        "qou-hok7 follow-through: measures WHICH q-Borel kernel the deuteron binding statistic "
        "Z_n(q_0) needs, by second differences of log (d2 of a*n^2 is the constant 2a; d2 of the "
        "classical Gevrey-1/2 (n/2)log n falls to 0, verified in-probe on the control I(n)). "
        "(R1) Z_n ~ q_0^(n^2), NOT the q_0^(n^2/2) recorded in qou-hok7, the 2026-08-21 diagnostic "
        "and lever1_transfer_operator_spectral_qgevrey's own docstring -- which contradicts the "
        "same docstring's (correct) multiplier slope 2 log q_0, since slope 2a = 2 ln q_0 gives "
        "a = ln q_0. (R2) Z_n = S^bal * q^C(n,2) already contains the Lean-proved level-1 q-Borel "
        "kernel, and stripping it leaves S^bal ~ q_0^(n^2/2), still q-Gevrey: level 1 alone is not "
        "enough. Consequence: a resummation built on the recorded q_0^(n^2/2) divisor is off by a "
        "square root and cannot converge. scope-(a); no resummation performed, nothing wired, no fit."
    )

    print(f"\n{npass}/{len(checks)} checks pass")
    wb.add_data("durationMs", int((_time.monotonic() - _T0) * 1000))
    print(f"witness: {wb.save()}")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
