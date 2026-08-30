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

## The one link NOT established

The `1` in `alpha = (z - 1)h/2` is a **bare literal** at
`computations/qbeta/qbeta_utils.py:255`. That it IS `tr_M(1)` is an
interpretation this probe does not prove — it is the reading under which the
conclusion above follows. If the `1` has a different provenance, the weight-0
argument does not apply to it and the offset question reopens. Whoever takes
the next step should settle that provenance first; it is cheap and it decides
which of two paths the re-derivation takes.

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


def main() -> int:
    data = json.loads(WENZL_WITNESS.read_text())["results"]

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
                "weight 0 != weight -4, so IF the phase offset is the trace "
                "normalisation then no offset-reinterpretation makes the D "
                "phase bar-homogeneous. The natural repair is CLOSED; the D "
                "ladder must be rebuilt on another principle."
            ),
        },
        "link_not_established": (
            "the `1` in alpha = (z - 1)h/2 is a BARE LITERAL at "
            "computations/qbeta/qbeta_utils.py:255. That it IS tr_M(1) is the "
            "reading under which the verdict follows, and this probe does not "
            "prove it. Settle that provenance first — it is cheap and it "
            "decides which path the re-derivation takes."
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

    out = WitnessBuilder.wrap_legacy(
        "qbeta-trm-identity-normalisation-under-d", payload,
        script_path=__file__, engine="python+sympy+exact rationals",
    ).save()

    print("=== What replaces tr_M(1) = 1 under convention D? NOTHING ===")
    print(f"  sum_lambda y_lambda f^lambda == 1 exactly, all rows : {all_one}")
    print(f"    ({len(rows)} rows: 3 s-values x n = 2..5, exact rationals)")
    print(f"  derived, or imposed?                                : IMPOSED at the")
    print(f"    recursion base, then REPRODUCED by the D solve — a consistency")
    print(f"    check, not a derivation")
    print(f"  bar-weight of the offset 1                          : {one_weight}  (weight 0)")
    print(f"  bar-weight of z_D                                   : {z_weight} (weight -4)")
    print(f"  => Step 2's required weight -4 is UNAVAILABLE; the offset repair")
    print(f"     is CLOSED and the D ladder needs another principle.")
    print(f"\n  NOT established: that the `1` in alpha IS tr_M(1) — bare literal")
    print(f"  at qbeta_utils.py:255. Settle that first.")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
