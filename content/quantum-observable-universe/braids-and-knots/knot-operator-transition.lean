/-
  Knot operators for nucleon addition.
  D→³H: Hopf link operator. ³H→⁴He: trefoil operator.
  Ref: [manuscript] §5.11, prop:knot-operator-transition
-/
namespace QOU.BraidKnot
/-- The nucleon-addition operator type. -/
inductive AdditionKnotType where
  | singleCrossing : AdditionKnotType  -- p → D
  | hopfLink : AdditionKnotType        -- D → ³H, D → ³He
  | trefoil : AdditionKnotType         -- ³H → ⁴He, ³He → ⁴He
end QOU.BraidKnot
