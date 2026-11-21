import QOU.MassTheory.CoCasimirDimQTraces
import QOU.Mathlib.NumSYTPos

/-!
# The symmetrising trace does not descend to the surviving blocks

Convention D removes every block `λ` of `H_{n+1}(q)` with three or more rows: the Markov
weight `w_λ` at `z_D = q³/(q²+1)` is zero there (`wD_ne_zero_iff`). Call `x` **supported off the
surviving blocks** if its Wedderburn image `Ψ x` is zero on every block with at most two rows
(`OffSurviving`). These `x` form the kernel of the projection onto the surviving-block algebra.

A trace on `H_{n+1}(q)` passes to the surviving-block algebra exactly when it vanishes on that
kernel. This file compares the two traces of `CoCasimirDimQTraces`:

* `markov_eq_zero_of_offSurviving`: every Markov trace at `z_D` vanishes on the kernel, so it
  is a trace of the surviving-block algebra.
* `symTrace_primIdem_ne_zero`: the symmetrising trace `τ₀(T_w) = δ_{w,1}` is nonzero on every
  primitive idempotent, three-row blocks included, since
  `τ₀(e_{λ,i}) = q^{−κ(λ)} / ∏ [h(x)]_q` and no balanced quantum integer `[h]_q`, `h ≥ 1`,
  vanishes when `q` is not a root of unity.
* `symTrace_not_descend`: for `n + 1 ≥ 3` there is an `x` supported off the surviving blocks
  with `τ₀(x) ≠ 0`, namely a primitive idempotent of the one-column block `(1^{n+1})`.

So `τ₀` is not a trace of the surviving-block algebra for any `n + 1 ≥ 3`. The hook-formula
`dim_q`, which is `τ₀`'s per-simple weight up to `q^{−κ}`
(`qFact_mul_symTrace_primIdem_eq_dimQ`), is therefore not the quantum dimension of any block
with respect to a trace that lives on the surviving blocks. The convention-D Markov trace is such
a trace, and its per-simple weight on a two-row block `(m, k)` is the `sl₂` dimension
`[m − k + 1]_q` (`quantumDim_primIdem_twoRow`).

## What is proved and what is not

Proved: the statements above, for a generic field. Not proved, and not claimed: that every trace
of the surviving-block algebra is a multiple of the Markov trace, or that Term 4 of the mass
formula must be built from a trace of the surviving-block algebra. The second is the modelling
reading under review on issue #8109.

## Base ring (§7c)

Generic `[Field K]`, `q ≠ 0`, `q` not a root of unity. No ordering, no `ℝ`.

LaTeX label: `thm:cocasimir-tau0-not-descend`
-/

namespace QOU.MassTheory.CoCasimirHecke

open Finset QOU.SchurWeyl QOU.MassTheory.CoCasimirSurviving
open QOU.Mathlib (StandardYoungTableau partitionShape)

noncomputable section

open Classical

/-- The number of rows of a partition's Young diagram is its number of parts. -/
theorem colLen_zero_partitionShape {m : ℕ} (p : Nat.Partition m) :
    (partitionShape p).colLen 0 = Multiset.card p.parts := by
  unfold partitionShape
  rw [QOU.Mass.QHookDiagram.colLen_ofRowLens, List.filter_eq_self.mpr, Multiset.length_sort]
  intro a ha
  simpa using p.parts_pos ((Multiset.mem_sort _).mp ha)

/-- The one-column partition `(1^m)`. -/
def columnPartition (m : ℕ) : Nat.Partition m where
  parts := Multiset.replicate m 1
  parts_pos := fun h => by rw [Multiset.eq_of_mem_replicate h]; exact Nat.one_pos
  parts_sum := by simp

theorem colLen_zero_columnPartition (m : ℕ) :
    (partitionShape (columnPartition m)).colLen 0 = m := by
  rw [colLen_zero_partitionShape]
  simp [columnPartition]

variable {K : Type*} [Field K]
variable (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- `x` is supported off the surviving blocks: `Ψ x` vanishes on every block with at most two
rows. -/
def OffSurviving (x : Hecke K q q⁻¹ n) : Prop :=
  ∀ lam : Nat.Partition (n + 1), (partitionShape lam).colLen 0 ≤ 2 → Ψ q hq0 hq2 n x lam = 0

/-- **The Markov trace at `z_D` passes to the surviving blocks.** It vanishes on every element
supported off them. -/
theorem markov_eq_zero_of_offSurviving
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke K q q⁻¹ n) (hx : OffSurviving q hq0 hq2 n x) :
    T.tr n x = 0 := by
  have hq21 := GenericParameter.sq_add_one_ne_zero hq2
  have hgen := gen_of_notRootOfUnity hq2
  rw [markov_eq_tr q hq0 hq2 n hq21 hgen T]
  unfold tr
  refine Finset.sum_eq_zero fun lam _ => ?_
  by_cases h : (partitionShape lam).colLen 0 ≤ 2
  · rw [hx lam h, Matrix.trace_zero, mul_zero]
  · have : wD q n lam = 0 := by
      by_contra hw
      exact h ((wD_ne_zero_iff q hq0 n hq21 hgen lam).mp hw)
    rw [this, zero_mul]

/-- A primitive idempotent of a block with three or more rows is supported off the surviving
blocks. -/
theorem primIdem_offSurviving (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam))
    (h3 : 2 < (partitionShape lam).colLen 0) :
    OffSurviving q hq0 hq2 n (primIdem q hq0 hq2 n lam i) := by
  intro mu hmu
  have hne : mu ≠ lam := by
    rintro rfl
    omega
  unfold primIdem
  rw [AlgEquiv.apply_symm_apply, Pi.single_eq_of_ne hne]

include hq0 hq2 in
/-- No balanced quantum integer `[h]_q`, `h ≥ 1`, vanishes at a `q` that is not a root of
unity. -/
theorem qIntBal_ne_zero_of_pos {h : ℕ} (hh : 0 < h) : QOU.QInteger.qIntBal q h ≠ 0 := by
  have hgen := gen_of_notRootOfUnity hq2 (h : ℤ) (by exact_mod_cast hh.ne')
  rw [zpow_natCast] at hgen
  have hd : q - q⁻¹ ≠ 0 :=
    QOU.Mass.QHookDimensionBalanced.sub_inv_ne_zero hq0 (GenericParameter.sq_ne_one hq2)
  rw [QOU.QInteger.qIntBal_def]
  refine div_ne_zero ?_ hd
  intro h0
  apply hgen
  have hpow : q ^ h = q⁻¹ ^ h := sub_eq_zero.mp h0
  calc (q ^ 2) ^ h = q ^ h * q ^ h := by ring
    _ = q ^ h * q⁻¹ ^ h := by rw [← hpow]
    _ = 1 := by rw [← mul_pow, mul_inv_cancel₀ hq0, one_pow]

/-- **The symmetrising trace is nonzero on every primitive idempotent**, three-row blocks
included. -/
theorem symTrace_primIdem_ne_zero (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    HeckeCoset.symTrace q q⁻¹ n (primIdem q hq0 hq2 n lam i) ≠ 0 := by
  rw [symTrace_primIdem]
  refine div_ne_zero (zpow_ne_zero _ hq0) ?_
  rw [Finset.prod_ne_zero_iff]
  intro x hx
  exact qIntBal_ne_zero_of_pos q hq0 hq2 (QOU.QBeta.WenzlWeight.one_le_hook hx)

/-- Every block has a primitive idempotent: `#SYT(λ) > 0`. -/
theorem dim_pos (lam : Nat.Partition (n + 1)) : 0 < dim n lam :=
  Fintype.card_pos

/-- **The symmetrising trace does not pass to the surviving blocks** when `n + 1 ≥ 3`: some
element supported off the surviving blocks has nonzero `τ₀`. -/
theorem symTrace_not_descend (hn : 2 ≤ n) :
    ∃ x : Hecke K q q⁻¹ n, OffSurviving q hq0 hq2 n x ∧ HeckeCoset.symTrace q q⁻¹ n x ≠ 0 := by
  let lam := columnPartition (n + 1)
  have h3 : 2 < (partitionShape lam).colLen 0 := by
    rw [colLen_zero_columnPartition]
    omega
  let i : Fin (dim n lam) := ⟨0, dim_pos n lam⟩
  exact ⟨primIdem q hq0 hq2 n lam i, primIdem_offSurviving q hq0 hq2 n lam i h3,
    symTrace_primIdem_ne_zero q hq0 hq2 n lam i⟩

/-- **The two traces differ on the surviving-block quotient.** For `n + 1 ≥ 3` the symmetrising
trace is not any function of the surviving-block image: two elements with the same image (here
`x` and `0`) get different values of `τ₀`, while every Markov trace at `z_D` gives both `0`. -/
theorem symTrace_not_factor (hn : 2 ≤ n)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1))) :
    ∃ x : Hecke K q q⁻¹ n, OffSurviving q hq0 hq2 n x ∧ T.tr n x = 0
      ∧ HeckeCoset.symTrace q q⁻¹ n x ≠ 0 := by
  obtain ⟨x, hx, hτ⟩ := symTrace_not_descend q hq0 hq2 n hn
  exact ⟨x, hx, markov_eq_zero_of_offSurviving q hq0 hq2 n T x hx, hτ⟩

end

end QOU.MassTheory.CoCasimirHecke
