import QOU.BraidsAndKnots.NucleonWeightSpaceTraces

/-!
# Second-order weak terms `FE`, `EF` on the nucleon weight spaces

Setting as in `NucleonWeightSpaceTraces`: level-2 Jimbo braiding on `(C²)^{⊗3}`, the proton-type
weight space `(2,1)` and the neutron-type weight space `(1,2)`. With the coproduct
`Δ(E) = E ⊗ K + 1 ⊗ E`, `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F` (the one of the two standard coproducts that
commutes with `Ř`; probe `np_second_order_weak_fe_ef_probe.py`), the products `FE` and `EF`
preserve both weight spaces. Their restrictions are the 3×3 matrices below, in the bases of
`NucleonWeightSpaceTraces` (`FEp`, `EFp` on `(2,1)`; `FEn`, `EFn` on `(1,2)`).

Results (np-splitting audit §22):
* `FE` and `EF` commute with the braid generators on each weight space, and satisfy the
  two-root polynomials that make them sector scalars (isospin `3/2` versus `1/2`).
* The same intertwiner `P` that identifies the braid actions sends `EF` on the proton space to
  `FE` on the neutron space, and `FE` to `EF`. So, for every braid word,
  `tr(FE·w)` on the neutron space equals `tr(EF·w)` on the proton space and vice versa.
  Any insertion symmetric in `FE` and `EF` therefore has equal plain traces on the two spaces,
  and the n/p ratio of quantum traces stays exactly the `K`-weight ratio `q⁻²`.
* Taken alone, `FE` (or `EF`) does give different traces: already for the empty word they differ
  by `3`, a value independent of `q`. This is the ordering choice, not a `q`-effect.

No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces

variable {R : Type*} [Field R]

/-- `FE` on the `(2,1)` weight space. -/
def FEp (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹ ^ 2, q⁻¹, 1; q⁻¹, 1, q; 1, q, q ^ 2]
/-- `EF` on the `(2,1)` weight space. -/
def EFp (q : R) : Matrix (Fin 3) (Fin 3) R := !![1 + q⁻¹ ^ 2, q⁻¹, 1; q⁻¹, 2, q; 1, q, q ^ 2 + 1]
/-- `FE` on the `(1,2)` weight space. -/
def FEn (q : R) : Matrix (Fin 3) (Fin 3) R := !![1 + q⁻¹ ^ 2, q⁻¹, 1; q⁻¹, 2, q; 1, q, q ^ 2 + 1]
/-- `EF` on the `(1,2)` weight space. -/
def EFn (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹ ^ 2, q⁻¹, 1; q⁻¹, 1, q; 1, q, q ^ 2]

/-- The commutator `[E, F] = (K - K⁻¹)/(q - q⁻¹)` acts by `+1` on the `(2,1)` space. -/
theorem EFp_eq (q : R) : EFp q = FEp q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [EFp, FEp] <;> ring

/-- … and by `-1` on the `(1,2)` space. -/
theorem FEn_eq (q : R) : FEn q = EFn q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [FEn, EFn] <;> ring

theorem FEp_comm₁ (q : R) (hq : q ≠ 0) : FEp q * A₁ q = A₁ q * FEp q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [FEp, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem FEp_comm₂ (q : R) (hq : q ≠ 0) : FEp q * A₂ q = A₂ q * FEp q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [FEp, A₂, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem EFn_comm₁ (q : R) (hq : q ≠ 0) : EFn q * B₁ q = B₁ q * EFn q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [EFn, B₁, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem EFn_comm₂ (q : R) (hq : q ≠ 0) : EFn q * B₂ q = B₂ q * EFn q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [EFn, B₂, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- Sector scalars on the proton space: `FE` has roots `0` and `[3] = q² + 1 + q⁻²`. -/
theorem FEp_sector (q : R) (hq : q ≠ 0) :
    FEp q * (FEp q - (q ^ 2 + 1 + q⁻¹ ^ 2) • (1 : Matrix (Fin 3) (Fin 3) R)) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [FEp, Matrix.mul_apply, Fin.sum_univ_three, Matrix.sub_apply, Matrix.one_apply] <;>
    field_simp <;> ring

/-- Sector scalars on the neutron space: `EF` has the same roots `0` and `[3]`. -/
theorem EFn_sector (q : R) (hq : q ≠ 0) :
    EFn q * (EFn q - (q ^ 2 + 1 + q⁻¹ ^ 2) • (1 : Matrix (Fin 3) (Fin 3) R)) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [EFn, Matrix.mul_apply, Fin.sum_univ_three, Matrix.sub_apply, Matrix.one_apply] <;>
    field_simp <;> ring

/-- `P` sends `EF` on the proton space to `FE` on the neutron space. -/
theorem intertwine_EF_FE (q : R) (hq : q ≠ 0) : P q * EFp q = FEn q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, EFp, FEn, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `P` sends `FE` on the proton space to `EF` on the neutron space. -/
theorem intertwine_FE_EF (q : R) (hq : q ≠ 0) : P q * FEp q = EFn q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, FEp, EFn, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp

private theorem trace_conj (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (Xp Xn : Matrix (Fin 3) (Fin 3) R) (hX : P q * Xp = Xn * P q) (w : List Bool) :
    trace (Xn * word (B₁ q) (B₂ q) w) = trace (Xp * word (A₁ q) (A₂ q) w) := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  have hw : word (B₁ q) (B₂ q) w = P q * word (A₁ q) (A₂ q) w * (P q)⁻¹ := by
    rw [intertwine_word q hq w, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  have hXn : Xn = P q * Xp * (P q)⁻¹ := by
    rw [hX, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  rw [hw, hXn]
  have : P q * Xp * (P q)⁻¹ * (P q * word (A₁ q) (A₂ q) w * (P q)⁻¹)
      = P q * (Xp * word (A₁ q) (A₂ q) w) * (P q)⁻¹ := by
    simp only [Matrix.mul_assoc, ← Matrix.mul_assoc (P q)⁻¹ (P q),
      Matrix.nonsing_inv_mul _ hdet, Matrix.one_mul]
  rw [this, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hdet, Matrix.one_mul]

/-- **State-swapped traces.** For every braid word, `FE` on the neutron space has the same
plain trace as `EF` on the proton space. -/
theorem trace_FEn_eq_EFp (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (FEn q * word (B₁ q) (B₂ q) w) = trace (EFp q * word (A₁ q) (A₂ q) w) :=
  trace_conj q hq hq2 _ _ (intertwine_EF_FE q hq) w

/-- … and `EF` on the neutron space matches `FE` on the proton space. -/
theorem trace_EFn_eq_FEp (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (EFn q * word (B₁ q) (B₂ q) w) = trace (FEp q * word (A₁ q) (A₂ q) w) :=
  trace_conj q hq hq2 _ _ (intertwine_FE_EF q hq) w

/-- **Symmetric insertion.** `FE + EF` has equal plain traces on the two weight spaces for every
braid word, so it adds nothing to the `K`-weight ratio. -/
theorem trace_symmetric_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace ((FEn q + EFn q) * word (B₁ q) (B₂ q) w)
      = trace ((FEp q + EFp q) * word (A₁ q) (A₂ q) w) := by
  rw [Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
    trace_FEn_eq_EFp q hq hq2, trace_EFn_eq_FEp q hq hq2, add_comm]

/-- **Ordering matters, classically.** Taken alone, `FE` has different traces on the two spaces:
already for the empty word they differ by `3`, independent of `q`. -/
theorem trace_FE_differ (q : R) : trace (FEn q) - trace (FEp q) = 3 := by
  simp [FEn, FEp, Matrix.trace_fin_three]; ring

end QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder
