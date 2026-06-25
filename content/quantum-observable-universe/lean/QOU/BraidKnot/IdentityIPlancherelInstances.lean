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

This file **discharges the class outright for every `n = 3..12`** — the full range the underlying
`decide`-checks (`dim_validated_le12` / `idB_verified_le12`) cover, including the physically-relevant
`n` (the deuteron `pn` channel at `n = 3`; the s5-so3 keystone itself at `n = 5`; the defect-cubic
sign flip at `n = 7`) — by an explicit finite construction, **needing no Specht / RSK / Jucys–Murphy
infrastructure**:

* `parts` = the partitions of `n` (read off the verified `allPartsLE9` enumeration);
* `dim`   = the **Frame–Robinson–Thrall hook-length dimension** `dimHLF` of
  `IdentityIContentDecomposition`, whose value is the honest `#SYT(λ)` (certified by
  `dim_validated_le12`, the RSK sum-of-squares);
* both axioms **(i)/(ii)** discharged by kernel `decide` — the *same* finite computation already
  run in `dim_validated_le12` / `idB_verified_le12`, now wired into the class.

Consequently `two_sum_dim_sq_hooks` and `twoM_eq_plancherel_hook_sum` (the keystone's
`WLambdaDefect.twoM` = Identity I bridge) hold **unconditionally** at every `n = 3..12`: at these
`n` the keystone's one carried representation-theoretic input is *proved*, not axiomatic, so the
falsifiable defect cubic `144·C(n) = −n(n−1)(2n−13)` — including its sign flip at `n = 7` — rests
on proved inputs there.  The final section makes this explicit: `n144C_eq_twelve_plancherel` and
`defect_closedform_plancherel` re-express `WLambdaDefect.n144C` (defined from the carried `twoM`)
directly in terms of the **genuine Plancherel-weighted squared-hook sum**, so the keystone defect
coefficient is grounded in real representation theory (not a bare `def`) for every registered `n`.

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

/-- **`PlancherelSnData 6`** — the 11 partitions of 6 (`Σ dim² = 720 = 6!`). -/
instance plancherelSnData_six : PlancherelSnData 6 where
  parts := {[6], [5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1], [2, 2, 2],
            [2, 2, 1, 1], [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 7`** — the 15 partitions of 7 (`Σ dim² = 5040 = 7!`).  `n = 7` is where
the falsifiable defect cubic `144·C(n) = −n(n−1)(2n−13)` has its **sign flip** (`2n−13` changes
sign), so this is the most diagnostic `n` for the keystone's defect target — Identity I is now
proved (not axiomatic) exactly there. -/
instance plancherelSnData_seven : PlancherelSnData 7 where
  parts := {[7], [6, 1], [5, 2], [5, 1, 1], [4, 3], [4, 2, 1], [4, 1, 1, 1], [3, 3, 1], [3, 2, 2],
            [3, 2, 1, 1], [3, 1, 1, 1, 1], [2, 2, 2, 1], [2, 2, 1, 1, 1], [2, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 8`** — 22 partitions (`Σ dim² = 8! = 40320`). -/
instance plancherelSnData_eight : PlancherelSnData 8 where
  parts := {[8], [7, 1], [6, 2], [6, 1, 1], [5, 3], [5, 2, 1], [5, 1, 1, 1], [4, 4], [4, 3, 1], [4, 2, 2], [4, 2, 1, 1], [4, 1, 1, 1, 1], [3, 3, 2], [3, 3, 1, 1], [3, 2, 2, 1], [3, 2, 1, 1, 1], [3, 1, 1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 1, 1], [2, 2, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 9`** — 30 partitions (`Σ dim² = 9! = 362880`). -/
instance plancherelSnData_nine : PlancherelSnData 9 where
  parts := {[9], [8, 1], [7, 2], [7, 1, 1], [6, 3], [6, 2, 1], [6, 1, 1, 1], [5, 4], [5, 3, 1], [5, 2, 2], [5, 2, 1, 1], [5, 1, 1, 1, 1], [4, 4, 1], [4, 3, 2], [4, 3, 1, 1], [4, 2, 2, 1], [4, 2, 1, 1, 1], [4, 1, 1, 1, 1, 1], [3, 3, 3], [3, 3, 2, 1], [3, 3, 1, 1, 1], [3, 2, 2, 2], [3, 2, 2, 1, 1], [3, 2, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 1], [2, 2, 2, 1, 1, 1], [2, 2, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 10`** — 42 partitions (`Σ dim² = 10! = 3628800`). -/
instance plancherelSnData_ten : PlancherelSnData 10 where
  parts := {[10], [9, 1], [8, 2], [8, 1, 1], [7, 3], [7, 2, 1], [7, 1, 1, 1], [6, 4], [6, 3, 1], [6, 2, 2], [6, 2, 1, 1], [6, 1, 1, 1, 1], [5, 5], [5, 4, 1], [5, 3, 2], [5, 3, 1, 1], [5, 2, 2, 1], [5, 2, 1, 1, 1], [5, 1, 1, 1, 1, 1], [4, 4, 2], [4, 4, 1, 1], [4, 3, 3], [4, 3, 2, 1], [4, 3, 1, 1, 1], [4, 2, 2, 2], [4, 2, 2, 1, 1], [4, 2, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1], [3, 3, 3, 1], [3, 3, 2, 2], [3, 3, 2, 1, 1], [3, 3, 1, 1, 1, 1], [3, 2, 2, 2, 1], [3, 2, 2, 1, 1, 1], [3, 2, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1], [2, 2, 2, 1, 1, 1, 1], [2, 2, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 11`** — 56 partitions (`Σ dim² = 11! = 39916800`). -/
instance plancherelSnData_eleven : PlancherelSnData 11 where
  parts := {[11], [10, 1], [9, 2], [9, 1, 1], [8, 3], [8, 2, 1], [8, 1, 1, 1], [7, 4], [7, 3, 1], [7, 2, 2], [7, 2, 1, 1], [7, 1, 1, 1, 1], [6, 5], [6, 4, 1], [6, 3, 2], [6, 3, 1, 1], [6, 2, 2, 1], [6, 2, 1, 1, 1], [6, 1, 1, 1, 1, 1], [5, 5, 1], [5, 4, 2], [5, 4, 1, 1], [5, 3, 3], [5, 3, 2, 1], [5, 3, 1, 1, 1], [5, 2, 2, 2], [5, 2, 2, 1, 1], [5, 2, 1, 1, 1, 1], [5, 1, 1, 1, 1, 1, 1], [4, 4, 3], [4, 4, 2, 1], [4, 4, 1, 1, 1], [4, 3, 3, 1], [4, 3, 2, 2], [4, 3, 2, 1, 1], [4, 3, 1, 1, 1, 1], [4, 2, 2, 2, 1], [4, 2, 2, 1, 1, 1], [4, 2, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1, 1], [3, 3, 3, 2], [3, 3, 3, 1, 1], [3, 3, 2, 2, 1], [3, 3, 2, 1, 1, 1], [3, 3, 1, 1, 1, 1, 1], [3, 2, 2, 2, 2], [3, 2, 2, 2, 1, 1], [3, 2, 2, 1, 1, 1, 1], [3, 2, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 1, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **`PlancherelSnData 12`** — 77 partitions (`Σ dim² = 12! = 479001600`), the bound of the
underlying `dim_validated_le12` / `idB_verified_le12` machine checks. -/
instance plancherelSnData_twelve : PlancherelSnData 12 where
  parts := {[12], [11, 1], [10, 2], [10, 1, 1], [9, 3], [9, 2, 1], [9, 1, 1, 1], [8, 4], [8, 3, 1], [8, 2, 2], [8, 2, 1, 1], [8, 1, 1, 1, 1], [7, 5], [7, 4, 1], [7, 3, 2], [7, 3, 1, 1], [7, 2, 2, 1], [7, 2, 1, 1, 1], [7, 1, 1, 1, 1, 1], [6, 6], [6, 5, 1], [6, 4, 2], [6, 4, 1, 1], [6, 3, 3], [6, 3, 2, 1], [6, 3, 1, 1, 1], [6, 2, 2, 2], [6, 2, 2, 1, 1], [6, 2, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1, 1], [5, 5, 2], [5, 5, 1, 1], [5, 4, 3], [5, 4, 2, 1], [5, 4, 1, 1, 1], [5, 3, 3, 1], [5, 3, 2, 2], [5, 3, 2, 1, 1], [5, 3, 1, 1, 1, 1], [5, 2, 2, 2, 1], [5, 2, 2, 1, 1, 1], [5, 2, 1, 1, 1, 1, 1], [5, 1, 1, 1, 1, 1, 1, 1], [4, 4, 4], [4, 4, 3, 1], [4, 4, 2, 2], [4, 4, 2, 1, 1], [4, 4, 1, 1, 1, 1], [4, 3, 3, 2], [4, 3, 3, 1, 1], [4, 3, 2, 2, 1], [4, 3, 2, 1, 1, 1], [4, 3, 1, 1, 1, 1, 1], [4, 2, 2, 2, 2], [4, 2, 2, 2, 1, 1], [4, 2, 2, 1, 1, 1, 1], [4, 2, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1, 1, 1], [3, 3, 3, 3], [3, 3, 3, 2, 1], [3, 3, 3, 1, 1, 1], [3, 3, 2, 2, 2], [3, 3, 2, 2, 1, 1], [3, 3, 2, 1, 1, 1, 1], [3, 3, 1, 1, 1, 1, 1, 1], [3, 2, 2, 2, 2, 1], [3, 2, 2, 2, 1, 1, 1], [3, 2, 2, 1, 1, 1, 1, 1], [3, 2, 1, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 1, 1], [2, 2, 2, 2, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 1, 1], [2, 2, 1, 1, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-! ## Identity I is now unconditional at `n = 3..12`

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

/-- Identity I, **unconditional at `n = 6`**. -/
theorem twoM_plancherel_six :
    2 * ∑ l ∈ plancherelSnData_six.parts,
        (plancherelSnData_six.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (6 : ℤ) * (Nat.factorial 6 : ℤ) := by
  exact twoM_eq_plancherel_hook_sum 6

/-- Identity I, **unconditional at `n = 7`** (the defect-cubic sign-flip degree). -/
theorem twoM_plancherel_seven :
    2 * ∑ l ∈ plancherelSnData_seven.parts,
        (plancherelSnData_seven.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (7 : ℤ) * (Nat.factorial 7 : ℤ) := by
  exact twoM_eq_plancherel_hook_sum 7

/-! ## The keystone defect coefficient `n144C`, grounded in genuine representation theory

`WLambdaDefect.n144C n = 6·twoM n − sixS n − 12n` is the keystone's falsifiable defect coefficient
`144·C(n)` (`n144C_closed_form : n144C n = −n(n−1)(2n−13)`), but it is built from the **carried**
`def twoM n = n(3n−1)` — `WLambdaDefectClosedForm` only anchors that `def` to the genuine quantity
at `n = 4, 6` via its own local `numerComputed`.  The two theorems below replace the carried `twoM`
by the **genuine Plancherel-weighted squared-hook sum** for any `n` with a `PlancherelSnData`
instance — i.e. at every `n = 2..12` registered here — so the defect coefficient (and its closed
form, sign flip included) rests on real `S_n` representation theory, not a `def`.  This is the
Lean complement to #2744's numerical cross-check of `C(n)` against the directly-computed `1−Z(n)`. -/

/-- **`n144C` in terms of the genuine Plancherel sum.** For any `n` with `PlancherelSnData`,
`n144C n · n! = 12·(Σ_λ dim(λ)²·Σ_c h_c²) − (sixS n + 12n)·n!` — the carried `twoM` `def` is
eliminated in favour of the real squared-hook sum via `twoM_eq_plancherel_hook_sum`. -/
theorem n144C_eq_twelve_plancherel (n : ℕ) [h : PlancherelSnData n] :
    QOU.BraidKnot.WLambdaDefect.n144C (n : ℤ) * (Nat.factorial n : ℤ)
      = 12 * (∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * sumSqHooks l)
        - (QOU.BraidKnot.WLambdaDefect.sixS (n : ℤ) + 12 * (n : ℤ)) * (Nat.factorial n : ℤ) := by
  have hh := twoM_eq_plancherel_hook_sum n
  unfold QOU.BraidKnot.WLambdaDefect.n144C
  linear_combination (-6 : ℤ) * hh

/-- **The keystone defect cubic, grounded in genuine representation theory.** Composing
`n144C_eq_twelve_plancherel` with `n144C_closed_form`: for any `n` with `PlancherelSnData`, the
genuine Plancherel squared-hook expression equals the keystone defect cubic `−n(n−1)(2n−13)`
(cleared by `n!`).  At the registered `n = 2..12` this is therefore **unconditional** — including
the `n = 7` sign flip the keystone's falsifiable target hinges on. -/
theorem defect_closedform_plancherel (n : ℕ) [h : PlancherelSnData n] :
    12 * (∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * sumSqHooks l)
        - (QOU.BraidKnot.WLambdaDefect.sixS (n : ℤ) + 12 * (n : ℤ)) * (Nat.factorial n : ℤ)
      = -((n : ℤ) * ((n : ℤ) - 1) * (2 * (n : ℤ) - 13)) * (Nat.factorial n : ℤ) := by
  rw [← n144C_eq_twelve_plancherel n, QOU.BraidKnot.WLambdaDefect.n144C_closed_form]

end QOU.BraidKnot.IdentityI
