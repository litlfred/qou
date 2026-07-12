import Mathlib.Tactic.Abel

/-!
# QOU.BringsSurface.PentagonTwistAssociator

**Non-associativity as a pentagon (3-cocycle) deformation — the categorical
route to octonion multiplication.**

Two independent deformations of a monoidal category, from its two coherence laws:

| deform | constraint | coherence law | deformation datum | algebraic home |
|---|---|---|---|---|
| commutative → non-commutative | braiding `c` | **hexagon** (Yang–Baxter) | R-matrix | quantum groups (QOU's Hecke) |
| associative → **non-associative** | associator `α` | **pentagon** (Mac Lane) | 3-cocycle / Drinfeld `Φ` | quasi-Hopf algebras (Drinfeld) |

The octonions realise the *second* row: `𝕆 = ℝ_F[(ℤ/2)³]`, the group algebra of
`(ℤ/2)³` (its `8` elements index `e₀,…,e₇`) twisted by a 2-cochain `F` whose
associator is a **nontrivial 3-cocycle** on `(ℤ/2)³` (Albuquerque–Majid 1999). So
"the non-associative doubling `ℍ → 𝕆`" is precisely "turn on a 3-cocycle
associator" — a **pentagon deformation**, exactly as deforming the braiding
(hexagon) turns commutative into non-commutative.

This file formalises the mechanism: for a graded twist `e_a·e_b = F(a,b)·e_{a+b}`,
the associator is `α = dF` (the coboundary of `F`), and it **automatically
satisfies the pentagon** because `d² = 0`. That is why a graded twist keeps Mac
Lane coherence while breaking strict associativity. The specific octonion cochain
`F` (whose `α` is cohomologically nontrivial) is the remaining datum — a finite
`(ℤ/2)³` object, the natural next `decide`-target.

The grading group `G` and phase group `k` are written **additively** (cohomology
is naturally additive; the octonion signs live in `k = ℤ/2`). Generic
(`[AddCommGroup G]`, `[AddCommGroup k]`; §7c), sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.PentagonTwist

variable {G k : Type*} [AddCommGroup G] [AddCommGroup k]

/-- Associator of a 2-cochain twist `F` (`e_a·e_b = F(a,b) · e_{a+b}`, phases
additive): the "defect" `(e_a·e_b)·e_c − e_a·(e_b·e_c)`, i.e. the coboundary
`dF`. -/
def assoc (F : G → G → k) (a b c : G) : k :=
  F a b + F (a + b) c - F b c - F a (b + c)

/-- **Pentagon holds automatically for a twist associator (`d² = 0`).**
For any 2-cochain twist, the associator `α = dF` satisfies the pentagon /
3-cocycle identity. This is the mechanism by which turning on a graded twist
(the octonion `(ℤ/2)³` cochain) breaks strict associativity while preserving Mac
Lane coherence — the categorical form of "deform the pentagon." -/
theorem assoc_pentagon (F : G → G → k) (a b c d : G) :
    assoc F a b c + assoc F a (b + c) d + assoc F b c d
      = assoc F (a + b) c d + assoc F a b (c + d) := by
  simp only [assoc, add_assoc]
  abel

end QOU.BringsSurface.PentagonTwist
