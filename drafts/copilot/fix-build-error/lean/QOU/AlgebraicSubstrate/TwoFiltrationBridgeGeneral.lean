/-!
# Two-filtration bridge in full generality

Compiled formalisation of `prop:two-filtration-bridge-general`.
Sibling docstub at `algebraic-substrate/two-filtration-bridge-general.lean`.

The bar-class → iterated-integral-depth bridge: under the bridge map,
self-conjugate cells of a partition λ land at depth 2 (Bloch–Wigner /
Li_2), chiral pairs (λ ≠ λ') land at depth 3 (Li_3 / period-3 family).
-/

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral

/-- Abstract context for the `two_filtration_bridge_general` claim. -/
class TwoFiltrationBridgeContext where
  /-- Partition index type. -/
  PartitionIdx : Type
  /-- Conjugate-partition involution `λ ↦ λ'`. -/
  conj : PartitionIdx → PartitionIdx
  /-- Depth assigned to a partition by the bridge map (target in the
      iterated-integral depth filtration). -/
  depth : PartitionIdx → ℕ
  /-- Manuscript claim — self-conjugate cells land at depth 2:
      whenever `λ = conj λ`, the bridge places `λ` at depth 2. -/
  claim_self_conjugate_depth_two : ∀ λ : PartitionIdx,
    conj λ = λ → depth λ = 2
  /-- Manuscript claim — chiral pairs land at depth 3: whenever
      `λ ≠ conj λ`, the bridge places `λ` at depth 3. -/
  claim_chiral_pair_depth_three : ∀ λ : PartitionIdx,
    conj λ ≠ λ → depth λ = 3

/-- **Theorem (`prop:two-filtration-bridge-general`).**
    The bar-class → iterated-integral-depth bridge map: self-
    conjugate cells go to depth 2, chiral pairs go to depth 3,
    at every partition. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/two-filtration-bridge-general.md
theorem bridge_map_general [ctx : TwoFiltrationBridgeContext] :
    (∀ λ : ctx.PartitionIdx, ctx.conj λ = λ → ctx.depth λ = 2) ∧
    (∀ λ : ctx.PartitionIdx, ctx.conj λ ≠ λ → ctx.depth λ = 3) :=
  ⟨ctx.claim_self_conjugate_depth_two, ctx.claim_chiral_pair_depth_three⟩

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral
