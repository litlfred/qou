import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.BringsSurface.OctonionCocycle

**The concrete octonion associator on `(ℤ/2)³` — a genuine pentagon (3-)cocycle.**

Completing the categorical route (`PentagonTwistAssociator`): the octonions are
`𝕆 = ℝ_F[(ℤ/2)³]`, the `(ℤ/2)³` group algebra twisted by a 2-cochain `F` whose
associator is a nontrivial 3-cocycle (Albuquerque–Majid 1999). That associator is
the **`𝔽₂` determinant** (the trilinear alternating form) on `(ℤ/2)³`:
`φ(a,b,c) = det₂[a b c]` — the octonion sign rule "`(e_a e_b)e_c = ± e_a(e_b e_c)`
with `−` exactly on `𝔽₂`-independent triples."

Here `φ` is written additively (values in `ℤ/2`; the octonion sign `(-1)^φ`), so
the pentagon / 3-cocycle condition is the additive
`φ(b,c,d) + φ(a,b+c,d) + φ(a,b,c) = φ(a+b,c,d) + φ(a,b,c+d)`.

* `det3_is_3cocycle` — `φ` **satisfies the pentagon**, verified exhaustively over
  all `8⁴` tuples (`decide`). Trilinearity makes the coboundary telescope to `0`,
  so the octonion associator is pentagon-coherent — a bona fide 3-cocycle.
* `det3_nonzero` — the deformation genuinely fires: on the independent triple
  `e₁, e₂, e₄` the associator is `1 ≠ 0`, i.e. `(e₁e₂)e₄ = −e₁(e₂e₄)`
  (non-associativity).

What remains (honestly open): `φ` is **cohomologically nontrivial** (not a
coboundary) — a rank fact over `𝔽₂^{64}` that the `decide` here does not establish;
`det3_nonzero` only shows `φ ≠ 0` as a cochain. Full `H³((ℤ/2)³; ℤ/2) ∋ [φ] ≠ 0`
is Albuquerque–Majid 1999. Generic `ZMod 2` (§7c), sorry-free.

-- Ref: [albuquerque-majid1999] https://arxiv.org/abs/math/9802116
-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionCocycle

/-- `(ℤ/2)³`, the octonion grading group (`8` elements index `e₀,…,e₇`). -/
abbrev V := ZMod 2 × ZMod 2 × ZMod 2

/-- The `𝔽₂` determinant (trilinear alternating form) of three `(ℤ/2)³` vectors —
the octonion associator `φ(a,b,c)` (additive; the sign is `(-1)^φ`). -/
def det3 (a b c : V) : ZMod 2 :=
  a.1 * (b.2.1 * c.2.2 + b.2.2 * c.2.1)
  + a.2.1 * (b.1 * c.2.2 + b.2.2 * c.1)
  + a.2.2 * (b.1 * c.2.1 + b.2.1 * c.1)

/-- **The octonion associator satisfies the pentagon (3-cocycle) identity.**
Exhaustive over all `8⁴` tuples of `(ℤ/2)³`; the octonion sign rule is a genuine
group 3-cocycle, pentagon-coherent. -/
theorem det3_is_3cocycle :
    ∀ a b c d : V,
      det3 b c d + det3 a (b + c) d + det3 a b c
        = det3 (a + b) c d + det3 a b (c + d) := by
  decide

/-- **The deformation genuinely fires (non-associativity).** On the independent
triple `e₁ = (1,0,0)`, `e₂ = (0,1,0)`, `e₄ = (0,0,1)` the associator is `1 ≠ 0`:
`(e₁e₂)e₄ = − e₁(e₂e₄)`. -/
theorem det3_nonzero : det3 (1, 0, 0) (0, 1, 0) (0, 0, 1) = 1 := by
  decide

end QOU.BringsSurface.OctonionCocycle
