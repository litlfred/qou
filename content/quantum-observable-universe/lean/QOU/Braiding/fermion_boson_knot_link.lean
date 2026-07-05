import Mathlib.Tactic

/-!
# QOU.Braiding.fermion_boson_knot_link

**Canonical declaration** for content block referenced by
`qou:QOU.Braiding.fermion_boson_knot_link`.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.Braiding


/-- Abstract context for the `fermion_boson_knot_link` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class FermionBosonKnotLinkContext where
  /-- The categorical object / monoidal structure. -/
  CategoricalObj : Type
  /-- The torus-knot/link family `T(2, n)` indexed by `n`. -/
  T_2n : ℕ → Type
  /-- Predicate: `T(2, n)` is a knot (odd `n`) or link (even `n`). -/
  is_knot : ℕ → Prop
  is_link : ℕ → Prop
  /-- Manuscript identity: `T(2, n)` is a knot iff `n` is odd. -/
  claim_knot_iff_odd : ∀ n : ℕ, 1 ≤ n → (is_knot n ↔ Odd n)
  /-- Manuscript identity: `T(2, n)` is a link iff `n` is even. -/
  claim_link_iff_even : ∀ n : ℕ, 1 ≤ n → (is_link n ↔ Even n)
  /-- Predicate: `T(2, n)` corresponds to a fermion (knot)
      or boson (link) under fermion–boson decomposition. -/
  is_fermion : ℕ → Prop
  is_boson : ℕ → Prop
  /-- Manuscript claim: the knot–link decomposition of `T(2, n)`
      coincides with the fermion–boson decomposition. -/
  claim_fermion_boson_knot_link : ∀ n : ℕ, 1 ≤ n →
    (is_fermion n ↔ is_knot n) ∧ (is_boson n ↔ is_link n)

/-- **Content statement** (from manuscript):

**Proposition.**
The fermion--boson decomposition
([fermion--boson decomposition](#def:fermion-boson-decomposition))
coincides with the knot--link decomposition of the $T(2,n)$
torus family on the Bring's surface:

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/fermion-boson-knot-link.ts
def fermion_boson_knot_link [ctx : FermionBosonKnotLinkContext] :
    (∀ n : ℕ, 1 ≤ n → (ctx.is_knot n ↔ Odd n)) ∧
    (∀ n : ℕ, 1 ≤ n → (ctx.is_link n ↔ Even n)) ∧
    (∀ n : ℕ, 1 ≤ n →
      (ctx.is_fermion n ↔ ctx.is_knot n) ∧
      (ctx.is_boson n ↔ ctx.is_link n)) :=
  ⟨ctx.claim_knot_iff_odd, ctx.claim_link_iff_even,
   ctx.claim_fermion_boson_knot_link⟩

end QOU.Braiding
