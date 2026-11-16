import Mathlib.Tactic

/-!
# Two-filtration bridge in full generality

Compiled formalisation of `conj:two-filtration-bridge-general`.
Sibling docstub at `algebraic-substrate/two-filtration-bridge-general.lean`.

The bar-class → iterated-integral-depth bridge: under the bridge map,
self-conjugate cells of a partition λ land at depth 2 (Bloch–Wigner /
Li_2), chiral pairs (λ ≠ λ') land at depth 3 (Li_3 / period-3 family).
-/

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral

open Classical

/-- Abstract context for the `two_filtration_bridge_general` claim. -/
class TwoFiltrationBridgeContext where
  /-- Partition index type. -/
  PartitionIdx : Type
  /-- Conjugate-partition involution `λ ↦ λ'`. -/
  conj : PartitionIdx → PartitionIdx
  /-- Depth assigned to a partition by the bridge map (target in the
      iterated-integral depth filtration). -/
  depth : PartitionIdx → ℕ
  /-- Chiral/self-conjugate splitting: the depth is 2 for self-conjugate and 3 for chiral. -/
  depth_formula : ∀ lam : PartitionIdx, depth lam = if conj lam = lam then 2 else 3

/-- **Restatement of the class field, not a derivation.**
    (`conj:two-filtration-bridge-general`.) Self-conjugate cells go to
    depth 2, chiral pairs to depth 3, at every partition.

    The class field `depth_formula` *is* this statement, and the proof
    only unfolds it, so this is a self-assuming projection: it holds for
    any context whatsoever and carries no evidence for the bridge. The
    claim rests on `conj:two-filtration-bridge` and on matching the
    transposing involution on `H_n(q)` with orientation reversal on
    periods; neither is formalised. (The bar involution fixes every
    `e_λ`, so it cannot be the separating involution.) Queued for
    demotion to a conjecture carrier (2026-11-16). -/
-- Ref: [leitner2026] quantum-observable-universe/algebraic-substrate/two-filtration-bridge-general.md
theorem bridge_map_general [ctx : TwoFiltrationBridgeContext] :
    (∀ lam : ctx.PartitionIdx, ctx.conj lam = lam → ctx.depth lam = 2) ∧
    (∀ lam : ctx.PartitionIdx, ctx.conj lam ≠ lam → ctx.depth lam = 3) := by
  constructor
  · intro lam h
    rw [ctx.depth_formula lam, if_pos h]
  · intro lam h
    rw [ctx.depth_formula lam, if_neg h]

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral
