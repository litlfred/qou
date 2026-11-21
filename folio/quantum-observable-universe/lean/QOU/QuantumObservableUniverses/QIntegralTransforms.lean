import QOU.Archimedean.GroundRing


/-!
# QOU.QuantumObservableUniverses.QIntegralTransforms — q-integral-transform display structures

Authoritative library home for the categorical Fourier and Laplace
transform data, previously defined only inside content-object display
snippets (`categorical-fourier-transform.lean`,
`categorical-laplace-transform.lean`).  Relocated here (2026-06-09
axiom audit) so the companion `*-unique.lean` display files can
`import` the real structures and carry genuinely type-checked
uniqueness statements.

Ground ring `R_q = ℤ[q, q⁻¹]` from `QOU.Archimedean.GroundRing`.

## References

- [leitner2026] §2-quantum-observable-universes
- [kassel1995] Quantum Groups (Springer GTM 155), §IV
-/

namespace QOU

/-- **Categorical Fourier transform data**: a monoidal functor
    intertwining q-convolution with pointwise product, given as the
    family of Peter–Weyl projections. -/
-- Ref: [leitner2026] §2
structure CategoricalFourier (A : Type*) (Irreps : Type*) where
  /-- The Fourier-image family: one projection per irreducible. -/
  project : Irreps → (A → A) → (A → A)
  /-- Monoidal property: convolution becomes pointwise product
      on each irreducible component. -/
  monoidal :
    ∀ (j : Irreps) (f g : A → A) (q_conv : (A → A) → (A → A) → (A → A)),
      project j (q_conv f g) = fun x => project j f (project j g x)

/-- **Categorical Laplace transform data**: a monoidal functor from
    q-convolution to pointwise product (Hopf pairing with the
    real-exponential grouplike). -/
-- Ref: [leitner2026] §2
structure CategoricalLaplace (A : Type*) where
  /-- Pairing: `f ↦ (s ↦ ⟨exp_q(-s·), f⟩)`. -/
  transform : (A → A) → Archimedean.R_q → (A → A)
  /-- Monoidal: `L[f ∗_q g] = L[f] · L[g]`. -/
  monoidal_mul :
    ∀ (f g : A → A) (s : Archimedean.R_q) (q_conv : (A → A) → (A → A) → (A → A)),
      (transform (q_conv f g) s) = fun x => transform f s (transform g s x)
  /-- Unit preservation: `L[𝟙] = 𝟙`, with the monoidal unit of `A → A`
      under composition pinned to `id`.  Quantifying `one` over *all*
      functions (the previous form) together with `monoidal_mul` makes
      the structure uninhabitable for `|A| ≥ 2`; the unit is a specific
      object, so it is `id`. -/
  monoidal_unit :
    ∀ (s : Archimedean.R_q),
      transform id s = id

end QOU
