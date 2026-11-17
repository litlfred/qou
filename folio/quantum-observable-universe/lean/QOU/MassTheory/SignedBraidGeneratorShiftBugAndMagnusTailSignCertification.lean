/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Signed Braid Generator Shift Defect and $A=4$ Banked-Partition Sign Certification

Formalizes two linked structural diagnostics in multi-nucleon braid words and $A=4$ evaluation:

1. **Signed Braid Generator Shift Defect in Multi-Nucleon Words (`qou-yaqm`)**:
   - Shifting a signed braid generator $g \ne 0$ by a strand offset $k > 0$ via the naive
     formula $\text{naiveBraidShift}(g, k) = g + k$ maps negative generators $g = -2$ at
     $k = 3$ to $-2 + 3 = +1$, flipping the crossing sign from $-1$ to $+1$ (adding $+2$
     to the writhe per negative letter, and $+8$ across the $4$ negative letters of the
     deuteron's second nucleon: $9 + 8 = 17$) and failing to reach generator index $5$.
   - The sign-preserving shift $\text{signPreservingBraidShift}(g, k)$ maps $g = -2, k = 3$
     to $-5$, preserving crossing sign $-1$, writhe $9$, and top generator index $5$ on $6$ strands.

2. **$A=4$ Heavy-Partition Tail Bound and Negative Sign Certification (`qou-z9xt`)**:
   - At $A = 4$ ($n = 12$, $p(12) = 77$ partitions), banking $48$ partitions leaves
     $77 - 48 = 29$ heavy partitions (dimensions up to $7700$) with banked sum
     $P_{\text{banked}} = -105757211820$.
   - Whenever the unbanked tail $P_{\text{tail}}$ satisfies $-R \le P_{\text{tail}} \le R$
     with $1000 R < -P_{\text{banked}}$ ($< 0.1\%$ tail bound), the exact total
     $P_{\text{exact}} = P_{\text{banked}} + P_{\text{tail}}$ is strictly negative
     ($P_{\text{exact}} < 0$) and retains over $99.9\%$ of the banked magnitude.
-/

namespace QOU.MassTheory.SignedBraidGeneratorShiftBugAndMagnusTailSignCertification

/-- Naive generator offset $g + k$ that drops the sign of negative braid letters. -/
def naiveBraidShift (g k : Int) : Int :=
  g + k

/-- Sign-preserving generator offset $\text{sign}(g) \cdot (|g| + k)$ for $k > 0$. -/
def signPreservingBraidShift (g k : Int) : Int :=
  if 0 < g then g + k else g - k

/-- Crossing sign $+1$ for positive braid letters and $-1$ for non-positive braid letters. -/
def crossingSign (g : Int) : Int :=
  if 0 < g then 1 else -1

/-- Absolute generator strand index $|g|$. -/
def generatorStrandIndex (g : Int) : Int :=
  if 0 ≤ g then g else -g

/-- Unbanked partition count $\text{total} - \text{banked}$. -/
def unbankedPartitionCount (totalPartitions bankedPartitions : Int) : Int :=
  totalPartitions - bankedPartitions

/-- Exact partition sum $P_{\text{banked}} + P_{\text{tail}}$. -/
def exactPartitionSum (pBanked pTail : Int) : Int :=
  pBanked + pTail

/-- Naive braid shift on $g = -2, k = 3$ flips crossing sign from $-1$ to $+1$, inflates
    deuteron writhe by $4 \times 2 = 8$ ($9 \to 17$), and reaches strand index $1$ instead
    of $5$ (`qou-yaqm`). -/
theorem naive_braid_shift_flips_negative_crossing_sign_and_misses_top_strand :
    naiveBraidShift (-2) 3 = 1 ∧
      signPreservingBraidShift (-2) 3 = -5 ∧
      crossingSign (naiveBraidShift (-2) 3) = 1 ∧
      crossingSign (signPreservingBraidShift (-2) 3) = -1 ∧
      generatorStrandIndex (signPreservingBraidShift (-2) 3) = 5 ∧
      9 + 4 * (crossingSign (naiveBraidShift (-2) 3) -
        crossingSign (signPreservingBraidShift (-2) 3)) = 17 := by
  dsimp [naiveBraidShift, signPreservingBraidShift, crossingSign, generatorStrandIndex]
  refine ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- Banking $48$ of $77$ partitions at $A = 4$ ($29$ unbanked) with $P_{\text{banked}} < 0$
    and tail bound $1000 R < -P_{\text{banked}}$ deterministically locks $P_{\text{exact}} < 0$
    and preserves over $99.9\%$ of the magnitude (`qou-z9xt`). -/
theorem banked_forty_eight_partitions_lock_negative_sign_under_tail_bound
    (pBanked pTail tailBound : Int)
    (hBanked : pBanked = -105757211820)
    (hLower : -tailBound ≤ pTail) (hUpper : pTail ≤ tailBound)
    (hSmall : 1000 * tailBound < -pBanked) :
    unbankedPartitionCount 77 48 = 29 ∧
      exactPartitionSum pBanked pTail < 0 ∧
      pBanked - tailBound ≤ exactPartitionSum pBanked pTail ∧
      exactPartitionSum pBanked pTail ≤ pBanked + tailBound ∧
      999 * (-pBanked) < 1000 * (-exactPartitionSum pBanked pTail) := by
  dsimp [unbankedPartitionCount, exactPartitionSum]
  have hneg : pBanked + pTail < 0 := by omega
  have hlo : pBanked - tailBound ≤ pBanked + pTail := by omega
  have hhi : pBanked + pTail ≤ pBanked + tailBound := by omega
  have h999 : 999 * (-pBanked) < 1000 * (-(pBanked + pTail)) := by omega
  exact ⟨rfl, hneg, hlo, hhi, h999⟩

end QOU.MassTheory.SignedBraidGeneratorShiftBugAndMagnusTailSignCertification
