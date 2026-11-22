import Mathlib.Tactic
import QOU.Archimedean.lepton_continuant_recurrence

/-!
# QOU.ParticleInteractions.even_tower_continuant_harmonics — the boson tower is uniformly harmonic

**Interpretive derivation** for the electroweak/boson even-winding tower
([`conj:electroweak-higgs-torus-link-triplet`](../../../particle-interactions/electroweak-higgs-torus-link-triplet.md)),
the boson-side mirror of the fermion-side generation-exclusion result
(the odd-prime windings `3,5,7`; landing separately in PR #4456).

## Setup

The Gröbner–Shirshov normal form of `T(2,n) = σ₀ⁿ` in `H₂(q)` is
`a_n · 𝟏 + b_n · σ₀` with `b_n = morganVoyceB n` the Morgan–Voyce
(Fibonacci) continuant over `Polynomial ℤ` (`X` = the Hecke parameter
`h = q − q⁻¹`), `b₀ = 0`, `b₁ = 1`, `b_{n+2} = X·b_{n+1} + b_n`
(`lepton_continuant_recurrence`).

The **bosons** are the even windings `n = 2k` (two-component links,
`boson_iff_even`); the electroweak carriers are `W ↔ T(2,4)`,
`Z ↔ T(2,6)`, `H ↔ T(2,8)`, with the Hopf link `T(2,2)` the trivial
fundamental.

## What this file derives

The Morgan–Voyce continuant is a **strong divisibility sequence**: its
polynomial coefficient satisfies `a ∣ n ⇒ b_a ∣ b_n`. This is the
general theorem the fermion sibling's docstring asserts but only
instantiates on `{3,5,7,9}`; here it is **proved in general** from the
addition formula `b_{m+n+1} = b_{m+1}·b_{n+1} + b_m·b_n`, then applied to
the even tower.

Consequences on the boson windings, all `Polynomial ℤ` (derived, not
asserted):

* **Every even winding is a harmonic of the fundamental Hopf continuant**
  `b₂ = X`: `b₂ ∣ b_{2k}` for all `k` (`b2_dvd_even`). The whole boson
  tower descends from the single fundamental `b₂`.
* The concrete carriers, with explicit cofactors:
  `b₂ ∣ b₄`, `b₂ ∣ b₆`, `b₂ ∣ b₈` (all of `W,Z,H` are `b₂`-harmonics),
  and `b₄ ∣ b₈` (`H`'s coefficient factors through `W`'s).

## Honest scope (scope-(a), not scope-(b))

This sharpens the **fermion/boson class distinction** (`C1` selection) at
the normal-form level with a *derived* reason:

* fermion tower — the odd **prime** windings `3,5,7` are mutually
  non-divisible (the fermion generation-exclusion result, PR #4456): three
  independent *generations*;
* boson tower — **every** even winding factors through `b₂`
  (`b2_dvd_even` below): no even winding is a "prime generation", the
  tower is uniformly non-generational — exactly the gauge/link
  (`boson_iff_even`) character.

It does **not** derive the specific `W↔4 / Z↔6 / H↔8` mass labels: the
observed `m_W < m_Z < m_H` ordering still maps onto `4 < 6 < 8` only
numerically (the paper's mass ordering is necessary, not sufficient; the
`C_sector` / `C_top` identification stays conjectural, and the continuant
`net` ratios are `O(1)` while the observed boson-mass ratios are not).
What is closed is the *class-level* "why the even tower is
non-generational", not the per-boson identification.

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
-/

namespace QOU.ParticleInteractions

open Polynomial QOU.Archimedean

/-! ### The addition formula for the Morgan–Voyce continuant

`b_{m+n+1} = b_{m+1}·b_{n+1} + b_m·b_n` — the Fibonacci-polynomial
addition law, proved by two-step induction on `m` from the recurrence. -/

/-- **Addition formula** for the Morgan–Voyce continuant `b_n`:
    `b_{m+n+1} = b_{m+1}·b_{n+1} + b_m·b_n`.

    Derived by two-step induction on `m` from
    `morganVoyceB_recurrence`; it is the polynomial Fibonacci addition
    law specialised to `b₁ = 1`, `b₂ = X`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem morganVoyceB_add (m n : ℕ) :
    morganVoyceB (m + n + 1)
      = morganVoyceB (m + 1) * morganVoyceB (n + 1)
        + morganVoyceB m * morganVoyceB n := by
  induction m using Nat.twoStepInduction with
  | zero =>
      simp only [Nat.zero_add, morganVoyceB, one_mul, zero_mul, add_zero]
  | one =>
      rw [show 1 + n + 1 = n + 2 from by omega, morganVoyceB_recurrence]
      simp only [morganVoyceB]
      ring
  | more m ih1 ih2 =>
      rw [show m + 2 + n + 1 = (m + n + 1) + 2 from by omega,
          morganVoyceB_recurrence,
          show (m + n + 1) + 1 = (m + 1) + n + 1 from by omega,
          ih2, ih1,
          show m + 2 + 1 = (m + 1) + 2 from by omega,
          morganVoyceB_recurrence (m + 1),
          show (m + 1) + 1 = m + 2 from by omega,
          morganVoyceB_recurrence m]
      ring

/-! ### Strong divisibility: `a ∣ n ⇒ b_a ∣ b_n` -/

/-- `b_n ∣ b_{n·k}`: the continuant coefficient of every multiple winding
    is divisible by that of the base winding. Proved by induction on `k`
    from the addition formula. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem morganVoyceB_dvd_mul (n k : ℕ) : morganVoyceB n ∣ morganVoyceB (n * k) := by
  induction k with
  | zero => simp [morganVoyceB]
  | succ k ih =>
      rcases Nat.eq_zero_or_pos n with hn | hn
      · subst hn; simp [morganVoyceB]
      · obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
        -- n = n'+1; b_{(n'+1)·(k+1)} = b_{(n'+1)·k + n' + 1}
        have hidx : (n' + 1) * (k + 1) = ((n' + 1) * k) + n' + 1 := by ring
        rw [hidx, morganVoyceB_add]
        exact dvd_add (dvd_mul_left _ _) (ih.mul_right _)

/-- **Strong divisibility of the Morgan–Voyce continuant.**
    `a ∣ n ⇒ b_a ∣ b_n` — the general theorem behind the fermion
    generation-exclusion instances and the boson harmonic tower. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem morganVoyceB_dvd_of_dvd {a n : ℕ} (h : a ∣ n) :
    morganVoyceB a ∣ morganVoyceB n := by
  obtain ⟨k, rfl⟩ := h
  exact morganVoyceB_dvd_mul a k

/-! ### The boson tower: every even winding is a `b₂`-harmonic -/

/-- **Every even winding is a harmonic of the fundamental Hopf continuant
    `b₂`.** `b₂ ∣ b_{2k}` for all `k`: the entire boson (even-winding)
    tower descends from the single fundamental `b₂ = X`. This is the
    boson-side statement dual to the fermion generation-exclusion:
    there is no even "prime generation" — every even winding factors
    through `b₂`, matching the non-generational gauge/link character of
    bosons (`boson_iff_even`). -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem b2_dvd_even (k : ℕ) : morganVoyceB 2 ∣ morganVoyceB (2 * k) :=
  morganVoyceB_dvd_mul 2 k

/-! ### Concrete electroweak carriers, with explicit cofactors -/

/-- `b₂ = X`. -/
theorem morganVoyceB_two : morganVoyceB 2 = X := by
  simp only [morganVoyceB]; ring

/-- `b₄ = X³ + 2X = X·(X² + 2)`. -/
theorem morganVoyceB_four : morganVoyceB 4 = X ^ 3 + 2 * X := by
  simp only [morganVoyceB]; ring

/-- `b₆ = X⁵ + 4X³ + 3X`. -/
theorem morganVoyceB_six : morganVoyceB 6 = X ^ 5 + 4 * X ^ 3 + 3 * X := by
  simp only [morganVoyceB]; ring

/-- `b₈ = X⁷ + 6X⁵ + 10X³ + 4X`. -/
theorem morganVoyceB_eight :
    morganVoyceB 8 = X ^ 7 + 6 * X ^ 5 + 10 * X ^ 3 + 4 * X := by
  simp only [morganVoyceB]; ring

/-- **`W ↔ T(2,4)` is a `b₂`-harmonic**: `b₄ = b₂·(X² + 2)`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem b2_dvd_b4 : morganVoyceB 2 ∣ morganVoyceB 4 :=
  ⟨X ^ 2 + 2, by rw [morganVoyceB_two, morganVoyceB_four]; ring⟩

/-- **`Z ↔ T(2,6)` is a `b₂`-harmonic**: `b₆ = b₂·(X⁴ + 4X² + 3)`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem b2_dvd_b6 : morganVoyceB 2 ∣ morganVoyceB 6 :=
  ⟨X ^ 4 + 4 * X ^ 2 + 3, by rw [morganVoyceB_two, morganVoyceB_six]; ring⟩

/-- **`H ↔ T(2,8)` is a `b₂`-harmonic**: `b₈ = b₂·(X⁶ + 6X⁴ + 10X² + 4)`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem b2_dvd_b8 : morganVoyceB 2 ∣ morganVoyceB 8 :=
  ⟨X ^ 6 + 6 * X ^ 4 + 10 * X ^ 2 + 4,
    by rw [morganVoyceB_two, morganVoyceB_eight]; ring⟩

/-- **`H`'s continuant factors through `W`'s**: `b₄ ∣ b₈` with cofactor
    `X⁴ + 4X² + 2` (`b₈ = b₄·(X⁴ + 4X² + 2)`), the internal harmonic
    `T(2,8) = (T(2,4))²`-type factorisation on the normal-form data. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem b4_dvd_b8 : morganVoyceB 4 ∣ morganVoyceB 8 :=
  ⟨X ^ 4 + 4 * X ^ 2 + 2,
    by rw [morganVoyceB_four, morganVoyceB_eight]; ring⟩

/-- **Boson-tower harmonic summary.** All three electroweak carriers are
    harmonics of the fundamental Hopf continuant `b₂`, and `H`'s
    coefficient additionally factors through `W`'s. Contrast the fermion
    tower, whose prime windings `3,5,7` are mutually non-divisible
    (the fermion generation-exclusion result, PR #4456): the boson
    tower is uniformly non-generational. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md
theorem boson_tower_is_uniformly_harmonic :
    morganVoyceB 2 ∣ morganVoyceB 4 ∧
    morganVoyceB 2 ∣ morganVoyceB 6 ∧
    morganVoyceB 2 ∣ morganVoyceB 8 ∧
    morganVoyceB 4 ∣ morganVoyceB 8 ∧
    (∀ k, morganVoyceB 2 ∣ morganVoyceB (2 * k)) :=
  ⟨b2_dvd_b4, b2_dvd_b6, b2_dvd_b8, b4_dvd_b8, b2_dvd_even⟩

end QOU.ParticleInteractions
