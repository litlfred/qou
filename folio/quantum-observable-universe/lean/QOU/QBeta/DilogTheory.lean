import QOU.QBeta.FiveTwoFiveTermArguments
import Mathlib.Tactic

/-!
# Dilogarithm theories — the functional equations as one class

Categorify audit 2026-11-15, item 1. Every dilogarithm identity in the 5₂ ladder was proved for
the concrete Rogers `L` by "derivative zero, then a boundary limit". The downstream algebra
(`FiveTwoFiveTermArguments.numerators_of_abel`) already worked for an arbitrary `L`; this file
names the class it needs.

* **Part A, `RogersDilogTheory K`** (`K` an ordered field): `L` with reflection and Abel's
  five-term relation on `(0,1)`. `RogersDilogTheory.numerators` gives the level-7 numerators
  `(17, 5, −1)` for **every** instance. `rogers` (in `DilogTheoryArchimedean`, split per §7c) is the real instance; its analytic content is
  exactly `rogersL_reflection` and `rogersL_fiveTerm`.
* **Part B, `SuslinDilogTheory F A`** (`F` any field, `A` any abelian group): oddness under
  `z ↦ 1/z` plus Suslin's five-term relation, in the orientation of PR #7946
  (the corpus's `PentagonCoherent` uses the inverted orientation and forces `D = 0`).
  `SuslinDilogTheory.anharmonic` derives the whole anharmonic orbit (including the Landen-type
  `D(z/(z−1)) = −D z`) by algebra, given reflection oddness. The Bloch–Wigner instance and the
  rigidity of continuous instances over `ℂ` are in `DilogTheoryArchimedean`.

-- Ref: [leitner2026] /mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md item 1
-/
namespace QOU.QBeta.DilogTheory

/-! ## Part A — Rogers-type theories on `(0,1)` of an ordered field -/

/-- **A Rogers-type dilogarithm theory** on an ordered field `K`: a function `L` with
reflection and Abel's five-term relation on the open unit interval. -/
structure RogersDilogTheory (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K] where
  L : K → K
  L1 : K
  reflection : ∀ x : K, 0 < x → x < 1 → L x + L (1 - x) = L1
  abel : ∀ x y : K, 0 < x → x < 1 → 0 < y → y < 1 →
    L x + L y - L (x * y) - L (x * (1 - y) / (1 - x * y)) - L (y * (1 - x) / (1 - x * y)) = 0

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem root_bounds {x : K} (hlo : 1 / 2 < x) (hhi : x < 1) :
    (0 < 1 / (2 - x) ∧ 1 / (2 - x) < 1) ∧ (0 < x / (x + 1) ∧ x / (x + 1) < 1)
      ∧ (0 < (1 - x) / x ∧ (1 - x) / x < 1) := by
  have hx0 : (0 : K) < x := lt_trans (by norm_num) hlo
  have h2 : (0 : K) < 2 - x := by linarith
  have h1 : (0 : K) < x + 1 := by linarith
  have h1x : (0 : K) < 1 - x := by linarith
  refine ⟨⟨by positivity, ?_⟩, ⟨by positivity, ?_⟩, ⟨by positivity, ?_⟩⟩
  · rw [div_lt_one h2]; linarith
  · rw [div_lt_one h1]; linarith
  · rw [div_lt_one hx0]
    have : (1 : K) < 2 * x := by
      have := mul_lt_mul_of_pos_left hlo (by norm_num : (0 : K) < 2)
      simpa using this
    linarith

/-- **The level-7 numerators `(17, 5, −1)` hold in every Rogers-type theory.**
No analysis: the inputs are the two fields of the structure and the cubic. -/
theorem RogersDilogTheory.numerators (T : RogersDilogTheory K) {x : K}
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hlo : 1 / 2 < x) (hhi : x < 1) :
    (7 * (2 * T.L1 + 2 * T.L x - T.L (1 / (2 - x))) = 17 * T.L1)
      ∧ (7 * (2 * T.L x - T.L (x / (x + 1))) = 5 * T.L1)
      ∧ (7 * (-(2 * T.L1) + 2 * T.L x + T.L ((1 - x) / x)) = -T.L1) := by
  obtain ⟨⟨hq0, hq1⟩, ⟨hr0, hr1⟩, ⟨hs0, hs1⟩⟩ := root_bounds hlo hhi
  have hx0 : (0 : K) < x := lt_trans (by norm_num) hlo
  have h2' : (0 : K) < 2 - x := by linarith
  have h1 : (0 : K) < x + 1 := by linarith
  have hxx : (1 : K) - x * x ≠ 0 := by nlinarith
  have hq : (1 / (2 - x)) * (2 - x) = 1 := by field_simp
  have hr : (x / (x + 1)) * (x + 1) = x := by field_simp
  have hs : ((1 - x) / x) * x = 1 - x := by field_simp
  have one_sub : ∀ t : K, 0 < t → t < 1 → T.L (1 - t) = T.L1 - T.L t := fun t h0 h1 => by
    have := T.reflection t h0 h1; linear_combination this
  exact FiveTwoFiveTermArguments.numerators_of_abel T.L T.L1 hx hq hr hs hxx
    (one_sub x hx0 hhi) (one_sub _ hq0 hq1) (one_sub _ hr0 hr1) (one_sub _ hs0 hs1)
    (T.abel x x hx0 hhi hx0 hhi)
    (T.abel (1 - x) (1 / (2 - x)) (by linarith) (by linarith) hq0 hq1)
    (T.abel x ((1 - x) / x) hx0 hhi hs0 hs1)

/-! ## Part B — Bloch–Wigner-type theories on a field (Suslin orientation) -/

/-- **A Bloch–Wigner-type dilogarithm theory** on a field `F` with values in an abelian
group `A`: oddness under `z ↦ 1/z` and Suslin's five-term relation, in the orientation of
`QOU.Archimedean.SuslinFiveTerm` (PR #7946). The corpus's `PentagonCoherent` uses the inverted
orientation and forces `D = 0`. -/
structure SuslinDilogTheory (F : Type*) [Field F] (A : Type*) [AddCommGroup A] where
  D : F → A
  inv_odd : ∀ z : F, z ≠ 0 → D (1 / z) = -D z
  five : ∀ x y : F, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
    D x - D y + D (y / x) - D ((1 - x⁻¹) / (1 - y⁻¹)) + D ((1 - x) / (1 - y)) = 0

variable {F : Type*} [Field F] {A : Type*} [AddCommGroup A]

/-- **The anharmonic orbit**, given reflection oddness `D(1 − z) = −D z`: the six cross-ratio
images of `z` carry `±D z`. Pure algebra. Reflection is a hypothesis here, not a field: it is
proved for the Bloch–Wigner instance in `FiveTermProof.blochD_one_sub`; see
`blochWigner_anharmonic`. -/
theorem SuslinDilogTheory.anharmonic (T : SuslinDilogTheory F A)
    (hrefl : ∀ z : F, T.D (1 - z) = -T.D z) {z : F} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    T.D (1 / (1 - z)) = T.D z ∧ T.D ((z - 1) / z) = T.D z ∧ T.D (z / (z - 1)) = -T.D z := by
  have h1z : (1 : F) - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
  have hA : T.D (1 / (1 - z)) = T.D z := by
    rw [T.inv_odd _ h1z, hrefl, neg_neg]
  have hB : T.D ((z - 1) / z) = T.D z := by
    have : (z - 1) / z = 1 - 1 / z := by field_simp
    rw [this, hrefl, T.inv_odd _ hz0, neg_neg]
  refine ⟨hA, hB, ?_⟩
  have hne : (z - 1) / z ≠ 0 := div_ne_zero (sub_ne_zero.mpr hz1) hz0
  have : z / (z - 1) = 1 / ((z - 1) / z) := by
    field_simp
  rw [this, T.inv_odd _ hne, hB]

end QOU.QBeta.DilogTheory
