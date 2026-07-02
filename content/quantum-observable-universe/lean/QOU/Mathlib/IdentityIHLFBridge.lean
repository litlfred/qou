import QOU.Mathlib.SYTHookGNW
import QOU.Mathlib.SYTEnumerationFintype
import QOU.Mathlib.RSKBurnsideTarget
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.IdentityIHLFBridge — the hook-length bridge `dimSYT = dimHLF ∘ toList` (proved)

The session's two dimension notions for a partition `λ ⊢ n` are:

* `dimSYT p := numStandardYoungTableaux (partitionShape p)` — the **genuine** SYT count, a
  `Finite`-backed `Nat.card` over the `StandardYoungTableau` type (`RSKBurnsideTarget`); and
* `QOU.BraidKnot.IdentityI.dimHLF l := (sz l).factorial / ∏_c h_c` — the **Frame–Robinson–Thrall
  hook-length dimension** over the weakly-decreasing `List ℕ` model (`IdentityIContentDecomposition`),
  already `decide`-validated `Σ_λ dimHLF(λ)² = n!` for `n ≤ 12` (`dim_validated_le12`) and wired into
  the `PlancherelSnData {3..12}` instances.

The **hook-length formula** asserts these agree: `#SYT(λ) = n!/∏_c h_c`.  Stated on the partition
index (`p.parts` sorted weakly-decreasing is exactly the row-length list both `partitionShape` and
`PartitionListBridge.toList` build):

    dimSYT p = dimHLF (p.parts.sort (· ≥ ·)).

**Now sorry-free**, by composing two independently-proved halves:

* the counting bridge `SYTEnum.dimSYT_eq_numSYTenum` (`SYTEnumerationFintype`) — the genuine
  `Nat.card`-count equals the brute-force list enumeration `numSYTenum` of the sorted parts; and
* the general Frame–Robinson–Thrall HLF `SYTEnum.numSYTenum_eq_dimHLF` (`SYTHookGNW`) — the
  Greene–Nijenhuis–Wilf corner recursion closed via the β-Lagrange / Vandermonde-keystone
  identity, `numSYTenum l = dimHLF l` for every sorted positive `l`.

This was the load-bearing target flagged when the file carried its cited `sorry`: with it proved,
the abstract RSK/Burnside statement `RSKBurnsideHolds n` (`Σ_p dimSYT(p)² = n!`) becomes a
**computable** statement in `dimHLF` (`rskBurnsideHolds_iff_dimHLF` below), connecting the
`decide`-verified `n ≤ 12` `dimHLF` Plancherel data to the genuine `#SYT` count.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open QOU.BraidKnot.IdentityI

/-- **Hook-length bridge (proved).**  The genuine SYT count equals the Frame–Robinson–Thrall
hook-length dimension of the partition's (weakly-decreasing) row-length list — the hook-length
formula `#SYT(λ) = n!/∏_c h_c`.  Composition of the counting bridge
`SYTEnum.dimSYT_eq_numSYTenum` with the general HLF `SYTEnum.numSYTenum_eq_dimHLF`
(GNW corner recursion; positivity of the parts is `Nat.Partition.parts_pos`). -/
theorem dimSYT_eq_dimHLF {n : ℕ} (p : Nat.Partition n) :
    dimSYT p = dimHLF (p.parts.sort (· ≥ ·)) :=
  (SYTEnum.dimSYT_eq_numSYTenum p).trans
    (SYTEnum.numSYTenum_eq_dimHLF _ (Multiset.sort_sorted _ _)
      fun _a ha => p.parts_pos (by rwa [← Multiset.mem_coe, Multiset.sort_eq] at ha))

/-- The RSK/Burnside sum over the genuine SYT counts equals the same sum over the computable
hook-length dimensions — `dimSYT_eq_dimHLF` applied under `Σ_p`. -/
theorem sum_dimSYT_sq_eq_sum_dimHLF_sq (n : ℕ) :
    ∑ p : Nat.Partition n, (dimSYT p) ^ 2
      = ∑ p : Nat.Partition n, (dimHLF (p.parts.sort (· ≥ ·))) ^ 2 :=
  Finset.sum_congr rfl fun p _ => by rw [dimSYT_eq_dimHLF]

/-- **`RSKBurnsideHolds` is now a computable statement.**  The abstract RSK/Burnside identity
`Σ_{p ⊢ n} dimSYT(p)² = n!` (a sum of noncomputable `Nat.card`s) holds iff the corresponding
`dimHLF` sum does — the form the `decide`-verified `n ≤ 12` Plancherel data
(`IdentityIContentDecomposition.dim_validated_le12`, over the `partitionsOf` list enumerator)
computes.  Discharging `RSKBurnsideHolds n` from that list-model data now needs only the
`Nat.Partition n ↔ partitionsOf n` enumeration bridge, not any SYT structure theory. -/
theorem rskBurnsideHolds_iff_dimHLF (n : ℕ) :
    RSKBurnsideHolds n ↔
      ∑ p : Nat.Partition n, (dimHLF (p.parts.sort (· ≥ ·))) ^ 2 = n.factorial := by
  unfold RSKBurnsideHolds
  rw [sum_dimSYT_sq_eq_sum_dimHLF_sq]

end QOU.Mathlib
