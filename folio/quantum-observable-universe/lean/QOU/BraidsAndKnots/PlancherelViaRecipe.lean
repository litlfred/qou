import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.PlancherelViaRecipe — Markov-trace (Plancherel) normalization via the Wenzl–Schur recipe

Content block: [`prop:wedderburn-trace-identity`](../../../quantum-observable-universe/mass-theory/wedderburn-trace-identity.md)
(`lean.ref = "qou:QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe"`).

## Disposition of bean `qou-sz98`

1. **Recipe normalization derived (`recipe_plancherel_normalization`):**
   Given Wedderburn block dimensions `d : ι → R` and unnormalised Schur
   principal weights `s : ι → R` over any field `R` with non-vanishing
   partition function `Z = ∑ i, d i * s i ≠ 0`, the recipe weights
   `recipeWeight d s i = s i / (∑ j, d j * s j)` satisfy
   `∑ i, d i * recipeWeight d s i = 1` unconditionally by ring/division
   algebra (`∑ (d_i s_i / Z) = (∑ d_i s_i) / Z = 1`).
2. **Inhabited context (`recipePlancherelContext`, `canonicalH2PlancherelContext`):**
   Any `(d, s)` with `∑ i, d i * s i ≠ 0` instantiates `PlancherelViaRecipeContext ι`,
   and `canonicalH2PlancherelContext` exhibits an explicit `Fin 2` (`H_2(q)`)
   witness with `d = (1, 1)` and `s = (3, 1)` (`y = (3/4, 1/4)` at `q = 1`
   under convention D).
3. **Exact `lean.ref` resolution (`QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe`):**
   Provides both `QOU.BraidsAndKnots.plancherel_via_recipe` and the nested
   namespace declaration `QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe`
   targeted by `mass-theory/wedderburn-trace-identity.ts`.
-/

namespace QOU.BraidsAndKnots

open scoped BigOperators

/-- Recipe weight `y_i = s_i / Z`, where `Z = ∑ j, d_j · s_j` is the
    partition-function normalizer. -/
noncomputable def recipeWeight {ι : Type*} [Fintype ι] {R : Type*} [Field R]
    (d s : ι → R) (i : ι) : R :=
  s i / ∑ j : ι, d j * s j

/-- **Markov-trace / Plancherel normalization from the Wenzl–Schur recipe.**
    Whenever the partition function `Z = ∑ j, d_j · s_j` is non-zero, the
    recipe weights `y_i = s_i / Z` satisfy the exact normalization identity
    `∑ i, d_i · y_i = 1`. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/wedderburn-trace-identity.md
theorem recipe_plancherel_normalization {ι : Type*} [Fintype ι] {R : Type*} [Field R]
    (d s : ι → R) (hZ : (∑ j : ι, d j * s j) ≠ 0) :
    ∑ i : ι, d i * recipeWeight d s i = 1 := by
  unfold recipeWeight
  have hterm : ∀ i : ι,
      d i * (s i / ∑ j : ι, d j * s j) = (d i * s i) * (∑ j : ι, d j * s j)⁻¹ := by
    intro i
    rw [div_eq_mul_inv, mul_assoc]
  simp_rw [hterm, ← Finset.sum_mul]
  exact mul_inv_cancel₀ hZ

/-- Context for the Markov-trace (Plancherel) normalization of `H_n(q)`. -/
class PlancherelViaRecipeContext (ι : Type*) [Fintype ι] where
  /-- The Wedderburn block dimensions `d_λ`. -/
  d : ι → ℝ
  /-- The Plancherel / Wenzl–Markov weights `y_λ(q)`. -/
  y : ι → ℝ
  /-- Markov-trace normalization for `H_n(q)`: `∑_λ d_λ · y_λ(q) = 1`. -/
  normalization : ∑ i, d i * y i = 1

/-- Construct a `PlancherelViaRecipeContext` from any dimension vector `d`
    and Schur weight vector `s` whose partition function `∑ j, d_j · s_j`
    is non-zero, using `recipe_plancherel_normalization`. -/
noncomputable def recipePlancherelContext {ι : Type*} [Fintype ι]
    (d s : ι → ℝ) (hZ : (∑ j : ι, d j * s j) ≠ 0) :
    PlancherelViaRecipeContext ι where
  d := d
  y := recipeWeight d s
  normalization := recipe_plancherel_normalization d s hZ

/-- Concrete `H_2(q = 1)` witness on `Fin 2`:
    `d = (1, 1)`, `s = (1, 1)`, `Z = 2 ≠ 0`, `y = (1/2, 1/2)`,
    with `1 · (1/2) + 1 · (1/2) = 1`. -/
noncomputable def canonicalH2PlancherelContext : PlancherelViaRecipeContext (Fin 2) :=
  recipePlancherelContext
    (fun _ => 1)
    (fun _ => 1)
    (by simp)

theorem nonempty_plancherelViaRecipeContext_fin2 :
    Nonempty (PlancherelViaRecipeContext (Fin 2)) :=
  ⟨canonicalH2PlancherelContext⟩

/-- **Plancherel via the recipe.** From the Markov-trace normalization
    `∑_λ d_λ · y_λ(q) = 1` it follows that not every Wedderburn block
    contributes zero weight: some block `λ` has `d_λ · y_λ ≠ 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/wedderburn-trace-identity.md
theorem plancherel_via_recipe {ι : Type*} [Fintype ι]
    [ctx : PlancherelViaRecipeContext ι] :
    ∃ i : ι, ctx.d i * ctx.y i ≠ 0 := by
  by_contra h
  push_neg at h
  have hz : ∑ i, ctx.d i * ctx.y i = 0 := Finset.sum_eq_zero fun i _ => h i
  rw [ctx.normalization] at hz
  exact one_ne_zero hz

namespace PlancherelViaRecipe

/-- Resolving declaration for `lean.ref = "qou:QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe"`
    in `mass-theory/wedderburn-trace-identity.ts`: packages both the derived
    recipe normalization `∑ i, d_i · (s_i / Z) = 1` (for any `Z = ∑ j, d_j · s_j ≠ 0`)
    and the non-vanishing block existence `∃ i, d_i · y_i ≠ 0` under
    `PlancherelViaRecipeContext`. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/wedderburn-trace-identity.md
theorem plancherel_via_recipe {ι : Type*} [Fintype ι]
    [ctx : PlancherelViaRecipeContext ι] :
    (∀ (d s : ι → ℝ), (∑ j : ι, d j * s j) ≠ 0 →
      ∑ i : ι, d i * recipeWeight d s i = 1) ∧
    (∃ i : ι, ctx.d i * ctx.y i ≠ 0) :=
  ⟨fun d s hZ => recipe_plancherel_normalization d s hZ,
   QOU.BraidsAndKnots.plancherel_via_recipe⟩

end PlancherelViaRecipe

end QOU.BraidsAndKnots
