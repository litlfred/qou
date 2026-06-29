import QOU.Mathlib.SYTBetaLagrange

/-!
# QOU.Mathlib.SYTGnwHookClosure — closing `SYTHookGNW.gnwHookIdentity` (WIP scaffold)

`SYTHookGNW.gnwHookIdentity` (`∑_{corners c} prodHooks(l)/prodHooks(l∖c) = sz l`) is the sole
remaining gap of the GNW route to the SYT hook-length formula.  This file collects the **β-Lagrange
side** building blocks for its closure; the full reduction is:

Let `β = betaVec l` (`βᵢ = l[i] + (k−1−i)`, distinct, antitone).  `SYTBetaLagrange.betaLagrange`
already proves, sorry-free,

    ∑_{i : Fin k} βᵢ · ∏_{j≠i}(βᵢ − 1 − βⱼ) / vWeight βᵢ = (∑ⱼ βⱼ) − C(k,2) = sz l   (`sum_betaVec_sub`).

The closure has three steps:

1. **Per-corner ratio = β-Lagrange term** (`per_corner_ratio`, the remaining gap).  For a corner `c`,
   `prodHooks(l)/prodHooks(l∖c) = βc · ∏_{j≠c}(βc − 1 − βj) / vWeight βc`.  Via the proved
   `prodHooks_mul_betaProdGap` (`prodHooks · betaProdGap = betaFactProd`) and the casts
   `betaProdGap_cast` / `betaFactProd_cast`, this reduces to: the factorial side contributes `βc`
   (`betaFactProd(l)/betaFactProd(l∖c) = βc`), and the Vandermonde side contributes the lower-and-upper-
   triangular split product handled by `wall_split` below.  The **row-drop corner** (`l[c]=1`, the last
   row vanishes, `k → k−1`, every `β` shifts by `−1`) needs separate handling — the heavy combinatorial
   `betaVec ∘ removeCorner` step.  *(open: the documented multi-session core.)*

2. **Non-corner terms vanish** (`betaLagrange_term_zero`, proved below).  At a non-corner row `i`
   (`l[i] = l[i+1]`, no strict descent), `βᵢ − 1 = β_{i+1}`, so the `j = i+1` factor of
   `∏_{j≠i}(βᵢ − 1 − βⱼ)` is `0`, killing the whole term.  Hence the β-Lagrange sum over `Fin k` equals
   the sum over corners only.

3. **Assembly**: `∑_{corners} prodHooks-ratio = ∑_{corners} β-Lagrange-term = ∑_{Fin k} β-Lagrange-term
   = sz l` (steps 1 + 2 + `betaLagrange` + `sum_betaVec_sub`).

Steps 2 and the algebraic core of step 1 are proved here, sorry-free.  Pure `ℚ` combinatorics; nothing
archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Finset

variable {k : ℕ}

/-- **The Vandermonde-ratio split (algebraic core of step 1).**  The lower-and-upper-triangular factors of
`betaProdGap(l∖c)/betaProdGap(l)` reassemble the β-Lagrange numerator's denominator-paired product:

    (∏_{i<c}(βᵢ − βc + 1)/(βᵢ − βc)) · (∏_{j>c}(βc − 1 − βj)/(βc − βj))
      = ∏_{j≠c}(βc − 1 − βj)/(βc − βj).

The `i < c` factors flip sign per-factor: `(βᵢ − βc + 1)/(βᵢ − βc) = (βc − 1 − βᵢ)/(βc − βᵢ)`
(cross-multiplying, both equal `−(βᵢ − βc)² − (βᵢ − βc)`).  Then `erase c = {<c} ⊔ {>c}` recombines. -/
theorem wall_split (β : Fin k → ℚ) (hβ : Function.Injective β) (c : Fin k) :
    (∏ i ∈ univ.filter (· < c), (β i - β c + 1) / (β i - β c))
      * (∏ j ∈ univ.filter (c < ·), (β c - 1 - β j) / (β c - β j))
      = ∏ j ∈ univ.erase c, (β c - 1 - β j) / (β c - β j) := by
  have hsplit : univ.erase c = univ.filter (· < c) ∪ univ.filter (c < ·) := by
    ext x
    simp only [mem_erase, mem_univ, and_true, true_and, mem_union, mem_filter]
    constructor
    · intro hx; rcases lt_or_gt_of_ne hx with h | h
      · exact Or.inl h
      · exact Or.inr h
    · rintro (h | h)
      · exact ne_of_lt h
      · exact ne_of_gt h
  have hdis : Disjoint (univ.filter (· < c)) (univ.filter (c < ·)) := by
    rw [Finset.disjoint_left]; intro x h1 h2
    rw [mem_filter] at h1 h2; exact absurd (h1.2.trans h2.2) (lt_irrefl x)
  rw [hsplit, Finset.prod_union hdis]
  congr 1
  apply Finset.prod_congr rfl
  intro i hi
  rw [mem_filter] at hi
  have hne : β i ≠ β c := fun e => (ne_of_lt hi.2) (hβ e)
  have h1 : β i - β c ≠ 0 := sub_ne_zero.mpr hne
  have h2 : β c - β i ≠ 0 := sub_ne_zero.mpr (fun e => hne e.symm)
  field_simp
  ring

/-- **Non-corner vanishing (step 2).**  If `βᵢ − 1 = βⱼ` for some `j ≠ i` (the defining feature of a
non-corner row, where `l[i] = l[i+1]` forces `βᵢ − 1 = β_{i+1}`), the β-Lagrange summand at `i` is `0`:
the `j`-th factor of `∏_{j'≠i}(βᵢ − 1 − βⱼ')` vanishes. -/
theorem betaLagrange_term_zero (β : Fin k → ℚ) (i : Fin k)
    (j : Fin k) (hji : j ≠ i) (h : β i - 1 = β j) :
    β i * (∏ j' ∈ univ.erase i, (β i - 1 - β j')) / vWeight β i = 0 := by
  have hz : (∏ j' ∈ univ.erase i, (β i - 1 - β j')) = 0 := by
    apply Finset.prod_eq_zero (i := j)
    · rw [mem_erase]; exact ⟨hji, mem_univ j⟩
    · rw [h]; ring
  rw [hz]; simp

end QOU.Mathlib.SYTBetaLagrange
