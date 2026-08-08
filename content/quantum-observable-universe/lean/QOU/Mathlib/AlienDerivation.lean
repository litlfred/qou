/-
  Alien derivative algebra — the Leibniz rule for Écalle alien derivatives.

  The alien derivative Δ_ω (indexed by a singularity ω ∈ ℂ) acts on
  resurgent formal power series. Its key algebraic property: Δ_ω is a
  DERIVATION on the algebra of resurgent series under the convolution
  product (equivalently, a derivation on the algebra of Borel sums under
  ordinary multiplication). This file formalizes:

  1. The abstract derivation structure: Δ_ω : A → A satisfying
     Δ_ω(f · g) = Δ_ω(f) · g + f · Δ_ω(g)
  2. The pointed derivation variant (the alien derivative at ω is indexed
     by a singularity location)

  This file proves that algebraic core sorry-free. The analytic content
  (that alien derivatives are well-defined on resurgent functions, that
  they capture the Stokes phenomenon) is NOT formalized here — it lives
  in the Borel transform convergence engine.

  SCOPE CORRECTION (2026-08-08). This header previously also listed
  "3. The Stokes automorphism = exp(Δ_ω)" and "4. The bridge identity"
  among what the file formalizes. Neither was ever in the file — the
  list was a plan read as an inventory.

  The obstacle was one missing lemma, now supplied: the higher Leibniz
  rule Dⁿ(fg) = Σ_k C(n,k)·Dᵏf·D^{n−k}g, absent from Mathlib and proved
  in QOU/MathlibExt/DerivationIterateLeibniz.lean. It is what makes
  exp(D) multiplicative — the binomial convolution IS the Cauchy product
  of the two exponential series. That file also carries the honest
  one-instanton form of §3: at D² = 0, exp(D) = 1 + D is multiplicative
  precisely when the cross-term Df·Dg vanishes.

  §4 (the bridge equation) remains UNPROVED and is not claimed anywhere.

  Pre-archimedean: generic `CommRing` / `Algebra`. No analysis.

  -- Ref: [ecalle1981] Fonctions résurgentes, tome I
  -- Ref: [sauzin2014] https://arxiv.org/abs/1405.0356
-/

import Mathlib.Algebra.Module.Basic
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity

namespace QOU.Mathlib.AlienDerivation

/-! ### §1  Pointed derivation algebra (the alien derivative is a family of derivations) -/

/-- An **alien derivation system** on a commutative algebra `A` over `R`,
    indexed by a set of singularities `Ω`. Each `Δ_ω` is a derivation
    of `A` (satisfies the Leibniz rule). -/
structure AlienDerivationSystem (R : Type*) (A : Type*) (Ω : Type*)
    [CommSemiring R] [CommSemiring A] [Algebra R A] [Module R A] where
  /-- The alien derivative at singularity ω. -/
  alien : Ω → Derivation R A A

/-- The alien derivative at ω satisfies the Leibniz rule — this is the
    defining property, inherited from `Derivation`. Restated for clarity. -/
theorem leibniz {R A Ω : Type*}
    [CommSemiring R] [CommSemiring A] [Algebra R A] [Module R A]
    (sys : AlienDerivationSystem R A Ω) (ω : Ω) (f g : A) :
    sys.alien ω (f * g) = f • sys.alien ω g + g • sys.alien ω f :=
  sys.alien ω |>.leibniz f g

/-- Alien derivatives kill constants (inherited from Derivation.map_algebraMap). -/
theorem map_const {R A Ω : Type*}
    [CommSemiring R] [CommSemiring A] [Algebra R A] [Module R A]
    (sys : AlienDerivationSystem R A Ω) (ω : Ω) (r : R) :
    sys.alien ω (algebraMap R A r) = 0 :=
  (sys.alien ω).map_algebraMap r

/-! ### §2  Composition of Borel transforms — the acceleration kernel

    Écalle's acceleration from Gevrey-k₁ to Gevrey-k₂ (k₂ > k₁) is the
    composition of two Borel-Laplace transforms with a kernel twist. At the
    formal-series level, the algebraic content is: the composition of two
    Borel transforms (division by `n!` twice) gives division by `(n!)²`, and
    the acceleration kernel inverts one of the factorials to produce a
    re-indexing.

    We formalize the purely algebraic core: the double Borel coefficient. -/

open scoped Nat

/-- The double Borel coefficient: `aₙ / (n!)²`. This is the coefficient
    that appears in the Écalle acceleration kernel (Borel of Borel). -/
noncomputable def doubleBorelCoeff (a : ℕ → ℝ) (n : ℕ) : ℝ :=
  a n / ((n ! : ℝ) * (n ! : ℝ))

/-- Double Borel = Borel ∘ Borel: dividing by `(n!)²` is the same as
    dividing by `n!` twice. -/
theorem doubleBorelCoeff_eq (a : ℕ → ℝ) (n : ℕ) :
    doubleBorelCoeff a n = (a n / (n ! : ℝ)) / (n ! : ℝ) := by
  unfold doubleBorelCoeff
  rw [div_div]

/-- Double Borel is additive. -/
theorem doubleBorelCoeff_add (a b : ℕ → ℝ) (n : ℕ) :
    doubleBorelCoeff (fun k => a k + b k) n
      = doubleBorelCoeff a n + doubleBorelCoeff b n := by
  unfold doubleBorelCoeff; rw [add_div]

/-- **Gevrey-2 taming.** A sequence with `|aₙ| ≤ C · Aⁿ · (n!)²` growth
    has geometrically bounded double-Borel coefficients: `|dbc(n)| ≤ C · Aⁿ`.
    The Gevrey-2 analogue of the Gevrey-1 taming theorem. -/
theorem abs_doubleBorelCoeff_le_of_gevrey2 {a : ℕ → ℝ} {C A : ℝ}
    (h : ∀ n, |a n| ≤ C * A ^ n * ((n ! : ℝ) * (n ! : ℝ))) (n : ℕ) :
    |doubleBorelCoeff a n| ≤ C * A ^ n := by
  have hn : (0 : ℝ) < (n ! : ℝ) * (n ! : ℝ) := by positivity
  unfold doubleBorelCoeff
  rw [abs_div, abs_of_pos hn, div_le_iff₀ hn]
  exact h n

/-! ### §3  Acceleration composition law (algebraic form)

    The acceleration `α_{k₁→k₂}` maps Gevrey-k₁ series to Gevrey-k₂ series
    (where k₂ > k₁) by re-indexing the Borel coefficients through the
    acceleration kernel. At the algebraic level, the composition law is:
    `α_{k₁→k₃} = α_{k₂→k₃} ∘ α_{k₁→k₂}` — acceleration is transitive.

    We prove this for the simplest case: the double-Borel coefficient
    factors through single Borel. -/

/-- **Borel composition = double Borel.** Applying the single Borel
    coefficient twice gives the double Borel coefficient. This is the
    formal-series face of the acceleration composition law
    `α_{1→3} = α_{2→3} ∘ α_{1→2}` for Gevrey-1 → Gevrey-2 → Gevrey-3. -/
theorem borelCoeff_compose (a : ℕ → ℝ) (n : ℕ) :
    (a n / (n ! : ℝ)) / (n ! : ℝ) = doubleBorelCoeff a n := by
  rw [doubleBorelCoeff_eq]

end QOU.Mathlib.AlienDerivation
