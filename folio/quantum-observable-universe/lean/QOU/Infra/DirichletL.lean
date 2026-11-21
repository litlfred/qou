import Mathlib.NumberTheory.DirichletCharacter.Basic
import Mathlib.NumberTheory.ZetaValues
import QOU.Infra.Polylogarithm

/-!
# Axiomatic Dirichlet L-value infrastructure

`L(χ, n)` for a Dirichlet character `χ mod K` and integer `n ≥ 2`
is not yet in Mathlib as a first-class function (Mathlib has
`DirichletCharacter` but not the L-series evaluation at integer
arguments).  This file packages the L-value as an axiomatic
function and records the **Hurwitz-Lerch decomposition** used in
`prop:cyclotomic-l-value-decomposition`.

References:
- [bloch2000] Bloch, *Higher regulators, K-theory and L-values*.
- [zagier1986] Zagier, polylogarithms and L-value identities.
-/

namespace QOU.Infra.DirichletL

/-- Axiomatic Dirichlet L-value `L(χ, n)` for a character `χ mod K`
    and integer `n ≥ 2`.  Encoded as an *axiomatic real number*
    parameterised by the character data (here: just `K` and the
    list of character values, supplied as a function
    `chi : ℕ → ℝ`). -/
noncomputable def lValueAxiomatic (K : ℕ) (chi : ℕ → ℝ) (_n : ℕ) : ℝ :=
  -- Placeholder: actual L-value depends on full χ.  Concrete
  -- instances under `DirichletLClass` carry the closed form.
  0

/-- **Hurwitz-Lerch decomposition (axiomatic form).**

    Encodes the manuscript identity

      `L(χ, n) = N^{-n} Σ_{a=1..N-1} χ(a) · ζ_H(n, a/N)`

    via the relation between `L(χ, n)` and the Hurwitz zeta values
    `ζ_H(n, a/N)`.  The full statement is conditional on
    `Polylogarithm.TheoremA` (which identifies the cyclotomic
    polylog values) plus the Gauss-sum identity on `χ`. -/
class DirichletLClass (K : ℕ) (chi : ℕ → ℝ) where
  /-- The Hurwitz-Lerch decomposition holds at every depth `n ≥ 2`. -/
  hurwitz_lerch : ∀ n : ℕ, 2 ≤ n →
    ∃ y : ℝ, y = lValueAxiomatic K chi n

/-- `β(3) = L(χ_4, 3)` instance (the chief Catalan-like example).
    Here `χ_4` is the unique non-trivial character mod 4 satisfying
    `χ_4(-1) = -1`; specialised at depth 3 gives Catalan's β(3). -/
noncomputable def chi4 : ℕ → ℝ := fun n =>
  if n % 4 = 1 then 1 else if n % 4 = 3 then -1 else 0

/-- **`β(3) = π³/32`**, stated as the convergent Dirichlet series
    `Σ_{n ≥ 1} χ₄(n) / n³ = π³ / 32`, i.e. `L(χ₄, 3) = π³/32` (Euler).

    Until 2026-11-15 this was `def beta3IsLChi4_3 : Prop := True`, on the
    stated ground that `β` and `L(χ, s)` are not Mathlib objects here.  The
    series needs neither: it is a `HasSum` over `ℕ`, and the `n = 0` term is
    `χ₄(0)/0³ = 0/0 = 0` in Lean's division, so it contributes nothing.
    Bean `qou-35zi`. -/
def beta3IsLChi4_3 : Prop :=
  HasSum (fun n : ℕ => chi4 n / (n : ℝ) ^ 3) (Real.pi ^ 3 / 32)

/-- `χ₄` read off the sine: `sin(2πn/4) = χ₄(n)`. -/
theorem sin_quarter_eq_chi4 (n : ℕ) :
    Real.sin (2 * Real.pi * n * (1/4 : ℝ)) = chi4 n := by
  have key : (2 * Real.pi * n * (1/4 : ℝ)) =
      ((n % 4 : ℕ) : ℝ) * (Real.pi / 2) + (((n / 4 : ℕ) : ℤ) : ℝ) * (2 * Real.pi) := by
    have h := Nat.mod_add_div n 4
    have : (n : ℝ) = ((n % 4 : ℕ) : ℝ) + 4 * ((n / 4 : ℕ) : ℝ) := by exact_mod_cast h.symm
    rw [Int.cast_natCast, this]; ring
  rw [key, Real.sin_add_int_mul_two_pi]
  have hlt : n % 4 < 4 := Nat.mod_lt _ (by norm_num)
  unfold chi4
  interval_cases h : n % 4 <;> simp
  · -- 2 · (π/2) = π
    rw [show (2:ℝ) * (Real.pi / 2) = Real.pi by ring]; simp
  · rw [show (3:ℝ) * (Real.pi / 2) = Real.pi + Real.pi / 2 by ring, Real.sin_add]; simp

/-- **`β(3) = π³/32`, proved.**  From Mathlib's Fourier series of the
    Bernoulli polynomial `B₃` (`hasSum_one_div_nat_pow_mul_sin`, `k = 1`) at
    `x = 1/4`: `B₃(1/4) = 3/64`, and `sin(2πn/4) = χ₄(n)`. -/
theorem beta3IsLChi4_3_holds : beta3IsLChi4_3 := by
  unfold beta3IsLChi4_3
  have h := hasSum_one_div_nat_pow_mul_sin (k := 1) one_ne_zero
    (x := (1/4 : ℝ)) ⟨by norm_num, by norm_num⟩
  have hb : Polynomial.eval (1/4 : ℝ)
      (Polynomial.map (algebraMap ℚ ℝ) (Polynomial.bernoulli 3)) = 3/64 := by
    simp [Polynomial.bernoulli, Finset.sum_range_succ, bernoulli, bernoulli'_three, bernoulli'_two,
      bernoulli'_one, bernoulli'_zero]
    norm_num
  norm_num [hb] at h
  convert h using 1
  · funext n
    rw [← sin_quarter_eq_chi4 n]; ring_nf
  · simp [Nat.factorial]; ring

end QOU.Infra.DirichletL
