import Mathlib.RingTheory.Adjoin.Basic
import Mathlib.Data.Finset.NAry
import Mathlib.Data.Nat.Factorial.Basic

/-!
# QOU.IwahoriHecke.JonesNormalForm — the Jones normal form spans, and the Markov trace is unique

Placeholder; filled in below.
-/

namespace QOU.IwahoriHecke.JonesNormalForm

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Type-`A` Hecke relations on the first `N` members of a family `s : ℕ → A`,
with an arbitrary quadratic relation `sᵢ² = a·sᵢ + b`. -/
structure HeckeFamily (N : ℕ) (a b : R) (s : ℕ → A) : Prop where
  quad : ∀ i, i < N → s i * s i = a • s i + b • (1 : A)
  braid : ∀ i, i + 1 < N → s i * s (i + 1) * s i = s (i + 1) * s i * s (i + 1)
  comm : ∀ i j, i + 2 ≤ j → j < N → s i * s j = s j * s i

/-- The descending run `dprod s j m = s_{j+m-1} ⋯ s_{j+1} s_j` (`m` letters). -/
def dprod (s : ℕ → A) (j : ℕ) : ℕ → A
  | 0 => 1
  | m + 1 => s (j + m) * dprod s j m

@[simp] theorem dprod_zero (s : ℕ → A) (j : ℕ) : dprod s j 0 = 1 := rfl

theorem dprod_succ (s : ℕ → A) (j m : ℕ) : dprod s j (m + 1) = s (j + m) * dprod s j m := rfl

/-- Peeling the run from the foot: `dprod s j (m+1) = dprod s (j+1) m * s j`. -/
theorem dprod_succ' (s : ℕ → A) (j m : ℕ) : dprod s j (m + 1) = dprod s (j + 1) m * s j := by
  induction m with
  | zero => simp [dprod]
  | succ m ih =>
    rw [dprod_succ, ih, dprod_succ, show j + (m + 1) = j + 1 + m by omega, mul_assoc]

section Relations

variable {N : ℕ} {a b : R} {s : ℕ → A}

/-- A generator strictly below the run commutes past it. -/
theorem comm_dprod_low (hs : HeckeFamily N a b s) {i j : ℕ} (hij : i + 2 ≤ j) :
    ∀ m, j + m ≤ N → s i * dprod s j m = dprod s j m * s i := by
  intro m
  induction m with
  | zero => intro _; simp
  | succ m ih =>
    intro hm
    rw [dprod_succ, ← mul_assoc, hs.comm i (j + m) (by omega) (by omega), mul_assoc,
      ih (by omega), mul_assoc]

/-- A generator strictly above the run (by at least two) commutes past it. -/
theorem comm_dprod_high (hs : HeckeFamily N a b s) {i j : ℕ} (hi : i < N) :
    ∀ m, j + m + 1 ≤ i → s i * dprod s j m = dprod s j m * s i := by
  intro m
  induction m with
  | zero => intro _; simp
  | succ m ih =>
    intro hm
    rw [dprod_succ, ← mul_assoc, ← hs.comm (j + m) i (by omega) hi, mul_assoc,
      ih (by omega), mul_assoc]

/-- A generator above the foot passes through the run with its index lowered by one:
`dprod s j m * s_{i+1} = s_i * dprod s j m` for `j ≤ i`, `i + 2 ≤ j + m`. -/
theorem dprod_push (hs : HeckeFamily N a b s) {i j : ℕ} (hji : j ≤ i) :
    ∀ m, j + m ≤ N → i + 2 ≤ j + m → dprod s j m * s (i + 1) = s i * dprod s j m := by
  intro m
  induction m with
  | zero => intro _ h; omega
  | succ m ih =>
    intro hN him
    by_cases hlt : i + 2 ≤ j + m
    · rw [dprod_succ, mul_assoc, ih (by omega) hlt, ← mul_assoc,
        ← hs.comm i (j + m) (by omega) (by omega), mul_assoc]
    · obtain ⟨m', rfl⟩ : ∃ m', m = m' + 1 := ⟨m - 1, by omega⟩
      have hi : i = j + m' := by omega
      subst hi
      have hhigh := comm_dprod_high hs (i := j + m' + 1) (j := j) (by omega) m' le_rfl
      have hbr := hs.braid (j + m') (by omega)
      show s (j + (m' + 1)) * (s (j + m') * dprod s j m') * s (j + m' + 1)
        = s (j + m') * (s (j + (m' + 1)) * (s (j + m') * dprod s j m'))
      rw [show j + (m' + 1) = j + m' + 1 by omega]
      calc s (j + m' + 1) * (s (j + m') * dprod s j m') * s (j + m' + 1)
          = s (j + m' + 1) * s (j + m') * (dprod s j m' * s (j + m' + 1)) := by
            simp only [mul_assoc]
        _ = s (j + m' + 1) * s (j + m') * s (j + m' + 1) * dprod s j m' := by
            rw [← hhigh]; simp only [mul_assoc]
        _ = s (j + m') * s (j + m' + 1) * s (j + m') * dprod s j m' := by rw [hbr]
        _ = s (j + m') * (s (j + m' + 1) * (s (j + m') * dprod s j m')) := by
            simp only [mul_assoc]

end Relations

/-! ### The Jones normal-form words and their span -/

open Classical in
/-- The Jones normal-form words at level `n` (in `s₀, …, s_{n-1}`):
`words 0 = {1}`, `words (n+1) = { x · dprod s j (n+1-j) : x ∈ words n, j ≤ n+1 }`. -/
noncomputable def words (s : ℕ → A) : ℕ → Finset A
  | 0 => {1}
  | n + 1 => Finset.image₂ (· * ·) (words s n)
      ((Finset.range (n + 2)).image fun j => dprod s j (n + 1 - j))

/-- **The word count**: at most `(n+1)!` words at level `n` (`= |S_{n+1}|`). -/
theorem card_words_le (s : ℕ → A) (n : ℕ) : (words s n).card ≤ (n + 1).factorial := by
  induction n with
  | zero => simp [words]
  | succ n ih =>
    classical
    calc (words s (n + 1)).card
        ≤ (words s n).card * ((Finset.range (n + 2)).image fun j => dprod s j (n + 1 - j)).card :=
          by rw [words]; exact Finset.card_image₂_le _ _ _
      _ ≤ (n + 1).factorial * (n + 2) := by
          gcongr
          exact Finset.card_image_le.trans (by simp)
      _ = (n + 2).factorial := by rw [Nat.factorial_succ (n + 1), Nat.mul_comm]

variable (R) in
/-- The span of the level-`n` words. -/
noncomputable def level (s : ℕ → A) (n : ℕ) : Submodule R A :=
  Submodule.span R (words s n : Set A)

theorem mul_dprod_mem_words {s : ℕ → A} {n j m : ℕ} {x : A} (hx : x ∈ words s n)
    (hjm : j + m = n + 1) : x * dprod s j m ∈ words s (n + 1) := by
  classical
  rw [words]
  refine Finset.mem_image₂.mpr ⟨x, hx, dprod s j m, Finset.mem_image.mpr ⟨j, ?_, ?_⟩, rfl⟩
  · exact Finset.mem_range.mpr (by omega)
  · rw [show n + 1 - j = m by omega]

theorem mul_dprod_mem {s : ℕ → A} {n j m : ℕ} {x : A} (hx : x ∈ level R s n)
    (hjm : j + m = n + 1) : x * dprod s j m ∈ level R s (n + 1) := by
  induction hx using Submodule.span_induction with
  | mem y hy => exact Submodule.subset_span (mul_dprod_mem_words hy hjm)
  | zero => simp
  | add y z _ _ hy hz => rw [add_mul]; exact add_mem hy hz
  | smul c y _ hy => rw [smul_mul_assoc]; exact Submodule.smul_mem _ c hy

theorem one_mem_level (s : ℕ → A) : ∀ n, (1 : A) ∈ level R s n
  | 0 => Submodule.subset_span (by simp [words])
  | n + 1 => by simpa using mul_dprod_mem (j := n + 1) (m := 0) (one_mem_level s n) rfl

theorem level_le_succ (s : ℕ → A) (n : ℕ) : level R s n ≤ level R s (n + 1) := by
  intro x hx
  simpa using mul_dprod_mem (j := n + 1) (m := 0) hx rfl

theorem dprod_mem_level (s : ℕ → A) {n j m : ℕ} (hjm : j + m = n) : dprod s j m ∈ level R s n := by
  cases n with
  | zero =>
    obtain ⟨rfl, rfl⟩ : j = 0 ∧ m = 0 := ⟨by omega, by omega⟩
    exact one_mem_level s 0
  | succ n => simpa using mul_dprod_mem (one_mem_level (R := R) s n) hjm

section Closure

variable {N : ℕ} {a b : R} {s : ℕ → A}

/-- The case analysis: a single summand `y · dprod s j m` times a generator `sᵢ`
(`i ≤ n`) stays in the span of the level-`(n+1)` words. -/
theorem mul_dprod_mul_gen_mem (hs : HeckeFamily N a b s) {n : ℕ} (hn : n + 1 ≤ N)
    (ih : ∀ i, i < n → ∀ x ∈ level R s n, x * s i ∈ level R s n)
    {y : A} (hy : y ∈ level R s n) {j m : ℕ} (hjm : j + m = n + 1) {i : ℕ} (hi : i < n + 1) :
    y * dprod s j m * s i ∈ level R s (n + 1) := by
  rcases lt_trichotomy (i + 1) j with h | h | h
  · -- commute: `sᵢ` is strictly below the run
    rw [mul_assoc, ← comm_dprod_low hs (by omega) m (by omega), ← mul_assoc]
    exact mul_dprod_mem (ih i (by omega) y hy) hjm
  · -- extend: the run grows by one letter
    subst h
    rw [mul_assoc, ← dprod_succ']
    exact mul_dprod_mem hy (by omega)
  · rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp h) with h2 | h2
    · -- fold: `sᵢ` is the foot, and the quadratic relation fires
      subst h2
      obtain ⟨m', rfl⟩ : ∃ m', m = m' + 1 := ⟨m - 1, by omega⟩
      have e : y * dprod s j (m' + 1) * s j
          = a • (y * dprod s j (m' + 1)) + b • (y * dprod s (j + 1) m') := by
        rw [dprod_succ' s j m', mul_assoc, mul_assoc, hs.quad j (by omega)]
        simp only [mul_add, mul_smul_comm, mul_one]
      rw [e]
      exact add_mem (Submodule.smul_mem _ _ (mul_dprod_mem hy hjm))
        (Submodule.smul_mem _ _ (mul_dprod_mem hy (by omega)))
    · -- push: `sᵢ` is above the foot and comes out with index `i - 1`
      obtain ⟨i', rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
      rw [mul_assoc, dprod_push hs (by omega) m (by omega) (by omega), ← mul_assoc]
      exact mul_dprod_mem (ih i' (by omega) y hy) hjm

/-- **Closure.** For `n ≤ N`, the span of the level-`n` words is closed under right
multiplication by `s₀, …, s_{n-1}`. -/
theorem level_mul_gen (hs : HeckeFamily N a b s) :
    ∀ n, n ≤ N → ∀ i, i < n → ∀ x ∈ level R s n, x * s i ∈ level R s n
  | 0, _, i, hi, _, _ => absurd hi (Nat.not_lt_zero _)
  | n + 1, hn, i, hi, x, hx => by
    have ih := level_mul_gen hs n (by omega)
    induction hx using Submodule.span_induction with
    | mem y hy =>
      classical
      rw [words] at hy
      obtain ⟨y', hy', d, hd, rfl⟩ := Finset.mem_image₂.mp hy
      obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hd
      have hj' := Finset.mem_range.mp hj
      exact mul_dprod_mul_gen_mem hs hn ih (Submodule.subset_span hy') (by omega) hi
    | zero => simp
    | add y z _ _ hy hz => rw [add_mul]; exact add_mem hy hz
    | smul c y _ hy => rw [smul_mul_assoc]; exact Submodule.smul_mem _ c hy

/-- The level-`n` span is closed under right multiplication by every element of the
subalgebra generated by `s₀, …, s_{n-1}`. -/
theorem level_mul_adjoin (hs : HeckeFamily N a b s) {n : ℕ} (hn : n ≤ N) {y : A}
    (hy : y ∈ Algebra.adjoin R (s '' Set.Iio n)) : ∀ x ∈ level R s n, x * y ∈ level R s n := by
  induction hy using Algebra.adjoin_induction with
  | mem y hy =>
    obtain ⟨i, hi, rfl⟩ := hy
    exact level_mul_gen hs n hn i hi
  | algebraMap c =>
    intro x hx
    rw [← Algebra.commutes, ← Algebra.smul_def]
    exact Submodule.smul_mem _ c hx
  | add y z _ _ hy hz =>
    intro x hx; rw [mul_add]; exact add_mem (hy x hx) (hz x hx)
  | mul y z _ _ hy hz =>
    intro x hx; rw [← mul_assoc]; exact hz _ (hy x hx)

theorem words_subset_adjoin (s : ℕ → A) :
    ∀ n, ∀ x ∈ words s n, x ∈ Algebra.adjoin R (s '' Set.Iio n)
  | 0, x, hx => by
    simp only [words, Finset.mem_singleton] at hx
    subst hx; exact Subalgebra.one_mem _
  | n + 1, x, hx => by
    classical
    rw [words] at hx
    obtain ⟨y, hy, d, hd, rfl⟩ := Finset.mem_image₂.mp hx
    obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hd
    have hj' := Finset.mem_range.mp hj
    refine Subalgebra.mul_mem _ ?_ ?_
    · exact Algebra.adjoin_mono (Set.image_mono (Set.Iio_subset_Iio (Nat.le_succ n)))
        (words_subset_adjoin s n y hy)
    · have key : ∀ m, j + m ≤ n + 1 → dprod s j m ∈ Algebra.adjoin R (s '' Set.Iio (n + 1)) := by
        intro m
        induction m with
        | zero => intro _; exact Subalgebra.one_mem _
        | succ m ihm =>
          intro hm
          exact Subalgebra.mul_mem _
            (Algebra.subset_adjoin ⟨j + m, Set.mem_Iio.mpr (by omega), rfl⟩) (ihm (by omega))
      exact key _ (by omega)

/-- **The spanning theorem (Jones normal form).** For `n ≤ N`, the subalgebra generated
by `s₀, …, s_{n-1}` is spanned by the at most `(n+1)!` Jones normal-form words
`words s n` (`card_words_le`). -/
theorem adjoin_eq_level (hs : HeckeFamily N a b s) {n : ℕ} (hn : n ≤ N) :
    Subalgebra.toSubmodule (Algebra.adjoin R (s '' Set.Iio n)) = level R s n := by
  apply le_antisymm
  · intro y hy
    simpa using level_mul_adjoin hs hn hy 1 (one_mem_level s n)
  · exact Submodule.span_le.mpr fun x hx => words_subset_adjoin s n x hx

end Closure

end QOU.IwahoriHecke.JonesNormalForm
