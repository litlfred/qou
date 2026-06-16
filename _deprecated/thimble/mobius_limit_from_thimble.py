#!/usr/bin/env python3
"""
Möbius integration limit a(q) = (4-q)/(4q+3) — closed-form witness.

Linked to content block: conj:mobius-limit-from-thimble.

The conjecture asserts that the integration limit appearing in the
baryon-period real-axis integral is the closed-form Möbius pencil

    a(q) = (4 - q) / (4 q + 3).

CAL-4 caveat (2026-05-22). The earlier framing — that a(q) is the
"steepest-descent re-entry abscissa of the Picard–Lefschetz thimble
emanating from z_c^+" — was retracted on main (def:picard-lefschetz-
thimble demoted to rem: on commit f86ea9d7a; the descent crossing
witness gives x_re ≈ 3.86, an order of magnitude larger than
a(q_0) ≈ 0.388). The Möbius matrix M = [[-1, 4], [4, 3]] entries
{4, 3} match the cubic's c²-coefficient + degree, but the variable
q in (4-q) and (4q+3) is NOT sourced by the color-tube cubic
F(z, c) ∈ ℤ[z][c] (no q in F). Consequently this ansatz remains
a fit to the CODATA m_p target (cheat-sheet Migration Backlog #1;
companion to LAMBDA_PROTON_FITTED_FROM_CODATA per PR #888).

This script certifies the closed-form algebraically, evaluates it at
q = q₀, and cross-checks the q = 1 sanity value a(1) = 3/7. It does
NOT derive a(q); the q-source is open work.

Trust chain
-----------
sympy closed-form   ──→   evaluate at q₀   ──→   numerical sanity at q = 1.

The asserted equality is the algebraic identity itself (sympy-
verified). The numerical agreement with CODATA m_p via A(a(q)) is
empirical (CAL-4-fitted, per the caveat above).

Usage
-----
    python3 computations/mobius_limit_from_thimble.py
"""

import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from witness_base import WitnessBuilder
from witness_polynomial import expose_polynomial


def build_witness() -> WitnessBuilder:
    w = WitnessBuilder("mobius-limit-from-thimble", engine="sympy")
    w.set_description(
        "Closed-form Möbius pencil a(q) = (4-q)/(4q+3) — CAL-4-"
        "fitted ansatz on the categorical-action integration limit "
        "(conj:mobius-limit-from-thimble). The earlier PL "
        "re-entry-abscissa framing was retracted on main "
        "(commit f86ea9d7a); the q-source is open work. Algebraic "
        "identity (closed form, sanity at q=1) verified by sympy."
    )
    w.set_content_block("conj:mobius-limit-from-thimble")
    w.add_parameter("q0", float(q0))

    # ── Algebraic identity ─────────────────────────────────────
    q = sp.symbols("q", positive=True)
    a = (4 - q) / (4 * q + 3)

    # Sanity: a(1) = 3/7
    a_at_1 = sp.simplify(a.subs(q, 1))
    w.add_assertion(
        "a(1) = 3/7",
        computed=str(a_at_1),
        expected="3/7",
        source="algebraic substitution q = 1",
    )

    # Numerical evaluation at q₀
    a_at_q0 = float(a.subs(q, sp.Float(float(q0), 30)))
    w.add_assertion(
        "a(q0) ≈ 0.38843",
        computed=a_at_q0,
        expected=0.38843,
        tolerance=1e-3,
        source="evaluation of closed form at q = q0",
    )

    # Möbius-pole structure: numerator vanishes at q = 4
    # (re-entry collapses) and denominator at q = -3/4 (off the
    # physical range q > 0).  Both are simple poles → Möbius.
    q_free = sp.symbols("q_free")
    pole_q = sp.solve(4 * q_free + 3, q_free)
    zero_q = sp.solve(4 - q_free, q_free)
    w.add_assertion(
        "Möbius zero at q = 4",
        computed=str(zero_q),
        expected="[4]",
        source="numerator (4 - q) of a(q)",
    )
    w.add_assertion(
        "Möbius pole at q = -3/4",
        computed=str(pole_q),
        expected="[-3/4]",
        source="denominator (4q + 3) of a(q)",
    )

    w.add_data("a_q_closed_form", str(a))
    w.add_data("a_q_polynomial", expose_polynomial(a, q))
    w.add_data("a_q0_numeric", a_at_q0)

    # Möbius matrix M = (-1, 4; 4, 3) — referenced in
    # prop:mobius-golden-fixed-points
    M = sp.Matrix([[-1, 4], [4, 3]])
    w.add_data("mobius_matrix_M", [[int(M[i, j]) for j in range(2)] for i in range(2)])
    w.add_data("mobius_matrix_det", int(M.det()))
    w.add_data("mobius_matrix_trace", int(M.trace()))

    # CAL-4 caveat (2026-05-22): the historical PL re-entry-abscissa
    # cross-check is no longer informative — the descent crossing
    # witness gives x_re ≈ 3.86, an order of magnitude larger than
    # a(q_0) ≈ 0.388. The retained certification is the algebraic
    # identity at q = 1 and the closed-form evaluation at q_0.
    w.add_caveat(
        "Closed-form Möbius pencil — CAL-4-fitted ansatz "
        "(conj:mobius-limit-from-thimble). The earlier "
        "steepest-descent re-entry framing was retracted on main "
        "(commit f86ea9d7a) since the PL crossing is numerically at "
        "x_re ≈ 3.86, not at a(q_0) ≈ 0.388. The q-source is open "
        "work; this witness certifies only the algebraic closed form "
        "and its sanity at q = 1."
    )

    return w


def main() -> int:
    w = build_witness()
    w.save()
    return 0 if all(a.passed for a in w.assertions) else 1


if __name__ == "__main__":
    sys.exit(main())
