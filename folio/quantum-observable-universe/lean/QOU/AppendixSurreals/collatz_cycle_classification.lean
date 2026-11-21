import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Reverse
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Laurent

/-!
# Every cycle of the Skein–Collatz map on `ℤ[q^{±1}]` is known

The Skein–Collatz map (see `QOU/AppendixSurreals/QCollatz.lean`) acts on the
Laurent ring `ℤ[q^{±1}]` by

* even step (`[2]_q ∣ P`):     `[2]_q · P' = P`,
* odd step  (`[2]_q ∣ P + 1`): `[2]_q · P' = [3]_q · P + 1`,

with `[2]_q = q + 1`, `[3]_q = q² + q + 1`.

**Theorem (cycle classification).** The periodic orbits are exactly
`{0}`, the odd fixed point `{-q⁻²}`, and the fundamental cycle `{q⁻¹, 1 + q⁻¹}`.

No positivity hypothesis is used, and no evaluation at a real `q`. The proof
is by three integer invariants of a Laurent polynomial read off at its two
ends:

1. **Bottom end, `ord_q P ≤ -2`.** With `β` the lowest coefficient and `β'`
   the next one, an even step sends `β' ↦ β' - β` and an odd step fixes it
   (the `+1` sits too high to reach it). Around a cycle `#even · β = 0`, so
   every step is odd, and the odd map is affine with multiplier
   `[3]_q/[2]_q`, which is not a root of unity: the only odd cycle is its
   fixed point `-q⁻²`.
2. **Bottom end, `ord_q P ≥ 0`.** Evaluation at `q = 0` adds `1` on every odd
   step and nothing on an even step, so there is no odd step, and then
   `((q+1)^K - 1)·P = 0` forces `P = 0`.
3. **`ord_q P = -1`.** The same argument as in 1, run on the *top* end (the
   reversed polynomial), shows that a cycle avoiding the constant `q⁻¹·1`
   has no even step, which is impossible for degree reasons; a cycle through
   `q⁻¹` is the fundamental cycle.

The file proves the statement for polynomial representatives: a Laurent
cycle multiplied by `q^M` becomes a polynomial sequence with source term `X^M`
in place of `1` (`StepRel M`). `cycle_classification` is the polynomial form;
the representatives it allows (`Cl M`) are `0`, `-X^{M-2}`, `X^{M-1}` and
`X^M + X^{M-1}`, i.e. `0`, `-q⁻²`, `q⁻¹`, `1 + q⁻¹` after dividing by `q^M`.

Status: sorry-free, axioms `[propext, Classical.choice, Quot.sound]`.
This is a statement about the formal ring `ℤ[q^{±1}]` only. It does not touch
the convergence half of the q-Collatz conjecture (`reaches_cycle`), and it
says nothing about the classical Collatz problem: a classical integer cycle
need not lift to a cycle in `ℤ[q^{±1}]`, so the classical cycle question is
not a specialisation of this one.

Main results: `cycle_classification` (polynomial representatives) and
`laurent_cycle_classification` (the statement on `ℤ[q^{±1}]`).
Beans: `qcz8` (Attack B, affine cycle exclusion), `qou-4ocd` (q-Steiner
clustered residue), `qcz19` B2 (general-word height bound).
-/

namespace QOU.AppendixSurreals.CollatzCycleClassification

open Polynomial

/-- One step of the Skein–Collatz map in polynomial representatives with
    source term `X^M` (a Laurent element `P` is represented by `q^M · P`). -/
def StepRel (M : ℕ) (s s' : ℤ[X]) : Prop :=
  (X + 1) * s' = s ∨ (X + 1) * s' = (X ^ 2 + X + 1) * s + X ^ M

/-- The admissible cycle values at shift `M`: `0`, `-q⁻²`, `q⁻¹`, `1 + q⁻¹`. -/
def Cl (M : ℕ) (p : ℤ[X]) : Prop :=
  p = 0 ∨ (2 ≤ M ∧ p = -X ^ (M - 2)) ∨
    (1 ≤ M ∧ (p = X ^ (M - 1) ∨ p = X ^ M + X ^ (M - 1)))

/-! ### Low coefficients -/

lemma coeff_zero_X_add_one_mul (g : ℤ[X]) : ((X + 1) * g).coeff 0 = g.coeff 0 := by
  simp [add_mul]

lemma coeff_one_X_add_one_mul (g : ℤ[X]) :
    ((X + 1) * g).coeff 1 = g.coeff 0 + g.coeff 1 := by
  simp [add_mul, coeff_X_mul]

lemma coeff_zero_odd (g : ℤ[X]) (t : ℕ) (ht : 1 ≤ t) :
    ((X ^ 2 + X + 1) * g + X ^ t).coeff 0 = g.coeff 0 := by
  have : (X ^ t : ℤ[X]).coeff 0 = 0 := by
    rw [coeff_X_pow]; simp; omega
  simp [add_mul, this]

lemma coeff_one_odd (g : ℤ[X]) (t : ℕ) (ht : 2 ≤ t) :
    ((X ^ 2 + X + 1) * g + X ^ t).coeff 1 = g.coeff 0 + g.coeff 1 := by
  have : (X ^ t : ℤ[X]).coeff 1 = 0 := by
    rw [coeff_X_pow]; simp; omega
  simp [add_mul, coeff_X_mul, coeff_X_pow_mul', this]

lemma even_coeffs {s s' : ℤ[X]} (h : (X + 1) * s' = s) :
    s'.coeff 0 = s.coeff 0 ∧ s'.coeff 1 = s.coeff 1 - s.coeff 0 := by
  have h0 := coeff_zero_X_add_one_mul s'
  have h1 := coeff_one_X_add_one_mul s'
  rw [h] at h0 h1
  constructor <;> linarith

lemma odd_coeffs {s s' : ℤ[X]} (t : ℕ) (ht : 2 ≤ t)
    (h : (X + 1) * s' = (X ^ 2 + X + 1) * s + X ^ t) :
    s'.coeff 0 = s.coeff 0 ∧ s'.coeff 1 = s.coeff 1 := by
  have h0 := coeff_zero_X_add_one_mul s'
  have h1 := coeff_one_X_add_one_mul s'
  rw [h, coeff_zero_odd s t (by omega)] at h0
  rw [h, coeff_one_odd s t ht] at h1
  constructor <;> linarith

/-! ### The core counting lemma

Along a cycle, an even step lowers the coefficient of `X` by the constant
coefficient `β`, and an "odd-like" step fixes both. So `#even · β = 0`. -/

theorem core (Odd : ℤ[X] → ℤ[X] → Prop)
    (hOdd : ∀ s s', Odd s s' → s'.coeff 0 = s.coeff 0 ∧ s'.coeff 1 = s.coeff 1)
    (s : ℕ → ℤ[X]) (K : ℕ) (hK : s K = s 0)
    (hstep : ∀ j < K, (X + 1) * s (j + 1) = s j ∨ Odd (s j) (s (j + 1)))
    (hβ : (s 0).coeff 0 ≠ 0) :
    ∀ j < K, Odd (s j) (s (j + 1)) := by
  have inv : ∀ i ≤ K, ∃ e : ℕ, (s i).coeff 0 = (s 0).coeff 0 ∧
      (s i).coeff 1 = (s 0).coeff 1 - e * (s 0).coeff 0 ∧
      (e = 0 → ∀ j < i, Odd (s j) (s (j + 1))) := by
    intro i
    induction i with
    | zero => intro _; exact ⟨0, rfl, by simp, fun _ j hj => absurd hj (by omega)⟩
    | succ i ih =>
      intro hi
      obtain ⟨e, h0, h1, he⟩ := ih (by omega)
      by_cases hO : Odd (s i) (s (i + 1))
      · obtain ⟨c0, c1⟩ := hOdd _ _ hO
        refine ⟨e, by rw [c0, h0], by rw [c1, h1], fun he0 j hj => ?_⟩
        rcases Nat.lt_succ_iff_lt_or_eq.mp hj with hj | hj
        · exact he he0 j hj
        · subst hj; exact hO
      · have hE : (X + 1) * s (i + 1) = s i := by
          rcases hstep i (by omega) with h | h
          · exact h
          · exact absurd h hO
        obtain ⟨c0, c1⟩ := even_coeffs hE
        refine ⟨e + 1, by rw [c0, h0], ?_, fun h => absurd h (by omega)⟩
        rw [c1, h1, h0]; push_cast; ring
  obtain ⟨e, _, h1, he⟩ := inv K le_rfl
  rw [hK] at h1
  have : (e : ℤ) * (s 0).coeff 0 = 0 := by linarith
  have he0 : e = 0 := by
    rcases mul_eq_zero.mp this with h | h
    · exact_mod_cast h
    · exact absurd h hβ
  exact he he0

/-! ### Affine and all-even lemmas -/

lemma X_add_one_pow_ne_three_pow (K : ℕ) (hK : 1 ≤ K) :
    ((X + 1) ^ K : ℤ[X]) ≠ (X ^ 2 + X + 1) ^ K := by
  intro h
  have := congrArg (eval 1) h
  simp only [eval_pow, eval_add, eval_X, eval_one] at this
  norm_num at this
  have : (2 : ℤ) ^ K < 3 ^ K := pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  omega

/-- A sequence obeying the linear odd recursion `[2]·D' = [3]·D` around a cycle
    vanishes: `[3]_q/[2]_q` is not a root of unity. -/
theorem affine_zero (D : ℕ → ℤ[X]) (K : ℕ) (hK1 : 1 ≤ K) (hK : D K = D 0)
    (h : ∀ j < K, (X + 1) * D (j + 1) = (X ^ 2 + X + 1) * D j) : D 0 = 0 := by
  have key : ∀ i ≤ K, (X + 1) ^ i * D i = (X ^ 2 + X + 1) ^ i * D 0 := by
    intro i
    induction i with
    | zero => intro _; simp
    | succ i ih =>
      intro hi
      calc (X + 1) ^ (i + 1) * D (i + 1) = (X + 1) ^ i * ((X + 1) * D (i + 1)) := by ring
        _ = (X + 1) ^ i * ((X ^ 2 + X + 1) * D i) := by rw [h i (by omega)]
        _ = (X ^ 2 + X + 1) * ((X + 1) ^ i * D i) := by ring
        _ = (X ^ 2 + X + 1) ^ (i + 1) * D 0 := by rw [ih (by omega)]; ring
  have hk := key K le_rfl
  rw [hK] at hk
  have : ((X + 1) ^ K - (X ^ 2 + X + 1) ^ K) * D 0 = 0 := by rw [sub_mul, hk, sub_self]
  rcases mul_eq_zero.mp this with h' | h'
  · exact absurd (sub_eq_zero.mp h') (X_add_one_pow_ne_three_pow K hK1)
  · exact h'

/-- A cycle made only of even steps is `0`. -/
theorem all_even_zero (s : ℕ → ℤ[X]) (K : ℕ) (hK1 : 1 ≤ K) (hK : s K = s 0)
    (h : ∀ j < K, (X + 1) * s (j + 1) = s j) : s 0 = 0 := by
  have key : ∀ i ≤ K, (X + 1) ^ i * s i = s 0 := by
    intro i
    induction i with
    | zero => intro _; simp
    | succ i ih =>
      intro hi
      calc (X + 1) ^ (i + 1) * s (i + 1) = (X + 1) ^ i * ((X + 1) * s (i + 1)) := by ring
        _ = s 0 := by rw [h i (by omega)]; exact ih (by omega)
  have hk := key K le_rfl
  rw [hK] at hk
  have : ((X + 1) ^ K - 1) * s 0 = 0 := by rw [sub_mul, hk, one_mul, sub_self]
  rcases mul_eq_zero.mp this with h' | h'
  · exfalso
    have := congrArg (eval 1) (sub_eq_zero.mp h')
    simp only [eval_pow, eval_add, eval_X, eval_one] at this
    norm_num at this
    have : (1 : ℤ) < 2 ^ K := one_lt_pow₀ (by norm_num) (by omega)
    omega
  · exact h'

/-! ### Shift `M = 0`: evaluation at `q = 0` -/

theorem classify_zero (s : ℕ → ℤ[X]) (K : ℕ) (hK1 : 1 ≤ K) (hK : s K = s 0)
    (hstep : ∀ j < K, StepRel 0 (s j) (s (j + 1))) : s 0 = 0 := by
  have inv : ∀ i ≤ K, ∃ o : ℕ, (s i).coeff 0 = (s 0).coeff 0 + o ∧
      (o = 0 → ∀ j < i, (X + 1) * s (j + 1) = s j) := by
    intro i
    induction i with
    | zero => intro _; exact ⟨0, by simp, fun _ j hj => absurd hj (by omega)⟩
    | succ i ih =>
      intro hi
      obtain ⟨o, h0, ho⟩ := ih (by omega)
      rcases hstep i (by omega) with hE | hO
      · refine ⟨o, ?_, fun ho0 j hj => ?_⟩
        · rw [(even_coeffs hE).1, h0]
        · rcases Nat.lt_succ_iff_lt_or_eq.mp hj with hj | hj
          · exact ho ho0 j hj
          · subst hj; exact hE
      · refine ⟨o + 1, ?_, fun h => absurd h (by omega)⟩
        have c := coeff_zero_X_add_one_mul (s (i + 1))
        rw [hO] at c
        simp [add_mul] at c
        rw [← c, h0]; push_cast; ring
  obtain ⟨o, h0, ho⟩ := inv K le_rfl
  rw [hK] at h0
  have : o = 0 := by omega
  exact all_even_zero s K hK1 hK (ho this)

/-! ### Shift reduction: if `X` divides every term, divide it out -/

lemma coeff_zero_invariant (M : ℕ) (hM : 1 ≤ M) (s : ℕ → ℤ[X]) (K : ℕ)
    (hstep : ∀ j < K, StepRel M (s j) (s (j + 1))) :
    ∀ i ≤ K, (s i).coeff 0 = (s 0).coeff 0 := by
  intro i
  induction i with
  | zero => intro _; rfl
  | succ i ih =>
    intro hi
    rcases hstep i (by omega) with hE | hO
    · rw [(even_coeffs hE).1, ih (by omega)]
    · have c := coeff_zero_X_add_one_mul (s (i + 1))
      rw [hO, coeff_zero_odd _ M hM] at c
      rw [← c, ih (by omega)]

lemma X_mul_divX_of_coeff_zero (p : ℤ[X]) (h : p.coeff 0 = 0) : X * p.divX = p := by
  have := X_mul_divX_add p
  rw [h, map_zero, add_zero] at this
  exact this

theorem reduce (M : ℕ) (s : ℕ → ℤ[X]) (K : ℕ)
    (hstep : ∀ j < K, StepRel (M + 1) (s j) (s (j + 1)))
    (h0 : ∀ i ≤ K, (s i).coeff 0 = 0) :
    ∀ j < K, StepRel M ((s j).divX) ((s (j + 1)).divX) := by
  intro j hj
  have ej := X_mul_divX_of_coeff_zero _ (h0 j (by omega))
  have ej1 := X_mul_divX_of_coeff_zero _ (h0 (j + 1) (by omega))
  have hX : (X : ℤ[X]) ≠ 0 := X_ne_zero
  rcases hstep j hj with hE | hO
  · left
    apply mul_left_cancel₀ hX
    calc X * ((X + 1) * (s (j + 1)).divX) = (X + 1) * (X * (s (j + 1)).divX) := by ring
      _ = X * (s j).divX := by rw [ej1, ej, hE]
  · right
    apply mul_left_cancel₀ hX
    calc X * ((X + 1) * (s (j + 1)).divX) = (X + 1) * (X * (s (j + 1)).divX) := by ring
      _ = (X ^ 2 + X + 1) * (X * (s j).divX) + X ^ (M + 1) := by rw [ej1, ej, hO]
      _ = X * ((X ^ 2 + X + 1) * (s j).divX + X ^ M) := by ring

lemma Cl_succ_of_Cl (M : ℕ) (r : ℤ[X]) (h : Cl M r) : Cl (M + 1) (X * r) := by
  rcases h with h | ⟨hM, h⟩ | ⟨hM, h | h⟩
  · left; simp [h]
  · right; left
    refine ⟨by omega, ?_⟩
    rw [h, show M + 1 - 2 = (M - 2) + 1 by omega, pow_succ]; ring
  · right; right
    refine ⟨by omega, Or.inl ?_⟩
    rw [h, show M + 1 - 1 = (M - 1) + 1 by omega, pow_succ]; ring
  · right; right
    refine ⟨by omega, Or.inr ?_⟩
    rw [h, show M + 1 - 1 = (M - 1) + 1 by omega]
    rw [show M = (M - 1) + 1 by omega]
    simp only [Nat.add_sub_cancel]
    ring

/-! ### Shift `M ≥ 2`, `β ≠ 0`: only the odd fixed point -/

theorem classify_ge_two_unit (M : ℕ) (hM : 2 ≤ M) (s : ℕ → ℤ[X]) (K : ℕ) (hK1 : 1 ≤ K)
    (hK : s K = s 0) (hstep : ∀ j < K, StepRel M (s j) (s (j + 1)))
    (hβ : (s 0).coeff 0 ≠ 0) : s 0 = -X ^ (M - 2) := by
  have hodd := core (fun s s' => (X + 1) * s' = (X ^ 2 + X + 1) * s + X ^ M)
    (fun s s' h => odd_coeffs M hM h) s K hK hstep hβ
  have := affine_zero (fun i => s i + X ^ (M - 2)) K hK1 (by simp [hK]) (by
    intro j hj
    simp only
    rw [mul_add, hodd j hj]
    have : (X : ℤ[X]) ^ M = X ^ 2 * X ^ (M - 2) := by
      rw [← pow_add]; congr 1; omega
    rw [this]; ring)
  simpa [add_eq_zero_iff_eq_neg] using this

/-! ### Shift `M = 1`, `β ≠ 0`: only the fundamental cycle -/

lemma reverse_X_add_one : (X + 1 : ℤ[X]).reverse = X + 1 := by
  have h1 : (1 : ℤ[X]).reverse = 1 := by simp [reverse]
  rw [show (X + 1 : ℤ[X]) = X * 1 + C 1 by simp, reverse_add_C, reverse_X_mul, h1]
  simp; ring

lemma natDegree_three : (X ^ 2 + X + 1 : ℤ[X]).natDegree = 2 := by
  compute_degree!

lemma reverse_three : (X ^ 2 + X + 1 : ℤ[X]).reverse = X ^ 2 + X + 1 := by
  have h2 : (X ^ 2 + X : ℤ[X]).natDegree = 2 := by compute_degree!
  rw [show (X ^ 2 + X + 1 : ℤ[X]) = X * (X + 1) + C 1 by simp; ring, reverse_add_C,
    reverse_X_mul, reverse_X_add_one, show X * (X + 1) = (X ^ 2 + X : ℤ[X]) by ring, h2]
  simp; ring

lemma reflect_two_three : reflect 2 (X ^ 2 + X + 1 : ℤ[X]) = X ^ 2 + X + 1 := by
  have := reverse_three
  rwa [reverse, natDegree_three] at this

/-- Reversal of an odd step at `M = 1` for `s ≠ 0`: the source term `X` lands at
    `X^{d+1}`, `d = natDegree s`. -/
lemma reverse_odd_one (s : ℤ[X]) (hs : s ≠ 0) :
    ((X ^ 2 + X + 1) * s + X).reverse =
      (X ^ 2 + X + 1) * s.reverse + X ^ (s.natDegree + 1) := by
  have h3 : (X ^ 2 + X + 1 : ℤ[X]) ≠ 0 := by
    intro h; have := congrArg natDegree h; rw [natDegree_three] at this; simp at this
  have hdm : ((X ^ 2 + X + 1) * s).natDegree = s.natDegree + 2 := by
    rw [natDegree_mul h3 hs, natDegree_three]; ring
  have hd : ((X ^ 2 + X + 1) * s + X).natDegree = s.natDegree + 2 := by
    rw [natDegree_add_eq_left_of_natDegree_lt (by rw [hdm]; simp), hdm]
  show reflect _ _ = _
  rw [hd, reflect_add]
  congr 1
  · rw [show s.natDegree + 2 = 2 + s.natDegree by ring,
      reflect_mul _ _ (le_of_eq natDegree_three) le_rfl, reflect_two_three]
    rfl
  · rw [show (X : ℤ[X]) = X ^ 1 by simp, reflect_monomial, revAt_le (by omega)]
    simp

lemma X_add_one_ne_zero' : (X + 1 : ℤ[X]) ≠ 0 := by
  intro h; have := congrArg (coeff · 0) h; simp at this

lemma natDegree_X_add_one : (X + 1 : ℤ[X]).natDegree = 1 := by compute_degree!

lemma reverse_even (s s' : ℤ[X]) (h : (X + 1) * s' = s) :
    (X + 1) * s'.reverse = s.reverse := by
  rw [← h, reverse_mul_of_domain, reverse_X_add_one]

theorem classify_one_unit (s : ℕ → ℤ[X]) (K : ℕ) (hK1 : 1 ≤ K) (hK : s K = s 0)
    (hstep : ∀ j < K, StepRel 1 (s j) (s (j + 1)))
    (hβ : (s 0).coeff 0 ≠ 0) : s 0 = 1 ∨ s 0 = X + 1 := by
  have hc0 := coeff_zero_invariant 1 le_rfl s K hstep
  have hne : ∀ i ≤ K, s i ≠ 0 := by
    intro i hi h; apply hβ; rw [← hc0 i hi, h, coeff_zero]
  by_cases hconst : ∃ j < K, (s j).natDegree = 0
  · -- the cycle passes through a constant, which must be `1`: the fundamental cycle
    obtain ⟨j, hj, hd⟩ := hconst
    have prop : ∀ i, j ≤ i → i ≤ K → s i = 1 ∨ s i = X + 1 := by
      intro i hji hiK
      induction i, hji using Nat.le_induction with
      | base =>
        left
        rw [eq_C_of_natDegree_eq_zero hd]
        set c := (s j).coeff 0 with hcdef
        rcases hstep j hj with hE | hO
        · exfalso
          have := congrArg natDegree hE
          rw [eq_C_of_natDegree_eq_zero hd, natDegree_C,
            natDegree_mul X_add_one_ne_zero' (hne _ (by omega)), natDegree_X_add_one] at this
          omega
        · have := congrArg (eval (-1 : ℤ)) hO
          rw [eq_C_of_natDegree_eq_zero hd] at this
          simp at this
          rw [show c = 1 by linarith]; simp
      | succ i hji ih =>
        have hi : i < K := by omega
        rcases ih (by omega) with h1 | h1
        · rcases hstep i hi with hE | hO
          · exfalso; have := congrArg (eval (-1 : ℤ)) hE; rw [h1] at this; simp at this
          · right
            rw [h1] at hO
            apply mul_left_cancel₀ (show (X + 1 : ℤ[X]) ≠ 0 from X_add_one_ne_zero')
            rw [hO, pow_one]; ring
        · rcases hstep i hi with hE | hO
          · left
            rw [h1] at hE
            apply mul_left_cancel₀ (show (X + 1 : ℤ[X]) ≠ 0 from X_add_one_ne_zero')
            rw [hE, mul_one]
          · exfalso; have := congrArg (eval (-1 : ℤ)) hO; rw [h1] at this; simp at this
    rw [← hK]; exact prop K (by omega) le_rfl
  · -- every term has degree ≥ 1: run the core lemma on the reversed sequence
    push_neg at hconst
    exfalso
    set T := fun i => (s i).reverse with hT
    have hodd := core
      (fun t t' => ∃ m, 2 ≤ m ∧ (X + 1) * t' = (X ^ 2 + X + 1) * t + X ^ m)
      (fun t t' ⟨m, hm, h⟩ => odd_coeffs m hm h) T K (by simp [hT, hK]) (by
        intro j hj
        rcases hstep j hj with hE | hO
        · left; exact reverse_even _ _ hE
        · right
          refine ⟨(s j).natDegree + 1, by have := hconst j hj; omega, ?_⟩
          simp only [hT]
          rw [pow_one] at hO
          rw [← reverse_odd_one _ (hne j (by omega)), ← hO, reverse_mul_of_domain,
            reverse_X_add_one])
      (by simp only [hT]; rw [coeff_zero_reverse]; exact leadingCoeff_ne_zero.mpr (hne 0 (by omega)))
    -- every original step is odd, so the shifted sequence `X·s + 1` obeys the linear recursion
    have allodd : ∀ j < K, (X + 1) * s (j + 1) = (X ^ 2 + X + 1) * s j + X ^ 1 := by
      intro j hj
      rcases hstep j hj with hE | hO
      · exfalso
        obtain ⟨m, _, h⟩ := hodd j hj
        have hE' := reverse_even _ _ hE
        simp only [hT] at h
        have h3 := hE'.symm.trans h
        have h4 := congrArg (eval (-1 : ℤ)) h3
        simp at h4
      · exact hO
    have := affine_zero (fun i => X * s i + 1) K hK1 (by simp [hK]) (by
      intro j hj; simp only
      rw [mul_add, mul_left_comm, allodd j hj]; ring)
    have := congrArg (coeff · 0) this
    simp at this

/-! ### The classification -/

theorem cycle_classification (M : ℕ) :
    ∀ (s : ℕ → ℤ[X]) (K : ℕ), 1 ≤ K → s K = s 0 →
      (∀ j < K, StepRel M (s j) (s (j + 1))) → Cl M (s 0) := by
  induction M with
  | zero =>
    intro s K hK1 hK hstep
    left; exact classify_zero s K hK1 hK hstep
  | succ M ih =>
    intro s K hK1 hK hstep
    by_cases hβ : (s 0).coeff 0 = 0
    · have h0 : ∀ i ≤ K, (s i).coeff 0 = 0 := fun i hi => by
        rw [coeff_zero_invariant (M + 1) (by omega) s K hstep i hi, hβ]
      have hr := ih (fun i => (s i).divX) K hK1 (by simp [hK]) (reduce M s K hstep h0)
      have := Cl_succ_of_Cl M _ hr
      rwa [X_mul_divX_of_coeff_zero _ hβ] at this
    · rcases Nat.lt_or_ge M 1 with hM | hM
      · have hM0 : M = 0 := by omega
        subst hM0
        right; right
        refine ⟨le_rfl, ?_⟩
        rcases classify_one_unit s K hK1 hK hstep hβ with h | h
        · left; simpa using h
        · right; simpa [add_comm] using h
      · right; left
        exact ⟨by omega, classify_ge_two_unit (M + 1) (by omega) s K hK1 hK hstep hβ⟩

/-! ### The statement on the Laurent ring `ℤ[q^{±1}]` -/

open LaurentPolynomial in
/-- **Cycle classification for the Skein–Collatz map on `ℤ[q^{±1}]`.**
    Every periodic orbit (`K ≥ 1` steps, each even or odd) starts at `0`, at the
    odd fixed point `-q⁻²`, or on the fundamental cycle `{q⁻¹, 1 + q⁻¹}`. -/
theorem laurent_cycle_classification (P : ℕ → LaurentPolynomial ℤ) (K : ℕ) (hK1 : 1 ≤ K)
    (hK : P K = P 0)
    (hstep : ∀ j < K, (T 1 + 1) * P (j + 1) = P j ∨
      (T 1 + 1) * P (j + 1) = (T 2 + T 1 + 1) * P j + 1) :
    P 0 = 0 ∨ P 0 = -T (-2) ∨ P 0 = T (-1) ∨ P 0 = 1 + T (-1) := by
  -- a common shift `N` making every term a polynomial
  have hN : ∀ L : ℕ, ∃ N : ℕ, ∀ j ≤ L, ∃ f : ℤ[X], toLaurent f = P j * T N := by
    intro L
    induction L with
    | zero =>
      obtain ⟨n, f, hf⟩ := exists_T_pow (P 0)
      exact ⟨n, fun j hj => ⟨f, by rw [show j = 0 by omega]; exact hf⟩⟩
    | succ L ih =>
      obtain ⟨N, hN⟩ := ih
      obtain ⟨n, f, hf⟩ := exists_T_pow (P (L + 1))
      refine ⟨N + n, fun j hj => ?_⟩
      rcases Nat.lt_succ_iff_lt_or_eq.mp (Nat.lt_succ_of_le hj) with hj | hj
      · obtain ⟨g, hg⟩ := hN j (by omega)
        refine ⟨g * X ^ n, ?_⟩
        rw [map_mul, hg, toLaurent_X_pow, Nat.cast_add, T_add]; ring
      · subst hj
        refine ⟨f * X ^ N, ?_⟩
        rw [map_mul, hf, toLaurent_X_pow, Nat.cast_add, T_add]; ring
  obtain ⟨N, hN⟩ := hN K
  have H : ∀ j, ∃ f : ℤ[X], j ≤ K → toLaurent f = P j * T N := by
    intro j
    by_cases hj : j ≤ K
    · obtain ⟨f, hf⟩ := hN j hj; exact ⟨f, fun _ => hf⟩
    · exact ⟨0, fun h => absurd h hj⟩
  choose s hs using H
  have hsK : s K = s 0 := by
    apply toLaurent_injective; rw [hs K le_rfl, hs 0 (by omega), hK]
  have hsstep : ∀ j < K, StepRel N (s j) (s (j + 1)) := by
    intro j hj
    have e1 := hs j (by omega)
    have e2 := hs (j + 1) (by omega)
    rcases hstep j hj with hE | hO
    · left
      apply toLaurent_injective
      rw [map_mul, e1, e2, map_add, toLaurent_X, map_one, ← mul_assoc, hE]
    · right
      apply toLaurent_injective
      simp only [map_mul, map_add, map_one, map_pow, toLaurent_X, e1, e2]
      rw [← mul_assoc, hO, show (T 1 : LaurentPolynomial ℤ) ^ N = T N by rw [T_pow, mul_one],
        show (T 1 : LaurentPolynomial ℤ) ^ 2 = T 2 by rw [T_pow]; norm_num]
      ring
  have hcl := cycle_classification N s K hK1 hsK hsstep
  have h0 := hs 0 (by omega)
  -- divide by `T N`
  have hP : P 0 = toLaurent (s 0) * T (-(N : ℤ)) := by
    rw [h0, mul_assoc, ← T_add, add_neg_cancel, T_zero, mul_one]
  rcases hcl with h | ⟨hM, h⟩ | ⟨hM, h | h⟩
  · left; rw [hP, h]; simp
  · right; left
    rw [hP, h, map_neg, toLaurent_X_pow, neg_mul, ← T_add]
    congr 2; omega
  · right; right; left
    rw [hP, h, toLaurent_X_pow, ← T_add]
    congr 1; omega
  · right; right; right
    rw [hP, h, map_add, toLaurent_X_pow, toLaurent_X_pow, add_mul, ← T_add, ← T_add]
    rw [show ((N : ℕ) : ℤ) + -N = 0 by ring, T_zero]
    congr 2; omega

end QOU.AppendixSurreals.CollatzCycleClassification
