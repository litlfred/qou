import QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional

/-!
# Sibling Lean file for `prop:delta-lambda-dt-index-unification`

The canonical general-`n` unconditional proof of

* **value:** `dtEulerG (nStatList l) d = deltaLambdaG (nStatList l) d`, and
* **geometric chirality:** `deltaSignParity (nStatList l) = (-1 : ℤ) ^ (sumChoose2 (conjugate l))`

lives in the Lake-package module `QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional`
(`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, `0` `sorry`), referenced
by `lean.ref` in `delta-lambda-dt-index-unification.ts`.

-- Ref: [springer1976] T. A. Springer, "Trigonometric sums, Green functions of finite groups and representations of Weyl groups", Invent. Math. 36 (1976), 173–207.
-- Ref: [shoji2019] T. Shoji, "Green functions of reductive groups — after Lusztig", 2019, Thm. 2.1.
-- Ref: [manuscript] prop:delta-lambda-dt-index-unification
-/

namespace QOU.BraidsAndKnots

#check @dtEuler_eq_deltaLambda_unconditional
#check @parity_eq_w0_sign_general

end QOU.BraidsAndKnots
