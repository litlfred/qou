import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# The r = 5 affine-Weyl fold of the Ê₈ mark vector — exact algebra behind the
# Lawrence–Rozansky modulus identification on Σ(2,3,5)

Companion to `computations/lr_modulus_identification_sigma235.py` (PR #3822, the
W_λ keystone's last open piece).  That probe establishes the **corrected exact
identity**

  `|S_{0λ}^{(m)}(ζ)| = 2·|[mark λ]_{ζ^m}| / D_Ê₈(ζ^m)`,  `ζ = e^{iπ/5}`, `m = 1, 2`,

for the 9 affine-Ê₈ McKay nodes of `2I` (marks `1,2,3,4,5,6,4,2,3`), with the two
flat connections of `Σ(2,3,5)` as the two Galois embeddings.  This file proves the
**algebraic core** of that identity — everything that is pure ring/field algebra —
sorry-free:

* the Chebyshev fold values of the quantum integers `[m]` at the two folds
  (`2cos(π/5) = φ`, `2cos(2π/5) = φ − 1`, with `φ² = φ + 1`): `[3] = φ`, `[4] = 1`,
  `[5] = 0`, `[6] = −1` (first fold) and the Galois-conjugate values (second fold);
* the Ê₈-node normalizers `D²(ζ) = 8 + 4φ` and `D²(ζ²) = 12 − 4φ`
  (= `10 ± 2√5` under `φ = (1+√5)/2`);
* the **fold multiplicity** `D_Ê₈² = 2·D_MTC²` (the 9-node set folds 2:1 onto the
  r = 5 alcove `{1,2,3,4}`, node 5 → 0) — the exact origin of the global factor 2
  (resp. √2) correcting the conjectured modulus identification;
* the **core normalization identity** `(10−2s)(10+2s) = 80` for `s² = 5`, which is
  exactly `((2/√5)·sin(mπ/5))² · D²(ζ^m) = 4` — the factor-2-corrected modulus
  identity at the vacuum node, whence at every node by multiplying with `[mark]²`.

What is **not** in this file: the colored Lawrence–Rozansky flat-connection
amplitudes `A_m(α) = ±(2/√5)·sin(αmπ/5)`.  Its **bare (α = 1) case is now a Lean
theorem** — the real-trigonometric identity `A_m(1)² = 4/D²(ζ^m)` is proved in the
archimedean companion
[`KeystoneLRAmplitudeReal.lean`](KeystoneLRAmplitudeReal.lean) (§7c: `Real.sin`
lives in a separate file from this generic-field core), promoting the
former ~1% machine-evidence to exact.  The full colored `α ≥ 2` amplitude and the
`q₀` archimedean continuation (the `loc_matches` gate) remain open.

## Base ring (§7c)

Generic: the fold lemmas need only `[CommRing R]` with a golden element
`φ² = φ + 1`; the normalization identity needs only `[Field K]` with `s² = 5`
(rational literals, no `ℝ`, no `Real.sqrt`, no ordering).

Refs:
- [hikami2005brieskorn] https://doi.org/10.1142/S0129167X05003004
- [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
- [fintushelstern1990] https://doi.org/10.1112/plms/s3-61.1.109
-/

namespace QOU.BraidKnot.KeystoneLRModulusFold

section Fold

variable {R : Type*} [CommRing R]

/-- Chebyshev-recursed quantum integer `[n]` at a fold parameter `t = ζ + ζ⁻¹`:
`[0] = 0`, `[1] = 1`, `[n+2] = t·[n+1] − [n]`. -/
def qi (t : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | n + 2 => t * qi t (n + 1) - qi t n

@[simp] lemma qi_zero (t : R) : qi t 0 = 0 := rfl
@[simp] lemma qi_one (t : R) : qi t 1 = 1 := rfl
lemma qi_two (t : R) : qi t 2 = t := by simp [qi]
lemma qi_three (t : R) : qi t 3 = t * t - 1 := by simp [qi]
lemma qi_four (t : R) : qi t 4 = t * (t * t - 1) - t := by
  show t * qi t 3 - qi t 2 = _
  rw [qi_three, qi_two]
lemma qi_five (t : R) : qi t 5 = t * (t * (t * t - 1) - t) - (t * t - 1) := by
  show t * qi t 4 - qi t 3 = _
  rw [qi_four, qi_three]
lemma qi_six (t : R) : qi t 6 = t * (t * (t * (t * t - 1) - t) - (t * t - 1))
    - (t * (t * t - 1) - t) := by
  show t * qi t 5 - qi t 4 = _
  rw [qi_five, qi_four]

/-- The affine-Ê₈ marks (= dimensions of the 2I irreps), trivial node included. -/
def marks : List ℕ := [1, 2, 3, 4, 5, 6, 4, 2, 3]

/-- `Σ mark² = 120 = |2I|` — the `q = 1` group-side anchor. -/
lemma sum_marks_sq : (marks.map fun m => m * m).sum = 120 := by decide

/-! ### First fold: `t = 2cos(π/5) = φ` -/

lemma qi_phi_three {φ : R} (hφ : φ ^ 2 = φ + 1) : qi φ 3 = φ := by
  rw [qi_three]; linear_combination hφ

lemma qi_phi_four {φ : R} (hφ : φ ^ 2 = φ + 1) : qi φ 4 = 1 := by
  rw [qi_four]; linear_combination (φ + 1) * hφ

lemma qi_phi_five {φ : R} (hφ : φ ^ 2 = φ + 1) : qi φ 5 = 0 := by
  rw [qi_five]; linear_combination (φ ^ 2 + φ - 1) * hφ

lemma qi_phi_six {φ : R} (hφ : φ ^ 2 = φ + 1) : qi φ 6 = -1 := by
  rw [qi_six]; linear_combination (φ ^ 3 + φ ^ 2 - 2 * φ - 1) * hφ

/-- `D_Ê₈²` at the first fold: the sum of `[mark]²` over the 9 nodes is `8 + 4φ`
(= `10 + 2√5` at `φ = (1+√5)/2`). -/
theorem D2_E8_first_fold {φ : R} (hφ : φ ^ 2 = φ + 1) :
    (marks.map fun m => qi φ m * qi φ m).sum = 8 + 4 * φ := by
  simp only [marks, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  rw [qi_one, qi_two, qi_phi_three hφ, qi_phi_four hφ, qi_phi_five hφ, qi_phi_six hφ]
  linear_combination 4 * hφ

/-- `D_MTC²`: the sum of `[α]²` over the r = 5 alcove `{1,2,3,4}` is `4 + 2φ`. -/
theorem D2_MTC_first_fold {φ : R} (hφ : φ ^ 2 = φ + 1) :
    qi φ 1 * qi φ 1 + qi φ 2 * qi φ 2 + qi φ 3 * qi φ 3 + qi φ 4 * qi φ 4
      = 4 + 2 * φ := by
  rw [qi_one, qi_two, qi_phi_three hφ, qi_phi_four hφ]
  linear_combination 2 * hφ

/-- **Fold multiplicity**: `D_Ê₈² = 2·D_MTC²` — the affine-Ê₈ node set folds 2:1
onto the r = 5 alcove (node 5 → 0).  This is the exact origin of the global
factor 2 (resp. √2) correcting the conjectured modulus identification. -/
theorem fold_multiplicity {φ : R} (hφ : φ ^ 2 = φ + 1) :
    (marks.map fun m => qi φ m * qi φ m).sum
      = 2 * (qi φ 1 * qi φ 1 + qi φ 2 * qi φ 2 + qi φ 3 * qi φ 3
              + qi φ 4 * qi φ 4) := by
  rw [D2_E8_first_fold hφ, D2_MTC_first_fold hφ]; ring

/-! ### Second fold (Galois conjugate): `t = 2cos(2π/5) = φ − 1` -/

lemma qi_phi'_three {φ : R} (hφ : φ ^ 2 = φ + 1) : qi (φ - 1) 3 = 1 - φ := by
  rw [qi_three]; linear_combination hφ

lemma qi_phi'_four {φ : R} (hφ : φ ^ 2 = φ + 1) : qi (φ - 1) 4 = -1 := by
  rw [qi_four]; linear_combination (φ - 2) * hφ

lemma qi_phi'_five {φ : R} (hφ : φ ^ 2 = φ + 1) : qi (φ - 1) 5 = 0 := by
  rw [qi_five]; linear_combination (φ ^ 2 - 3 * φ + 1) * hφ

lemma qi_phi'_six {φ : R} (hφ : φ ^ 2 = φ + 1) : qi (φ - 1) 6 = 1 := by
  rw [qi_six]; linear_combination (φ ^ 3 - 4 * φ ^ 2 + 3 * φ + 1) * hφ

/-- `D_Ê₈²` at the second fold is `12 − 4φ` (= `10 − 2√5`): the Galois conjugate
of `8 + 4φ` under `φ ↦ 1 − φ`. -/
theorem D2_E8_second_fold {φ : R} (hφ : φ ^ 2 = φ + 1) :
    (marks.map fun m => qi (φ - 1) m * qi (φ - 1) m).sum = 12 - 4 * φ := by
  simp only [marks, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  rw [qi_one, qi_two, qi_phi'_three hφ, qi_phi'_four hφ, qi_phi'_five hφ,
    qi_phi'_six hφ]
  linear_combination 4 * hφ

/-- Alcove sum of squared quantum integers at the second fold `t = φ − 1`:
`[1]² + [2]² + [3]² + [4]² = 6 − 2φ`. -/
theorem D2_MTC_second_fold {φ : R} (hφ : φ ^ 2 = φ + 1) :
    qi (φ - 1) 1 * qi (φ - 1) 1 + qi (φ - 1) 2 * qi (φ - 1) 2
      + qi (φ - 1) 3 * qi (φ - 1) 3 + qi (φ - 1) 4 * qi (φ - 1) 4
      = 6 - 2 * φ := by
  rw [qi_one, qi_two, qi_phi'_three hφ, qi_phi'_four hφ]
  linear_combination 2 * hφ

/-- **Second-fold multiplicity**: the 9-node sum at `t = φ − 1` also equals twice
the 4-node alcove sum (`12 − 4φ = 2 · (6 − 2φ)`). -/
theorem fold_multiplicity_second {φ : R} (hφ : φ ^ 2 = φ + 1) :
    (marks.map fun m => qi (φ - 1) m * qi (φ - 1) m).sum
      = 2 * (qi (φ - 1) 1 * qi (φ - 1) 1 + qi (φ - 1) 2 * qi (φ - 1) 2
              + qi (φ - 1) 3 * qi (φ - 1) 3 + qi (φ - 1) 4 * qi (φ - 1) 4) := by
  rw [D2_E8_second_fold hφ, D2_MTC_second_fold hφ]; ring

/-- **Trace and norm of the two fold normalizers in `[CommRing R]`**: the sum of the
first-fold and second-fold 9-node normalizers is `20` and their product is `80`
directly from `φ² = φ + 1`, without adjoining `√5` or inverting `2`. -/
theorem D2_E8_fold_sum_and_product {φ : R} (hφ : φ ^ 2 = φ + 1) :
    (marks.map fun m => qi φ m * qi φ m).sum
      + (marks.map fun m => qi (φ - 1) m * qi (φ - 1) m).sum = 20 ∧
    (marks.map fun m => qi φ m * qi φ m).sum
      * (marks.map fun m => qi (φ - 1) m * qi (φ - 1) m).sum = 80 := by
  rw [D2_E8_first_fold hφ, D2_E8_second_fold hφ]
  exact ⟨by ring, by linear_combination (-16 : R) * hφ⟩

end Fold

section Normalization

variable {K : Type*} [Field K]

/-- **Core normalization identity**: for `s² = 5` (a square root of 5 in any
characteristic-zero field), `(10 − 2s)(10 + 2s) = 80`.  Under `s = √5` this is
exactly `((2/√5)·sin(π/5))² · D_Ê₈(ζ)² = 4` — i.e. the vacuum-node case of the
factor-2-corrected modulus identity `|A_m(mark)|·D_Ê₈(ζ^m) = 2·|[mark]_{ζ^m}|` —
since `sin²(π/5) = (10−2√5)/16` and `D_Ê₈(ζ)² = 10+2√5` (and Galois-symmetrically
for the second flat connection, `sin²(2π/5) = (10+2√5)/16`, `D² = 10−2√5`). -/
theorem core_normalization (s : K) (hs : s ^ 2 = 5) :
    (10 - 2 * s) * (10 + 2 * s) = 80 := by
  linear_combination (-4 : K) * hs

/-- The vacuum-node modulus identity, first flat connection, written out:
`(4/5)·((10−2s)/16)·(10+2s) = 4` — `|A₁(1)|² · D_Ê₈(ζ)² = 4·[1]²`. -/
theorem vacuum_modulus_identity_first [CharZero K] (s : K) (hs : s ^ 2 = 5) :
    (4 / 5 : K) * ((10 - 2 * s) / 16) * (10 + 2 * s) = 4 := by
  field_simp
  linear_combination (-4 : K) * hs

/-- The vacuum-node modulus identity, second flat connection (Galois conjugate):
`(4/5)·((10+2s)/16)·(10−2s) = 4`. -/
theorem vacuum_modulus_identity_second [CharZero K] (s : K) (hs : s ^ 2 = 5) :
    (4 / 5 : K) * ((10 + 2 * s) / 16) * (10 - 2 * s) = 4 := by
  field_simp
  linear_combination (-4 : K) * hs

/-- The golden element `(1+s)/2` satisfies the fold relation `φ² = φ + 1`, tying
the two sections: the fold parameter of `qi` at the first flat connection is the
golden ratio of the same `√5` that carries the normalization identity. -/
theorem golden_of_sqrt5 [CharZero K] (s : K) (hs : s ^ 2 = 5) :
    ((1 + s) / 2) ^ 2 = (1 + s) / 2 + 1 := by
  field_simp
  linear_combination hs

end Normalization

end QOU.BraidKnot.KeystoneLRModulusFold
