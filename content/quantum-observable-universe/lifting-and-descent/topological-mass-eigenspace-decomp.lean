/-!
# QOU.LiftingDescent.tm_eigenspace_decomp

The mass-identity integrand `α = (∇_A q, L ∧ F⁺)` decomposes under
the descent involution `τ̂ₙ` into descended and transient parts:

  α = descendedPart(α) + transientPart(α),

with `descendedPart(α) = τ̂ₙ(α)` lying in `im τ̂ₙ = im ℓₙ` (the
descended subalgebra `𝒜_{n+1}^{desc}`), and `transientPart(α) = α −
τ̂ₙ(α)` lying in `ker τ̂ₙ` (the transient subalgebra
`𝒜_{n+1}^{trans}`).  The Killing-form orthogonality of these two
subalgebras together with multiplicative-integral additivity over
orthogonal direct sums gives the lemma's full statement.

This sibling extracts the structural decomposition statement,
delegating to the existing `JetChain.decomposition` theorem in the
Lake tree.

LaTeX label: `lem:topological-mass-eigenspace-decomp`

## References

- [manuscript] §3 Lifting and Descent
- See `QOU.LiftingDescent.JetChain.decomposition` for the underlying
  module-theoretic decomposition.
-/

import QOU.LiftingDescent.JetProlongation

namespace QOU.LiftingDescent

open QOU.LiftingDescent.JetChain in
/-- **Eigenspace decomposition under the descent involution.**

    For any `JetChain` with carriers `EndAlg n`, every element `x ∈
    EndAlg (n+1)` decomposes as the sum of its descended part
    (image of `τ̂ₙ`) and its transient part (kernel of `τ̂ₙ`).  This
    is the structural statement that powers the Killing-form
    orthogonality + multiplicative-integral additivity used in the
    mass-identity proof. -/
-- Ref: [manuscript] §3 Lifting and Descent
theorem tm_eigenspace_decomp
    {R : Type*} [CommRing R]
    {EndAlg : ℕ → Type*}
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [JetChain R EndAlg]
    (n : ℕ) (x : EndAlg (n + 1)) :
    x = QOU.LiftingDescent.JetChain.descendedPart (R := R)
          (EndAlg := EndAlg) n x +
        QOU.LiftingDescent.JetChain.transientPart (R := R)
          (EndAlg := EndAlg) n x :=
  QOU.LiftingDescent.JetChain.decomposition n x

/-- The descended part of `x` lies in the descended subalgebra
    `𝒜_{n+1}^{desc} = im τ̂ₙ = im ℓₙ`. -/
-- Ref: [manuscript] §3 Lifting and Descent
theorem tm_eigenspace_descendedPart_isDescended
    {R : Type*} [CommRing R]
    {EndAlg : ℕ → Type*}
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [JC : JetChain R EndAlg]
    (n : ℕ) (x : EndAlg (n + 1)) :
    QOU.LiftingDescent.JetChain.isDescended (JC := JC) n
      (QOU.LiftingDescent.JetChain.descendedPart
        (R := R) (EndAlg := EndAlg) n x) :=
  QOU.LiftingDescent.JetChain.descendedPart_isDescended n x

/-- The transient part of `x` lies in the transient subalgebra
    `𝒜_{n+1}^{trans} = ker τ̂ₙ`. -/
-- Ref: [manuscript] §3 Lifting and Descent
theorem tm_eigenspace_transientPart_isTransient
    {R : Type*} [CommRing R]
    {EndAlg : ℕ → Type*}
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [JC : JetChain R EndAlg]
    (n : ℕ) (x : EndAlg (n + 1)) :
    QOU.LiftingDescent.JetChain.isTransient (JC := JC) n
      (QOU.LiftingDescent.JetChain.transientPart
        (R := R) (EndAlg := EndAlg) n x) :=
  QOU.LiftingDescent.JetChain.transientPart_isTransient n x

end QOU.LiftingDescent
