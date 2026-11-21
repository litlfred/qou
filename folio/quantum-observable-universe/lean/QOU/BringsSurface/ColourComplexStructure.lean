import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Ring

/-!
# QOU.BringsSurface.ColourComplexStructure

The algebraic kernel of octonion **colour**, and the ladder `ℂ → ℍ → 𝕆`.

Colour `SU(3) ⊂ G₂ = Aut(𝕆)` acts on the colour triplet `ℂ³`, and that `ℂ³` is
built from a single **complex structure**: fixing an imaginary octonion unit `e`
(`e² = -1`), left-multiplication by `e` is a complex structure `J = L_e`
(`J² = -1`) on the `6`-dimensional space of the other imaginary units, turning
`ℝ⁶` into `ℂ³`. The three colours `𝔯, 𝔤, 𝔟` are the three `ℂ`-directions
(Günaydin–Gürsey; `Im 𝕆 = 1 ⊕ 3 ⊕ 3̄` under `SU(3)`).

This file formalises the two rungs that the "just need complex multiplication,
then rotate across `i, j, k`" intuition captures, and pins where it stops:

* **`complex_mul_from_sqrt_neg_one`** — one complex structure gives ordinary
  *commutative* complex multiplication (the `ℂ` / colour atom). Over any
  `CommRing`; §7c.
* **`rotate_ijk_sq`** — two *anti-commuting* complex structures `i, j` produce a
  third, `k = ij` with `k² = -1` (the quaternions `ℍ`; the "rotate across
  `i, j, k`" step). The proof **uses associativity** — exactly why it lands on
  `ℍ` (associative), not `𝕆`.

**What octonion multiplication needs beyond this.** The step `ℍ → 𝕆` is one more
Cayley–Dickson doubling `(a,b)(c,d) = (ac − d̄b, da + bc̄)`, and it is
**non-associative**: the associator `(x,y,z) := (xy)z − x(yz)` becomes nonzero.
"Rotation" (associative reassociation, as used in `rotate_ijk_sq`) can never
produce a nonzero associator, so it reaches `ℍ` (electroweak `SU(2)`) but not `𝕆`
(colour `SU(3) ⊂ G₂`). The missing ingredient is precisely the non-associative
doubling — not a further rotation. (Mathlib has `Quaternion` but no octonions, so
the `𝕆` rung is stated, not built here.)

-- Ref: [leitner2026] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.ColourComplexStructure

/-- **Colour atom — complex multiplication from an imaginary unit.**
In any commutative ring, an element `j` with `j² = -1` makes `a + b·j` multiply
exactly like complex numbers. This single complex structure is the colour `ℂ`;
the colour triplet `ℂ³` is three such directions, on which `SU(3)` acts. -/
theorem complex_mul_from_sqrt_neg_one {R : Type*} [CommRing R] (j : R)
    (hj : j * j = -1) (a b c d : R) :
    (a + b * j) * (c + d * j) = (a * c - b * d) + (a * d + b * c) * j := by
  linear_combination (b * d) * hj

/-- **Rotation step — anti-commuting complex structures give the quaternion `k`.**
In any (associative) ring, if `i, j` are complex structures (`i² = j² = -1`) that
anti-commute (`j·i = -(i·j)`), then `k := i·j` is again a complex structure:
`k² = -1`. This is the "rotate across `i, j, k`" that builds `ℍ`. The proof uses
associativity — the reason the intuition stops at `ℍ` and not `𝕆`. -/
theorem rotate_ijk_sq {R : Type*} [Ring R] (i j : R)
    (hi : i * i = -1) (hj : j * j = -1) (hij : j * i = -(i * j)) :
    (i * j) * (i * j) = -1 := by
  have reassoc : (i * j) * (i * j) = i * ((j * i) * j) := by noncomm_ring
  rw [reassoc, hij]
  have step : i * (-(i * j) * j) = -(i * i * (j * j)) := by noncomm_ring
  rw [step, hi, hj]; noncomm_ring

end QOU.BringsSurface.ColourComplexStructure
