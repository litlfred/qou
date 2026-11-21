import QOU.LiftingDescent.JetProlongation

/-!
# QOU.LiftingDescent.tm_eigenspace_decomp

**Canonical declaration** for content block
[`lem:topological-mass-eigenspace-decomp`](../../../mass-endomorphism/topological-mass-eigenspace-decomp.md):
*Eigenspace decomposition of the mass integrand (descent involution)*.

The manuscript lemma says: the mass-identity integrand
`α = (∇_A q, L ∧ F⁺)` splits under the descent involution `τ̂ₙ` into a
descended and a transient part, those two parts are Killing-orthogonal,
and the multiplicative-integral norm is additive over Killing-orthogonal
sums — whence `‖MI(α)‖ = ‖MI(α_desc)‖ + ‖MI(α_trans)‖`.

**What is proved here versus what is assumed.** The *splitting* is not
assumed: it is `QOU.LiftingDescent.JetChain.decomposition`, proved in
`JetProlongation` from the retraction identity. What the context class
carries is the two genuinely-open inputs — Killing-orthogonality of the
two eigenspaces at the integrand, and the additivity law for `MI` over
Killing-orthogonal sums. Neither is a bare `Prop`: each is an equation
in the class's own data, so no instance can discharge it with `trivial`,
and the conclusion is *derived* from them rather than carried as a field
(AGENTS.md §3b-cond item 5).

This replaces an earlier encoding in which `killing_orthogonal` and
`mi_additive` were opaque `Prop` fields with companion witnesses and the
conclusion was a third field projected out — a shape under which an
instance could take both hypotheses to be `True` and still be forced to
supply the conclusion outright.
**The `mi_additive` field is not satisfiable by a norm (2026-11-20).** If `MI`
is an actual norm induced by an inner product, and `killing` is that inner
product, then two non-zero orthogonal elements satisfy the triangle inequality
**strictly** (`QOU.Torsion.norm_add_lt_of_inner_eq_zero`, PR #8581). So
`mi_additive` fails for them, and the class has no honest instance with
`MI = norm`. The content block now states `≤`. Its Lean is
`QOU.LiftingDescent.tm_eigenspace_decomp_norm_le` in the content sibling. The
equality is tracked as open in bean `qou-tmeq`. This conditional theorem is
kept as a record of the earlier claim. It is no longer the block's `lean.ref`.
-/

universe u v

namespace QOU.LiftingDescent

open QOU.LiftingDescent.JetChain in
/-- Context for the `tm_eigenspace_decomp` claim: a jet-chain level, a
Killing form and a multiplicative-integral norm on that level, the mass
integrand, and the two manuscript hypotheses relating them. -/
class TmEigenspaceDecompContext
    (R : Type u) [CommRing R]
    (EndAlg : ℕ → Type v)
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [JetChain R EndAlg] where
  /-- The brane-tower level at which the decomposition is taken. -/
  level : ℕ
  /-- The Killing form on the level-`level + 1` endomorphism algebra. -/
  killing : EndAlg (level + 1) → EndAlg (level + 1) → R
  /-- The multiplicative-integral norm functional `x ↦ ‖MI(x)‖`. -/
  MI : EndAlg (level + 1) → ℝ
  /-- The mass-identity integrand `α = (∇_A q, L ∧ F⁺)`. -/
  alpha : EndAlg (level + 1)
  /-- **Killing-form orthogonality** of `𝒜^desc` and `𝒜^trans` at the
  integrand: the descended and transient parts of `α` pair to zero. -/
  killing_orthogonal :
    killing (descendedPart (R := R) (EndAlg := EndAlg) level alpha)
            (transientPart (R := R) (EndAlg := EndAlg) level alpha) = 0
  /-- **Multiplicative-integral additivity** over Killing-orthogonal
  sums: `MI` is additive on any pair that pairs to zero. -/
  mi_additive :
    ∀ x y : EndAlg (level + 1), killing x y = 0 → MI (x + y) = MI x + MI y

open QOU.LiftingDescent.JetChain in
/-- **Lemma** (manuscript `lem:topological-mass-eigenspace-decomp`).

Let `α` be the integrand of the mass identity for a vortex `ϱ` and let
`τ̂ₙ` be the descent involution. Killing-form orthogonality of
`𝒜_{n+1}^desc ⊕ 𝒜_{n+1}^trans` together with multiplicative-integral
additivity over orthogonal direct sums gives

    ‖MI(α)‖ = ‖MI(α_desc)‖ + ‖MI(α_trans)‖.

The proof rewrites `α` by the *proved* jet-chain decomposition and then
applies the additivity law at the orthogonality hypothesis. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-eigenspace-decomp.ts
theorem tm_eigenspace_decomp
    {R : Type u} [CommRing R]
    {EndAlg : ℕ → Type v}
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [JetChain R EndAlg]
    [ctx : TmEigenspaceDecompContext R EndAlg] :
    ctx.MI ctx.alpha =
      ctx.MI (descendedPart (R := R) (EndAlg := EndAlg) ctx.level ctx.alpha) +
      ctx.MI (transientPart (R := R) (EndAlg := EndAlg) ctx.level ctx.alpha) := by
  conv_lhs =>
    rw [JetChain.decomposition (R := R) (EndAlg := EndAlg) ctx.level ctx.alpha]
  exact ctx.mi_additive _ _ ctx.killing_orthogonal

end QOU.LiftingDescent
