import Mathlib.Tactic.NormNum
/-!
# Frobenius traces of 50a1 and the Hasse inequality at `7 ≤ p ≤ 41` (algebraic core)

**Human-readable statement** (owner ruling 2026-11-28; prose in
`q-geometric-langlands/weil-bound-intro.md`): for the elliptic curve
`E : y² + xy + y = x³ − x − 2` (Cremona 50a1), with `#E(𝔽_p)` its projective
point count and `a_p = p + 1 − #E(𝔽_p)`, the values of `a_p` at the primes
`7 ≤ p ≤ 41` are those in `bringFrobeniusTraces`, and at each of them
`a_p² < 4p`.

Since `J(ℬ) ~ E⁴` for Bring's curve `ℬ`, the reversed Frobenius polynomial of
`ℬ` at a good prime `p` is `(X² − a_p X + p)⁴` (Weil rationality and the
isogeny are cited; `computations/bring_local_zeta_point_counts.py` checks
`|ℬ(𝔽_p)| = p + 1 − 4a_p` exactly). So `a_p² ≤ 4p` **is** the finite-field
Riemann hypothesis for `ℬ` at `p`, stated with integers only.

This module is the algebraic side of the strangler split: integers and finite
counts, no reals, no limits. The translation to `|αᵢ| = p^{1/2}`,
`Re ρ = 1/2` and `L(E, s)` lives in
`QOU/Transcendental/BringsSurface/BringHasseLocalZeta.lean` and
`QOU/Transcendental/BringsSurface/AdelicPersistenceL.lean`.
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- Projective point count of `E : y² + xy + y = x³ − x − 2` over `𝔽_p`:
the affine solutions in `{0, …, p−1}²` plus the point at infinity. -/
def ec50a1Count (p : ℕ) : ℕ :=
  1 + ((List.range p).product (List.range p)).countP (fun xy =>
    ((xy.2 : ℤ) * xy.2 + (xy.1 : ℤ) * xy.2 + xy.2
      - (xy.1 : ℤ) ^ 3 + xy.1 + 2) % (p : ℤ) == 0)

/-- `a_p = p + 1 − #E(𝔽_p)`. -/
def ec50a1Trace (p : ℕ) : ℤ := (p : ℤ) + 1 - ec50a1Count p

/-- `(p, a_p)` for 50a1 at the primes `7 ≤ p ≤ 41`. -/
def bringFrobeniusTraces : List (ℤ × ℤ) :=
  [(7, 2), (11, -3), (13, -4), (17, -3), (19, 5), (23, 6), (29, 0), (31, 2),
   (37, 2), (41, -3)]

/-- The point count reproduces the table. -/
theorem ec50a1Trace_table :
    ∀ x ∈ bringFrobeniusTraces, ec50a1Trace x.1.toNat = x.2 := by
  decide +kernel

/-- Hasse's inequality, strictly, at every listed prime: the finite-field
Riemann hypothesis for Bring's curve at `7 ≤ p ≤ 41`, given the cited
identification of its local zeta. -/
theorem bring_hasse_table :
    ∀ x ∈ bringFrobeniusTraces, 0 < x.1 ∧ x.2 ^ 2 < 4 * x.1 := by
  decide

end QOU.AlgebraicSubstrate
