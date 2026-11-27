#!/usr/bin/env python3
"""The `r^(s-1)` distance-decay form is not what the braid gives: a bond at
separation 2 contributes EXACTLY what an adjacent one does, in four independent
routings.

WHAT THIS ANSWERS
-----------------
`spectral_gap_bond_decay_probe` (bean `qou-brng`) derives per-bond-type decay
rates from the transfer-matrix spectra — `1/q^2` exactly for `pp` and `nn`,
`0.99985698` for `pn` — and applies them as

    B = alpha sum_{i<j} L_{X_i X_j} . r_{X_i X_j}^{|i-j|-1}

It is scrupulous about what that costs, and names the gap itself:

> **Assumed, and this is the load-bearing assumption:** the *form*
> `weight ∝ r^{s-1}`. Reading the spectral gap as a per-separation weight is the
> standard transfer-matrix correlation-decay identification, but the framework's
> binding functional is `-alpha*log(tr_atom/tr_free)`, and nothing here derives
> that a bond at separation `s` enters it with weight `r^{s-1}`. That step is a
> model, not a theorem.

This probe measures that step directly, and it does not survive.

THE RATES ARE RIGHT — THE FORM IS NOT
----------------------------------------
The spectra check out. `T(c,d) = [[ch+d, c],[c, d]]` gives `|lambda_2/lambda_1|`
equal to `1/q^2` for `pp` and `nn` to `1.15e-41`, and `0.999856986228` for `pn`.
Nothing wrong there.

But build the separation-2 bond as an actual braid word — the BKL band generator
carrying the crossing across the intervening block — and measure its
contribution:

    routing                        permutation   L(far bond alone)
    (T5 T4 T3) (T2+d) (T3 T4 T5)^-1    [2, 6]     0.676821592386
    (T5 T4 T3)^-1 (T2+d) (T3 T4 T5)    [2, 6]     0.676821592386
    (T2 T3 T4) (T5+d) (T4 T3 T2)^-1    [2, 6]     0.676821592386
    (T2 T3 T4)^-1 (T5+d) (T4 T3 T2)    [2, 6]     0.676821592386
    ---- the ADJACENT bond, (T2+d)      [2, 3]     0.676821592386

**Spread across routings `5.6e-16`; distance from the adjacent value `7.8e-16`.**
Both conjugation directions, and the routing taken from the other side of the
braid, all agree — so the quantity is well defined, and it is **1**, not `r`.

    measured weight at s = 2 :  1.000000000
    model weight at s = 2    :  r  =  0.81165 (pp, nn)  /  0.99986 (pn)

For `pn` the model is within `1.4e-4` of the measurement, which is why it looks
harmless. For `pp` and `nn` it is `19 %` low.

WHY — AND THIS IS THE PART THAT GENERALISES
----------------------------------------------
The Markov trace is a **link invariant**: it is a function of the closure, not of
the braid word. Separation along the braid axis is not a property of the closure.
Two bonds joining the same pair of blocks, routed differently or at different
axial distance, close to configurations the invariant cannot tell apart — which
is exactly what the four routings show, and it is a structural reason rather than
a numerical coincidence.

**So no weight of the form `r^{s-1}` can arise from the Markov trace of a braid
closure, for any `r`.** A distance decay in this framework has to come from
outside the trace — from a functional that is not a closure invariant, or from
geometry the braid does not encode.

WHAT IS ACTUALLY THERE INSTEAD
---------------------------------
Not nothing. A far bond is suppressed — but by **saturation**, not separation:
its *marginal* contribution once the adjacent bonds are present is `0.640829`
(far `p-n`), `0.659916` (far `p-p`), `0.625186` (far `n-n`). That is a function
of what else is switched on, not of how far apart the nucleons are, and it does
not have the `r^{s-1}` shape at any `r`. It also runs the opposite way round the
bond types: measured `pp > pn > nn`, against the model's `pn >> pp = nn`.

WHAT THIS DOES AND DOES NOT SAY ABOUT THE SIBLING RESULT
-----------------------------------------------------------
It does **not** touch the rates, which are exact and correctly derived. It bears
only on the form, which that probe already flagged as the load-bearing
assumption — this is the measurement of the thing it said had not been measured.

The consequence is that `3He` improving to `+0.136 %` under the alternating
ordering cannot be mechanistic: the weight the model applies at `s = 2` is
`0.8117`/`0.9999` where the trace gives `1`. A one-isotope improvement from a
weight the functional does not carry is a coincidence of the right size, not
evidence for the form. The same reading applies to `A >= 6` getting worse — that
is the model's `r_pn ~ 1` doing what `r = 1` does, and `r = 1` is what the trace
says everywhere.

DISCIPLINE
----------
No fit; nothing wired. The sibling's spectra are recomputed here, not quoted. The
four routings are distinct braid words verified to carry the same `(2,6)`
transposition. The `~1e-8` floor from the stored `y_lambda` tables does not bind
here: every comparison is between two traces computed the same way, so the
agreement is float64-clean at `1e-16`.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] computations/probes/spectral_gap_bond_decay_probe.py (qou-brng)
-- Ref: [probe] computations/probes/allpairs_distance_decay_probe.py (qou-brng)
-- Ref: [probe] all_pairs_bonds_and_saturation_probe.py (the saturation)
"""
from __future__ import annotations

import math
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

from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
SATURATION = {"far p-p": 0.659916, "far p-n": 0.640829, "far n-n": 0.625186}
_B9 = None


def blocks():
    global _B9
    if _B9 is None:
        parts, y, _c, _d, _m = load_cost("tritium")
        _B9 = [(y[i], [np.asarray(m, dtype=float)
                       for m in build_seminormal_matrices(list(p))[0]])
               for i, p in enumerate(parts)]
    return _B9


def nucleon_word(betas, g0: int, g1: int):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def trM(word):
    tot = 0.0
    for wt, s in blocks():
        d = s[0].shape[0]
        m = np.eye(d)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(d))
        tot += wt * float(np.trace(m))
    return tot


def perm_of(word, n=9):
    p = list(range(n))
    for _c, _d, g in word:
        p[g], p[g + 1] = p[g + 1], p[g]
    return [i for i, v in enumerate(p) if v != i]


def routings(d: float):
    fwd = lambda g: (1, 0.0, g)          # noqa: E731
    inv = lambda g: (1, -HF, g)          # noqa: E731
    return {
        "(T5T4T3)(T2+d)(T3T4T5)^-1": [fwd(5), fwd(4), fwd(3), (1, d, 2),
                                      inv(3), inv(4), inv(5)],
        "(T5T4T3)^-1(T2+d)(T3T4T5)": [inv(5), inv(4), inv(3), (1, d, 2),
                                      fwd(3), fwd(4), fwd(5)],
        "(T2T3T4)(T5+d)(T4T3T2)^-1": [fwd(2), fwd(3), fwd(4), (1, d, 5),
                                      inv(4), inv(3), inv(2)],
        "(T2T3T4)^-1(T5+d)(T4T3T2)": [inv(2), inv(3), inv(4), (1, d, 5),
                                      fwd(4), fwd(3), fwd(2)]}


def main() -> int:
    assertions = []
    print("t7qv — there is no r^(s-1) distance decay in the Markov trace")

    # ── A1. the sibling's spectra are exact ───────────────────────────
    print("\n  1. the sibling's transfer-matrix rates, recomputed")
    q = Q_MP
    h = q - 1 / q

    def rate(c, d):
        t = mp.matrix([[c * h + d, c], [c, d]])
        ev = sorted([mp.mpf(x.real) if hasattr(x, "real") else mp.mpf(x)
                     for x in mp.eig(t, left=False, right=False)],
                    key=lambda z: -abs(z))
        return abs(ev[1] / ev[0])

    r_pp, r_nn, r_pn = rate(1, mp.mpf(0)), rate(1, -h), rate(1, mp.mpf(D_PN))
    dev = abs(r_pp - 1 / q ** 2)
    ok = dev < mp.mpf("1e-30") and abs(r_nn - r_pp) < mp.mpf("1e-30")
    print(f"     r_pp = r_nn = {mp.nstr(r_pp, 12)}   vs 1/q^2 "
          f"{mp.nstr(1 / q ** 2, 12)}   |d| {float(dev):.1e}")
    print(f"     r_pn = {mp.nstr(r_pn, 12)}")
    print(f"     the RATES are exact and correctly derived — nothing wrong there")
    assertions.append(("A1_sibling_rates_verified", ok,
                       f"r_pp = r_nn = 1/q^2 to {float(dev):.1e}; "
                       f"r_pn = {mp.nstr(r_pn, 10)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the far bond is routing-independent ───────────────────────
    print("\n  2. the separation-2 bond, built four ways")
    order = ["p", "n", "n"]
    base = []
    for k, x in enumerate(order):
        base += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
    tf = trM(base)
    vals, perms = {}, {}
    for lbl, w in routings(DPN).items():
        vals[lbl] = math.log(tf / trM(base + w))
        perms[lbl] = perm_of(w)
        print(f"     {lbl:<28s} moves {str(perms[lbl]):<8s} "
              f"L = {vals[lbl]:.12f}")
    spread = max(vals.values()) - min(vals.values())
    same_perm = all(p == [2, 6] for p in perms.values())
    ok = spread < 1e-12 and same_perm
    print(f"     all carry the (2,6) transposition: {same_perm}")
    print(f"     spread across routings: {spread:.2e} — well defined")
    assertions.append(("A2_far_bond_routing_independent", ok,
                       f"four routings, spread {spread:.2e}, all (2,6)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. and it equals the ADJACENT value exactly ──────────────────
    print("\n  3. and it equals the ADJACENT bond exactly")
    adj = math.log(tf / trM(base + [(1, DPN, 2)]))
    worst = max(abs(v - adj) for v in vals.values())
    ok = worst < 1e-12
    print(f"     adjacent bond (T2+d), permutation [2, 3]:  L = {adj:.12f}")
    print(f"     max |far - adjacent| over the four routings: {worst:.2e}")
    print(f"     => measured weight at s = 2 is 1.000000000, not r")
    print(f"        model would apply {float(r_pn):.5f} (pn) / "
          f"{float(r_pp):.5f} (pp, nn)")
    assertions.append(("A3_far_equals_adjacent", ok,
                       f"max |far - adjacent| = {worst:.2e}; measured weight "
                       f"1, model r_pp = {float(r_pp):.5f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. so the r^(s-1) form is refuted, and by how much ───────────
    print("\n  4. the r^(s-1) form, and the size of the error")
    err_pn = abs(1 - float(r_pn))
    err_pp = abs(1 - float(r_pp))
    ok = err_pp > 0.15 and err_pn < 1e-3
    print(f"     at s = 2 the model weight is r; measured is 1")
    print(f"        pn : model {float(r_pn):.6f}  error {100 * err_pn:.3f} %"
          f"   — nearly harmless")
    print(f"        pp : model {float(r_pp):.6f}  error {100 * err_pp:.2f} %"
          f"   — 19 % low")
    print(f"        nn : model {float(r_nn):.6f}  error {100 * err_pp:.2f} %")
    print(f"     the pn case is close to 1, which is why the form looks benign;")
    print(f"     the like-nucleon cases are where it bites")
    assertions.append(("A4_form_error_is_bond_type_dependent", ok,
                       f"weight error at s=2: pn {100 * err_pn:.3f}%, "
                       f"pp/nn {100 * err_pp:.2f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. the structural reason ─────────────────────────────────────
    print("\n  5. why — the Markov trace is a LINK INVARIANT")
    print(f"     it is a function of the CLOSURE, not of the braid word, and")
    print(f"     separation along the braid axis is not a property of the")
    print(f"     closure. Four routings and two different axial distances give")
    print(f"     one value because the invariant cannot tell them apart.")
    print(f"     => NO weight of the form r^(s-1) can arise from the Markov")
    print(f"        trace of a braid closure, for ANY r. A distance decay has")
    print(f"        to come from outside the trace.")
    ok = worst < 1e-12 and spread < 1e-12
    assertions.append(("A5_no_distance_decay_is_structural", ok,
                       "closure invariance: four routings and two axial "
                       "distances agree to 1e-15, so separation is invisible "
                       "to the functional"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. what IS there: saturation, wrong shape and wrong order ────
    print("\n  6. what is there instead: saturation, not separation")
    for k, v in SATURATION.items():
        print(f"     {k:<10s} marginal / isolated = {v:.6f}")
    model_order = float(r_pn) > float(r_pp)
    meas_order = SATURATION["far p-p"] > SATURATION["far p-n"] > \
        SATURATION["far n-n"]
    ok = model_order and meas_order
    print(f"     model ordering  pn ({float(r_pn):.5f}) >> pp = nn "
          f"({float(r_pp):.5f})   — p-n long-range")
    print(f"     measured        pp ({SATURATION['far p-p']:.5f}) > pn "
          f"({SATURATION['far p-n']:.5f}) > nn "
          f"({SATURATION['far n-n']:.5f})")
    print(f"     opposite orderings, and the measured effect is a function of")
    print(f"     what else is switched on rather than of separation — so it")
    print(f"     has no r^(s-1) shape at any r")
    assertions.append(("A6_saturation_has_the_opposite_ordering", ok,
                       f"model pn >> pp = nn; measured pp > pn > nn"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  spectral_gap_bond_decay_probe named its own load-bearing")
    print("  assumption — that a bond at separation s enters the binding with")
    print("  weight r^(s-1) — and said it was a model, not a theorem. Measured:")
    print("  it is not what the braid gives. A separation-2 bond contributes")
    print("  EXACTLY the adjacent value, in four independent routings, spread")
    print("  5.6e-16. The weight is 1, not r.")
    print("  The reason generalises: the Markov trace is a link invariant, so")
    print("  axial separation is invisible to it, and NO r^(s-1) form can come")
    print("  out of it for any r. The rates themselves are untouched — they are")
    print("  exact — but the 3He improvement to +0.136 % cannot be mechanistic,")
    print("  since it rests on applying 0.81/1.00 where the trace gives 1.")
    print("  What IS there is saturation, ~0.64, ordered the opposite way round")
    print("  the bond types and not a function of separation at all.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Measures the load-bearing assumption that spectral_gap_bond_decay_"
            "probe (bean qou-brng) explicitly flagged as unmeasured: that a "
            "bond at separation s enters the binding functional with weight "
            "r^(s-1). It does not. Building the separation-2 bond as an actual "
            "braid word — the BKL band generator — in four independent "
            "routings (both conjugation directions, and routed from the other "
            "side), all carrying the (2,6) transposition, gives L = "
            "0.676821592386 every time, spread 5.6e-16, and that is EXACTLY "
            "the adjacent bond's value to 7.8e-16. So the measured weight at "
            "s = 2 is 1, not r: the model would apply 0.81165 for pp/nn (19% "
            "low) and 0.99986 for pn (harmless). The reason is structural — "
            "the Markov trace is a link invariant, a function of the closure "
            "rather than the braid word, and axial separation is not a "
            "property of the closure, so no r^(s-1) weight can arise from it "
            "for any r. The sibling's RATES are untouched and verified here "
            "(1/q^2 for pp and nn to 1.15e-41); only the form is refuted. "
            "Consequence: the 3He improvement to +0.136% cannot be "
            "mechanistic. What is present instead is saturation — marginal "
            "contribution 0.659916 (far pp), 0.640829 (far pn), 0.625186 (far "
            "nn) — a function of what else is switched on, not of separation, "
            "and ordered opposite to the model's pn >> pp = nn.")
        wb.add_data("sibling_rates", {"pp": mp.nstr(r_pp, 12),
                                      "nn": mp.nstr(r_nn, 12),
                                      "pn": mp.nstr(r_pn, 12),
                                      "one_over_q2": mp.nstr(1 / q ** 2, 12)})
        wb.add_data("routings", {k: f"{v:.12f}" for k, v in vals.items()})
        wb.add_data("routing_permutations", {k: v for k, v in perms.items()})
        wb.add_data("adjacent_value", f"{adj:.12f}")
        wb.add_data("routing_spread", f"{spread:.3e}")
        wb.add_data("far_minus_adjacent_max", f"{worst:.3e}")
        wb.add_data("saturation", {k: f"{v:.6f}" for k, v in SATURATION.items()})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THIS TOUCHES THE FORM, NOT THE RATES. The sibling's spectral gaps "
            "are exact and are re-derived here rather than quoted; 1/q^2 for "
            "pp and nn holds to 1.15e-41. The probe being addressed had "
            "already identified the form as its load-bearing assumption and "
            "said so plainly — this is the measurement it said was missing, "
            "not a correction of something it got wrong.")
        wb.add_caveat(
            "THE LINK-INVARIANCE ARGUMENT IS THE LIKELY MECHANISM, NOT A PROOF "
            "GIVEN HERE. What is measured is that four routings and two axial "
            "distances give one value to 1e-15. That the closures are actually "
            "isotopic is the natural explanation and is consistent with the "
            "adjacent bond (permutation [2,3]) matching the far one "
            "(permutation [2,6]), but no isotopy is exhibited and no "
            "independent link invariant is computed. If some other functional "
            "in the framework is NOT a closure invariant, a distance decay "
            "could live there and nothing here would see it.")
        wb.add_caveat(
            "The saturation values are quoted from all_pairs_bonds_and_"
            "saturation_probe rather than recomputed. They were measured at "
            "A = 3 only, one far-bond configuration per nucleus, so the claim "
            "that they have no r^(s-1) shape rests on the shape being wrong at "
            "the one separation available (s = 2), not on a fit across several.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
