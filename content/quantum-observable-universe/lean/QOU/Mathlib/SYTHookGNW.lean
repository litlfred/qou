import QOU.Mathlib.SYTHookFormulaGeneral
import QOU.Mathlib.SYTListCorner
import QOU.Mathlib.SYTCornerListConnection
import QOU.Mathlib.SYTHookGNWRatio

/-!
# QOU.Mathlib.SYTHookGNW — corner-recursion route for the general HLF (GNW)

The general dimension hook-length formula `numSYTenum l = dimHLF l` was once isolated to the single
**Aitken/Frobenius determinant identity** (ii), blocked by the pinned Mathlib (no `Combinatorics.RSK` /
Specht / Frobenius-determinant infrastructure).  This file closes it **sorry-free** via the
**Greene–Nijenhuis–Wilf corner-recursion** route, which needs **none** of that infrastructure — pure
`ℕ`/`ℚ` combinatorics — from two identities, both now proved:

* **corner recursion of the count** (`cornerRecursion`):
  `numSYTenum λ = Σ_{removable corners c} numSYTenum (λ ∖ c)` — sorry-free in
  `SYTCornerListConnection.cornerRecursion_proof`, via the structural branching rule on
  `StandardYoungTableau` (`SYTBranchingRule`) and the diagram↔list corner correspondence;
* **GNW hook-summation identity** (`gnwHookIdentity`, over `ℚ`):
  `Σ_{corners c} ∏h_λ / ∏h_{λ∖c} = n` — the partial-fractions / telescoping identity on hook products,
  sorry-free in `SYTHookGNWRatio.gnwHookIdentity_proof` (per-corner hook ratio + the β-Lagrange
  Vandermonde keystone in `SYTBetaLagrange`).

A strong induction on `n = sz l` combines the two into the divisor-free HLF `#SYT(λ)·∏h_λ = n!`, whence
the Aitken identity and the general HLF.  Because the corner-removal infrastructure (`SYTListCorner`)
sits **downstream** of `SYTHookFormulaGeneral`, the canonical sorry-free names `dimAitkenIdentity` and
`numSYTenum_eq_dimHLF` live here (the former `SYTHookFormulaGeneral` versions carried the now-retired
cited `sorry`).

Pure combinatorics on `ℕ`/`ℚ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (prodHooks dimHLF sz)

/-! ## The residual GNW hook identity (cited `sorry`) and the count corner recursion (now proved)

The **count corner recursion** (`cornerRecursion`) is now **discharged** — proved sorry-free in
`SYTCornerListConnection` (`cornerRecursion_proof`), through the structural branching rule on
`StandardYoungTableau` and the diagram↔list corner correspondence.  The *only* remaining gap of the GNW
route is the hook-summation identity below (pure `ℚ` partial fractions). -/

/-- **(GNW count) corner recursion of the standard-tableau count (proved).**  In any standard tableau of
shape `λ` the largest entry `n` occupies a removable corner; deleting it is a bijection
`SYT(λ) ≃ ⨆_{corners c} SYT(λ ∖ c)`, whence the count splits as a sum.  Proved sorry-free in
`SYTCornerListConnection.cornerRecursion_proof` via the structural branching rule. -/
theorem cornerRecursion (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a)
    (hne : l ≠ []) :
    numSYTenum l = ((corners l).map (fun c => numSYTenum (removeCorner l c))).sum :=
  cornerRecursion_proof l hl (by
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => have := hpos a (List.mem_cons_self ..); unfold sz; rw [List.sum_cons]; omega)

/-- **(GNW hook) hook-summation identity — the sole remaining gap of the GNW route.**  Summing the
hook-product ratios over the removable corners gives the cell count: `∑_{corners c} ∏h_λ / ∏h_{λ∖c} = n`.
This is the partial-fractions / telescoping core of the Greene–Nijenhuis–Wilf proof — the rational
identity that turns the count recursion into the hook-length formula.

**Closure (PROVED, sorry-free).**  Via the *already-proved* β-number identity (i)
(`SYTHookFormulaGeneral.prodHooks_mul_betaProdGap`: `∏h_λ · betaProdGap = betaFactProd`,
`β_i = λ_i + (k−1−i)`), each ratio rewrites as a β-ratio, reducing this to the **β-Lagrange identity**

    ∑_i β_i · ∏_{j≠i} (β_i − 1 − β_j) / (β_i − β_j) = (∑_i β_i) − C(k,2)   ( = sz l ),

a self-contained `ℚ` partial-fractions identity over the distinct `β_i` (non-corner `i` drop out because
`β_i − 1 = β_{i+1}` there).  The β-Lagrange identity is proved in `SYTBetaLagrange.betaLagrange` via the
Vandermonde/`det_vandermonde` keystone (`SYTVandermonde.interp_leadingCoeff`); the per-corner hook ratio
(`SYTHookGNWRatio.prodHooks_ratio`/`prodHooks_removeCorner`, incl. the row-drop corner) and the assembly
over corners (`SYTHookGNWRatio.gnwHookIdentity_proof`) discharge this identity outright. -/
theorem gnwHookIdentity (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a)
    (hne : l ≠ []) :
    ((corners l).map (fun c => (prodHooks l : ℚ) / (prodHooks (removeCorner l c) : ℚ))).sum
      = (sz l : ℚ) :=
  QOU.Mathlib.SYTBetaLagrange.gnwHookIdentity_proof l hl hpos hne

/-! ## The sorry-free reduction: corner recursion + GNW hook identity ⟹ HLF

Strong induction on `n = sz l` combining `cornerRecursion` and `gnwHookIdentity`.  Everything below is
machine-checked; the *only* unproved inputs are the two identities above. -/

/-- Strong-induction core: `#SYT(λ) = n! / ∏h_λ` over `ℚ`, conditional on the two GNW identities. -/
private theorem numSYTenum_eq_div_aux :
    ∀ (n : ℕ) (l : List ℕ), sz l = n → List.Sorted (· ≥ ·) l → (∀ a ∈ l, 0 < a) →
      (numSYTenum l : ℚ) = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro l hsz hl hpos
    rcases eq_or_ne l [] with hnil | hne
    · subst hnil
      have h1 : numSYTenum [] = 1 := by decide
      have h2 : prodHooks [] = 1 := by decide
      simp [h1, h2, sz]
    · -- inductive step
      have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
      have hphQ : (prodHooks l : ℚ) ≠ 0 := by exact_mod_cast hph.ne'
      have hn1 : 1 ≤ n := by
        rcases l with _ | ⟨a, t⟩
        · exact absurd rfl hne
        · have := hpos a (List.mem_cons_self ..)
          rw [← hsz]; unfold sz; rw [List.sum_cons]; omega
      have hcr := cornerRecursion l hl hpos hne
      have hgnw := gnwHookIdentity l hl hpos hne
      -- value of the inner ∑ (∏h_{λ∖c})⁻¹
      have hSval : ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum
          = (sz l : ℚ) / prodHooks l := by
        have hg : (prodHooks l : ℚ)
            * ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum = (sz l : ℚ) := by
          rw [← sum_map_const_mul, ← hgnw]
          apply congrArg List.sum
          apply List.map_congr_left
          intro c _
          rw [div_eq_mul_inv]
        rw [eq_div_iff hphQ, mul_comm]
        exact hg
      -- n! = n · (n−1)!
      have hfact : (n.factorial : ℚ) = (n : ℚ) * ((n - 1).factorial : ℚ) := by
        rcases n with _ | m
        · omega
        · simp only [Nat.add_sub_cancel, Nat.factorial_succ]; push_cast; ring
      calc (numSYTenum l : ℚ)
          = ((corners l).map (fun c => (numSYTenum (removeCorner l c) : ℚ))).sum := by
            rw [hcr]; push_cast; rw [List.map_map]; rfl
        _ = ((corners l).map
              (fun c => ((n - 1).factorial : ℚ) * (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum := by
            apply congrArg List.sum
            apply List.map_congr_left
            intro c hc
            have hcorner := mem_corners hc
            have hszc1 : sz (removeCorner l c) + 1 = sz l :=
              sz_removeCorner l c hcorner.1 (getD_pos_of_corner hpos hcorner)
            have hszc : sz (removeCorner l c) = n - 1 := by omega
            have hmlt : sz (removeCorner l c) < n := by omega
            have hihc := ih (sz (removeCorner l c)) hmlt (removeCorner l c) rfl
              (sorted_removeCorner l c hl hcorner) (removeCorner_pos l c)
            rw [hihc, hszc, div_eq_mul_inv]
        _ = ((n - 1).factorial : ℚ)
              * ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum := by
            rw [sum_map_const_mul]
        _ = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) := by
            rw [hSval, hsz, hfact]; field_simp

/-- **#SYT(λ) = n!/∏h_λ over `ℚ`** — conditional on `cornerRecursion` + `gnwHookIdentity`. -/
theorem numSYTenum_eq_factorial_div (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    (numSYTenum l : ℚ) = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) :=
  numSYTenum_eq_div_aux (sz l) l rfl hl hpos

/-- **Divisor-free HLF `#SYT(λ) · ∏h_λ = n!`** (over `ℕ`) — conditional on the two GNW identities.
This is exactly the divisor-free Frame–Robinson–Thrall form; proving the two GNW identities makes it
unconditional. -/
theorem numSYTenum_mul_prodHooks (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * prodHooks l = (sz l).factorial := by
  have hQ := numSYTenum_eq_factorial_div l hl hpos
  have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
  have hphQ : (prodHooks l : ℚ) ≠ 0 := by exact_mod_cast hph.ne'
  have hmul : (numSYTenum l : ℚ) * prodHooks l = ((sz l).factorial : ℚ) := by
    rw [hQ]; field_simp
  exact_mod_cast hmul

/-- **General Frame–Robinson–Thrall HLF `#SYT(λ) = dimHLF λ`** via the GNW route (sorry-free).
Routed through the self-contained corner recursion rather than any Mathlib determinant. -/
theorem numSYTenum_eq_dimHLF_gnw (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = dimHLF l := by
  have hkey := numSYTenum_mul_prodHooks l hl hpos
  have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
  unfold dimHLF
  rw [← hkey, Nat.mul_div_cancel _ hph]

/-- **The Aitken/Frobenius determinant identity, via the GNW route (sorry-free).**  Once the
determinant-blocked residual gap (`det(1/(β_i − k + j)!)`, needing Specht/RSK infra absent from the
pinned Mathlib), here obtained with **no determinant infrastructure**: combine the divisor-free HLF
`#SYT·∏h = n!` with the merged hook-product identity (i) `∏h · betaProdGap = betaFactProd`. -/
theorem dimAitkenIdentity_of_gnw (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by
  have hi := prodHooks_mul_betaProdGap l hl
  have hkey := numSYTenum_mul_prodHooks l hl hpos
  rw [← hi, ← mul_assoc, hkey]

/-! ## Canonical sorry-free entry points

The corner-recursion infrastructure (`SYTListCorner`/`SYTCornerListConnection`) and the β-Lagrange
Vandermonde keystone sit *downstream* of `SYTHookFormulaGeneral` (they import it), so the canonical
sorry-free names live here, where the GNW proof is available.  These supersede the former
`SYTHookFormulaGeneral.{dimAitkenIdentity, numSYTenum_eq_dimHLF}` (which carried a cited determinant
`sorry`, now retired). -/

/-- **The general-`n` Aitken/Frobenius determinant identity (sorry-free).** Canonical name; closes the
former determinant-blocked gap via the GNW corner recursion. -/
theorem dimAitkenIdentity (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l :=
  dimAitkenIdentity_of_gnw l hl hpos

/-- **The general Frame–Robinson–Thrall hook-length formula `#SYT(λ) = dimHLF λ` (sorry-free).**
Canonical name; the corpus' general-`n` HLF, closed via the GNW corner recursion. -/
theorem numSYTenum_eq_dimHLF (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = dimHLF l :=
  numSYTenum_eq_dimHLF_gnw l hl hpos

end QOU.Mathlib.SYTEnum
