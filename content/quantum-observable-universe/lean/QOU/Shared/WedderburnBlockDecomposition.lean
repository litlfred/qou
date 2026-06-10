import Mathlib.Data.Real.Basic

/-!
# QOU.Shared.WedderburnBlockDecomposition — shared context for Wedderburn-block claims

A *Wedderburn-block claim* is any proposition that bundles:
- A coefficient ring `R` (generic / `ℝ` / `ℂ` per §7c)
- A semisimple algebra `A` (typically Hecke at generic `q`)
- A partition indexing `λ ⊢ n` of the central idempotents
- Per-block dimensions `d_λ` and / or `q`-deformed dimensions `dim_q(λ)`
- The block weights `w_λ = (dim_q(λ))² / [n]_q!`

Per `local/lean-substantive-pass`, ~15 blocks share this shape
(Wenzl bridge / Plancherel weight / spectral decomposition /
isotypic projection content).

**Usage**:

```lean
class MyWedderburnClaim extends QOU.Shared.WedderburnBlockDecompositionContext where
  claim_partition_specific :
    w_tilde my_partition = 3 / 14
```

-- Ref: [manuscript] braids-and-knots/wedderburn-weight-canonical.md (shared)
-/

namespace QOU.Shared

universe u

/-- Shared context for any block whose claim involves Wedderburn-
    block decomposition of a semisimple algebra `A`. -/
class WedderburnBlockDecompositionContext where
  /-- The coefficient ring `R`. -/
  R : Type u
  /-- The strand count `n`. -/
  n : ℕ
  /-- Partition / Young-diagram indexing for irreps. -/
  PartitionIdx : Type
  /-- The classical block dimension `d_λ = dim V_λ`. -/
  d : PartitionIdx → ℕ
  /-- The `q`-deformed block dimension `dim_q(λ)`. -/
  dim_q : PartitionIdx → ℝ
  /-- The classical Plancherel weight `w_λ = d_λ² / n!`. -/
  w : PartitionIdx → ℝ
  /-- The `q`-deformed Wedderburn-block weight
      `w̃_λ = dim_q(λ)² / [n]_q!`. -/
  w_tilde : PartitionIdx → ℝ

end QOU.Shared
