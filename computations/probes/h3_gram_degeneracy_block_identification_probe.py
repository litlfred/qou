#!/usr/bin/env python3
"""Which Wedderburn block degenerates at each zero of the H_3 Gram determinant?

`QOU.Machinery.H3.gramMatrix_det_ne_zero` (sorry-free) excludes four points, and
its docstring names them:

    the character weights `z = q`, `z = -q^-1` (quintic factor) and the two
    **(2,1)-block** Markov-weight zeros `z = q^3/(q^2+1)`, `z = -1/(q(q^2+1))`
    (quadratic factor)

The theorem is TRUE -- its four hypotheses do exclude exactly the vanishing
locus, and this probe re-derives the determinant to confirm that.  The defect is
the *identification* in the prose: the quadratic zeros are attributed to the
`(2,1)` block, which has dimension 2.  A block of dimension `d` dropping out of
the trace costs the Gram `d^2` dimensions, so `(2,1)` would give corank 4.

Measured corank at each quadratic zero is **1**, and the null vector is a
one-dimensional block:

  * `z = q^3/(q^2+1)` (convention D)  ->  radical `(-q^3, q^2, q^2, -q, -q, 1)`,
    which is `(-1/q)^len(w)` up to scale: the q-ANTIsymmetriser, i.e. the SIGN
    representation `(1^3)`, dim 1.
  * `z = -1/(q(q^2+1))`              ->  radical `(q^-3, q^-2, q^-2, q^-1, q^-1, 1)`,
    which is `q^len(w)` up to scale: the q-symmetriser, i.e. the TRIVIAL
    representation `(3)`, dim 1.

So the quadratic factor tracks the two one-dimensional blocks, not `(2,1)`.
Corank at the quintic zeros is 5, not 1, which the prose also does not say.

This matters beyond tidiness: the z_D radical is exactly `gramRadicalD` in
`QOU.Interactions.GramMatrixH3Symbolic`, and reading it as `(2,1)` instead of
`(1^3)` breaks the connection to `y_lambda = 0` for partitions with >= 3 rows
(bean qou-8iru) -- which is the same phenomenon seen from the weights.

Exact over Q(q) throughout; no float anywhere.  The Gram is transcribed from the
Lean `def gramMatrix (z h : R)` and the transcription is checked against the
Lean's own closed-form determinant before anything is concluded from it.
"""

from __future__ import annotations

import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from witness_base import WitnessBuilder  # noqa: E402

LEAN_REL = "content/quantum-observable-universe/lean/QOU/Machinery/HeckeH3GramNondegeneracy.lean"

z, h, q = sp.symbols("z h q")

#: `QOU.Machinery.H3.gramMatrix`, on the GB normal-form basis [γ, σ₀, σ₁, L₊, L₋, e⁻].
GRAM = sp.Matrix([
    [1, z, z, z**2, z**2, h*z**2 + z],
    [z, h*z + 1, z**2, h*z**2 + z, h*z**2 + z, h**2*z**2 + h*z + z**2],
    [z, z**2, h*z + 1, h*z**2 + z, h*z**2 + z, h**2*z**2 + h*z + z**2],
    [z**2, h*z**2 + z, h*z**2 + z, h**2*z**2 + h*z + z**2,
     h**2*z**2 + 2*h*z + 1, h**3*z**2 + h**2*z + 2*h*z**2 + z],
    [z**2, h*z**2 + z, h*z**2 + z, h**2*z**2 + 2*h*z + 1,
     h**2*z**2 + h*z + z**2, h**3*z**2 + h**2*z + 2*h*z**2 + z],
    [h*z**2 + z, h**2*z**2 + h*z + z**2, h**2*z**2 + h*z + z**2,
     h**3*z**2 + h**2*z + 2*h*z**2 + z, h**3*z**2 + h**2*z + 2*h*z**2 + z,
     h**4*z**2 + h**3*z + 3*h**2*z**2 + 3*h*z + 1],
])

#: Coxeter lengths of the normal-form words, in basis order.
LENGTHS = [0, 1, 1, 2, 2, 3]

POINTS = [
    ("z_eq_q",            q,                     "quintic"),
    ("z_eq_neg_inv_q",   -1/q,                   "quintic"),
    ("z_D",               q**3/(q**2 + 1),       "quadratic"),
    ("z_eq_neg_inv_q_q2p1", -1/(q*(q**2 + 1)),   "quadratic"),
]


def proportional(a, b) -> bool:
    ratios = {sp.simplify(x / y) for x, y in zip(a, b) if sp.simplify(y) != 0}
    return len(ratios) == 1


def main() -> int:
    # Gate: the transcription must reproduce the Lean's own closed form, or
    # nothing below is about the Lean object.
    det = sp.expand(GRAM.det(method="berkowitz"))
    lean_det = sp.expand(-(z**2 - h*z - 1)**5 * ((h**2 + 4)*z**2 - (h**3 + 4*h)*z - 1))
    transcription_ok = sp.simplify(det - lean_det) == 0

    Gq = GRAM.subs(h, q - 1/q)
    antisym = [(-1/q)**n for n in LENGTHS]
    sym = [q**n for n in LENGTHS]

    rows = []
    for name, val, factor in POINTS:
        ns = sp.simplify(Gq.subs(z, val)).nullspace()
        corank = len(ns)
        vec = [sp.simplify(c) for c in ns[0]] if corank else []
        ident, dim = "n/a", None
        if corank:
            if proportional(vec, antisym):
                ident, dim = "sign (1^3)", 1
            elif proportional(vec, sym):
                ident, dim = "trivial (3)", 1
            else:
                ident = "unidentified"
        rows.append({
            "point": name,
            "z": str(val),
            "det_factor": factor,
            "corank": corank,
            "null_vector": [str(sp.factor(c)) for c in vec],
            "block": ident,
            "block_dim": dim,
        })

    by = {r["point"]: r for r in rows}
    quad = [r for r in rows if r["det_factor"] == "quadratic"]
    quint = [r for r in rows if r["det_factor"] == "quintic"]

    checks = [
        ("transcription_matches_lean_closed_form", transcription_ok, True,
         "GRAM reproduces QOU.Machinery.H3.gramMatrix_det exactly"),
        ("quadratic_zeros_have_corank_one",
         all(r["corank"] == 1 for r in quad), True,
         "both quadratic zeros drop exactly one dimension"),
        ("quadratic_blocks_are_one_dimensional",
         all(r["block_dim"] == 1 for r in quad), True,
         "sign (1^3) at z_D, trivial (3) at the other -- NOT (2,1), which is dim 2"),
        ("zD_radical_is_the_antisymmetriser",
         by["z_D"]["block"] == "sign (1^3)", True,
         "matches GramMatrixH3Symbolic.gramRadicalD exactly"),
        ("quintic_zeros_have_corank_five",
         all(r["corank"] == 5 for r in quint), True,
         "the quintic factor's zeros are a far larger degeneracy than the prose suggests"),
        ("docstring_2_1_attribution_holds",
         any(r["block"] == "(2,1)" for r in quad), False,
         "EXPECTED FALSE -- this is the defect being recorded"),
    ]

    payload = {
        "description": (
            "Corank and Wedderburn-block identification at each of the four "
            "degeneracy points excluded by QOU.Machinery.H3.gramMatrix_det_ne_zero. "
            "The theorem is true; its docstring misattributes the two quadratic "
            "zeros to the (2,1) block, which has dimension 2 and would therefore "
            "cost corank 4. Measured corank is 1 at each, and the radicals are the "
            "q-antisymmetriser (sign, at z_D) and the q-symmetriser (trivial)."
        ),
        "lean": LEAN_REL,
        "general_determinant": "-(z^2 - h z - 1)^5 * ((h^2+4) z^2 - (h^3+4h) z - 1)",
        "hecke_specialisation": "h = q - 1/q",
        "points": rows,
        "assertions": [
            {"name": n, "value": bool(g), "expected": bool(w),
             "passed": bool(g) is w, "note": note}
            for n, g, w, note in checks
        ],
        "allPassed": all(bool(g) is w for _n, g, w, _note in checks),
        "context": {
            "bean": "qou-zf9n",
            "affects": [
                "QOU.Machinery.H3.gramMatrix_det_ne_zero (docstring only; theorem is true)",
                "QOU.Interactions.GramMatrixH3Symbolic.gramRadicalD (confirmed independently)",
            ],
            "scope": (
                "(b) structural: the corank of an explicit matrix over Q(q) and the "
                "dimension of an S_3 irrep are both exact invariants, so 'dim 2 "
                "cannot produce corank 1' is a proved exclusion, not a probe result."
            ),
            "arithmetic": "exact over Q(q); no float64 anywhere",
        },
    }

    out = WitnessBuilder.wrap_legacy(
        "h3-gram-degeneracy-block-identification", payload,
        script_path=__file__, engine="python+sympy(exact over Q(q))",
    ).save()

    print("=== H_3 Gram: which block degenerates where? ===")
    print(f"  transcription matches Lean closed form: {transcription_ok}")
    print()
    print(f"  {'point':<22} {'factor':<10} {'corank':>6}  block")
    for r in rows:
        print(f"  {r['point']:<22} {r['det_factor']:<10} {r['corank']:>6}  {r['block']}")
    print()
    for n, g, w, note in checks:
        good = bool(g) is w
        print(f"  [{'PASS' if good else 'FAIL'}] {n:<40} = {bool(g)!s:<5} ({note})")
    print()
    print("The Lean theorem is TRUE -- all four hypotheses are needed and sufficient.")
    print("Only the docstring's block attribution is wrong: the quadratic zeros are")
    print("the two ONE-dimensional blocks, sign (1^3) at z_D and trivial (3) at the")
    print("other, not the two-dimensional (2,1).")
    print()
    print(f"  witness -> {out}")
    return 0 if payload["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
