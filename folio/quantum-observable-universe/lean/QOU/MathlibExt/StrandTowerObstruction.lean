/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.MarkovUnusedGenerator

/-!
# C-5a, reading A: the strand-tower R-matrix cannot give `κ_n = 0 ↔ n ∣ 6`

Relation C-5 (`vertex-algebra-relations`) reads

  `κ_n = tr_M(Ř_(n+1) − L_{-1} Ř_(n))`,

and C-5a asks whether `κ_n = 0 ↔ n ∣ 6`. The corpus fixes the inter-level map:
`vertex-algebra-jet-relations` sets `ℓ_n(σ_i^(n)) = σ_i^(n+1)`, the standard
strand inclusion `H_n ⊆ H_{n+1}`. It does **not** define `Ř_(n)`.

This file fixes one reading of `Ř_(n)`, the strand tower, and proves that it
fails C-5a for a structural reason. The definition was fixed before anything
was computed (owner decision, 2026-11-15; note
`qou-leftovers/r2-candidate-definitions.md`, candidate A).

**Definition.** `Ř_0 = 1` and `Ř_(n+1) = ℓ_n(Ř_(n)) · σ_n`, so
`Ř_(n) = σ_0 σ_1 ⋯ σ_(n-1)`.

**Result.** For any Markov-trace tower with parameter `z`:

* `κ_n = (z − 1) · z^n · tr 1` (`kappa_eq`).
* Over a domain, the zero set of `κ` is all of `ℕ` or empty
  (`kappa_zero_set_dichotomy`), so it never depends on `n`.
* Hence `κ_n = 0 ↔ n ∣ 6` (`n ≥ 1`) is false for every Markov parameter
  (`not_kappa_eq_zero_iff_dvd_six`). Levels 1 and 4 cannot both be matched.

**Scope (b), for this definition only.** The invariant is the Markov property.
Other definitions of `Ř_(n)` are not excluded. In particular a
Hecke-dependent, non-monomial `Ř_(n)` is untouched by this argument.

## Base ring
Generic `[CommRing R]`, generic `R`-algebra. `z` is abstract, so the result
holds under convention C and convention D alike.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] climax-volume-mass, relation C-5a; vertex-algebra-jet-relations J-intro
-/

namespace QOU.MathlibExt.StrandTowerObstruction

open QOU.MathlibExt.MarkovUnusedGenerator

variable {R : Type*} [CommRing R]
variable {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTower R A)

/-- The strand-tower R-matrix: `Ř_0 = 1`, `Ř_(n+1) = Ř_(n) · σ_n`. -/
def rCheck : ℕ → A
  | 0 => 1
  | n + 1 => rCheck n * T.σ n

theorem rCheck_mem (n : ℕ) : rCheck T n ∈ T.H n := by
  induction n with
  | zero => exact (T.H 0).one_mem
  | succ n ih =>
    exact (T.H (n + 1)).mul_mem (T.H_mono (Nat.le_succ n) ih) (T.σ_mem n)

/-- The level-`n` obstruction `κ_n = tr(Ř_(n+1) − ℓ_n Ř_(n))`, with `ℓ_n` the
strand inclusion (the identity on the ambient algebra). -/
def kappa (n : ℕ) : R := T.tr (rCheck T (n + 1) - rCheck T n)

theorem tr_rCheck (n : ℕ) : T.tr (rCheck T n) = T.z ^ n * T.tr 1 := by
  induction n with
  | zero => simp [rCheck]
  | succ n ih =>
    show T.tr (rCheck T n * T.σ n) = _
    rw [T.markov n _ (rCheck_mem T n), ih]
    ring

/-- `κ_n = (z − 1) · z^n · tr 1`. -/
theorem kappa_eq (n : ℕ) : kappa T n = (T.z - 1) * T.z ^ n * T.tr 1 := by
  unfold kappa
  rw [map_sub, tr_rCheck, tr_rCheck]
  ring

/-- Over a domain, on the levels `n ≥ 1` the zero set of `κ` is all of them or
none of them. (Level `0` can differ only when `z = 0`.) -/
theorem kappa_zero_set_dichotomy [IsDomain R] :
    (∀ n, 1 ≤ n → kappa T n = 0) ∨ (∀ n, 1 ≤ n → kappa T n ≠ 0) := by
  have key : ∀ n, 1 ≤ n →
      (kappa T n = 0 ↔ (T.z - 1) * T.tr 1 * T.z = 0) := by
    intro n hn
    obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    rw [kappa_eq]
    have e : (T.z - 1) * T.z ^ (m + 1) * T.tr 1
        = ((T.z - 1) * T.tr 1 * T.z) * T.z ^ m := by ring
    rw [e]
    constructor
    · intro h
      rcases mul_eq_zero.mp h with h | h
      · exact h
      · have : T.z = 0 := pow_eq_zero_iff'.mp h |>.1
        rw [this, mul_zero]
    · intro h; rw [h, zero_mul]
  by_cases h : (T.z - 1) * T.tr 1 * T.z = 0
  · exact Or.inl fun n hn => (key n hn).2 h
  · exact Or.inr fun n hn hk => h ((key n hn).1 hk)

/-- **C-5a fails for the strand tower.** For every Markov-trace tower over a
domain, whatever the Markov parameter, it is false that `κ_n = 0 ↔ n ∣ 6`
for all `n ≥ 1`: levels `1` and `4` would need opposite answers. -/
theorem not_kappa_eq_zero_iff_dvd_six [IsDomain R] :
    ¬ (∀ n, 1 ≤ n → (kappa T n = 0 ↔ n ∣ 6)) := by
  intro hC
  have h1 : kappa T 1 = 0 := (hC 1 le_rfl).2 (by norm_num)
  have h4 : kappa T 4 ≠ 0 := fun h => by
    have := (hC 4 (by norm_num)).1 h; norm_num at this
  rcases kappa_zero_set_dichotomy T with hall | hnone
  · exact h4 (hall 4 (by norm_num))
  · exact hnone 1 le_rfl h1

end QOU.MathlibExt.StrandTowerObstruction
