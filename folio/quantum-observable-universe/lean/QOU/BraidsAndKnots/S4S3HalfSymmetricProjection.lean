/-
  S_3-trivial share of the half-symmetric part of H_4 (S_4 ↓ S_3 branching).

  Weighted dimension 5, weighted trivial-S_3 multiplicity 2, share 2/5.
  This is branching arithmetic only.  It selects no cell of a hyperbolic
  decomposition: S³ ∖ 𝓑₃ is TWO regular ideal octahedra (Vol = 2·V_oct
  = 8G, V_oct = 4G), so the earlier "one of eight octahedra" reading had
  no geometric basis and was removed (2026-11-15).

  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
  -- Ref: [adams1985hyperbolic] ISBN 978-0-7167-1510-2 (two ideal octahedra)
-/
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

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

/-- The product (5/2) × (2/5) = 1.  Arithmetic only: 5/2 is the weighted
    number of half-symmetric irreducibles.  No geometric meaning is claimed. -/
def effectiveCellCount : ℚ := (5 : ℚ) / 2 * s3TrivialFactor

-- The three key assertions, verified by `simp` / `norm_num`.
-- Ref: [james1984representation] §2 (S_n branching rules)

theorem halfSymTotalDim_eq : halfSymTotalDim = 5 := by
  simp only [halfSymTotalDim, halfSymRepresentatives, List.foldl_cons, List.foldl_nil]; norm_num

theorem halfSymTrivialS3_eq : halfSymTrivialS3 = 2 := by
  simp only [halfSymTrivialS3, halfSymRepresentatives, List.foldl_cons, List.foldl_nil]; norm_num

theorem s3TrivialFactor_eq : s3TrivialFactor = 2 / 5 := by
  unfold s3TrivialFactor
  rw [halfSymTrivialS3_eq, halfSymTotalDim_eq]

theorem effectiveCellCount_eq : effectiveCellCount = 1 := by
  unfold effectiveCellCount
  rw [s3TrivialFactor_eq]
  norm_num

/-- Main result: in the half-symmetric part of H_4 at q = 1, the weighted
    dimension is 5, the weighted trivial-S_3 multiplicity is 2, and the
    S_3-trivial share is 2/5.  Branching arithmetic only
    ([james1984representation] §2); no per-cell or curvature claim. -/
-- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
theorem s4_s3_half_symmetric_projection :
    halfSymTotalDim = 5 ∧ halfSymTrivialS3 = 2 ∧ s3TrivialFactor = 2 / 5 :=
  ⟨halfSymTotalDim_eq, halfSymTrivialS3_eq, s3TrivialFactor_eq⟩

end QOU.BraidsAndKnots
