import QOU.Mathlib.SYTHookFormulaRows
import QOU.Mathlib.SYTHookFormulaBetaProd
import QOU.Mathlib.SYTEnumeration

/-!
# QOU.Mathlib.SYTHookFormulaGeneral — the general Frame–Robinson–Thrall hook-length formula

**Target:**

    numSYTenum_eq_dimHLF (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
        QOU.Mathlib.SYTEnum.numSYTenum l = QOU.BraidKnot.IdentityI.dimHLF l

This is the single pure-combinatorial identity the merged bridge collapses the dimension hook-length
formula to (`SYTEnumerationFintype.numSYTenum_eq_numStandardYoungTableaux`, all `n`, sorry-free): the
brute-force standard-tableau count equals the Frame–Robinson–Thrall closed form `(∑l)! / ∏h_c`.  It is
already closed for `∑l ≤ 4` (`numSYTenum_eq_dimHLF_le4`) and for one-row / two-row shapes
(`SYTHookFormulaRows`).

## State of the beta-number route (this PR)

The classical beta-number proof factors HLF as **two** identities (`β_i = l[i] + (k−1−i)`):

* **(i) hook side** — `∏_c h_λ(c) = (∏_i β_i!) / ∏_{i<j}(β_i − β_j)`.  **CLOSED, sorry-free, general
  `n`** in `SYTHookFormulaBetaProd` (`prodHooks_mul_betaGapProd`): in divisor-free form

      prodHooks l · betaProdGap l = betaFactProd l,

  where `betaProdGap l = ∏_i betaGapProd (l[i]) (l.drop (i+1)) = ∏_{i<j}(β_i − β_j)` (the Vandermonde)
  and `betaFactProd l = ∏_i (l[i] + (l.drop (i+1)).length)! = ∏_i β_i!`.

* **(ii) dimension side** — `#SYT(λ) = n! · ∏_{i<j}(β_i − β_j) / ∏_i β_i!` (Aitken / Frobenius
  determinant = Vandermonde / ∏β_i!).  In divisor-free form

      numSYTenum l · betaFactProd l = (sz l)! · betaProdGap l.        (`dimAitkenIdentity`)

  This is the **residual gap**: it is the Aitken/Frobenius determinant evaluation of the number of
  standard tableaux, for which the pinned Mathlib has **no** infrastructure (no `Combinatorics.RSK`,
  no Specht/Frobenius determinant).  It is stated here with a cited `sorry` (the honest "queued, not
  yet proved" marker — §1a), exactly as `IdentityIHLFBridge.dimSYT_eq_dimHLF` carries the same gap.

## The conditional composition (sorry-free *given* (ii))

`numSYTenum_eq_dimHLF_of_aitken` derives the full HLF from (i) + (ii) **with no further sorry**:
substitute (i) `betaFactProd = prodHooks · betaProdGap` into (ii), cancel the positive Vandermonde
`betaProdGap` (`betaProdGap_pos`), obtaining the divisor-free HLF `numSYTenum l · prodHooks l = (sz l)!`,
then divide.  So the general-`n` HLF is now **isolated to the single determinant identity (ii)** — the
hook side and the entire composition are machine-checked.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (prodHooks dimHLF sz)
open QOU.Mathlib.SYTBeta (betaGapProd betaGapProd_pos rowHookProd_mul_betaGapProd
  prodHooks_mul_betaGapProd drop_sorted drop_le_getD list_range_map_prod)

/-- The Vandermonde product `∏_{i<j}(β_i − β_j) = ∏_i betaGapProd (l[i]) (l.drop (i+1))`, in
divisor-free recursion-matched form. -/
def betaProdGap (l : List ℕ) : ℕ :=
  ((List.range l.length).map (fun i => betaGapProd (l.getD i 0) (l.drop (i + 1)))).prod

/-- The beta-factorial product `∏_i β_i! = ∏_i (l[i] + (l.drop (i+1)).length)!`. -/
def betaFactProd (l : List ℕ) : ℕ :=
  ((List.range l.length).map
    (fun i => Nat.factorial (l.getD i 0 + (l.drop (i + 1)).length))).prod

/-- **(i) hook side, general `n` (sorry-free), in the named form.**
`prodHooks l · betaProdGap l = betaFactProd l` — the Frame–Robinson–Thrall hook product cleared of its
Vandermonde denominator.  A thin renaming of `prodHooks_mul_betaGapProd`. -/
theorem prodHooks_mul_betaProdGap (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooks l * betaProdGap l = betaFactProd l := by
  unfold betaProdGap betaFactProd
  exact prodHooks_mul_betaGapProd l hl

/-- **The Vandermonde product is positive (sorry-free).** Each beta-gap factor is `≥ 1`. -/
theorem betaProdGap_pos (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) : 0 < betaProdGap l := by
  unfold betaProdGap
  rw [list_range_map_prod]
  apply Finset.prod_pos
  intro i hi
  rw [Finset.mem_range] at hi
  exact betaGapProd_pos (l.getD i 0) (l.drop (i + 1)) (drop_le_getD l hl i hi)

/-- **(ii) dimension side — the residual Aitken/Frobenius determinant identity (cited `sorry`).**
`numSYTenum l · betaFactProd l = (sz l)! · betaProdGap l`, i.e. `#SYT(λ) = n!·∏(β_i−β_j)/∏β_i!`.

This is the only remaining gap of the general-`n` hook-length formula in this corpus.  It is the
Aitken / Frobenius determinant evaluation `det(1/(β_i − k + j)!)` of the number of standard tableaux,
equal by `Matrix.det_vandermonde` to `∏_{i<j}(β_i − β_j)/∏β_i!` times `n!`.  The pinned Mathlib carries
no `Combinatorics.RSK` / Specht / Frobenius-determinant infrastructure, so this combinatorial identity
is queued, not yet proved (mirrors `IdentityIHLFBridge.dimSYT_eq_dimHLF`). -/
theorem dimAitkenIdentity (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by
  -- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001 (Aitken/Frobenius
  -- determinant for #SYT; §I.1, Ex. 1 and §I.5; HLF as Vandermonde / ∏β_i!).  Residual general-n gap.
  sorry

/-- **Divisor-free HLF, conditional on the Aitken identity (ii) (sorry-free given (ii)).**
`numSYTenum l · prodHooks l = (sz l)!`.  Substitutes (i) `betaFactProd = prodHooks · betaProdGap` into
(ii) and cancels the positive Vandermonde `betaProdGap`. -/
theorem numSYTenum_mul_prodHooks_of_aitken (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * prodHooks l = (sz l).factorial := by
  have hi := prodHooks_mul_betaProdGap l hl
  have hii := dimAitkenIdentity l hl hpos
  have hpgpos := betaProdGap_pos l hl
  -- numSYTenum * (prodHooks * betaProdGap) = (sz)! * betaProdGap
  rw [← hi] at hii
  -- hii : numSYTenum l * (prodHooks l * betaProdGap l) = (sz l)! * betaProdGap l
  have : numSYTenum l * prodHooks l * betaProdGap l = (sz l).factorial * betaProdGap l := by
    rw [mul_assoc]; exact hii
  exact Nat.eq_of_mul_eq_mul_right hpgpos this

/-- **General Frame–Robinson–Thrall hook-length formula, conditional on the Aitken identity (ii).**
`numSYTenum l = dimHLF l = (∑l)! / ∏h_c`.  Sorry-free **given** `dimAitkenIdentity`; divides the
divisor-free form by the positive hook product. -/
theorem numSYTenum_eq_dimHLF_of_aitken (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = dimHLF l := by
  have hkey := numSYTenum_mul_prodHooks_of_aitken l hl hpos
  unfold dimHLF
  -- prodHooks l > 0 (else (sz l)! = 0, impossible)
  have hph : 0 < prodHooks l := by
    rcases Nat.eq_zero_or_pos (prodHooks l) with h0 | hpos'
    · rw [h0, Nat.mul_zero] at hkey; exact absurd hkey.symm (Nat.factorial_ne_zero _)
    · exact hpos'
  rw [← hkey, Nat.mul_div_cancel _ hph]

/-- **General Frame–Robinson–Thrall hook-length formula (target).** `numSYTenum l = dimHLF l`.
Currently delegates to `numSYTenum_eq_dimHLF_of_aitken`, hence isolates the *entire* general-`n` gap to
the single Aitken/Frobenius determinant identity `dimAitkenIdentity` (ii); the hook side (i) and the
whole composition are sorry-free. -/
theorem numSYTenum_eq_dimHLF (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = dimHLF l :=
  numSYTenum_eq_dimHLF_of_aitken l hl hpos

end QOU.Mathlib.SYTEnum
