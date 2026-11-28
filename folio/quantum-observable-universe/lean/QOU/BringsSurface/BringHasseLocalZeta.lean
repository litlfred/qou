import QOU.BringsSurface.WeilZeta
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Local zeta data of the shape `(X² − aX + p)⁴`, and Bring's curve at `7 ≤ p ≤ 41`

**Human-readable statement** (the semantic equivalent required by the owner
ruling of 2026-11-28; prose in `q-geometric-langlands/weil-bound-intro.md`):

> Let `p > 0` and `a` be integers with `a² ≤ 4p`. Let `α = (a + i√(4p − a²))/2`,
> so `α` and its conjugate `ᾱ` are the two roots of `X² − aX + p`. The local
> zeta datum with `q = p` and eigenvalues `α, ᾱ, α, ᾱ, α, ᾱ, α, ᾱ` has
> characteristic polynomial `(X² − aX + p)⁴` and satisfies both Weil inputs of
> `IsWeilZeta`: the functional equation (`α ↦ p/α` permutes the eigenvalues)
> and Castelnuovo–Severi (`|α|² ≤ p`). Hence `|αᵢ| = p^{1/2}` for all eight.

For Bring's curve `ℬ`, `J(ℬ) ~ E⁴` with `E` the elliptic curve 50a1, and the
point counts in `computations/bring_local_zeta_point_counts.py` give
`|ℬ(𝔽_p)| = p + 1 − 4a_p` with `a_p = p + 1 − |E(𝔽_p)|` for `7 ≤ p ≤ 41`. So
the reversed characteristic polynomial of Frobenius on `H¹(ℬ/𝔽_p)` is
`(X² − a_p X + p)⁴`.

**What Lean checks and what it does not.** Lean checks the algebra above and
the integer inequalities `a_p² ≤ 4p` for the listed primes (`bring_hasse_table`).
Lean does **not** check that these data are the zeta function of Bring's curve:
that step is Weil's rationality theorem plus the isogeny `J(ℬ) ~ E⁴` plus the
point counts, none of which is in Mathlib. The instances below are therefore
statements about the quadratic `X² − aX + p`, applied at the `a_p` that the
cited mathematics and the exact count supply.

Unlike `weilZetaExample` (supersingular, all eigenvalues equal), these are
Weil data with two distinct non-real eigenvalues, so `IsWeilZeta` is inhabited
by the shape the Bring arc actually needs.
-/

set_option autoImplicit false

open Polynomial Complex

namespace QOU.AlgebraicSubstrate

/-- The Frobenius root `α = (a + i√(4p − a²))/2` of `X² − aX + p`. -/
noncomputable def hasseRoot (p a : ℤ) : ℂ :=
  ⟨(a : ℝ) / 2, Real.sqrt (4 * (p : ℝ) - (a : ℝ) ^ 2) / 2⟩

theorem hasseRoot_re (p a : ℤ) : (hasseRoot p a).re = (a : ℝ) / 2 := rfl

theorem hasseRoot_im (p a : ℤ) :
    (hasseRoot p a).im = Real.sqrt (4 * (p : ℝ) - (a : ℝ) ^ 2) / 2 := rfl

/-- `|α|² = p` when `a² ≤ 4p`. -/
theorem hasseRoot_normSq (p a : ℤ) (h : a ^ 2 ≤ 4 * p) :
    Complex.normSq (hasseRoot p a) = p := by
  have h' : (0 : ℝ) ≤ 4 * (p : ℝ) - (a : ℝ) ^ 2 := by
    have : ((a ^ 2 : ℤ) : ℝ) ≤ ((4 * p : ℤ) : ℝ) := by exact_mod_cast h
    push_cast at this; linarith
  rw [Complex.normSq_apply, hasseRoot_re, hasseRoot_im]
  have hs := Real.mul_self_sqrt h'
  nlinarith [hs]

/-- `α · ᾱ = p`. -/
theorem hasseRoot_mul_conj (p a : ℤ) (h : a ^ 2 ≤ 4 * p) :
    hasseRoot p a * (starRingEnd ℂ) (hasseRoot p a) = (p : ℂ) := by
  rw [Complex.mul_conj, hasseRoot_normSq p a h]
  norm_cast

/-- `α + ᾱ = a`. -/
theorem hasseRoot_add_conj (p a : ℤ) :
    hasseRoot p a + (starRingEnd ℂ) (hasseRoot p a) = (a : ℂ) := by
  apply Complex.ext <;> simp [hasseRoot_re, hasseRoot_im]

theorem hasseRoot_ne_zero (p a : ℤ) (hp : 0 < p) (h : a ^ 2 ≤ 4 * p) :
    hasseRoot p a ≠ 0 := by
  intro h0
  have := hasseRoot_normSq p a h
  rw [h0, map_zero] at this
  have : (0 : ℝ) < p := by exact_mod_cast hp
  linarith

/-- The eight eigenvalues `α, ᾱ, α, ᾱ, α, ᾱ, α, ᾱ`. -/
noncomputable def hasseEig (p a : ℤ) : Fin 8 → ℂ :=
  ![hasseRoot p a, (starRingEnd ℂ) (hasseRoot p a),
    hasseRoot p a, (starRingEnd ℂ) (hasseRoot p a),
    hasseRoot p a, (starRingEnd ℂ) (hasseRoot p a),
    hasseRoot p a, (starRingEnd ℂ) (hasseRoot p a)]

/-- The local zeta datum with `q = p` and eigenvalues `hasseEig p a`. -/
noncomputable def hasseLocalZeta (p a : ℤ) (hp : 0 < p) (h : a ^ 2 ≤ 4 * p) :
    LocalQZetaFunction where
  q := p
  q_pos := by exact_mod_cast hp
  eigenvalues := hasseEig p a
  eigenvalues_ne_zero := by
    have h1 := hasseRoot_ne_zero p a hp h
    have h2 : (starRingEnd ℂ) (hasseRoot p a) ≠ 0 := by
      simpa using h1
    intro i; fin_cases i <;> simp [hasseEig, h1, h2]
  charPoly := ∏ i : Fin 8, (Polynomial.X - Polynomial.C (hasseEig p a i))
  charPoly_degree := by
    rw [Polynomial.natDegree_prod _ _ (fun i _ => Polynomial.X_sub_C_ne_zero _)]
    simp [bringsGenus]
  charPoly_roots := rfl

/-- The characteristic polynomial is `(X² − aX + p)⁴`, the reversed form of
`(1 − aT + pT²)⁴`. -/
theorem hasseLocalZeta_charPoly (p a : ℤ) (hp : 0 < p) (h : a ^ 2 ≤ 4 * p) :
    (hasseLocalZeta p a hp h).charPoly
      = (Polynomial.X ^ 2 - Polynomial.C (a : ℂ) * Polynomial.X
          + Polynomial.C (p : ℂ)) ^ 4 := by
  have hq : (Polynomial.X - Polynomial.C (hasseRoot p a))
      * (Polynomial.X - Polynomial.C ((starRingEnd ℂ) (hasseRoot p a)))
      = Polynomial.X ^ 2 - Polynomial.C (a : ℂ) * Polynomial.X
          + Polynomial.C (p : ℂ) := by
    rw [← hasseRoot_add_conj p a, ← hasseRoot_mul_conj p a h]
    simp only [map_add, map_mul]
    ring
  show ∏ i : Fin 8, (Polynomial.X - Polynomial.C (hasseEig p a i)) = _
  rw [Fin.prod_univ_eight, ← hq]
  simp [hasseEig]
  ring

/-- The pairing permutation `0↔1, 2↔3, 4↔5, 6↔7`. -/
def hassePairing : Equiv.Perm (Fin 8) :=
  Equiv.swap 0 1 * Equiv.swap 2 3 * Equiv.swap 4 5 * Equiv.swap 6 7

/-- Both Weil inputs hold for `hasseLocalZeta p a`. -/
instance hasseLocalZeta_isWeilZeta (p a : ℤ) (hp : 0 < p) (h : a ^ 2 ≤ 4 * p) :
    IsWeilZeta (hasseLocalZeta p a hp h) where
  functional_equation := by
    refine ⟨hassePairing, ?_⟩
    have h1 := hasseRoot_ne_zero p a hp h
    have h2 : (starRingEnd ℂ) (hasseRoot p a) ≠ 0 := by simpa using h1
    have hm := hasseRoot_mul_conj p a h
    -- `ᾱ = p/α` and `α = p/ᾱ`
    have e1 : (starRingEnd ℂ) (hasseRoot p a) = (p : ℂ) / hasseRoot p a := by
      rw [eq_div_iff h1, mul_comm]; exact hm
    have e2 : hasseRoot p a = (p : ℂ) / (starRingEnd ℂ) (hasseRoot p a) := by
      rw [eq_div_iff h2]; exact hm
    intro i
    show hasseEig p a (hassePairing i) = ((p : ℝ) : ℂ) / hasseEig p a i
    have hpc : (((p : ℝ)) : ℂ) = (p : ℂ) := by push_cast; rfl
    rw [hpc]
    fin_cases i
    · show hasseEig p a (hassePairing 0) = (p : ℂ) / hasseEig p a 0
      rw [show hassePairing 0 = 1 by decide]; simpa [hasseEig] using e1
    · show hasseEig p a (hassePairing 1) = (p : ℂ) / hasseEig p a 1
      rw [show hassePairing 1 = 0 by decide]; simpa [hasseEig] using e2
    · show hasseEig p a (hassePairing 2) = (p : ℂ) / hasseEig p a 2
      rw [show hassePairing 2 = 3 by decide]; simpa [hasseEig] using e1
    · show hasseEig p a (hassePairing 3) = (p : ℂ) / hasseEig p a 3
      rw [show hassePairing 3 = 2 by decide]; simpa [hasseEig] using e2
    · show hasseEig p a (hassePairing 4) = (p : ℂ) / hasseEig p a 4
      rw [show hassePairing 4 = 5 by decide]; simpa [hasseEig] using e1
    · show hasseEig p a (hassePairing 5) = (p : ℂ) / hasseEig p a 5
      rw [show hassePairing 5 = 4 by decide]; simpa [hasseEig] using e2
    · show hasseEig p a (hassePairing 6) = (p : ℂ) / hasseEig p a 6
      rw [show hassePairing 6 = 7 by decide]; simpa [hasseEig] using e1
    · show hasseEig p a (hassePairing 7) = (p : ℂ) / hasseEig p a 7
      rw [show hassePairing 7 = 6 by decide]; simpa [hasseEig] using e2
  castelnuovo_severi := by
    intro i
    show ‖hasseEig p a i‖ ^ 2 ≤ (p : ℝ)
    have hn : ‖hasseRoot p a‖ ^ 2 = (p : ℝ) := by
      rw [Complex.sq_norm, hasseRoot_normSq p a h]
    fin_cases i <;> simp [hasseEig, hn]

/-- **Hasse–Weil for `hasseLocalZeta`:** every eigenvalue has `|αᵢ| = p^{1/2}`.
This is `hasse_weil_bound` applied to the instance above. -/
theorem hasseLocalZeta_norm (p a : ℤ) (hp : 0 < p) (h : a ^ 2 ≤ 4 * p) (i : Fin 8) :
    ‖(hasseLocalZeta p a hp h).eigenvalues i‖ = (p : ℝ) ^ (1 / 2 : ℝ) :=
  hasse_weil_bound (hasseLocalZeta p a hp h) i

/-- `(p, a_p)` for the elliptic curve 50a1 at the primes `7 ≤ p ≤ 41`,
from the exact counts in `computations/bring_local_zeta_point_counts.py`.
These are the data `(p, a)` at which Bring's local zeta is
`hasseLocalZeta p a` (see the module docstring for what is cited). -/
def bringFrobeniusTraces : List (ℤ × ℤ) :=
  [(7, 2), (11, -3), (13, -4), (17, -3), (19, 5), (23, 6), (29, 0), (31, 2),
   (37, 2), (41, -3)]

/-- Hasse's inequality `a_p² ≤ 4p` holds at every listed prime: the
finite-field Riemann hypothesis for Bring's curve at `7 ≤ p ≤ 41`, given the
cited identification of its local zeta. -/
theorem bring_hasse_table :
    ∀ x ∈ bringFrobeniusTraces, 0 < x.1 ∧ x.2 ^ 2 ≤ 4 * x.1 := by
  decide

/-- Bring's local zeta at `p = 7`: `(X² − 2X + 7)⁴`, eigenvalues `1 ± i√6`. -/
noncomputable abbrev bringLocalZeta7 : LocalQZetaFunction :=
  hasseLocalZeta 7 2 (by norm_num) (by norm_num)

example (i : Fin 8) : ‖bringLocalZeta7.eigenvalues i‖ = (7 : ℝ) ^ (1 / 2 : ℝ) := by
  have := hasseLocalZeta_norm 7 2 (by norm_num) (by norm_num) i
  simpa using this

end QOU.AlgebraicSubstrate
