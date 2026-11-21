import QOU.BraidKnot.KeystoneN5ValueMapRigidity
import QOU.BraidKnot.KeystoneHabiroInfiniteRigidity

/-!
# Level 6 suffices for the `n = 5` blocks — the mark-6 block is `[5]+1`, not `[6]`

Bean `bwsc`, under parent `bws0`. That bean sets the WRT obligation at level `N ≥ 7`,
by the reasoning *"max mark-6 ⇒ degree 5 in `t`, so need ≥ 6 distinct fibre points"*.
**The premise is wrong**, and the corpus already contains the counter-value.

`KeystoneWLambdaContinuation.block_dims_explicit` gives the four blocks as

```
d((5))     = 1                    d((4,1))   = t³ − 2t
d((3,2))   = t⁴ − 3t² + 1         d((3,1,1)) = t⁴ − 3t² + 2
```

The mark-6 block is `d((3,1,1)) = [5] + 1`, the A₅-split `3 ⊕ 3′` signature — **not**
`[6] = t⁵ − 4t³ + 3t`. The two agree at `t = 2` (both `6`, which is what "mark 6"
names) and are different polynomials, of degree `4` and `5`. `mark_six_block_is_not_qi_six`
exhibits exactly that: equal at `t = 2`, unequal as polynomials.

So the maximum degree over the four blocks is `4`, not `5`; five distinct points
suffice; and the level-`N` fibre supplies `N − 1` of them. **`N = 6` closes the
`n = 5` case**, and the level-7 instance in `KeystoneN5ValueMapRigidity` is one root
more than the mathematics needs. That is a strictly smaller obligation on the still-open
half of `bwsc` — the WRT = modular-data agreement itself, of which
`KeystoneLRAmplitudeReal` (#4365) supplies the `Σ(2,3,5)` slice.

## The bracket is now tight

`KeystoneHabiroInfiniteRigidity.two_roots_insufficient` brackets `bwsc` from below with
`2`. The sharp statement is `no_finite_root_set_suffices`: **without a degree bound no
finite set of roots suffices at all**, for the same reason and with the same one-line
witness `V + ∏_{s ∈ S}(X − s)`. Two was not special.

With the measured degree bound the bracket closes exactly: `four_roots_insufficient`
(a corollary) fails at four, `muon_block_pinned_level6` succeeds at five. Five is the
threshold, not a sufficient-but-unsharp count.

## The degree hypothesis is removable, and had never been removed here

Bean `bwsd` was dissolved on 2026-08-01: `eq_of_habiro_root_agreement` uses the
**infinite** fibre-root family, so agreement at all roots forces equality with no
degree bound. That lemma has **no consumers** anywhere in the corpus, and the concrete
`n = 5` theorems still carry `hbw : bwPoly.natDegree < 6` — the very hypothesis the
dissolution removes. `muon_block_pinned_all_roots` and `electron_block_pinned_all_roots`
are that wiring.

The two forms are a genuine trade, not a strict improvement, and neither dominates:
the level-6 form asks for agreement at **five roots of one level**; the all-roots form
asks for agreement at **one root of every level** and pays no degree. Which is cheaper
depends on what WRT actually supplies, which is `bwsc` and is open.

## Honest scope (STRICT)

Nothing here proves the gauge row `bwS0` agrees with the value map at any root. That is
`bwsc` and it stays open; what changes is its *price* — five roots at level 6 rather
than six at level 7, or none at all if the all-levels family is available instead. No
fit; nothing wired; L2 unchanged.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-- Ref: [habiro2004] https://doi.org/10.1007/s00222-007-0071-0
-/

namespace QOU.BraidKnot.KeystoneN5LevelSixSuffices

open Polynomial Real
open QOU.BraidKnot.KeystoneN5ValueMapRigidity
open QOU.BraidKnot.KeystoneHabiroRootFamily

/-! ### The premise of `bwsc`'s level count is false -/

/-- `[6]` as a Chebyshev polynomial in the fold variable: `t⁵ − 4t³ + 3t`, degree `5`. -/
noncomputable def qiSix : ℝ[X] := X ^ 5 - 4 * X ^ 3 + 3 * X

/-- **The mark-6 block is not `[6]`.**

`d((3,1,1)) = [5] + 1` and `[6]` take the same value `6` at `t = 2` — which is what the
mark names — and are different polynomials. Reading the mark as an index into the
quantum integers is what puts a degree-`5` block in the `n = 5` list, and there is
none. -/
theorem mark_six_block_is_not_qi_six :
    poly311.eval 2 = qiSix.eval 2 ∧ poly311 ≠ qiSix := by
  constructor
  · simp [poly311, qiSix]; norm_num
  · intro h
    have h4 : poly311.natDegree = 4 := natDegree_poly311
    have h5 : qiSix.natDegree = 5 := by unfold qiSix; compute_degree!
    rw [h] at h4
    omega

/-- **The four `n = 5` block degrees are `< 5`**, not merely `< 6`.

Sharpens `KeystoneN5ValueMapRigidity.n5_degrees_lt_six`, whose bound was chosen to
match the six level-7 fold points rather than the polynomials. -/
theorem n5_degrees_lt_five :
    vacPoly.natDegree < 5 ∧ poly41.natDegree < 5 ∧ poly32.natDegree < 5
      ∧ poly311.natDegree < 5 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold vacPoly; rw [natDegree_one]; norm_num
  · rw [natDegree_poly41]; norm_num
  · rw [natDegree_poly32]; norm_num
  · rw [natDegree_poly311]; norm_num

/-! ### Level 6 pins the physical blocks -/

/-- **The muon block is pinned by level-6 root agreement.**

Five fold points `2cos(kπ/6)`, `k = 1..5`, against a degree-`< 5` gauge row. One root
fewer than `KeystoneN5ValueMapRigidity.muon_block_pinned_level7`, and one level lower,
which is a strictly weaker demand on the open WRT agreement. -/
theorem muon_block_pinned_level6
    (bwPoly : ℝ[X]) (hbw : bwPoly.natDegree < 5)
    (hagree : ∀ k ∈ Finset.Icc 1 5,
      bwPoly.eval (foldValue 6 k) = poly32.eval (foldValue 6 k)) :
    bwPoly = poly32 :=
  eq_of_root_family_agreement bwPoly poly32 6 (by norm_num) (by simpa using hbw)
    (by rw [natDegree_poly32]; norm_num) (by simpa using hagree)

/-- **The electron block is pinned by level-6 root agreement** — same instance for
`d((3,1,1)) = t⁴ − 3t² + 2`. -/
theorem electron_block_pinned_level6
    (bwPoly : ℝ[X]) (hbw : bwPoly.natDegree < 5)
    (hagree : ∀ k ∈ Finset.Icc 1 5,
      bwPoly.eval (foldValue 6 k) = poly311.eval (foldValue 6 k)) :
    bwPoly = poly311 :=
  eq_of_root_family_agreement bwPoly poly311 6 (by norm_num) (by simpa using hbw)
    (by rw [natDegree_poly311]; norm_num) (by simpa using hagree)

/-! ### The lower bracket, sharp

    `KeystoneHabiroInfiniteRigidity.two_roots_insufficient` is not about the number
    two. -/

/-- **No finite set of roots suffices without a degree bound.**

For any finite `S` and any value map `V`, the polynomial `V + ∏_{s ∈ S}(X − s)` differs
from `V` and agrees with it on all of `S`. So a finite root family can only ever pin the
gauge row *together with* a degree hypothesis — which is precisely why `bwsd`'s
dissolution had to go through the infinite family rather than a bigger finite one. -/
theorem no_finite_root_set_suffices (S : Finset ℝ) (V : ℝ[X]) :
    ∃ W : ℝ[X], W ≠ V ∧ ∀ x ∈ S, W.eval x = V.eval x := by
  refine ⟨V + ∏ s ∈ S, (X - C s), ?_, ?_⟩
  · intro hWV
    have hP : (∏ s ∈ S, (X - C s)) = 0 := by linear_combination hWV
    have hne : (∏ s ∈ S, (X - C s)) ≠ (0 : ℝ[X]) :=
      Finset.prod_ne_zero_iff.mpr fun s _ => X_sub_C_ne_zero s
    exact hne hP
  · intro x hx
    have : (∏ s ∈ S, (X - C s)).eval x = 0 := by
      rw [eval_prod]
      exact Finset.prod_eq_zero hx (by simp)
    rw [eval_add, this, add_zero]

/-- **Four roots are not enough**, so five is the threshold rather than merely a
sufficient count: with the measured degree bound `< 5`, `muon_block_pinned_level6`
closes at five and this fails at four. -/
theorem four_roots_insufficient (S : Finset ℝ) (hS : S.card = 4) (V : ℝ[X]) :
    ∃ W : ℝ[X], W ≠ V ∧ ∀ x ∈ S, W.eval x = V.eval x :=
  no_finite_root_set_suffices S V

/-! ### The degree hypothesis, dropped -/

/-- **The muon block, pinned with no degree hypothesis at all.**

Agreement across the full fibre-root family `2cos(π/(N+2))` forces equality outright.
This is `bwsd`'s dissolution applied to a concrete physical block —
`eq_of_habiro_root_agreement` had no consumer anywhere in the corpus, and the `n = 5`
theorems went on carrying the hypothesis it removes. -/
theorem muon_block_pinned_all_roots (bwPoly : ℝ[X])
    (h : ∀ N : ℕ, bwPoly.eval (2 * Real.cos (π / ((N : ℝ) + 2)))
      = poly32.eval (2 * Real.cos (π / ((N : ℝ) + 2)))) :
    bwPoly = poly32 :=
  KeystoneHabiroInfiniteRigidity.eq_of_habiro_root_agreement bwPoly poly32 h

/-- **The electron block, pinned with no degree hypothesis at all.** -/
theorem electron_block_pinned_all_roots (bwPoly : ℝ[X])
    (h : ∀ N : ℕ, bwPoly.eval (2 * Real.cos (π / ((N : ℝ) + 2)))
      = poly311.eval (2 * Real.cos (π / ((N : ℝ) + 2)))) :
    bwPoly = poly311 :=
  KeystoneHabiroInfiniteRigidity.eq_of_habiro_root_agreement bwPoly poly311 h

end QOU.BraidKnot.KeystoneN5LevelSixSuffices
