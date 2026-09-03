#!/usr/bin/env python3
"""Formalize-first prune for the convention-D Q_beta ladder: the phase offset is
forced to bar-weight -4, and the naive z-swap violates it.

Bean `qou-cds1` asks for exactly this before any numerical re-fit:

    "Formalize-first: before any wide numerical re-fit of the ladder, state the
     structural constraint the D-frame ladder must satisfy and check whether it
     prunes the class."

## 1. Two recorded forms of one fact (not a contradiction)

`qou-cds1` records `bar(z_D) = q^-4 * z_D`. Elsewhere this session measured
`bar(z_D) = z_D - h`. Both are correct and equal:

    bar(z_D) = q^-4 z_D = z_D - h = 1/(q^3 + q)

Recorded because the two forms look like different claims about bar parity and
a reader could reasonably think the corpus disagrees with itself.

## 2. z is bar-HOMOGENEOUS in BOTH conventions

    bar(z_C)/z_C = 1        -> bar-weight  0
    bar(z_D)/z_D = q^-4     -> bar-weight -4

So "bar-even" is not a property C has and D lacks; it is weight 0. BOTH
conventions give a bar-eigenvector. The C-frame KC13 statement is the weight-0
instance of a two-case fact, not a special feature of C.

## 3. What actually breaks under D is the AFFINE offset, not z

The ladder phase is `alpha = (z - 1) h / 2`, and `h` is bar-odd
(`bar(h)/h = -1`). Measured:

    C:  bar(alpha)/alpha = -1                             (bar-ODD, clean)
    D:  bar(alpha)/alpha = (q^3+q-1) / (q(q^3-q^2-1))     (NOT homogeneous)

Under D the phase is not a bar-eigenvector at all. The cause is precise:
`z_D` has weight -4 and the constant `1` has weight 0, so `z_D - 1` is a sum of
two different bar-weights, and such a sum is never an eigenvector. **The `-1`
is the obstruction, not `z`.**

This explains the sensitivity measurement `qou-cds1` records -- `c_3 -> -974`,
"no convergence" -- as a structural consequence rather than a bare number: the
naive z-swap keeps a weight-mismatched offset, destroying the bar grading the
C ladder's convergence architecture rests on.

## 4. The prune

For `(z - c) h / 2` to be bar-anti-homogeneous, `c` must carry the SAME
bar-weight as `z`. For a monomial `c = q^n`, `bar(c)/c = q^(-2n)`, so:

    convention C   weight  0  =>  n = 0  =>  c = 1     (bar(alpha)/alpha = -1)
    convention D   weight -4  =>  n = 2  =>  c = q^2   (bar(alpha)/alpha = -q^-4)

**The rule DERIVES convention C's offset of 1 rather than assuming it.** That
is the consistency check that makes it worth stating: a constraint that only
described D could be tuned to say anything.

## What this does NOT establish

It does **not** claim `c = q^2` is the correct D offset. It says: IF the D
ladder is to keep the bar-eigenvector structure the C ladder's convergence
rests on, THEN the offset must carry bar-weight -4, and among monomials that
is uniquely `q^2`. Whether the physical normalisation supplies `q^2` requires
deriving what replaces `tr_M(1) = 1` in the D frame -- OPEN, and not settled
here. A `q^2` reached by search would be a fit; this is reached by grading.

No `c_k` value is proposed, extracted, or wired. Per `qou-cds1`: `c_3 ~ -974`
is a sensitivity measurement, not a value, and nothing here changes that.

Scope: conditional structural constraint (an exact identity in q), not a
numerical probe.

Run:  python3 -u computations/qbeta/qbeta_d_frame_ladder_bar_weight_prune.py
"""
from __future__ import annotations

import sys
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

q = sp.Symbol("q", positive=True)


def bar(e):
    """The bar involution q -> 1/q."""
    return sp.simplify(sp.together(e.subs(q, 1 / q)))


def main() -> int:
    z_C = sp.sqrt(q) / (q + 1)
    z_D = q**3 / (q**2 + 1)
    h = q - 1 / q

    # 1 — the two recorded forms agree
    forms = {
        "bar_z_D": str(bar(z_D)),
        "q_minus4_times_z_D": str(sp.simplify(q**-4 * z_D)),
        "z_D_minus_h": str(sp.simplify(z_D - h)),
        "all_three_equal": bool(
            sp.simplify(bar(z_D) - q**-4 * z_D) == 0
            and sp.simplify(bar(z_D) - (z_D - h)) == 0
        ),
    }

    # 2 — bar-homogeneity of z in both conventions
    weights = {
        "z_C": {"bar_ratio": str(sp.simplify(bar(z_C) / z_C)), "bar_weight": 0},
        "z_D": {"bar_ratio": str(sp.simplify(bar(z_D) / z_D)), "bar_weight": -4},
    }

    # 3 — the phase, with the CURRENT offset of 1
    phases = {}
    for name, zv in (("C", z_C), ("D", z_D)):
        a = (zv - 1) * h / 2
        phases[name] = {
            "alpha": str(sp.simplify(a)),
            "bar_ratio": str(sp.factor(sp.simplify(bar(a) / a))),
            "is_bar_eigenvector": bool(
                sp.simplify(sp.diff(sp.simplify(bar(a) / a), q)) == 0
            ),
        }

    # 4 — the prune: which monomial offset restores homogeneity
    offsets = {}
    for n in range(0, 4):
        c = q**n
        offsets[f"q^{n}"] = str(sp.simplify(bar(c) / c))
    c_D = q**2
    alpha_D = (z_D - c_D) * h / 2
    alpha_C = (z_C - 1) * h / 2
    prune = {
        "rule": "offset bar-weight must equal z's bar-weight; c = q^n has weight -2n",
        "C_forced_offset": "q^0 = 1",
        "C_alpha_bar_ratio": str(sp.simplify(bar(alpha_C) / alpha_C)),
        "C_reproduces_existing_ladder": bool(
            sp.simplify(bar(alpha_C) / alpha_C + 1) == 0
        ),
        "D_forced_offset": "q^2",
        "D_alpha_bar_ratio": str(sp.simplify(bar(alpha_D) / alpha_D)),
        "D_is_homogeneous": bool(
            sp.simplify(sp.simplify(bar(alpha_D) / alpha_D) - (-q**-4)) == 0
        ),
        "h_is_bar_odd": str(sp.simplify(bar(h) / h)),
    }

    q0 = q_at(40)
    q0s = sp.Float(str(q0), 40)
    numeric = {
        k: str(sp.N(v.subs(q, q0s), 20))
        for k, v in (("z_D", z_D), ("z_D_minus_1", z_D - 1),
                     ("z_D_minus_q2", z_D - c_D), ("alpha_D_pruned", alpha_D))
    }

    payload = {
        "description": (
            "Formalize-first prune for the convention-D Q_beta ladder: the "
            "phase offset is forced to bar-weight -4 (uniquely q^2 among "
            "monomials), the same rule derives convention C's offset of 1, and "
            "the naive z-swap violates it by keeping a weight-0 offset."
        ),
        "one_fact_two_forms": forms,
        "bar_weights_of_z": weights,
        "phase_with_current_offset_1": phases,
        "prune": prune,
        "monomial_offset_bar_ratios": offsets,
        "numeric_at_q0": numeric,
        "does_not_establish": (
            "that c = q^2 IS the D offset. Only that bar-homogeneity FORCES "
            "weight -4. What replaces tr_M(1) = 1 in the D normalisation is "
            "open; a q^2 reached by search would be a fit, this is reached by "
            "grading."
        ),
        "context": {
            "beans": ["qou-cds1", "qou-pmkh"],
            "prior": ("qou-cds1 Step 1 (MarkovZFullBarCondition.lean) proved the "
                      "ADDITIVE defect forms; this is the MULTIPLICATIVE "
                      "(eigenvector) reading, which is what prunes the offset"),
            "scope": "conditional structural constraint; exact identity in q",
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "qbeta-d-frame-ladder-bar-weight-prune", payload,
        script_path=__file__, engine="python+sympy (exact in q)",
    ).save()

    print("=== D-frame ladder: the bar-weight prune ===")
    print(f"  bar(z_D) = q^-4 z_D = z_D - h : {forms['all_three_equal']}"
          f"   (= {forms['bar_z_D']})")
    print(f"  bar-weight of z_C / z_D       : 0 / -4  (both eigenvectors)")
    print(f"  phase (z-1)h/2 under C        : bar ratio "
          f"{phases['C']['bar_ratio']}   eigenvector={phases['C']['is_bar_eigenvector']}")
    print(f"  phase (z-1)h/2 under D        : bar ratio "
          f"{phases['D']['bar_ratio']}")
    print(f"                                  eigenvector="
          f"{phases['D']['is_bar_eigenvector']}  <- the swap breaks it")
    print(f"  PRUNE: offset weight must match z's")
    print(f"     C -> c = 1   , bar(alpha)/alpha = {prune['C_alpha_bar_ratio']}"
          f"   (derives the EXISTING ladder)")
    print(f"     D -> c = q^2 , bar(alpha)/alpha = {prune['D_alpha_bar_ratio']}")
    print(f"\n  NOT established: that q^2 is the D offset — only that the "
          f"weight is forced.")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
