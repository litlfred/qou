import QOU.Shared.MarkovTraceClaim

/-!
# QOU.BraidsAndKnots.y_lambda_recipe_from_partition

**Canonical declaration** for content block y_lambda recipe from partition.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

Note: the chapter-dir uses singular `QOU.BraidKnot` for most blocks;
this plural `QOU.BraidsAndKnots` namespace was inherited from existing
`.ts` lean.ref URIs (a pre-existing convention drift).
-/

namespace QOU.BraidsAndKnots


/-- Abstract context for the `y_lambda_recipe_from_partition` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class YLambdaRecipeFromPartitionContext extends QOU.Shared.MarkovTraceContext where
  /-- Jones-Markov coefficient `y_λ(q)` per partition `λ`, valued in the
      inherited coefficient ring `R` of the parent Markov-trace context
      (§7c: `y_λ(q)` is a q-rational in `√q`, not a real). -/
  y_lambda : ℕ → R
  /-- Numerator and denominator of the q-rational representation. -/
  num : ℕ → R
  denom : ℕ → R
  /-- Manuscript identity: `y_λ(q)` is a q-rational with non-vanishing
      denominator and equals `num(λ) / denom(λ)`.

      The quotient is written `num · denom⁻¹` through the parent's `invR`:
      a generic `CommRing R` carries no `Div`, and at `R = ℝ` this is
      definitionally what `num / denom` unfolds to, so the statement is
      unchanged from the previous ℝ-specialised form. -/
  claim_y_lambda_recipe_from_partition :
    haveI := ringR; haveI := invR;
      ∀ lam : ℕ, denom lam ≠ 0 ∧ y_lambda lam = num lam * (denom lam)⁻¹
/-- **Content statement** (from manuscript):

**Proposition (recipe: $\lambda \mapsto y_\lambda(q)$ as q-rational).**
*Given a partition $\lambda \,\vdash\, n$, the Jones-Markov central
coefficient $y_\lambda(q)$ is determined by the following algorithm,
yielding a rational function in $\sqrt q$ with cyclotomic
denominator.*

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.ts
def y_lambda_recipe_from_partition [ctx : YLambdaRecipeFromPartitionContext] :
    haveI := ctx.ringR; haveI := ctx.invR;
      ∀ lam : ℕ,
        ctx.denom lam ≠ 0 ∧ ctx.y_lambda lam = ctx.num lam * (ctx.denom lam)⁻¹ :=
  ctx.claim_y_lambda_recipe_from_partition

end QOU.BraidsAndKnots
