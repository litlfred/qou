#!/usr/bin/env python3
"""gram_h3_supergolden_is_convention_c_artefact_probe.py
=========================================================

**Settles item 3 of bean `qou-zf9n`: the supergolden threshold in
`prop:spectrahedral-phase-collapse` is an artefact of the convention-C
substitution, not a frame-independent feature of the H_3 Gram determinant.**

## The question

`QOU/Archimedean/spectrahedral_phase_collapse.lean` proves
`(gramMatrix u).det = 0` at the supergolden threshold `u³ + u − 1 = 0`
(`u = 1/ψ ≈ 0.6823`), and the content block reads that as a phase transition —
the Gram matrix "develops a kernel and drops rank at `u = 1/ψ`", collapsing the
solution space onto a lower-dimensional face of the Hecke spectrahedron.

`gramMatrix` is the **convention-C** matrix. Bean `qou-zf9n` records that under
convention D the determinant is identically zero for every `q`
(`QOU.…GramMatrixH3Symbolic.gramMatrixD_det_eq_zero`, sorry-free), so the
theorem stays true and becomes empty: a vanishing that holds everywhere singles
out no threshold. The bean then asks — and says it is answerable directly from
the generic form — *is `1/ψ` intrinsic, or an artefact of the substitution?*

## The method (no fitting, no search, no numerics in the verdict)

Over `ℚ(q, z)` the H_3 Gram determinant factors as

    det = −(z − q)⁵ (qz + 1)⁵ ((q²+1)z − q³) (q³z + qz + 1) / q⁸

(recorded in `qou-zf9n`; this probe takes the four factors as given and does not
re-derive the determinant). Substitute each convention's `z` into each factor
and ask, **symbolically**, which factor supplies the supergolden cubic and
whether it survives the change of convention. Convention C is written in its
square-root variable, `q = u²` and `z_C = u/(u²+1)`, which is the form
`spectrahedral_phase_collapse.lean` is parameterised by.

The verdict rests on an **exact polynomial division with zero remainder**, not
on a numerical zero. That distinction is load-bearing here: evaluating
`z_C − q` at a float64 root of `u³+u−1` returns `5.55e-17`, which is the floor
of the arithmetic and is evidence about `float`, not about the algebra.

## The answer

**The supergolden cubic is the numerator of `(z − q)` under convention C,
exactly:**

    z_C − q  =  −u (u³ + u − 1) / (u² + 1)        with q = u², z_C = u/(u²+1)

Dividing that numerator by `u³ + u − 1` gives quotient `−u` and remainder
**0** — exact, in `ℚ[u]`.

**Under convention D the same factor never vanishes:**

    z_D − q  =  −q / (q² + 1)                     with z_D = q³/(q²+1)

whose numerator `−q` has no positive root. At `q = (1/ψ)²` it evaluates to
`−0.3826…`, not near zero.

**And the two frames' det-vanishings have disjoint mechanisms.** Under D the
determinant vanishes through `((q²+1)z − q³) ≡ 0` — the Markov-parameter
relation itself, which is `markovWeightD_root`. Under C that same factor is
`−u(u−1)(u⁶+u⁵+2u⁴+u³+u²+u+1)/(u²+1)`, vanishing on `u > 0` only at `u = 1`,
i.e. `q = 1`, the classical point. So convention C's threshold is the
supergolden value and convention D's is everywhere, and neither is the other's
image.

## Scope: (a), not (b) — and the distinction matters for what comes next

This is **not** a structural exclusion of a supergolden feature anywhere in the
framework. It is the narrower, stronger-than-numerical claim that *this*
threshold, in *this* determinant, is the root the convention-C substitution
creates in the factor `(z − q)`. Bean `qou-zf9n` item 2 offers, as one honest
disposition of the content block, re-deriving "whether some other D-frame
object has a supergolden rank drop, which would be a real result rather than a
relabel". This measurement does not forbid that search; it removes the
motivation the block's own claim rested on, because the supergolden value is
not a frame-independent feature of the Gram determinant. An agent taking that
route should know it is looking for a new result, not recovering an old one.

## What this probe does NOT establish

- It does not re-derive the generic factorisation; it consumes it from
  `qou-zf9n` and `gram_h3_convention_frame_probe.py`.
- It says nothing about whether `prop:spectrahedral-phase-collapse` should be
  retired, re-scoped or re-derived. That is authoring in a second content
  block and is the owner's call (bean `qou-zf9n` item 2).
- The convention-C theorems are **correct theorems about a non-canonical
  frame** and are not touched. Per AGENTS.md a Lean-proved piece is a permanent
  contribution; this probe scopes a reading, not a proof.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Same bootstrap as the sibling `gram_h3_convention_frame_probe.py`.
# `witness_base` lives under `computations/substrate/`, not `computations/`,
# so a plain `PYTHONPATH=computations` is not enough to import it.
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent.parent / "computations"
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

q, z, u = sp.symbols("q z u", positive=True)

#: The four non-trivial factors of the H_3 Gram determinant over ``Q(q, z)``,
#: as recorded in bean ``qou-zf9n`` (which derives them in
#: ``computations/probes/gram_h3_convention_frame_probe.py``). This probe
#: consumes them; it does not re-derive the determinant.
FACTORS: dict[str, sp.Expr] = {
    "(z - q)": z - q,
    "(q*z + 1)": q * z + 1,
    "((q^2+1)*z - q^3)": (q**2 + 1) * z - q**3,
    "(q^3*z + q*z + 1)": q**3 * z + q * z + 1,
}

#: The supergolden cubic. Its real root ``u = 1/psi`` is the threshold
#: ``spectrahedral_phase_collapse.lean`` singles out.
SUPERGOLDEN = u**3 + u - 1

Z_D = q**3 / (q**2 + 1)          # convention D, canonical (owner ruling R1)


def _c_frame(expr: sp.Expr) -> sp.Expr:
    """A factor rewritten in convention C's square-root variable.

    ``q = u**2`` and ``z_C = u/(u**2 + 1)``, which is ``sqrt(q)/(q+1)``. This is
    the parameterisation ``gramMatrix u`` uses, so the result is directly
    comparable with the Lean statement.
    """
    return sp.together(expr.subs({q: u**2, z: u / (u**2 + 1)}))


def _d_frame(expr: sp.Expr) -> sp.Expr:
    """A factor rewritten in convention D, rational in ``q``."""
    return sp.simplify(sp.together(expr.subs(z, Z_D)))


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append((name, bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    print("=" * 84)
    print(" H_3 Gram determinant: is the supergolden threshold a convention-C artefact?")
    print("=" * 84)
    print()

    print("Each factor under convention C, in the sqrt variable (q = u^2, z_C = u/(u^2+1)):")
    c_forms: dict[str, str] = {}
    for name, f in FACTORS.items():
        fu = sp.factor(_c_frame(f))
        c_forms[name] = sp.sstr(fu)
        print(f"  {name:22s} -> {fu}")
    print()

    print("Each factor under convention D (rational in q):")
    d_forms: dict[str, str] = {}
    for name, f in FACTORS.items():
        fd = sp.factor(_d_frame(f))
        d_forms[name] = sp.sstr(fd)
        pos_roots = [r for r in sp.solve(sp.numer(sp.together(fd)), q) if r.is_positive]
        print(f"  {name:22s} -> {fd}      positive roots: {pos_roots or 'none'}")
    print()

    # ---- 1. The supergolden cubic IS the numerator of (z - q) under C. -----
    num_c = sp.expand(sp.numer(_c_frame(z - q)))
    quo, rem = sp.div(num_c, sp.expand(SUPERGOLDEN), u)
    check(
        "supergolden_divides_zC_minus_q_exactly",
        sp.expand(rem) == 0 and sp.expand(quo + u) == 0,
        f"numer(z_C - q) = {sp.factor(num_c)}; divided by u^3+u-1 -> "
        f"quotient {sp.expand(quo)}, remainder {sp.expand(rem)} (EXACT in Q[u], "
        f"not a numerical zero)",
    )

    # ---- 2. Under D that same factor never vanishes for q > 0. ------------
    zd_minus_q = _d_frame(z - q)
    check(
        "zD_minus_q_has_no_positive_root",
        sp.simplify(zd_minus_q - (-q / (q**2 + 1))) == 0
        and not [r for r in sp.solve(sp.numer(sp.together(zd_minus_q)), q) if r.is_positive],
        f"z_D - q = {sp.factor(zd_minus_q)}; numerator -q has no positive root, "
        f"so the factor carrying C's threshold is nowhere zero under D",
    )

    # ---- 3. D's identical vanishing comes from a DIFFERENT factor. --------
    markov_d = _d_frame((q**2 + 1) * z - q**3)
    check(
        "D_vanishing_is_the_markov_relation_not_z_minus_q",
        sp.simplify(markov_d) == 0,
        "((q^2+1)z - q^3) == 0 identically under D (this is markovWeightD_root), "
        "so D's det-vanishing and C's supergolden threshold have disjoint "
        "mechanisms",
    )

    # ---- 4. Under C that Markov factor singles out q = 1, not 1/psi. ------
    markov_c_num = sp.expand(sp.numer(_c_frame((q**2 + 1) * z - q**3)))
    markov_c_pos = sorted(
        {r for r in sp.solve(markov_c_num, u) if r.is_real and r.is_positive}
    )
    check(
        "C_markov_factor_vanishes_only_at_u_eq_1",
        markov_c_pos == [sp.Integer(1)],
        f"numer under C factors as {sp.factor(markov_c_num)}; its only positive "
        f"real root is u = {markov_c_pos} (i.e. q = 1, the classical point), "
        f"NOT the supergolden value",
    )

    # ---- 5. The other C factor is the supergolden CONJUGATE cubic, and it
    #         has no positive root -- so it cannot supply a threshold either.
    qz1_num = sp.expand(sp.numer(_c_frame(q * z + 1)))
    qz1_pos = [r for r in sp.solve(qz1_num, u) if r.is_real and r.is_positive]
    check(
        "C_qz_plus_1_factor_has_no_positive_root",
        qz1_num == sp.expand(u**3 + u**2 + 1) and not qz1_pos,
        f"numer(q*z_C + 1) = {sp.factor(qz1_num)} -- the supergolden-family "
        f"conjugate cubic -- with no positive real root, so the (qz+1)^5 factor "
        f"supplies no threshold on u > 0",
    )

    # ---- 6. Report the root itself at high precision, labelled as numeric. -
    root = sp.real_roots(sp.Poly(SUPERGOLDEN, u))[0]
    root_str = sp.sstr(sp.N(root, 50))
    zd_at_root = sp.N(zd_minus_q.subs(q, sp.N(root, 60) ** 2), 30)
    check(
        "zD_minus_q_at_supergolden_is_far_from_zero",
        abs(zd_at_root) > sp.Rational(1, 10),
        f"u = 1/psi = {root_str[:32]}...; z_D - q at q = u^2 is "
        f"{sp.sstr(zd_at_root)[:24]}..., i.e. O(0.1), not a near-vanishing. "
        f"(Evaluating z_C - q here in float64 returns ~5.6e-17, the floor of "
        f"that arithmetic -- which is why the verdict rests on check 1's exact "
        f"division and not on this number.)",
    )

    print()
    all_ok = all(ok for _, ok, _ in checks)
    print(f"  {sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks passed")
    print()
    print("VERDICT: the supergolden cubic u^3 + u - 1 is the numerator of the")
    print("         convention-C factor (z - q). Under convention D that factor is")
    print("         -q/(q^2+1), nowhere zero for q > 0, and D's identical")
    print("         det-vanishing comes from ((q^2+1)z - q^3) instead. So the")
    print("         threshold at u = 1/psi is an artefact of the substitution")
    print("         z = u/(u^2+1), not a frame-independent feature of the H_3 Gram")
    print("         determinant. Scope (a): this does not exclude a supergolden")
    print("         feature elsewhere -- it removes the motivation the content")
    print("         block's claim rested on. Bean qou-zf9n item 3.")

    w = WitnessBuilder("gram-h3-supergolden-is-convention-c-artefact", engine="python")
    w.set_description(
        "Settles bean qou-zf9n item 3: the supergolden threshold u^3+u-1 of "
        "prop:spectrahedral-phase-collapse is the numerator of the convention-C "
        "factor (z - q), by exact division in Q[u] with remainder 0. Under the "
        "canonical convention D that factor is -q/(q^2+1), which has no positive "
        "root, and D's identical determinant-vanishing comes from the Markov "
        "relation ((q^2+1)z - q^3) = 0 instead. The two frames' vanishings have "
        "disjoint mechanisms and C's threshold has no D-frame counterpart. "
        "Scope (a), not (b): no supergolden feature is excluded anywhere else."
    )
    w.add_data("determinant_factors_generic", {k: sp.sstr(v) for k, v in FACTORS.items()})
    w.add_data("factors_under_convention_C_in_sqrt_variable", c_forms)
    w.add_data("factors_under_convention_D", d_forms)
    w.add_data("markov_parameter_C", "z_C = sqrt(q)/(q+1) = u/(u^2+1) with q = u^2")
    w.add_data("markov_parameter_D", "z_D = q^3/(q^2+1) (canonical, owner ruling R1)")
    w.add_data("supergolden_cubic", sp.sstr(SUPERGOLDEN))
    w.add_data("supergolden_root_1_over_psi_50dps", root_str)
    w.add_data("exact_division", {
        "numerator_of_zC_minus_q": sp.sstr(sp.factor(num_c)),
        "divided_by": sp.sstr(SUPERGOLDEN),
        "quotient": sp.sstr(sp.expand(quo)),
        "remainder": sp.sstr(sp.expand(rem)),
        "note": "remainder 0 in Q[u] -- exact, not a numerical zero",
    })
    w.add_data("verdict", "convention-C artefact of the substitution z = u/(u^2+1)")
    w.add_data("scope", "(a) scope-limited negative, NOT (b) structural exclusion")
    w.add_data("does_not_establish", [
        "the generic factorisation (consumed from qou-zf9n / "
        "gram_h3_convention_frame_probe.py, not re-derived here)",
        "what prop:spectrahedral-phase-collapse should say instead -- authoring "
        "in a second content block, owner's call (qou-zf9n item 2)",
        "that no supergolden feature exists elsewhere in the framework",
    ])
    w.add_data("tracked_by", "qou-zf9n (item 3)")
    for name, ok, detail in checks:
        # Every check here is a symbolic yes/no, so computed/expected carry the
        # verdict as a string rather than a number with a tolerance. A numeric
        # tolerance would be meaningless: the evidence is an exact division in
        # Q[u], not an agreement to N digits.
        w.add_assertion(name, "PASS" if ok else "FAIL", "PASS", source=detail)
    w.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})
    print()
    print(f"  Witness: gram-h3-supergolden-is-convention-c-artefact.witness.json")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
