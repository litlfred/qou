import QOU.SchurWeyl.MarkovNormalisation
import QOU.SchurWeyl.SeminormalCornerTrace
import QOU.SchurWeyl.MarkovTraceUnique

/-!
# QOU.SchurWeyl.MarkovTraceInstance — the Ocneanu weight *is* the Markov trace

This is where the tranche closes.  `MarkovConventionD` and `MarkovNormalisation` proved the two
defining properties of the weight; `MarkovTraceUnique` proved that a Markov trace is determined by
its parameter, but **about an abstract structure with no instance**.  This file builds the
instance and draws the conclusion:

```
ocneanuMarkovTrace : MarkovTraceFamily ℝ q q⁻¹ (q³/(q²+1))
eq_wtrace_of_markov : ∀ T : MarkovTraceFamily ℝ q q⁻¹ (q³/(q²+1)), ∀ n x, T.tr n x = wtrace … n x
```

**Every** Markov trace on the Hecke tower with parameter `z_D` is the Ocneanu-weighted seminormal
trace.  That is the statement `QOU/QBeta/WenzlWeightVanishing.lean` cites Wenzl for, and at
convention D it is now proved rather than cited.

## The two properties this file adds

`wtrace` is `x ↦ ∑_{|ν| = n+1} W_ν · tr(ρ_ν x)`, as a bundled `→ₗ[ℝ]`.  Two of the four
`MarkovTraceFamily` fields were already proved elsewhere (`markov_conventionD`,
`sum_dim_weight_eq_one`); the other two are here:

* **cyclicity** — `seminormalRep` is an `AlgHom`, so this is `Matrix.trace_mul_comm` blockwise.
* **consistency** `tr_{n+1}(ι x) = tr_n x` — the corner decomposition once more, *without* the `σ`
  factor.  `trace_eq_sum_compress` splits the diagonal sum over the corners (no block hypothesis
  needed — the trace is a sum over `SYT μ` and `branchEquiv` is a bijection onto it),
  `compress_seminormalRep_heckeIncl` identifies each block with the downstairs matrix, and
  `ocneanuWeight_addable_sum` closes the reindexed weight sum.

## Scope — read before quoting this

* **Convention D only.**  `z = q³/(q²+1)`.  Nothing here says anything about other `z`.
* **Hypotheses:** `q ≠ 0`, `q² ≠ 1`, `q² + 1 ≠ 0`, and the genericity condition
  `∀ i > 0, (q²)^i ≠ 1` — i.e. `q²` is not a root of unity.  At a root of unity `H_n(q)` is not
  semisimple and partitions stop indexing the irreducibles, so the statement would need a
  different formulation, not a better proof.
* The uniqueness half is generic `[CommRing K]`; only the instance is `ℝ`-specific.

## Base ring (§7c)

`ℝ`, inherited from `seminormalRep` and `seminormalParam`.

LaTeX label: `thm:markov-trace-instance`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

variable {μ : YoungDiagram}

variable {μ : YoungDiagram}

/-- **The diagonal sum splits over the corners.**  No block hypothesis is needed: the trace is a
sum over `SYT μ`, and `branchEquiv` is a bijection onto it. -/
theorem trace_eq_sum_compress (hμ : 0 < μ.cells.card)
    (X : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) :
    X.trace = ∑ c : {c : ℕ × ℕ // IsCornerCell μ c}, (compress c.1 c.2 X).trace := by
  classical
  rw [Matrix.trace]
  simp only [Matrix.diag_apply]
  rw [← Equiv.sum_comp (branchEquiv (μ := μ) hμ) (fun T => X T T), Fintype.sum_sigma]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Matrix.trace]
  simp only [Matrix.diag_apply]
  rfl


/-- The weighted seminormal trace at convention D. -/
noncomputable def wtrace (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Hecke ℝ q q⁻¹ n →ₗ[ℝ] ℝ where
  toFun x := ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace
  map_add' x y := by
    simp only [map_add, Matrix.trace_add, mul_add]
    exact Finset.sum_add_distrib
  map_smul' c x := by
    simp only [map_smul, Matrix.trace_smul, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]
    exact Finset.sum_congr rfl fun ν _ => by ring

theorem wtrace_apply (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    wtrace q hq0 hq2 n x = ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace := rfl

theorem wtrace_cyclic (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (x y : Hecke ℝ q q⁻¹ n) :
    wtrace q hq0 hq2 n (x * y) = wtrace q hq0 hq2 n (y * x) := by
  rw [wtrace_apply, wtrace_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [map_mul, map_mul, Matrix.trace_mul_comm]

theorem wtrace_one (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    wtrace q hq0 hq2 n 1 = 1 := by
  rw [wtrace_apply]
  have key : ∀ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1
          * ((seminormalRep q hq0 hq2 n ν.2) 1).trace
        = (numStandardYoungTableaux ν.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 := by
    intro ν
    rw [map_one, Matrix.trace_one, numStandardYoungTableaux, Nat.card_eq_fintype_card]
    ring
  rw [Finset.sum_congr rfl fun ν _ => key ν]
  exact sum_dim_weight_eq_one q hq0 hq21 hgen (n + 1)


theorem seminormalRep_last (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {m : ℕ}
    {μ : YoungDiagram} (hN : μ.cells.card = m + 2) :
    seminormalRep q hq0 hq2 (m + 1) hN (Hecke.σ ℝ q q⁻¹ (m + 1) (Fin.last m))
      = genMat q (m + 1) (by omega) (by omega) := by
  rw [seminormalRep_σ]
  rfl

theorem wtrace_markov (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) (y : Hecke ℝ q q⁻¹ m) :
    wtrace q hq0 hq2 (m + 1)
        (heckeIncl ℝ q q⁻¹ m y * Hecke.σ ℝ q q⁻¹ (m + 1) (Fin.last m))
      = (q ^ 3 / (q ^ 2 + 1)) * wtrace q hq0 hq2 m y := by
  rw [wtrace_apply, wtrace_apply]
  rw [← markov_conventionD q hq0 hq2 hq21 hgen y]
  refine Finset.sum_congr rfl fun L _ => ?_
  rw [map_mul, seminormalRep_last q hq0 hq2 L.2]

theorem wtrace_incl (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) (y : Hecke ℝ q q⁻¹ m) :
    wtrace q hq0 hq2 (m + 1) (heckeIncl ℝ q q⁻¹ m y) = wtrace q hq0 hq2 m y := by
  classical
  rw [wtrace_apply, wtrace_apply]
  set F : {ν : YoungDiagram // ν.cells.card = m + 1} → (ℕ × ℕ) → ℝ :=
    fun ν c => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCellOrSelf ν.1 c)
      * (seminormalRep q hq0 hq2 m ν.2 y).trace with hF
  have step : ∀ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
          * (seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y)).trace
        = ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := by
    intro L
    have hpos : 0 < L.1.cells.card := by rw [L.2]; omega
    rw [trace_eq_sum_compress hpos, Finset.mul_sum]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [hF]
    have hadd : addCellOrSelf (eraseCorner L.1 c.1 c.2) c.1 = L.1 := by
      rw [addCellOrSelf_of (isAddableCell_eraseCorner c.1 c.2), addCell_eraseCorner]
    simp only [hadd]
    rw [compress_seminormalRep_heckeIncl hq0 hq2 m L.2 c.1 c.2
      (card_eraseCorner_of_card c.1 c.2 L.2) y]
  calc ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
          * (seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y)).trace
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := Finset.sum_congr rfl fun L _ => step L
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, F ν s.1 :=
        sum_corner_eq_sum_addable (m + 1) F
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1
            * (seminormalRep q hq0 hq2 m ν.2 y).trace := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [hF]
        simp only
        rw [← Finset.sum_mul, ← ocneanuWeight_addable_sum q hq0 hq21 hgen ν.1]
        congr 1
        exact Finset.sum_congr rfl fun s _ => by rw [addCellOrSelf_of s.2]


/-- **The Ocneanu weight defines a Markov trace on the Hecke tower**, at convention D. -/
noncomputable def ocneanuMarkovTrace (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) :
    HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)) where
  tr := wtrace q hq0 hq2
  tr_one := wtrace_one q hq0 hq2 hq21 hgen
  tr_cyclic := wtrace_cyclic q hq0 hq2
  tr_incl := wtrace_incl q hq0 hq2 hq21 hgen
  tr_markov := wtrace_markov q hq0 hq2 hq21 hgen

/-- **The identification.**  *Every* Markov trace on the Hecke tower with parameter `z_D` is the
Ocneanu-weighted seminormal trace. -/
theorem eq_wtrace_of_markov (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = wtrace q hq0 hq2 n x :=
  HeckeCoset.markovTrace_unique T (ocneanuMarkovTrace q hq0 hq2 hq21 hgen) n x


end SeminormalRep
end QOU.SchurWeyl
