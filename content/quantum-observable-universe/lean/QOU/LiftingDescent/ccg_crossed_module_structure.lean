/-!
# QOU.LiftingDescent.ccg_crossed_module_structure — `(SU_{q_n}(2), 𝓞_M^×)` crossed module

**Lemma** ([`lem:ccg-crossed-module-structure`](../../../quantum-observable-universe/lifting-and-descent/ccg-crossed-module-structure.md)).

*At each level `n`, the pair `(SU_{q_n}(2), 𝓞_M^×)` is a crossed module
in the sense of Yekutieli (2010), with boundary `∂(a) = a · 𝟙` and
conjugation action `g · a = g a g⁻¹`.*

The Lean encoding records the crossed-module axioms (Peiffer
identity + boundary compatibility) as fields of an abstract
`CrossedModuleContext`.

-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-crossed-module-structure.md
-- Ref: [yekutieli2010] A. Yekutieli, *Nonabelian Multiplicative Integration*, 2010
-/

namespace QOU.LiftingDescent

/-- Abstract crossed-module context for `(SU_{q_n}(2), 𝓞_M^×)`. -/
class CrossedModuleContext where
  /-- The base group `G_n = SU_{q_n}(2)`. -/
  G_n : Type
  /-- The fibre group `H = 𝓞_M^×`. -/
  H : Type
  /-- Group operation on `G_n`. -/
  mul_G : G_n → G_n → G_n
  inv_G : G_n → G_n
  one_G : G_n
  /-- Group operation on `H`. -/
  mul_H : H → H → H
  inv_H : H → H
  one_H : H
  /-- The boundary map `∂ : H → G_n`. -/
  boundary : H → G_n
  /-- The conjugation action `G_n ⊗ H → H`. -/
  action : G_n → H → H
  /-- Embed map from H to G_n. -/
  embed : H → G_n
  /-- Boundary is just the embed map. -/
  boundary_def : ∀ a, boundary a = embed a
  /-- Embed is a homomorphism. -/
  embed_mul : ∀ a b, embed (mul_H a b) = mul_G (embed a) (embed b)
  embed_inv : ∀ a, embed (inv_H a) = inv_G (embed a)
  /-- Action is conjugation in G_n. -/
  action_def : ∀ g a, embed (action g a) = mul_G (mul_G g (embed a)) (inv_G g)
  /-- Embed is injective. -/
  embed_inj : ∀ a b, embed a = embed b → a = b

/-- **Crossed-module axioms hold for `(SU_{q_n}(2), 𝓞_M^×)`**
    ([`lem:ccg-crossed-module-structure`]). -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-crossed-module-structure.md
-- Ref: [yekutieli2010]
theorem ccg_crossed_module_structure
    [ctx : CrossedModuleContext] :
    -- The two axioms are accessible directly via the context's fields.
    (∀ g a, ctx.boundary (ctx.action g a)
              = ctx.mul_G (ctx.mul_G g (ctx.boundary a)) (ctx.inv_G g)) ∧
    (∀ a b, ctx.action (ctx.boundary b) a
              = ctx.mul_H (ctx.mul_H b a) (ctx.inv_H b)) := by
  constructor
  · intro g a
    rw [ctx.boundary_def, ctx.boundary_def]
    exact ctx.action_def g a
  · intro a b
    apply ctx.embed_inj
    rw [ctx.action_def, ctx.boundary_def]
    rw [ctx.embed_mul, ctx.embed_mul, ctx.embed_inv]

end QOU.LiftingDescent
