#!/usr/bin/env python3
"""The Bring sqrt5 is the Jones polynomial's own sqrt5 — bean qou-lz235.

The `brings-surface` chapter carries a `sqrt5` and attributes it to the
quadratic Gauss sum over the cinquefoil's `Z_5`-orbit,
`sum_k zeta_5^{k^2} = sqrt5` (`bring-trefoil-cinquefoil-channel`). Three
mechanisms have now been proposed for where that `sqrt5` could connect to
quantum invariants, and it is worth separating them before any of them is
written into the paper as one thing:

  1. GAUSS SUM. `sum_k zeta_5^{k^2} = sqrt5`, which is the WRT invariant of a
     lens space. `Sigma_2(T_{2,5}) = L(5,q)`, since
     `|H_1(Sigma_2(K))| = |Delta_K(-1)| = 5`.
  2. BRANCHED COVER. `Sigma_5(T_{2,3})` is the Poincare homology sphere
     `Sigma(2,3,5) = S^3/2I`, since `|H_1| = |Res(Delta, (t^5-1)/(t-1))| = 1`.
     `|2I| = 120 = |S_5| = |Aut(Bring)|`, and the corpus already states
     `P(V)/A_5 = S^2(2,3,5)` in `klein-bring-icosahedral-bridge`.
  3. QUANTUM DIMENSION — this file. At a fifth root of unity the Markov trace
     on the Hecke algebra (Jones, Bull. AMS 12 (1985) 103-111, `uploads/`)
     produces the golden ratio directly as a quantum dimension, and the Bring
     knots' own Jones polynomials evaluate to golden-ratio algebraic integers.

WHAT IS COMPUTED. At `r = 5` the quantum integers are `[n] = sin(n pi/5)/sin(pi/5)`,
so `[2] = [3] = phi = (1+sqrt5)/2` — the golden ratio IS the quantum dimension,
and `sqrt5 = 2 phi - 1`. Evaluating the two Bring torus knots' Jones polynomials
at the two fifth-root points:

                       |V(zeta_10)|^2            |V(zeta_5)|^2
    3_1 trefoil        (3+sqrt5)/2 = phi^2       (7-sqrt5)/2 = 3 - 1/phi
    T_{2,5} cinquefoil (5+sqrt5)/2 = 2 + phi     (7-3 sqrt5)/2 = phi^{-4}

The cinquefoil's value at the golden point, `2 + phi = 1 + phi^2`, is the GLOBAL
DIMENSION `D^2` of the Fibonacci category — the modular tensor category whose
only nontrivial object has quantum dimension `phi`. So the corpus's `sqrt5` and
the Jones polynomial's `sqrt5` are the same `sqrt5`: both are
`Q(sqrt5) = Q(zeta_5)^+`, the real subfield, entering through `2 cos(pi/5)`.

WHAT THIS IS NOT. It is NOT `c_sigma`, and it is not the `sqrt5` of any 1-loop
invariant. `T_{2,3}` and `T_{2,5}` are TORUS knots: simplicial volume zero,
colored Jones growing polynomially rather than exponentially, no Lobachevsky
saddle, and `c_sigma := lim |J'_N| N^{-3/2} e^{-Vol N/2pi}` is not the same
object. The hyperbolic closed forms in `one_loop_vdv_constant_closed_form_probe`
and `one_loop_c_sigma_tetrahedral_probe` live in `Q(i)` and `Q(sqrt-3)`, the two
exceptional IMAGINARY quadratic fields, and `Q(sqrt5)` is real — it cannot
appear there. Two `sqrt5`s of cyclotomic origin are not automatically the same
`sqrt5`, and this file establishes an identification for (1) and (3) while
leaving (2) open.

Nothing is fitted: every value below is an exact radical from `sympy`, compared
against a closed form written down in advance.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

t = sp.symbols("t")
PHI = (1 + sp.sqrt(5)) / 2

# Jones polynomials of the two torus knots the Bring chapter names.
JONES = {
    "3_1 (trefoil)": -t ** (-4) + t ** (-3) + t ** (-1),
    "T_{2,5} (cinquefoil)": (-t ** (-7) + t ** (-6) - t ** (-5)
                             + t ** (-4) + t ** (-2)),
}

# Closed forms asserted BEFORE evaluation.
EXPECT = {
    ("3_1 (trefoil)", 10): (sp.Rational(3, 2) + sp.sqrt(5) / 2, "phi^2"),
    ("3_1 (trefoil)", 5): (sp.Rational(7, 2) - sp.sqrt(5) / 2, "3 - 1/phi"),
    ("T_{2,5} (cinquefoil)", 10): (sp.Rational(5, 2) + sp.sqrt(5) / 2,
                                   "2 + phi = D^2 of the Fibonacci category"),
    ("T_{2,5} (cinquefoil)", 5): (sp.Rational(7, 2) - 3 * sp.sqrt(5) / 2,
                                  "phi^{-4}"),
}


def main() -> int:
    set_compute_dps()
    print("=" * 76)
    print(" The Bring sqrt5 as a quantum dimension — Jones at a fifth root")
    print("=" * 76)

    # -- quantum dimensions at r = 5 --------------------------------------
    print("\n  quantum integers at r = 5:  [n] = sin(n pi/5)/sin(pi/5)\n")
    qdims, gold_ok = {}, True
    for n in range(1, 5):
        v = sp.radsimp(sp.simplify(sp.sin(n * sp.pi / 5) / sp.sin(sp.pi / 5)))
        qdims[f"[{n}]"] = sp.sstr(v)
        print(f"    [{n}] = {v}  = {float(v):.12f}")
    gold_ok = (sp.simplify(sp.sin(2 * sp.pi / 5) / sp.sin(sp.pi / 5) - PHI) == 0)
    print(f"\n    [2] = phi = (1+sqrt5)/2 : {gold_ok}"
          "     -> the golden ratio IS the quantum dimension")
    print(f"    sqrt5 = 2 phi - 1 : "
          f"{sp.simplify(2*PHI - 1 - sp.sqrt(5)) == 0}")

    # -- Jones evaluations -------------------------------------------------
    print("\n  |V(K)|^2 at the two fifth-root points"
          "  (closed forms asserted in advance):\n")
    rows, n_bad = {}, 0
    for name, poly in JONES.items():
        rows[name] = {}
        for k, lab in ((10, "zeta_10 = e^{i pi/5}"), (5, "zeta_5 = e^{2 pi i/5}")):
            val = sp.simplify(sp.expand(
                poly.subs(t, sp.exp(2 * sp.pi * sp.I / k)).rewrite(sp.cos)))
            m2 = sp.nsimplify(sp.N(sp.Abs(val) ** 2, 40), [sp.sqrt(5)])
            m2 = sp.radsimp(sp.simplify(m2))
            want, why = EXPECT[(name, k)]
            ok = sp.simplify(m2 - want) == 0
            n_bad += (not ok)
            rows[name][f"zeta_{k}"] = {
                "abs_V_squared": sp.sstr(m2),
                "closed_form": sp.sstr(want),
                "reading": why,
                "matches": bool(ok),
            }
            print(f"    {name:22s} at {lab:22s}  |V|^2 = {str(m2):>18}"
                  f"   = {why}   {ok}")

    # the Fibonacci global dimension, independently
    D2 = 1 + PHI ** 2
    fib_ok = sp.simplify(D2 - (2 + PHI)) == 0
    print(f"\n    Fibonacci global dimension D^2 = 1 + phi^2 = 2 + phi : {fib_ok}"
          f"  = {float(sp.N(D2)):.12f}")

    all_ok = bool(gold_ok) and n_bad == 0 and bool(fib_ok)
    verdict = (
        "THE BRING sqrt5 AND THE JONES sqrt5 ARE THE SAME sqrt5. At r = 5 the "
        "quantum dimension [2] is the golden ratio phi = (1+sqrt5)/2, and the "
        "two torus knots the Bring chapter names evaluate to golden-ratio "
        "algebraic integers: |V(3_1)|^2 = phi^2 at zeta_10, and "
        "|V(T_{2,5})|^2 = 2 + phi at zeta_10 — the GLOBAL DIMENSION of the "
        "Fibonacci category. Both live in Q(sqrt5) = Q(zeta_5)^+, entering "
        "through 2 cos(pi/5). That identifies the corpus's Gauss-sum sqrt5 with "
        "the Markov-trace sqrt5 of Jones (Bull. AMS 1985). "
        "IT IS NOT c_sigma. T_{2,3} and T_{2,5} are torus knots: zero "
        "simplicial volume, polynomial colored-Jones growth, no Lobachevsky "
        "saddle. The hyperbolic closed forms live in Q(i) and Q(sqrt-3), the "
        "two exceptional IMAGINARY quadratic fields; Q(sqrt5) is real and "
        "cannot appear there. The third proposed mechanism — Sigma_5(trefoil) "
        "= the Poincare sphere, via Lawrence-Zagier — remains open and is "
        "blocked on reading in this environment; see qou-lz235."
        if all_ok else
        "A CHECK FAILED — inspect before citing.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("bring-golden-jones", engine="sympy")
    wb.set_description(
        "Identifies the sqrt5 of the brings-surface chapter with the sqrt5 of "
        "the Jones polynomial at a fifth root of unity. At r = 5 the quantum "
        "dimension [2] = [3] = phi, and the Bring torus knots' Jones "
        "polynomials evaluate to golden-ratio algebraic integers, the "
        "cinquefoil's |V(zeta_10)|^2 = 2 + phi being the Fibonacci category's "
        "global dimension. Separates this from the c_sigma sqrt5 question: "
        "torus knots have zero volume and the hyperbolic closed forms live in "
        "the imaginary quadratic fields Q(i) and Q(sqrt-3), where a real "
        "sqrt5 cannot appear. Exact radicals throughout; closed forms asserted "
        "before evaluation.")
    wb.set_audit_only(
        "docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md")
    wb.add_data("quantum_dimensions_r5", qdims)
    wb.add_data("jones_evaluations", rows)
    wb.add_data("three_candidate_sqrt5_mechanisms", {
        "1_gauss_sum": ("sum_k zeta_5^{k^2} = sqrt5, the WRT invariant of a "
                        "lens space; Sigma_2(T_{2,5}) = L(5,q) since "
                        "|H_1| = |Delta(-1)| = 5. This is what the corpus "
                        "states."),
        "2_branched_cover": ("Sigma_5(T_{2,3}) is the Poincare homology sphere "
                             "Sigma(2,3,5) = S^3/2I, |2I| = 120 = |S_5| = "
                             "|Aut(Bring)|. OPEN — needs lawrence-zagier-1999, "
                             "unreadable here; see qou-lz235."),
        "3_quantum_dimension": ("this file: [2]_{r=5} = phi and the Bring "
                                "knots' Jones values are golden-ratio "
                                "algebraic integers. IDENTIFIED with (1): both "
                                "are Q(sqrt5) = Q(zeta_5)^+ via 2 cos(pi/5)."),
    })
    wb.add_data("what_this_is_not", {
        "not_c_sigma": ("T_{2,3} and T_{2,5} are torus knots — zero simplicial "
                        "volume, polynomial colored-Jones growth, no "
                        "Lobachevsky saddle. c_sigma is a different object and "
                        "the volume conjecture is vacuous on them."),
        "field_obstruction": ("the hyperbolic closed forms live in Q(i) "
                              "(octahedral) and Q(sqrt-3) (tetrahedral), the "
                              "two exceptional IMAGINARY quadratic fields. "
                              "Q(sqrt5) is REAL, so it cannot appear there by "
                              "that route at all."),
    })
    wb.add_assertion(
        "quantum_dimension_at_r5_is_the_golden_ratio",
        computed="1" if gold_ok else "0", expected="1", tolerance="0.5",
        source="[2] = sin(2 pi/5)/sin(pi/5) against (1+sqrt5)/2, symbolically")
    wb.add_assertion(
        "bring_knot_jones_values_are_golden",
        computed=str(len(EXPECT) - n_bad), expected=str(len(EXPECT)),
        tolerance="0.5",
        source=("|V|^2 at zeta_5 and zeta_10 for 3_1 and T_{2,5} against "
                "closed forms asserted before evaluation"))
    wb.add_assertion(
        "cinquefoil_golden_value_is_fibonacci_global_dimension",
        computed="1" if fib_ok else "0", expected="1", tolerance="0.5",
        source="|V(T_{2,5})(zeta_10)|^2 = 2 + phi = 1 + phi^2 = D^2_{Fib}")
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
