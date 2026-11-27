import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi
import QOU.FluidDynamics.q_ns_block_ladder

/-!
# QOU.FluidDynamics.q_ns_haar_field_invariance — `h ∘ X₊ = 0` and `h ∘ X₋ = 0` on the
# blocks that the integration by parts uses

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), triad front.

The off-diagonal fields `X₊`, `X₋` of `OqSU2OffDiagonal` move torus weight. The Haar state
reads only weight zero. So `h(X₊ x) = 0` is automatic unless `X₊ x` has weight zero, and
`h(X₋ x) = 0` is automatic unless `X₋ x` has weight zero. This file proves both on every
block where `X₊ x` or `X₋ x` can land in weight zero, among the blocks the corpus has:

| `x` in | `X₊ x` in | `h(X₊ x) = 0` | `X₋ x` in | `h(X₋ x) = 0` |
|---|---|---|---|---|
| `K[ζ]` | `αγ · K[ζ]` | weight (`haarState_fieldPlus_ev`) | `βδ · K[ζ]` | weight (`haarState_fieldMinus_ev`) |
| `βδ · K[ζ]` | `K[ζ]` | `h(L ζ^{k+1}) = 0` (`haarState_fieldPlus_ev_betaDelta`) | — | — |
| `αγ · K[ζ]` | — | — | `K[ζ]` | moment identity (`haarState_fieldMinus_ev_alphaGamma`) |

Here `ζ = βγ`. The `βδ` row uses that `ζ^k βδ` is a multiple of `X₋ ζ^{k+1}`, so
`h(X₊(ζ^k βδ))` is a multiple of `h(L ζ^{k+1})`, which is zero (`haarState_lap_const`).
The `αγ` row is a direct computation with the Jackson moments `h(ζ^m) = (−q)^m/[m+1]_{q²}`,
using `βδ · αγ = ζ + q⁻¹ ζ²` (`betaDelta_alphaGamma`).

Hypotheses. `hq1 : (q : K) ≠ 1` is used only to make a torus automorphism act on the
weight vectors `αγ`, `βδ` by a scalar other than `1`. `hq : ∀ n, qSqNum q n ≠ 0` is the
nonvanishing of `[n+1]_{q²}` that every Haar moment needs.

## Not established

* `h ∘ X₊ = 0` on the whole algebra is **not proved in this file**. It is now proved in
  `q_ns_haar_field_invariance_full` (`haarState_fieldPlus_eq_zero`,
  `haarState_fieldMinus_eq_zero`, for `q` not a root of unity), from the PBW basis of
  `CompactQuantumMetrics.OqSU2PBW` and the block lemmas below. The full invariance
  `(id ⊗ h)Δ = h(·)1` is still open.
  The rows above are exactly the blocks that `q_ns_block_weight_lap` and
  `q_ns_block_ladder` produce at block index `0` and `±1`.
* The blocks `(αγ)^s K[ζ]`, `(βδ)^s K[ζ]` for `s ≥ 2`, whose image under `X∓` has weight
  `±2(s − 1) ≠ 0` and so pairs to zero for the same weight reason; that is not stated here.
* Any link to the q-NS advection term: the corpus defines no `∇_q` on `O_q(SU(2))`.

Everything is algebraic, so the file stays out of `QOU/Transcendental/`. No empirical
value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the relations and Haar state of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.HaarFieldInvariance

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.BlockLadder

variable {K : Type*} [Field K] (q : Kˣ)

/-! ## Weight: the Haar state kills `αγ · K[ζ]` and `βδ · K[ζ]` -/

theorem torus_alphaGamma (u b : Kˣ) :
    torusScaleAlgHom q u b (α q * γ q) = ((u : K) * ((b⁻¹ : Kˣ) : K)) • (α q * γ q) := by
  simp only [map_mul, torusScaleAlgHom, liftQuadruple_alpha, liftQuadruple_gamma,
    smul_mul_smul_comm]

theorem torus_betaDelta (u b : Kˣ) :
    torusScaleAlgHom q u b (β q * δ q) = ((b : K) * ((u⁻¹ : Kˣ) : K)) • (β q * δ q) := by
  simp only [map_mul, torusScaleAlgHom, liftQuadruple_beta, liftQuadruple_delta,
    smul_mul_smul_comm]

/-- `h(ζ^m · αγ) = 0` for `q ≠ 1`: `αγ` has nonzero torus weight. -/
theorem haarState_zeta_pow_alphaGamma (hq1 : (q : K) ≠ 1) (m : ℕ) :
    haarState q (zetaB q ^ m * (α q * γ q)) = 0 := by
  have h := haarState_torus q q 1 (zetaB q ^ m * (α q * γ q))
  rw [map_mul, map_pow, torus_zeta, torus_alphaGamma, mul_smul_comm, map_smul,
    smul_eq_mul] at h
  have h' : ((q : K) - 1) * haarState q (zetaB q ^ m * (α q * γ q)) = 0 := by
    simp only [inv_one, Units.val_one, mul_one] at h
    linear_combination h
  exact (mul_eq_zero.1 h').resolve_left (sub_ne_zero.2 hq1)

/-- `h(ζ^m · βδ) = 0` for `q ≠ 1`: `βδ` has nonzero torus weight. -/
theorem haarState_zeta_pow_betaDelta (hq1 : (q : K) ≠ 1) (m : ℕ) :
    haarState q (zetaB q ^ m * (β q * δ q)) = 0 := by
  have h := haarState_torus q 1 q (zetaB q ^ m * (β q * δ q))
  rw [map_mul, map_pow, torus_zeta, torus_betaDelta, mul_smul_comm, map_smul,
    smul_eq_mul] at h
  have h' : ((q : K) - 1) * haarState q (zetaB q ^ m * (β q * δ q)) = 0 := by
    simp only [inv_one, Units.val_one, mul_one] at h
    linear_combination h
  exact (mul_eq_zero.1 h').resolve_left (sub_ne_zero.2 hq1)

/-! ## The Cartan block `K[ζ]` -/

theorem haarState_fieldPlus_zeta_pow (hq1 : (q : K) ≠ 1) (k : ℕ) :
    haarState q (fieldPlus q (zetaB q ^ k)) = 0 := by
  rcases k with _ | k
  · rw [pow_zero, fieldPlus_one, map_zero]
  · rw [fieldPlus_zeta_pow, map_smul, haarState_zeta_pow_alphaGamma q hq1, smul_zero]

theorem haarState_fieldMinus_zeta_pow (hq1 : (q : K) ≠ 1) (k : ℕ) :
    haarState q (fieldMinus q (zetaB q ^ k)) = 0 := by
  rcases k with _ | k
  · rw [pow_zero, fieldMinus_one, map_zero]
  · rw [fieldMinus_zeta_pow, map_smul, haarState_zeta_pow_betaDelta q hq1, smul_zero]

/-- **`h ∘ X₊ = 0` on `K[ζ]`.** -/
theorem haarState_fieldPlus_ev (hq1 : (q : K) ≠ 1) (P : Polynomial K) :
    haarState q (fieldPlus q (ev q P)) = 0 := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => rw [map_add, map_add, map_add, h₁, h₂, add_zero]
  | monomial n c =>
    rw [ev_monomial, map_smul, map_smul, haarState_fieldPlus_zeta_pow q hq1, smul_zero]

/-- **`h ∘ X₋ = 0` on `K[ζ]`.** -/
theorem haarState_fieldMinus_ev (hq1 : (q : K) ≠ 1) (P : Polynomial K) :
    haarState q (fieldMinus q (ev q P)) = 0 := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => rw [map_add, map_add, map_add, h₁, h₂, add_zero]
  | monomial n c =>
    rw [ev_monomial, map_smul, map_smul, haarState_fieldMinus_zeta_pow q hq1, smul_zero]

/-! ## The block `βδ · K[ζ]`: `h ∘ X₊ = 0` from `h(L ζ^{k+1}) = 0` -/

theorem haarState_fieldPlus_zeta_pow_betaDelta (hq : ∀ n, qSqNum q n ≠ 0) (k : ℕ) :
    haarState q (fieldPlus q (zetaB q ^ k * (β q * δ q))) = 0 := by
  have hc : jk ((((q⁻¹ : Kˣ) : K)) * ((q⁻¹ : Kˣ) : K)) (k + 1) ≠ 0 := by
    rw [jk_inv_eq, ← qSqNum_eq_jk]
    exact mul_ne_zero (pow_ne_zero _ (by simp [q.ne_zero])) (hq k)
  have h := haarState_lap_const q hq (k + 1)
  rw [lap_apply, fieldMinus_zeta_pow, map_smul, map_smul, smul_eq_mul] at h
  exact (mul_eq_zero.1 h).resolve_left hc

/-- **`h ∘ X₊ = 0` on `βδ · K[ζ]`.** -/
theorem haarState_fieldPlus_ev_betaDelta (hq : ∀ n, qSqNum q n ≠ 0) (P : Polynomial K) :
    haarState q (fieldPlus q (ev q P * (β q * δ q))) = 0 := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => rw [map_add, add_mul, map_add, map_add, h₁, h₂, add_zero]
  | monomial n c =>
    rw [ev_monomial, smul_mul_assoc, map_smul, map_smul,
      haarState_fieldPlus_zeta_pow_betaDelta q hq, smul_zero]

/-! ## The block `αγ · K[ζ]`: `h ∘ X₋ = 0` from the Jackson moments -/

/-- `βδ · αγ = ζ + q⁻¹ ζ²`. -/
theorem betaDelta_alphaGamma :
    (β q * δ q) * (α q * γ q) =
      zetaB (R := K) q + (((q⁻¹ : Kˣ) : K)) • (zetaB q * zetaB q) := by
  have hda : δ q * α q = 1 + (((q⁻¹ : Kˣ) : K)) • zetaB (R := K) q := by
    rw [← rel_det_right q]; simp [zetaB]
  have hb : β q * zetaB (R := K) q * γ q = zetaB q * zetaB q := by
    simp only [zetaB, mul_assoc]
    rw [← mul_assoc (γ q) (β q), ← rel_bg, mul_assoc]
  calc β q * δ q * (α q * γ q) = β q * (δ q * α q) * γ q := by simp only [mul_assoc]
    _ = _ := by
      rw [hda, mul_add, add_mul, mul_one, mul_smul_comm, smul_mul_assoc, hb]
      rfl

theorem haarState_fieldMinus_zeta_pow_alphaGamma (hq : ∀ n, qSqNum q n ≠ 0) (k : ℕ) :
    haarState q (fieldMinus q (zetaB q ^ k * (α q * γ q))) = 0 := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  obtain ⟨ta, -, tg, -⟩ := field_twist_generators (R := K) q
  have htw : torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (α q * γ q) =
      ((((q⁻¹ : Kˣ) : K)) * ((q⁻¹ : Kˣ) : K)) • (α q * γ q) := by
    rw [map_mul, ta, tg, smul_mul_smul_comm]
  rw [field_leibniz, htw, fieldMinus_alphaGamma]
  rcases k with _ | m
  · rw [pow_zero, fieldMinus_one, zero_mul, zero_add, one_mul, map_add, map_smul,
      haarState_one, smul_eq_mul, ← pow_one (zetaB q), haarState_zetaB_pow]
    have h1 := hq 1
    simp only [haarMoment, qSqNum, Finset.sum_range_succ, qi_eq_inv] at h1 ⊢
    field_simp
    simp at h1 ⊢
    field_simp at h1 ⊢
    ring
  · have hJ1 := hq m
    have hJ2 := hq (m + 1)
    have hJ3 := hq (m + 2)
    rw [fieldMinus_zeta_pow, smul_mul_assoc, mul_smul_comm, smul_smul, mul_assoc,
      betaDelta_alphaGamma, mul_add, mul_add, mul_smul_comm, mul_smul_comm, mul_one]
    simp only [← mul_assoc, ← pow_succ]
    have hinv := jk_inv_eq q m
    rw [qi_eq_inv, ← mul_inv, inv_pow, mul_inv] at hinv
    simp only [map_add, map_smul, smul_eq_mul, haarState_zetaB_pow, haarMoment, qSqNum_eq_jk,
      qi_eq_inv] at hJ1 hJ2 hJ3 ⊢
    rw [hinv]
    rw [show m + 1 + 1 = m + 2 from rfl] at *
    rw [show m + 2 + 1 = m + 3 from rfl] at *
    have e2 : jk ((q : K) * q) (m + 2) = jk ((q : K) * q) (m + 1) + ((q : K) * q) ^ (m + 1) :=
      jk_succ _ _
    have e3 : jk ((q : K) * q) (m + 3) = jk ((q : K) * q) (m + 2) + ((q : K) * q) ^ (m + 2) :=
      jk_succ _ _
    rw [e3] at hJ3 ⊢
    rw [e2] at hJ2 hJ3 ⊢
    rw [pow_succ ((q : K) * q) (m + 1)] at hJ3 ⊢
    rw [pow_succ ((q : K) * q) m] at hJ2 hJ3 ⊢
    rw [pow_succ (-(q : K)) (m + 1)]
    generalize jk ((q : K) * q) (m + 1) = A at *
    generalize hX : ((q : K) * q) ^ m = X at *
    have hX0 : X ≠ 0 := by rw [← hX]; exact pow_ne_zero _ (mul_ne_zero hq0 hq0)
    generalize (-(q : K)) ^ (m + 1) = P at *
    have h2' : A + X * (q : K) ^ 2 ≠ 0 := by convert hJ2 using 2; ring
    have h3' : A + X * (q : K) ^ 2 + X * (q : K) ^ 4 ≠ 0 := by convert hJ3 using 1; ring
    field_simp
    ring_nf

/-- **`h ∘ X₋ = 0` on `αγ · K[ζ]`.** -/
theorem haarState_fieldMinus_ev_alphaGamma (hq : ∀ n, qSqNum q n ≠ 0) (P : Polynomial K) :
    haarState q (fieldMinus q (ev q P * (α q * γ q))) = 0 := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => rw [map_add, add_mul, map_add, map_add, h₁, h₂, add_zero]
  | monomial n c =>
    rw [ev_monomial, smul_mul_assoc, map_smul, map_smul,
      haarState_fieldMinus_zeta_pow_alphaGamma q hq, smul_zero]

end QOU.FluidDynamics.HaarFieldInvariance
