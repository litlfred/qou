#!/usr/bin/env python3
"""What replaces `tr_M(1) = 1` under convention D: NOTHING. It is a
normalisation, not a convention-dependent value — and that CLOSES the natural
repair of the D-frame ladder phase.

Follow-up to `qbeta_d_frame_ladder_bar_weight_prune.py` (bean `qou-cds1`,
Step 2), which left exactly one thing open:

    "What replaces tr_M(1) = 1 in the D normalisation is OPEN, and not settled
     here."

## The measurement

`tr_M(1) = Sum_lambda y_lambda . f^lambda`, with `f^lambda` the ordinary
S_n dimension. Evaluated on the convention-D Wenzl weights that
`markov_trace_weights_wenzl.py` solves for in EXACT rational arithmetic:

    s = 3/2, 7/5, 13/9   x   n = 2, 3, 4, 5      ->   == 1 EXACTLY, all twelve

Note this holds even though the ell(lambda) >= 3 weights all VANISH under D:
the surviving two-row blocks carry the whole normalisation on their own.

## What that is, and what it is NOT

It is **not** an independent derivation that `tr_M(1)` must be 1 under D.
`markov_trace_s` seeds the recursion with `tr = {1: {(0,): Fraction(1)}}` — the
normalisation is IMPOSED at the base. What the twelve exact hits establish is
that the D Wedderburn solve REPRODUCES it: the imposed normalisation and the
D-frame block weights are consistent, and the vanishing of the ell >= 3 blocks
does not break it.

So the honest answer to the open question is: **nothing replaces it.** It is a
normalisation carried unchanged across the convention, not a quantity the
convention determines.

## Why that matters — the natural repair is CLOSED

Step 2 showed the D ladder phase `alpha = (z - 1)h/2` is not a bar-eigenvector,
that the obstruction is the affine offset rather than `z`, and that
bar-homogeneity FORCES the offset to carry bar-weight -4 (uniquely `q^2` among
monomials). The obvious hope was that the D normalisation would supply
something of weight -4 in place of the `1`.

It does not. `tr_M(1) = 1` has bar-weight 0 in BOTH conventions. So IF the
phase's offset is the trace normalisation, the required weight -4 is
unavailable and **no offset-reinterpretation can make the D phase
bar-homogeneous.** The most natural repair route is closed, and the D ladder
must be rebuilt on a principle other than bar-homogeneity of this phase.

## THE LINK IS FALSE — settled 2026-08-30, same session

The paragraph above flagged the `tr_M(1)` reading as unproved and said settling
it would decide the path. It is now settled, and it goes the OTHER way.

`folio/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md`
line 21 states it outright:

    alpha = (z-1)h/2 is the single-wrap EIGENPHASE on V_(2,1)
    (per conj:q-beta-spectral-bridge)

So the `1` is an artifact of an eigenphase computation on the 2-dimensional
Wedderburn block, **not** the trace normalisation. The weight-0 argument does
not bind it, and **the conclusion "the offset repair is CLOSED" DOES NOT
FOLLOW.** That conclusion is retracted here; the offset question is REOPENED.

What survives, unaffected: the measurement itself. `tr_M(1) = 1` is preserved
exactly under D at all 12 rows, it is imposed rather than derived, and nothing
replaces it. That answers the question Step 2 asked. It simply does not have
the consequence Step 2's framing expected, because Step 2 mis-identified which
`1` was in the phase.

## The sharpened next step

Structure visible from `beta-decay-transfer-matrix-proof.md`: the phase factors
as `(z - 1) * (h/2)`, and the `h/2` is the beta-decay transfer-matrix shift
`Delta_beta = (h/2) . I`, which is built from `h` alone — **z-free, hence
convention-independent.** The entire convention dependence of the phase sits in
the `(z - 1)` factor.

So the D-frame ladder phase is obtained by re-deriving the single-wrap
eigenphase on V_(2,1) under the D trace, from conj:q-beta-spectral-bridge —
NOT by substituting z_D, and NOT by adjusting the offset to weight -4. That is
the concrete open item, and it is narrower than "re-derive the ladder".

Consistent with the corpus already treating this as unresolved:
`qbeta_utils.py` WITHHOLDS `z` and `alpha` under convention D behind a guard
citing the proved invalidity of substituting `z_D` into this phase.

No `c_k` value is proposed, extracted, or wired.

Run:  python3 -u computations/qbeta/qbeta_trm_identity_normalisation_under_d.py
"""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

WENZL_WITNESS = COMP / "markov-trace-weights-wenzl.witness.json"


def s_n_dimension(lam: tuple[int, ...]) -> int:
    """Ordinary S_n irrep dimension by the hook-length formula."""
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(max(lam))]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j) + (conj[j] - i) - 1
    return math.factorial(n) // prod


def symbolic_h3_weights():
    """Solve the H_3 Wedderburn weights with z FREE, then specialise.

    Upgrades the sampled measurement below to an IDENTITY in q, and answers a
    question the sampled form cannot: does the ladder's carrier block survive
    convention D, or is it in the radical?
    """
    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    # characters on (1, sigma, sigma_1 sigma_2); Hecke eigenvalues q and -1/q
    sol = sp.solve(
        [y3 + 2 * y21 + y111 - 1,
         y3 * q + y21 * h + y111 * (-1 / q) - z,
         y3 * q**2 + y21 * (-1) + y111 * (1 / q**2) - z**2],
        [y3, y21, y111], dict=True)[0]
    z_D = q**3 / (q**2 + 1)
    wD = {k: sp.simplify(sp.factor(sol[v].subs(z, z_D)))
          for k, v in (("(3)", y3), ("(2,1)", y21), ("(1^3)", y111))}
    total = sp.simplify(wD["(3)"] + 2 * wD["(2,1)"] + wD["(1^3)"])
    num, _ = sp.fraction(sp.together(wD["(2,1)"]))
    roots = sp.real_roots(sp.Poly(sp.expand(num), q))
    return {
        "y_(3)": str(wD["(3)"]),
        "y_(2,1)": str(wD["(2,1)"]),
        "y_(1^3)": str(wD["(1^3)"]),
        "radical_is_identically_zero": bool(sp.simplify(wD["(1^3)"]) == 0),
        "sum_y_f_symbolic": str(total),
        "sum_equals_one_for_all_q": bool(total == 1),
        "carrier_numerator": str(sp.factor(num)),
        "carrier_real_roots": [str(r) for r in roots],
        "carrier_nonzero_for_q_positive": all(sp.N(r) <= 0 for r in roots),
    }


def main() -> int:
    data = json.loads(WENZL_WITNESS.read_text())["results"]
    sym = symbolic_h3_weights()

    rows, all_one = [], True
    for s, blk in data.items():
        totals: dict[int, Fraction] = {}
        vanished: dict[int, int] = {}
        for lam_s, v in blk["per_lambda"].items():
            lam = tuple(int(x) for x in
                        lam_s.strip("()").replace(" ", "").rstrip(",").split(","))
            n = sum(lam)
            w = Fraction(str(v["weight"]))
            totals[n] = totals.get(n, Fraction(0)) + w * s_n_dimension(lam)
            if w == 0:
                vanished[n] = vanished.get(n, 0) + 1
        for n in sorted(totals):
            ok = totals[n] == 1
            all_one = all_one and ok
            rows.append({"s": s, "n": n, "sum_y_f": str(totals[n]),
                         "equals_one_exactly": ok,
                         "vanishing_blocks": vanished.get(n, 0)})

    # bar weights, exact in q
    q = sp.Symbol("q", positive=True)
    bar = lambda e: sp.simplify(sp.together(e.subs(q, 1 / q)))  # noqa: E731
    one_weight = sp.simplify(bar(sp.Integer(1)) / sp.Integer(1))
    z_D = q**3 / (q**2 + 1)
    z_weight = sp.simplify(bar(z_D) / z_D)

    q0 = q_at(40)
    payload = {
        "description": (
            "tr_M(1) = 1 is a normalisation, not a convention-dependent value: "
            "it is imposed at the base of the Markov recursion and reproduced "
            "exactly by the convention-D Wedderburn solve. Nothing replaces it, "
            "which closes the offset-reinterpretation repair of the D ladder "
            "phase."
        ),
        "measurement": {
            "quantity": "tr_M(1) = sum_lambda y_lambda * f^lambda",
            "source_weights": "computations/markov-trace-weights-wenzl.witness.json (convention D, exact rationals)",
            "rows": rows,
            "all_equal_one": all_one,
            "note": ("holds even though every ell(lambda) >= 3 block vanishes "
                     "under D — the two-row blocks carry the normalisation alone"),
        },
        "symbolic_h3_under_D": sym,
        "is_it_derived": {
            "answer": "NO — imposed, then reproduced",
            "where_imposed": "markov_trace_s seeds tr = {1: {(0,): Fraction(1)}}",
            "what_the_twelve_hits_establish": (
                "that the imposed normalisation and the D-frame block weights "
                "are CONSISTENT, and that the vanishing ell >= 3 blocks do not "
                "break it — not that tr_M(1) must be 1 under D"
            ),
        },
        "consequence_for_the_ladder": {
            "step2_requirement": "offset must carry bar-weight -4 for alpha to be bar-homogeneous under D",
            "bar_weight_of_1": str(one_weight),
            "bar_weight_of_z_D": str(z_weight),
            "verdict": (
                "RETRACTED. The antecedent is false: the phase offset is NOT "
                "the trace normalisation but a single-wrap eigenphase artifact "
                "on V_(2,1). The weight-0 argument does not bind it. See "
                "link_settled_and_FALSE."
            ),
        },
        "link_settled_and_FALSE": (
            "the `1` is NOT tr_M(1). q-beta-categorical-precision-ladder.md:21 "
            "states alpha = (z-1)h/2 is the single-wrap EIGENPHASE on V_(2,1) "
            "(conj:q-beta-spectral-bridge). So the weight-0 argument does not "
            "bind it and the 'offset repair is CLOSED' verdict is RETRACTED; "
            "the offset question is REOPENED. The tr_M(1) = 1 measurement is "
            "unaffected — it simply lacks the consequence Step 2 expected."
        ),
        "sharpened_next_step": (
            "the phase factors as (z-1)*(h/2), and h/2 is Delta_beta = (h/2).I "
            "from beta-decay-transfer-matrix-proof.md — built from h alone, so "
            "z-free and convention-INDEPENDENT. All convention dependence sits "
            "in (z-1). The D phase therefore comes from re-deriving the "
            "single-wrap eigenphase on V_(2,1) under the D trace, not from "
            "substituting z_D and not from a weight -4 offset."
        ),
        "context": {
            "beans": ["qou-cds1"],
            "step2": "computations/qbeta/qbeta_d_frame_ladder_bar_weight_prune.py",
            "corpus_agrees_unresolved": (
                "qbeta_utils.py withholds z and alpha under convention D behind "
                "a guard citing the proved invalidity of substituting z_D here"
            ),
            "scope": "(a) exact measurement at 3 s-values x 4 n; (b) the weight algebra is an identity in q",
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    # bean qou-srvu. Every claim below is EXACT -- Fraction arithmetic for the
    # sampled rows, sympy over Q(q) for the symbolic ones -- and each was
    # computed, printed and left in `data`, so `save()` emitted
    # `allPassed: true` over an EMPTY assertions list. Nothing here is
    # tolerance-based, so no threshold is introduced and no float64 floor is
    # involved: `all_one` is `== 1` over exact rationals, not an approximate
    # comparison, and `radical_is_identically_zero` is an identity in q.
    #
    # NOTE ON SCOPE, kept deliberately: the payload's own `is_it_derived` says
    # "NO -- imposed, then reproduced". These assertions therefore certify
    # CONSISTENCY between the imposed normalisation and the D-frame weights;
    # they do not assert that tr_M(1) must be 1 under D. The source strings
    # below say so, so the scope travels with the assertion.
    _b = WitnessBuilder.wrap_legacy(
        "qbeta-trm-identity-normalisation-under-d", payload,
        script_path=__file__, engine="python+sympy+exact rationals",
    )
    _b.add_assertion(
        "sum_y_lambda_f_lambda_equals_one_exactly",
        computed=bool(all_one), expected=True,
        source=("sum_lambda y_lambda * f^lambda == 1 EXACTLY (Fraction "
                "arithmetic, not a tolerance) on every sampled row, even "
                "though every ell(lambda) >= 3 block vanishes under D. "
                "CONSISTENCY of an imposed normalisation with the D-frame "
                "weights -- not a derivation of it"))
    _b.add_assertion(
        "radical_is_identically_zero",
        computed=bool(sym["radical_is_identically_zero"]), expected=True,
        source=("y_(1^3) == 0 as an IDENTITY in q under convention D -- "
                "sympy over Q(q) with z free, then specialised at "
                "z_D = q^3/(q^2+1)"))
    _b.add_assertion(
        "sum_equals_one_for_all_q",
        computed=bool(sym["sum_equals_one_for_all_q"]), expected=True,
        source=("the symbolic upgrade of the sampled measurement: the sum is "
                "1 for ALL q, not merely at the sampled points"))
    _b.add_assertion(
        "carrier_nonzero_for_q_positive",
        computed=bool(sym["carrier_nonzero_for_q_positive"]), expected=True,
        source=("every real root of the y_(2,1) carrier numerator is <= 0, so "
                "the ladder's carrier block survives convention D for q > 0 "
                "rather than falling into the radical"))
    out = _b.save()

    print("=== What replaces tr_M(1) = 1 under convention D? NOTHING ===")
    print(f"  sum_lambda y_lambda f^lambda == 1 exactly, all rows : {all_one}")
    print(f"    ({len(rows)} rows: 3 s-values x n = 2..5, exact rationals)")
    print(f"  derived, or imposed?                                : IMPOSED at the")
    print(f"    recursion base, then REPRODUCED by the D solve — a consistency")
    print(f"    check, not a derivation")
    print(f"  bar-weight of the offset 1                          : {one_weight}  (weight 0)")
    print(f"  bar-weight of z_D                                   : {z_weight} (weight -4)")
    print(f"  => Step 2 expected weight -4 to close the offset repair. RETRACTED:")
    print(f"     the `1` is NOT tr_M(1). It is the single-wrap EIGENPHASE on")
    print(f"     V_(2,1) (q-beta-categorical-precision-ladder.md:21,")
    print(f"     conj:q-beta-spectral-bridge), so the weight-0 argument does not")
    print(f"     bind it. The offset question is REOPENED.")
    print(f"\n  What survives: the measurement. tr_M(1) = 1 is preserved under D,")
    print(f"  imposed not derived, and nothing replaces it — it simply lacks the")
    print(f"  consequence Step 2's framing expected.")
    print(f"\n  NEXT: the phase factors as (z-1)*(h/2); h/2 is Delta_beta = (h/2).I,")
    print(f"  built from h alone, so z-FREE and convention-independent. All the")
    print(f"  convention dependence is in (z-1). Re-derive the single-wrap")
    print(f"  eigenphase on V_(2,1) under the D trace.")
    print()
    print("  === SYMBOLIC, all q (upgrades the 12 sampled rows to an identity) ===")
    print(f"    y_(3)   = {sym['y_(3)']}")
    print(f"    y_(2,1) = {sym['y_(2,1)']}")
    print(f"    y_(1^3) = {sym['y_(1^3)']}   identically zero: {sym['radical_is_identically_zero']}")
    print(f"    sum y_lambda f^lambda = {sym['sum_y_f_symbolic']}  -> == 1 for ALL q: {sym['sum_equals_one_for_all_q']}")
    print(f"    carrier V_(2,1) numerator {sym['carrier_numerator']}, real roots "
          f"{sym['carrier_real_roots']}")
    print(f"    => the ladder's CARRIER BLOCK SURVIVES convention D "
          f"(nonzero for every q > 0): {sym['carrier_nonzero_for_q_positive']}")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
