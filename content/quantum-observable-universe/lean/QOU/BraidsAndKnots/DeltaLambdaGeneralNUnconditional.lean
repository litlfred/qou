import QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN
import QOU.BraidsAndKnots.NStatConjugateGeneral

/-!
# Δ_λ = DT/3d-index, general `n` — the UNCONDITIONAL capstone

`DeltaLambdaDTIndexGeneralN` (bean `qou-bvpp`) proved, for every partition:

* the **value** identity `dtEulerG (nStatList l) d = deltaLambdaG (nStatList l) d`
  (`dtEulerG_eq_deltaLambdaG`) — unconditional; and
* the **geometric-chirality** leg
  `deltaSignParity (nStatList l) = (-1)^{Σ_i C(λ'_i,2)}`
  (`parity_eq_w0_sign_of_nStat_eq_sumChoose2`) — but only *conditionally* on the
  identity `(†) n(λ) = Σ_i C(λ'_i, 2)`, discharged there only at `n ≤ 5`.

`NStatConjugateGeneral` (bean `qou-r0xk`) then proved `(†)` for **all** `n`
(`aStat_eq_sumChoose2_conjugate`, with `aStat` defeq to `nStatList`).

This file wires the two together: the chirality leg — and hence the full
general-`n` DT unification — with **no `n ≤ 5` restriction**.  Cosmetic bundle;
all mathematical content lives in the two imported modules.
-/

namespace QOU.BraidsAndKnots

/-- **Geometric-chirality leg, UNCONDITIONAL for all `n`.**  Discharges `(†)` via
    `aStat_eq_sumChoose2_conjugate` (`nStatList` is defeq to `aStat`), removing the
    `n ≤ 5` restriction of `parity_eq_w0_sign_of_nStat_eq_sumChoose2`. -/
theorem parity_eq_w0_sign_general (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    deltaSignParity (nStatList l) = (-1 : ℤ) ^ (sumChoose2 (conjugate l)) := by
  have hdagger : nStatList l = sumChoose2 (conjugate l) :=
    aStat_eq_sumChoose2_conjugate l hl
  exact parity_eq_w0_sign_of_nStat_eq_sumChoose2 l (conjugate l) hdagger

/-- **Capstone — the full general-`n` DT unification, UNCONDITIONAL.**  For every
    partition (a-function grade `nStatList l`, Wedderburn dimension `d`) the
    DT/3d-index Euler characteristic equals `Δ_λ` (the **value**), and the
    a-function-parity chirality equals the geometric longest-element sign
    `(-1)^{Σ_i C(λ'_i,2)}` (the **sign**) — with no `n ≤ 5` restriction on either
    leg. -/
theorem dtEuler_eq_deltaLambda_unconditional
    (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (d : ℕ) :
    dtEulerG (nStatList l) d = deltaLambdaG (nStatList l) d
      ∧ deltaSignParity (nStatList l) = (-1 : ℤ) ^ (sumChoose2 (conjugate l)) :=
  ⟨dtEulerG_eq_deltaLambdaG (nStatList l) d, parity_eq_w0_sign_general l hl⟩

end QOU.BraidsAndKnots
