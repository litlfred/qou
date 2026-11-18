/-
Copyright (c) 2026 litlfred. All rights reserved.

# The n=5 value map is pinned by level-7 root-family agreement (chips bwsc + bwsd)

Instantiates the abstract root-family rigidity
(`KeystoneHabiroRootFamily.eq_of_root_family_agreement`) for the **concrete `n = 5`
physical blocks** of the W_λ keystone.  Two chips toward the full closure of
`bwS0_eq_hecke` (bean `bws0`):

* **bwsd (bounded degree):** the value-map polynomials in the fold variable `t` are
  explicit and of degree `≤ 4` — `d((5)) = 1`, `d((4,1)) = t³−2t`,
  `d((3,2)) = t⁴−3t²+1`, `d((3,1,1)) = t⁴−3t²+2` (from `KeystoneWLambdaContinuation`,
  `block_dims_explicit`).  Their `natDegree`s are computed here.
* **bwsc (which level suffices):** since every block polynomial has degree `≤ 4 < 6`,
  agreement of a candidate gauge-row polynomial with the value map across the
  **level-7 fibre roots** (the 6 fold points `2cos(kπ/7)`, `k = 1..6`) already pins
  it — the concrete instance of `eq_of_root_family_agreement` at `N = 7`.

So the residual open content of `bwS0_eq_hecke` for the `n = 5` blocks is exactly:
*does the gauge row `bwS0` agree with the value map at the 6 level-7 roots, and is it
a degree-`< 6` polynomial?* — the WRT=modular-data agreement (bwsc) + Habiro
bounded-degree (bwsd), of which `KeystoneLRAmplitudeReal` (#4365) supplies the
`Σ(2,3,5)` slice.

**Honest scope (STRICT).** Concretises *which* rigidity instance closes the `n = 5`
case; it does **not** prove the gauge row satisfies the hypotheses.  No fit; nothing
wired; L2 unchanged.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneHabiroRootFamily
import Mathlib.Tactic.ComputeDegree

namespace QOU.BraidKnot.KeystoneN5ValueMapRigidity

open Polynomial KeystoneHabiroRootFamily

/-- Value-map polynomial of the vacuum block `(5)`: `d = [1] = 1`. -/
noncomputable def vacPoly : ℝ[X] := 1

/-- Value-map polynomial of `(4,1)`: `d = [4] = t³ − 2t`. -/
noncomputable def poly41 : ℝ[X] := X ^ 3 - 2 * X

/-- Value-map polynomial of the muon block `(3,2)`: `d = [5] = t⁴ − 3t² + 1`. -/
noncomputable def poly32 : ℝ[X] := X ^ 4 - 3 * X ^ 2 + 1

/-- Value-map polynomial of the electron block `(3,1,1)`: `d = [5]+1 = t⁴ − 3t² + 2`. -/
noncomputable def poly311 : ℝ[X] := X ^ 4 - 3 * X ^ 2 + 2

/-! ### bwsd — the value-map polynomial degrees are bounded (`≤ 4`) -/

theorem natDegree_poly41 : poly41.natDegree = 3 := by
  unfold poly41; compute_degree!

theorem natDegree_poly32 : poly32.natDegree = 4 := by
  unfold poly32; compute_degree!

theorem natDegree_poly311 : poly311.natDegree = 4 := by
  unfold poly311; compute_degree!

/-- Every `n = 5` value-map polynomial has degree `< 6` (`= 7 − 1`), the count of
level-7 fold points. -/
theorem n5_degrees_lt_six :
    vacPoly.natDegree < 6 ∧ poly41.natDegree < 6 ∧ poly32.natDegree < 6
      ∧ poly311.natDegree < 6 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold vacPoly; rw [natDegree_one]; norm_num
  · rw [natDegree_poly41]; norm_num
  · rw [natDegree_poly32]; norm_num
  · rw [natDegree_poly311]; norm_num

/-! ### bwsc — level-7 agreement pins each block's value map -/

/-- **The muon block is pinned by level-7 root agreement.** A degree-`< 6` gauge-row
polynomial agreeing with the muon value map `d((3,2)) = t⁴−3t²+1` at the six level-7
fold points `2cos(kπ/7)` (`k = 1..6`) equals it identically — hence at the substrate
`t₀`.  The concrete `n = 5`, `N = 7` instance of `eq_of_root_family_agreement`. -/
theorem muon_block_pinned_level7
    (bwPoly : ℝ[X]) (hbw : bwPoly.natDegree < 6)
    (hagree : ∀ k ∈ Finset.Icc 1 6,
      bwPoly.eval (foldValue 7 k) = poly32.eval (foldValue 7 k)) :
    bwPoly = poly32 := by
  have h := eq_of_root_family_agreement bwPoly poly32 7 (by norm_num) (by simpa using hbw)
    (by rw [natDegree_poly32]; norm_num) (by simpa using hagree)
  exact h

/-- **The electron block is pinned by level-7 root agreement** — same instance for
`d((3,1,1)) = t⁴−3t²+2`. -/
theorem electron_block_pinned_level7
    (bwPoly : ℝ[X]) (hbw : bwPoly.natDegree < 6)
    (hagree : ∀ k ∈ Finset.Icc 1 6,
      bwPoly.eval (foldValue 7 k) = poly311.eval (foldValue 7 k)) :
    bwPoly = poly311 := by
  have h := eq_of_root_family_agreement bwPoly poly311 7 (by norm_num) (by simpa using hbw)
    (by rw [natDegree_poly311]; norm_num) (by simpa using hagree)
  exact h

/-- Subtracting the target polynomial from a bounded-degree polynomial agreeing at six level-seven fold points yields the zero polynomial. -/
theorem muon_block_pinned_level7_sub_eq_zero
    (bwPoly : ℝ[X]) (hbw : bwPoly.natDegree < 6)
    (hagree : ∀ k ∈ Finset.Icc 1 6,
      bwPoly.eval (foldValue 7 k) = poly32.eval (foldValue 7 k)) :
    bwPoly - poly32 = 0 := by
  rw [muon_block_pinned_level7 bwPoly hbw hagree, sub_self]

end QOU.BraidKnot.KeystoneN5ValueMapRigidity
