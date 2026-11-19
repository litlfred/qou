import QOU.Infra.Polylogarithm

/-!
# General Cl_3 orbit sum at every N

Compiled formalisation of `prop:cyclotomic-cl3-orbit-sum-general`.
Sibling docstub at `braids-and-knots/cyclotomic-cl3-orbit-sum-general.lean`.
-/

namespace QOU.BraidKnot.CyclotomicCl3OrbitSum

open QOU.Infra.Polylogarithm

/-- **The `N = 5` closed form** (the Bring / `ζ₅` row of
    `prop:cyclotomic-cl3-orbit-sum-general`): the predicted orbit sum
    evaluates to `-(24/25) · ζ(3)`.

    **Restated 2026-08-21** (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology`).  This read
    `∀ N, 2 ≤ N → cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3`,
    closed by `rfl` — both binders decoration, the claim holding for every
    `N` and every `zeta3` with or without `2 ≤ N`.  Its own docstring
    conceded the RHS "equals itself by `rfl`", yet the name promised a
    general orbit-sum identity, so a reader grepping for whether that
    identity is established found a green `theorem`.

    What is genuinely derivable here is the arithmetic at the verified
    index — the same computation `defaultTheoremB.value_at_5` performs, so
    it needs no class instance.  The **general-`N`** identification of the
    predicted closed form with the analytic orbit sum `Σ_k Cl₃(2πk/N)`
    remains conditional content, carried by `TheoremB.agrees_at`; it is
    *not* proved here and this statement does not imply it. -/
theorem orbit_sum_at_five (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 = -(24 / 25) * zeta3 := by
  unfold cl3OrbitSumPredicted
  field_simp
  ring

/-- **General-`N` cyclotomic `Cl₃` orbit-sum reduction (`prop:cyclotomic-cl3-orbit-sum-general`).**
    For any `N ≥ 2` and any orbit evaluation `cl3Orbit : Fin N → ℝ` representing
    `k ↦ Cl₃(2π k / N)` that satisfies the zero-mode value `cl3Orbit 0 = zeta3`
    and the weight-3 Kubert distribution sum
    `∑ k : Fin N, cl3Orbit k = zeta3 / (N : ℝ) ^ 2`, the primitive/non-zero orbit
    sum over `k ∈ {1, …, N - 1}` equals `cl3OrbitSumPredicted N zeta3`, and is
    strictly negative whenever `0 < zeta3`. -/
-- Ref: [zagier1986] §1; [leitner2026] prop:cyclotomic-cl3-orbit-sum-general
theorem orbit_sum_general (N : ℕ) (hN : 2 ≤ N) (zeta3 : ℝ)
    (cl3Orbit : Fin N → ℝ)
    (hzero : cl3Orbit ⟨0, by omega⟩ = zeta3)
    (hkubert : (Finset.univ.sum fun k : Fin N => cl3Orbit k) = zeta3 / (N : ℝ) ^ 2) :
    (Finset.univ.erase ⟨0, by omega⟩).sum cl3Orbit = cl3OrbitSumPredicted N zeta3 ∧
    (0 < zeta3 → (Finset.univ.erase ⟨0, by omega⟩).sum cl3Orbit < 0) := by
  have hsplit :
      cl3Orbit ⟨0, by omega⟩ + (Finset.univ.erase ⟨0, by omega⟩).sum cl3Orbit =
        Finset.univ.sum cl3Orbit :=
    Finset.add_sum_erase Finset.univ cl3Orbit (Finset.mem_univ _)
  have hN2 : (2 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
  have hN_pos : (0 : ℝ) < (N : ℝ) := lt_of_lt_of_le (by norm_num) hN2
  have hN_ne : (N : ℝ) ≠ 0 := ne_of_gt hN_pos
  have hsum : (Finset.univ.erase ⟨0, by omega⟩).sum cl3Orbit =
      zeta3 / (N : ℝ) ^ 2 - zeta3 :=
    eq_sub_of_add_eq' (by rw [← hkubert, ← hsplit, hzero])
  have heq : (Finset.univ.erase ⟨0, by omega⟩).sum cl3Orbit = cl3OrbitSumPredicted N zeta3 := by
    rw [hsum]
    unfold cl3OrbitSumPredicted
    field_simp [hN_ne]
    ring
  refine ⟨heq, fun hz => ?_⟩
  rw [heq]
  unfold cl3OrbitSumPredicted
  have hsq_gt_one : (1 : ℝ) < (N : ℝ) ^ 2 := by
    have h1 : (1 : ℝ) < (N : ℝ) := lt_of_lt_of_le (by norm_num) hN2
    exact one_lt_pow₀ h1 (by decide)
  have hnum_pos : (0 : ℝ) < ((N : ℝ) ^ 2 - 1) / (N : ℝ) ^ 2 :=
    div_pos (sub_pos.mpr hsq_gt_one) (sq_pos_of_pos hN_pos)
  have hprod_pos : (0 : ℝ) < (((N : ℝ) ^ 2 - 1) / (N : ℝ) ^ 2) * zeta3 :=
    mul_pos hnum_pos hz
  simpa [neg_mul] using neg_lt_zero.mpr hprod_pos

end QOU.BraidKnot.CyclotomicCl3OrbitSum
