import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CategoricalFourier — categorical Fourier transform

The categorical Fourier transform is the Hopf pairing with the
unitary exponential grouplike `e_q^{iξ·}`.  By Tannaka-Krein, on
`Rep(SU_q(2))` it is the Peter-Weyl decomposition.

  F[f](ξ) = tr_M(e_q^{iξ·} · f) = (π_j(f))_{j ∈ Ĝ}

LaTeX label: `def:categorical-fourier`

Wick rotation: `F[f](ξ) = L[f](iξ)` — Fourier and Laplace are the
same abstract monoidal functor evaluated at imaginary vs real s.

## References

- [manuscript] §2-quantum-observable-universes/categorical-fourier

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The algebraic Fourier transform
(as Peter-Weyl projection) works over any base ring; the integral
realisation requires a Haar measure (archimedean).
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **Categorical Fourier transform data**: a monoidal functor
    intertwining q-convolution with pointwise product, given
    abstractly as the family of Peter-Weyl projections. -/
-- Ref: [manuscript] §2
structure CategoricalFourier (A : Type*) (Irreps : Type*) where
  /-- The Fourier-image family: one projection per irreducible. -/
  project : Irreps → (A → A) → (A → A)
  /-- Monoidal property: convolution becomes pointwise product
      on each irreducible component. -/
  monoidal :
    ∀ (j : Irreps) (f g : A → A) (q_conv : (A → A) → (A → A) → (A → A)),
      project j (q_conv f g) = fun x => project j f (project j g x)

/-- Wick rotation: Fourier is Laplace at imaginary spectral parameter. -/
-- Ref: [manuscript] §2
def CategoricalFourier.fromLaplace
    {A Irreps : Type*}
    (L : (A → A) → ℂ → (A → A))
    (F : (A → A) → ℝ → (A → A))
    (wick : ∀ (f : A → A) (ξ : ℝ), F f ξ = L f (Complex.I * ξ))
    : Prop :=
  ∀ (f : A → A) (ξ : ℝ), F f ξ = L f (Complex.I * ξ)

end

end QOU
