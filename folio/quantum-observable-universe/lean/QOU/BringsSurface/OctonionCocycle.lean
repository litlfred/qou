import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.BringsSurface.OctonionCocycle

**The concrete octonion associator on `(ℤ/2)³` — a genuine pentagon (3-)cocycle.**

Completing the categorical route (`PentagonTwistAssociator`): the octonions are
`𝕆 = ℝ_F[(ℤ/2)³]`, the `(ℤ/2)³` group algebra twisted by a sign 2-cochain `F`. Its
multiplication associator is the **`𝔽₂` determinant** (trilinear alternating form)
`φ(a,b,c) = det₂[a b c]` — the sign rule "`(e_a e_b)e_c = (-1)^φ · e_a(e_b e_c)`,
i.e. `−` exactly on `𝔽₂`-independent triples."

**Verified against the real octonions.** Building `𝕆` by Cayley–Dickson
(`ℝ → ℂ → ℍ → 𝕆`) and reading off the basis signs, the index law is XOR (the group
is `(ℤ/2)³`) and the associativity defect equals `det₂` **exactly as a cochain**;
`168` of the `512` triples fail to associate.

Written additively (values in `ℤ/2`; sign `(-1)^φ`), the pentagon / 3-cocycle
condition is `φ(b,c,d) + φ(a,b+c,d) + φ(a,b,c) = φ(a+b,c,d) + φ(a,b,c+d)`.

* `det3_is_3cocycle` — `φ` **satisfies the pentagon**, verified exhaustively over
  all `8⁴` tuples (`decide`). Trilinearity telescopes the coboundary to `0`, so the
  octonion associator is pentagon-coherent — a bona fide 3-cocycle.
* `det3_nonzero` — the deformation genuinely fires: on the independent triple
  `e₁, e₂, e₄` the associator is `1 ≠ 0`, i.e. `(e₁e₂)e₄ = −e₁(e₂e₄)`
  (non-associativity).

**Cohomology (correcting an earlier over-claim).** `φ` is a coboundary `φ = dF`,
so `[φ] = 0` in `H³((ℤ/2)³; ℤ/2)` — the octonion multiplication associator is
cohomologically **trivial** (verified: `φ` equals the coboundary of the
Cayley–Dickson sign cochain, exactly). There is therefore **no H³-nontriviality to
prove**: non-associativity is `φ ≠ 0` *as a cochain* (`F` is not a 2-cocycle), not
an `H³` phenomenon. The gauge `e_a ↦ λ_a e_a` changes `F` by `dλ` and leaves
`φ = dF` fixed, so `𝕆` is non-associative under *every* basis rescaling even though
`[φ] = 0`. (The nontrivial `H³` 3-cocycle of Albuquerque–Majid 1999 is the
*category* associator making `𝕆` associative in `Vect_{(ℤ/2)³}^ω`, a distinct
object from this multiplication associator; not claimed here.) Generic `ZMod 2`
(§7c), sorry-free.

-- Ref: [albuquerque-majid1999] https://arxiv.org/abs/math/9802116
-- Ref: [leitner2026] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
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

/-- Cyclic shift of the three `(ℤ/2)³` coordinates — a `GL(3, 𝔽₂)` element (a
3-cycle of the coordinates, an even permutation). -/
def cyc (x : V) : V := (x.2.1, x.2.2, x.1)

/-- **Fano / `PSL(2,7)` symmetry of the octonion associator (witness).** `det3` is
invariant under the coordinate 3-cycle `cyc ∈ GL(3, 𝔽₂)`. More generally
`det3 (g·a) (g·b) (g·c) = det(g) · det3 a b c = det3 a b c` for **every**
`g ∈ GL(3, 𝔽₂) ≅ PSL(2,7)` (order 168 — the Fano-plane / Klein-quartic symmetry),
since `det g = 1` over `𝔽₂`. This is the concrete tie between the `(ℤ/2)³`
octonion sign structure and the genus-3 (Klein-quartic, `PSL(2,7) =` Fano) home of
the octonion product. Here the `cyc` generator is machine-checked; the full
`GL(3,𝔽₂)`-invariance is determinant multiplicativity. -/
theorem det3_cyclic_invariant :
    ∀ a b c : V, det3 (cyc a) (cyc b) (cyc c) = det3 a b c := by
  decide

end QOU.BringsSurface.OctonionCocycle
