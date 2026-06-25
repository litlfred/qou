import QOU.BraidKnot.IdentityIPlancherelConditional

/-!
# Identity I — explicit `PlancherelSnData n` instances (per-`n` axiom discharge)

`IdentityIPlancherelConditional` (#2709) proves the keystone's **Identity I** sorry-free
**conditional** on a single `class PlancherelSnData n`, which axiomatises the two standard
`ℂ[S_n]` facts the pinned Mathlib lacks:

* **(i)** `Σ_λ dim(λ)² = n!` (`sum_dim_sq`);
* **(ii)** the Jucys–Murphy / Okounkov–Vershik content-square Plancherel mean
  `2·Σ_λ dim(λ)²·Σ_c c(c)² = n(n−1)·n!` (`two_sum_dim_sq_content`).

That file ships only **one** model, `plancherelSnData_two`, so the conditional theorems are
non-vacuous but otherwise carry the `PlancherelSnData` hypothesis everywhere.

This file **discharges the class outright for `n = 3, 4, 5`** — the physically-relevant range
(the deuteron `pn` channel lives at `n = 3`; the s5-so3 keystone itself at `n = 5`) — by an
explicit finite construction, **needing no Specht / RSK / Jucys–Murphy infrastructure**:

* `parts` = the partitions of `n` (read off the verified `allPartsLE9` enumeration);
* `dim`   = the **Frame–Robinson–Thrall hook-length dimension** `dimHLF` of
  `IdentityIContentDecomposition`, whose value is the honest `#SYT(λ)` (certified by
  `dim_validated_le12`, the RSK sum-of-squares);
* both axioms **(i)/(ii)** discharged by kernel `decide` — the *same* finite computation already
  run in `dim_validated_le12` / `idB_verified_le12`, now wired into the class.

Consequently `two_sum_dim_sq_hooks` and `twoM_eq_plancherel_hook_sum` (the keystone's
`WLambdaDefect.twoM` = Identity I bridge) hold **unconditionally** at `n = 3, 4, 5`: at these `n`
the keystone's one carried representation-theoretic input is *proved*, not axiomatic, so the
falsifiable defect cubic `144·C(n) = −n(n−1)(2n−13)` rests on proved inputs there.

**Scope (honest).** This is the per-`n` slice only. The general-`n` discharge (Specht modules,
RSK / Jucys–Murphy, the hook-length formula) remains the multi-session program scoped in
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md` (phases P1–P5). This file is
its tractable down-payment: the conditional terminus is now also an *unconditional* result on the
physically-used `n`. No fit; base ring `ℤ`; nothing archimedean (no `q₀`, no 210 ppb).
-/

namespace QOU.BraidKnot.IdentityI

set_option maxRecDepth 100000

/-- **`PlancherelSnData 3`** — partitions `[3], [2,1], [1,1,1]` with hook-length dimensions
`1, 2, 1`.  (i) `Σ dim² = 1+4+1 = 6 = 3!`; (ii) `2·Σ dim²·Σc² = 2·(1·5+4·2+1·5) = 36 = 3·2·3!`.
`n = 3` is the deuteron `pn` channel of the keystone's binding-side target. -/
instance plancherelSnData_three : PlancherelSnData 3 where
  parts := {[3], [2, 1], [1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 4`** — the 5 partitions of 4, hook-length dimensions `1, 3, 2, 3, 1`
(`Σ dim² = 1+9+4+9+1 = 24 = 4!`). -/
instance plancherelSnData_four : PlancherelSnData 4 where
  parts := {[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 5`** — the 7 partitions of 5, hook-length dimensions `1, 4, 5, 6, 5, 4, 1`
(`Σ dim² = 1+16+25+36+25+16+1 = 120 = 5!`).  `n = 5` is the s5-so3 keystone's own degree
(`S₅ ⊃ A₅ ≅ I ⊂ SO(3)`). -/
instance plancherelSnData_five : PlancherelSnData 5 where
  parts := {[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-! ## Identity I is now unconditional at `n = 3, 4, 5`

With the instances above registered, the conditional theorems of
`IdentityIPlancherelConditional` fire with **no** hypothesis at these `n`: the keystone's
`WLambdaDefect.twoM` equals its Plancherel squared-hook sum (cleared of `1/n!`) outright. The
proofs are the conditional theorems applied at the concrete `n`; instance resolution supplies the
now-proved `PlancherelSnData` data. -/

/-- Identity I, **unconditional at `n = 3`** (the deuteron `pn` channel). -/
theorem twoM_plancherel_three :
    2 * ∑ l ∈ plancherelSnData_three.parts,
        (plancherelSnData_three.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (3 : ℤ) * (Nat.factorial 3 : ℤ) := by
  exact twoM_eq_plancherel_hook_sum 3

/-- Identity I, **unconditional at `n = 4`**. -/
theorem twoM_plancherel_four :
    2 * ∑ l ∈ plancherelSnData_four.parts,
        (plancherelSnData_four.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (4 : ℤ) * (Nat.factorial 4 : ℤ) := by
  exact twoM_eq_plancherel_hook_sum 4

/-- Identity I, **unconditional at `n = 5`** (the s5-so3 keystone's own `n`). -/
theorem twoM_plancherel_five :
    2 * ∑ l ∈ plancherelSnData_five.parts,
        (plancherelSnData_five.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (5 : ℤ) * (Nat.factorial 5 : ℤ) := by
  exact twoM_eq_plancherel_hook_sum 5

end QOU.BraidKnot.IdentityI
