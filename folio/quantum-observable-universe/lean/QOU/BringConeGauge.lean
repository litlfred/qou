import Mathlib.Tactic
import QOU.BringCone

/-!
# The unit `u` of the chirality grading is a gauge choice — and exactly when

Bean `qou-wqto`, issue #7783. Owner ruling 2026-11-15: set `u = i` without loss of
generality and prove that the choice does not matter.

`QOU.BringCone` builds the chirality grading `Γ_u = L_u ∘ M_i`, `p ↦ u·p·i`, for a
pure unit quaternion `u`, and shows nothing in the Reeb triad picks `u`. This file
proves what "the choice does not matter" means, and where it stops being true.

## What is proved

* **Gauge equivalence (`exists_triad_equiv_conj_chiralGammaU`).** For pure units
  `u`, `v` there is an `R`-linear automorphism `e` of the cone commuting with all
  three Reeb operators and carrying `Γ_u` to `Γ_v` (`e ∘ Γ_u = Γ_v ∘ e`), provided
  either `2·(1 + u·v)` is a unit, or `v = −u` and there is a pure `w ⊥ u` whose norm
  is a unit. The two cases use `L_{1−vu}` and `L_w` respectively.
* **Unconditional over an ordered field (`exists_triad_equiv_conj_chiralGammaU_ordered`).**
  Over a linearly ordered field (so over `ℝ`) the hypothesis is always met: any two
  points of the sphere of pure units give gauge-equivalent gradings.
* **Transport (`TriadGauge.eigen_iff`, `TriadGauge.reeb_*`).** A gauge equivalence
  carries `Γ_u`-eigenvectors to `Γ_v`-eigenvectors with the same eigenvalue and
  commutes with the triad, so every statement built from `Γ`, the eigenvalues and
  the Reeb operators moves from `u = i` to any `u`.
* **Directly `u`-generic forms** of the `u = i` statements that did not yet have
  one: `reebM_j_flips_eigenU` and its three siblings (`M_j`, `M_k` exchange the
  `Γ_u = ∓1` eigenvectors, `M_i` preserves them).

## What is NOT covariant — a finding, not a defect

* **Over a general commutative ring the choice is NOT a gauge choice.**
  `isUnit_two_of_triadGauge_i_j`: if any triad-commuting automorphism carries
  `Γ_i` to `Γ_j`, then `2` is a unit in `R`. So over `ℤ` (or any ring where `2` is
  not invertible) the gradings at `u = i` and `u = j` are genuinely inequivalent
  under the commutant of the Reeb triad. "WLOG `u = i`" is sound over `ℝ`, `ℚ`,
  any ordered field; it is not sound over `ℤ`.
* **The coordinate form `chiralGamma_apply`** (`Γ = −1` on `span(1, i)`, `+1` on
  `span(j, k)`) is a statement in the gauge `u = i` and is not covariant as written;
  its covariant content is `TriadGauge.eigen_iff`: the `Γ_v`-eigenspaces are the
  images of `span(1, i)` and `span(j, k)` under `e`.

Generic `[CommRing R]` throughout, per §7c, except §4, which needs an order
(sums of squares vanish only at zero) and says so in its typeclasses.

🛑 Nothing here closes the open item of `qou-wqto`: it removes the choice of `u`
from the list of things to derive. The model is still the Hopf cone `ℍ`, not
Bring's own cone (`qou-rydq`).
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-! ## 1. Gauge transformations of the chirality grading -/

/-- Euclidean dot product of the imaginary parts. -/
def imDot (u v : BringCone R) : R := u.imI * v.imI + u.imJ * v.imJ + u.imK * v.imK

/-- A **triad gauge transformation** from `Γ_u` to `Γ_v`: an `R`-linear automorphism
of the cone that commutes with each Reeb operator and intertwines the two gradings. -/
structure TriadGauge (u v : BringCone R) where
  /-- The automorphism. -/
  e : BringCone R ≃ₗ[R] BringCone R
  comm_i : ∀ p, e (reebM_i p) = reebM_i (e p)
  comm_j : ∀ p, e (reebM_j p) = reebM_j (e p)
  comm_k : ∀ p, e (reebM_k p) = reebM_k (e p)
  conj : ∀ p, e (chiralGammaU u p) = chiralGammaU v (e p)

/-- Left multiplication by an invertible quaternion, as a linear equivalence. -/
def leftMulEquiv (q q' : BringCone R) (h1 : q' * q = 1) (h2 : q * q' = 1) :
    BringCone R ≃ₗ[R] BringCone R where
  toFun := leftMul q
  invFun := leftMul q'
  map_add' x y := by simp [leftMul, mul_add]
  map_smul' c x := by simp [leftMul]
  left_inv x := by simp [leftMul, ← mul_assoc, h1]
  right_inv x := by simp [leftMul, ← mul_assoc, h2]

/-- **A quaternion `q` with `q·u = v·q` and invertible norm is a triad gauge
transformation `Γ_u → Γ_v`.** -/
noncomputable def TriadGauge.ofIntertwiner {u v q : BringCone R} (hq : q * u = v * q)
    (hc : IsUnit (Quaternion.normSq q)) : TriadGauge u v where
  e := leftMulEquiv q ((↑(hc.unit⁻¹) : R) • star q)
    (by
      rw [smul_mul_assoc, Quaternion.star_mul_self, ← Quaternion.coe_mul_eq_smul,
        ← Quaternion.coe_mul]
      have : (↑(hc.unit⁻¹) : R) * Quaternion.normSq q = 1 := by
        have h := Units.inv_mul hc.unit; rwa [IsUnit.unit_spec] at h
      rw [this]; rfl)
    (by
      rw [mul_smul_comm, Quaternion.self_mul_star, ← Quaternion.coe_mul_eq_smul,
        ← Quaternion.coe_mul]
      have : (↑(hc.unit⁻¹) : R) * Quaternion.normSq q = 1 := by
        have h := Units.inv_mul hc.unit; rwa [IsUnit.unit_spec] at h
      rw [this]; rfl)
  comm_i p := leftMul_comm_reebM_i q p
  comm_j p := leftMul_comm_reebM_j q p
  comm_k p := leftMul_comm_reebM_k q p
  conj p := by
    show leftMul q (chiralGammaU u p) = chiralGammaU v (leftMul q p)
    simp only [chiralGammaU, leftMul, reebM_i]
    rw [← mul_assoc, ← mul_assoc, hq]
    simp only [mul_assoc]

/-- For pure `u`, `w` with `u ⊥ w`: `w·u = (−u)·w`, i.e. they anticommute. -/
theorem mul_eq_neg_mul_of_orthogonal {u w : BringCone R} (hu0 : u.re = 0)
    (hw0 : w.re = 0) (hd : imDot u w = 0) : w * u = -u * w := by
  unfold imDot at hd
  ext <;> simp [hu0, hw0] <;>
    first | linear_combination (-2 : R) * hd | linear_combination (2 : R) * hd | linear_combination

/-! ## 2. The gauge-equivalence theorem -/

/-- **The choice of `u` is a gauge choice.** For pure units `u`, `v`, a triad gauge
transformation `Γ_u → Γ_v` exists, provided either `2·(1 + u·v)` is a unit (then
`L_{1−vu}` works), or `v = −u` and some pure `w ⊥ u` has invertible norm (then
`L_w` works). -/
theorem exists_triad_equiv_conj_chiralGammaU {u v : BringCone R}
    (hu0 : u.re = 0) (hv0 : v.re = 0)
    (hu1 : Quaternion.normSq u = 1) (hv1 : Quaternion.normSq v = 1)
    (h : IsUnit (2 * (1 + imDot u v)) ∨
      (v = -u ∧ ∃ w : BringCone R, w.re = 0 ∧ imDot u w = 0 ∧
        IsUnit (Quaternion.normSq w))) :
    Nonempty (TriadGauge u v) := by
  rcases h with h | ⟨rfl, w, hw0, hd, hw⟩
  · have hu : u * u = -1 := (sq_eq_neg_one_iff_normSq_of_pure u hu0).mpr hu1
    have hv : v * v = -1 := (sq_eq_neg_one_iff_normSq_of_pure v hv0).mpr hv1
    refine ⟨TriadGauge.ofIntertwiner (intertwiner_mul hu hv) ?_⟩
    rw [normSq_intertwiner hu0 hv0 hu1 hv1]
    exact h
  · exact ⟨TriadGauge.ofIntertwiner (mul_eq_neg_mul_of_orthogonal hu0 hw0 hd) hw⟩

/-! ## 3. Transport: what a gauge transformation carries -/

namespace TriadGauge

variable {u v : BringCone R} (g : TriadGauge u v)

/-- **Eigenvectors are carried to eigenvectors with the same eigenvalue.** This is
the covariant content of `chiralGamma_apply`: the `Γ_v`-eigenspaces are the
`e`-images of the `Γ_u`-eigenspaces. -/
theorem eigen_iff (s : R) (p : BringCone R) :
    chiralGammaU u p = s • p ↔ chiralGammaU v (g.e p) = s • g.e p := by
  rw [← g.conj, ← map_smul]
  exact g.e.injective.eq_iff.symm

/-- `e` carries a `Γ_u = −1` vector to a `Γ_v = −1` vector. -/
theorem eigen_neg (p : BringCone R) :
    chiralGammaU u p = -p ↔ chiralGammaU v (g.e p) = -g.e p := by
  rw [← g.conj, ← map_neg]
  exact g.e.injective.eq_iff.symm

/-- The inverse of a triad gauge transformation is one. -/
def symm : TriadGauge v u where
  e := g.e.symm
  comm_i p := g.e.injective (by rw [g.comm_i]; simp)
  comm_j p := g.e.injective (by rw [g.comm_j]; simp)
  comm_k p := g.e.injective (by rw [g.comm_k]; simp)
  conj p := g.e.injective (by rw [g.conj]; simp)

end TriadGauge

/-! ### The `u = i` statements of `BringCone.lean`, for every `u`

`chiralGamma_sq`, `chiralGamma_comm_reebM_i`, `chiralGamma_anticomm_reebM_j` already
have `u`-generic forms there (`chiralGammaU_sq`, `chiralGammaU_comm_reebM_i`,
`chiralGammaU_anticomm_reebM_j`, `chiralGammaU_anticomm_reebM_k`); `reebM_j_ray_free`
does not mention `Γ`. The eigenvector-flip statement had only the `u = i` form. -/

/-- `M_j` sends a `Γ_u = −1` vector to a `Γ_u = +1` vector, for every `u`. -/
theorem reebM_j_flips_eigenU {u p : BringCone R} (hp : chiralGammaU u p = -p) :
    chiralGammaU u (reebM_j p) = reebM_j p := by
  rw [chiralGammaU_anticomm_reebM_j, hp]
  simp [reebM_j]

/-- `M_j` sends a `Γ_u = +1` vector to a `Γ_u = −1` vector, for every `u`. -/
theorem reebM_j_flips_eigenU' {u p : BringCone R} (hp : chiralGammaU u p = p) :
    chiralGammaU u (reebM_j p) = -reebM_j p := by
  rw [chiralGammaU_anticomm_reebM_j, hp]

/-- `M_k` also exchanges the two chiralities, for every `u`. -/
theorem reebM_k_flips_eigenU {u p : BringCone R} (hp : chiralGammaU u p = -p) :
    chiralGammaU u (reebM_k p) = reebM_k p := by
  rw [chiralGammaU_anticomm_reebM_k, hp]
  simp [reebM_k]

/-- `M_i` preserves each chirality, for every `u`. -/
theorem reebM_i_preserves_eigenU {u p : BringCone R} {s : R}
    (hp : chiralGammaU u p = s • p) :
    chiralGammaU u (reebM_i p) = s • reebM_i p := by
  rw [chiralGammaU_comm_reebM_i, hp]
  simp [reebM_i]

/-- `reebM_j_flips_eigen` (BringCone) is the `u = i` case of `reebM_j_flips_eigenU`: `Γ_i = Γ`. -/
theorem reebM_j_flips_eigen_eq_U {p : BringCone R} (hp : chiralGamma p = -p) :
    chiralGamma (reebM_j p) = reebM_j p :=
  reebM_j_flips_eigenU (u := unitI) hp

/-! ## 4. Over an ordered field the gauge freedom is the whole sphere -/

section Ordered

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

private theorem sq3_eq_zero {a b c : F} (h : a * a + b * b + c * c = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 := by
  have ha : a * a = 0 := by nlinarith [mul_self_nonneg a, mul_self_nonneg b, mul_self_nonneg c]
  have hb : b * b = 0 := by nlinarith [mul_self_nonneg a, mul_self_nonneg b, mul_self_nonneg c]
  have hc : c * c = 0 := by nlinarith [mul_self_nonneg a, mul_self_nonneg b, mul_self_nonneg c]
  exact ⟨mul_self_eq_zero.mp ha, mul_self_eq_zero.mp hb, mul_self_eq_zero.mp hc⟩

/-- **Over a linearly ordered field (e.g. `ℝ`), any two pure units give
gauge-equivalent gradings.** No hypothesis beyond `u`, `v` being points of `S²`. -/
theorem exists_triad_equiv_conj_chiralGammaU_ordered {u v : BringCone F}
    (hu0 : u.re = 0) (hv0 : v.re = 0)
    (hu1 : Quaternion.normSq u = 1) (hv1 : Quaternion.normSq v = 1) :
    Nonempty (TriadGauge u v) := by
  have hu1' := hu1
  have hv1' := hv1
  rw [Quaternion.normSq_def'] at hu1' hv1'
  rw [hu0] at hu1'
  rw [hv0] at hv1'
  apply exists_triad_equiv_conj_chiralGammaU hu0 hv0 hu1 hv1
  by_cases hd : 1 + imDot u v = 0
  · right
    -- `|u + v|² = 2(1 + u·v) = 0`, so `v = −u`.
    have hsum : (u.imI + v.imI) * (u.imI + v.imI) + (u.imJ + v.imJ) * (u.imJ + v.imJ)
        + (u.imK + v.imK) * (u.imK + v.imK) = 0 := by
      unfold imDot at hd
      linear_combination hu1' + hv1' + 2 * hd
    obtain ⟨h1, h2, h3⟩ := sq3_eq_zero hsum
    refine ⟨?_, ?_⟩
    · ext
      · simp [hu0, hv0]
      · simp; linear_combination h1
      · simp; linear_combination h2
      · simp; linear_combination h3
    · by_cases hjk : u.imJ * u.imJ + u.imK * u.imK = 0
      · refine ⟨unitJ, rfl, ?_, ?_⟩
        · have := (sq3_eq_zero (a := u.imJ) (b := u.imK) (c := (0 : F))
            (by linear_combination hjk)).1
          simp [imDot, unitJ, this]
        · rw [Quaternion.normSq_def']; simp [unitJ]
      · refine ⟨⟨0, 0, u.imK, -u.imJ⟩, rfl, ?_, ?_⟩
        · simp [imDot]; ring
        · rw [Quaternion.normSq_def']
          refine (isUnit_iff_ne_zero).mpr ?_
          simp only
          intro h; apply hjk; linear_combination h
  · left
    exact (isUnit_iff_ne_zero).mpr (mul_ne_zero two_ne_zero hd)

end Ordered

/-! ## 5. Not covariant over a general ring: the obstruction is `1/2` -/

/-- **If `Γ_i` and `Γ_j` are triad-gauge-equivalent, then `2` is a unit.** So over a
ring in which `2` is not invertible (e.g. `ℤ`), the choice of `u` is NOT a gauge
choice: `Γ_i` and `Γ_j` are inequivalent under the commutant of the Reeb triad. -/
theorem isUnit_two_of_triadGauge_i_j (g : TriadGauge (unitI : BringCone R) unitJ) :
    IsUnit (2 : R) := by
  have hL := commutes_reeb_triad_iff_leftMul g.e.toLinearMap g.comm_i g.comm_j g.comm_k
  have hL' := commutes_reeb_triad_iff_leftMul g.symm.e.toLinearMap
    g.symm.comm_i g.symm.comm_j g.symm.comm_k
  have e_eq : ∀ p, g.e p = g.e 1 * p := fun p => hL p
  have e'_eq : ∀ p, g.e.symm p = g.e.symm 1 * p := fun p => hL' p
  have hqq' : g.e 1 * g.e.symm 1 = 1 := by
    rw [← e_eq, LinearEquiv.apply_symm_apply]
  have hq'q : g.e.symm 1 * g.e 1 = 1 := by
    rw [← e'_eq, LinearEquiv.symm_apply_apply]
  set q := g.e 1 with hq
  set q' := g.e.symm 1 with hq'
  have hn : IsUnit (Quaternion.normSq q) := by
    refine isUnit_of_mul_eq_one _ (Quaternion.normSq q') ?_
    rw [← map_mul, hqq', map_one]
  have hc := g.conj 1
  rw [e_eq, e_eq] at hc
  simp only [chiralGammaU, leftMul, reebM_i, unitI, unitJ, mul_one] at hc
  have hre := congrArg (fun x : BringCone R => x.re) hc
  have hI := congrArg (fun x : BringCone R => x.imI) hc
  have hJ := congrArg (fun x : BringCone R => x.imJ) hc
  have hK := congrArg (fun x : BringCone R => x.imK) hc
  simp at hre hI hJ hK
  have hnorm : Quaternion.normSq q = 2 * (q.re * q.re + q.imI * q.imI) := by
    rw [Quaternion.normSq_def']
    linear_combination (q.imJ + q.imI) * hJ + (q.imK + q.re) * hK
  rw [hnorm] at hn
  exact isUnit_of_mul_isUnit_left hn

end QOU.Tetraplectic
