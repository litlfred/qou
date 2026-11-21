import QOU.MathlibExt.QPlancherel
import QOU.MathlibExt.NormalizedSumUnconditional

/-!
# QOU.MathlibExt.QPlancherelPartitionInstance — a genuine q-Plancherel instance

`QOU.MathlibExt.QPlancherel` packages the q-Plancherel measure behind two classes,
`QDimension` and `HasPartitionFunction`. Until this file the **only** inhabitants of
those classes in the corpus were the one-block toy witnesses `unitQDimension` and
`badPartitionFunction` over `Fin 1`, which exist to show that `Z_pos` alone does not
give total mass one (bean `qou-ltwg`, M4 of epic `qou-dxbw`: both carriers are listed
`TOY_ONLY_INSTANCE`).

This file supplies the real one.

* **Index type.** `Partitions := Σ n, Nat.Partition n`, Mathlib's partitions of every
  size; the level-`k` block is the `Finset` `levelSet k`.
* **q-dimension.** `partitionQDimension q` sends `p ⊢ n` to the hook-length
  q-dimension `qDim q λ_p = [n]_q! / ∏_x [h_x]_q` of
  `QPartitionCombinatorics`, with `λ_p = toList p`. It is defined over a generic
  `[Field R]` (AGENTS.md §7c).
* **Partition function.** `qPlancherelZ q k = Σ_{p ⊢ k} qDim q λ_p ²` is a
  *definition*, and `qPlancherelZ_eq_on` shows it is literally the constructed
  `qPartitionFunctionOn (levelSet k)` of `QPlancherel` §3.
* **Positivity is derived, not assumed.** For `1 < q`, `qPlancherelZ_pos` proves
  `0 < Z_q(k)` for every `k`. The input is the proved general-`n` Molien identity
  `NormalizedSumUnconditional.molienSum_eq_qFactorial`: since
  `Σ_p f_p q^{-κ_p} qDim q λ_p = [k]_q! ≠ 0`, some `qDim q λ_p` is nonzero, so the sum
  of squares is positive. No hook-length positivity lemma is needed.
* **Total mass one.** `sum_measure_eq_one` discharges, for this instance, the exact
  hypothesis `hZ` that `QPlancherel.sum_measure_eq_one_of_Z_eq_sum` isolates as the gap
  in the opaque framework: here `Z k` *is* the sum of squares over the level set, so
  §1's `measure` is a probability measure on the partitions of `k`.

## What this does NOT claim

* The normaliser here is `Σ_λ d_q(λ)²`, the self-normalised family that
  `QPlancherel` §1 defines. It is **not** `[n]_q!`: the two differ at `q ≠ 1`
  (the `Z(n)` defect recorded in `QPlancherel` §3). Nothing here says which
  normaliser the physics wants; for the Φ_k weight the owner-ruled family is Molien
  (bean `qou-oots`), which is a different object.
* Nothing here touches `HasQPlancherelCLT` (Féray–Méliot); that class stays
  uninstantiated.

-- Ref: [feray2010] V. Féray, P.-L. Méliot, *Asymptotics of q-Plancherel measures*,
--   PTRF 152 (2012) — the measure `d_q(λ)²/Z`; the CLT is not used here.
-- Ref: [macdonald1995] I.3 — hook-length formula for `d_q`.
-/

namespace QOU.MathlibExt.QPlancherelPartitionInstance

open QOU.MathlibExt.QPlancherel
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.MathlibExt.MolienFakeDegreeGeneralN
open QOU.Mathlib.PartitionListBridge (toList)

/-- All integer partitions, of every size. -/
abbrev Partitions : Type := Σ n : ℕ, Nat.Partition n

/-- The partitions of `k`, as a `Finset` of `Partitions`. -/
def levelSet (k : ℕ) : Finset Partitions :=
  (Finset.univ : Finset (Nat.Partition k)).map ⟨Sigma.mk k, sigma_mk_injective⟩

theorem mem_levelSet {k : ℕ} (p : Nat.Partition k) : (⟨k, p⟩ : Partitions) ∈ levelSet k := by
  simp [levelSet]

section Generic

variable {R : Type*} [Field R]

/-- **The hook-length q-dimension on partitions**: `p ⊢ n ↦ qDim q (toList p)`.
    Generic `[Field R]` (§7c). Supplied as a `def` because it depends on `q`. -/
noncomputable def partitionQDimension (q : R) : QDimension Partitions R :=
  ⟨fun p => qDim q (toList p.2)⟩

/-- **The q-Plancherel partition function** `Z_q(k) = Σ_{p ⊢ k} d_q(p)²`, as a definition. -/
noncomputable def qPlancherelZ (q : R) (k : ℕ) : R :=
  ∑ p : Nat.Partition k, qDim q (toList p) ^ 2

/-- `qPlancherelZ` is exactly the constructed `qPartitionFunctionOn` of the level set. -/
theorem qPlancherelZ_eq_on (q : R) (k : ℕ) :
    letI := partitionQDimension q
    qPartitionFunctionOn (Λ' := Partitions) (R' := R) (levelSet k) = qPlancherelZ q k := by
  letI := partitionQDimension q
  simp [qPartitionFunctionOn, levelSet, qPlancherelZ, partitionQDimension]

end Generic

/-! ## Positivity, derived from the Molien identity (`1 < q`, archimedean) -/

/-- **Some partition of `k` has nonvanishing q-dimension**, for every `k` and `1 < q`.

    Derived from the proved general-`n` Molien identity: if every `qDim q λ_p` vanished,
    the Molien sum would be `0`, but it equals `[k]_q! ≠ 0`. -/
theorem exists_qDim_ne_zero (k : ℕ) {q : ℝ} (hq : 1 < q) :
    ∃ p : Nat.Partition k, qDim q (toList p) ≠ 0 := by
  by_contra h
  push_neg at h
  have h0 : molienSum k q = 0 := by
    unfold molienSum
    exact Finset.sum_eq_zero (fun p _ => by rw [h p, mul_zero])
  rw [QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial k q hq] at h0
  exact qFactorial_ne_zero hq k h0

/-- **`0 < Z_q(k)`** for every `k`, at `1 < q` — the `Z_pos` field, proved. -/
theorem qPlancherelZ_pos (k : ℕ) {q : ℝ} (hq : 1 < q) : 0 < qPlancherelZ q k := by
  obtain ⟨p, hp⟩ := exists_qDim_ne_zero k hq
  exact Finset.sum_pos' (fun i _ => sq_nonneg _)
    ⟨p, Finset.mem_univ _, pow_two_pos_of_ne_zero hp⟩

/-- **The genuine `HasPartitionFunction` instance**: `Z = qPlancherelZ q`, with `Z_pos`
    discharged by `qPlancherelZ_pos` rather than postulated. -/
noncomputable def partitionPartitionFunction {q : ℝ} (hq : 1 < q) :
    HasPartitionFunction Partitions ℝ :=
  ⟨qPlancherelZ q, fun k => qPlancherelZ_pos k hq⟩

/-- **Total mass one for the genuine q-Plancherel measure.** For `1 < q` and every `k`,
    `Σ_{p ⊢ k} d_q(p)² / Z_q(k) = 1`, with §1's `measure` built from the two genuine
    instances above. This is `QPlancherel.sum_measure_eq_one_of_Z_eq_sum` with its `hZ`
    hypothesis discharged — the step the `Fin 1` toy shows cannot come from `Z_pos`. -/
theorem sum_measure_eq_one {q : ℝ} (hq : 1 < q) (k : ℕ) :
    letI := partitionQDimension q
    letI := partitionPartitionFunction hq
    ∑ lam ∈ levelSet k, measure (R := ℝ) (Λ := Partitions) lam k = 1 := by
  letI := partitionQDimension q
  letI := partitionPartitionFunction hq
  have hZ : qPartitionFunctionOn (Λ' := Partitions) (R' := ℝ) (levelSet k)
      = qPlancherelZ q k := qPlancherelZ_eq_on q k
  exact sum_measure_eq_one_of_Z_eq_sum (levelSet k) k hZ.symm
    (by rw [hZ]; exact (qPlancherelZ_pos k hq).ne')

/-- **Non-vacuity at level `k`.** Under the genuine instances, some partition of `k`
    carries strictly positive q-Plancherel weight — so the measure is not the zero
    function and the level set is not empty. -/
theorem exists_measure_pos {q : ℝ} (hq : 1 < q) (k : ℕ) :
    letI := partitionQDimension q
    letI := partitionPartitionFunction hq
    ∃ lam ∈ levelSet k, 0 < measure (R := ℝ) (Λ := Partitions) lam k := by
  letI := partitionQDimension q
  letI := partitionPartitionFunction hq
  obtain ⟨p, hp⟩ := exists_qDim_ne_zero k hq
  refine ⟨⟨k, p⟩, mem_levelSet p, ?_⟩
  exact div_pos (pow_two_pos_of_ne_zero hp) (qPlancherelZ_pos k hq)

end QOU.MathlibExt.QPlancherelPartitionInstance
