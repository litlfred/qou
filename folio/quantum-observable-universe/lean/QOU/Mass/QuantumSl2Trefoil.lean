import QOU.Mass.QuantumSl2MarkovTrace

/-!
# The `U_q(sl₂)` invariant is not constant: the trefoil at `N = 2`

The invariant of `QuantumSl2MarkovTrace` is `J(β) = θ^{−w(β)} tr(K^{⊗(n+1)} ρ_n(β))`. This file
computes it on the closure of `σ³ ∈ B₂`, the trefoil, in the fundamental colour `N = 2`
(`d = 1`), and shows that it differs from the unknot.

* `rCheck1_eq`: on `V₂ ⊗ V₂`, `Ř` is the explicit matrix `R1` (diagonal `s` on `v₀⊗v₀`,
  `v₁⊗v₁`; the block `[[0, s⁻¹], [s⁻¹, s⁻¹(q − q⁻¹)]]` on `v₀⊗v₁, v₁⊗v₀`).
* `R1_sq`: the Hecke relation `Ř² = (s − s⁻³) Ř + s⁻²`.
* `jonesSl2_trefoil`: `J(trefoil) = [2] · (q⁻² + q⁻⁶ − q⁻⁸)`, `q = s²`, `[2] = q + q⁻¹`.
  Up to the variable `t = q²` this is the Jones polynomial `t⁻¹ + t⁻³ − t⁻⁴` of a trefoil.
* `jonesSl2_unknot`: `J(unknot) = [2]`.
* `jonesSl2_trefoil_ne_unknot`: at `s = 2` over `ℚ` the two values differ, so the invariant
  separates the trefoil from the unknot and is not constant.

The trace of `σ³` is computed from the Hecke relation and the two traces the Markov moves
already give: `tr(K⊗K · 1) = [2]²` and `tr(K⊗K · Ř) = θ[2]` (positive stabilisation of the
one-strand identity).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. X.6 (the trefoil)
-/

namespace QOU.Mass.QuantumSl2.Trefoil

open Matrix
open scoped Kronecker
open QOU.Mass.QuantumSl2.BraidAction
open QOU.Mass.QuantumSl2.Markov
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.IwahoriHecke.TensorEmbed (coxA)
open QOU.IwahoriHecke.BraidGroup (BraidGroupN braidGen)
open QOU.IwahoriHecke.JonesNormalisation (writhe writhe_braidGen)
open QOU.Torsion.MassTraceMarkovClass (artinTower)
open QOU.MathlibExt.MarkovMoves

set_option linter.unusedSectionVars false

variable {𝕜 : Type*} [Field 𝕜] (s : 𝕜) (hs : s ≠ 0)

/-- `Ř` on `V₂ ⊗ V₂`, written out. -/
def R1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) 𝕜 := Matrix.of fun y x =>
  if y = x then (if y.1 = y.2 then s else if y = (1, 0) then s⁻¹ * (s ^ 2 - (s ^ 2)⁻¹) else 0)
  else if y.swap = x then s⁻¹ else 0

theorem rCheck1_eq (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) : rCheckMat s hs 1 1 = R1 s := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
  simp [R1, rCheckMat, rMat, Rep.rSum, rOrder, cartanTheta, rcoef, qfact, irrep, irrepE, irrepF,
    Finset.sum_range_succ, mul_apply, Fintype.sum_prod_type, wt, kroneckerMap_apply, qint, hq2]

include hs in
/-- **The Hecke relation** `Ř² = (s − s⁻³) Ř + s⁻²` on `V₂ ⊗ V₂`. -/
theorem R1_sq : R1 s * R1 s
    = (s - s⁻¹ ^ 3) • R1 s + s⁻¹ ^ 2 • (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) 𝕜) := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
  simp [R1, mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two]
  all_goals (try field_simp)
  all_goals first | ring1 | simp

section Linear

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι] {n : ℕ}

theorem pembed_add (i j : Fin n) (M N : Matrix (ι × ι) (ι × ι) R) :
    pembed i j (M + N) = pembed i j M + pembed i j N := by
  ext a b
  simp only [pembed_apply, add_apply]
  split_ifs <;> simp

theorem pembed_smul (i j : Fin n) (r : R) (M : Matrix (ι × ι) (ι × ι) R) :
    pembed i j (r • M) = r • pembed i j M := by
  ext a b
  simp only [pembed_apply, smul_apply]
  split_ifs <;> simp

theorem wtrace_add (c : ι → R) (A B : Matrix (Fin n → ι) (Fin n → ι) R) :
    wtrace c (A + B) = wtrace c A + wtrace c B := by
  simp [wtrace, mul_add, Finset.sum_add_distrib]

theorem wtrace_smul (c : ι → R) (r : R) (A : Matrix (Fin n → ι) (Fin n → ι) R) :
    wtrace c (r • A) = r * wtrace c A := by
  simp [wtrace, Finset.mul_sum, mul_left_comm]

end Linear

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (hint : ∀ k, 0 < k → k ≤ 2 * 1 → qint (s ^ 2) k ≠ 0)

/-- `[2] = q + q⁻¹`, the quantum dimension of `V₂`, as the sum of the weights. -/
theorem sum_qWt : ∑ r : Fin 2, qWt s 1 r = s ^ 2 + (s ^ 2)⁻¹ := by
  simp [qWt, wt, Fin.sum_univ_two, zpow_neg, zpow_ofNat]

/-- The generator `σ₀ ∈ B₂`. -/
abbrev sig : BraidGroupN 1 := braidGen (coxA 1) 0

theorem rep_sig : ((rCheckRep s hs 1 hq2 hint 1 (sig) :
    (Matrix (Fin 2 → Fin 2) (Fin 2 → Fin 2) 𝕜)ˣ) : Matrix (Fin 2 → Fin 2) (Fin 2 → Fin 2) 𝕜)
      = pembed 0 1 (R1 s) := by
  rw [rCheckRep_braidGen, strandMat, rCheck1_eq s hs hq2]
  rfl

private theorem h01 : (0 : Fin 2) ≠ 1 := by decide

include hs in
/-- `ρ(σ)² = (s − s⁻³) ρ(σ) + s⁻²`. -/
theorem rep_sig_sq :
    pembed (0 : Fin 2) 1 (R1 s) * pembed 0 1 (R1 s)
      = (s - s⁻¹ ^ 3) • pembed (0 : Fin 2) 1 (R1 s) + s⁻¹ ^ 2 • (1 : Matrix (Fin 2 → Fin 2) _ 𝕜) := by
  rw [pembed_mul h01, R1_sq s hs, pembed_add, pembed_smul, pembed_smul, pembed_one h01]

include hs hq2 hint in
/-- `tr(K⊗K · ρ(σ)) = θ [2]`, by positive stabilisation of the one-strand identity. -/
theorem wtrace_sig :
    wtrace (qWt s 1) (pembed (0 : Fin 2) 1 (R1 s)) = theta s 1 * (s ^ 2 + (s ^ 2)⁻¹) := by
  have h := qtrace_stab s hs 1 hq2 hint 0 1
  rw [qtrace_one, sum_qWt] at h
  rw [← h, ← rep_sig s hs hq2 hint]
  simp only [qtrace]
  congr 2

/-- `tr(K⊗K) = [2]²`. -/
theorem wtrace_one2 :
    wtrace (qWt s 1) (1 : Matrix (Fin 2 → Fin 2) (Fin 2 → Fin 2) 𝕜)
      = (s ^ 2 + (s ^ 2)⁻¹) ^ 2 := by
  simp only [wtrace, siteWt, one_apply_eq, mul_one]
  rw [← Fintype.prod_sum (fun (_ : Fin 2) (r : Fin 2) => qWt s 1 r), Fin.prod_univ_two, sum_qWt]
  ring

include hs in
/-- `ρ(σ)³ = ((s − s⁻³)² + s⁻²) ρ(σ) + (s − s⁻³) s⁻²`. -/
theorem rep_sig_cube :
    pembed (0 : Fin 2) 1 (R1 s) * pembed 0 1 (R1 s) * pembed 0 1 (R1 s)
      = ((s - s⁻¹ ^ 3) ^ 2 + s⁻¹ ^ 2) • pembed (0 : Fin 2) 1 (R1 s)
        + ((s - s⁻¹ ^ 3) * s⁻¹ ^ 2) • (1 : Matrix (Fin 2 → Fin 2) _ 𝕜) := by
  rw [rep_sig_sq s hs, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul, rep_sig_sq s hs]
  module

include hs hq2 hint in
/-- The quantum trace of `σ³ ∈ B₂`. -/
theorem qtrace_trefoil :
    qtrace s hs 1 hq2 hint ⟨1, sig ^ 3⟩
      = ((s - s⁻¹ ^ 3) ^ 2 + s⁻¹ ^ 2) * (theta s 1 * (s ^ 2 + (s ^ 2)⁻¹))
        + ((s - s⁻¹ ^ 3) * s⁻¹ ^ 2) * (s ^ 2 + (s ^ 2)⁻¹) ^ 2 := by
  simp only [qtrace]
  rw [map_pow, Units.val_pow_eq_pow_val, rep_sig s hs hq2 hint, pow_succ, sq, rep_sig_cube s hs,
    wtrace_add, wtrace_smul, wtrace_smul, wtrace_sig s hs hq2 hint, wtrace_one2]

theorem theta_one : theta s 1 = s ^ 3 := by
  rw [theta, show ((1 : ℕ) : ℤ) * ((1 : ℕ) + 2) = ((3 : ℕ) : ℤ) by norm_num, zpow_natCast]

theorem writhe_sig_cube :
    Multiplicative.toAdd (artinFraming.w 1 (sig ^ 3)) = 3 := by
  simp [artinFraming, map_pow, sig]

/-- **The trefoil.** `J(σ³) = [2] (q⁻² + q⁻⁶ − q⁻⁸)`, `q = s²`. -/
theorem jonesSl2_trefoil :
    normalise artinFraming (thetaU s hs 1)⁻¹ 1 (qtrace s hs 1 hq2 hint) ⟨1, sig ^ 3⟩
      = (s ^ 2 + (s ^ 2)⁻¹) * ((s ^ 2)⁻¹ ^ 2 + (s ^ 2)⁻¹ ^ 6 - (s ^ 2)⁻¹ ^ 8) := by
  rw [normalise_apply, writhe_sig_cube, qtrace_trefoil s hs hq2 hint, theta_one]
  simp only [one_pow, mul_one, Units.val_zpow_eq_zpow_val, Units.val_inv_eq_inv_val, thetaU,
    Units.val_mk0, theta_one]
  field_simp
  ring

/-- **The unknot.** `J(1 ∈ B₁) = [2]`. -/
theorem jonesSl2_unknot :
    normalise artinFraming (thetaU s hs 1)⁻¹ 1 (qtrace s hs 1 hq2 hint) ⟨0, 1⟩
      = s ^ 2 + (s ^ 2)⁻¹ := by
  rw [normalise_apply, qtrace_one, sum_qWt]
  simp [artinFraming]

/-- `s = 2` over `ℚ` satisfies the genericity hypotheses at `d = 1`. -/
theorem hq2_two : (2 : ℚ) ^ 2 - ((2 : ℚ) ^ 2)⁻¹ ≠ 0 := by norm_num

theorem hint_two : ∀ k, 0 < k → k ≤ 2 * 1 → qint ((2 : ℚ) ^ 2) k ≠ 0 := by
  intro k hk hk2
  interval_cases k <;> norm_num [qint]

/-- **The invariant is not constant.** At `s = 2` it separates the trefoil from the unknot:
`J(trefoil) = 69887/262144 ≠ 17/4 = J(unknot)`. -/
theorem jonesSl2_trefoil_ne_unknot :
    normalise artinFraming (thetaU (2 : ℚ) two_ne_zero 1)⁻¹ 1
        (qtrace (2 : ℚ) two_ne_zero 1 hq2_two hint_two) ⟨1, sig ^ 3⟩
      ≠ normalise artinFraming (thetaU (2 : ℚ) two_ne_zero 1)⁻¹ 1
        (qtrace (2 : ℚ) two_ne_zero 1 hq2_two hint_two) ⟨0, 1⟩ := by
  rw [jonesSl2_trefoil, jonesSl2_unknot]
  norm_num

end QOU.Mass.QuantumSl2.Trefoil
