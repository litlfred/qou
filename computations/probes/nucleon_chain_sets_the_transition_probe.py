#!/usr/bin/env python3
"""What sets the two transition points: the crossing-branch content of a
three-letter middle — and `q_0` is inside the reachable range, not outside it.

WHERE THIS PICKS UP
-------------------
`binding_window_is_a_dual_vertex_hysteresis_probe.py` reduced binding to one
sentence: it is the split between the proton's and the neutron's dual-vertex
transition points, `h = 0.477185` and `h = 0.569840`, and `q_0` sits below both.
Those two numbers are the only contingent quantities left in the picture — they
are properties of `v_p` and `v_n`, not of `q`. This probe measures what sets
them.

THE CHAINS DECODE EXACTLY
---------------------------
`_hm_mp(nf, c, d, g, h)` right-multiplies by `(c . sigma_g + d)`, and in this
convention `T^2 = h T + 1` gives `T^-1 = T - h` (verified: `(sigma_0 - h)
sigma_0 = 1` exactly). So write

    sigma_g(beta)  :=  sigma_g - beta . h        beta = 0    ->  sigma_g
                                                 beta = 1/2  ->  (sigma_g + sigma_g^-1)/2
                                                 beta = 1    ->  sigma_g^-1

`beta` is exactly the **crossing-branch content**: 0 is a forward crossing, 1 an
inverse one, 1/2 the unoriented average. Then both nucleon chains are

    prefix (shared)   (sigma_0 sigma_1^-1)^3
    MIDDLE            sigma_0(b_0) . sigma_0(b_1) . sigma_1(b_2)
    suffix (shared)   sigma_0^2

with

    proton    b = (0,   1/2, 1/2)
    neutron   b = (1/2, 1/2, 1  )

reproducing `v_p` and `v_n` to a maximum difference of **exactly 0.0**. So

    proton -> neutron   is exactly   b += (1/2, 0, 1/2)

— two half-steps toward inverse content, one on the first `sigma_0` letter and
one on the `sigma_1` letter. That is the entire flavour split, and it is
entirely a statement about crossing branches. It also lines up with the corpus's
own reading that inverse crossings are the entanglement/"backwards" content: the
neutron carries a full `sigma_1^-1` where the proton carries the unoriented
average.

WHAT MOVES THE TRANSITION
---------------------------
Sensitivities of the transition `h*` to each letter:

                d h* / d b_0   d h* / d b_1   d h* / d b_2
    proton        -0.0525        -0.0498        **+0.4241**
    neutron       -0.0818        -0.0818        **+0.1543**

**`b_2`, the `sigma_1` letter, dominates**: it is the only positive
sensitivity, and the largest in magnitude at both — by 8.1x at the proton and
1.9x at the neutron.
Inverse content there pushes the transition up; the two `sigma_0` letters push
weakly the other way.

And `b_0, b_1` enter **symmetrically**, as they must: both multiply the same
generator, so `(sigma_0 - b_0 h)(sigma_0 - b_1 h)` is symmetric. Confirmed to
all printed digits — `(0.2, 1.0)` and `(1.0, 0.2)` both give `h* =
0.046510103635`, `(0.4, 0.8)` and `(0.8, 0.4)` both give `0.046498885007`. It is
*not* sum-only: equal sums with different products give different `h*`, exactly
as the elementary symmetric functions predict.

A THIRD, INDEPENDENT ROUTE TO THE SAME TWO NUMBERS
-----------------------------------------------------
Bisecting the margin `lam (Gv)_2 - (Gv)_0` in `h` gives

    proton   h* = 0.477184636796        neutron  h* = 0.569840290998

against `0.47718474189158` and `0.56984029056366` from the dual-support
bisection, which in turn matched the primal gap window. Three different
computations — primal gap, dual support, margin root — on the same two numbers.

`q_0` IS INSIDE THE REACHABLE RANGE
-------------------------------------
This is the part that changes the outlook. Sweeping the **physical** box
`beta in [0,1]^3` (forward through inverse, nothing exotic), the transition
ranges from about **0.046 to 0.649**, and

    h(q_0) = 0.209060299     lies INSIDE that range
    of 195 box points with a transition, 15 fall BELOW q_0 and 180 above

So a proton/neutron pair whose transitions **straddle** `q_0` is not forbidden
by anything structural — the reachable set comfortably contains it. What fails
is the specific assignment: the corpus's chains put *both* nucleons at 0.477 and
0.570, on the same side.

Along the `b_0 = b_1 = 1/2` line the transition is monotone in `b_2` and comes
down to `0.220405` at `b_2 = 0.1` — within 5 % of `h(q_0)` — before disappearing
entirely at `b_2 = 0`. The points that actually fall below `q_0` have `b_2 = 0`
with the two `sigma_0` letters carrying the inverse content instead.

**No `beta` values are proposed here.** Which crossing branches the nucleons
carry is a physical question the chains already answer; this probe measures the
consequence of that answer, and reports that the answer, not the framework, is
what puts binding at zero.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. Nothing in the corpus is modified — the
`beta` family is a re-parametrisation that reproduces the existing chains
exactly at `beta = (0,1/2,1/2)` and `(1/2,1/2,1)`. A correction against my own
first pass: it located transitions with a single-root bisection over
`h in [0.02, 3]`, which returns garbage where the margin has zero or two roots
(it reported `h* = 2.0009` for a chain that has no root in range at all). Every
transition here is found by scanning for sign changes first and bisecting only
inside a bracketed one.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] binding_window_is_a_dual_vertex_hysteresis_probe.py
-- Ref: [probe] nfold_ip_coupling_duality_gap_probe.py (the gap window)
"""
from __future__ import annotations

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
import numpy as np  # noqa: E402

from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 25
H_Q0 = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
# transitions from the dual-support bisection, previous probe
DUAL_P, DUAL_N = 0.47718474189158, 0.56984029056366

_CACHE: dict = {}


def base(hv: float):
    key = round(hv, 13)
    if key in _CACHE:
        return _CACHE[key]
    q = mp.mpf(hv) / 2 + mp.sqrt(mp.mpf(hv) ** 2 + 4) / 2
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    gram = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    cost = np.array([float(x) for x in
                     [mp.mpf(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]])
    _CACHE[key] = (gram, cost, h, cost[2] / gram[2, 2])
    return _CACHE[key]


def chain(betas, h):
    """(sigma_0 sigma_1^-1)^3 . sigma_0(b0) sigma_0(b1) sigma_1(b2) . sigma_0^2"""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for _ in range(3):
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
    for c, g in ((betas[0], 0), (betas[1], 0), (betas[2], 1)):
        nf = _hm_mp(nf, mp.mpf(1), -mp.mpf(c) * h, g, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    return np.array([float(x) for x in nf])


def original(kind: str, h):
    """The corpus's chain, verbatim, for the equivalence check."""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for _ in range(3):
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
    if kind == "p":
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h / 2, 1, h)
    else:
        nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    return np.array([float(x) for x in nf])


def margin(betas, hv: float) -> float:
    gram, _cost, h, lam = base(hv)
    gv = gram @ chain(betas, h)
    return lam * gv[2] - gv[0]


SCAN = [0.02 * (1.055 ** i) for i in range(80)]
SCAN = [x for x in SCAN if x < 1.3]


def brackets(betas):
    """Sign changes of the margin — scan FIRST, never assume a single root."""
    m = [margin(betas, hv) for hv in SCAN]
    return [(SCAN[i], SCAN[i + 1]) for i in range(len(SCAN) - 1)
            if m[i] * m[i + 1] < 0]


def transition(betas):
    br = brackets(betas)
    if not br:
        return None
    a, b = br[0]
    fa = margin(betas, a) > 0
    for _ in range(46):
        m = 0.5 * (a + b)
        if (margin(betas, m) > 0) == fa:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


def main() -> int:
    assertions = []
    print("t7qv — what sets the two transition points")
    _g, _t, h0, _l = base(H_Q0)

    # ── A1. the beta decoding is exact ────────────────────────────────
    print("\n  1. the chains decode as crossing-branch content")
    one = [mp.mpf(1)] + [mp.mpf(0)] * 5
    inv = _hm_mp(one, mp.mpf(1), -h0, 0, h0)
    prod = _hm_mp(inv, mp.mpf(1), mp.mpf(0), 0, h0)
    inv_ok = abs(prod[0] - 1) < 1e-25 and all(abs(x) < 1e-25 for x in prod[1:])
    dp = float(np.max(np.abs(chain(B_P, h0) - original("p", h0))))
    dn = float(np.max(np.abs(chain(B_N, h0) - original("n", h0))))
    ok = inv_ok and dp == 0.0 and dn == 0.0
    print(f"     T^-1 = T - h : (sigma_0 - h) sigma_0 = 1 -> {inv_ok}")
    print(f"     so beta = 0 / 1/2 / 1  is  forward / unoriented / inverse")
    print(f"     proton  b = {B_P}  reproduces v_p, maxdiff {dp:.1e}")
    print(f"     neutron b = {B_N}  reproduces v_n, maxdiff {dn:.1e}")
    assertions.append(("A1_beta_decoding_is_exact", ok,
                       f"T^-1 = T-h verified; chains reproduced, maxdiff "
                       f"{dp:.0e} and {dn:.0e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the flavour split is +(1/2, 0, 1/2) ───────────────────────
    print("\n  2. the entire flavour split")
    delta = tuple(round(n - p, 12) for p, n in zip(B_P, B_N))
    ok = delta == (0.5, 0.0, 0.5)
    print(f"     proton -> neutron  is  b += {delta}")
    print(f"     two half-steps toward INVERSE content: one on the first")
    print(f"     sigma_0 letter, one on the sigma_1 letter. Nothing else differs.")
    assertions.append(("A2_flavour_split_is_two_half_steps", ok,
                       f"b_n - b_p = {delta}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. beta_0, beta_1 enter symmetrically ────────────────────────
    print("\n  3. b_0 and b_1 act on the same generator, so they commute")
    pairs = [((0.2, 1.0), (1.0, 0.2)), ((0.4, 0.8), (0.8, 0.4))]
    sym_ok, vals = True, []
    for (a, b) in pairs:
        ta = transition((a[0], a[1], 0.0))
        tb = transition((b[0], b[1], 0.0))
        sym_ok &= (ta is not None and tb is not None and abs(ta - tb) < 1e-11)
        vals.append((a, ta, tb))
        print(f"     b = ({a[0]}, {a[1]}, 0.0) -> {ta:.12f}   "
              f"({b[0]}, {b[1]}, 0.0) -> {tb:.12f}")
    not_sum_only = abs(vals[0][1] - vals[1][1]) > 1e-9
    ok = sym_ok and not_sum_only
    print(f"     symmetric under b_0 <-> b_1: {sym_ok}")
    print(f"     but equal sums (1.2) give different h*: {not_sum_only} — so it")
    print(f"     depends on both elementary symmetric functions, not the sum")
    assertions.append(("A3_beta0_beta1_symmetric_not_sum_only", ok,
                       "swap-invariant to 1e-11; equal sums differ, as the "
                       "commuting product predicts"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. beta_2 dominates ──────────────────────────────────────────
    print("\n  4. the sigma_1 letter dominates the transition")
    sens = {}
    for nm, bb in (("proton", B_P), (
            "neutron", B_N)):
        t0 = transition(bb)
        row = []
        for i in range(3):
            pert = list(bb)
            pert[i] += 0.01
            tp = transition(tuple(pert))
            row.append((tp - t0) / 0.01 if tp is not None else float("nan"))
        sens[nm] = row
        print(f"     {nm:<8s} h* = {t0:.9f}   d h*/d b = "
              f"[{row[0]:+.4f}, {row[1]:+.4f}, {row[2]:+.4f}]")
    ratios = {k: abs(v[2]) / max(abs(v[0]), abs(v[1])) for k, v in sens.items()}
    only_pos = all(v[2] > 0 > max(v[0], v[1]) for v in sens.values())
    biggest = all(abs(v[2]) > max(abs(v[0]), abs(v[1])) for v in sens.values())
    ok = only_pos and biggest and ratios["proton"] > 3
    print(f"     b_2 is the only POSITIVE sensitivity: {only_pos}; and the")
    print(f"     largest in magnitude at both: {biggest}")
    print(f"     magnitude ratio to the larger of the other two: "
          f"proton {ratios['proton']:.1f}x, neutron {ratios['neutron']:.1f}x")
    assertions.append(("A4_beta2_dominates", ok,
                       f"b_2 uniquely positive and largest at both; ratio "
                       f"{ratios['proton']:.1f}x (proton), "
                       f"{ratios['neutron']:.1f}x (neutron)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. third independent route to the same two numbers ───────────
    print("\n  5. margin roots reproduce the dual-support transitions")
    tp, tn = transition(B_P), transition(B_N)
    ep, en = abs(tp - DUAL_P), abs(tn - DUAL_N)
    ok = ep < 1e-6 and en < 1e-6
    print(f"     margin root   proton {tp:.12f}   neutron {tn:.12f}")
    print(f"     dual support  proton {DUAL_P:.12f}   neutron {DUAL_N:.12f}")
    print(f"     agreement {ep:.1e} and {en:.1e} — a third computation, after")
    print(f"     the primal gap window and the dual support")
    assertions.append(("A5_third_route_agrees", ok,
                       f"margin roots match dual-support bisection to "
                       f"{ep:.0e}, {en:.0e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. q_0 is inside the reachable range ─────────────────────────
    print("\n  6. h(q_0) lies INSIDE the reachable range of the physical box")
    found, below = [], 0
    N = 5
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(N + 1):
                tr = transition((i / N, j / N, k / N))
                if tr is None:
                    continue
                found.append(tr)
                if tr < H_Q0:
                    below += 1
    lo, hi = min(found), max(found)
    inside = lo < H_Q0 < hi
    both_above = tp > H_Q0 and tn > H_Q0
    ok = bool(inside and below > 0 and both_above)
    print(f"     beta in [0,1]^3: {len(found)} points have a transition,")
    print(f"     spanning h* in [{lo:.6f}, {hi:.6f}]")
    print(f"     h(q_0) = {H_Q0:.9f} -> inside: {inside}; "
          f"{below} of {len(found)} fall below it")
    print(f"     the ACTUAL chains give {tp:.6f} and {tn:.6f} — both ABOVE")
    print(f"     so straddling q_0 is not structurally forbidden; the specific")
    print(f"     crossing-branch assignment is what puts both on one side")
    assertions.append(("A6_q0_inside_reachable_range", ok,
                       f"box transitions span [{lo:.4f}, {hi:.4f}]; "
                       f"{below}/{len(found)} below h(q_0); actual chains both "
                       f"above"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The two transition points are set by the crossing-branch content")
    print("  of a three-letter middle segment. In the beta parametrisation")
    print("  (0 forward, 1/2 unoriented, 1 inverse) the proton is (0, 1/2, 1/2)")
    print("  and the neutron (1/2, 1/2, 1) — exactly, maxdiff 0.0 — so the whole")
    print("  flavour split is b += (1/2, 0, 1/2), two half-steps toward inverse")
    print("  content. The sigma_1 letter dominates the transition, 8.1x at the")
    print("  proton and 1.9x at the neutron, and it is the only positive one;")
    print("  b_0 and b_1 enter symmetrically because they commute.")
    print("  And the outlook changes: over the physical box the transition")
    print("  spans roughly 0.046 to 0.649, so h(q_0) = 0.209 is INSIDE the")
    print("  reachable range, with 15 of 195 box points below it. A pair whose")
    print("  transitions straddle q_0 is not forbidden by anything structural.")
    print("  The corpus's own chains simply put both at 0.477 and 0.570.")
    print("  No beta values are proposed: which branches the nucleons carry is")
    print("  a physical question the chains already answer.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Measures what sets the two dual-vertex transition points that the "
            "binding window is the gap between. Writing sigma_g(beta) = "
            "sigma_g - beta*h (beta = 0 forward, 1/2 unoriented average, 1 "
            "inverse, since T^-1 = T - h in this convention), both nucleon "
            "chains are a shared prefix (sigma_0 sigma_1^-1)^3, a three-letter "
            "middle sigma_0(b0) sigma_0(b1) sigma_1(b2), and a shared suffix "
            "sigma_0^2, with proton b = (0, 1/2, 1/2) and neutron "
            "b = (1/2, 1/2, 1) reproducing v_p and v_n to maxdiff exactly 0.0. "
            "The whole flavour split is b += (1/2, 0, 1/2). The sigma_1 letter "
            "dominates the transition (d h*/d b_2 = +0.424 at the proton, 8x "
            "the other two); b_0 and b_1 enter symmetrically because they "
            "multiply the same generator, though not through their sum alone. "
            "Margin-root bisection reproduces the transitions 0.477184636796 "
            "and 0.569840290998, a third independent route after the primal "
            "gap window and the dual support. Over the physical box "
            "beta in [0,1]^3 the transition spans about 0.046 to 0.649, so "
            "h(q_0) = 0.209060299 is INSIDE the reachable range with 15 of 195 "
            "box points below it: a straddling pair is not structurally "
            "forbidden, and the corpus's specific assignment is what puts both "
            "nucleons above.")
        wb.add_data("beta_semantics", {"0": "sigma (forward)",
                                       "1/2": "(sigma + sigma^-1)/2",
                                       "1": "sigma^-1 (inverse)"})
        frac = {0.0: "0", 0.5: "1/2", 1.0: "1"}
        wb.add_data("betas", {"proton": [frac[x] for x in B_P],
                              "neutron": [frac[x] for x in B_N],
                              "split": [frac[x] for x in delta]})
        wb.add_data("sensitivities", {k: [f"{x:+.6f}" for x in v]
                                      for k, v in sens.items()})
        wb.add_data("transitions_margin_root",
                    {"proton": f"{tp:.12f}", "neutron": f"{tn:.12f}"})
        wb.add_data("transitions_dual_support",
                    {"proton": f"{DUAL_P:.12f}", "neutron": f"{DUAL_N:.12f}"})
        wb.add_data("box_range", {"lo": f"{lo:.6f}", "hi": f"{hi:.6f}",
                                  "points": len(found), "below_q0": below})
        wb.add_data("h_q0", f"{H_Q0:.12f}")
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "NO BETA VALUES ARE PROPOSED, and none should be read out of this. "
            "The parametrisation is a re-description that reproduces the "
            "existing chains exactly; the box sweep measures what the "
            "transition WOULD be at other crossing-branch assignments, in "
            "order to establish whether h(q_0) is reachable at all. Which "
            "branches the nucleons actually carry is a physical question the "
            "chains already answer, and choosing betas to place a transition "
            "at q_0 would be exactly the census-fitting this probe series "
            "documents elsewhere.")
        wb.add_caveat(
            "CORRECTION against my own first pass, which located transitions "
            "with a single-root bisection over h in [0.02, 3]. That returns "
            "garbage where the margin has zero or two roots — it reported "
            "h* = 2.0009 for a chain with no root in range at all. Every "
            "transition here scans for sign changes on a geometric grid first "
            "and bisects only inside a bracketed one. The proton and neutron "
            "each have a single crossing, so their values were never affected.")
        wb.add_caveat(
            "The box sweep is a 6x6x6 grid, so 'spans 0.046 to 0.649' and "
            "'15 of 195 below' are grid statistics, not certified extrema of "
            "the continuous family. They are sufficient for the claim actually "
            "made — that h(q_0) lies strictly between attainable transitions — "
            "since specific grid points fall on either side of it.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
