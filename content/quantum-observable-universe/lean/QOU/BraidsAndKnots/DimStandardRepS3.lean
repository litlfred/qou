import QOU.MathlibExt.QPartitionCombinatorics

/-!
# Dimension of the Standard Representation V_{(2,1)} of S₃

The irreducible representation V_{(2,1)} of the symmetric group S₃
has classical dimension 2, computed via the Frame–Robinson–Thrall
hook-length formula:

  dim V_λ = n! / ∏_{(i,j) ∈ λ} hook(i,j)

For λ = (2,1) ⊢ 3:
  - Cells: (0,0), (0,1), (1,0)
  - Hook lengths: h(0,0) = 3, h(0,1) = 1, h(1,0) = 1
  - Hook product = 3 × 1 × 1 = 3
  - dim = 3! / 3 = 6 / 3 = 2

## Significance for the proton mass identity

Per `docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md`,
the factor "2" in the substrate identity

  m_p = 2 · m_μ · F_Bor(q₀) − 12 · m_e

equals dim V_{(2,1)}: the classical dimension of the standard
(trace-dominant) S₃ irrep that contributes 49% of the proton's
Wedderburn T1 trustable trace.

## References

-- Ref: [manuscript] Frame–Robinson–Thrall hook-length formula (1954)
-- Ref: [manuscript] James–Kerber, The Representation Theory of the Symmetric Group (1981)
-/

namespace QOU.BraidsAndKnots

open QOU.MathlibExt.QPartitionCombinatorics

/-! ## Hook-length computations for (2,1) ⊢ 3 -/

/-- Hook length at cell (0,0) of partition [2,1] is 3. -/
theorem hookLength_21_00 : Partition.hookLength [2, 1] 0 0 = 3 := by decide

/-- Hook length at cell (0,1) of partition [2,1] is 1. -/
theorem hookLength_21_01 : Partition.hookLength [2, 1] 0 1 = 1 := by decide

/-- Hook length at cell (1,0) of partition [2,1] is 1. -/
theorem hookLength_21_10 : Partition.hookLength [2, 1] 1 0 = 1 := by decide

/-! ## Computable classical dimension via hook-length formula -/

/-- Product of all hook lengths in a partition λ. -/
def hookProduct (lam : Partition) : ℕ :=
  (List.range lam.length).foldl
    (fun acc i =>
      acc * (List.range ((lam.get? i).getD 0)).foldl
        (fun a j => a * Partition.hookLength lam i j) 1) 1

/-- Classical dimension of the irrep V_λ of S_n:
    `dim V_λ = n! / ∏_{cells} hook(cell)`. -/
def classicalDim (lam : Partition) : ℕ :=
  Nat.factorial (Partition.size lam) / hookProduct lam

/-- The hook product of partition (2,1) is 3. -/
theorem hookProduct_21 : hookProduct [2, 1] = 3 := by decide

/-- **dim V_{(2,1)} = 2** — the classical dimension of the standard
    irrep of S₃ indexed by the partition (2,1).

    This is the factor "2" in the proton substrate identity
    `m_p = dim V_{(2,1)} · m_μ · F_Bor(q₀) − 12 · m_e`. -/
-- Ref: [manuscript] Frame–Robinson–Thrall hook-length formula (1954)
theorem dim_V_21_eq_two : classicalDim [2, 1] = 2 := by decide

/-! ## Cross-checks: all partitions of 3 -/

/-- dim V_{(3)} = 1 — the trivial (symmetric) representation. -/
theorem dim_V_3_eq_one : classicalDim [3] = 1 := by decide

/-- dim V_{(1,1,1)} = 1 — the sign (alternating) representation. -/
theorem dim_V_111_eq_one : classicalDim [1, 1, 1] = 1 := by decide

/-- Dimension check: dim V_{(3)} + dim V_{(2,1)} + dim V_{(1,1,1)} = 1 + 2 + 1 = 4.

    This does NOT equal 3! = 6 because the Burnside formula is
    `Σ_λ (dim V_λ)² = n!`, i.e. 1² + 2² + 1² = 6 = 3!. -/
theorem burnside_S3 :
    classicalDim [3] ^ 2 + classicalDim [2, 1] ^ 2 + classicalDim [1, 1, 1] ^ 2 =
      Nat.factorial 3 := by decide

end QOU.BraidsAndKnots
