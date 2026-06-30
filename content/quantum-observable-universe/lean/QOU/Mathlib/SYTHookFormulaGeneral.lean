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

  Once the **residual gap** — the Aitken/Frobenius determinant evaluation, for which the pinned Mathlib
  has no `Combinatorics.RSK`/Specht/Frobenius-determinant infrastructure — it is now **proved sorry-free**
  via the Greene–Nijenhuis–Wilf **corner recursion** (no determinant infrastructure at all).

## Where the closed (ii) and the general HLF live

The corner-recursion infrastructure (`SYTListCorner`/`SYTCornerListConnection`) and the β-Lagrange
Vandermonde keystone (`SYTHookGNWRatio`/`SYTBetaLagrange`) sit **downstream** of this file, so the
canonical sorry-free statements live in `SYTHookGNW`: `SYTHookGNW.dimAitkenIdentity` (ii) and the
general HLF `SYTHookGNW.numSYTenum_eq_dimHLF` (`= #SYT(λ) = dimHLF λ`).  The upstream inputs they consume
— hook side (i) `prodHooks_mul_betaProdGap` and positivity `betaProdGap_pos` — are below, both
sorry-free.  The `decide`-verified `dimAitkenIdentity_le4`/`_5`/`_6` remain as finite cross-checks.

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

/-! ## (ii) dimension side — the Aitken/Frobenius determinant identity (CLOSED, sorry-free, downstream)

The dimension-side identity `numSYTenum l · betaFactProd l = (sz l)! · betaProdGap l`
(`#SYT(λ) = n!·∏(β_i−β_j)/∏β_i!`) — once the residual general-`n` gap, the Aitken/Frobenius
determinant `det(1/(β_i − k + j)!)` blocked by the pinned Mathlib's missing
`Combinatorics.RSK`/Specht/Frobenius-determinant infrastructure — is now **proved sorry-free** via the
Greene–Nijenhuis–Wilf **corner recursion**, with no determinant infrastructure at all.

Because the corner-recursion infrastructure (`SYTListCorner`/`SYTCornerListConnection`) and the
β-Lagrange Vandermonde keystone (`SYTHookGNWRatio`/`SYTBetaLagrange`) sit **downstream** of this file
(they import it), the canonical sorry-free statement lives in `SYTHookGNW`:
`SYTHookGNW.dimAitkenIdentity` (= `dimAitkenIdentity_of_gnw`) and the general HLF
`SYTHookGNW.numSYTenum_eq_dimHLF` (= `numSYTenum_eq_dimHLF_gnw`).  The hook side (i)
`prodHooks_mul_betaProdGap` and the positivity `betaProdGap_pos` above are the upstream inputs that
identity consumes; the `decide`-verified `dimAitkenIdentity_le4`/`_5`/`_6` below are finite
cross-checks of the same equation. -/

/-- **Aitken identity, `decide`-verified for every shape of `sz ≤ 4` (sorry-free).**  The exact
`dimAitkenIdentity` equation on a closed shape is a decidable `ℕ` computation; this discharges it for
all `sz ≤ 4` directly from the brute-force `numSYTenum`. -/
theorem dimAitkenIdentity_le4 :
    ∀ l ∈ shapesLE4, numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by decide

/-- **Aitken identity, `decide`-verified for every shape of `sz = 5` (sorry-free).** -/
theorem dimAitkenIdentity_5 :
    ∀ l ∈ shapes5, numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by decide

set_option maxRecDepth 20000 in
/-- **Aitken identity, `decide`-verified for every shape of `sz = 6` (sorry-free).**  Needs
`maxRecDepth` raised for the `720`-deep structural permutation recursion in `numSYTenum`. -/
theorem dimAitkenIdentity_6 :
    ∀ l ∈ shapes6, numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by decide

/-! The divisor-free HLF `#SYT(λ)·∏h_λ = n!` and the general HLF `numSYTenum l = dimHLF l` are proved
sorry-free downstream from the corner recursion: `SYTHookGNW.numSYTenum_mul_prodHooks` and
`SYTHookGNW.numSYTenum_eq_dimHLF` (the former `numSYTenum_eq_dimHLF_of_aitken`-style wrappers, which were
conditional on the now-discharged Aitken gap, are retired in favour of those unconditional proofs). -/

end QOU.Mathlib.SYTEnum
