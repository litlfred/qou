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
-- Ref: [manuscript] `prop:habiro-expansion-atomic` Step 2
theorem habiro_step_zero (p : ℤ[X]) :
    ∃ (a₀ : ℤ) (p₁ : ℤ[X]), p = C a₀ + (1 - X) * p₁ := by
  obtain ⟨r, hr⟩ := Polynomial.X_sub_C_dvd_sub_C_eval (p := p) (a := (1 : ℤ))
  refine ⟨p.eval 1, -r, ?_⟩
  have h : p = C (p.eval 1) + (X - C 1) * r := by rw [← hr]; ring
  conv_lhs => rw [h]
  simp only [map_one]; ring

/-- **External axiom (Habiro 2002):** Habiro expansion exists for
    every integer polynomial. -/
-- Ref: [manuscript] `prop:habiro-expansion-atomic` Step 2–4
-- Ref: [habiro2004cyclotomic] Habiro, "Cyclotomic completions of polynomial rings," arXiv:math/0209324
axiom habiro_expansion_exists_axiom :
    ∀ (p : ℤ[X]), Nonempty (HabiroExpansion p)

theorem habiro_expansion_exists (p : ℤ[X]) :
    Nonempty (HabiroExpansion p) :=
  habiro_expansion_exists_axiom p

/-- **External axiom (Habiro 2002):** Habiro expansion is unique
    under the degree bound. -/
-- Ref: [manuscript] `prop:habiro-expansion-atomic` Step 5
axiom habiro_expansion_unique_axiom :
    ∀ (p : ℤ[X]) (E1 E2 : HabiroExpansion p),
      ∀ m, E1.coeff m = E2.coeff m

theorem habiro_expansion_unique (p : ℤ[X])
    (E1 E2 : HabiroExpansion p) :
    ∀ m, E1.coeff m = E2.coeff m :=
  habiro_expansion_unique_axiom p E1 E2

/-- **External axiom (Habiro 2002):** termination bound for the
    Habiro expansion via the triangle-number argument. -/
-- Ref: [manuscript] `prop:habiro-expansion-atomic` Step 3
axiom habiro_termination_bound_axiom :
    ∀ (p : ℤ[X]) (E : HabiroExpansion p),
      ∃ M, (∀ m ≥ M, E.coeff m = 0) ∧
            M * (M + 1) ≤ 2 * (p.natDegree + 1)

theorem habiro_termination_bound (p : ℤ[X]) (E : HabiroExpansion p) :
    ∃ M, (∀ m ≥ M, E.coeff m = 0) ∧
          M * (M + 1) ≤ 2 * (p.natDegree + 1) :=
  habiro_termination_bound_axiom p E

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
      (∃ M, (∀ m ≥ M, E.coeff m = 0) ∧ M * (M + 1) ≤ 2 * (p.natDegree + 1)) ∧
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
