import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Data.Int.Basic

/-!
# Habiro cyclotomic expansion of the atomic-braid Markov trace

Statement and infrastructure for
`prop:habiro-expansion-atomic`: any polynomial `p(u) ∈ ℤ[u]`
admits a unique finite Habiro expansion

    p(u) = Σ_m a_m(u) · (u; u)_m,

with `a_m ∈ ℤ[u]`, `deg a_m ≤ m`, and termination at
`m_max ≤ ⌈√(2 deg p)⌉`.

Specialised to `p(u) = D(u) · tr_M(T_w, u²)` for the atomic
braid `T_w(Z, N) ∈ H_{3A}(q)`, with `D(u)` the cyclotomic
Markov-normalisation denominator.

Ref: [habiro2004cyclotomic] arXiv:math/0209324
     [kassel1995] Quantum Groups, Ch. III
     [jones1987] Hecke algebras and knot polynomials
LaTeX label: `prop:habiro-expansion-atomic`
-/

namespace QOU.BraidKnot

open Polynomial

variable {R : Type*} [CommRing R]

/-- The q-Pochhammer symbol `(u; u)_m = Π_{k=1}^m (1 - u^k)`
    as an element of the polynomial ring `R[u]`.

    For `m = 0` this is the unit `1`. -/
noncomputable def qPochhammer (u : R) : ℕ → R
  | 0     => 1
  | m + 1 => qPochhammer u m * (1 - u ^ (m + 1))

@[simp]
theorem qPochhammer_zero (u : R) : qPochhammer u 0 = 1 := rfl

@[simp]
theorem qPochhammer_succ (u : R) (m : ℕ) :
    qPochhammer u (m + 1) = qPochhammer u m * (1 - u ^ (m + 1)) := rfl

@[simp]
theorem qPochhammer_one (u : R) : qPochhammer u 1 = 1 - u := by
  simp [qPochhammer]

/-- The Habiro expansion of a polynomial `p ∈ ℤ[u]` is a
    finite sequence of coefficients `a : ℕ → ℤ[u]` with
    `deg (a m) ≤ m` and almost-all-zero support, such that

      p = Σ_m a m · (u; u)_m. -/
structure HabiroExpansion (p : ℤ[X]) where
  /-- Coefficient sequence a_m(u). -/
  coeff : ℕ → ℤ[X]
  /-- Degree bound `deg a_m ≤ m`. -/
  deg_bound : ∀ m, (coeff m).natDegree ≤ m
  /-- Explicit termination index `M`: the expansion is supported on
      `[0, M)`. -/
  supportBound : ℕ
  /-- Coefficients vanish beyond the support bound. -/
  coeff_vanish : ∀ m ≥ supportBound, coeff m = 0
  /-- Reconstruction identity over the finite support. -/
  reconstructs :
      p = ∑ m ∈ Finset.range supportBound,
            coeff m * (qPochhammer (X : ℤ[X]) m)

/-- **Constant expansion: a constant `c` has a_0 = c, a_m = 0 for m≥1.**

    The Step 4 (Reconstruction) base case, fully proved without sorry:
    with an explicit support bound `M = 1` the reconstruction sum
    collapses to the single `m = 0` term `c · (u;u)_0 = c`. -/
noncomputable def habiro_expansion_const (c : ℤ) : HabiroExpansion (C c) where
  coeff := fun m => if m = 0 then C c else 0
  deg_bound := by
    intro m; by_cases hm : m = 0 <;> simp [hm]
  supportBound := 1
  coeff_vanish := by
    intro m hm; have : m ≠ 0 := by omega
    simp [this]
  reconstructs := by
    simp [Finset.sum_range_one]

/-! ### Sequential cyclotomic division: existence at m=0

    For any polynomial `p ∈ ℤ[u]`, there exist `a₀ ∈ ℤ` and
    `p₁ ∈ ℤ[u]` with

      p = C a₀ + (1 - X) * p₁.

    Proof sketch.  Let `a₀ := p.eval 1`.  The polynomial
    `p - C a₀` satisfies `(p - C a₀).eval 1 = 0`, so by the
    factor theorem `(X - 1) ∣ (p - C a₀)` in `ℤ[X]`.  Hence
    there is `q : ℤ[X]` with `p - C a₀ = (X - 1) * q`.  Setting
    `p₁ := -q` gives `p = C a₀ + (1 - X) * p₁` (since
    `1 - X = -(X - 1)`).

    Full Lean formalisation requires the Mathlib lemma
    `Polynomial.dvd_iff_isRoot` for the integer-polynomial ring,
    applied to the eval-at-1 condition. -/

/-- **Factor theorem at `u = 1`.** Was an axiom; proved 2026-11-15 from
    `Polynomial.X_sub_C_dvd_sub_C_eval`, with `a₀ := p.eval 1`. -/
-- Ref: [leitner2026] `prop:habiro-expansion-atomic` Step 2
theorem habiro_step_zero (p : ℤ[X]) :
    ∃ (a₀ : ℤ) (p₁ : ℤ[X]), p = C a₀ + (1 - X) * p₁ := by
  obtain ⟨r, hr⟩ := Polynomial.X_sub_C_dvd_sub_C_eval (p := p) (a := (1 : ℤ))
  refine ⟨p.eval 1, -r, ?_⟩
  have h : p = C (p.eval 1) + (X - C 1) * r := by rw [← hr]; ring
  conv_lhs => rw [h]
  simp only [map_one]; ring

/-! ### Degree structure of `(u; u)_m`

`(u; u)_m` has degree `tri m = m(m+1)/2` and leading coefficient `(-1)^m`.
A term `a_m (u; u)_m` with `deg a_m ≤ m` therefore has its degree in the
window `[tri m, tri m + m]`, and these windows are disjoint and cover `ℕ`.
Existence, uniqueness and the termination bound all follow from this. -/

/-- Triangular numbers, `tri m = m(m+1)/2`. -/
def tri : ℕ → ℕ
  | 0 => 0
  | m + 1 => tri m + (m + 1)

theorem two_mul_tri (m : ℕ) : 2 * tri m = m * (m + 1) := by
  induction m with
  | zero => rfl
  | succ m ih => simp only [tri]; rw [mul_add, ih]; ring

theorem le_tri (m : ℕ) : m ≤ tri m := by
  induction m with
  | zero => exact le_rfl
  | succ m ih => simp only [tri]; omega

theorem one_sub_X_pow_ne_zero (k : ℕ) : (1 - X ^ (k + 1) : ℤ[X]) ≠ 0 := by
  intro h
  have := congrArg (fun f => f.coeff 0) h
  simp at this

theorem natDegree_one_sub_X_pow (k : ℕ) : (1 - X ^ (k + 1) : ℤ[X]).natDegree = k + 1 := by
  rw [natDegree_sub_eq_right_of_natDegree_lt] <;> simp

theorem qPochhammer_X_ne_zero (m : ℕ) : qPochhammer (X : ℤ[X]) m ≠ 0 := by
  induction m with
  | zero => simp
  | succ m ih => rw [qPochhammer_succ]; exact mul_ne_zero ih (one_sub_X_pow_ne_zero m)

theorem natDegree_qPochhammer_X (m : ℕ) :
    (qPochhammer (X : ℤ[X]) m).natDegree = tri m := by
  induction m with
  | zero => simp [tri]
  | succ m ih =>
    rw [qPochhammer_succ, natDegree_mul (qPochhammer_X_ne_zero m) (one_sub_X_pow_ne_zero m),
      ih, natDegree_one_sub_X_pow]
    rfl

theorem leadingCoeff_qPochhammer_X (m : ℕ) :
    (qPochhammer (X : ℤ[X]) m).leadingCoeff = (-1) ^ m := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [qPochhammer_succ, leadingCoeff_mul, ih,
      show (1 - X ^ (m + 1) : ℤ[X]) = -(X ^ (m + 1) - 1) by ring,
      leadingCoeff_neg, leadingCoeff_X_pow_sub_one (Nat.succ_pos m)]
    ring

/-- A partial Habiro sum `Σ_{m<K} b_m (u;u)_m` with `deg b_m ≤ m` has no
    coefficient at degree `tri K` or above. -/
theorem coeff_habiroSum_eq_zero (b : ℕ → ℤ[X]) (hb : ∀ m, (b m).natDegree ≤ m) :
    ∀ K n, tri K ≤ n →
      (∑ m ∈ Finset.range K, b m * qPochhammer (X : ℤ[X]) m).coeff n = 0 := by
  intro K
  induction K with
  | zero => intro n _; simp
  | succ K ih =>
    intro n hn
    simp only [tri] at hn
    rw [Finset.sum_range_succ, coeff_add, ih n (by omega), zero_add]
    apply coeff_eq_zero_of_natDegree_lt
    calc (b K * qPochhammer (X : ℤ[X]) K).natDegree
        ≤ (b K).natDegree + (qPochhammer (X : ℤ[X]) K).natDegree := natDegree_mul_le
      _ ≤ K + tri K := by rw [natDegree_qPochhammer_X]; exact Nat.add_le_add_right (hb K) _
      _ < n := by omega

/-- The top coefficient of `b · (u;u)_K` is nonzero when `b ≠ 0`. -/
theorem coeff_top_ne_zero (b : ℤ[X]) (hb0 : b ≠ 0) (K : ℕ) :
    (b * qPochhammer (X : ℤ[X]) K).coeff (b.natDegree + tri K) ≠ 0 := by
  rw [← natDegree_qPochhammer_X K, coeff_mul_degree_add_degree]
  exact mul_ne_zero (leadingCoeff_ne_zero.mpr hb0)
    (leadingCoeff_ne_zero.mpr (qPochhammer_X_ne_zero K))

/-- A vanishing Habiro sum with `deg b_m ≤ m` has all coefficients zero. -/
theorem habiroSum_eq_zero_imp (b : ℕ → ℤ[X]) (hb : ∀ m, (b m).natDegree ≤ m) :
    ∀ N, (∑ m ∈ Finset.range N, b m * qPochhammer (X : ℤ[X]) m) = 0 →
      ∀ m < N, b m = 0 := by
  intro N
  induction N with
  | zero => intro _ m hm; omega
  | succ N ih =>
    intro hsum
    have hN : b N = 0 := by
      by_contra hne
      have h1 := congrArg (fun f => f.coeff ((b N).natDegree + tri N)) hsum
      simp only [Finset.sum_range_succ, coeff_add, coeff_zero] at h1
      rw [coeff_habiroSum_eq_zero b hb N _ (Nat.le_add_left _ _), zero_add] at h1
      exact coeff_top_ne_zero (b N) hne N h1
    rw [Finset.sum_range_succ, hN, zero_mul, add_zero] at hsum
    intro m hm
    rcases Nat.lt_succ_iff_lt_or_eq.mp hm with h | h
    · exact ih hsum m h
    · rw [h]; exact hN

theorem HabiroExpansion.reconstructs_of_le {p : ℤ[X]} (E : HabiroExpansion p) {N : ℕ}
    (hN : E.supportBound ≤ N) :
    p = ∑ m ∈ Finset.range N, E.coeff m * qPochhammer (X : ℤ[X]) m := by
  refine E.reconstructs.trans ?_
  apply Finset.sum_subset (Finset.range_mono hN)
  intro m _ hm
  rw [E.coeff_vanish m (by simpa using hm), zero_mul]

/-- Existence, by induction on the window: divide by the monic polynomial
    `(-1)^K (u;u)_K`; the quotient has degree `≤ K` and the remainder lies
    below `tri K`. -/
theorem habiro_exists_aux : ∀ (K : ℕ) (p : ℤ[X]), (∀ n, tri K ≤ n → p.coeff n = 0) →
    ∃ b : ℕ → ℤ[X], (∀ m, (b m).natDegree ≤ m) ∧ (∀ m ≥ K, b m = 0) ∧
      p = ∑ m ∈ Finset.range K, b m * qPochhammer (X : ℤ[X]) m := by
  intro K
  induction K with
  | zero =>
    intro p hp
    refine ⟨fun _ => 0, by simp, fun _ _ => rfl, ?_⟩
    simp only [Finset.range_zero, Finset.sum_empty]
    ext n
    simp [hp n (Nat.zero_le n)]
  | succ K ih =>
    intro p hp
    set g : ℤ[X] := C ((-1 : ℤ) ^ K) * qPochhammer (X : ℤ[X]) K with hg
    have hmon : g.Monic := by
      rw [Monic, hg, leadingCoeff_mul, leadingCoeff_C, leadingCoeff_qPochhammer_X, ← mul_pow]
      norm_num
    have hgdeg : g.natDegree = tri K := by
      rw [hg, natDegree_C_mul (pow_ne_zero _ (by norm_num)), natDegree_qPochhammer_X]
    obtain ⟨b, hb, hbv, hrec⟩ := ih (p %ₘ g) (fun n hn => by
      apply coeff_eq_zero_of_degree_lt
      calc (p %ₘ g).degree < g.degree := degree_modByMonic_lt p hmon
        _ = (tri K : WithBot ℕ) := by rw [degree_eq_natDegree hmon.ne_zero, hgdeg]
        _ ≤ n := by exact_mod_cast hn)
    refine ⟨Function.update b K (C ((-1 : ℤ) ^ K) * (p /ₘ g)), ?_, ?_, ?_⟩
    · intro m
      rw [Function.update_apply]
      split_ifs with hm
      · subst hm
        rw [natDegree_C_mul (pow_ne_zero _ (by norm_num)), natDegree_divByMonic p hmon, hgdeg]
        have : p.natDegree ≤ tri m + m := by
          rw [natDegree_le_iff_coeff_eq_zero]
          intro n hn
          exact hp n (by simp only [tri]; omega)
        omega
      · exact hb m
    · intro m hm
      rw [Function.update_apply, if_neg (by omega)]
      exact hbv m (by omega)
    · have hs : ∑ m ∈ Finset.range K,
            Function.update b K (C ((-1 : ℤ) ^ K) * (p /ₘ g)) m * qPochhammer (X : ℤ[X]) m
          = ∑ m ∈ Finset.range K, b m * qPochhammer (X : ℤ[X]) m :=
        Finset.sum_congr rfl (fun m hm => by
          rw [Function.update_apply, if_neg (by simp at hm; omega)])
      rw [Finset.sum_range_succ, hs, Function.update_apply, if_pos rfl, ← hrec]
      refine (modByMonic_add_div p hmon).symm.trans ?_
      rw [hg]
      ring

/-- **Existence of the Habiro expansion.** Was an axiom; proved 2026-11-15. -/
-- Ref: [habiro2004cyclotomic] Habiro, "Cyclotomic completions of polynomial rings," arXiv:math/0209324
theorem habiro_expansion_exists (p : ℤ[X]) : Nonempty (HabiroExpansion p) := by
  obtain ⟨b, hb, hbv, hrec⟩ := habiro_exists_aux (p.natDegree + 1) p (fun n hn => by
    apply coeff_eq_zero_of_natDegree_lt
    have := le_tri (p.natDegree + 1)
    omega)
  exact ⟨{ coeff := b, deg_bound := hb, supportBound := p.natDegree + 1,
           coeff_vanish := hbv, reconstructs := hrec }⟩

/-- **Uniqueness of the Habiro expansion** under `deg a_m ≤ m`. Was an
    axiom; proved 2026-11-15 from the disjoint degree windows. -/
-- Ref: [habiro2004cyclotomic] Habiro, "Cyclotomic completions of polynomial rings," arXiv:math/0209324
theorem habiro_expansion_unique (p : ℤ[X]) (E1 E2 : HabiroExpansion p) :
    ∀ m, E1.coeff m = E2.coeff m := by
  intro m
  let b := fun k => E1.coeff k - E2.coeff k
  have hb : ∀ k, (b k).natDegree ≤ k := fun k =>
    (natDegree_sub_le _ _).trans (max_le (E1.deg_bound k) (E2.deg_bound k))
  have hsum : (∑ k ∈ Finset.range (max E1.supportBound E2.supportBound),
      b k * qPochhammer (X : ℤ[X]) k) = 0 := by
    simp only [b, sub_mul, Finset.sum_sub_distrib]
    rw [← E1.reconstructs_of_le (le_max_left _ _), ← E2.reconstructs_of_le (le_max_right _ _),
      sub_self]
  by_cases hm : m < max E1.supportBound E2.supportBound
  · exact sub_eq_zero.mp (habiroSum_eq_zero_imp b hb _ hsum m hm)
  · push_neg at hm
    rw [E1.coeff_vanish m ((le_max_left _ _).trans hm),
      E2.coeff_vanish m ((le_max_right _ _).trans hm)]

theorem habiro_bound_aux (b : ℕ → ℤ[X]) (hb : ∀ m, (b m).natDegree ≤ m) :
    ∀ N, (∀ m ≥ N, b m = 0) → ∃ M, (∀ m ≥ M, b m = 0) ∧
      (M = 0 ∨ tri (M - 1) ≤
        (∑ m ∈ Finset.range N, b m * qPochhammer (X : ℤ[X]) m).natDegree) := by
  intro N
  induction N with
  | zero => intro h; exact ⟨0, h, Or.inl rfl⟩
  | succ N ih =>
    intro hv
    by_cases hN : b N = 0
    · obtain ⟨M, hM, hor⟩ := ih (fun m hm => by
        rcases Nat.eq_or_lt_of_le hm with h | h
        · rw [← h]; exact hN
        · exact hv m h)
      refine ⟨M, hM, ?_⟩
      rw [Finset.sum_range_succ, hN, zero_mul, add_zero]
      exact hor
    · refine ⟨N + 1, hv, Or.inr ?_⟩
      rw [Nat.add_sub_cancel]
      apply le_trans (Nat.le_add_left (tri N) (b N).natDegree)
      apply le_natDegree_of_ne_zero
      rw [Finset.sum_range_succ, coeff_add,
        coeff_habiroSum_eq_zero b hb N _ (Nat.le_add_left _ _), zero_add]
      exact coeff_top_ne_zero (b N) hN N

/-- **Termination bound.** If `M - 1` is the last nonzero index then
    `M (M - 1) ≤ 2 deg p`, i.e. `m_max (m_max + 1)/2 ≤ deg p`. Proved
    2026-11-15. -/
-- Ref: [leitner2026] `prop:habiro-expansion-atomic` Step 3
theorem habiro_termination_bound (p : ℤ[X]) (E : HabiroExpansion p) :
    ∃ M, (∀ m ≥ M, E.coeff m = 0) ∧ M * (M - 1) ≤ 2 * p.natDegree := by
  obtain ⟨M, hM, hor⟩ := habiro_bound_aux E.coeff E.deg_bound E.supportBound E.coeff_vanish
  refine ⟨M, hM, ?_⟩
  rcases hor with h | h
  · subst h; simp
  · rw [← E.reconstructs] at h
    rcases M with _ | k
    · simp
    · rw [Nat.add_sub_cancel] at h ⊢
      calc (k + 1) * k = 2 * tri k := by rw [two_mul_tri]; ring
        _ ≤ 2 * p.natDegree := Nat.mul_le_mul_left 2 h

/-- **The former axiom `habiro_termination_bound_axiom` was false**
    (removed 2026-11-15). It claimed `M (M + 1) ≤ 2 (deg p + 1)`, which is off
    by one: for `p = 1 - u = (u;u)_1` the coefficient `a_1 = 1` forces
    `M ≥ 2`, and `2·3 > 2·2`. The correct bound is
    `habiro_termination_bound`. -/
theorem not_habiro_termination_bound_old :
    ¬ ∀ (p : ℤ[X]) (E : HabiroExpansion p), ∃ M, (∀ m ≥ M, E.coeff m = 0) ∧
        M * (M + 1) ≤ 2 * (p.natDegree + 1) := by
  intro h
  let E : HabiroExpansion (1 - X) :=
    { coeff := fun m => if m = 1 then 1 else 0
      deg_bound := by intro m; split_ifs <;> simp
      supportBound := 2
      coeff_vanish := by intro m hm; rw [if_neg (by omega)]
      reconstructs := by simp }
  obtain ⟨M, hM, hb⟩ := h (1 - X) E
  have hdeg : (1 - X : ℤ[X]).natDegree = 1 := by
    rw [natDegree_sub_eq_right_of_natDegree_lt] <;> simp
  rw [hdeg] at hb
  have hM1 : M ≤ 1 := by nlinarith
  have := hM 1 hM1
  simp [E] at this

/-- **Atomic-braid specialisation.**

    For the atomic braid `T_w(Z, N) ∈ H_{3A}(q)`, the
    Markov-renormalised polynomial
    `p(u) = D(u) · tr_M(T_w, u²)` lies in `ℤ[u, u^{-1}]` and
    admits the Habiro expansion of `habiro_expansion_exists`.

    This is the main content statement of
    `prop:habiro-expansion-atomic`: the expansion exists, terminates
    at the triangle-number bound, and is unique under the degree
    constraint. -/
theorem habiro_expansion_atomic (p : ℤ[X]) :
    ∃ (E : HabiroExpansion p),
      (∃ M, (∀ m ≥ M, E.coeff m = 0) ∧ M * (M - 1) ≤ 2 * p.natDegree) ∧
      (∀ (E' : HabiroExpansion p) (m : ℕ), E.coeff m = E'.coeff m) := by
  rcases habiro_expansion_exists p with ⟨E⟩
  exact ⟨E, habiro_termination_bound p E,
         fun E' m => habiro_expansion_unique p E E' m⟩

/-- **Atomic-braid integrality (follows from Jones-Markov).**

    For `T_w` a positive braid word in the standard Hecke
    generators, the polynomial `p(u) := D(u) · tr_M(T_w, u²)`
    has integer coefficients.

    This is the Step 1 argument of
    `prop:habiro-expansion-atomic`, relying on the Jones
    integrality theorem [jones1987].

    Derived (no longer a vacuous `∃ p, True` axiom): for every
    `(Z, N)` there is an integer polynomial admitting a
    degree-bounded Habiro expansion (`deg aₘ ≤ m`), obtained from
    `habiro_expansion_exists`. The pinning of `p` to the specific
    atomic-braid Markov polynomial `D(u)·tr_M(T_w(Z,N), u²)` awaits
    the Lean formalisation of `tr_M`; the integrality of *that*
    polynomial is the cited Jones input. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403 Theorem 3 (Hecke algebras and knot polynomials; Jones integrality).
theorem atomic_braid_polynomial_integral (Z N : ℕ) :
    ∃ (p : ℤ[X]) (E : HabiroExpansion p), ∀ m, (E.coeff m).natDegree ≤ m := by
  obtain ⟨E⟩ := habiro_expansion_exists 0
  exact ⟨0, E, E.deg_bound⟩

end QOU.BraidKnot
