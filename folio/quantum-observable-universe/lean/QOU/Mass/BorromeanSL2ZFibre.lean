import QOU.Mass.BorromeanWordForcing
import Mathlib.Data.Complex.Basic
import QOU.MathlibExt.SL2ZPositiveWords

/-!
# The same-character fibre of `β_Bor` at writhe 0, at every length

Thread "Derive the proton's Borromean braid" (2026-11-22). Companion of
`QOU.Mass.BorromeanWordForcing`. The mass identity sees a writhe-0 word only through its
`(2,1)` character `χ₍₂,₁₎`. `fibre` shows that the words with `β_Bor`'s character are
exactly `β_Bor`'s conjugacy class, at any length.

## The argument (structural, with one small check)

1. At `q = i` the character of a writhe-0 word is the trace of its image under the
   Burau representation at `t = −1`, `B₃ → SL(2, ℤ)` (`chi21_I`); for `β_Bor` it is 18.
2. That image is conjugate to a positive word in `R = [[1,1],[0,1]]`, `L = [[1,0],[1,1]]`
   (`PositiveRepresentatives`, proved as `positiveRepresentatives` from
   `QOU.MathlibExt.SL2Z.exists_conj_posProd`).
3. **Trace bound** (`ptr_ge`): `r` letters `R` and `l` letters `L` give trace at least
   `2 + r·l`. With one letter of a kind the trace is exactly `2 +` the other count
   (`ptr_oneL`, `ptr_oneR`).
4. Lifting the conjugacy back to `B₃` costs a power of `Δ⁴`, which has writhe 12
   (`lift_conj`, hypothesis `KernelIsDeltaFour`). So writhe 0 forces `r ≡ l (mod 12)`.
   With `r·l ≤ 16` and step 3 this leaves `r = l ≤ 4`.
5. With `n ≤ 4` letters of each kind, trace 18 is the top of the `n = 3` range,
   `(RL)³ = β_Bor`, or the bottom of the `n = 4` range, `R⁴L⁴` (`trace18_small`, a
   `decide` over 340 words).
6. `χ₍₂,₁₎` is a class function on `B₃` (`chi21_conj`), and `R⁴L⁴` has a different value
   at `q = 2`. So only `β_Bor` remains.

## Classical facts

* `KernelIsDeltaFour` (from `BorromeanWordForcing`): the kernel of `B₃ → SL(2, ℤ)` is
  `⟨Δ⁴⟩`, `Δ = σ₀σ₁σ₀`. **Still a named hypothesis** here; surjectivity is proved
  (`burauNeg_surjective`).
* `PositiveRepresentatives`: every element of `SL(2, ℤ)` of trace `> 2` is conjugate to
  a positive `R/L` word. **Proved** (`positiveRepresentatives`, via
  `QOU.MathlibExt.SL2Z.exists_conj_posProd`, sorry-free, standard axioms).

So `fibre_of_kernel` is conditional on the kernel fact alone.

No measured value enters.
-/

namespace QOU.Mass.BorromeanSL2ZFibre

open QOU.Mass.GammaGammaWordSelection QOU.MathlibExt.Braid QOU.Mass.BorromeanWordForcing

/-! ## Positive words in `R = [[1,1],[0,1]]` and `L = [[1,0],[1,1]]` -/

/-- A `2 × 2` matrix of natural numbers, `[[a, b], [c, d]]`. -/
structure NM where
  a : ℕ
  b : ℕ
  c : ℕ
  d : ℕ
deriving DecidableEq

/-- The product of a positive word (`true = R`, `false = L`), multiplied on the left. -/
def posMat : List Bool → NM
  | [] => ⟨1, 0, 0, 1⟩
  | true :: u => ⟨(posMat u).a + (posMat u).c, (posMat u).b + (posMat u).d,
      (posMat u).c, (posMat u).d⟩
  | false :: u => ⟨(posMat u).a, (posMat u).b,
      (posMat u).a + (posMat u).c, (posMat u).b + (posMat u).d⟩

/-- Its trace. -/
def ptr (u : List Bool) : ℕ := (posMat u).a + (posMat u).d

/-- **The trace bound.** A positive word with `r` letters `R` and `l` letters `L` has
trace at least `2 + r·l`: prepending `R` adds the lower-left entry (at least `l`),
prepending `L` adds the upper-right entry (at least `r`). -/
theorem posMat_bound (u : List Bool) :
    1 ≤ (posMat u).a ∧ 1 ≤ (posMat u).d ∧ u.count true ≤ (posMat u).b ∧
      u.count false ≤ (posMat u).c ∧ 2 + u.count true * u.count false ≤ ptr u := by
  induction u with
  | nil => simp [posMat, ptr]
  | cons x u ih =>
    obtain ⟨h1, h2, h3, h4, h5⟩ := ih
    simp only [ptr] at h5
    cases x
    · simp only [posMat, ptr, List.count_cons, beq_iff_eq, reduceCtorEq, if_false, if_true, add_zero]
      refine ⟨by omega, by omega, by omega, by omega, ?_⟩
      nlinarith
    · simp only [posMat, ptr, List.count_cons, beq_iff_eq, reduceCtorEq, if_false, if_true, add_zero]
      refine ⟨by omega, by omega, by omega, by omega, ?_⟩
      nlinarith

theorem ptr_ge (u : List Bool) : 2 + u.count true * u.count false ≤ ptr u :=
  (posMat_bound u).2.2.2.2

/-! ### One letter of a kind: the trace is `2 + (number of the other letter)` -/

theorem posMat_noL (u : List Bool) (h : u.count false = 0) :
    posMat u = ⟨1, u.count true, 0, 1⟩ := by
  induction u with
  | nil => rfl
  | cons x u ih =>
    cases x
    · simp at h
    · simp only [List.count_cons, beq_iff_eq, reduceCtorEq, if_false, add_zero] at h
      simp [posMat, ih h]

theorem posMat_noR (u : List Bool) (h : u.count true = 0) :
    posMat u = ⟨1, 0, u.count false, 1⟩ := by
  induction u with
  | nil => rfl
  | cons x u ih =>
    cases x
    · simp only [List.count_cons, beq_iff_eq, reduceCtorEq, if_false, add_zero] at h
      simp [posMat, ih h, add_comm]
    · simp at h

theorem ptr_oneL (u : List Bool) (h : u.count false = 1) :
    (posMat u).c = 1 ∧ ptr u = 2 + u.count true := by
  induction u with
  | nil => simp at h
  | cons x u ih =>
    cases x
    · simp only [List.count_cons, beq_iff_eq, if_true] at h
      have h0 : u.count false = 0 := by simpa using h
      simp [posMat, ptr, posMat_noL u h0]; omega
    · simp only [List.count_cons, beq_iff_eq, reduceCtorEq, if_false, add_zero] at h
      obtain ⟨hc, ht⟩ := ih h
      simp only [ptr] at ht
      simp [posMat, ptr, hc]; omega

theorem ptr_oneR (u : List Bool) (h : u.count true = 1) :
    (posMat u).b = 1 ∧ ptr u = 2 + u.count false := by
  induction u with
  | nil => simp at h
  | cons x u ih =>
    cases x
    · simp only [List.count_cons, beq_iff_eq, reduceCtorEq, if_false, add_zero] at h
      obtain ⟨hb, ht⟩ := ih h
      simp only [ptr] at ht
      simp [posMat, ptr, hb]; omega
    · simp only [List.count_cons, beq_iff_eq, if_true] at h
      have h0 : u.count true = 0 := by simpa using h
      simp [posMat, ptr, posMat_noR u h0]; omega

/-! ### The small check: `n` letters of each kind, `n ≤ 4` -/

/-- All Boolean words of length `n`. -/
def allWords : ℕ → List (List Bool)
  | 0 => [[]]
  | n + 1 => (allWords n).flatMap fun w => [true :: w, false :: w]

theorem mem_allWords (u : List Bool) : u ∈ allWords u.length := by
  induction u with
  | nil => simp [allWords]
  | cons x u ih =>
    simp only [List.length_cons, allWords, List.mem_flatMap]
    exact ⟨u, ih, by cases x <;> simp⟩

/-- The rotations of `RLRLRL` and of `R⁴L⁴`. -/
def bor6 : List (List Bool) :=
  [[true, false, true, false, true, false], [false, true, false, true, false, true]]

def r4l4 : List (List Bool) :=
  [[true, true, true, true, false, false, false, false],
   [true, true, true, false, false, false, false, true],
   [true, true, false, false, false, false, true, true],
   [true, false, false, false, false, true, true, true],
   [false, false, false, false, true, true, true, true],
   [false, false, false, true, true, true, true, false],
   [false, false, true, true, true, true, false, false],
   [false, true, true, true, true, false, false, false]]

/-- **The confirmation.** With `n ≤ 4` letters of each kind, trace 18 occurs only for
the rotations of `(RL)³` (the top of the `n = 3` range) and of `R⁴L⁴` (the bottom of
the `n = 4` range). 340 words. -/
theorem trace18_small :
    ∀ n < 5, ∀ u ∈ allWords (2 * n), u.count true = n → ptr u = 18 →
      u ∈ bor6 ∨ u ∈ r4l4 := by
  decide +kernel

/-! ## Positive words as braids -/

/-- A positive word as a `B₃` word: `R ↦ σ₀`, `L ↦ σ₁⁻¹`. -/
def toWord (u : List Bool) : Word := u.map fun x => if x then a else b'

theorem eval_cons (c : Crossing) (w : Word) : eval (c :: w) = evalLetter c * eval w := by
  simp [eval]

/-- `burauNeg` sends a positive word to its `R/L` product. -/
theorem burauNeg_toWord (u : List Bool) :
    ((burauNeg (eval (toWord u)) : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
      Matrix (Fin 2) (Fin 2) ℤ) =
      !![((posMat u).a : ℤ), (posMat u).b; (posMat u).c, (posMat u).d] := by
  induction u with
  | nil => ext i j; fin_cases i <;> fin_cases j <;> simp [toWord, eval, posMat]
  | cons x u ih =>
    cases x
    · simp only [toWord, List.map_cons, Bool.false_eq_true, if_false] at ih ⊢
      rw [eval_cons, map_mul, Matrix.SpecialLinearGroup.coe_mul, ih]
      simp only [evalLetter, Bool.false_eq_true, if_false, one_ne_zero, map_inv, burauNeg_σ]
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [burauGen, posMat, Matrix.SpecialLinearGroup.coe_inv, Matrix.adjugate_fin_two,
          Matrix.mul_apply, Fin.sum_univ_two]
    · simp only [toWord, List.map_cons, if_true] at ih ⊢
      rw [eval_cons, map_mul, Matrix.SpecialLinearGroup.coe_mul, ih]
      simp only [evalLetter, if_true, burauNeg_σ]
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [burauGen, posMat, Matrix.mul_apply, Fin.sum_univ_two]

theorem trace_burauNeg_toWord (u : List Bool) :
    ((burauNeg (eval (toWord u)) : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
      Matrix (Fin 2) (Fin 2) ℤ).trace = (ptr u : ℤ) := by
  rw [burauNeg_toWord]; simp [Matrix.trace_fin_two, ptr]

theorem writhe_toWord (u : List Bool) :
    writhe (toWord u) = (u.count true : ℤ) - u.count false := by
  induction u with
  | nil => simp [toWord, writhe]
  | cons x u ih =>
    simp only [toWord, writhe, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]; cases x <;> simp [sign] <;> ring

/-- The writhe homomorphism on a word is its writhe. -/
theorem exponentSum_eval (w : Word) :
    exponentSum 2 (eval w) = Multiplicative.ofAdd (writhe w) := by
  induction w with
  | nil => simp [eval, writhe]
  | cons c w ih =>
    rw [eval_cons, map_mul, ih]
    simp only [writhe, List.map_cons, List.sum_cons, ofAdd_add]
    congr 1
    rcases c with ⟨g, _ | _⟩ <;> simp [evalLetter, sign]

/-! ## The `(2,1)` character is a class function on `B₃` -/

section Rep

variable {R : Type*} [Field R]

/-- `Tᵢ` as a unit, with inverse `Tᵢ⁻¹`. -/
def heckeUnit (q : R) (hq : q ≠ 0) (i : Fin 2) : (Matrix (Fin 2) (Fin 2) R)ˣ :=
  ⟨heckeMat q ⟨i, true⟩, heckeMat q ⟨i, false⟩, heckeMat_inv q hq i i.isLt true,
    by simpa using heckeMat_inv q hq i i.isLt false⟩

theorem heckeUnit_relators (q : R) (hq : q ≠ 0) :
    ∀ r ∈ braidRelators 2, (FreeGroup.lift (heckeUnit q hq)) r = 1 := by
  rintro r (⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩)
  · exfalso; have := i.isLt; have := j.isLt; omega
  · have hi : i = 0 := by ext; have := i.isLt; simp at h ⊢; omega
    subst hi
    simp only [map_mul, map_inv, FreeGroup.lift_apply_of, mul_inv_eq_one]
    ext : 1
    simpa [heckeUnit] using heckeMat_braid q hq

/-- The `(2,1)` representation of `B₃`. -/
def rep21Hom (q : R) (hq : q ≠ 0) : BraidGroup 2 →* (Matrix (Fin 2) (Fin 2) R)ˣ :=
  PresentedGroup.toGroup (heckeUnit_relators q hq)

theorem rep21Hom_σ (q : R) (hq : q ≠ 0) (i : Fin 2) : rep21Hom q hq (σ i) = heckeUnit q hq i :=
  PresentedGroup.toGroup.of _

theorem rep21Hom_eval (q : R) (hq : q ≠ 0) (w : Word) (hw : InB3Letters w) :
    ((rep21Hom q hq (eval w) : (Matrix (Fin 2) (Fin 2) R)ˣ) : Matrix (Fin 2) (Fin 2) R) =
      rep21 q w := by
  induction w with
  | nil => simp [eval, rep21]
  | cons c w ih =>
    rw [eval_cons, map_mul, Units.val_mul, ih (fun x hx => hw x (List.mem_cons_of_mem _ hx))]
    have hc := hw c List.mem_cons_self
    simp only [rep21, List.map_cons, List.prod_cons]
    congr 1
    simp only [letters, List.mem_cons, List.not_mem_nil, or_false] at hc
    rcases hc with rfl | rfl | rfl | rfl <;>
      simp [evalLetter, map_inv, rep21Hom_σ, heckeUnit]

/-- **`χ₍₂,₁₎` is a class function:** conjugate braids have the same character. -/
theorem chi21_conj (q : R) (hq : q ≠ 0) {w v : Word} (hw : InB3Letters w)
    (hv : InB3Letters v) (h : IsConj (eval w) (eval v)) : chi21 q w = chi21 q v := by
  obtain ⟨c, hc⟩ := isConj_iff.mp h
  have := congrArg (fun g => ((rep21Hom q hq g : (Matrix (Fin 2) (Fin 2) R)ˣ) :
    Matrix (Fin 2) (Fin 2) R)) hc
  simp only [map_mul, map_inv, Units.val_mul, rep21Hom_eval q hq w hw,
    rep21Hom_eval q hq v hv] at this
  rw [chi21, chi21, ← this, Matrix.trace_mul_cycle, Units.inv_mul, one_mul]

end Rep

/-! ## At `q = i` the `(2,1)` character of a writhe-0 word is the `SL(2, ℤ)` trace -/

section AtI

open Complex

/-- The integer matrix of a braid, cast to `ℂ`. -/
def burauC (g : BraidGroup 2) : Matrix (Fin 2) (Fin 2) ℂ :=
  ((burauNeg g : Matrix.SpecialLinearGroup (Fin 2) ℤ) : Matrix (Fin 2) (Fin 2) ℤ).map
    (Int.castRingHom ℂ)

theorem heckeMat_I (c : Crossing) (hc : c ∈ letters) :
    heckeMat I c = I ^ sign c • burauC (evalLetter c) := by
  simp only [letters, List.mem_cons, List.not_mem_nil, or_false] at hc
  rcases hc with rfl | rfl | rfl | rfl <;>
    (ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeMat, burauC, evalLetter, sign, burauNeg_σ, burauGen,
        Matrix.SpecialLinearGroup.coe_inv, Matrix.adjugate_fin_two])

theorem rep21_I (w : Word) (hw : InB3Letters w) :
    rep21 I w = I ^ writhe w • burauC (eval w) := by
  induction w with
  | nil => ext i j; fin_cases i <;> fin_cases j <;> simp [rep21, burauC, eval, writhe]
  | cons c w ih =>
    have hc := hw c List.mem_cons_self
    rw [show rep21 I (c :: w) = heckeMat I c * rep21 I w by simp [rep21],
      heckeMat_I c hc, ih (fun x hx => hw x (List.mem_cons_of_mem _ hx)), smul_mul_smul_comm,
      ← zpow_add₀ I_ne_zero, eval_cons,
      show writhe (c :: w) = sign c + writhe w by simp [writhe]]
    congr 1
    rw [burauC, burauC, burauC, map_mul, Matrix.SpecialLinearGroup.coe_mul, Matrix.map_mul]

/-- At writhe 0, `χ₍₂,₁₎(i)` is the trace of the `SL(2, ℤ)` image. -/
theorem chi21_I (w : Word) (hw : InB3Letters w) (h0 : writhe w = 0) :
    chi21 I w = (((burauNeg (eval w) : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
      Matrix (Fin 2) (Fin 2) ℤ).trace : ℂ) := by
  rw [chi21, rep21_I w hw, h0, zpow_zero, one_smul]
  simp [burauC, Matrix.trace_fin_two]

theorem chi21_borromean_I : chi21 I [a, b', a, b', a, b'] = 18 := by
  have h2 : I ^ 2 = -1 := I_sq
  have h2' : I⁻¹ ^ 2 = -1 := by rw [inv_I, neg_sq, I_sq]
  have h4 : I ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2]; norm_num
  have h4' : I⁻¹ ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2']; norm_num
  have h6 : I ^ 6 = -1 := by rw [show (6 : ℕ) = 2 * 3 from rfl, pow_mul, h2]; norm_num
  have h6' : I⁻¹ ^ 6 = -1 := by rw [show (6 : ℕ) = 2 * 3 from rfl, pow_mul, h2']; norm_num
  rw [chi21_borromean I I_ne_zero, h2, h2', h4, h4', h6, h6']
  norm_num

end AtI

/-! ## The fibre theorem -/

theorem toWord_letters (u : List Bool) : InB3Letters (toWord u) := by
  intro c hc
  simp only [toWord, List.mem_map] at hc
  obtain ⟨x, -, rfl⟩ := hc
  cases x <;> simp [letters]

theorem count_add (u : List Bool) : u.count true + u.count false = u.length := by
  induction u with
  | nil => simp
  | cons x u ih => cases x <;> simp <;> omega

/-- **Classical fact (F2):** every element of `SL(2, ℤ)` of trace `> 2` is
conjugate to a positive word in `R = [[1,1],[0,1]]` and `L = [[1,0],[1,1]]`. Proved
below as `positiveRepresentatives`. -/
def PositiveRepresentatives : Prop :=
  ∀ M : Matrix.SpecialLinearGroup (Fin 2) ℤ, 2 < (M : Matrix (Fin 2) (Fin 2) ℤ).trace →
    ∃ u : List Bool, IsConj M (burauNeg (eval (toWord u)))

/-- `burauNeg` of a positive word is the matching `R/L` product of
`QOU.MathlibExt.SL2Z`. -/
theorem burauNeg_toWord_eq_posProd (u : List Bool) :
    burauNeg (eval (toWord u)) = QOU.MathlibExt.SL2Z.posProd u := by
  induction u with
  | nil => simp [toWord, eval]
  | cons x u ih =>
    cases x
    · simp only [toWord, List.map_cons, Bool.false_eq_true, if_false] at ih ⊢
      rw [eval_cons, map_mul, ih, QOU.MathlibExt.SL2Z.posProd_cons_false]
      congr 1
      simp only [evalLetter, Bool.false_eq_true, if_false, one_ne_zero, map_inv, burauNeg_σ]
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [burauGen, QOU.MathlibExt.SL2Z.L, Matrix.SpecialLinearGroup.coe_inv,
          Matrix.adjugate_fin_two]
    · simp only [toWord, List.map_cons, if_true] at ih ⊢
      rw [eval_cons, map_mul, ih, QOU.MathlibExt.SL2Z.posProd_cons_true]
      congr 1
      simp only [evalLetter, if_true, burauNeg_σ]
      ext i j; fin_cases i <;> fin_cases j <;> simp [burauGen, QOU.MathlibExt.SL2Z.R]

/-- The classical fact (F2), now proved (`QOU.MathlibExt.SL2Z.exists_conj_posProd`). -/
theorem positiveRepresentatives : PositiveRepresentatives := fun M hM => by
  obtain ⟨u, hu⟩ := QOU.MathlibExt.SL2Z.exists_conj_posProd M hM
  exact ⟨u, by rw [burauNeg_toWord_eq_posProd]; exact hu⟩

theorem trace_isConj {M N : Matrix.SpecialLinearGroup (Fin 2) ℤ} (h : IsConj M N) :
    (M : Matrix (Fin 2) (Fin 2) ℤ).trace = (N : Matrix (Fin 2) (Fin 2) ℤ).trace := by
  obtain ⟨c, rfl⟩ := isConj_iff.mp h
  rw [Matrix.SpecialLinearGroup.coe_mul, Matrix.SpecialLinearGroup.coe_mul,
    Matrix.trace_mul_cycle, ← Matrix.SpecialLinearGroup.coe_mul, inv_mul_cancel,
    Matrix.SpecialLinearGroup.coe_one, one_mul]

/-- Conditional on the kernel fact: braids with conjugate `SL(2, ℤ)` images are
conjugate up to a power of `Δ⁴`. -/
theorem lift_conj (hK : KernelIsDeltaFour) {g h : BraidGroup 2}
    (hc : IsConj (burauNeg g) (burauNeg h)) : ∃ k : ℤ, IsConj g ((delta ^ 4) ^ k * h) := by
  rw [isConj_iff] at hc
  obtain ⟨c, hc⟩ := hc
  obtain ⟨c', rfl⟩ := burauNeg_surjective c
  obtain ⟨k, hk⟩ := hK (c' * g * c'⁻¹ * h⁻¹) (by simp [map_mul, map_inv, hc])
  exact ⟨k, isConj_iff.mpr ⟨c', mul_inv_eq_iff_eq_mul.mp hk⟩⟩

/-- **The same-character fibre of `β_Bor` at writhe 0, at every length.** A writhe-0
three-strand word whose `(2,1)` character equals that of `β_Bor` for every `q ≠ 0` is
conjugate to `β_Bor` in `B₃`. Conditional on two classical facts, both named
hypotheses: the kernel of `B₃ → SL(2, ℤ)` is `⟨Δ⁴⟩` (`KernelIsDeltaFour`) and hyperbolic
classes have positive `R/L` representatives (`PositiveRepresentatives`).

Proof. At `q = i` the character is the `SL(2, ℤ)` trace, 18. Its positive
representative has `r` letters `R` and `l` letters `L`, with `2 + r·l ≤ 18`
(`ptr_ge`). Lifting back to `B₃` costs a power of `Δ⁴` (writhe 12), so writhe 0 forces
`r ≡ l (mod 12)`; with `r·l ≤ 16` and the one-letter traces `2 + r`, `2 + l`, this leaves
`r = l ≤ 4`. Among those, trace 18 is `(RL)³` or `R⁴L⁴` (`trace18_small`), and `R⁴L⁴`
has a different character at `q = 2`. -/
theorem fibre (hK : KernelIsDeltaFour) (hP : PositiveRepresentatives) (w : Word)
    (hw : InB3Letters w) (h0 : writhe w = 0)
    (hχ : ∀ q : ℂ, q ≠ 0 → chi21 q w = chi21 q [a, b', a, b', a, b']) :
    IsConj (eval w) (eval [a, b', a, b', a, b']) := by
  have htr : ((burauNeg (eval w) : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
      Matrix (Fin 2) (Fin 2) ℤ).trace = 18 := by
    have := hχ Complex.I Complex.I_ne_zero
    rw [chi21_I w hw h0, chi21_borromean_I] at this
    exact_mod_cast this
  obtain ⟨u, hu⟩ := hP _ (by rw [htr]; norm_num)
  have hpt : ptr u = 18 := by
    have := trace_isConj hu
    rw [htr, trace_burauNeg_toWord] at this
    exact_mod_cast this.symm
  obtain ⟨k, hk⟩ := lift_conj hK hu
  have hwr : (0 : ℤ) = 12 * k + ((u.count true : ℤ) - u.count false) := by
    obtain ⟨c, hc⟩ := isConj_iff.mp hk
    have h1 := congrArg (exponentSum 2) hc
    rw [map_mul, map_mul, map_inv, mul_comm (exponentSum 2 c), mul_inv_cancel_right] at h1
    rw [map_mul, map_zpow, exponentSum_delta_four, exponentSum_eval, exponentSum_eval, h0,
      writhe_toWord] at h1
    have h2 := congrArg Multiplicative.toAdd h1
    simp only [toAdd_ofAdd, toAdd_mul, toAdd_zpow, smul_eq_mul] at h2
    linarith
  have hb := ptr_ge u
  rw [hpt] at hb
  have hr1 : 1 ≤ u.count true := by
    by_contra h
    have := posMat_noR u (by omega)
    simp [ptr, this] at hpt
  have hl1 : 1 ≤ u.count false := by
    by_contra h
    have := posMat_noL u (by omega)
    simp [ptr, this] at hpt
  rcases Nat.lt_or_ge (u.count true) 2 with hr | hr2
  · have := (ptr_oneR u (by omega)).2
    omega
  rcases Nat.lt_or_ge (u.count false) 2 with hl | hl2
  · have := (ptr_oneL u (by omega)).2
    omega
  have hr8 : u.count true ≤ 8 := by nlinarith
  have hl8 : u.count false ≤ 8 := by nlinarith
  have hrl : u.count true = u.count false := by omega
  have hk0 : k = 0 := by omega
  have hr4 : u.count true < 5 := by rw [← hrl] at hb; nlinarith
  have hmem : u ∈ allWords (2 * u.count true) := by
    have := mem_allWords u
    rwa [show u.length = 2 * u.count true by have := count_add u; omega] at this
  subst hk0
  rw [zpow_zero, one_mul] at hk
  rcases trace18_small _ hr4 u hmem rfl hpt with hb6 | hr44
  · simp only [bor6, List.mem_cons, List.not_mem_nil, or_false] at hb6
    rcases hb6 with rfl | rfl
    · exact hk
    · exact hk.trans (eval_borOrbit_conj _ (by simp [borOrbit, toWord]))
  · exfalso
    have h2 := hχ 2 two_ne_zero
    rw [chi21_conj 2 two_ne_zero hw (toWord_letters u) hk] at h2
    simp only [r4l4, List.mem_cons, List.not_mem_nil, or_false] at hr44
    rcases hr44 with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      (simp [chi21, rep21, toWord, heckeMat, Matrix.trace_fin_two] at h2; norm_num at h2)


/-- `fibre` with the positive-representative fact discharged: conditional only on the
kernel fact `KernelIsDeltaFour`. -/
theorem fibre_of_kernel (hK : KernelIsDeltaFour) (w : Word) (hw : InB3Letters w)
    (h0 : writhe w = 0)
    (hχ : ∀ q : ℂ, q ≠ 0 → chi21 q w = chi21 q [a, b', a, b', a, b']) :
    IsConj (eval w) (eval [a, b', a, b', a, b']) :=
  fibre hK positiveRepresentatives w hw h0 hχ

end QOU.Mass.BorromeanSL2ZFibre
