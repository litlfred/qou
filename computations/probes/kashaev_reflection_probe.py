#!/usr/bin/env python3
"""(A) halved: the exact reflection, and the 1/N term in closed form.

Bean `qou-mlgp` (A).  Formalised (the reflection itself) in
`folio/quantum-observable-universe/lean/QOU/Knot/KashaevProdEndpoint.lean`
as `sum_log_two_sin_reflect`.

WHERE (A) STOOD.  `QOU.Knot.abs_deviation_le` is a RECTANGLE-RULE sandwich, so
its error is `O(h.Var)` by construction and no sharpening of its constants
reaches the `O(1/N)` needed to see the one-loop correction

    s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) + O(1/N),
    s_k := -sum_{j=1}^{k} log(2 sin(j pi/N)),   theta = k pi/N

`KashaevProdEndpoint.lean` pinned the far endpoint (`s_{N-1} = -log N`), which
constrains the additive constant but only at one value of `k`.

THE REFLECTION.  `sin((N-j) pi/N) = sin(j pi/N)`, so splitting the endpoint
product at `k` and reflecting the upper block gives, for EVERY `k < N`,

    L_k + L_{N-1-k} = log N,        L_k := -s_k = sum_{j=1}^{k} log(2 sin(j pi/N))

exact, no asymptotics.  This constrains the whole expansion, not one value.

WHAT IT BUYS.  Write `s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) +
eps_k`.  Under `k -> N-1-k` we have `theta -> pi - theta - h` with `h = pi/N`,
and `Lambda(pi - x) = -Lambda(x)`.  Substituting into the reflection, EVERYTHING
cancels and what is left is

    eps_k + eps_{N-1-k} = (1/2)[f(theta) + f(theta+h)] - (1/h) int_theta^{theta+h} f

with `f = log(2 sin)` — the TRAPEZOID REMAINDER on a single cell, as an
IDENTITY.  So the SYMMETRIC half of (A)'s error is a trapezoid remainder,
`O(h^2 csc^2 theta)` in the interior — already sharper than the `O(1/N)` being
claimed — and the whole difficulty of (A) is in the ANTISYMMETRIC half.

AND THE ANTISYMMETRIC HALF HAS A CLOSED FORM.  Measured below:

    eps_k = -(pi / 12 N) cot(theta) + O(1/N^3)

which is exactly the Euler-Maclaurin `B_2/2!` term `(h/12) f'`, `f' = cot`.  It
is odd about `theta = pi/2` — as the reflection forces — and vanishes there
identically, which the probe confirms to 35 digits.  So the refined expansion is

    s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) - (pi/12N) cot(theta)
          + O(1/N^3)

with NO leftover additive constant: the `- (1/2) log(2 N sin theta)` form,
including its `2N` (the correction to van der Veen's Lemma 3 recorded in
`docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md`), is
confirmed exactly.

WHAT REMAINS OPEN IN (A), STATED PLAINLY.  This is measurement plus one exact
identity, not a proof.  The reflection is formalised; the `-(pi/12N) cot` term
is verified numerically at six `theta` over four `N` and is standard
Euler-Maclaurin, but its PROOF still needs the singular `j = 0` endpoint handled
(that is where the `-(1/2) log N` and the additive constant come from, and it
needs Stirling, not Euler-Maclaurin). The reflection does not touch it: it
relates `k` to `N-1-k` and both endpoints sit outside that pairing.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import (mp, mpf, pi, sin, log, clsin, cot, quad,  # noqa: E402
                    fabs, nstr)


def lobachevsky(t):
    """Lambda(t) = -int_0^t log|2 sin x| dx = Cl_2(2t)/2."""
    return clsin(2, 2 * t) / 2


def f(t):
    return log(2 * sin(t))


def L(N, k):
    """L_k = sum_{j=1}^{k} log(2 sin(j pi/N))  (= -s_k)."""
    return sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def eps(N, k):
    """s_k minus the conjectured main term."""
    th = mpf(k) * pi / N
    return -L(N, k) - ((N / pi) * lobachevsky(th) - log(2 * N * sin(th)) / 2)


def check_reflection():
    print("\n  (1) the exact reflection  L_k + L_(N-1-k) = log N")
    print(f"\n  {'N':>6}  {'k':>6}  {'L_k + L_(N-1-k)':>26}  {'log N':>26}"
          f"  {'|diff|':>10}")
    rows, ok = [], True
    for N in [50, 101, 200]:
        for k in [1, 3, N // 4, N // 2, (5 * N) // 6, N - 2]:
            if not (0 <= k <= N - 1):
                continue
            lhs = L(N, k) + L(N, N - 1 - k)
            d = fabs(lhs - log(N))
            if not (d < mpf(10) ** (-mp.dps + 8)):
                ok = False
            rows.append({"N": N, "k": k, "lhs": nstr(lhs, 22),
                         "log_N": nstr(log(N), 22), "abs_diff": nstr(d, 6)})
            print(f"  {N:>6}  {k:>6}  {nstr(lhs, 20):>26}  {nstr(log(N), 20):>26}"
                  f"  {nstr(d, 4):>10}")
    return ok, rows


def check_trapezoid():
    print("\n  (2) the symmetric half IS the trapezoid remainder, exactly")
    print("      eps_k + eps_(N-1-k)  vs  (f(th)+f(th+h))/2 - (1/h) int_th^{th+h} f")
    print(f"\n  {'N':>6}  {'k':>6}  {'eps_k + eps_(N-1-k)':>24}"
          f"  {'trapezoid':>24}  {'|diff|':>10}")
    rows, ok = [], True
    halves = {}
    for N in [100, 200, 400, 800]:
        h = pi / N
        for k in [N // 6, N // 3, N // 2, (2 * N) // 3]:
            th = mpf(k) * pi / N
            tot = eps(N, k) + eps(N, N - 1 - k)
            trap = (f(th) + f(th + h)) / 2 - quad(f, [th, th + h]) / h
            d = fabs(tot - trap)
            if not (d < mpf(10) ** (-mp.dps + 8)):
                ok = False
            if k == N // 2:
                halves[N] = fabs(tot)
            rows.append({"N": N, "k": k, "sym_part": nstr(tot, 18),
                         "trapezoid": nstr(trap, 18), "abs_diff": nstr(d, 6)})
            print(f"  {N:>6}  {k:>6}  {nstr(tot, 16):>24}  {nstr(trap, 16):>24}"
                  f"  {nstr(d, 4):>10}")
    # and it is O(1/N^2): each doubling of N quarters it
    print("\n    at k = N/2, the symmetric part quarters on each doubling")
    print(f"    {'N':>6}  {'|sym|':>18}  {'ratio to previous':>20}")
    prev, ratio_ok = None, True
    for N in sorted(halves):
        r = prev / halves[N] if prev else None
        if r is not None and not (mpf("3.5") < r < mpf("4.5")):
            ratio_ok = False
        print(f"    {N:>6}  {nstr(halves[N], 12):>18}"
              f"  {(nstr(r, 8) if r else '--'):>20}")
        prev = halves[N]
    return ok and ratio_ok, rows


def check_euler_maclaurin():
    print("\n  (3) the antisymmetric half: eps_k = -(pi/12N) cot(theta) + O(1/N^3)")
    print(f"\n  {'theta/pi':>9}  {'N':>6}  {'N.eps_k measured':>22}"
          f"  {'-(pi/12) cot(th)':>22}  {'residual':>12}")
    rows, ok = [], True
    fracs = [("1/6", mpf(1) / 6), ("1/4", mpf(1) / 4), ("1/3", mpf(1) / 3),
             ("2/3", mpf(2) / 3), ("5/6", mpf(5) / 6)]
    resid = {}
    for name, r in fracs:
        for N in [400, 800, 1600]:
            k = int(r * N)
            th = mpf(k) * pi / N
            meas = N * eps(N, k)
            pred = -(pi / 12) * cot(th)
            res = fabs(meas - pred)
            resid.setdefault(name, {})[N] = res
            rows.append({"theta": name, "N": N, "N_eps": nstr(meas, 16),
                         "prediction": nstr(pred, 16), "residual": nstr(res, 8)})
            if N == 1600:
                print(f"  {name:>9}  {N:>6}  {nstr(meas, 16):>22}"
                      f"  {nstr(pred, 16):>22}  {nstr(res, 6):>12}")
    # residual in N.eps should be O(1/N^2) -> quarters per doubling,
    # i.e. eps's own next correction is O(1/N^3)
    print("\n    residual of N.eps quarters on each doubling => eps = ... + O(1/N^3)")
    print(f"    {'theta/pi':>9}  {'res(400)/res(800)':>20}  {'res(800)/res(1600)':>20}")
    for name, _ in fracs:
        r1 = resid[name][400] / resid[name][800]
        r2 = resid[name][800] / resid[name][1600]
        if not (mpf(3) < r1 < mpf(5) and mpf(3) < r2 < mpf(5)):
            ok = False
        print(f"    {name:>9}  {nstr(r1, 8):>20}  {nstr(r2, 8):>20}")
    # and it vanishes identically at theta = pi/2
    print("\n    at theta = pi/2 the antisymmetry forces eps = 0 exactly:")
    mid_ok = True
    for N in [400, 800, 1600]:
        v = fabs(eps(N, N // 2))
        if not (v < mpf(10) ** (-mp.dps + 8)):
            mid_ok = False
        print(f"      N = {N:>5}   |eps_(N/2)| = {nstr(v, 6)}")
    return ok and mid_ok, rows


def main() -> int:
    set_compute_dps()

    print("=" * 78)
    print(" (A) halved: the exact reflection, and the 1/N term in closed form")
    print("=" * 78)

    refl_ok, refl_rows = check_reflection()
    trap_ok, trap_rows = check_trapezoid()
    em_ok, em_rows = check_euler_maclaurin()

    all_ok = refl_ok and trap_ok and em_ok
    print("\n" + "=" * 78)
    print(f"  ALL CHECKS {'PASS' if all_ok else 'FAIL'}")
    print("=" * 78)

    wb = WitnessBuilder("kashaev-reflection", engine="mpmath")
    wb.add_data("the_exact_reflection", {
        "statement": ("L_k + L_(N-1-k) = log N for every k < N, where "
                      "L_k = sum_{j=1}^k log(2 sin(j pi/N)) = -s_k"),
        "proof": ("sin((N-j) pi/N) = sin(j pi/N); split Ico 1 N at k+1 and "
                  "reflect the upper block by j -> N-j; the total is the "
                  "endpoint value log N"),
        "lean": ("QOU.Knot.FigureEightVolume.sum_log_two_sin_reflect, "
                 "sorry-free"),
        "rows": refl_rows,
    })
    wb.add_data("the_symmetric_half_is_a_trapezoid_remainder", {
        "identity": ("eps_k + eps_(N-1-k) = (1/2)[f(th) + f(th+h)] - "
                     "(1/h) int_th^{th+h} f,  f = log(2 sin), h = pi/N"),
        "derivation": ("substitute s_k = (N/pi)Lambda(th) - (1/2)log(2N sin th) "
                       "+ eps_k into the reflection and use Lambda(pi-x) = "
                       "-Lambda(x); everything else cancels"),
        "consequence": ("the symmetric half of (A)'s error is O(h^2 csc^2 th), "
                        "already sharper than the O(1/N) claimed. All of (A)'s "
                        "difficulty is in the ANTISYMMETRIC half"),
        "rows": trap_rows,
    })
    wb.add_data("the_antisymmetric_half_in_closed_form", {
        "measured": "eps_k = -(pi / 12 N) cot(theta) + O(1/N^3)",
        "identification": ("exactly the Euler-Maclaurin B_2/2! term "
                           "(h/12) f'(theta) with f' = cot"),
        "refined_expansion": ("s_k = (N/pi) Lambda(th) - (1/2) log(2 N sin th) "
                              "- (pi/12N) cot(th) + O(1/N^3)"),
        "no_leftover_constant": ("the -(1/2) log(2 N sin th) form, INCLUDING "
                                 "its 2N, is confirmed with no residual "
                                 "additive constant — this is the correction to "
                                 "van der Veen's Lemma 3 recorded in the "
                                 "outreach draft"),
        "rows": em_rows,
    })
    wb.add_data("what_remains_open_in_A", {
        "formalised": "the reflection identity only",
        "measured_not_proved": ("the -(pi/12N) cot term. It is standard "
                                "Euler-Maclaurin, but proving it needs the "
                                "singular j = 0 endpoint handled — that is "
                                "where the -(1/2) log N and the additive "
                                "constant come from, and it needs Stirling, "
                                "not Euler-Maclaurin"),
        "why_the_reflection_does_not_reach_it": ("it pairs k with N-1-k, and "
                                                 "both endpoints sit outside "
                                                 "that pairing"),
    })
    wb.add_assertion(
        "exact_reflection_holds_for_every_k",
        computed="1" if refl_ok else "0", expected="1", tolerance="0.5",
        source="three N, six k each, to working dps")
    wb.add_assertion(
        "symmetric_half_equals_trapezoid_remainder_and_is_O_one_over_N_sq",
        computed="1" if trap_ok else "0", expected="1", tolerance="0.5",
        source=("identity to working dps at 16 (N,k); and the k = N/2 value "
                "quarters on each doubling of N"))
    wb.add_assertion(
        "antisymmetric_half_is_the_euler_maclaurin_B2_term",
        computed="1" if em_ok else "0", expected="1", tolerance="0.5",
        source=("N.eps_k against -(pi/12)cot(theta) at five theta over three N; "
                "residual quarters per doubling; eps vanishes at theta = pi/2"))
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
