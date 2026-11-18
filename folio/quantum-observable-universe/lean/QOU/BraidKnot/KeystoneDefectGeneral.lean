import QOU.BraidKnot.IdentityIPlancherelInstances
import QOU.BraidKnot.PlancherelSnDataGeneral

/-!
# The keystone defect cubic on genuine representation theory, at every `n`

`WLambdaDefect.n144C n = 6·twoM n − sixS n − 12n` is the keystone's falsifiable defect coefficient
`144·C(n)`, and `WLambdaDefectClosedForm` carries `twoM n = n(3n−1)` as a bare `def`.
`IdentityIPlancherelInstances` replaces that carried `def` by the genuine Plancherel-weighted
squared-hook sum — `n144C_eq_twelve_plancherel` and `defect_closedform_plancherel` — for any `n`
carrying a `PlancherelSnData` instance, which meant `n = 2 … 12`.

`PlancherelSnDataGeneral` builds that datum at every `n`, so both restate here with no hypothesis
and no bound. The `n = 7` sign flip the keystone's falsifiable target hinges on sits inside the old
range and is unaffected; what changes is that the grounding no longer *stops* at 12, so the cubic's
behaviour at large `n` rests on the same representation theory as its behaviour at small `n`.

**This grounds the defect coefficient; it does not vindicate the keystone.** `n144C_closed_form`
is an identity about `n144C`, and what these theorems add is that the `twoM` inside it is the real
Plancherel sum rather than a carried `def`. Whether the keystone's physical claim holds is a
separate question and is untouched.

Pure instantiation; nothing archimedean; no fit.
-/

namespace QOU.BraidKnot.KeystoneDefectGeneral

open QOU.BraidKnot
open QOU.BraidKnot.IdentityI (dimHLF sumSqHooks partitionsOf)

/-- **`n144C` in terms of the genuine Plancherel sum, at every `n`.** -/
theorem n144C_eq_twelve_plancherel (n : ℕ) :
    WLambdaDefect.n144C (n : ℤ) * (Nat.factorial n : ℤ)
      = 12 * (∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l)
        - (WLambdaDefect.sixS (n : ℤ) + 12 * (n : ℤ)) * (Nat.factorial n : ℤ) :=
  IdentityI.n144C_eq_twelve_plancherel (h := PlancherelSnDataGeneral.plancherelSnDataGeneral n) n

/-- **The keystone defect cubic, grounded in genuine representation theory, at every `n`** —
`12·Σ_λ dim(λ)²·Σ_c h_c² − (sixS n + 12n)·n! = −n(n−1)(2n−13)·n!`, where the corpus had `n = 2 … 12`. -/
theorem defect_closedform_plancherel (n : ℕ) :
    12 * (∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l)
        - (WLambdaDefect.sixS (n : ℤ) + 12 * (n : ℤ)) * (Nat.factorial n : ℤ)
      = -((n : ℤ) * ((n : ℤ) - 1) * (2 * (n : ℤ) - 13)) * (Nat.factorial n : ℤ) :=
  IdentityI.defect_closedform_plancherel (h := PlancherelSnDataGeneral.plancherelSnDataGeneral n) n

/-- Past the old registered range: `n = 20` carries no hand-written instance. -/
example :
    12 * (∑ l ∈ (partitionsOf 20).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l)
        - (WLambdaDefect.sixS 20 + 12 * 20) * (Nat.factorial 20 : ℤ)
      = -(20 * (20 - 1) * (2 * 20 - 13)) * (Nat.factorial 20 : ℤ) :=
  defect_closedform_plancherel 20

/-- Subtracting the closed-form cubic factorial product from the Plancherel hook-square defect expression yields zero. -/
theorem defect_closedform_plancherel_sub_eq_zero (n : ℕ) :
    (12 * (∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l)
        - (WLambdaDefect.sixS (n : ℤ) + 12 * (n : ℤ)) * (Nat.factorial n : ℤ))
      - (-((n : ℤ) * ((n : ℤ) - 1) * (2 * (n : ℤ) - 13)) * (Nat.factorial n : ℤ)) = 0 := by
  rw [defect_closedform_plancherel, sub_self]

end QOU.BraidKnot.KeystoneDefectGeneral
