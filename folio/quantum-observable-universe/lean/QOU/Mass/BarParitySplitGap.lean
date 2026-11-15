import Mathlib.Algebra.Field.Rat
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Algebra.Module.Pi
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.BarParitySplitGap — what `conj:bar-parity-split` needs, and why it fails as stated

Companion to `conj:bar-parity-split` (demoted from a proposition 2026-11-15) and to
the probe `computations/qbeta/qbeta_bar_parity_split_gap_probe.py`. Bean `qou-hlx8`.

* `exists_parts_iff` — with identity readouts, an element `F` whose even and odd
  parts are `2•τ` and `2•r` exists **iff** `τ` is σ-fixed and `r` is σ-anti. So the
  conjecture has content only with readout maps fixed in advance.
* `trace_anti_iff` — if a linear map `T` intertwines involutions, `T x` is anti
  **iff** `T` kills the even part `x + σx`. This is the exact condition under which a
  bar-odd letter-level difference gives a bar-odd trace.
* `zD_bar_shift` — the one-letter intertwining identity
  `z_D(q) − (q − q⁻¹) = z_D(q⁻¹)`, i.e. `tr(σ⁻¹)(q) = tr(σ)(q⁻¹)` at convention D.
* `odd_mul_of_anti` — if `σ h = −h` for a ring involution `σ`, the odd part of
  `h·g` is `h` times the even part of `g`.
* `ruledTrace_not_bar_odd` — the ruled `Q_β` trace `f` (z_D, `nuc11_interleaved`)
  is not bar-odd: `f 2 + f (1/2) = −765/128 ≠ 0`. Hence, by `exists_parts_iff`, no
  `F : ℚ → ℚ` has odd part `2•f` under `q ↦ q⁻¹`.

Nothing here asserts the conjecture. Ground ring generic except where a concrete
rational evaluation is the content.
-/

namespace QOU.Mass.BarParitySplitGap

section Module

variable {R : Type*} [CommRing R] {V : Type*} [AddCommGroup V] [Module R V]

/-- Un-normalised even part. -/
def evenP (σ : V →ₗ[R] V) (x : V) : V := x + σ x

/-- Un-normalised odd part. -/
def oddP (σ : V →ₗ[R] V) (x : V) : V := x - σ x

/-- With identity readouts, a common element exists iff the two readouts have the
parities. The forward direction needs `V` to have no `2`-torsion. -/
theorem exists_parts_iff (σ : V →ₗ[R] V) (hσ : ∀ y, σ (σ y) = y)
    (h2 : ∀ v : V, v + v = 0 → v = 0) (τ r : V) :
    (∃ F, evenP σ F = τ + τ ∧ oddP σ F = r + r) ↔ (σ τ = τ ∧ σ r = -r) := by
  constructor
  · rintro ⟨F, hE, hO⟩
    simp only [evenP, oddP] at hE hO
    refine ⟨?_, ?_⟩
    · have : σ τ - τ + (σ τ - τ) = 0 := by
        have h' := congrArg σ hE
        simp only [map_add, hσ] at h'
        have e : σ τ + σ τ - (τ + τ) = 0 := by rw [← h', ← hE]; abel
        rw [← e]; abel
      exact sub_eq_zero.mp (h2 _ this)
    · have : σ r + r + (σ r + r) = 0 := by
        have h' := congrArg σ hO
        simp only [map_sub, hσ] at h'
        have : σ r + σ r + (r + r) = 0 := by
          rw [← map_add, ← hO, map_sub, hσ]; abel
        rw [← this]; abel
      exact eq_neg_of_add_eq_zero_left (h2 _ this)
  · rintro ⟨hτ, hr⟩
    refine ⟨τ + r, ?_, ?_⟩
    · simp only [evenP, map_add, hτ, hr]; abel
    · simp only [oddP, map_add, hτ, hr]; abel

/-- Intertwining: `T (σA x) = σR (T x)` for all `x`. Then `T x` is σR-anti iff `T`
annihilates the even part of `x`. -/
theorem trace_anti_iff {W : Type*} [AddCommGroup W] [Module R W]
    (σA : V →ₗ[R] V) (σR : W →ₗ[R] W) (T : V →ₗ[R] W)
    (hT : ∀ x, T (σA x) = σR (T x)) (x : V) :
    σR (T x) = - T x ↔ T (evenP σA x) = 0 := by
  simp only [evenP, map_add, hT]
  constructor
  · intro h; rw [h]; abel
  · intro h; exact eq_neg_of_add_eq_zero_right h

end Module

/-- Odd part of a product with an anti element, for a ring involution. -/
theorem odd_mul_of_anti {S : Type*} [CommRing S] (σ : S →+* S) (h g : S)
    (hh : σ h = -h) : h * g - σ (h * g) = h * (g + σ g) := by
  rw [map_mul, hh]; ring

/-- Convention-D one-letter intertwining: `tr(σ⁻¹) = z − h` at `q` equals `tr(σ) = z`
at `q⁻¹`, for `z = z_D = q³/(q²+1)`. -/
theorem zD_bar_shift {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) = q⁻¹ ^ 3 / (q⁻¹ ^ 2 + 1) := by
  have h' : q⁻¹ ^ 2 + 1 ≠ 0 := by
    rw [inv_pow]; intro h
    apply hq2
    have : ((q ^ 2)⁻¹ + 1) * q ^ 2 = 0 := by rw [h, zero_mul]
    rw [add_mul, inv_mul_cancel₀ (pow_ne_zero 2 hq)] at this
    linear_combination this
  have h3 : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  field_simp
  ring

/-- The ruled `Q_β` trace at `z_D` on `nuc11_interleaved`, as a rational function
(probe `qbeta_bar_parity_split_gap_probe.py`, check `base_f_matches_recorded_closed_form`). -/
noncomputable def ruledTrace (q : ℚ) : ℚ :=
  (q ^ 2 - 1) * (q ^ 4 + 1) *
    (2 * q ^ 12 - 6 * q ^ 10 + 3 * q ^ 8 - 6 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
    (4 * q ^ 7 * (q ^ 2 + 1) ^ 2)

/-- Bar on functions: `g ↦ (q ↦ g q⁻¹)`; linear and involutive. -/
def barFun : (ℚ → ℚ) →ₗ[ℚ] (ℚ → ℚ) where
  toFun g := fun q => g q⁻¹
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem barFun_invol (g : ℚ → ℚ) : barFun (barFun g) = g := by
  funext q; simp [barFun]

theorem ruledTrace_witness : ruledTrace 2 + ruledTrace (1 / 2) = -765 / 128 := by
  norm_num [ruledTrace]

/-- The ruled trace is not bar-odd. -/
theorem ruledTrace_not_bar_odd : barFun ruledTrace ≠ -ruledTrace := by
  intro h
  have := congrFun h 2
  simp only [barFun, LinearMap.coe_mk, AddHom.coe_mk, Pi.neg_apply] at this
  have hw := ruledTrace_witness
  rw [show (1 / 2 : ℚ) = (2 : ℚ)⁻¹ by norm_num, this] at hw
  norm_num at hw

/-- Hence no `F : ℚ → ℚ` has (un-normalised) odd part `2•f` under `q ↦ q⁻¹`, whatever
its even part. -/
theorem no_F_with_ruledTrace_odd :
    ¬ ∃ F : ℚ → ℚ, oddP barFun F = ruledTrace + ruledTrace := by
  rintro ⟨F, hF⟩
  apply ruledTrace_not_bar_odd
  have h' := congrArg barFun hF
  simp only [oddP, map_sub, barFun_invol, map_add] at h'
  have hsum : barFun ruledTrace + barFun ruledTrace + (ruledTrace + ruledTrace) = 0 := by
    rw [← h', ← hF]; simp only [oddP]; abel
  funext q
  have := congrFun hsum q
  simp only [Pi.add_apply, Pi.zero_apply] at this
  simp only [Pi.neg_apply]
  linarith

end QOU.Mass.BarParitySplitGap
