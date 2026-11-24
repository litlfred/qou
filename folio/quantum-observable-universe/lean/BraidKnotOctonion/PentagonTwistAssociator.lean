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
`(ℤ/2)³` (its `8` elements index `e₀,…,e₇`) twisted by a sign 2-cochain `F` that is
**not a 2-cocycle** — its associator `α = dF` is a nonzero 3-cochain (a genuine
3-cocycle, though a *coboundary*, so cohomologically trivial; see `OctonionCocycle`)
(Albuquerque–Majid 1999). So "the non-associative doubling `ℍ → 𝕆`" is precisely
"turn on a twist `F` with `dF ≠ 0`" — a **pentagon-cochain deformation**, the
associativity-side analogue of deforming the braiding (hexagon) to turn commutative
into non-commutative.

This file formalises the mechanism: for a graded twist `e_a·e_b = F(a,b)·e_{a+b}`,
the associator is `α = dF` (the coboundary of `F`), and it **automatically
satisfies the pentagon** because `d² = 0`. That is why a graded twist keeps Mac
Lane coherence while breaking strict associativity. The specific octonion cochain
`F` — whose associator `α = dF` is cohomologically **trivial** (a coboundary) yet
**nonzero as a cochain** (non-associativity) — is realised concretely in
`OctonionCocycle` (`det3` on `(ℤ/2)³`, `decide`-verified).

The grading group `G` and phase group `k` are written **additively** (cohomology
is naturally additive; the octonion signs live in `k = ℤ/2`). Generic
(`[AddCommGroup G]`, `[AddCommGroup k]`; §7c), sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
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
