import Mathlib.Data.Real.Basic

/-!
# QOU.Descent.descended_level_zero

Canonical Lean declaration for content block
[`prop:descended-level-zero`](../../../quantum-observable-universe/braids-and-knots/descended-level-zero.md): *QOU.Descent.descended_level_zero*.

The jet-tower decomposition asserts that the descended (holonomy)
contribution to the mass appears **once only**, at jet level `0`; levels
`n ≥ 1` carry only singleton and quadratic transient contributions.  The
derivation: the descended projector stabilises under composition, so
iterated descent collapses to the base-level holonomy regardless of the
jet level at which it is read off.

The vanishing-at-higher-levels claim is irreducibly abstract over the
opaque holonomy contribution function; no Mathlib structure makes it
tautologous.  We therefore **name** the conditional conjecture as a
`Prop` (pattern C of the vacuity-fix playbook): for a contribution
function `desc_contrib : ℕ → ℝ`, `descended_level_zero` is the
proposition that the contribution vanishes at every jet level `≥ 1`.  The
self-assuming `claim_descended_level_zero` carrier field of the old
encoding is removed; inhabiting the proposition is the open conditional
claim, not faked by a projection.
-/

namespace QOU.Descent

/-- **Descended-level-zero collapse** (named conditional conjecture).

For a descended (holonomy) contribution function
`desc_contrib : ℕ → ℝ` indexed by jet level, `descended_level_zero
desc_contrib` is the proposition that the descended contribution appears
only at jet level `0`:

`∀ n, 1 ≤ n → desc_contrib n = 0`.

This names the conditional claim of the jet-tower descent proposition
(pattern C); it is *not* asserted — an inhabitant witnesses the
stabilisation of the descended projector under iterated descent. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/descended-level-zero.ts
def descended_level_zero (desc_contrib : ℕ → ℝ) : Prop :=
    ∀ n : ℕ, 1 ≤ n → desc_contrib n = 0

end QOU.Descent
