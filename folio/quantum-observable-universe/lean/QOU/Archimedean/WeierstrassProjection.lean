import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import QOU.GroundRingCore

/-!
# QOU.Archimedean.weierstrassProjection — Weierstrass projection ℘_q(z)

The Weierstrass elliptic function associated to the Descartes elliptic
curve E_q, defined via the classical Laurent series on ℂ/Λ_q.

LaTeX label: `def:weierstrass-projection`

## References
- [leitner2026] §5/weierstrass-projection

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

-- Ground ring from the canonical module rather than re-declared here.
-- This file used to carry its own
--     abbrev R_q := LaurentPolynomial ℤ
-- inside `namespace QOU.Archimedean`, byte-identical to the one in
-- `QOU/Archimedean/GroundRing.lean:33` and therefore a duplicate
-- **fully-qualified** name: `QOU.Archimedean.R_q` declared in two modules, so
-- the two could never both be imported (bean `qou-kfcl`).
open QOU.GroundRing

namespace QOU.Archimedean

/-- Archimedean specialization map for Laurent-polynomial coefficients.
    This keeps the formal coefficients in `R_q` while allowing the
    differential equation to be stated over `ℂ`.

    Intended semantics: a chosen coefficient specialization
    `ℤ[q, q⁻¹] → ℂ` for the archimedean model. The algebraic properties
    of this map are left axiomatic here because this file only needs
    coefficient transport into the analytic differential equation. -/
opaque coeffEmbed : R_q → ℂ

/-- **External axiom** (Lang, Elliptic Functions §VI.3; manuscript
    §5/weierstrass-projection): the Weierstrass projection ℘_q
    associated to the Descartes elliptic curve.  Axiomatised pending
    a complex Weierstrass-℘ formalisation in Mathlib. -/
-- Ref: [leitner2026] §5/weierstrass-projection
opaque weierstrassProjection : R_q → R_q → ℂ → ℂ

/-- **Derivative `℘'_q` of the Weierstrass projection.**  Opaque for the
    same reason as `weierstrassProjection` itself: there is no complex
    Weierstrass-℘ in Mathlib to differentiate, so `℘'` enters as its own
    named primitive and the differential equation below is what ties the
    two together. -/
-- Ref: [leitner2026] §5/weierstrass-projection
opaque weierstrassProjectionDeriv : R_q → R_q → ℂ → ℂ

/-- **External axiom (Lang, Elliptic Functions Thm VI.3.6):** the
    Weierstrass differential equation

      `℘'(z)² = 4℘(z)³ − g₂·℘(z) − g₃`   for `z ≠ 0`.

    **This axiom used to state something else entirely.**  It read

    ```lean
    ∀ (g2 g3 : R_q) (z : ℂ), z ≠ 0 →
      ∃ (wp_deriv wp_val : ℂ),
        wp_deriv ^ 2 = 4 * wp_val ^ 3 - coeffEmbed g2 * wp_val - coeffEmbed g3
    ```

    — an existential over two *free* complex numbers that never mentions
    `weierstrassProjection`.  Over `ℂ` that is a **theorem, not an
    axiom**: take `wp_val := 0` and `wp_deriv` any square root of
    `−g₃`, which exists because `ℂ` is algebraically closed.  Verified by
    proving it outright, `#print axioms` clean
    (`[propext, Classical.choice, Quot.sound]`).  So the old form
    asserted nothing about ℘, constrained nothing, and its `z` was bound
    but unused in the conclusion.

    The corrected statement quantifies over the *named* primitives
    `weierstrassProjection` and `weierstrassProjectionDeriv`, which is
    what makes it a genuine (and genuinely unproved) external input.
    Bean `qou-t7zg`. -/
-- Ref: [leitner2026] §5/weierstrass-projection
-- Ref: [lang2002algebra] https://doi.org/10.1007/978-0-387-09494-6 Theorem VI.3.6
axiom weierstrass_diff_eq_axiom :
    ∀ (g2 g3 : R_q) (z : ℂ),
      z ≠ 0 →
      weierstrassProjectionDeriv g2 g3 z ^ 2
        = 4 * weierstrassProjection g2 g3 z ^ 3
            - coeffEmbed g2 * weierstrassProjection g2 g3 z
            - coeffEmbed g3

/-- The Weierstrass function satisfies the differential equation
    `℘'(z)² = 4℘(z)³ − g₂℘(z) − g₃`. -/
theorem weierstrass_diff_eq (g2 g3 : R_q) (z : ℂ) (hz : z ≠ 0) :
    weierstrassProjectionDeriv g2 g3 z ^ 2
      = 4 * weierstrassProjection g2 g3 z ^ 3
          - coeffEmbed g2 * weierstrassProjection g2 g3 z
          - coeffEmbed g3 :=
  weierstrass_diff_eq_axiom g2 g3 z hz

/-- **The differential equation exhibits `(℘, ℘')` as a point of the
    Descartes elliptic curve** `y² = 4x³ − g₂x − g₃`.

    A regression witness for the correction above: this is the content
    the old existential form *appeared* to provide and did not.  Under
    that form it was unprovable — `weierstrassProjection` did not occur
    in the axiom, so nothing connected ℘ to the cubic. -/
theorem weierstrass_on_curve (g2 g3 : R_q) (z : ℂ) (hz : z ≠ 0) :
    ∃ x y : ℂ,
      x = weierstrassProjection g2 g3 z ∧
      y = weierstrassProjectionDeriv g2 g3 z ∧
      y ^ 2 = 4 * x ^ 3 - coeffEmbed g2 * x - coeffEmbed g3 :=
  ⟨_, _, rfl, rfl, weierstrass_diff_eq g2 g3 z hz⟩

end QOU.Archimedean
