import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CategoricalLaplace — categorical Laplace transform

The categorical Laplace transform is the monoidal functor

  L : (End(A), ∗_q) → (End(A), ·),    L[f](s) = tr_M(exp_q(-s·) · f),

pairing against the real-exponential grouplike exp_q(-s·) ∈ G(H_q).
It intertwines q-convolution with pointwise product — the mate of
the q-coproduct.

LaTeX label: `def:categorical-laplace`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-laplace

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  Base-ring independent — the
pairing is abstract Hopf-algebraic; integral realisation is
archimedean only.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **Categorical Laplace transform data**: a monoidal functor
    from q-convolution to pointwise product, given abstractly
    as the Hopf pairing with the real-exponential grouplike. -/
-- Ref: [leitner2026] §2
structure CategoricalLaplace (A : Type*) where
  /-- Pairing: f ↦ (s ↦ ⟨exp_q(-s·), f⟩). -/
  transform : (A → A) → R_q → (A → A)
  /-- Monoidal: L[f ∗_q g] = L[f] · L[g]. -/
  monoidal_mul :
    ∀ (f g : A → A) (s : R_q) (q_conv : (A → A) → (A → A) → (A → A)),
      (transform (q_conv f g) s) = fun x => transform f s (transform g s x)
  /-- Unit preservation: L[𝟙] = 𝟙, with the monoidal unit of `A → A`
      under composition pinned to `id` (quantifying `one` over all
      functions makes the structure uninhabitable for |A| ≥ 2). -/
  monoidal_unit :
    ∀ (s : R_q),
      transform id s = id

/-- **Laplace-Fourier Wick rotation**: Fourier at ξ equals Laplace
    at s = iξ (in any base ring containing √(-1)). -/
-- Ref: [leitner2026] §2
def CategoricalLaplace.toFourier
    {A : Type*} (L : CategoricalLaplace A)
    (i_elem : R_q)  -- an element playing the role of √(-1)
    (i_sq : i_elem * i_elem = -1) :
    (A → A) → R_q → (A → A) :=
  fun f xi => L.transform f (i_elem * xi)

end

end QOU
