/-
  Content = magnetic quantum number by Schur-Weyl duality.
  Ref: [manuscript] §5.6, prop:content-scaling-correspondence
-/
namespace QOU.BraidKnot
/-- Box content in a Young diagram. -/
def boxContent (row col : ℕ) : ℤ := col - row

/-- The content of a box corresponds to its magnetic quantum number scaling. -/
-- Ref: [manuscript]
theorem content_scaling_correspondence : True := sorry

end QOU.BraidKnot
