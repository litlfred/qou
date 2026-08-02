import Mathlib.Tactic
import QOU.Archimedean.lepton_continuant_recurrence

/-!
# QOU.Archimedean.lepton_continuant_divisibility_general — the general harmonic law

**Interpretive derivation** for the three-generation gap
([`prop:lepton-meson-torus-knot-dictionary`](../../../quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md),
bean `qou-x4qm`).  Universalises the four hand-checked instances of
`lepton_continuant_generation_exclusion` (`b₃ ∣ b₉`, `b₃ ∤ b₅`, `b₃ ∤ b₇`)
to **every** winding.

## What this file adds

The sibling file `lepton_continuant_generation_exclusion` proved the
harmonic law `b_a ∣ b_n` only for the genus-admissible window
`{3, 5, 7, 9}`, by explicit polynomial arithmetic.  The audit doc
[`docs/audits/2026-08-02-generation-count-t29-continuant-divisibility.md`]
states the *general* law `b_a ∣ b_n ⟺ a ∣ n`, but only its four instances
were in Lean.  This file derives the **forward** half of that law for
**all** windings, sorry-free:

* `morganVoyceB_add` — the Fibonacci-polynomial addition formula
  `b_{m+n+1} = b_{m+1}·b_{n+1} + b_m·b_n` (the `Polynomial ℤ` lift of
  Mathlib's `Nat.fib_add`), and
* `morganVoyceB_dvd_of_dvd` — `a ∣ n ⟹ b_a ∣ b_n`.

The Morgan–Voyce continuant `bₙ` (`b₀=0, b₁=1, b_{n+2}=X·b_{n+1}+b_n`,
`X` = the Hecke parameter `h = q − q⁻¹`) is the Fibonacci polynomial.  The
forward divisibility is the exact statement *"every composite winding is a
harmonic of a smaller one"*: for `n = a·k` the braid `σ₀ⁿ = (σ₀ᵃ)^k` is a
power of the winding-`a` braid, and its normal-form `σ`-coefficient `bₙ`
factors through `b_a`.  So among the odd windings, **every composite is a
harmonic** — the generation windings are contained in the primes.

## Honest scope — (a), not (b); reverse direction open

This derives the *factorisation* `b_a ∣ b_n`, not a proof that a harmonic
winding cannot be a physical state (that physical bridge stays open, bean
`qou-x4qm`).  The **reverse** implication `b_a ∣ b_n ⟹ a ∣ n` — the
strong-divisibility half that would show the *primes* are the *only* non-
harmonics — is **not** proved here.

-- GAP: the reverse implication `morganVoyceB a ∣ morganVoyceB n → a ∣ n`
-- (for `a ≥ 1`) needs `gcd(morganVoyceB m, morganVoyceB n) =
-- morganVoyceB (Nat.gcd m n)` over `Polynomial ℤ` (the Fibonacci strong-
-- divisibility identity).  The forward `a ∣ n → b_a ∣ b_n` below is the
-- half the physics uses (composite ⟹ harmonic); the reverse strengthens
-- "generations ⊆ primes" to "generations = primes".  Tracked in bean
-- `qou-x4qm` / the 2026-08-02 audit doc.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
-/

namespace QOU.Archimedean

open Polynomial

/-! ### The Fibonacci-polynomial addition formula -/

/-- **Addition formula** for the Morgan–Voyce continuant (Fibonacci
    polynomial): `b_{m+n+1} = b_{m+1}·b_{n+1} + b_m·b_n`.  The
    `Polynomial ℤ` lift of Mathlib's `Nat.fib_add`, proved by two-step
    induction on `n` (fixed `m`), using the defining recurrence. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_add (m n : ℕ) :
    morganVoyceB (m + n + 1)
      = morganVoyceB (m + 1) * morganVoyceB (n + 1)
        + morganVoyceB m * morganVoyceB n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [morganVoyceB]
  | one =>
      rw [show m + 1 + 1 = m + 2 from rfl, morganVoyceB_recurrence]
      simp only [morganVoyceB]
      ring
  | more n ih1 ih2 =>
      rw [show n + 1 + 1 = n + 2 from rfl] at ih2
      have rTop : morganVoyceB (m + (n + 2) + 1)
          = Polynomial.X * morganVoyceB (m + (n + 1) + 1) + morganVoyceB (m + n + 1) := by
        rw [show m + (n + 2) + 1 = (m + n + 1) + 2 from by omega,
            show m + (n + 1) + 1 = (m + n + 1) + 1 from by omega,
            morganVoyceB_recurrence]
      have rB3 : morganVoyceB (n + 2 + 1)
          = Polynomial.X * morganVoyceB (n + 2) + morganVoyceB (n + 1) := by
        rw [show n + 2 + 1 = (n + 1) + 2 from by omega, morganVoyceB_recurrence,
            show n + 1 + 1 = n + 2 from rfl]
      have rB2 : morganVoyceB (n + 2)
          = Polynomial.X * morganVoyceB (n + 1) + morganVoyceB n :=
        morganVoyceB_recurrence n
      rw [rTop, ih2, ih1, rB3, rB2]
      ring

/-! ### Forward divisibility: `a ∣ n ⟹ b_a ∣ b_n` -/

/-- **Forward harmonic law.**  If `a ∣ n` then the winding-`a` continuant
    coefficient divides the winding-`n` one: `morganVoyceB a ∣ morganVoyceB n`.
    Proof: write `n = a·k`, induct on `k`, and split `b_{a·(k+1)} =
    b_{a·k + a}` with the addition formula — both summands are divisible
    by `b_a` (the first structurally, the second by induction). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem morganVoyceB_dvd_of_dvd {a n : ℕ} (h : a ∣ n) :
    morganVoyceB a ∣ morganVoyceB n := by
  obtain ⟨k, rfl⟩ := h
  rcases a with _ | a'
  · simp [morganVoyceB]
  · induction k with
    | zero => simp [morganVoyceB]
    | succ k ih =>
        have key : (a' + 1) * (k + 1) = (a' + 1) * k + a' + 1 := by ring
        rw [key, morganVoyceB_add]
        exact dvd_add (dvd_mul_left _ _) (ih.mul_right _)

/-! ### The general theorem subsumes the four hand-checked instances -/

/-- The sibling file's `b₃ ∣ b₉` (winding 9 is a harmonic of generation 1)
    is now a one-line corollary of the general law (`3 ∣ 9`), rather than
    the explicit cofactor computation `t29_harmonic_of_first_generation`. -/
theorem morganVoyceB_three_dvd_nine :
    morganVoyceB 3 ∣ morganVoyceB 9 :=
  morganVoyceB_dvd_of_dvd (by norm_num)

end QOU.Archimedean
