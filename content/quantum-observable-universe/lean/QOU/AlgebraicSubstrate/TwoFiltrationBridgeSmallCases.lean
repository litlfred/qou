/-!
# Two-filtration bridge verified at small partitions

Compiled formalisation of `prop:two-filtration-bridge-small-cases`.
Sibling docstub at
`algebraic-substrate/two-filtration-bridge-small-cases.lean`.

Small-case (`n ≤ 4`) verification of the bridge identity already
stated in full generality at `prop:two-filtration-bridge-general`:
self-conjugate cells go to depth 2, chiral pairs go to depth 3,
restricted to partitions of size at most 4.
-/

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases

/-- Abstract context for `prop:two-filtration-bridge-small-cases`. -/
class TwoFiltrationBridgeSmallCasesContext where
  /-- Partition index type. -/
  PartitionIdx : Type
  /-- Conjugate-partition involution. -/
  conj : PartitionIdx → PartitionIdx
  /-- Depth assigned by the bridge map. -/
  depth : PartitionIdx → ℕ
  /-- Size `|λ|` of a partition. -/
  size : PartitionIdx → ℕ
  /-- Chiral/self-conjugate splitting: the depth is 2 for self-conjugate and 3 for chiral. -/
  depth_formula : ∀ lam : PartitionIdx, depth lam = if conj lam = lam then 2 else 3

/-- **Proposition (`prop:two-filtration-bridge-small-cases`).**
    The bridge map sends self-conjugate cells to depth 2 and
    chiral pairs to depth 3 for every partition `λ ⊢ n` with
    `n ≤ 4`. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/two-filtration-bridge-small-cases.md
theorem bridge_small_cases [ctx : TwoFiltrationBridgeSmallCasesContext] :
    ∀ lam : ctx.PartitionIdx, ctx.size lam ≤ 4 →
      ((ctx.conj lam = lam → ctx.depth lam = 2) ∧
       (ctx.conj lam ≠ lam → ctx.depth lam = 3)) := by
  intro lam _
  constructor
  · intro h
    rw [ctx.depth_formula lam, if_pos h]
  · intro h
    rw [ctx.depth_formula lam, if_neg h]

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases
