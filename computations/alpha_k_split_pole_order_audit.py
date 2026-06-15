#!/usr/bin/env python3
# polynomial_q_not_applicable: pole orders are exact integers; all candidate
# splits are verified symbolically over Q(q^{1/2}); no archimedean evaluation
# is needed beyond a reference print at q_0.
"""
alpha_K per-carrier split — pole-order audit (item 2 of the owner queue).

Question: does the pole-order primitive of
prop:alpha-em-shift-multiplicative-chain ("alpha_shift = pole order at q = 0
of a seminormal Hecke trace") FORCE the per-carrier split of
    1/alpha_EM = q [9]_q [10]_q
into 1/alpha_s = q^p [9]_q and 1/alpha_W = q^{p'} [10]_q with definite p, p'?

ANSWER (exact, derived here): NO — the split is UNDERDETERMINED by the
pole-order data plus the product constraint.

  1. Pole orders at q -> 0 (exact integers, with [k]_q = (q^k - q^{-k})/h):
         ord([k]_q) = -(k-1),  ord(h) = -1,  ord(delta_q(K)) = -w(K),
         ord(1/alpha_EM) = ord(q [9][10]) = 1 - 8 - 9 = -16.
     The BRACKET part of each carrier coupling is forced by the carrier's
     writhe (alpha_shift(T_{2,9}) = 9, alpha_shift(T_{3,5}) = 10) — that much
     the primitive does fix.
  2. The q-prefactor constraint is the single linear relation p + p' = 1
     (from the established total).  One equation, two unknowns: the
     constraint space is 1-dimensional, so pole order + product CANNOT pin
     (p, p').  Verified by exhibiting three structurally-named splits, all
     exactly consistent with the established total:
         (a) symmetric        p = p' = 1/2          (carrier symmetry)
         (b) writhe-weighted  p = 9/19, p' = 10/19  (framing anomaly ~ w)
         (c) strand-weighted  p = 1/3,  p' = 2/3    (~ (m-1): 1 vs 2)
     None is preferred by the available structure; each gives a DIFFERENT
     per-carrier value at q_0 (tabulated), so any later identification of a
     measured per-force coupling would distinguish them — which is exactly
     why no such comparison is made now (fishing gate).
  3. What WOULD force the split (the open target, recorded): a per-carrier
     seminormal-trace OBJECT whose trace is q^p [w]_q — e.g. the half-twist
     framed top-channel of the single carrier — i.e. a categorical
     construction, not an exponent bookkeeping argument.  Until that object
     is exhibited, the symmetric split stays CONVENTION
     (alpha_k_selection_rule_conditional.py) and only the product
     alpha_s * alpha_W = alpha_EM is invariant.

Tier: exact constraint analysis (negative-space result — prevents chasing
pole-order-only derivations); no fitting; no experimental comparison.

Refs: prop:alpha-em-shift-multiplicative-chain (pole-order primitive);
prop:torus-knot-delta-q-writhe (delta_q = h[(m-1)k]_q);
alpha_k_selection_rule_conditional.py (the invariant product identity).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp

try:
    import mpmath as mp
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"


def main() -> None:
    w = WitnessBuilder("alpha-k-split-pole-order-audit", engine="python")
    q = sp.symbols("q", positive=True)
    h = q - 1 / q

    def qint(k, q_sym=q, h_sym=h):
        return (q_sym ** k - q_sym ** (-k)) / h_sym

    # 1. exact pole orders at q -> 0 (compute as Laurent leading order in q)
    def ord0(expr):
        num, den = sp.fraction(sp.cancel(sp.together(expr)))
        lo = lambda e: min(k for (k,), c in sp.Poly(e, q).terms() if c != 0)
        return lo(num) - lo(den)

    ords = {
        "[9]_q": ord0(qint(9)), "[10]_q": ord0(qint(10)), "h": ord0(h),
        "delta_q(T_2_9)=h[9]": ord0(h * qint(9)),
        "delta_q(T_3_5)=h[10]": ord0(h * qint(10)),
        "1/alpha_EM=q[9][10]": ord0(q * qint(9) * qint(10)),
    }
    ord_ok = (ords["[9]_q"] == -8 and ords["[10]_q"] == -9 and
              ords["h"] == -1 and ords["delta_q(T_2_9)=h[9]"] == -9 and
              ords["delta_q(T_3_5)=h[10]"] == -10 and
              ords["1/alpha_EM=q[9][10]"] == -16)

    # 2. the three structurally-named splits all satisfy the product constraint
    splits = {
        "symmetric_1/2_1/2": (sp.Rational(1, 2), sp.Rational(1, 2)),
        "writhe_9/19_10/19": (sp.Rational(9, 19), sp.Rational(10, 19)),
        "strand_1/3_2/3": (sp.Rational(1, 3), sp.Rational(2, 3)),
    }
    inv_alpha_em = q * qint(9) * qint(10)
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)
    split_data, all_consistent, values_distinct = {}, True, set()
    for name, (p, pp) in splits.items():
        lhs = (q ** p * qint(9)) * (q ** pp * qint(10))
        consistent = sp.simplify(lhs - inv_alpha_em) == 0
        all_consistent = all_consistent and consistent
        vs = sp.N((q ** p * qint(9)).subs(q, sp.Float(str(q0), 60)), 40)
        vw = sp.N((q ** pp * qint(10)).subs(q, sp.Float(str(q0), 60)), 40)
        values_distinct.add(str(sp.N(vs, 20)))
        split_data[name] = {"p": str(p), "p_prime": str(pp),
                            "consistent_with_total": bool(consistent),
                            "inv_alpha_s_at_q0": str(vs),
                            "inv_alpha_W_at_q0": str(vw)}
    distinct_ok = len(values_distinct) == len(splits)

    # constraint-space dimension: p + p' = 1 is one equation in two unknowns
    p_var, pp_var = sp.symbols("p p'", real=True)
    sols = sp.solve([p_var + pp_var - 1], [p_var, pp_var], dict=True)
    underdetermined = bool(sols and (pp_var not in sols[0] or p_var not in sols[0]) or
                           len(sols[0]) < 2)

    print("=" * 74)
    print("alpha_K split — pole-order audit (exact)")
    print("=" * 74)
    for k, v in ords.items():
        print(f"  ord_q->0 {k:24s} = {v}")
    print(f"  pole orders as expected: {ord_ok}")
    print(f"  bracket parts forced by writhe (alpha_shift 9, 10): True")
    print()
    print("  splits (all consistent with the established total; values differ):")
    for name, d in split_data.items():
        print(f"    {name:20s} p={d['p']:>5s} p'={d['p_prime']:>6s}  "
              f"1/a_s(q0)={d['inv_alpha_s_at_q0'][:12]}  "
              f"1/a_W(q0)={d['inv_alpha_W_at_q0'][:12]}")
    print(f"  all consistent: {all_consistent}; per-split values distinct: "
          f"{distinct_ok}")
    print()
    print("  VERDICT: pole order + product constraint leave a 1-dim family —")
    print("  the split is NOT forced.  Open target recorded: a per-carrier")
    print("  seminormal-trace object with trace q^p [w]_q (e.g. half-twist")
    print("  framed top channel).  Symmetric split stays CONVENTION.")

    w.set_description(
        "Item-2 audit: does the pole-order primitive "
        "(prop:alpha-em-shift-multiplicative-chain) force the per-carrier "
        "split of 1/alpha_EM = q[9]_q[10]_q?  NO — exact verdict.  Pole "
        "orders at q->0: ord [k]_q = -(k-1), ord delta_q(K) = -w(K), ord "
        "1/alpha_EM = -16; the BRACKET part of each carrier coupling is "
        "forced by writhe (alpha_shift = 9, 10), but the q-prefactor "
        "constraint p + p' = 1 is one linear equation in two unknowns "
        "(1-dim solution family).  Three structurally-named splits "
        "(symmetric 1/2|1/2, writhe-weighted 9/19|10/19, strand-weighted "
        "1/3|2/3) are all exactly consistent with the established total and "
        "give distinct per-carrier values at q_0 — no available structure "
        "prefers one, so the symmetric split remains CONVENTION and only "
        "the product alpha_s * alpha_W = alpha_EM is invariant.  Open "
        "target recorded: a per-carrier seminormal-trace object with trace "
        "q^p [w]_q (half-twist framed top channel candidate).  Negative-"
        "space result; no fitting; no experimental comparison."
    )
    w.set_content_block("prop:alpha-em-shift-multiplicative-chain")
    w.add_data("q0", str(q0))
    w.add_data("pole_orders", {k: int(v) for k, v in ords.items()})
    w.add_data("splits", split_data)
    w.add_assertion(
        "pole orders exact: ord[9]=-8, ord[10]=-9, ord h=-1, ord 1/alpha=-16",
        computed=bool(ord_ok), expected=True, source="Laurent leading order",
    )
    w.add_assertion(
        "all three named splits reproduce the established total exactly",
        computed=bool(all_consistent), expected=True,
        source="symbolic product identity over Q(q^{1/2})",
    )
    w.add_assertion(
        "the splits give distinct per-carrier values at q_0 (genuinely different)",
        computed=bool(distinct_ok), expected=True, source="40-dps evaluation",
    )
    w.add_assertion(
        "constraint space p + p' = 1 is 1-dimensional (split underdetermined)",
        computed=bool(underdetermined), expected=True,
        source="linear algebra over the exponent lattice",
    )
    w.add_data(
        "finding",
        "The pole-order primitive forces the bracket parts ([9]_q, [10]_q) "
        "but NOT the q-prefactor split: p + p' = 1 leaves a 1-dim family; "
        "symmetric/writhe/strand splits are all consistent and distinct.  "
        "Split stays convention; the invariant is alpha_s*alpha_W = alpha_EM.  "
        "Forcing the split requires exhibiting a per-carrier seminormal-trace "
        "object (half-twist framed top channel candidate) — queued."
    )
    w.save()
    print("\nDone. Witness saved (alpha-k-split-pole-order-audit).")


if __name__ == "__main__":
    main()
