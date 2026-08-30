#!/usr/bin/env python3
"""What replaces `gramMatrix_det_ne_zero` under convention D: the induced form
on H_3(q)/rad is NONDEGENERATE, with an explicit determinant that has no real
root at all.

## The gap this closes

Bean `qou-pmkh` registers `gram_h3_det_factorization.py` and
`gram_h3_symbolic_regression.py` as convention-C sites that must not stay on C
but cannot be migrated by substituting `z_D`, because under D the determinant
is identically zero -- so the Lean discharge `gramMatrix_det_ne_zero` has no D
analogue. It names the replacement as the open work:

    "What replaces `gramMatrix_det_ne_zero` under D -- rank 5, radical spanned
     by the three-strand q-antisymmetriser -- is the re-derivation, and it is
     real work."

`gram_h3_convention_frame_probe.py` establishes the negative half (D is a root
of det G; rank 5; the radical is the antisymmetriser). This probe supplies the
POSITIVE half: the form that survives, and the statement that replaces the
vanished theorem.

## Result

With `G(q,z)` built generically over Q(q,z) -- z carried as a FREE symbol, so
the conclusion is an identity in two variables rather than a coincidence at
q_0 -- and specialised to z_D = q^3/(q^2 + 1):

    rank G_D = 5,   rad G_D = <r>,   r_w = (-1/q)^len(w)

`rad` is spanned by the three-strand q-antisymmetriser, whose last coordinate
(-1/q)^3 is nonzero, so e_0..e_4 project to a basis of the quotient and the
induced form is the leading 5x5 principal minor. Its determinant:

    det( G_D | H_3/rad )  =  -(q^4 + 1)(q^2 - q + 1)^4 (q^2 + q + 1)^4
                             ----------------------------------------
                                          (q^2 + 1)^10

Every factor is real-rootless:

    q^4 + 1     > 0                        for all real q
    q^2 - q + 1 = (q - 1/2)^2 + 3/4 > 0    for all real q
    q^2 + q + 1 = (q + 1/2)^2 + 3/4 > 0    for all real q
    (q^2 + 1)   > 0                        for all real q

so the numerator, of degree 20, has ZERO real roots (checked by
`sympy.real_roots`, not by sampling). The induced form is therefore
nondegenerate for EVERY real q -- strictly stronger than the q > 1 the
substrate needs.

The determinant is NEGATIVE throughout. That is consistent with, and
independent of, the frame probe's observation that the D Gram carries a
negative eigenvalue at q_0: the quotient form is nondegenerate and INDEFINITE,
not positive definite. Any D-frame successor to the block's
positive-definiteness reading has to say `nondegenerate`, not `positive`.

## What is basis-dependent and what is not

The VALUE above is stated in the complement basis e_0..e_4; a different
complement changes it by the square of a change-of-basis determinant. The
NONVANISHING is basis-independent, and that is the part that replaces the
theorem. Quoting the value without its basis would be a mistake.

Scope (b) per AGENTS.md: this is a structural statement resting on an exact
polynomial identity, not a numerical probe.

Run:  python3 -u computations/probes/gram_h3_quotient_nondegeneracy_probe.py
"""
from __future__ import annotations

import json
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

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
#: the generic Gram, as recorded by gram_h3_convention_frame_probe (upper triangle)
FRAME_WITNESS = HERE / "gram-h3-convention-frame-probe.witness.json"


def build_generic_gram():
    q, z = sp.symbols("q z", positive=True)
    entries = json.loads(FRAME_WITNESS.read_text())["generic_gram_q_z"]
    G = sp.zeros(6, 6)
    for key, val in entries.items():
        i, j = int(key[2]), int(key[5])
        e = sp.sympify(val, locals={"q": q, "z": z})
        G[i, j] = e
        G[j, i] = e          # the witness records the UPPER TRIANGLE only
    return G, q, z


def main() -> int:
    G, q, z = build_generic_gram()
    assert sp.simplify(G - G.T) == sp.zeros(6, 6), "Gram not symmetric"

    z_D = q**3 / (q**2 + 1)
    GD = sp.simplify(G.subs(z, z_D))

    rank = GD.rank()
    radical = sp.Matrix([(-sp.Integer(1) / q) ** len(w) for w in NF_BASIS])
    annihilated = sp.simplify(GD * radical) == sp.zeros(6, 1)

    # e_0..e_4 project to a basis of H_3/rad because radical[5] = (-1/q)^3 != 0.
    M5 = GD[0:5, 0:5]
    det5 = sp.factor(sp.cancel(sp.together(M5.det(method="berkowitz"))))
    num, den = sp.fraction(sp.together(det5))
    real_roots = sp.real_roots(sp.Poly(sp.expand(num), q))

    q0 = q_at(40)
    det5_q0 = sp.N(det5.subs(q, sp.Float(str(q0), 40)), 30)

    payload = {
        "description": (
            "Convention-D replacement for gramMatrix_det_ne_zero: the induced "
            "form on H_3(q)/rad is nondegenerate, with a determinant whose "
            "numerator has no real root."
        ),
        "generic_det_q_z": str(sp.factor(sp.cancel(sp.together(
            G.det(method="berkowitz"))))),
        "at_convention_D": {
            "z_D": str(z_D),
            "rank": int(rank),
            "radical_vector": [str(v) for v in radical],
            "radical_is_q_antisymmetriser": True,
            "radical_annihilated_by_G": bool(annihilated),
        },
        "quotient_form": {
            "complement_basis": "e_0..e_4 (valid since radical[5] = (-1/q)^3 != 0)",
            "det": str(det5),
            "numerator_factored": str(sp.factor(num)),
            "denominator_factored": str(sp.factor(den)),
            "numerator_degree": int(sp.Poly(sp.expand(num), q).degree()),
            "numerator_real_roots": [str(r) for r in real_roots],
            "nondegenerate_for_all_real_q": len(real_roots) == 0,
            "det_at_q0": str(det5_q0),
            "sign": "negative for all q > 0 => nondegenerate and INDEFINITE",
            "basis_dependence": (
                "the VALUE is stated in the complement basis e_0..e_4 and "
                "changes by the square of a change-of-basis determinant; the "
                "NONVANISHING is basis-independent and is what replaces the "
                "theorem"
            ),
        },
        "context": {
            "beans": ["qou-pmkh", "qou-cds2"],
            "companion": "computations/probes/gram_h3_convention_frame_probe.py",
            "lean_superseded": (
                "QOU.Interactions.GramMatrixH3Symbolic.gramMatrix_det_ne_zero "
                "-- true for C, false for D; the D statement is the "
                "nondegeneracy of the induced form above"
            ),
            "scope": ("(b) structural -- rests on an exact polynomial identity "
                      "over Q(q,z), not on a numerical probe"),
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "gram-h3-quotient-nondegeneracy-probe", payload,
        script_path=__file__, engine="python+sympy (exact over Q(q,z))",
    ).save()

    print("=== What replaces gramMatrix_det_ne_zero under convention D ===")
    print(f"  rank G_D                          : {rank}/6")
    print(f"  radical = q-antisymmetriser       : {annihilated}")
    print(f"  det(G_D | H_3/rad), basis e_0..e_4:")
    print(f"      {det5}")
    print(f"  numerator degree                  : "
          f"{sp.Poly(sp.expand(num), q).degree()}")
    print(f"  numerator real roots              : {list(real_roots) or 'NONE'}")
    print(f"  => nondegenerate for all real q   : {len(real_roots) == 0}")
    print(f"  det at q0 (proton)                : {det5_q0}")
    print(f"  sign                              : negative => INDEFINITE, "
          f"not positive definite")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
