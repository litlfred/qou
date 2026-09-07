import QOU.Machinery.CoxeterGeometricRepresentationFull
import QOU.Machinery.CoxeterRankTwo

/-!
# `σᵢσⱼ` has order exactly `M i j` — `DihedralExact`, for every Coxeter system

`QOU.Machinery.CoxeterGeometricRepresentationFull` closes with an explicit HONESTY note listing
what it does **not** prove: *"full Tits faithfulness (`ℓ` of arbitrary words / the order of `σᵢσⱼ`
being exactly `mᵢⱼ`)"*. This file proves the second half of that.

`QOU.Machinery.CoxeterRankTwo.DihedralExact` is the predicate — no positive power below `M i j`
is trivial — and it gates, at present, the whole Matsumoto/Bruhat arc: Matsumoto, the `T_w` basis,
the subword property, transitivity, lifting, and the two Bruhat-order equivalences are all
hypothesis-free only on **type `A`**, where `dihedralExact_le_three` discharges it. With
`dihedralExact_full` below they are unconditional for **every** Coxeter system.

## The proof, and why it is shorter than the one already here

`reflEnd_pair_pow_eq_one` proves `(fᵢfⱼ)^m = 1` by showing the scalar pair is `m`-periodic and
then arguing that periodicity forces two accumulated sums to vanish. That needs `sin φ ≠ 0`, hence
`m ≥ 3`, and a real-analysis argument at the end.

The **converse** turns out to need less, not more. Track a single scalar along the orbit of one
root:

    x k = ⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩.

`formLin_i_pair` and `formLin_j_pair` — already in that file — give the 2×2 recursion, and
eliminating the other coordinate leaves the Chebyshev two-step recursion
`x (k+2) = (4c² − 2)·x (k+1) − x k` with `c = B(αᵢ,αⱼ) = −cos(π/m)`.

The **initial data is what makes this work**: `x 0 = 1` and `x 1 = 2c² − 1 = cos φ`, where
`φ = 2π/m`. Those are exactly `cos 0` and `cos φ`, so matching against `k ↦ cos (kφ)` — same
recursion, same first two terms — gives

    x k = cos (k φ)   for every k,

with **no** sine anywhere and no invertibility hypothesis. So `m ≥ 2` suffices, where the forward
direction needed `m ≥ 3`.

Then `(fᵢfⱼ)^k = 1` forces `x k = x 0 = 1`, i.e. `cos (kφ) = 1`; and for `0 < k < m` we have
`0 < kφ < 2π`, where `Real.cos_eq_one_iff_of_lt_of_lt` says the cosine is `1` only at `0`.

Transporting back to the group is `geomRepFull`, a monoid hom, so a trivial power upstairs would
give a trivial power downstairs.

-- Ref: [bourbaki1968] Groupes et algèbres de Lie, Ch. V §4 (the dihedral case of the geometric rep)
-- Ref: [humphreys1990] Reflection Groups and Coxeter Groups, §5.3–5.4
-- Ref: [manuscript] bean qou-1u90
-/

namespace QOU.Machinery.CoxeterDihedralOrder

open CoxeterSystem
open QOU.Machinery.HeckeGeneral QOU.Machinery.CoxeterParabolic
open QOU.Machinery.CoxeterRankTwo

variable {B : Type*} {M : CoxeterMatrix B}

/-! ## A two-step recursion is determined by its first two terms -/

private theorem two_step_eq' (T : ℝ) (u v : ℕ → ℝ)
    (hu : ∀ k, u (k + 2) = T * u (k + 1) - u k)
    (hv : ∀ k, v (k + 2) = T * v (k + 1) - v k)
    (h0 : u 0 = v 0) (h1 : u 1 = v 1) : ∀ k, u k = v k := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    match k with
    | 0 => exact h0
    | 1 => exact h1
    | (k + 2) => rw [hu, hv, ih (k + 1) (by omega), ih k (by omega)]

private theorem cos_two_step' (a f : ℝ) :
    Real.cos (a + 2 * f) = 2 * Real.cos f * Real.cos (a + f) - Real.cos a := by
  rw [show a + 2 * f = a + f + f from by ring, Real.cos_add (a + f) f,
    Real.cos_add a f, Real.sin_add a f]
  linear_combination (-Real.cos a) * Real.sin_sq_add_cos_sq f

/-! ## The scalar pair along the orbit of `αᵢ` -/

variable (M) in
/-- `xSeq i j k = ⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩`. -/
noncomputable def xSeq (i j : B) (k : ℕ) : ℝ :=
  formLin M i (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1))

variable (M) in
/-- `ySeq i j k = ⟨αⱼ, (fᵢfⱼ)^k αᵢ⟩`. -/
noncomputable def ySeq (i j : B) (k : ℕ) : ℝ :=
  formLin M j (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1))

theorem xSeq_succ (i j : B) (k : ℕ) :
    xSeq M i j (k + 1) = -(xSeq M i j k) + 2 * bilinCoeff M i j * ySeq M i j k := by
  show formLin M i (((reflEnd M i * reflEnd M j) ^ (k + 1)) _) = _
  rw [pow_succ']
  exact formLin_i_pair M i j _

theorem ySeq_succ (i j : B) (k : ℕ) :
    ySeq M i j (k + 1)
      = -(2 * bilinCoeff M i j) * xSeq M i j k
        + (4 * bilinCoeff M i j ^ 2 - 1) * ySeq M i j k := by
  show formLin M j (((reflEnd M i * reflEnd M j) ^ (k + 1)) _) = _
  rw [pow_succ']
  exact formLin_j_pair M i j _

/-- **The Chebyshev recursion.** Eliminating `ySeq` between the two first-order relations leaves a
single two-step recursion with `T = 4c² − 2`, which is `2 cos φ`. -/
theorem xSeq_two_step (i j : B) (k : ℕ) :
    xSeq M i j (k + 2)
      = (4 * bilinCoeff M i j ^ 2 - 2) * xSeq M i j (k + 1) - xSeq M i j k := by
  have e1 := xSeq_succ (M := M) i j (k + 1)
  have e2 := ySeq_succ (M := M) i j k
  have e3 := xSeq_succ (M := M) i j k
  rw [e1, e2]
  linear_combination (1 - 4 * bilinCoeff M i j ^ 2) * e3

/-! ## Initial data -/

@[simp] theorem xSeq_zero (i j : B) : xSeq M i j 0 = 1 := by
  show formLin M i (((reflEnd M i * reflEnd M j) ^ 0) _) = _
  rw [pow_zero]
  show formLin M i (Finsupp.single i 1) = 1
  rw [formLin_single, bilinCoeff_diag, mul_one]

@[simp] theorem ySeq_zero (i j : B) : ySeq M i j 0 = bilinCoeff M i j := by
  show formLin M j (((reflEnd M i * reflEnd M j) ^ 0) _) = _
  rw [pow_zero]
  show formLin M j (Finsupp.single i 1) = _
  rw [formLin_single, mul_one, bilinCoeff_symm]

theorem xSeq_one (i j : B) : xSeq M i j 1 = 2 * bilinCoeff M i j ^ 2 - 1 := by
  have h := xSeq_succ (M := M) i j 0
  rw [xSeq_zero, ySeq_zero] at h
  rw [h]
  ring

/-! ## `xSeq` is a cosine -/

/-- **`⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩ = cos (k · 2π/m)`.**

The whole content is that the initial data matches: `x 0 = 1 = cos 0` and, because
`c = −cos(π/m)`, `x 1 = 2c² − 1 = 2cos²(π/m) − 1 = cos(2π/m)` by the double-angle formula. No
sine, no invertibility, and `m ≥ 2` rather than `m ≥ 3`. -/
theorem xSeq_eq_cos {i j : B} (hij : i ≠ j) {m : ℕ} (hm : M i j = m) (k : ℕ) :
    xSeq M i j k = Real.cos (k * (2 * Real.pi / m)) := by
  have hc : bilinCoeff M i j = -Real.cos (Real.pi / m) := by
    unfold bilinCoeff
    rw [if_neg hij, hm]
  set φ := 2 * Real.pi / m with hφ
  have hcosφ : Real.cos φ = 2 * bilinCoeff M i j ^ 2 - 1 := by
    have h2 : φ = 2 * (Real.pi / m) := by rw [hφ]; ring
    rw [h2, Real.cos_two_mul, hc]
    ring
  refine two_step_eq' (4 * bilinCoeff M i j ^ 2 - 2) (xSeq M i j)
    (fun n => Real.cos (n * φ)) (xSeq_two_step i j) ?_ ?_ ?_ k
  · intro n
    simp only
    push_cast
    rw [show ((n : ℝ) + 2) * φ = (n : ℝ) * φ + 2 * φ from by ring, cos_two_step',
      show (n : ℝ) * φ + φ = ((n : ℝ) + 1) * φ from by ring, hcosφ]
    ring
  · show xSeq M i j 0 = Real.cos ((0 : ℕ) * φ)
    rw [xSeq_zero]
    norm_num
  · show xSeq M i j 1 = Real.cos ((1 : ℕ) * φ)
    rw [xSeq_one]
    push_cast
    rw [one_mul, hcosφ]

/-! ## The order is exactly `M i j` -/

/-- **No smaller positive power of `fᵢfⱼ` is the identity.** -/
theorem reflEnd_pair_pow_ne_one {i j : B} (hij : i ≠ j) {m : ℕ} (hm : M i j = m)
    {k : ℕ} (hk : 0 < k) (hkm : k < m) :
    (reflEnd M i * reflEnd M j) ^ k ≠ 1 := by
  intro hpow
  have hm2 : (0 : ℝ) < m := by
    have : (0 : ℕ) < m := by omega
    exact_mod_cast this
  set φ := 2 * Real.pi / m with hφ
  -- A trivial power fixes `αᵢ`, so the scalar returns to its initial value.
  have hx : xSeq M i j k = 1 := by
    have h0 : ((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1) = Finsupp.single i 1 := by
      rw [hpow]; rfl
    show formLin M i (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1)) = 1
    rw [h0, formLin_single, bilinCoeff_diag, mul_one]
  rw [xSeq_eq_cos hij hm] at hx
  -- But `0 < k·φ < 2π`, where the cosine is `1` only at `0`.
  have hpos : 0 < (k : ℝ) * φ := by
    have hk' : (0 : ℝ) < k := by exact_mod_cast hk
    have : 0 < φ := by rw [hφ]; positivity
    positivity
  have hlt : (k : ℝ) * φ < 2 * Real.pi := by
    rw [hφ, mul_div_assoc']
    rw [div_lt_iff₀ hm2]
    have hkm' : (k : ℝ) < m := by exact_mod_cast hkm
    nlinarith [Real.pi_pos]
  have := (Real.cos_eq_one_iff_of_lt_of_lt (by linarith [Real.pi_pos]) hlt).mp hx
  linarith

/-! ## `DihedralExact`, in general -/

variable {W : Type*} [Group W]

/-- **`σᵢσⱼ` has order exactly `M i j`, in every Coxeter system.**

This is the second half of what `CoxeterGeometricRepresentationFull`'s HONESTY note excludes from
its own scope, and it discharges `CoxeterRankTwo.DihedralExact` unconditionally — so Matsumoto,
the `T_w` basis, the subword property, Bruhat transitivity, lifting and the order equivalences hold
for every Coxeter system, not only type `A`. -/
theorem dihedralExact_full (cs : CoxeterSystem M W) : DihedralExact cs := by
  intro i j hij k hk hkm hpow
  have himg : (reflEnd M i * reflEnd M j) ^ k = 1 := by
    have h := congrArg (geomRepFull cs) hpow
    rw [map_pow, map_mul, geomRepFull_simple, geomRepFull_simple, map_one] at h
    exact h
  exact reflEnd_pair_pow_ne_one hij rfl hk hkm himg

end QOU.Machinery.CoxeterDihedralOrder
