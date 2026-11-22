import Mathlib.Algebra.Field.Basic

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

**Base ring (§7c).** The Wedderburn-block data are rational functions
of `q` over the coefficient field (`ℚ(q)`, generically): the `q`-deformed
dimension `dim_q(λ)`, the classical Plancherel weight `w_λ = d_λ²/n!`,
and the `q`-deformed weight `w̃_λ = dim_q(λ)²/[n]_q!` are all algebraic.
The context is therefore parameterised over a **generic field**
`(R : Type*) [Field R]` rather than specialised to `ℝ`; the
substrate→archimedean evaluation at `q₀ ∈ ℝ` happens at the
instantiation site `(R := ℝ)`, never in this shared shape.

**Usage**:

```lean
class MyWedderburnClaim (R : Type*) [Field R]
    extends QOU.Shared.WedderburnBlockDecompositionContext R where
  claim_partition_specific :
    w_tilde my_partition = 3 / 14
```

-- Ref: [leitner2026] braids-and-knots/wedderburn-weight-canonical.md (shared)
-/

namespace QOU.Shared

/-- Shared context for any block whose claim involves Wedderburn-
    block decomposition of a semisimple algebra `A`, over a generic
    coefficient field `R` (§7c). -/
class WedderburnBlockDecompositionContext (R : Type*) [Field R] where
  /-- The strand count `n`. -/
  n : ℕ
  /-- Partition / Young-diagram indexing for irreps. -/
  PartitionIdx : Type
  /-- The classical block dimension `d_λ = dim V_λ`. -/
  d : PartitionIdx → ℕ
  /-- The `q`-deformed block dimension `dim_q(λ)`. -/
  dim_q : PartitionIdx → R
  /-- The classical Plancherel weight `w_λ = d_λ² / n!`. -/
  w : PartitionIdx → R
  /-- The `q`-deformed Wedderburn-block weight
      `w̃_λ = dim_q(λ)² / [n]_q!`. -/
  w_tilde : PartitionIdx → R

end QOU.Shared
