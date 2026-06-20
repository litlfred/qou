-- Ref: [conway1976] Conway, *On Numbers and Games*, Academic Press.
-- Ref: [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
--      Numbers*, Cambridge University Press.
-- Ref: [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of finite
--      groups with BN-pairs of classical type*, PhD Thesis, UBC.
--
-- Sibling stub for `prop:hoefsmit-is-surreal-construction`.
--
-- The compiled formalisation lives in:
--   QOU/AppendixSurreals/HoefsmitBridge.lean
--
-- See `QOU.AppendixSurreals.TwoRowTableau`,
--     `QOU.AppendixSurreals.hoefsmitDyadic`                  — restricted to n ≤ 2
--     `QOU.AppendixSurreals.hoefsmit_bridge_zero`            — proved
--     `QOU.AppendixSurreals.hoefsmit_bridge_one`             — proved
--     `QOU.AppendixSurreals.hoefsmit_bridge_two`             — proved
--     `QOU.AppendixSurreals.hoefsmit_is_surreal_construction`
--       (consolidated `n ≤ 2` injectivity, named to match the
--        LaTeX label of this content block)               — proved
--
-- The bridge is proved in Lean for tableau sizes n ≤ 2 (the first
-- non-trivial cases).  `hoefsmitDyadic` is restricted at the type
-- level to `n ≤ 2`: the row-only `TwoRowTableau` data is sufficient
-- to distinguish standard tableaux exactly in that range.  The
-- general-`n` Hoefsmit-to-dyadic bijection requires an entry-aware
-- tableau type plus a YJM-tree formalisation in Mathlib, neither of
-- which currently exists; we do not assert it as an axiom.

namespace QOU.AppendixSurreals

/-- **PROPOSITION.** Hoefsmit seminormal form is Conway -/
def hoefsmit_is_surreal_construction : True := by
  -- Ref: [manuscript] prop:hoefsmit-is-surreal-construction
  trivial

end QOU.AppendixSurreals
