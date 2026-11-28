import QOU.Transcendental.BringsSurface.BringHasseLocalZeta
import Mathlib.NumberTheory.LSeries.Basic

/-!
# Adelic critical-line persistence for `L(E, s)`, `E` = 50a1 (conjecture, §3b)

Carrier for `conj:adelic-critical-line-persistence` in its current form (owner
card 2026-11-28, *"Restate for L(E,s), keep ζ as backup"*). The `ζ` form,
`QOU.BraidKnot.AdelicCriticalLinePersistence`, is kept only as a labelled
backup.

This is the transcendental side of the strangler split: the L-series, its
continuation and its zeros are analytic. The algebraic core it rests on, the
traces `a_p` and the inequality `a_p² ≤ 4p`, is
`QOU.BringsSurface.BringFrobeniusTraces`.

**Human-readable statement** (the semantic equivalent required by the owner
ruling of 2026-11-28; prose in
`q-geometric-langlands/adelic-critical-line-persistence.md`):

> Let `E` be the elliptic curve `y² + xy + y = x³ − x − 2` (Cremona 50a1),
> whose fourth power is isogenous to the Jacobian of Bring's curve. Let
> `L(E, s) = ∑ aₙ n^{−s}` be its L-function, continued to an entire function.
> If the local Weil bound `a_p² ≤ 4p` holds at every prime of good reduction
> (`p ∤ 10`), then every zero of `L(E, s)` in the strip `1/2 < Re s < 3/2`
> lies on the line `Re s = 1`.

The hypothesis is exactly the local critical-line alignment of Bring's curve:
at a good prime its local zeta is `hasseLocalZeta p a_p`, and `a_p² ≤ 4p` makes
that datum `IsWeilZeta` (`hasseLocalZeta_isWeilZeta`), so `|αᵢ| = p^{1/2}`.

## The datum, and why it pins `L(E, s)`

`L50a1Datum` carries an entire `L` that agrees with the Dirichlet series of
coefficients `a` on `Re s > 3/2`, where `a` is fixed by:
* `a₁ = 1` and multiplicativity on coprime arguments;
* `a_p = p + 1 − #E(𝔽_p)` at every prime, with `#E(𝔽_p)` the point count
  `ec50a1Count` of the minimal model above (the same formula is right at the
  bad primes 2 and 5 for a minimal model);
* the good-prime recurrence `a_{p^{k+2}} = a_p a_{p^{k+1}} − p a_{p^k}` and
  the bad-prime recurrence `a_{p^{k+1}} = a_p a_{p^k}`.

Those conditions fix every coefficient, and the identity theorem then fixes
`L` from its values on `Re s > 3/2`. So any two data have the same `L`: the
datum is the L-function of 50a1, not an arbitrary function.

**What is cited, not formalised.** That a datum exists, i.e. that `L(E, s)`
continues to an entire function, is the modularity of `E` (Wiles; Breuil,
Conrad, Diamond, Taylor). Mathlib has neither the theorem nor the
construction, so the classes below take the datum as a parameter. Hasse's
theorem `a_p² ≤ 4p` for all `p` (1933) is not in Mathlib either; the ten cases
`7 ≤ p ≤ 41` are `bring_hasse_table`.

**Why it is still open.** The hypothesis is Hasse's theorem, which is true.
So the class is, mathematically, equivalent to the Riemann hypothesis for
`L(E, s)`, which is open. Unlike the `ζ` backup, its hypothesis and its
conclusion are about the *same* object: the `a_p` in the hypothesis are the
coefficients of the `L` in the conclusion. **No instance is provided; none
should be added without a proof.**
-/

set_option autoImplicit false

open Complex

namespace QOU.AlgebraicSubstrate

/-- The L-function of 50a1, as a datum: an entire function agreeing on
`Re s > 3/2` with the Dirichlet series whose coefficients are fixed by the
point counts and the Euler-product recurrences. See the module docstring. -/
structure L50a1Datum where
  /-- Dirichlet coefficients `aₙ`. -/
  a : ℕ → ℤ
  a_one : a 1 = 1
  a_mul : ∀ m n : ℕ, Nat.Coprime m n → a (m * n) = a m * a n
  a_prime : ∀ p : ℕ, p.Prime → a p = ec50a1Trace p
  a_good : ∀ p : ℕ, p.Prime → ¬ p ∣ 10 → ∀ k : ℕ,
    a (p ^ (k + 2)) = a p * a (p ^ (k + 1)) - (p : ℤ) * a (p ^ k)
  a_bad : ∀ p : ℕ, p.Prime → p ∣ 10 → ∀ k : ℕ,
    a (p ^ (k + 1)) = a p * a (p ^ k)
  /-- The continued L-function. -/
  L : ℂ → ℂ
  entire : Differentiable ℂ L
  agrees : ∀ s : ℂ, 3 / 2 < s.re → L s = LSeries (fun n => (a n : ℂ)) s

/-- **Riemann hypothesis for `L(E, s)`, `E` = 50a1.** Every zero in the
critical strip `1/2 < Re s < 3/2` lies on `Re s = 1`. -/
def RiemannHypothesis50a1 (D : L50a1Datum) : Prop :=
  ∀ s : ℂ, D.L s = 0 → 1 / 2 < s.re → s.re < 3 / 2 → s.re = 1

/-- **Conjecture (adelic critical-line persistence, current form).** Local
critical-line alignment at every good prime implies the Riemann hypothesis for
`L(E, s)`. Primary conjecture (§3b-tax); no instance. -/
class AdelicCriticalLinePersistenceL (D : L50a1Datum) : Prop where
  persistence :
    (∀ p : ℕ, p.Prime → ¬ p ∣ 10 → (D.a p) ^ 2 ≤ 4 * (p : ℤ)) →
      RiemannHypothesis50a1 D

/-- The hypothesis is the local alignment of Bring's curve: at each good prime
it makes the local datum `hasseLocalZeta p a_p` a Weil datum, so every
Frobenius eigenvalue has `|αᵢ| = p^{1/2}`. -/
theorem local_alignment_of_hasse (D : L50a1Datum) (p : ℕ) (hp : p.Prime)
    (h : (D.a p) ^ 2 ≤ 4 * (p : ℤ)) (i : Fin 8) :
    ‖(hasseLocalZeta (p : ℤ) (D.a p) (by exact_mod_cast hp.pos) h).eigenvalues i‖
      = ((p : ℤ) : ℝ) ^ (1 / 2 : ℝ) :=
  hasseLocalZeta_norm _ _ _ h i

/-- Composition: persistence plus local alignment gives RH for `L(E, s)`. -/
theorem riemannHypothesis50a1_of_persistence (D : L50a1Datum)
    [AdelicCriticalLinePersistenceL D]
    (h_local : ∀ p : ℕ, p.Prime → ¬ p ∣ 10 → (D.a p) ^ 2 ≤ 4 * (p : ℤ)) :
    RiemannHypothesis50a1 D :=
  AdelicCriticalLinePersistenceL.persistence h_local

/-- At the listed primes the datum's coefficients are the table values, so the
local hypothesis holds there (the finite part of Hasse's theorem). -/
theorem datum_hasse_on_table (D : L50a1Datum) :
    ∀ x ∈ bringFrobeniusTraces, (D.a x.1.toNat) ^ 2 ≤ 4 * x.1 := by
  intro x hx
  have hprime : x.1.toNat.Prime := by
    simp only [bringFrobeniusTraces, List.mem_cons, List.not_mem_nil, or_false] at hx
    rcases hx with h | h | h | h | h | h | h | h | h | h <;> subst h <;> decide +kernel
  rw [D.a_prime _ hprime, ec50a1Trace_table x hx]
  exact le_of_lt (bring_hasse_table x hx).2

end QOU.AlgebraicSubstrate
