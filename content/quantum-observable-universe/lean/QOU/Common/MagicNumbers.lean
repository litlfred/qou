/-!
# QOU.Common.MagicNumbers — shared canonical declaration

Single source of truth for the seven observed nuclear magic
numbers `{2, 8, 20, 28, 50, 82, 126}`.

Used by the four magic-number conjecture sibling Lean files to
avoid the cross-file constant-duplication flagged in the
Gemini review of PR #501:

  - content/.../braids-and-knots/categorical-neutrality-saturated-shells.lean
  - content/.../lifting-and-descent/homological-shell-condensation.lean
  - content/.../observations/diagrammatic-double-magic-lr-fusion.lean
  - content/.../algebraic-substrate/magic-numbers-bring.lean

Each of those files now imports this module and references
`QOU.Common.magicSet` rather than redefining its own
`magicSet : Finset ℕ`.

Ref: PR #501 review — gemini-code-assist[bot] flagged the
cross-file duplication on commit 0e86a151 / 57eae509.
-/

import Mathlib.Data.Finset.Basic

namespace QOU.Common

/-- The seven observed nuclear magic numbers
    `{2, 8, 20, 28, 50, 82, 126}`. -/
def magicSet : Finset ℕ := {2, 8, 20, 28, 50, 82, 126}

/-- Membership-as-Prop wrapper, useful as a class precondition. -/
def Saturated (n : ℕ) : Prop := n ∈ magicSet

end QOU.Common
