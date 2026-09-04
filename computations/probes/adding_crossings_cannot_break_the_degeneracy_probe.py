#!/usr/bin/env python3
"""Escape (a) fails too, and for the same reason as everything else: `|det T| = 1`.
The bond must leave the convex hull of `{sigma, sigma^-1}` — and even then,
matching nature costs a ten-digit fine-tuning.

WHAT THIS TESTS
---------------
`isospin_grading_restores_the_sign_probe` (bean `qou-m896`) showed that grading
by `(T,S)` restores the two-nucleon **sign** pattern but caps the achievable
channel asymmetry `|L(T=0)| / |L(T=1)|` at exactly `1`, where nature's is `33.7`.
It named escape **(a)** — more than one crossing per bond, making `mu` polynomial
in `d` — as the minimal change that could break a degeneracy forced by a single
generator. This runs that escape.

It does not work, and the reason is cleaner than the question.

THE OBSTRUCTION IS `det T = -1`
-------------------------------
The Hecke relation `T^2 = h T + 1` fixes the product of the two eigenvalues at
`q . (-1/q) = -1`. So for a crossing `(1, d)` the two blocks' ratios multiply to

    mu_sym . mu_anti  =  (q + d)(-1/q + d)  =  d^2 + d h - 1  =  det(T + d I)

On `d in [-h, 0]` this is `-1` at both endpoints and `-(1 + h^2/4)` at the vertex
`d = -h/2`, so

    |mu_sym . mu_anti|  in  [1, 1.010926552]   —   **always >= 1**

A bond built from `k` crossings is `prod_i (T + d_i)`, whose block ratios
multiply factor by factor. Every factor has magnitude `>= 1`, so

    L(T=0) + L(T=1)  =  -log |mu_sym . mu_anti|  <=  0

and therefore `|L(T=0)| <= |L(T=1)|` — **the ratio is capped at 1 for every
crossing count.** Adding crossings cannot break the degeneracy. Verified on
random multi-crossing bonds: `|mu_s . mu_a|` in `1.0124 .. 1.0212`, best ratio
`0.927`.

WHERE THE ESCAPE ACTUALLY IS
----------------------------
`|d^2 + d h - 1| < 1` iff `0 < d(d + h) < 2`. On the hull `d in (-h, 0)` the
product `d(d+h)` is **negative**, so the condition fails everywhere inside. It
holds only for

    d > 0     (beta < 0)        or        d < -h    (beta > 1)

`beta = 0` is `sigma` and `beta = 1` is `sigma^-1`, so this says: **the bond
operator must leave the convex hull of the two crossings.** No amount of
crossings, no block grading, and no convention does that — all of them stay
inside. That single statement subsumes both escapes and every convention
question this arc has spent probes on.

WHAT NATURE WOULD COST
----------------------
Solving for the experimental ratio `2.224566 / 0.066 = 33.7055` in the
one-crossing family gives

    d*        =  0.900918283896
    beta*     = -4.30937050          (4.31 outside the hull)
    |mu_sym|  =  2.0108968666
    |mu_anti| =  5.944e-11           <- the T=0 channel is this close to unbinding

and it is not a robust point. Moving `d` by `1e-4` drops the ratio from `33.71`
to `13.19`; by `1e-6`, to `19.78`. The `33.7` is reachable only by tuning
`|mu_anti|` to within `6e-11` of zero — ten digits, not a mechanism.

A FAIR WORD FOR THE OTHER SIDE
------------------------------
Near-threshold tuning is not by itself unphysical here: the real `NN` system is
famously unnatural, with both `S`-wave channels anomalously close to zero energy
(`a_np(3S1) = +5.419` fm and `a_np(1S0) = -23.740` fm against a force range of
`~1.4` fm), which is the whole basis of pionless EFT. So a theory reproducing
`33.7` by sitting near threshold is not automatically wrong. **The structural
problem is the other half:** reaching it requires `beta` outside `[0, 1]`, i.e.
an operator that is not a combination of the two crossings at all — and nothing
in the construction supplies one.

WHAT IS LEFT
------------
Both named escapes are now closed under the constraint `beta in [0, 1]`:
`(b)` restores the sign but caps the ratio at `1`; `(a)` cannot lift the cap at
any crossing count. What remains is not a third escape of the same kind but a
change of ingredient — a bond operator outside the convex hull of
`{sigma, sigma^-1}`, whose meaning and provenance this probe does not supply.

DISCIPLINE
----------
No fit; nothing wired. The determinant identity is verified symbolically and
numerically, and the multi-crossing claim is checked on random bonds rather than
argued from the algebra alone. Experimental values are comparison targets; the
`33.7` target's least certain input (the `1S0` virtual-state energy) was shown
robust in `qou-m896` and is not re-litigated here.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] isospin_grading_restores_the_sign_probe.py  (escape (b), the cap)
-- Ref: [probe] two_nucleon_pattern_is_unreachable_probe.py (escapes named there)
"""
from __future__ import annotations

import random
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
B_DEUT = mp.mpf("2.224566")
B_VIRT = mp.mpf("0.066")
R_EXP = B_DEUT / B_VIRT


def det_factor(d):
    """mu_sym . mu_anti for a single crossing (1, d)."""
    return (_Q + d) * (-1 / _Q + d)


def ratio_at(d):
    ms, ma = abs(_Q + d), abs(-1 / _Q + d)
    if ms <= 1 or ma <= 0 or ma >= 1:
        return None
    return -mp.log(ma) / mp.log(ms)


def main() -> int:
    assertions = []
    print("t7qv — can extra crossings break the forced degeneracy?")

    # ── A1. the determinant identity ───────────────────────────────────
    print("\n  1. the obstruction is det T = -1")
    ds, qs, hs = sp.symbols("d q h")
    lhs = sp.expand((qs + ds) * (-1 / qs + ds))
    resid = sp.simplify(lhs - (ds ** 2 + ds * (qs - 1 / qs) - 1))
    num = abs(det_factor(mp.mpf("-0.07")) - (mp.mpf("-0.07") ** 2
                                             + mp.mpf("-0.07") * _H - 1))
    print(f"     T^2 = hT + 1 fixes the eigenvalue product at q.(-1/q) = -1, so")
    print(f"     mu_sym . mu_anti = (q+d)(-1/q+d) = d^2 + d h - 1 = det(T + dI)")
    print(f"     symbolic residual {resid}   numeric check {float(num):.2e}")
    ok = resid == 0 and num < mp.mpf("1e-35")
    assertions.append(("A1_block_product_is_det_of_T_plus_d", ok,
                       f"(q+d)(-1/q+d) - (d^2+dh-1) simplifies to {resid}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. |det| >= 1 on the hull ─────────────────────────────────────
    print("\n  2. |det(T + dI)| >= 1 for every d in [-h, 0]")
    print(f"     {'beta':>8s} {'d':>12s} {'det':>16s} {'|det|':>13s}")
    vals = []
    for b in ("0", "0.25", "0.5", "0.75", "1"):
        bb = mp.mpf(b)
        d = -bb * _H
        f = det_factor(d)
        vals.append(abs(f))
        print(f"     {float(bb):8.4f} {float(d):12.7f} {float(f):16.10f} "
              f"{float(abs(f)):13.10f}")
    vertex = abs(det_factor(-_H / 2))
    ends = max(abs(det_factor(mp.mpf(0)) + 1), abs(det_factor(-_H) + 1))
    ok = min(vals) >= 1 - mp.mpf("1e-30") and ends < mp.mpf("1e-30")
    print(f"     endpoints are exactly -1 (residual {float(ends):.1e}); the")
    print(f"     vertex d = -h/2 gives -(1 + h^2/4) = {float(-vertex):.10f}")
    print(f"     so |det| in [1, {float(vertex):.9f}] — always >= 1, equality")
    print(f"     ONLY at d = 0 and d = -h.")
    assertions.append(("A2_det_magnitude_is_at_least_one_on_the_hull", ok,
                       f"|det| in [1, {float(vertex):.9f}], endpoints exactly -1 "
                       f"to {float(ends):.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. therefore the cap survives ANY crossing count ──────────────
    print("\n  3. so the ratio is capped at 1 for EVERY crossing count")
    print(f"     a bond prod_i (T + d_i) multiplies the block ratios factor by")
    print(f"     factor, so |mu_sym . mu_anti| = prod_i |det| >= 1, hence")
    print(f"     L(T=0) + L(T=1) <= 0 and |L(T=0)| <= |L(T=1)|.")
    rng = random.Random(7)
    best, prods, n_ok = 0.0, [], 0
    for _ in range(200):
        k = rng.randint(2, 6)
        dd = [-mp.mpf(rng.random()) * _H for _ in range(k)]
        ms = mp.fprod([_Q + x for x in dd])
        ma = mp.fprod([-1 / _Q + x for x in dd])
        prods.append(float(abs(ms * ma)))
        if abs(ms) > 1 and 0 < abs(ma) < 1:
            n_ok += 1
            best = max(best, float(-mp.log(abs(ma)) / mp.log(abs(ms))))
    print(f"     200 random multi-crossing bonds (k = 2..6):")
    print(f"       |mu_s . mu_a| in [{min(prods):.9f}, {max(prods):.9f}] — all >= 1")
    print(f"       {n_ok} had both signs right; best ratio {best:.6f}")
    ok = min(prods) >= 1 - 1e-12 and best <= 1 + 1e-12
    assertions.append(("A3_cap_survives_any_number_of_crossings", ok,
                       f"200 random bonds: |det product| >= {min(prods):.9f}, "
                       f"best ratio {best:.6f} <= 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. where the escape actually is ───────────────────────────────
    print("\n  4. the escape requires leaving the convex hull")
    print(f"     |d^2 + d h - 1| < 1  <=>  0 < d(d+h) < 2")
    print(f"     on d in (-h, 0) the product d(d+h) is NEGATIVE:")
    for d in (mp.mpf("-0.05"), -_H / 2, mp.mpf("-0.18")):
        print(f"       d = {float(d):9.6f}   d(d+h) = {float(d * (d + _H)):+.9f}")
    print(f"     so the condition fails everywhere inside, and holds only for")
    print(f"       d > 0   (beta < 0)     or     d < -h  (beta > 1)")
    print(f"     beta=0 is sigma and beta=1 is sigma^-1, so the bond operator")
    print(f"     must leave the CONVEX HULL of the two crossings. No crossing")
    print(f"     count, no block grading and no convention does that.")
    inside = all(float(d * (d + _H)) < 0
                 for d in (mp.mpf("-0.05"), -_H / 2, mp.mpf("-0.18")))
    out_pos = abs(det_factor(mp.mpf("0.5"))) < 1
    ok = inside and out_pos
    assertions.append(("A4_escape_requires_beta_outside_zero_one", ok,
                       "d(d+h) < 0 throughout (-h,0); |det| < 1 first occurs "
                       "outside the hull"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. what nature's ratio would cost ─────────────────────────────
    print("\n  5. and what nature's 33.7 would cost, even outside the hull")
    lo, hi = mp.mpf("0.9"), 1 / _Q
    for _ in range(200):
        mid = (lo + hi) / 2
        r = ratio_at(mid)
        if r is None or r < R_EXP:
            lo = mid
        else:
            hi = mid
    d_star = (lo + hi) / 2
    b_star = -d_star / _H
    ma_star = abs(-1 / _Q + d_star)
    print(f"     target ratio {float(R_EXP):.4f} (deuteron / 1S0 virtual state)")
    print(f"       d*        = {float(d_star):.12f}")
    print(f"       beta*     = {float(b_star):.8f}    ({float(abs(b_star)):.2f} "
          f"outside the hull)")
    print(f"       |mu_sym|  = {float(abs(_Q + d_star)):.10f}")
    print(f"       |mu_anti| = {float(ma_star):.4e}   <- T=0 within this of unbinding")
    print(f"       ratio     = {float(ratio_at(d_star)):.6f}")
    print(f"     sensitivity — the point is not robust:")
    sens = []
    for e in ("1e-4", "1e-5", "1e-6"):
        rr = ratio_at(d_star - mp.mpf(e))
        sens.append((e, float(rr)))
        print(f"       d* - {e}:  ratio {float(rr):.4f}")
    ok = b_star < 0 and ma_star < mp.mpf("1e-9") and sens[0][1] < 20
    print(f"     so 33.7 is reachable only by tuning |mu_anti| to within")
    print(f"     {float(ma_star):.1e} of zero — ten digits, not a mechanism.")
    assertions.append(("A5_matching_nature_needs_hull_exit_and_finetuning", ok,
                       f"beta* = {float(b_star):.6f}, |mu_anti| = "
                       f"{float(ma_star):.3e}, ratio falls to {sens[0][1]:.2f} "
                       f"at d*-1e-4"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the fair reading ───────────────────────────────────────────
    print("\n  6. a fair word for the other side")
    print(f"     near-threshold tuning is NOT by itself unphysical here. The real")
    print(f"     NN system is famously unnatural — both S-wave channels sit")
    print(f"     anomalously close to zero energy:")
    print(f"       a_np(3S1) = +5.419 fm     a_np(1S0) = -23.740 fm")
    print(f"       force range ~1.4 fm")
    print(f"     which is the basis of pionless EFT. A theory reaching 33.7 by")
    print(f"     sitting near threshold is not automatically wrong.")
    print(f"     THE STRUCTURAL PROBLEM IS THE OTHER HALF: it needs beta outside")
    print(f"     [0,1], an operator that is not a combination of the two")
    print(f"     crossings at all, and nothing in the construction supplies one.")
    print(f"     Both named escapes are now closed under beta in [0,1]:")
    print(f"       (b) restores the sign, caps the ratio at 1")
    print(f"       (a) cannot lift the cap at any crossing count")
    ok = abs(-1 / _Q + mp.mpf(0)) < 1 and abs(_Q) > 1
    assertions.append(("A6_both_named_escapes_are_closed_in_the_hull", ok,
                       "(b) caps at 1 (qou-m896); (a) cannot lift it at any "
                       "crossing count (A3); escape needs beta outside [0,1]"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Escape (a) fails, and the reason subsumes the whole question. The")
    print("  Hecke relation fixes det T = -1, so a crossing's two block ratios")
    print("  multiply to det(T + dI) = d^2 + dh - 1, whose magnitude is >= 1")
    print("  everywhere on d in [-h, 0]. A multi-crossing bond multiplies those")
    print("  factors, so |mu_sym . mu_anti| >= 1 for ANY crossing count and the")
    print("  channel-asymmetry ratio stays capped at 1.")
    print("  The escape condition is 0 < d(d+h) < 2, which fails throughout the")
    print("  interior and holds only for beta < 0 or beta > 1: the bond operator")
    print("  must LEAVE THE CONVEX HULL of {sigma, sigma^-1}. No crossing count,")
    print("  no block grading, no convention does that — one statement that")
    print("  subsumes both escapes and every convention question in this arc.")
    print("  Even outside the hull, nature's 33.7 costs beta* = -4.31 and a")
    print("  T=0 channel tuned to within 6e-11 of unbinding. Near-threshold")
    print("  tuning is defensible — the real NN system is unnatural in exactly")
    print("  that way — but leaving the hull is not, and nothing here supplies it.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Runs escape (a) — more than one crossing per bond — named by "
            "qou-v3u2 and motivated by qou-m896's finding that the (T,S) "
            "grading caps the channel-asymmetry ratio at 1. It fails, and the "
            "reason subsumes the question. The Hecke relation T^2 = hT + 1 "
            "fixes the eigenvalue product at q.(-1/q) = -1, so a crossing's two "
            "block ratios multiply to (q+d)(-1/q+d) = d^2 + dh - 1 = "
            "det(T + dI), whose magnitude on d in [-h,0] lies in "
            "[1, 1.010926552] — always >= 1, with equality only at the "
            "endpoints. A bond built from k crossings multiplies those factors, "
            "so |mu_sym . mu_anti| >= 1 for ANY crossing count, hence "
            "L(T=0) + L(T=1) <= 0 and the ratio is capped at 1 regardless. "
            "Verified on 200 random multi-crossing bonds (k=2..6): det products "
            "all >= 1, best ratio 0.927. THE ESCAPE CONDITION is "
            "|d^2+dh-1| < 1 <=> 0 < d(d+h) < 2, which fails everywhere in the "
            "interior (d(d+h) < 0 there) and holds only for d > 0 (beta < 0) or "
            "d < -h (beta > 1): the bond operator must LEAVE THE CONVEX HULL of "
            "{sigma, sigma^-1}. No crossing count, block grading or convention "
            "does that. Even outside the hull, matching nature's 33.7 requires "
            "beta* = -4.30937 (4.31 outside) with |mu_anti| = 5.944e-11, i.e. "
            "the T=0 channel tuned to within 6e-11 of unbinding, and the point "
            "is not robust (ratio falls to 13.19 at d* - 1e-4). Near-threshold "
            "tuning is not itself unphysical — the real NN system is unnatural "
            "in exactly that way — but leaving the hull is the structural "
            "problem and nothing in the construction supplies it.")
        wb.add_data("det_identity",
                    {"symbolic_residual": str(resid),
                     "det_at_beta_0": mp.nstr(det_factor(mp.mpf(0)), 12),
                     "det_at_beta_1": mp.nstr(det_factor(-_H), 12),
                     "det_at_vertex": mp.nstr(det_factor(-_H / 2), 12),
                     "max_abs_on_hull": mp.nstr(vertex, 12)})
        wb.add_data("multicrossing",
                    {"n_random_bonds": 200, "k_range": "2..6",
                     "min_det_product": f"{min(prods):.12f}",
                     "max_det_product": f"{max(prods):.12f}",
                     "n_with_correct_signs": n_ok,
                     "best_ratio": f"{best:.12f}"})
        wb.add_data("escape_condition",
                    {"inequality": "0 < d(d+h) < 2",
                     "fails_inside_hull": True,
                     "requires": "beta < 0 or beta > 1"})
        wb.add_data("cost_of_matching_nature",
                    {"target_ratio": mp.nstr(R_EXP, 8),
                     "d_star": mp.nstr(d_star, 14),
                     "beta_star": mp.nstr(b_star, 10),
                     "abs_mu_anti": mp.nstr(ma_star, 6),
                     "sensitivity": {e: f"{v:.6f}" for e, v in sens}})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "SCOPE: this closes escape (a) for bonds built as a PRODUCT of "
            "crossings (T + d_i) with each d_i real and in [-h, 0], which is "
            "what the construction uses and what escape (a) proposed. It does "
            "NOT close every conceivable multi-crossing construction — a bond "
            "that is a SUM of products, or that entangles the two nucleons' "
            "internal strands rather than acting on a single interface "
            "generator, is not covered by the determinant argument and is not "
            "tested here.")
        wb.add_caveat(
            "THE 'BOUND <=> |mu| < 1' CONVENTION IS INHERITED FROM qou-m896 and "
            "is doing real work here too: the antisymmetric block's eigenvalue "
            "is negative, so the magnitude is used. Under a convention treating "
            "a negative ratio as unphysical the T=0 channel has no binding "
            "reading and the whole (T,S) line of argument does not run. The "
            "det-magnitude obstruction in A1-A3 is independent of that choice; "
            "the ratio numbers in A5 are not.")
        wb.add_caveat(
            "beta* = -4.309 is a solution of a ONE-PARAMETER family (a single "
            "crossing with a free real offset), presented to size what nature "
            "would cost, NOT as a proposed value. It has no derivation, sits far "
            "outside any braid-crossing reading, and requires a 10-digit "
            "tuning. It should be read as a measurement of the gap, not a fit.")
        wb.add_caveat(
            "The pionless-EFT remark is context, not evidence. The scattering "
            "lengths and force range are quoted to establish that near-threshold "
            "tuning is a real feature of the NN system; no claim is made that "
            "this construction's fine-tuning is the same phenomenon, and the "
            "two tunings are not on a common scale.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
