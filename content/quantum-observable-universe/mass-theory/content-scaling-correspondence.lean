/-
  Content = magnetic quantum number by Schur-Weyl duality.
  Ref: [manuscript] §5.6, prop:content-scaling-correspondence
-/
namespace QOU.BraidKnot
/-- Box content in a Young diagram. -/
def boxContent (row col : ℕ) : ℤ := col - row
end QOU.BraidKnot
