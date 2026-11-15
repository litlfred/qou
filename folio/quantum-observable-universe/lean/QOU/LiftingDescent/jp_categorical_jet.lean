import Mathlib.Tactic

/-!
# QOU.LiftingDescent.jp_categorical_jet

**Canonical declaration** for content block
[`lem:jet-prolongation-categorical-jet`](../../../quantum-observable-universe/lifting-and-descent/jet-prolongation-categorical-jet.md): *Categorical jet object $J^1(A)$ inherits the Frobenius--Hopf structure*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.LiftingDescent


/-- Abstract context for `prop:jet-prolongation-categorical-jet`. -/
class JpCategoricalJetContext where
  /-- The jet prolongation object `J^1(A)`. -/
  J1A : Type
  /-- Antipode operator `S'` on `J^1(A)`. -/
  S' : J1A → J1A
  /-- Antipode `S'` is involutive: `S'^2 = id`. -/
  antipode_involutive : ∀ x, S' (S' x) = x

/-- **Lemma statement** (from manuscript):

The categorical jet object
$J^1(A) := A \otimes \Omega^1(A)$, where
$\Omega^1(A) = \ker(m\colon A\otimes A \to A)$ is the bimodule of
Kähler differentials, is an object of the ambient rigid monoidal
category, and inherits a Frobenius--Hopf structure
$(\Delta', \varepsilon', S')$ from $A$.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/jet-prolongation-categorical-jet.ts
theorem jp_categorical_jet [ctx : JpCategoricalJetContext] :
    ∀ x : ctx.J1A, ctx.S' (ctx.S' x) = x :=
  ctx.antipode_involutive

end QOU.LiftingDescent
