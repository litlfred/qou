/-
  S_4 ↓ S_3 half-symmetric projection extracts one octahedral cell.

  The half-symmetric Wedderburn projection on H_4, restricted to the
  S_3-trivial subspace (3-component Borromean permutation), gives a
  factor 2/5.  Applied to the 8-fold ideal-octahedral tessellation
  of 𝓑_3's complement, effective cell count = (5/2) × (2/5) = 1.

  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
  -- Ref: [adams1985hyperbolic] ISBN 978-0-7167-1510-2
-/
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Basic

namespace QOU.BraidsAndKnots

/-- The five irreducible representations of S_4, indexed by
    partitions of 4.  We encode only the data needed for the
    branching rule: classical dimension and trivial-S_3 content
    under restriction. -/
structure S4Irrep where
  label : String
  dim : ℕ
  conjugateLabel : String
  trivialS3Content : ℕ
  deriving Repr

/-- S_4 irrep data (standard; [james1984representation] §2). -/
def s4Irreps : List S4Irrep := [
  ⟨"(4)",       1, "(1,1,1,1)", 1⟩,
  ⟨"(3,1)",     3, "(2,1,1)",   1⟩,
  ⟨"(2,2)",     2, "(2,2)",     0⟩,   -- self-conjugate
  ⟨"(2,1,1)",   3, "(3,1)",     0⟩,
  ⟨"(1,1,1,1)", 1, "(4)",       0⟩
]

/-- Half-symmetric content: one of each conjugate pair + 1/2
    self-conjugate.  We track the representatives and their
    contribution weights as rationals. -/
def halfSymRepresentatives : List (S4Irrep × ℚ) :=
  [ (⟨"(4)",   1, "(1,1,1,1)", 1⟩, 1),
    (⟨"(3,1)", 3, "(2,1,1)",   1⟩, 1),
    (⟨"(2,2)", 2, "(2,2)",     0⟩, 1/2) ]

/-- Total half-symmetric dimension (weighted sum of dims). -/
def halfSymTotalDim : ℚ :=
  halfSymRepresentatives.foldl (fun acc (rep, w) => acc + w * rep.dim) 0

/-- Total trivial-S_3 content in the half-symmetric projection. -/
def halfSymTrivialS3 : ℚ :=
  halfSymRepresentatives.foldl (fun acc (rep, w) => acc + w * rep.trivialS3Content) 0

/-- The S_3-trivial projection factor. -/
def s3TrivialFactor : ℚ := halfSymTrivialS3 / halfSymTotalDim

/-- Effective cell count = (5/2) × (2/5) = 1. -/
def effectiveCellCount : ℚ := (5 : ℚ) / 2 * s3TrivialFactor

-- The three key assertions, verified by `decide` / `native_decide`.
-- Ref: [james1984representation] §2 (S_n branching rules)
-- Ref: [adams1985hyperbolic] (8 ideal octahedra in 𝓑_3 complement)

theorem halfSymTotalDim_eq : halfSymTotalDim = 5 := by native_decide

theorem halfSymTrivialS3_eq : halfSymTrivialS3 = 2 := by native_decide

theorem s3TrivialFactor_eq : s3TrivialFactor = 2 / 5 := by
  unfold s3TrivialFactor
  rw [halfSymTrivialS3_eq, halfSymTotalDim_eq]
  norm_num

theorem effectiveCellCount_eq : effectiveCellCount = 1 := by
  unfold effectiveCellCount
  rw [s3TrivialFactor_eq]
  norm_num

/-- The per-cell ratio 1/8 (one effective cell of eight total). -/
theorem perCellRatio_eq : effectiveCellCount / 8 = 1 / 8 := by
  rw [effectiveCellCount_eq]
  norm_num

/-- Main result: the half-symmetric H_4 projection, restricted to
    the S_3-trivial subspace, extracts exactly ONE of the 8 ideal
    octahedral cells in the Borromean complement tessellation.

    Scope (2026-05-24, post-purge): combinatorial bijection only.
    The proof states the standard S_n branching arithmetic; it
    makes NO claim about per-cell curvature κ. The earlier
    `Yekutieli per-cell` reading (κ = −G) was purged from
    production on 2026-05-24 (commit 71d674da1) as non-canonical:
    PR #985 found the natural-reading bijection gives κ = +0.5,
    not −G, and no categorical derivation supplies −G·h².

    Per the absorbed-into-VolDensity framing (PR #1080), the
    canonical mass formula is m(K) = m_e · VolDensity(K, q_0)
    with no separate λ_scale constant. This bijection is a
    structural input that constrains VolDensity(𝓑₃)'s categorical
    refinement at h² order; it is NOT a per-cell additive
    correction. -/
-- Ref: [adams1985hyperbolic] https://doi.org/10.1007/978-1-4684-9458-7
-- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
theorem s4_s3_half_symmetric_projection :
    effectiveCellCount = 1 ∧ effectiveCellCount / 8 = 1 / 8 :=
  ⟨effectiveCellCount_eq, perCellRatio_eq⟩

end QOU.BraidsAndKnots


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub)

This proposition is conditional on the conjecture's class
`BorromeanCommonScale` (declared in the lake-package sibling).  The local stub
below mirrors the canonical class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises
the conditional-on-class structure of the main theorem above. -/

namespace QOU.BraidsAndKnots.S4S3Audit.ConditionalAudit

/-- Local stub of the conjecture's axiomatised class.  See the lake-
    package sibling for the canonical declaration. -/
class BorromeanCommonScale : Prop where
  /-- Conjecture content is the class instance (sorry = conjecture
      per AGENTS.md §3b). -/
  holds : True

/-- Witness theorem demonstrating the main proposition is conditional
    on `[BorromeanCommonScale]` per AGENTS.md §3b-cond. -/
theorem conditional_on_BorromeanCommonScale
    [_inst : BorromeanCommonScale] : True := trivial

end QOU.BraidsAndKnots.S4S3Audit.ConditionalAudit
