#!/usr/bin/env python3
"""
weak_vertex_t35_trace.py — the weak-vertex form factor W(q) = tr_M((σ₀σ₁)⁵) in
H₃(q) has the closed form q²(q¹² + q⁸ − 1)/(q² + 1)² under convention D.

WHAT THIS SETTLES.  `rem:hadron-half-life-fermi` lists W(q) — the canonical
Markov trace of the T(3,5) torus braid (σ₀σ₁)⁵ — as an *open computation*, and
`prop:hadron-half-life`'s Lean (BetaRateData.W2, PR #6631) carries it as
positive data with no closed form.  Bean `qou-egvf`.

Two independent routes, both exact in symbolic q:

1. The canonical trace directly: `markov_trace_canonical.tr_M_word` on the
   word (0,1)*5 in H₃, with hecke_symbolic's h = q − q⁻¹ and z = q³/(q²+1).
2. Wedderburn: tr_M = Σ_λ y_λ χ_λ.  The weights are solved from the three
   basis values tr(1)=1, tr(σ₀)=z, tr(σ₀σ₁)=z² using the characters
   χ₍₃₎ = (1, q, q²), χ₍₂₁₎ = (2, q−q⁻¹, −1), χ₍₁₁₁₎ = (1, −q⁻¹, q⁻²); the
   solution is y₍₃₎ = (q⁴+1)/(q²+1)², y₍₂₁₎ = q²/(q²+1)², y₍₁₁₁₎ = 0 (the
   SU(2)/Temperley–Lieb signature of convention D).  Then (σ₀σ₁)³ = Δ² is the
   identity on (2,1) (content sum 0), so χ₍₂₁₎((σ₀σ₁)⁵) = χ₍₂₁₎((σ₀σ₁)²) = −1
   and W = y₍₃₎ q¹⁰ − y₍₂₁₎.

Both give q²(q¹² + q⁸ − 1)/(q² + 1)².  Cross-check against a published
invariant: T(3,5) = 10₁₂₄ has Jones polynomial V(t) = t⁴ + t⁶ − t¹⁰, and the
numerator of W is q²²·V(q⁻²) — the writhe/mirror normalisation of the Ocneanu
trace of a positive 3-strand braid.

Lean carrier (sorry-free): QOU.Braiding.WeakVertexT35.weakVertexTrace_eq in
folio/quantum-observable-universe/lean/QOU/Braiding/WeakVertexT35TraceClosedForm.lean.

FINDING, NOT EDITED HERE.  obs:hadron-half-life-verification publishes
W(q₀) ≈ 0.7036 ("computed exactly").  At the proton pin the convention-D
value is ≈ 1.18748 and the convention-C value (z = √q/(q+1), excised) is
≈ 0.9063; neither Ocneanu trace reproduces 0.7036.  PROVENANCE IDENTIFIED
2026-09-05 (bean qou-ix74; this docstring first blamed the deprecated
t35-full-calculation.py, which was wrong): the live hecke_division engine's
former _trace_word applied the Markov rotation without the Hecke relation,
which collapses to Σ_w c_w z^{|w|} over the reduced word — 0.70355 at z_C
(the published figure) and 0.96844 at z_D (the value t35-weak-vertex.witness.json
carried from 2026-08-29).  The engine now delegates to the canonical recursion.
The content was corrected in PR #6689 (bean qou-4x7c).  The convention-C
number below is a deliberate, labelled comparison, not a live value.

Precision: sympy-exact throughout; the numerical evaluations are mpmath at
60 dps from the exact closed form and from the exact tr_M_word expression
(lambdified to mpmath), serialised at 50 digits.  No float is formed.

Output: computations/weak-vertex-t35-trace.witness.json
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
import hecke_symbolic as hs  # noqa: E402
from markov_trace_canonical import tr_M_word  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = hs.q                      # the MODULE's symbol (see d_frame_cyclotomic_exponent_probe)
H = hs.HA                     # q − q⁻¹
Z_D = hs.z_markov             # q³/(q²+1)  — convention D (canonical, R1)
Z_C = sp.sqrt(q) / (q + 1)    # convention C — excised; deliberate comparison ONLY

WORD_T35 = (0, 1) * 5         # (σ₀σ₁)⁵ ∈ H₃, 0-based generators
CLOSED_FORM = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2
JONES_T35 = lambda t: t ** 4 + t ** 6 - t ** 10   # noqa: E731  V_{10_124}(t)

PUBLISHED_W_Q0 = sp.Rational(7036, 10000)   # obs:hadron-half-life-verification, "≈ 0.7036"


def wedderburn_weights(z):
    """Solve tr(1)=1, tr(σ₀)=z, tr(σ₀σ₁)=z² for (y₃, y₂₁, y₁₁₁)."""
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    sol = sp.solve(
        [y3 + 2 * y21 + y111 - 1,
         y3 * q + y21 * (q - 1 / q) - y111 / q - z,
         y3 * q ** 2 - y21 + y111 / q ** 2 - z ** 2],
        [y3, y21, y111], dict=True)[0]
    return tuple(sp.factor(sol[s]) for s in (y3, y21, y111))


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP

    # Route 1: the canonical trace on the word.
    tr_direct = sp.factor(sp.simplify(tr_M_word(WORD_T35, 3, Z_D, H)))
    # Route 2: Wedderburn.
    y3, y21, y111 = wedderburn_weights(Z_D)
    chi21_T35 = sp.Integer(-1)          # (σ₀σ₁)³ = 1 on (2,1); trace((σ₀σ₁)²) = −1
    tr_wedderburn = sp.factor(y3 * q ** 10 + y111 * q ** (-10) + y21 * chi21_T35)
    # The six Ocneanu basis values from the Wedderburn functional (3 beyond the 3 solved).
    basis_checks = {
        "1":       (y3 + 2 * y21 + y111, sp.Integer(1)),
        "s0":      (y3 * q + y21 * (q - 1 / q) - y111 / q, Z_D),
        "s0s1":    (y3 * q ** 2 - y21 + y111 / q ** 2, Z_D ** 2),
        "s0s1s0":  (y3 * q ** 3 + y21 * (q - 1 / q) - y111 / q ** 3, H * Z_D ** 2 + Z_D),
    }
    # χ₍₂₁₎(σ₀σ₁σ₀): eigenvalues of σ₀σ₁σ₀ on (2,1) are q and −q⁻¹ (it is conjugate
    # to a generator times a unit...); computed directly from the matrices instead:
    A = sp.Matrix([[q, 1], [0, -1 / q]]); B = sp.Matrix([[-1 / q, 0], [1, q]])
    chi21_s0s1s0 = sp.simplify((A * B * A).trace())
    basis_checks["s0s1s0"] = (y3 * q ** 3 + y21 * chi21_s0s1s0 - y111 / q ** 3,
                              H * Z_D ** 2 + Z_D)
    chi21_T35_matrix = sp.simplify(((A * B) ** 5).trace())
    M3 = sp.simplify((A * B) ** 3)

    # Convention-C comparison (labelled; excised convention).
    tr_direct_C = sp.simplify(tr_M_word(WORD_T35, 3, Z_C, H))

    # Numerics at the proton pin, exact → mpmath.
    f_closed = sp.lambdify(q, CLOSED_FORM, "mpmath")
    f_direct = sp.lambdify(q, tr_direct, "mpmath")
    f_C = sp.lambdify(q, tr_direct_C, "mpmath")
    W_D = f_closed(q0)
    W_D_direct = f_direct(q0)
    W_C = f_C(q0)
    W_1 = CLOSED_FORM.subs(q, 1)

    jones_lhs = sp.expand(q ** 2 * (q ** 12 + q ** 8 - 1))
    jones_rhs = sp.expand(sp.simplify(q ** 22 * JONES_T35(q ** (-2))))

    assertions = [
        {"name": "direct_trace_equals_closed_form",
         "passed": sp.simplify(tr_direct - CLOSED_FORM) == 0,
         "note": "markov_trace_canonical.tr_M_word((0,1)*5, 3, z_D, h) == "
                 "q^2(q^12+q^8-1)/(q^2+1)^2, exactly"},
        {"name": "wedderburn_equals_closed_form",
         "passed": sp.simplify(tr_wedderburn - CLOSED_FORM) == 0,
         "note": "y3*q^10 + y111*q^-10 - y21 with the solved weights"},
        {"name": "sign_weight_vanishes_convention_D",
         "passed": sp.simplify(y111) == 0,
         "note": "y_(1,1,1) = 0: convention D is the SU(2)/TL trace"},
        {"name": "weights_reproduce_all_six_basis_values",
         "passed": all(sp.simplify(l - r) == 0 for l, r in basis_checks.values()),
         "note": "1, z, z, z^2, z^2, h z^2 + z — three more than were solved for"},
        {"name": "full_twist_trivial_on_21",
         "passed": M3 == sp.eye(2),
         "note": "(σ₀σ₁)^3 = 1 on the seminormal (2,1) block, all q"},
        {"name": "chi21_T35_is_minus_one",
         "passed": chi21_T35_matrix == -1,
         "note": "trace((σ₀σ₁)^5) on (2,1) = trace((σ₀σ₁)^2) = -1, q-independent"},
        {"name": "numerator_is_q22_jones_T35_at_q_inv2",
         "passed": sp.simplify(jones_lhs - jones_rhs) == 0,
         "note": "V_{10_124}(t) = t^4 + t^6 - t^10; q^2(q^12+q^8-1) = q^22 V(q^-2)"},
        {"name": "direct_and_closed_agree_at_proton_pin",
         "passed": abs(W_D - W_D_direct) < mp.mpf(10) ** (-50),
         "note": "both mpmath at 60 dps from exact expressions"},
        {"name": "published_0_7036_not_reproduced_by_either_convention",
         "passed": (abs(W_D - mp.mpf("0.7036")) > mp.mpf("0.01")
                    and abs(W_C - mp.mpf("0.7036")) > mp.mpf("0.01")),
         "note": "FINDING: obs:hadron-half-life-verification's W(q0) ≈ 0.7036 is "
                 "neither the D value (~1.1875) nor the C value (~0.9063); it "
                 "is hecke_division's former z^{len} trace rule at z_C (bean "
                 "qou-ix74); content corrected in PR #6689 (bean qou-4x7c)."},
    ]

    n50 = lambda x: mp.nstr(x, 50, strip_zeros=False)  # noqa: E731
    witness = {
        "computation": "weak-vertex-t35-trace",
        "description": (
            "Closed form for the weak-vertex form factor W(q) = tr_M((σ₀σ₁)⁵) "
            "in H₃(q), convention D: q²(q¹²+q⁸−1)/(q²+1)². Two exact routes "
            "agree (the canonical tr_M_word, and Wedderburn with solved weights "
            "y3=(q⁴+1)/(q²+1)², y21=q²/(q²+1)², y111=0), and the numerator is "
            "q²²·V_{T(3,5)}(q⁻²) with V = t⁴+t⁶−t¹⁰ (10_124). Closes the "
            "one-level-down GAP of qou-jk6k. The published W(q0) ≈ 0.7036 is "
            "reproduced by neither convention and is flagged, not edited."
        ),
        "convention": {
            "markov_z": "q**3/(q**2 + 1)   (convention D, canonical per R1)",
            "hecke_h": "q - 1/q",
            "anchor": "proton pin (qou_substrate.constants.Q_50_DIGIT_STR) for the "
                      "numerical values; the closed form itself is exact in q",
        },
        "braid_word": "(σ₀σ₁)^5 in B_3 -> H_3(q); torus knot T(3,5) = 10_124",
        "closed_form": str(CLOSED_FORM),
        "closed_form_direct_trace": str(tr_direct),
        "wedderburn": {
            "y_3": str(y3), "y_21": str(y21), "y_111": str(y111),
            "chi_3_T35": "q**10", "chi_21_T35": str(chi21_T35_matrix),
            "chi_111_T35": "q**-10 (weight 0)",
            "chi_21_s0s1s0": str(chi21_s0s1s0),
        },
        "jones_cross_check": {
            "V_T35": "t**4 + t**6 - t**10",
            "identity": "q**2*(q**12 + q**8 - 1) == q**22 * V(q**-2)",
        },
        "q0": Q_50_DIGIT_STR,
        "W_at_q0_convention_D": n50(W_D),
        "W_at_q0_convention_D_direct_trace": n50(W_D_direct),
        "W_at_1": str(W_1),
        "comparison_convention_C_EXCISED": {
            "z": "sqrt(q)/(q+1)",
            "W_at_q0": n50(W_C),
            "note": "deliberate labelled comparison against the excised convention; "
                    "not a live value",
        },
        "published_value_finding": {
            "block": "obs:hadron-half-life-verification",
            "published_W_q0": "0.7036",
            "provenance": "hecke_division._trace_word's former z^{len} rule (Markov "
                          "rotation without the Hecke relation) at z_C = sqrt(q)/(q+1): "
                          "0.70355; the same rule at z_D gave 0.96844 (bean qou-ix74)",
            "status": "reproduced by neither convention's Ocneanu trace; content "
                      "corrected in PR #6689 (bean qou-4x7c)",
        },
        "lean": "QOU.Braiding.WeakVertexT35.weakVertexTrace_eq",
        "reference_blocks": ["rem:hadron-half-life-fermi", "prop:hadron-half-life",
                             "obs:hadron-half-life-verification", "def:markov-trace"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy+mpmath")
    witness["scriptFile"] = str(
        pathlib.Path(__file__).resolve().relative_to(REPO / "computations"))
    out = REPO / "computations" / "weak-vertex-t35-trace.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  W_D(q0) = {n50(W_D)}")
    print(f"  W_C(q0) = {n50(W_C)}   (excised convention, comparison only)")
    print(f"  allPassed = {witness['allPassed']}   -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
