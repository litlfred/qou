import QOU.Machinery.CoxeterGeometricRepresentationFull
import QOU.Machinery.CoxeterRankTwo

/-!
# `σᵢσⱼ` has order exactly `M i j` — `DihedralExact`, for every Coxeter system

`QOU.Machinery.CoxeterGeometricRepresentationFull` closes with an explicit HONESTY note listing
what it does **not** prove: *"full Tits faithfulness (`ℓ` of arbitrary words / the order of `σᵢσⱼ`
being exactly `mᵢⱼ`)"*. This file proves the second half of that.

`QOU.Machinery.CoxeterRankTwo.DihedralExact` is the predicate — no positive power below `M i j`
is trivial — and it used to gate the whole Matsumoto/Bruhat arc: Matsumoto, the `T_w` basis, the
subword property, transitivity, lifting and the two Bruhat-order equivalences were hypothesis-free
only on **type `A`**, where `dihedralExact_le_three` discharges it. `dihedralExact_full` below
discharges it for **every** Coxeter system, and `bond_ne_zero_of_pow_eq_one` disposes of the
companion `M i j ≠ 0`; `CoxeterDihedralDescent` spends both, so no statement anywhere in that arc
carries either hypothesis any more.

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
-- Ref: [leitner2026] bean qou-1u90
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

/-! ## The infinite-bond case: the order is genuinely infinite

`DihedralExact` is vacuous at `M i j = 0` — there is no `k` with `0 < k < 0` — so the theorems
above already cover it. But the *stronger* statement is true and is what the descent lemma needs:
at an infinite bond **no** positive power of `fᵢfⱼ` is the identity.

🛑 **The cosine argument cannot prove this, and it is worth saying why rather than trying.** At
`m = 0` the convention `π/0 = 0` gives `c = −1`, so the Gram matrix `[[1,c],[c,1]]` is singular and
the pair `(⟨αᵢ,v⟩, ⟨αⱼ,v⟩)` collapses onto the line `(1,−1)`: `xSeq` and `ySeq` are **constantly**
`1` and `−1`, for every `k`. They cannot distinguish anything — correctly, since the infinite
dihedral group has no relation to detect.

What does work is the **coefficient**, not the form value. The composite acts as a shear, and

    (fᵢfⱼ)^k αᵢ = (1 + 2k)·αᵢ + 2k·αⱼ,

so the `αᵢ`-coefficient is `1 + 2k` and is `1` only at `k = 0`.

## What this unlocks, and why it is NOT spent here

`hfin : ∀ i j, i ≠ j → M i j ≠ 0` is the last hypothesis on the Matsumoto/Bruhat arc. It enters at
one place — `CoxeterDihedralDescent.alternatingWord_reduced_of_both_descents`, which needs
`M i j ≠ 0` for `not_isReduced_alternatingWord`. `reflEnd_pair_pow_ne_one_of_infinite` **removes
that need**: the descent lemma already derives `(σᵢσⱼ)^k = 1` with `k ≥ 1`, and at `M i j = 0` that
is now impossible, so the `m = 0` branch is refuted rather than excluded.

**Measured cost of doing it: 17 theorem signatures and 79 call sites across five merged files**, one
of which a sibling session is actively extending. **Measured benefit: none today** — every Coxeter
matrix in this corpus is `CoxeterMatrix.Aₙ`, and a grep finds no infinite bond anywhere. So the
refactor is left as a deliberate, separately-reviewable change rather than folded in here. The
input it needs is proved and sitting in this file; bean `qou-1u90`. -/

/-- At an infinite bond the scalar pair is constant, hence blind. -/
theorem xSeq_ySeq_of_infinite {i j : B} (hij : i ≠ j) (hm : M i j = 0) :
    ∀ k : ℕ, xSeq M i j k = 1 ∧ ySeq M i j k = -1 := by
  have hc : bilinCoeff M i j = -1 := by
    unfold bilinCoeff
    rw [if_neg hij, hm]
    norm_num
  intro k
  induction k with
  | zero => exact ⟨xSeq_zero i j, by rw [ySeq_zero, hc]⟩
  | succ k ih =>
    refine ⟨?_, ?_⟩
    · rw [xSeq_succ, ih.1, ih.2, hc]; ring
    · rw [ySeq_succ, ih.1, ih.2, hc]; ring

/-- **The shear.** At an infinite bond, one step adds `2αᵢ + 2αⱼ` to the orbit vector. -/
theorem orbit_succ_of_infinite {i j : B} (hij : i ≠ j) (hm : M i j = 0) (k : ℕ) :
    ((reflEnd M i * reflEnd M j) ^ (k + 1)) (Finsupp.single i 1)
      = ((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1)
        + Finsupp.single i 2 + Finsupp.single j 2 := by
  have hc : bilinCoeff M i j = -1 := by
    unfold bilinCoeff
    rw [if_neg hij, hm]
    norm_num
  obtain ⟨hx, hy⟩ := xSeq_ySeq_of_infinite hij hm k
  rw [pow_succ', Module.End.mul_apply, reflEnd_pair_apply]
  have hxv : formLin M i (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1)) = 1 := hx
  have hyv : formLin M j (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1)) = -1 := hy
  rw [hxv, hyv, hc]
  norm_num
  abel

/-- **The `αᵢ`-coefficient along the orbit is `1 + 2k`.** -/
theorem orbit_coeff_of_infinite {i j : B} (hij : i ≠ j) (hm : M i j = 0) (k : ℕ) :
    (((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1)) i = 1 + 2 * k := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [orbit_succ_of_infinite hij hm k]
    simp only [Finsupp.add_apply, Finsupp.single_eq_same, ih]
    have hzero : (Finsupp.single j (2 : ℝ)) i = 0 := by
      apply Finsupp.single_eq_of_ne
      exact hij
    rw [hzero]
    push_cast
    ring

/-- **At an infinite bond, `fᵢfⱼ` has infinite order.** -/
theorem reflEnd_pair_pow_ne_one_of_infinite {i j : B} (hij : i ≠ j) (hm : M i j = 0)
    {k : ℕ} (hk : 0 < k) : (reflEnd M i * reflEnd M j) ^ k ≠ 1 := by
  intro hpow
  have h0 : ((reflEnd M i * reflEnd M j) ^ k) (Finsupp.single i 1) = Finsupp.single i 1 := by
    rw [hpow]; rfl
  have h1 := orbit_coeff_of_infinite hij hm k
  rw [h0, Finsupp.single_eq_same] at h1
  have hk' : (0 : ℝ) < k := by exact_mod_cast hk
  linarith

/-! ## `DihedralExact`, in general -/

variable {W : Type*} [Group W]

/-- Transport a trivial power of `σᵢσⱼ` along `geomRepFull` into the reflection representation.
Both results below turn on this one step. -/
private theorem reflEnd_pow_eq_one_of_simple (cs : CoxeterSystem M W) {i j : B} {k : ℕ}
    (hpow : (cs.simple i * cs.simple j) ^ k = 1) :
    (reflEnd M i * reflEnd M j) ^ k = 1 := by
  have h := congrArg (geomRepFull cs) hpow
  rw [map_pow, map_mul, geomRepFull_simple, geomRepFull_simple, map_one] at h
  exact h

/-- **`σᵢσⱼ` has order exactly `M i j`, in every Coxeter system.**

This is the second half of what `CoxeterGeometricRepresentationFull`'s HONESTY note excludes from
its own scope, and it discharges `CoxeterRankTwo.DihedralExact` unconditionally — so Matsumoto,
the `T_w` basis, the subword property, Bruhat transitivity, lifting and the order equivalences hold
for every Coxeter system, not only type `A`. -/
theorem dihedralExact_full (cs : CoxeterSystem M W) : DihedralExact cs :=
  fun _ _ hij _ hk hkm hpow =>
    reflEnd_pair_pow_ne_one hij rfl hk hkm (reflEnd_pow_eq_one_of_simple cs hpow)

/-- **A trivial positive power of `σᵢσⱼ` forces the bond order to be finite.**

The companion of `dihedralExact_full` at the other end of the range, and the input that lets the
descent lemma *derive* `M i j ≠ 0` instead of assuming it: at `M i j = 0` the rotation `fᵢfⱼ` is a
shear of infinite order (`reflEnd_pair_pow_ne_one_of_infinite`), so no positive power of `σᵢσⱼ`
can be trivial. -/
theorem bond_ne_zero_of_pow_eq_one (cs : CoxeterSystem M W) {i j : B} (hij : i ≠ j)
    {k : ℕ} (hk : 0 < k) (hpow : (cs.simple i * cs.simple j) ^ k = 1) : M i j ≠ 0 :=
  fun h0 =>
    reflEnd_pair_pow_ne_one_of_infinite hij h0 hk (reflEnd_pow_eq_one_of_simple cs hpow)

end QOU.Machinery.CoxeterDihedralOrder
