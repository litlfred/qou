import QOU.Mathlib.SYTHookFormulaBetaProd

/-!
# QOU.Mathlib.SYTHookGNW — closing the general HLF via corner recursion (GNW route)

Target (closes the residual gap of `SYTHookFormulaGeneral.dimAitkenIdentity`):

    numSYTenum_mul_prodHooks (l) (hl) (hpos) :
        QOU.Mathlib.SYTEnum.numSYTenum l * QOU.BraidKnot.IdentityI.prodHooks l = (sz l).factorial

the **divisor-free** Frame–Robinson–Thrall hook-length formula.  Proving it discharges
`dimAitkenIdentity` (via the merged hook-product identity (i) `prodHooks · betaProdGap = betaFactProd`)
and makes `numSYTenum_eq_dimHLF` unconditional.

Route (no Specht/determinant infra needed — pure ℕ/ℚ algebra):
* **corner recursion for the count** — `numSYTenum λ = Σ_{removable corners c} numSYTenum (λ∖c)`
  (the largest entry sits in a removable corner; delete it);
* **GNW hook-summation identity** — `(sz λ)!/∏h_λ = Σ_corners (sz(λ∖c))!/∏h_{λ∖c}`, i.e.
  `Σ_corners ∏ hook-ratios = 1` (partial fractions / telescoping);
* strong induction on `n = sz l`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.  Under construction.
-/

namespace QOU.Mathlib.SYTEnum

-- GNW corner-recursion HLF closure: under construction (see module docstring).

end QOU.Mathlib.SYTEnum
