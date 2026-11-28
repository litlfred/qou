import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Laurent
import QOU.Observations.collatz_cycle_classification

/-!
# The Skein–Collatz orbit lifts the classical Syracuse orbit

The Skein–Collatz map acts on `ℤ[q^{±1}]` by

* even step (`[2]_q ∣ P`):     `[2]_q · P' = P`,
* odd step  (`[2]_q ∣ P + 1`): `[2]_q · P' = [3]_q · P + 1`,

with `[2]_q = q + 1` and `[3]_q = q² + q + 1`. It is a partial map: an element
`P` is `q`-even when `P(-1) = 0` and `q`-odd when `P(-1) = -1`, and neither
otherwise. An orbit that stays inside the domain forever is *domain-stable*.

This file proves three things about a domain-stable orbit `P 0, P 1, …`.

1. **The specialisation `q ↦ 1` is the Syracuse map** (`syracuse_of_step`).
   For any ring map `φ : ℤ[q^{±1}] → ℤ` with `φ q = 1` (evaluation at `q = 1`),
   the integers `n_j = φ (P j)` satisfy `n_{j+1} = n_j / 2` after an even step
   and `n_{j+1} = (3 n_j + 1) / 2` after an odd step, and the step type is the
   classical parity of `n_j` (`parity_of_even_step`, `parity_of_odd_step`).
   So the parity word of the `q`-orbit is the classical parity word of `n_0`.

2. **An eventually periodic parity word forces an exact cycle**
   (`periodic_of_word_periodic`). If the step types repeat with period `K` from
   index `N` on, then `P (N + K) = P N`. The proof: the difference
   `D_j = P (N + K + j) - P (N + j)` satisfies `[2]_q D_{j+1} = c_j D_j` with
   `c_j ∈ {1, [3]_q}`, so `[2]_q^n` divides `(∏ c_j) · D_0` for every `n`; the
   `c_j` are coprime to `[2]_q` (Bézout: `[3]_q - q [2]_q = 1`), so `[2]_q^n`
   divides `D_0` for every `n`, and a nonzero Laurent polynomial has bounded
   `[2]_q`-adic order (`eq_zero_of_forall_pow_dvd`).

3. **Consequence** (`reaches_cycle_of_classical_periodic`). If the classical
   Syracuse orbit of `n_0 = φ (P 0)` is eventually periodic, the `q`-orbit
   lands on one of the three cycles of `ℤ[q^{±1}]` classified in
   `collatz_cycle_classification`: `{0}`, `{-q⁻²}`, `{q⁻¹, 1 + q⁻¹}`.

Reading. Together with the converse (a `q`-orbit that reaches a cycle maps under
`q ↦ 1` onto `{0}`, `{-1}` or `{1, 2}`), this says: a domain-stable `q`-orbit
converges exactly when the classical Syracuse orbit of its value at `q = 1` is
eventually periodic. So the convergence half of the `q`-Collatz conjecture is
*implied by* the classical statement "no Syracuse orbit diverges", and a
counterexample to it would be a Laurent polynomial lifting a divergent
classical orbit. It also shows that a domain-stable `P` cannot have `P(1)` in
the classical negative cycles `{-5, -7, -10}` or `{-17, …}`: those cycles do
not lift to `ℤ[q^{±1}]`.

Nothing here uses a real value of `q`, a positivity hypothesis, or a measured
number. Axioms: the standard three.
-/

namespace QOU.AppendixSurreals.CollatzSyracuseLift

open LaurentPolynomial Polynomial

/-- `[2]_q = q + 1` in `ℤ[q^{±1}]`. -/
noncomputable abbrev two : LaurentPolynomial ℤ := T 1 + 1

/-- `[3]_q = q² + q + 1` in `ℤ[q^{±1}]`. -/
noncomputable abbrev three : LaurentPolynomial ℤ := T 2 + T 1 + 1

/-- One step of the Skein–Collatz map, with its type recorded by `b`
(`false` = even step, `true` = odd step). -/
def Step (b : Bool) (P P' : LaurentPolynomial ℤ) : Prop :=
  if b then two * P' = three * P + 1 else two * P' = P

/-! ## 1. The specialisation `q ↦ 1` -/

section Specialisation

variable (φ : LaurentPolynomial ℤ →+* ℤ) (hφ : φ (T 1) = 1)
include hφ

lemma φ_T2 : φ (T 2) = 1 := by
  have : (T 2 : LaurentPolynomial ℤ) = T 1 * T 1 := by rw [← T_add]; norm_num
  rw [this, map_mul, hφ, one_mul]

lemma φ_two : φ two = 2 := by simp [two, hφ]

lemma φ_three : φ three = 3 := by simp [three, hφ, φ_T2 φ hφ]

/-- An even step specialises to halving, and the input is classically even. -/
theorem parity_of_even_step {P P' : LaurentPolynomial ℤ} (h : two * P' = P) :
    φ P = 2 * φ P' := by
  have := congrArg φ h
  simp only [map_mul, map_add, map_one, two, hφ] at this
  linarith

/-- An odd step specialises to `(3n + 1)/2`, and the input is classically odd. -/
theorem parity_of_odd_step {P P' : LaurentPolynomial ℤ} (h : two * P' = three * P + 1) :
    2 * φ P' = 3 * φ P + 1 := by
  have := congrArg φ h
  simp only [map_mul, map_add, map_one, two, three, hφ, φ_T2 φ hφ] at this
  linarith

/-- The classical Syracuse map on `ℤ`. -/
def syracuse (n : ℤ) : ℤ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- **The `q ↦ 1` specialisation of a Skein–Collatz step is the Syracuse step**,
and the step type equals the classical parity of the value at `q = 1`. -/
theorem syracuse_of_step {b : Bool} {P P' : LaurentPolynomial ℤ} (h : Step b P P') :
    φ P' = syracuse (φ P) ∧ (b = true ↔ φ P % 2 = 1) := by
  cases b with
  | false =>
    have h' : two * P' = P := by simpa [Step] using h
    have e := parity_of_even_step φ hφ h'
    refine ⟨?_, ?_⟩
    · unfold syracuse; rw [e]; simp
    · simp; omega
  | true =>
    have h' : two * P' = three * P + 1 := by simpa [Step] using h
    have e := parity_of_odd_step φ hφ h'
    refine ⟨?_, ?_⟩
    · unfold syracuse
      have : φ P % 2 ≠ 0 := by omega
      rw [if_neg this]; omega
    · simp; omega

end Specialisation

/-! ## 2. Bounded `[2]_q`-adic order and coprimality -/

lemma isCoprime_two_three : IsCoprime two three := by
  refine ⟨-T 1, 1, ?_⟩
  have : (T 2 : LaurentPolynomial ℤ) = T 1 * T 1 := by rw [← T_add]; norm_num
  simp only [two, three, this]; ring

lemma isCoprime_X_add_one_X : IsCoprime ((X : ℤ[X]) + 1) X :=
  ⟨1, -1, by ring⟩

/-- **A nonzero Laurent polynomial has bounded `[2]_q`-adic order.** -/
theorem eq_zero_of_forall_pow_dvd (D : LaurentPolynomial ℤ)
    (h : ∀ n : ℕ, two ^ n ∣ D) : D = 0 := by
  obtain ⟨N, f, hf⟩ := exists_T_pow D
  by_contra hD
  have hf0 : f ≠ 0 := by
    rintro rfl
    apply hD
    have hu : (T N : LaurentPolynomial ℤ) * T (-(N : ℤ)) = 1 := by
      rw [← T_add]; simp
    have : D * T N = 0 := by rw [← hf]; simp
    calc D = D * T N * T (-(N : ℤ)) := by rw [mul_assoc, hu, mul_one]
      _ = 0 := by rw [this, zero_mul]
  set n := f.natDegree + 1
  obtain ⟨E, hE⟩ := h n
  obtain ⟨M, g, hg⟩ := exists_T_pow E
  -- transport the divisibility to `ℤ[X]`
  have key : toLaurent (f * X ^ M) = toLaurent ((X + 1) ^ n * g * X ^ N) := by
    rw [map_mul, map_mul, map_mul, Polynomial.toLaurent_X_pow, Polynomial.toLaurent_X_pow, hf,
      map_pow, map_add, Polynomial.toLaurent_X, map_one, hg, hE]
    simp only [two]; ring
  have key' := toLaurent_injective key
  have hdvd : (X + 1 : ℤ[X]) ^ n ∣ f * X ^ M := ⟨g * X ^ N, by rw [key']; ring⟩
  have hdvd' : (X + 1 : ℤ[X]) ^ n ∣ f :=
    ((isCoprime_X_add_one_X.pow (m := n) (n := M))).dvd_of_dvd_mul_right hdvd
  have hdeg := Polynomial.natDegree_le_of_dvd hdvd' hf0
  have : ((X + 1 : ℤ[X]) ^ n).natDegree = n := by
    rw [Polynomial.natDegree_pow, show (X + 1 : ℤ[X]) = X + Polynomial.C 1 by simp,
      natDegree_X_add_C, mul_one]
  omega

/-! ## 3. Eventually periodic parity word ⇒ exact cycle -/

/-- **An eventually periodic parity word forces an exact cycle.** If an orbit
follows the step types `w`, and `w` repeats with period `K` from `N` on, then
`P (N + K) = P N`. -/
theorem periodic_of_word_periodic (P : ℕ → LaurentPolynomial ℤ) (w : ℕ → Bool)
    (hstep : ∀ j, Step (w j) (P j) (P (j + 1))) (N K : ℕ)
    (hw : ∀ j, N ≤ j → w (j + K) = w j) : P (N + K) = P N := by
  set D : ℕ → LaurentPolynomial ℤ := fun j => P (N + K + j) - P (N + j) with hDdef
  let c : ℕ → LaurentPolynomial ℤ := fun j => if w (N + j) then three else 1
  have hrec : ∀ j, two * D (j + 1) = c j * D j := by
    intro j
    have h1 := hstep (N + K + j)
    have h2 := hstep (N + j)
    have hwj : w (N + K + j) = w (N + j) := by
      have := hw (N + j) (by omega)
      rwa [show N + j + K = N + K + j by omega] at this
    rw [hwj] at h1
    have e1 : N + K + (j + 1) = N + K + j + 1 := by omega
    have e2 : N + (j + 1) = N + j + 1 := by omega
    simp only [hDdef, c, e1, e2, mul_sub]
    cases hb : w (N + j)
    · simp only [Step, hb, Bool.false_eq_true, if_false] at h1 h2 ⊢
      rw [h1, h2]; ring
    · simp only [Step, hb, if_true] at h1 h2 ⊢
      rw [h1, h2]; ring
  have hcop : ∀ j, IsCoprime two (c j) := by
    intro j; simp only [c]; split
    · exact isCoprime_two_three
    · exact isCoprime_one_right
  have hpow : ∀ n, two ^ n * D n = (∏ j ∈ Finset.range n, c j) * D 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Finset.prod_range_succ, pow_succ]
      calc two ^ n * two * D (n + 1) = two ^ n * (two * D (n + 1)) := by ring
        _ = two ^ n * (c n * D n) := by rw [hrec n]
        _ = c n * (two ^ n * D n) := by ring
        _ = _ := by rw [ih]; ring
  have hall : ∀ n, two ^ n ∣ D 0 := by
    intro n
    have hd : two ^ n ∣ (∏ j ∈ Finset.range n, c j) * D 0 := ⟨D n, (hpow n).symm⟩
    have hc : IsCoprime (two ^ n) (∏ j ∈ Finset.range n, c j) :=
      (IsCoprime.prod_right fun j _ => hcop j).pow_left
    exact hc.dvd_of_dvd_mul_left hd
  have h0 := eq_zero_of_forall_pow_dvd (D 0) hall
  simp only [hDdef, add_zero] at h0
  exact sub_eq_zero.mp h0

/-! ## 4. Classical eventual periodicity ⇒ the `q`-orbit lands on a known cycle -/

/-- **If the Syracuse orbit of `P(1)` is eventually periodic, the domain-stable
`q`-orbit of `P` lands on `{0}`, `{-q⁻²}` or `{q⁻¹, 1 + q⁻¹}`.** -/
theorem reaches_cycle_of_classical_periodic
    (φ : LaurentPolynomial ℤ →+* ℤ) (hφ : φ (T 1) = 1)
    (P : ℕ → LaurentPolynomial ℤ) (w : ℕ → Bool)
    (hstep : ∀ j, Step (w j) (P j) (P (j + 1)))
    (N K : ℕ) (hK : 1 ≤ K) (hn : φ (P (N + K)) = φ (P N)) :
    P N = 0 ∨ P N = -T (-2) ∨ P N = T (-1) ∨ P N = 1 + T (-1) := by
  -- the integer orbit is periodic from `N` on
  have hnj : ∀ j, φ (P (N + K + j)) = φ (P (N + j)) := by
    intro j
    induction j with
    | zero => simpa using hn
    | succ j ih =>
      rw [show N + K + (j + 1) = N + K + j + 1 by omega,
        show N + (j + 1) = N + j + 1 by omega,
        (syracuse_of_step φ hφ (hstep _)).1, (syracuse_of_step φ hφ (hstep _)).1, ih]
  -- hence so is the parity word
  have hw : ∀ j, N ≤ j → w (j + K) = w j := by
    intro j hj
    obtain ⟨i, rfl⟩ : ∃ i, j = N + i := ⟨j - N, by omega⟩
    have a := (syracuse_of_step φ hφ (hstep (N + K + i))).2
    have b := (syracuse_of_step φ hφ (hstep (N + i))).2
    rw [hnj i] at a
    rw [show N + i + K = N + K + i by omega]
    exact Bool.eq_iff_iff.mpr (a.trans b.symm)
  have hper := periodic_of_word_periodic P w hstep N K hw
  -- apply the cycle classification to the shifted orbit
  refine QOU.AppendixSurreals.CollatzCycleClassification.laurent_cycle_classification
    (fun j => P (N + j)) K hK (by simpa using hper) ?_
  intro j _
  have := hstep (N + j)
  show (T 1 + 1) * P (N + (j + 1)) = P (N + j) ∨
    (T 1 + 1) * P (N + (j + 1)) = (T 2 + T 1 + 1) * P (N + j) + 1
  rw [show N + (j + 1) = N + j + 1 by omega]
  cases hb : w (N + j) <;> simp only [Step, hb, Bool.false_eq_true, if_false, if_true] at this
  · left; exact this
  · right; exact this

/-! ## 5. Faithful statements, and the implication between them

These are the human-readable statements the book refers to. They mention only
`ℤ[q^{±1}]`, `ℤ` and the two maps; no free predicate, no abstracted cone. -/

/-- A domain-stable orbit of the Skein–Collatz map: every step is an even or an
odd step. (Because `[2]_q` is a non-zero-divisor, the step relation determines
`P (j + 1)` from `P j`, so this is exactly an infinite orbit of the partial map.) -/
def DomainStableOrbit (P : ℕ → LaurentPolynomial ℤ) : Prop :=
  ∃ w : ℕ → Bool, ∀ j, Step (w j) (P j) (P (j + 1))

/-- The three cycles of `ℤ[q^{±1}]`, as a set of points. -/
def OnKnownCycle (P : LaurentPolynomial ℤ) : Prop :=
  P = 0 ∨ P = -T (-2) ∨ P = T (-1) ∨ P = 1 + T (-1)

/-- **The convergence half of the `q`-Collatz conjecture**, stated faithfully:
every domain-stable orbit reaches one of the three cycles. -/
def QCollatzConvergence : Prop :=
  ∀ P : ℕ → LaurentPolynomial ℤ, DomainStableOrbit P → ∃ N, OnKnownCycle (P N)

/-- **Classical "no divergent Syracuse orbit" over `ℤ`**: every orbit of the
Syracuse map is eventually periodic. (For positive integers this is the usual
"no divergent trajectory" half of the Collatz conjecture.) -/
def SyracuseNoDivergence : Prop :=
  ∀ n : ℤ, ∃ N K : ℕ, 1 ≤ K ∧ syracuse^[N + K] n = syracuse^[N] n

/-- **Classical no-divergence implies `q`-Collatz convergence.** Given any ring
map `φ : ℤ[q^{±1}] → ℤ` with `φ q = 1`. -/
theorem qCollatzConvergence_of_syracuse
    (φ : LaurentPolynomial ℤ →+* ℤ) (hφ : φ (T 1) = 1)
    (h : SyracuseNoDivergence) : QCollatzConvergence := by
  rintro P ⟨w, hstep⟩
  have hit : ∀ j, φ (P j) = syracuse^[j] (φ (P 0)) := by
    intro j
    induction j with
    | zero => rfl
    | succ j ih =>
      rw [(syracuse_of_step φ hφ (hstep j)).1, ih, Function.iterate_succ_apply']
  obtain ⟨N, K, hK, hNK⟩ := h (φ (P 0))
  refine ⟨N, reaches_cycle_of_classical_periodic φ hφ P w hstep N K hK ?_⟩
  rw [hit (N + K), hit N]; exact hNK

/-- Evaluation at `q = 1`, as a ring map `ℤ[q^{±1}] → ℤ`. -/
noncomputable def evalOne : LaurentPolynomial ℤ →+* ℤ :=
  LaurentPolynomial.eval₂ (RingHom.id ℤ) 1

lemma evalOne_T1 : evalOne (T 1) = 1 := by
  simp [evalOne, LaurentPolynomial.eval₂_T]

/-- **Main theorem.** Classical "no divergent Syracuse orbit" implies the
convergence half of the `q`-Collatz conjecture. -/
theorem qCollatzConvergence_of_syracuseNoDivergence
    (h : SyracuseNoDivergence) : QCollatzConvergence :=
  qCollatzConvergence_of_syracuse evalOne evalOne_T1 h

end QOU.AppendixSurreals.CollatzSyracuseLift
