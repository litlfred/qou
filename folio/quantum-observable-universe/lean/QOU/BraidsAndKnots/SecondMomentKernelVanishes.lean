import QOU.BraidsAndKnots.PlancherelNormalisation
import QOU.BraidKnot.PlancherelSnDataGeneral
import QOU.BraidKnot.SnIsotypicSpechtSplitInstance

/-!
# The dim²-weighted content-spread total vanishes, at every `k`

`secondMomentKernel k = Σ_{λ⊢k} (f^λ)²·ω₃(λ)` with `ω₃(λ) = Σ_□ c(□)² − binom(k,2)`. It is zero,
and the corpus said so — but only by `decide`, over `3 ≤ k ≤ 20`
(`YoungDiagramKernel.secondMomentKernel_eq_zero_of_le_twenty`).

That lemma's own docstring names what a general-`k` proof needs and why it was not available:

> what the `decide` supplies is a certified floor pending the general character-orthogonality
> proof, which needs the JM-eigenvalue ⇒ Plancherel-mean bridge (Sₙ representation-theory
> infrastructure, **not yet in the corpus**).

It is in the corpus now. That bridge is Identity (ii) — `2·Σ_λ dim(λ)²·(Σ_□ c(□)²) = k(k−1)·k!` —
which `identityB_general` proves from the Jucys–Murphy central element acting on the Wedderburn
blocks of `ℚ[S_k]`, exactly the three inputs the docstring lists (JM elements with their content
eigenvalues, centrality of `Σ_i X_i²`, and the regular-representation trace that carries the
column-orthogonality content). `PlancherelSnDataGeneral` states it over the row-length list model.

So the identity is arithmetic:

    secondMomentKernel k = Σ_λ f²·Σc²  −  binom(k,2)·Σ_λ f²
                         = k!·binom(k,2)  −  binom(k,2)·k!  =  0.

## What this unblocks

`ω₃`'s mean-zero leg is what carried the `k ≤ 20` cap through the pincer:
`tiltedMean_zero_of_le_twenty` is the *only* consumer of that bound in
`YoungDiagramTailFirstInstance.nuV_top_closed_form` and `nuV_top_nonneg`. Both are restated here
without it. The **kernel conjecture itself is untouched** — `kernelValue k ≤ 0` is the `dim³`-weighted
total, which lies outside the polynomial-function algebra and remains open; this is the `dim²` total,
which was never conjectural, only uncertified past `k = 20`.

Pure arithmetic on top of the two transported identities; nothing archimedean; no fit.
-/

namespace QOU.BraidsAndKnots.SecondMomentKernelVanishes

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.YoungDiagramTailFirstInstance
open QOU.BraidKnot

/-! ## The two encodings agree on the summand -/

/-- The kernel's content-square sum and Identity I's are the same function. The two definitions are
written identically, but elaborate differently — `contentSq` leaves the inner `List.range` coerced
`ℕ → ℤ` as a monadic bind, `sumSqContents` annotates the bound variable and maps directly — so they
are not `rfl`-equal. -/
theorem contentSq_eq_sumSqContents (l : List ℕ) :
    contentSq l = IdentityI.sumSqContents l := by
  unfold contentSq IdentityI.sumSqContents
  refine congrArg List.sum (List.map_congr_left fun i _ => ?_)
  simp only [bind_pure_comp, Functor.map, List.map_map]
  rfl

/-- The kernel's hook-length dimension and Identity I's are the same function on a sorted parts
list. Both are `#SYT`; this composes the two routes to it that the corpus already has. -/
theorem sytDim_eq_dimHLF (k : ℕ) (p : Nat.Partition k) :
    sytDim (p.parts.sort (· ≥ ·)) = IdentityI.dimHLF (p.parts.sort (· ≥ ·)) := by
  rw [← PlancherelNormalisation.numSYT_diagram_eq_sytDim k p,
    SpechtWedderburnLe12.numSYT_partitionEquiv, QOU.Mathlib.dimSYT_eq_dimHLF]

/-! ## Identity (ii) in the kernel's encoding -/

/-- **`Σ_{λ⊢k} (f^λ)²·Σ_□ c(□)² = k!·binom(k,2)`**, over `partsOf` / `sytDim` / `contentSq` —
`PlancherelSnDataGeneral.sum_partition_content_int` reindexed onto the kernel's enumerator. -/
theorem sum_sytDim_sq_contentSq (k : ℕ) :
    ∑ l ∈ (partsOf k).toFinset, contentSq l * (sytDim l : ℤ) ^ 2
      = (k.factorial : ℤ) * (k.choose 2 : ℤ) := by
  rw [PlancherelNormalisation.sum_toFinset_eq_sum_natPartition k
      (fun l => contentSq l * (sytDim l : ℤ) ^ 2),
    ← PlancherelSnDataGeneral.sum_partition_content_int k]
  exact Finset.sum_congr rfl fun p _ => by
    rw [sytDim_eq_dimHLF k p, contentSq_eq_sumSqContents]
    rfl

/-- The Plancherel normalisation in `ℤ`, for the same enumerator. -/
theorem sum_sytDim_sq_int (k : ℕ) :
    ∑ l ∈ (partsOf k).toFinset, (sytDim l : ℤ) ^ 2 = (k.factorial : ℤ) := by
  have hN := PlancherelNormalisation.sum_sytDim_sq_eq_factorial k
  calc ∑ l ∈ (partsOf k).toFinset, (sytDim l : ℤ) ^ 2
      = ((∑ l ∈ (partsOf k).toFinset, (sytDim l) ^ 2 : ℕ) : ℤ) := by push_cast; rfl
    _ = (k.factorial : ℤ) := by rw [hN]

/-! ## The vanishing -/

/-- **`Σ_{λ⊢k} (f^λ)²·ω₃(λ) = 0`, for every `k`.** No `decide`, no bound. -/
theorem secondMomentKernel_eq_zero (k : ℕ) : secondMomentKernel k = 0 := by
  have hnd : (partsOf k).Nodup :=
    QOU.BraidsAndKnots.YoungDiagramTransposeBridge.partsFuel_nodup k k k
  have hlist : secondMomentKernel k
      = ∑ l ∈ (partsOf k).toFinset, (sytDim l : ℤ) ^ 2 * omega3 k l := by
    rw [secondMomentKernel, List.sum_toFinset _ hnd]
  have hsplit : ∑ l ∈ (partsOf k).toFinset, (sytDim l : ℤ) ^ 2 * omega3 k l
      = (∑ l ∈ (partsOf k).toFinset, contentSq l * (sytDim l : ℤ) ^ 2)
        - ((k * (k - 1) / 2 : ℕ) : ℤ) * ∑ l ∈ (partsOf k).toFinset, (sytDim l : ℤ) ^ 2 := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun l _ => by rw [omega3]; ring
  have hchoose : ((k * (k - 1) / 2 : ℕ) : ℤ) = (k.choose 2 : ℤ) := by
    rw [Nat.choose_two_right]
  rw [hlist, hsplit, sum_sytDim_sq_contentSq k, sum_sytDim_sq_int k, hchoose]
  ring

/-- Past the old `decide` frontier: `k = 25` is out of reach of `interval_cases … decide` and is
an instantiation here. -/
example : secondMomentKernel 25 = 0 := secondMomentKernel_eq_zero 25

/-- **`mean_zero`, at every `k`** — `E₂[ω₃] = 0`, where the corpus had `3 ≤ k ≤ 20`. -/
theorem tiltedMean_zero (k : ℕ) : tiltedMean k 0 = 0 :=
  tiltedMean_zero_of_secondMomentKernel_eq_zero k (secondMomentKernel_eq_zero k)

/-! ## The caps this lifts

Both restate a `YoungDiagramTailFirstInstance` result with its `k ≤ 20` hypothesis deleted. The
proofs are the originals with `tiltedMean_zero_of_le_twenty` swapped for `tiltedMean_zero`; that
lemma was the only consumer of the bound in either. -/

/-- **The (TAIL) first instance: `ν_n ≥ 0`, for every `k ≥ 3`.** -/
theorem nuV_top_nonneg (k : ℕ) (hk : 3 ≤ k) : 0 ≤ nuV k k := by
  obtain ⟨r, rfl⟩ : ∃ r, k = r + 2 := ⟨k - 2, by omega⟩
  have hr : 1 ≤ r := by omega
  unfold nuV
  rw [tiltedMean_zero (r + 2), mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [top_mixedMoment_eq_hookShapes_sum (r + 2) (by omega)]
  refine div_nonneg ?_ (le_of_lt (tiltNorm_zero_pos (r + 2) (by omega)))
  have h6 := six_mul_top_numerator r
  have hpos : (0 : ℝ) ≤ 2 * ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) *
      (((2 * r).choose r : ℕ) : ℝ) := by
    have h1 : (0 : ℝ) ≤ (r : ℝ) - 1 := by
      have : (1 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
      linarith
    have h2 : (0 : ℝ) ≤ (r : ℝ) := Nat.cast_nonneg r
    have h3 : (0 : ℝ) ≤ (((2 * r).choose r : ℕ) : ℝ) := Nat.cast_nonneg _
    positivity
  linarith [h6, hpos]

/-- **The (TAIL) first instance in closed form, for every `r ≥ 1`**:
`ν_n = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`, `n = r + 2`. -/
theorem nuV_top_closed_form (r : ℕ) (hr : 1 ≤ r) :
    nuV (r + 2) (r + 2)
      = ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ)
          / (3 * (Nat.factorial (r + 2) : ℝ)) := by
  unfold nuV
  rw [tiltedMean_zero (r + 2), mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [top_mixedMoment_eq_hookShapes_sum (r + 2) (by omega),
    PlancherelNormalisation.tiltNorm_zero_eq_factorial (r + 2)]
  have h6 := six_mul_top_numerator r
  have hfac : (0 : ℝ) < (Nat.factorial (r + 2) : ℝ) := by
    have := Nat.factorial_pos (r + 2)
    exact_mod_cast this
  field_simp
  linarith [h6]

end QOU.BraidsAndKnots.SecondMomentKernelVanishes
