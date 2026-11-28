import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.ZMod.Basic
import QOU.Observations.collatz_syracuse_lift

/-!
# A Skein–Collatz orbit with bounded support reaches a known cycle

Let `P 0, P 1, …` be a domain-stable orbit of the Skein–Collatz map on
`ℤ[q^{±1}]` (see `collatz_syracuse_lift`). Suppose its support stays in a
fixed window: there are `N₀` and `m` with `q^{N₀} · P j` a polynomial of degree
at most `m` for every `j`.

**Theorem** (`reaches_cycle_of_bounded_window`). Such an orbit reaches one of
the three cycles `{0}`, `{-q⁻²}`, `{q⁻¹, 1 + q⁻¹}`.

The proof needs no analysis and no bound on the coefficients. Reduce modulo
`2`. The reductions are polynomials over `ZMod 2` of degree at most `m`, so
they take finitely many values. A reduction determines the next step type (its
value at `q = 1`, which is `q = -1` mod `2`), and it also determines the next
reduction, because `q + 1` can be cancelled in the domain `(ZMod 2)[X]`. So two
equal reductions start the same parity word. By pigeonhole the word is
eventually periodic, and `periodic_of_word_periodic` turns that into an exact
cycle.

**Corollary** (`counterexample_shape`). If a domain-stable orbit never reaches
a known cycle, then (a) its support is not contained in any fixed window, and
(b) the classical Syracuse orbit of its value at `q = 1` is not eventually
periodic, so it is unbounded.

Axioms: the standard three.
-/

namespace QOU.AppendixSurreals.CollatzBoundedWindow

open LaurentPolynomial Polynomial QOU.AppendixSurreals.CollatzSyracuseLift

/-- The orbit's support lies in a fixed window: `q^{N₀} · P j = f j` with
`f j` a polynomial of degree at most `m`. -/
def BoundedWindow (P : ℕ → LaurentPolynomial ℤ) : Prop :=
  ∃ (N₀ m : ℕ) (f : ℕ → ℤ[X]), ∀ j, toLaurent (f j) = P j * T N₀ ∧ (f j).natDegree ≤ m

/-- Reduction of an integer polynomial modulo `2`. -/
noncomputable def red (f : ℤ[X]) : (ZMod 2)[X] := f.map (Int.castRingHom (ZMod 2))

lemma toLaurent_three : toLaurent ((X : ℤ[X]) ^ 2 + X + 1) = three := by
  simp [three, Polynomial.toLaurent_X_pow]

/-- The step relations, moved to the polynomial representatives. -/
lemma poly_step {N₀ : ℕ} {b : Bool} {P P' : LaurentPolynomial ℤ} {f f' : ℤ[X]}
    (hf : toLaurent f = P * T N₀) (hf' : toLaurent f' = P' * T N₀) (h : Step b P P') :
    if b then (X + 1) * f' = (X ^ 2 + X + 1) * f + X ^ N₀ else (X + 1) * f' = f := by
  cases b with
  | false =>
    have h' : two * P' = P := by simpa [Step] using h
    simp only [Bool.false_eq_true, if_false]
    apply Polynomial.toLaurent_injective
    rw [map_mul, hf', hf, map_add, Polynomial.toLaurent_X, map_one, ← h']
    simp only [two]; ring
  | true =>
    have h' : two * P' = three * P + 1 := by simpa [Step] using h
    simp only [if_true]
    apply Polynomial.toLaurent_injective
    rw [map_mul, hf', map_add, Polynomial.toLaurent_X, map_one, map_add, map_mul, hf,
      toLaurent_three, Polynomial.toLaurent_X_pow]
    calc (T 1 + 1) * (P' * T N₀) = (two * P') * T N₀ := by simp only [two]; ring
      _ = (three * P + 1) * T N₀ := by rw [h']
      _ = three * (P * T N₀) + T ↑N₀ := by ring

/-- The same relations modulo `2`. -/
lemma red_step {N₀ : ℕ} {b : Bool} {f f' : ℤ[X]}
    (h : if b then (X + 1) * f' = (X ^ 2 + X + 1) * f + X ^ N₀ else (X + 1) * f' = f) :
    if b then (X + 1) * red f' = (X ^ 2 + X + 1) * red f + X ^ N₀
    else (X + 1) * red f' = red f := by
  cases b with
  | false =>
    simp only [Bool.false_eq_true, if_false] at h ⊢
    have := congrArg red h
    simpa [red, Polynomial.map_mul, Polynomial.map_add] using this
  | true =>
    simp only [if_true] at h ⊢
    have := congrArg red h
    simpa [red, Polynomial.map_mul, Polynomial.map_add, Polynomial.map_pow] using this

/-- The step type is read off the reduction: odd exactly when it is `1` at `q = 1`. -/
lemma type_of_red {N₀ : ℕ} {b : Bool} {g g' : (ZMod 2)[X]}
    (h : if b then (X + 1) * g' = (X ^ 2 + X + 1) * g + X ^ N₀ else (X + 1) * g' = g) :
    (b = true ↔ g.eval 1 = 1) := by
  have h2 : (1 + 1 : ZMod 2) = 0 := by decide
  cases b with
  | false =>
    simp only [Bool.false_eq_true, if_false, false_iff] at h ⊢
    have := congrArg (Polynomial.eval 1) h
    simp only [eval_mul, eval_add, eval_X, eval_one, h2, zero_mul] at this
    rw [← this]; decide
  | true =>
    simp only [if_true, true_iff] at h ⊢
    have := congrArg (Polynomial.eval 1) h
    simp only [eval_mul, eval_add, eval_X, eval_one, eval_pow, one_pow, h2, zero_mul] at this
    -- `0 = (1 + 1 + 1) * g(1) + 1` in `ZMod 2`
    rw [zero_add, one_mul] at this
    generalize g.eval 1 = x at this ⊢
    revert x; decide

/-- Equal reductions with equal step types give equal next reductions. -/
lemma red_next {N₀ : ℕ} {b : Bool} {g g' h h' : (ZMod 2)[X]}
    (hg : if b then (X + 1) * g' = (X ^ 2 + X + 1) * g + X ^ N₀ else (X + 1) * g' = g)
    (hh : if b then (X + 1) * h' = (X ^ 2 + X + 1) * h + X ^ N₀ else (X + 1) * h' = h)
    (e : g = h) : g' = h' := by
  have hne : (X + 1 : (ZMod 2)[X]) ≠ 0 := X_add_C_ne_zero 1
  apply mul_left_cancel₀ hne
  cases b with
  | false => simp only [Bool.false_eq_true, if_false] at hg hh; rw [hg, hh, e]
  | true => simp only [if_true] at hg hh; rw [hg, hh, e]

/-- **A domain-stable orbit with support in a fixed window reaches one of the
three cycles of `ℤ[q^{±1}]`.** -/
theorem reaches_cycle_of_bounded_window (P : ℕ → LaurentPolynomial ℤ)
    (hP : DomainStableOrbit P) (hB : BoundedWindow P) : ∃ N, OnKnownCycle (P N) := by
  obtain ⟨w, hstep⟩ := hP
  obtain ⟨N₀, m, f, hf⟩ := hB
  have hrel : ∀ j, if w j then (X + 1) * red (f (j + 1)) = (X ^ 2 + X + 1) * red (f j) + X ^ N₀
      else (X + 1) * red (f (j + 1)) = red (f j) :=
    fun j => red_step (poly_step (hf j).1 (hf (j + 1)).1 (hstep j))
  -- pigeonhole on the coefficient vectors of the reductions
  let v : ℕ → (Fin (m + 1) → ZMod 2) := fun j k => (red (f j)).coeff k
  obtain ⟨i, j, hij, hv⟩ := Finite.exists_ne_map_eq_of_infinite v
  have hdeg : ∀ j, (red (f j)).natDegree ≤ m := fun j =>
    (Polynomial.natDegree_map_le).trans (hf j).2
  have heq : ∀ {a c : ℕ}, v a = v c → red (f a) = red (f c) := by
    intro a c h
    ext k
    by_cases hk : k ≤ m
    · exact congrFun h ⟨k, by omega⟩
    · rw [Polynomial.coeff_eq_zero_of_natDegree_lt (by have := hdeg a; omega),
        Polynomial.coeff_eq_zero_of_natDegree_lt (by have := hdeg c; omega)]
  -- order the pair
  obtain ⟨a, c, hac, hvac⟩ : ∃ a c, a < c ∧ v a = v c := by
    rcases Nat.lt_or_gt_of_ne hij with h | h
    · exact ⟨i, j, h, hv⟩
    · exact ⟨j, i, h, hv.symm⟩
  -- the parity words from `a` and from `c` agree
  have hagree : ∀ k, red (f (a + k)) = red (f (c + k)) ∧ w (a + k) = w (c + k) := by
    intro k
    induction k with
    | zero =>
      have e := heq hvac
      refine ⟨by simpa using e, ?_⟩
      have t1 := type_of_red (hrel a)
      have t2 := type_of_red (hrel c)
      rw [show a + 0 = a by rfl, show c + 0 = c by rfl]
      exact Bool.eq_iff_iff.mpr (t1.trans (e ▸ t2.symm))
    | succ k ih =>
      obtain ⟨e, ew⟩ := ih
      have h1 := hrel (a + k)
      have h2 := hrel (c + k)
      rw [ew] at h1
      have e' : red (f (a + k + 1)) = red (f (c + k + 1)) := red_next h1 h2 e
      refine ⟨by simpa [Nat.add_assoc] using e', ?_⟩
      have t1 := type_of_red (hrel (a + (k + 1)))
      have t2 := type_of_red (hrel (c + (k + 1)))
      have e'' : red (f (a + (k + 1))) = red (f (c + (k + 1))) := by
        simpa [Nat.add_assoc] using e'
      exact Bool.eq_iff_iff.mpr (t1.trans (e'' ▸ t2.symm))
  have hw : ∀ n, a ≤ n → w (n + (c - a)) = w n := by
    intro n hn
    obtain ⟨k, rfl⟩ : ∃ k, n = a + k := ⟨n - a, by omega⟩
    have := (hagree k).2
    rw [show a + k + (c - a) = c + k by omega]; exact this.symm
  have hper := periodic_of_word_periodic P w hstep a (c - a) hw
  refine ⟨a, ?_⟩
  refine QOU.AppendixSurreals.CollatzCycleClassification.laurent_cycle_classification
    (fun j => P (a + j)) (c - a) (by omega) (by simpa using hper) ?_
  intro j _
  have := hstep (a + j)
  show (T 1 + 1) * P (a + (j + 1)) = P (a + j) ∨
    (T 1 + 1) * P (a + (j + 1)) = (T 2 + T 1 + 1) * P (a + j) + 1
  rw [show a + (j + 1) = a + j + 1 by omega]
  cases hb : w (a + j) <;> simp only [Step, hb, Bool.false_eq_true, if_false, if_true] at this
  · left; exact this
  · right; exact this

/-- **Shape of a counterexample.** A domain-stable orbit that never reaches a
known cycle has support in no fixed window, and the Syracuse orbit of its value
at `q = 1` is not eventually periodic. -/
theorem counterexample_shape (P : ℕ → LaurentPolynomial ℤ) (hP : DomainStableOrbit P)
    (hno : ∀ N, ¬ OnKnownCycle (P N)) :
    ¬ BoundedWindow P ∧
      ∀ N K : ℕ, 1 ≤ K → syracuse^[N + K] (evalOne (P 0)) ≠ syracuse^[N] (evalOne (P 0)) := by
  refine ⟨fun hB => ?_, fun N K hK hNK => ?_⟩
  · obtain ⟨N, hN⟩ := reaches_cycle_of_bounded_window P hP hB
    exact hno N hN
  · obtain ⟨w, hstep⟩ := hP
    have hit : ∀ j, evalOne (P j) = syracuse^[j] (evalOne (P 0)) := by
      intro j
      induction j with
      | zero => rfl
      | succ j ih =>
        rw [(syracuse_of_step evalOne evalOne_T1 (hstep j)).1, ih,
          Function.iterate_succ_apply']
    have := reaches_cycle_of_classical_periodic evalOne evalOne_T1 P w hstep N K hK
      (by rw [hit (N + K), hit N]; exact hNK)
    exact hno N this

end QOU.AppendixSurreals.CollatzBoundedWindow
