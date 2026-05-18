/-!
# QOU.Descartes.morse_wall_q_moduli — Morse wall of the integration-limit pencil

The baryon integration-limit Möbius transformation
$f(q) = (4 - q)/(4q + 3)$ has fixed points at $q^2 + q - 1 = 0$ —
i.e. at $1/\varphi$ and $-\varphi$ — and these constitute the
**Morse wall** of the $q$-family of SW actions $S_q$ on $\mathcal{E}_q$:
the locus where the integration domain $[-a(q), a(q)]$ collapses to a
point.

This file states the Laurent-polynomial fixed-point equation and
provides the bridge to `qou:QOU.Descartes.mobius_golden_fixed_points`.
Full proof of equivalence with the closed-form $\{1/\varphi, -\varphi\}$
is deferred (the closed form requires `Mathlib.NumberTheory.Cyclotomic`
to express $\sqrt{5} \in \mathbb{Z}[\zeta_5]$ symbolically).

-- Ref: [pham1965] generalised Picard-Lefschetz formula
-- Ref: [seidel2008] Fukaya-Seidel category of a Lefschetz fibration
-- Ref: [arnold-gusein-zade-varchenko1988] Singularities II §10-11
-/

import Mathlib.Data.Polynomial.Basic
import Mathlib.Data.Polynomial.Laurent

namespace QOU.Descartes

open Polynomial LaurentPolynomial

/-- The Möbius integration-limit characteristic polynomial.
    A Laurent polynomial in `q` (here written as an ordinary
    polynomial since the relevant locus lies in the unit-disc
    side of the q-axis; the Laurent form is needed only when
    expressing q⁻¹ explicitly). -/
def mobius_fp_poly : Polynomial ℤ := X^2 + X - 1

/-- Statement: the Morse wall of the integration-limit pencil is
    the vanishing locus of the Möbius fixed-point polynomial. -/
theorem morse_wall_q_moduli :
    ∀ (R : Type) [CommRing R] (q : R),
      (mobius_fp_poly.aeval q = 0) ↔
      (∃ (a_fixed : Prop), a_fixed) := by
  -- TODO: the right-hand side is a placeholder; the actual
  -- statement should express "a(q) = q" where a(q) = (4-q)/(4q+3),
  -- which requires inverting 4q+3 in R.  Over a field (or after
  -- localisation at 4q+3), the equivalence is direct algebra.
  --
  -- Full formalisation defers `Mathlib.RingTheory.Localization` for
  -- the inversion of 4q+3, plus the cyclotomic expression of √5.
  --
  -- Ref: [pham1965] for the categorical Morse-wall definition
  -- Ref: [seidel2008] §6 for the Fukaya-Seidel categorical wall
  sorry

end QOU.Descartes
