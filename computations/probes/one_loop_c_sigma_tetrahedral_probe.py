#!/usr/bin/env python3
"""c_sigma(4_1) = 3^{-1/4}, DERIVED — the knot side, by the same method.

Bean qou-vdvK.  `qou-vdvS` derived `c_sigma` for van der Veen's `b = 1`
Whitehead chains and left the knot side explicitly open: "a b=1 Whitehead chain
has c+d+1 >= 2 components, so nothing above derives c_sigma(4_1) = 3^{-1/4},
and the one-cusped leg still rests on Garoufalidis-Yoon together with the 4_1
calibration."

That leg is now closed, and it did not need van der Veen at all.  It needs the
observation of WHY his computation closed in the first place.

WHAT MADE THE LINK CASE WORK.  The recipe is: explicit state-sum -> Lobachevsky
potential -> critical point -> Hessian, with

    |Q_inf|^2  proportional to  1 / det(Hessian at the geometric saddle).

His potential `f(x,y) = -2 Lambda(x+y) + 2 Lambda(y) + Lambda(x)` has its
critical point at `(pi/2, pi/4)` — a RATIONAL point in units of pi — because
those complements are glued from REGULAR IDEAL OCTAHEDRA
(`Vol = 8(c+d) Lambda(pi/4)`).  Rationality of the saddle is the whole reason a
closed form exists; nothing else in the argument cares which link it is.

SO LOOK FOR THE OTHER REGULAR IDEAL POLYHEDRON.  `4_1` is two regular ideal
TETRAHEDRA, and Kashaev's invariant is a ONE-variable sum of exactly the same
shape,

    <4_1>_N  =  sum_k |(q;q)_k|^2  =  sum_k prod_{j<=k} 4 sin^2(j pi/N)
             =  sum_k exp(-2 s_k),      s_k := -sum_{j<=k} log|2 sin(j pi/N)|

the same `s_k` whose expansion was already verified for van der Veen's Lemma 3.
Feeding it through:

    s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) + O(1/N),  theta = k pi/N

    log g_k = -(2N/pi) Lambda(theta) + log(2 N sin theta) + O(1/N)

  * SADDLE.  d/d theta of the leading term vanishes when `Lambda'(theta) = 0`,
    i.e. `2 sin theta = 1`, i.e. `theta* = pi/6` or `5 pi/6`.  The maximum is at
    `5 pi/6` (the other is a minimum).
  * VOLUME.  Its value is `(2N/pi) Lambda(pi/6) = Vol * N / (2 pi)`, since
    `Vol(4_1) = 4 Lambda(pi/6)`.  The volume conjecture falls out.
  * STIRLING.  The subleading term contributes `2 N sin(5 pi/6) = N`.
  * HESSIAN.  `Lambda''(theta) = -cot(theta)`, so `|phi''(k)| = 2 pi sqrt3 / N`
    and Laplace gives `sqrt(2 pi/|phi''|) = sqrt(N / sqrt3)`.

    <4_1>_N ~ N * sqrt(N/sqrt3) * e^{Vol N/2pi} = 3^{-1/4} N^{3/2} e^{Vol N/2pi}

so BOTH `c_sigma(4_1) = 3^{-1/4}` and the power `N^{3/2}` are derived, and

    k := c_sigma |tau_DG|^{1/2} = 3^{-1/4} (sqrt3/2)^{1/2} = 2^{-1/2}

on the knot side, with no calibration anywhere.

A RIGIDITY WORTH NOTICING.  In the one-variable case the saddle condition IS
`2 sin theta* = 1`, so the Stirling factor `2 sin theta*` is forced to 1 and

    c_sigma = |cot theta*|^{-1/2} = 3^{-1/4}

with no freedom at all.  `3^{-1/4}` is not a property of `4_1` so much as of
"one summation variable".  Equivalently `|tau_DG|(4_1) = sqrt3/2` IS the
Hessian `|cot theta*| = sqrt3` divided by the Stirling `2`: the 1-loop
invariant is literally the Hessian determinant of the potential at the
geometric saddle, which is what Dimofte-Garoufalidis assert in general and what
this file exhibits in the smallest case.

WHERE THE CLOSED FORMS LIVE, AND WHY THERE ARE ONLY TWO.  The saddle sits at a
root-of-unity shape exactly for the regular ideal polyhedra: `z = exp(i pi/3)`
(tetrahedron, trace field `Q(zeta_3) = Q(sqrt-3)`) and `z = i` (octahedron,
trace field `Q(zeta_4) = Q(i)`).  Those are the two imaginary quadratic fields
with extra units — the two Bianchi cases — and they are precisely the two
families this corpus has closed forms for:

    4_1              Q(sqrt-3)   |tau| = sqrt3 / 2
    W_{a,1,c,d}      Q(i)        |tau| = 2^{2n-2} |A|,  A = n - m i in Z[i]

In the link case `A` is a GAUSSIAN INTEGER and `|A| = sqrt(n^2+m^2)` is the
square root of its norm.  That is the arithmetic content of the closed form,
and it is why the method does not extend by analytic means alone: for a general
knot the trace field is a general number field and `det(Hessian)` is an
algebraic number in it with no reason to have a radical expression.

Nothing is fitted.  The prediction `3^{-1/4}` is written above from the Laplace
argument; the numerics below only confirm it.
"""

from __future__ import annotations

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

import numpy as np  # noqa: E402
from mpmath import mp, mpf, sqrt, cot, sin, pi, fabs, clsin  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
DISSOLUTION = COMP / "one-loop-c-sigma-percusp-dissolution.witness.json"

# Raise precision BEFORE building the module-scope constant below.  Without
# this line `mpf("2.0298…")` is constructed at mpmath's default 15 dps and its
# 60 digits are truncated to 53 bits the moment it is built — the call in
# main() runs too late to recover them, and no later dps setting can.  Caught
# by computations/module_const_precision_audit.py; idempotent, so it composes
# with the call in main() rather than replacing it.
set_compute_dps()

# Vol(4_1) = 2*Cl_2(pi/3) = 6*Lambda(pi/3) = 4*Lambda(pi/6). All three forms
# agree (verified to 35 digits); the comment's identity was correct. What was
# wrong is the literal it labelled "the standard 60-digit value": it printed 60
# and was correct to 30 --
#   was    2.0298832128193072500424051085 48644088360398378694438195202545
#   exact  2.0298832128193072500424051085 4904057188337861506...
# Computed now, so there is nothing to transcribe (bean qou-ckbv).
VOL_41 = 2 * clsin(2, pi / 3)


def kashaev_log(N: int) -> float:
    """log <4_1>_N = log sum_k prod_{j<=k} 4 sin^2(j pi/N), in log space."""
    j = np.arange(1, N)
    s = np.concatenate([[0.0],
                        -np.cumsum(np.log(2 * np.sin(j * math.pi / N)))])
    lg = -2 * s                       # log |(q;q)_k|^2
    mx = lg.max()
    return mx + math.log(np.exp(lg - mx).sum())


def c_sigma_N(N: int) -> float:
    return math.exp(kashaev_log(N) - 1.5 * math.log(N)
                    - float(VOL_41) * N / (2 * math.pi))


def main() -> int:
    set_compute_dps()
    dis = record_upstream(DISSOLUTION, _UPSTREAM_RECORDS)
    cs41_corpus = mpf(dis["c_sigma_measured"]["4_1"])
    tau41_corpus = mpf(dis["tau_dg"]["4_1"])

    print("=" * 74)
    print(" c_sigma(4_1) = 3^{-1/4}, derived — the tetrahedral case")
    print("=" * 74)

    # -- the Laplace ingredients, symbolically ---------------------------
    theta = 5 * pi / 6
    stirling = 2 * sin(theta)                 # forced to 1 by the saddle
    hess = fabs(cot(theta))                   # |Lambda''| = |cot|
    derived = stirling * hess ** (-mpf(1) / 2)
    target = mpf(3) ** (-mpf(1) / 4)
    print("\n  saddle  2 sin(theta*) = 1  =>  theta* = 5 pi/6")
    print(f"  Stirling factor 2 sin(theta*) = {mp.nstr(stirling, 20)}")
    print(f"  Hessian  |cot(theta*)|       = {mp.nstr(hess, 20)}   (= sqrt 3)")
    print(f"  c_sigma = 2 sin * |cot|^-1/2 = {mp.nstr(derived, 22)}")
    print(f"  3^(-1/4)                     = {mp.nstr(target, 22)}")
    symbolic_ok = fabs(derived / target - 1) < mpf("1e-40")
    print(f"  agree: {symbolic_ok}")

    # tau_DG is the Hessian over the Stirling factor
    tau_from_hess = hess / 2
    tau_ok = fabs(tau_from_hess / tau41_corpus - 1) < mpf("1e-40")
    print(f"\n  |tau_DG| from the Hessian = |cot(theta*)|/2 = "
          f"{mp.nstr(tau_from_hess, 22)}")
    print(f"  |tau_DG|(4_1) in the corpus                  = "
          f"{mp.nstr(tau41_corpus, 22)}   agree: {tau_ok}")

    k_derived = derived * tau_from_hess ** (mpf(1) / 2)
    k_ok = fabs(k_derived - mpf(2) ** (-mpf(1) / 2)) < mpf("1e-40")
    print(f"\n  k = c_sigma |tau|^(1/2) = {mp.nstr(k_derived, 22)}"
          f"   vs 2^(-1/2) = {mp.nstr(mpf(2)**(-mpf(1)/2), 22)}   {k_ok}")

    # -- numerical confirmation from Kashaev's sum -----------------------
    print("\n  Kashaev's sum, Richardson-extrapolated (error is O(1/N)):\n")
    print(f"    {'N':>7} {'c_sigma(N)':>20} {'rel to 3^-1/4':>15}")
    Ns = (4000, 8000, 16000, 32000, 64000)
    vals = {}
    for N in Ns:
        vals[N] = c_sigma_N(N)
        print(f"    {N:7d} {vals[N]:20.15f} {vals[N]/float(target)-1:15.3e}")
    rich = 2 * vals[64000] - vals[32000]
    rel = abs(rich / float(target) - 1)
    numeric_ok = rel < 1e-9
    print(f"\n    Richardson (32000, 64000) = {rich:.15f}")
    print(f"    3^(-1/4)                  = {float(target):.15f}")
    print(f"    relative                  = {rel:.3e}   -> {numeric_ok}")

    # the corpus's own extrapolated value, for the record
    corpus_rel = fabs(target / cs41_corpus - 1)
    print(f"\n  corpus measured c_sigma(4_1) = {mp.nstr(cs41_corpus, 22)}")
    print(f"  derived                       = {mp.nstr(target, 22)}"
          f"   rel {mp.nstr(corpus_rel, 4)}")
    corpus_ok = corpus_rel < mpf("1e-16")

    all_ok = symbolic_ok and tau_ok and k_ok and numeric_ok and corpus_ok
    verdict = (
        "THE KNOT SIDE IS CLOSED. c_sigma(4_1) = 3^{-1/4} and the power N^{3/2} "
        "are both DERIVED, by Laplace on Kashaev's one-variable sum: the saddle "
        "condition is 2 sin(theta) = 1, giving theta* = 5 pi/6, and c_sigma = "
        "2 sin(theta*) |cot(theta*)|^{-1/2}. In one variable the saddle "
        "condition forces the Stirling factor 2 sin(theta*) to 1, so c_sigma = "
        "3^{-1/4} with no freedom at all. Hence k = c_sigma |tau_DG|^{1/2} = "
        "2^{-1/2} on the KNOT side too, with no calibration anywhere: combined "
        "with qou-vdvS on the link side, the constant in "
        "c_sigma = k |tau_DG|^{-1/2} is now derived at both legs, and the 4_1 "
        "calibration that the whole c_sigma arc rested on is retired. The "
        "1-loop invariant is exhibited as literally the Hessian of the "
        "Lobachevsky potential at the geometric saddle: |tau_DG|(4_1) = "
        "|cot(theta*)|/2 = sqrt3/2. Closed forms exist at the two regular ideal "
        "polyhedra — tetrahedron (trace field Q(sqrt-3)) and octahedron (trace "
        "field Q(i)) — and those are the only two imaginary quadratic fields "
        "with extra units, which is why there is no third analytic case."
        if all_ok else
        "A CHECK FAILED — inspect before citing.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-c-sigma-tetrahedral", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Derives c_sigma(4_1) = 3^{-1/4} and the power N^{3/2} by Laplace on "
        "Kashaev's one-variable sum, closing the knot side that qou-vdvS left "
        "open. Together with the link-side closed form this retires the 4_1 "
        "calibration: k = 2^{-1/2} is derived at both legs. Exhibits tau_DG as "
        "the Hessian of the Lobachevsky potential at the geometric saddle, and "
        "identifies why exactly two closed-form families exist — the two "
        "regular ideal polyhedra, with trace fields Q(sqrt-3) and Q(i). "
        "Nothing fitted; the value is predicted from the saddle and only "
        "confirmed numerically.")
    wb.set_audit_only(
        "docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md")
    wb.add_data("derivation", {
        "state_sum": "<4_1>_N = sum_k |(q;q)_k|^2 = sum_k exp(-2 s_k)",
        "expansion": ("s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) "
                      "+ O(1/N), theta = k pi/N — the same expansion verified "
                      "for van der Veen's Lemma 3"),
        "saddle_condition": "Lambda'(theta) = -log(2 sin theta) = 0, so 2 sin theta* = 1",
        "theta_star": "5 pi/6 (pi/6 is the minimum)",
        "volume": "(2N/pi) Lambda(pi/6) = Vol N/(2 pi), Vol(4_1) = 4 Lambda(pi/6)",
        "stirling_factor": mp.nstr(stirling, 25),
        "hessian_abs_cot": mp.nstr(hess, 25),
        "c_sigma_derived": mp.nstr(derived, 25),
        "c_sigma_closed_form": "3^{-1/4}",
        "N_power": "3/2, also derived",
        "rigidity": ("in one variable the saddle condition IS 2 sin theta* = 1, "
                     "so the Stirling factor is forced to 1 and "
                     "c_sigma = |cot theta*|^{-1/2} = 3^{-1/4} with no freedom"),
    })
    wb.add_data("tau_is_the_hessian", {
        "claim": "|tau_DG|(4_1) = |cot(theta*)| / 2 = sqrt3 / 2",
        "from_hessian": mp.nstr(tau_from_hess, 25),
        "corpus_value": mp.nstr(tau41_corpus, 25),
        "agree": bool(tau_ok),
        "reading": ("the DG 1-loop invariant is the Hessian determinant of the "
                    "Lobachevsky potential at the geometric saddle, divided by "
                    "the Stirling factor; this is the smallest case where that "
                    "can be seen explicitly"),
    })
    wb.add_data("k_is_now_derived_at_both_legs", {
        "knot_side": "k = 3^{-1/4} (sqrt3/2)^{1/2} = 2^{-1/2}",
        "link_side": "k = 2^{1/2-n}(n^2+m^2)^{-1/4} * (2^{2n-2} sqrt(n^2+m^2))^{1/2} = 2^{-1/2}",
        "k_derived": mp.nstr(k_derived, 25),
        "calibration_retired": bool(k_ok),
    })
    wb.add_data("why_exactly_two_closed_form_families", {
        "principle": ("the saddle sits at a root-of-unity shape exactly for the "
                      "regular ideal polyhedra, and then det(Hessian) is an "
                      "algebraic number in a cyclotomic trace field"),
        "tetrahedral": {"shape": "exp(i pi/3)", "trace_field": "Q(zeta_3) = Q(sqrt-3)",
                        "tau": "sqrt3 / 2", "example": "4_1"},
        "octahedral": {"shape": "i", "trace_field": "Q(zeta_4) = Q(i)",
                       "tau": "2^{2n-2} |A|, A = n - m i in Z[i]",
                       "example": "W_{a,1,c,d}"},
        "why_no_third": ("those are the two imaginary quadratic fields with "
                         "extra units — the two Bianchi cases. Q(zeta_5) is "
                         "degree 4, so no 5-fold regular ideal polyhedron "
                         "arises by this route"),
        "but_the_pattern_is_norms_not_polyhedra": (
            "the polyhedra are how a Z[zeta] norm shows up HERE; they are not "
            "the general mechanism. |H_1(Sigma_d(K))| = "
            "|Res(Delta, (t^d-1)/(t-1))| is a norm from Z[zeta_d] too, and it "
            "needs no polyhedron: Sigma_5(trefoil) is the Poincare sphere "
            "Sigma(2,3,5) and Sigma_2(cinquefoil) is L(5,q) with |H_1| = 5, "
            "whose WRT invariant is the Gauss sum sum_k zeta_5^{k^2} = sqrt5. "
            "That is where a sqrt5 lives. It is NOT a c_sigma: Sigma(2,3,5) is "
            "Seifert-fibred with Vol = 0 and there is no Lobachevsky saddle at "
            "all, so the constant there is a different object reached by a "
            "different mechanism (Lawrence-Zagier 1999). See bean qou-lz235; "
            "do not conflate the two sqrt5's"),
    })
    wb.add_assertion(
        "c_sigma_4_1_derived_equals_3_pow_minus_quarter",
        computed="1" if symbolic_ok else "0", expected="1", tolerance="0.5",
        source="2 sin(theta*) |cot(theta*)|^{-1/2} against 3^{-1/4}, symbolically")
    wb.add_assertion(
        "kashaev_sum_confirms_numerically",
        computed="1" if numeric_ok else "0", expected="1", tolerance="0.5",
        source=("Kashaev's sum at N = 32000, 64000, Richardson-extrapolated, "
                "against 3^{-1/4}"))
    wb.add_assertion(
        "tau_dg_equals_hessian_over_stirling",
        computed="1" if tau_ok else "0", expected="1", tolerance="0.5",
        source="|cot(theta*)|/2 against the corpus's computed |tau_DG|(4_1)")
    wb.add_assertion(
        "k_equals_2_pow_minus_half_on_the_knot_side",
        computed="1" if k_ok else "0", expected="1", tolerance="0.5",
        source="c_sigma |tau_DG|^{1/2} against 2^{-1/2}, with both derived")
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
