import QOU.LiftingDescent.JetProlongation
import Mathlib.Analysis.Normed.Group.Basic


/-!
# QOU.LiftingDescent.tm_eigenspace_decomp

The mass-identity integrand `α = (∇_A q, L ∧ F⁺)` decomposes under
the descent involution `τ̂ₙ` into descended and transient parts:

  α = descendedPart(α) + transientPart(α),

with `descendedPart(α) = τ̂ₙ(α)` lying in `im τ̂ₙ = im ℓₙ` (the
descended subalgebra `𝒜_{n+1}^{desc}`), and `transientPart(α) = α −
τ̂ₙ(α)` lying in `ker τ̂ₙ` (the transient subalgebra
`𝒜_{n+1}^{trans}`).  The Killing-form orthogonality of these two
subalgebras gives additivity of squared norms only. The lemma's statement
is the bound `‖MI∫α‖ ≤ ‖MI∫ τ̂α‖ + ‖MI∫(α − τ̂α)‖`, proved below as
`tm_eigenspace_decomp_norm_le`; equality is open (bean `qou-tmeq`).

This sibling extracts the structural decomposition statement,
delegating to the existing `JetChain.decomposition` theorem in the
Lake tree.

LaTeX label: `lem:topological-mass-eigenspace-decomp`

## References

- [leitner2026] §3 Lifting and Descent
- See `QOU.LiftingDescent.JetChain.decomposition` for the underlying
  module-theoretic decomposition.
-/

namespace QOU.LiftingDescent

open QOU.LiftingDescent.JetChain in
/-- **Eigenspace decomposition under the descent involution.**

    For any `JetChain` with carriers `EndAlg n`, every element `x ∈
    EndAlg (n+1)` decomposes as the sum of its descended part
    (image of `τ̂ₙ`) and its transient part (kernel of `τ̂ₙ`).  This
    is the structural statement that powers the Killing-form
    orthogonality + multiplicative-integral additivity used in the
    mass-identity proof. -/
-- Ref: [leitner2026] §3 Lifting and Descent
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
-- Ref: [leitner2026] §3 Lifting and Descent
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
-- Ref: [leitner2026] §3 Lifting and Descent
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

/-- **The mass bound from the eigenspace split** (the lemma's statement, as
restated 2026-11-20).

Let the multiplicative integral of the mass integrand factor in a seminormed
group `G` as the product of the integrals of its descended and transient parts,
`MI∫α = MI∫τ̂(α) · MI∫(α − τ̂(α))` (`hsplit`). Then the mass, the norm of
`MI∫α`, is at most the sum of the two norms.

Equality is **not** claimed. Killing orthogonality of the two parts does not
give it: orthogonality makes squared norms add, and in a real inner-product
space two non-zero orthogonal vectors satisfy the triangle inequality strictly
(`QOU.Torsion.norm_add_lt_of_inner_eq_zero`, PR #8581). Equality holds iff the
two pieces lie on a common ray (`QOU.Torsion.mass_decomposition_eq_iff`), which
is open. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-eigenspace-decomp.md
theorem tm_eigenspace_decomp_norm_le {G : Type*} [SeminormedGroup G]
    (MIsig MIdesc MItrans : G) (hsplit : MIsig = MIdesc * MItrans) :
    ‖MIsig‖ ≤ ‖MIdesc‖ + ‖MItrans‖ := by
  rw [hsplit]
  exact norm_mul_le' MIdesc MItrans

end QOU.LiftingDescent
