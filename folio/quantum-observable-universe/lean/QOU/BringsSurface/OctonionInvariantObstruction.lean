import Mathlib.Algebra.Ring.Action.Basic

/-!
# QOU.BringsSurface.OctonionInvariantObstruction

**Structural obstruction to recovering the octonions `𝕆` from the genus-4
Bring surface `Σ₄` via its `S₅ = Aut(Σ₄)` action on `H¹(Σ₄) ≅ ℝ⁸`.**

The dimensional coincidence `2g = 8 = dim 𝕆` is real, but an `S₅`-equivariant
octonion structure on `H¹(Σ₄)` is **excluded** by a fixed-point invariant:

* Any algebra automorphism of a unital algebra fixes the identity `1`, so a
  group `G` acting on `𝕆` by algebra automorphisms fixes `1 ≠ 0` — a nonzero
  `G`-invariant vector. Hence `𝕆`, as a `G`-module, **always contains the
  trivial representation** (the real line `ℝ·1`).
* But `H¹(Σ₄)` has **no nonzero `S₅`-invariant vector**: the quotient
  `Σ₄ / S₅ ≅ ℙ¹` has genus `0`, so `(H¹(Σ₄))^{S₅} = H¹(ℙ¹) = 0`.

Therefore `H¹(Σ₄) ≇ 𝕆` as an `S₅`-module — no `S₅`-equivariant octonion
product exists on it. (Corroborating count: `S₅` has irreducible dimensions
`{1, 4, 5, 6}` — no `7` — so the `7`-dimensional imaginary octonions
`Im 𝕆` cannot even be an irreducible `S₅`-representation.)

This is a **scope-(b) structural exclusion** (a fixed-point / dimension
invariant, not a failed numerical probe). It does **not** exclude the
octonions via the icosahedral `A₅ → E₈ → integral-octonion` (McKay) route,
nor the colour `SU(3) ⊂ G₂ = Aut(𝕆)` piece carried by the three colour
`S₃` sub-sectors — see the companion audit.

The Lean below is the **abstract kernel**: a `G`-module with no nonzero
invariant admits no nonzero `G`-fixed unit, so it is not a unital algebra
with `G` acting by automorphisms. Generic (no associativity, no `ℝ`; §7c),
sorry-free. The geometric input `(H¹(Σ₄))^{S₅} = 0` and the fact that
automorphisms fix `1` are supplied in the narrative.

-- Ref: [leitner2026] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionObstruction

/-- **Invariant-vector obstruction (kernel).**  A `G`-module `A` with no nonzero
`G`-invariant vector contains no nonzero `G`-fixed element `u`.  Since an algebra
automorphism fixes the identity, a unital algebra with `G` acting by automorphisms
*does* have such a fixed unit (`u = 1 ≠ 0`); so a `G`-module with no invariant
cannot be one.  Fully general — no associativity, so it applies to the octonions. -/
theorem no_fixed_unit {G A : Type*} [Monoid G] [AddCommGroup A] [DistribMulAction G A]
    (hno : ∀ a : A, (∀ g : G, g • a = a) → a = 0)
    (u : A) (hu : u ≠ 0) (hfix : ∀ g : G, g • u = u) : False :=
  hu (hno u hfix)

/-- The fixed unit is automatic in the associative case: a group acting on a nontrivial
semiring by ring automorphisms fixes `1`, a nonzero invariant.  (The octonions are
non-associative, but their identity is fixed by any automorphism for the same reason —
`φ(1)` is an identity, hence equal to the unique identity `1`.) -/
theorem exists_nonzero_invariant {G A : Type*} [Monoid G] [Semiring A] [Nontrivial A]
    [MulSemiringAction G A] : ∃ a : A, a ≠ 0 ∧ ∀ g : G, g • a = a :=
  ⟨1, one_ne_zero, fun g => smul_one g⟩

end QOU.BringsSurface.OctonionObstruction
