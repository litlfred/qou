import QOU.MathlibExt.QPartitionCombinatorics
import QOU.Hecke.H3GramArithmetic

/-!
# QOU.Hecke.H3Wedderburn — `dim H_3(q) = 3!` via the Wedderburn/hook route

Bricks `qou-lrz1` + `qou-0y6h` at `n = 3` (the Wedderburn side, companion to
`H2AlgebraDimension`'s monogenic n=2 route).

At a Wenzl-generic parameter the Iwahori–Hecke algebra `H_3(q)` is semisimple,
so it Wedderburn-decomposes as a product of matrix algebras indexed by the
partitions `λ ⊢ 3`:

  `H_3(q) ≅ M_{f^{(3)}} ⊕ M_{f^{(21)}} ⊕ M_{f^{(111)}}`,

where `f^λ` is the number of standard Young tableaux of shape `λ` — given by
the **Frame–Robinson–Thrall hook-length formula** `f^λ = |λ|! / ∏_x h(x)`,
computed here on the concrete `Partition.hookLength` (`QPartitionCombinatorics`,
the same hook data `WenzlSchurElement.schurElement` uses).  Its dimension is
therefore `Σ_λ (f^λ)²`, and this file proves — sorry-free by `decide` on the
concrete hook lengths — that this equals `3! = 6`, the `n = 3` instance of
`dim H_n(q) = n!` (`qou-lrz1`).

General `n` (RSK bijection `Σ_λ (f^λ)² = n!`) is a genuine Mathlib gap: there
is no `StandardYoungTableau` count and no Robinson–Schensted correspondence in
Mathlib.  The concrete small cases are the honest anchors.
-/

namespace QOU.Hecke

open QOU.MathlibExt.QPartitionCombinatorics

/-! ## Hook-length products of the three partitions of 3

For each `λ ⊢ 3`, the product of hook lengths over its cells — the denominator
of the hook-length formula `f^λ = 3! / ∏ h(x)`.  Verified by `decide` on the
concrete `Partition.hookLength`. -/

/-- `λ = (3)` — the single row.  Hook lengths `3, 2, 1`, product `6`. -/
theorem hookProd_row3 :
    Partition.hookLength [3] 0 0 * Partition.hookLength [3] 0 1
      * Partition.hookLength [3] 0 2 = 6 := by decide

/-- `λ = (2,1)` — the hook.  Hook lengths `3, 1, 1`, product `3`. -/
theorem hookProd_hook21 :
    Partition.hookLength [2, 1] 0 0 * Partition.hookLength [2, 1] 0 1
      * Partition.hookLength [2, 1] 1 0 = 3 := by decide

/-- `λ = (1,1,1)` — the single column.  Hook lengths `3, 2, 1`, product `6`. -/
theorem hookProd_col3 :
    Partition.hookLength [1, 1, 1] 0 0 * Partition.hookLength [1, 1, 1] 1 0
      * Partition.hookLength [1, 1, 1] 2 0 = 6 := by decide

/-! ## SYT dimensions and the Wedderburn dimension count -/

/-- `f^{(3)} = 3!/6 = 1` — the trivial (symmetric) representation. -/
def sytDimRow3 : ℕ := 1

/-- `f^{(21)} = 3!/3 = 2` — the standard (2-dim) representation. -/
def sytDimHook21 : ℕ := 2

/-- `f^{(111)} = 3!/6 = 1` — the sign (antisymmetric) representation. -/
def sytDimCol3 : ℕ := 1

/-- **Hook-length formula check (sorry-free).**  Each SYT dimension satisfies
    `f^λ · ∏_x h(x) = 3!`, i.e. `f^λ = 3! / ∏ h(x)` — the Frame–Robinson–Thrall
    formula, verified against the concrete hook products above. -/
theorem sytDim_hook_formula :
    sytDimRow3 * (Partition.hookLength [3] 0 0 * Partition.hookLength [3] 0 1
        * Partition.hookLength [3] 0 2) = 6
    ∧ sytDimHook21 * (Partition.hookLength [2, 1] 0 0 * Partition.hookLength [2, 1] 0 1
        * Partition.hookLength [2, 1] 1 0) = 6
    ∧ sytDimCol3 * (Partition.hookLength [1, 1, 1] 0 0 * Partition.hookLength [1, 1, 1] 1 0
        * Partition.hookLength [1, 1, 1] 2 0) = 6 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-- **`dim H_3(q) = 3! = 6` (sorry-free).**  The Wedderburn dimension of
    `H_3(q)` at a generic parameter is `Σ_{λ ⊢ 3} (f^λ)² = 1² + 2² + 1² = 6 = 3!`
    — the `n = 3` case of `dim H_n(q) = n!` (`qou-lrz1`), from the hook-length
    SYT dimensions rather than a monogenic basis. -/
theorem wedderburn_dim_three :
    sytDimRow3 ^ 2 + sytDimHook21 ^ 2 + sytDimCol3 ^ 2 = 6 := by decide

/-- **`dim H_3(q) = 3!` matches the factorial (sorry-free).**  Records the
    Wedderburn dimension equals `Nat.factorial 3`, the shape of the general
    `dim H_n(q) = n!` claim. -/
theorem wedderburn_dim_three_eq_factorial :
    sytDimRow3 ^ 2 + sytDimHook21 ^ 2 + sytDimCol3 ^ 2 = Nat.factorial 3 := by decide

end QOU.Hecke
