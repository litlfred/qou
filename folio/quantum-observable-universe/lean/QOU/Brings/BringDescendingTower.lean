/-
# The descending tower below Bring's surface: Σ₄ → C₂, and it stops

Owner, 2026-10-12 (option 3 of the tower exploration, bean `qou-6082`): study the derived
descending step below Bring as the canonical tower, rather than the ascending homology tower
of `BringCoverTower.lean`, whose modulus `m` is chosen.

Bring's curve `B : Σ x = Σ x² = Σ x³ = 0 ⊂ ℙ⁴`, with `S₅` permuting coordinates. A quotient
`B → B/H` is unramified exactly when no non-identity element of `H` has a fixed point. A
permutation fixes a point of `ℙ⁴` only on one of its eigenspaces, so fixed points can be
counted eigenspace by eigenspace. This file proves the algebra that decides each case.

* **3-cycles act freely** (`threeCycle_eigen1_free`, `threeCycle_eigenω_off_curve`): on the
  `+1` eigenspace `(a,a,a,x,y)` the three equations force `a = x = y = 0`; on the `ω`- and
  `ω²`-eigenspaces `s(1,ω,ω²,0,0)` the cubic is `3s³ ≠ 0`.
* **Every other non-identity class has a fixed point** — explicit points on the curve:
  transpositions (`transposition_fixed_point`, from the roots of `t³+2t²+3t+4`), double
  transpositions (`doubleTransposition_fixed_point`, `(1,−1,i,−i,0)`), 4-cycles
  (`fourCycle_fixed_point`, `(1,i,−1,−i,0)`), 5-cycles (`BringConjugationChirality.lean`).
  An element of order 6 squares to a 3-cycle and cubes to a transposition.
* So a subgroup of `S₅` acts freely iff every non-identity element is a 3-cycle, i.e. it is
  a `C₃` (two 3-cycles not in one `C₃` generate `A₄` or `A₅`, both containing double
  transpositions; checked by enumeration in `bring_descending_tower_probe.py`).
* **Riemann–Hurwitz** (`free_quotient_genus`): `2·4 − 2 = 3(2h − 2)` gives `h = 2`.
* **The tower stops** (`genus_two_unramified_trivial`): an unramified cover of degree `d`
  onto a genus-`h'` curve from genus 2 needs `d (h' − 1) = 1`, so `d = 1`.

**So the forced descending tower is exactly `Σ₄ →(3:1, unramified) C₂`**, unique up to
conjugacy, of length one. This matches the genus-2 curve `𝒞₂` of Braden–Disney-Hogg
(*Bring's curve: old and new*, §4; `library/s40879-023-00706-0`).

§7c: the point computations are over a generic field (with the needed constants
invertible, and `i`, `ω` given as hypotheses); the genus arithmetic is over `ℕ`.

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist; Braden–Disney-Hogg 2024
   (library s40879-023-00706-0) §4; Farkas–Kra, *Riemann Surfaces*, §I.2 (Riemann–Hurwitz).
-/
import Mathlib.Tactic

namespace QOU.Brings.DescendingTower

section Points

variable {K : Type*} [Field K]

/-- **3-cycle, `+1` eigenspace**: the point `(a,a,a,x,y)` lies on Bring's curve only if it is
zero. Needs `30 ≠ 0` (characteristic not 2, 3, 5). -/
theorem threeCycle_eigen1_free (a x y : K) (h30 : (30 : K) ≠ 0)
    (h1 : 3 * a + x + y = 0) (h2 : 3 * a ^ 2 + x ^ 2 + y ^ 2 = 0)
    (h3 : 3 * a ^ 3 + x ^ 3 + y ^ 3 = 0) : a = 0 ∧ x = 0 ∧ y = 0 := by
  have hy : y = -3 * a - x := by linear_combination h1
  subst hy
  have h2ne : (2 : K) ≠ 0 := fun h => h30 (by linear_combination 15 * h)
  have h60 : 2 * (30 * a ^ 3) = 0 := by linear_combination 2 * h3 + 9 * a * h2
  have h30a : 30 * a ^ 3 = 0 := (mul_eq_zero.1 h60).resolve_left h2ne
  have ha : a = 0 := by
    rcases mul_eq_zero.1 h30a with h | h
    · exact absurd h h30
    · exact pow_eq_zero_iff (by norm_num) |>.1 h
  subst ha
  have h2' : 2 * x ^ 2 = 0 := by linear_combination h2
  have hx : x = 0 := by
    rcases mul_eq_zero.1 h2' with h | h
    · exact absurd h h2ne
    · exact pow_eq_zero_iff (by norm_num) |>.1 h
  subst hx
  exact ⟨rfl, rfl, by ring⟩

/-- **3-cycle, `ω`- and `ω²`-eigenspaces**: `s(1, ω, ω²)` has cubic sum `3s³`, nonzero. -/
theorem threeCycle_eigenω_off_curve (s ω : K) (hω : ω ^ 2 + ω + 1 = 0) (hs : s ≠ 0)
    (h3 : (3 : K) ≠ 0) : s ^ 3 + (s * ω) ^ 3 + (s * ω ^ 2) ^ 3 ≠ 0 := by
  have hω3 : ω ^ 3 = 1 := by linear_combination (ω - 1) * hω
  have : s ^ 3 + (s * ω) ^ 3 + (s * ω ^ 2) ^ 3 = 3 * s ^ 3 := by
    have h6 : ω ^ 6 = 1 := by rw [show ω ^ 6 = (ω ^ 3) ^ 2 by ring, hω3, one_pow]
    linear_combination s ^ 3 * hω3 + s ^ 3 * h6
  rw [this]
  exact mul_ne_zero h3 (pow_ne_zero 3 hs)

/-- **Transposition `(45)`**: with `r₁, r₂, r₃` the roots of `t³ + 2t² + 3t + 4`,
`(r₁, r₂, r₃, 1, 1)` lies on Bring's curve and is fixed by `(45)`. -/
theorem transposition_fixed_point (r₁ r₂ r₃ : K) (e1 : r₁ + r₂ + r₃ = -2)
    (e2 : r₁ * r₂ + r₁ * r₃ + r₂ * r₃ = 3) (e3 : r₁ * r₂ * r₃ = -4) :
    r₁ + r₂ + r₃ + 1 + 1 = 0 ∧ r₁ ^ 2 + r₂ ^ 2 + r₃ ^ 2 + 1 + 1 = 0 ∧
      r₁ ^ 3 + r₂ ^ 3 + r₃ ^ 3 + 1 + 1 = 0 := by
  refine ⟨by linear_combination e1, ?_, ?_⟩
  · linear_combination (r₁ + r₂ + r₃ - 2) * e1 - 2 * e2
  · linear_combination ((r₁ + r₂ + r₃) ^ 2 - 2 * (r₁ + r₂ + r₃) - 5) * e1
      - 3 * (r₁ + r₂ + r₃) * e2 + 3 * e3

/-- **Double transposition `(12)(34)`**: `(1, −1, i, −i, 0)` is a fixed point on the curve. -/
theorem doubleTransposition_fixed_point (i : K) (hi : i ^ 2 = -1) :
    (1 : K) + -1 + i + -i + 0 = 0 ∧ (1 : K) ^ 2 + (-1) ^ 2 + i ^ 2 + (-i) ^ 2 + 0 ^ 2 = 0 ∧
      (1 : K) ^ 3 + (-1) ^ 3 + i ^ 3 + (-i) ^ 3 + 0 ^ 3 = 0 := by
  refine ⟨by ring, by linear_combination 2 * hi, by ring⟩

/-- **4-cycle `(1234)`**: `(1, i, −1, −i, 0)` is a fixed point on the curve. -/
theorem fourCycle_fixed_point (i : K) (hi : i ^ 2 = -1) :
    (1 : K) + i + -1 + -i + 0 = 0 ∧ (1 : K) ^ 2 + i ^ 2 + (-1) ^ 2 + (-i) ^ 2 + 0 ^ 2 = 0 ∧
      (1 : K) ^ 3 + i ^ 3 + (-1) ^ 3 + (-i) ^ 3 + 0 ^ 3 = 0 := by
  refine ⟨by ring, by linear_combination 2 * hi, by ring⟩

end Points

section Genus

/-- **Riemann–Hurwitz for a free `C₃` quotient of a genus-4 curve**: `2·4 − 2 = 3(2h − 2)`. -/
theorem free_quotient_genus (h : ℕ) (hRH : 2 * 4 = 3 * (2 * h) - 4) : h = 2 := by
  omega

/-- **The descending tower stops at genus 2**: an unramified degree-`d` cover from genus 2
onto genus `h'` satisfies `2·2 − 2 = d (2h' − 2)`, forcing `d = 1`. Stated as
`1 = d * (h' - 1)` with `h' ≥ 2` (a genus-0 or genus-1 target is excluded by the sign/value of
the Euler characteristic). -/
theorem genus_two_unramified_trivial (d h' : ℕ) (hRH : 1 = d * (h' - 1)) : d = 1 :=
  Nat.eq_one_of_mul_eq_one_right hRH.symm

end Genus

end QOU.Brings.DescendingTower
