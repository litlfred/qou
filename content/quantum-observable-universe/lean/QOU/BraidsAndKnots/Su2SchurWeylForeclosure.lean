import Mathlib.Tactic

/-!
# SU(2) / WRT(S³/2I) Schur–Weyl foreclosure — the geometric `W_λ` index cannot be the naive SU(2)-side modular data

The s5-so3 keystone asks whether a geometric equivariant index (Beasley–Witten
Seifert–Chern–Simons on the Poincaré sphere `S³/2I`) reproduces the q-Plancherel weight
`W_λ = d_q(λ)²/[n]_q!`. WRT(S³/2I) carries **SU(2)-side modular data**; under classical
Schur–Weyl `(ℂ²)^{⊗n} = ⊕_{λ : ≤2 rows} S^λ ⊗ V_λ`, the **GL₂(=spinor ℂ²) image is
exactly the partitions with at most two rows**. The Step-1 gate
([`docs/audits/2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`](../../../../docs/audits/2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md),
PR #2717) ran this at n=3,4,5 and found the SU(2) side **omits every ≥3-row block**,
including the **electron `(3,1,1)`**.

This file machine-checks that structural foreclosure (previously prose / Python only in
#2406 / #2608 / #2717): the GL₂ Schur–Weyl image among the partitions of 5 is exactly
`{(5),(4,1),(3,2)}`, the electron `(3,1,1)` is **not** in it, and therefore **any weight
system supported on the GL₂ image differs from any `W_λ` that is nonzero on the electron
block** (`su2_index_ne_wlambda`). Since the actual `W_λ(3,1,1) = d_q(3,1,1)²/[5]_q! > 0`
at the substrate (`d_q(3,1,1) ≈ 6.2204`, witnessed in the Step-1 gate), the naive
SU(2)/WRT(S³/2I) index cannot equal `W_λ` — the geometric realization must live on the
**full-Hecke side** (`S_n`, `d→∞`), as the corpus arena correction (#2406) concluded.

The partition type here mirrors `QOU.BraidsAndKnots.PartitionOf5` (the keystone scaffold
in `S5SO3FiberAction.lean`); it is restated self-contained — under the dedicated
`Su2Foreclosure` namespace, importing only `Mathlib.Tactic` — to keep this foreclosure
free of the scaffold's heavier import surface. The row-counts and the electron block
`(3,1,1)` (which carries the central A₅ rep `T₁ ⊕ T₂`) coincide with the scaffold's.

This is a **(b) structural exclusion** (refutation-scope discipline): it rests on a proved
invariant — the row-count bound of the GL_d Schur–Weyl image — and excludes only the
**SU(2) sub-route**, *not* the full-Hecke geometric programme (the open frontier). No fit;
nothing archimedean here (the capstone is abstract over the weight codomain; positivity of
`W_λ(3,1,1)` enters only as the cited hypothesis `hW`).
-/

namespace QOU.BraidsAndKnots.Su2Foreclosure

/-- The 7 partitions of 5 (indexing the 7 irreps of `S₅`); mirrors the keystone scaffold's
`QOU.BraidsAndKnots.PartitionOf5`. -/
inductive PartitionOf5 where
  | five         -- (5)
  | fourOne      -- (4, 1)
  | threeTwo     -- (3, 2)
  | threeOneOne  -- (3, 1, 1)   ← the electron block (A₅ rep T₁ ⊕ T₂)
  | twoTwoOne    -- (2, 2, 1)
  | twoOneOneOne -- (2, 1, 1, 1)
  | onesFive     -- (1, 1, 1, 1, 1)
  deriving DecidableEq, Repr

/-- All 7 partitions of 5. -/
def PartitionOf5.allList : List PartitionOf5 :=
  [.five, .fourOne, .threeTwo, .threeOneOne, .twoTwoOne, .twoOneOneOne, .onesFive]

/-- Number of (nonzero) rows of the Young diagram. -/
def PartitionOf5.numRows : PartitionOf5 → ℕ
  | .five => 1
  | .fourOne => 2
  | .threeTwo => 2
  | .threeOneOne => 3
  | .twoTwoOne => 3
  | .twoOneOneOne => 4
  | .onesFive => 5

/-- A block lies in the **GL₂ (spinor ℂ²) Schur–Weyl image** iff its Young diagram has at
most two rows — `(ℂ²)^{⊗n} = ⊕_{λ:≤2 rows} S^λ ⊗ V_λ`.  This is the support of the
SU(2)-side WRT(S³/2I) modular data. -/
def PartitionOf5.inGL2SchurWeylImage (p : PartitionOf5) : Prop := p.numRows ≤ 2

instance (p : PartitionOf5) : Decidable p.inGL2SchurWeylImage :=
  inferInstanceAs (Decidable (p.numRows ≤ 2))

/-- The GL₂ Schur–Weyl image among the partitions of 5 is **exactly** the three ≤2-row
blocks `{(5),(4,1),(3,2)}`. -/
theorem gl2_image_eq_le2row :
    PartitionOf5.allList.filter (fun p => decide p.inGL2SchurWeylImage)
      = [.five, .fourOne, .threeTwo] := by decide

/-- The **electron block `(3,1,1)`** (3 rows; carries the central A₅ rep `T₁ ⊕ T₂`) is
**not** in the GL₂ Schur–Weyl image. The rigorous form of the ✅-forced corpus fact
"spinor ℂ² kills the electron (3,1,1)" (#2406). -/
theorem electron_not_in_gl2_image : ¬ PartitionOf5.threeOneOne.inGL2SchurWeylImage := by
  decide

/-- The SU(2) side **omits at least one block** of `S₅` (the coverage gap). -/
theorem gl2_image_has_coverage_gap :
    ∃ p ∈ PartitionOf5.allList, ¬ p.inGL2SchurWeylImage :=
  ⟨.threeOneOne, by decide, electron_not_in_gl2_image⟩

/-- **Foreclosure of the SU(2)/WRT(S³/2I) route (the keystone result of this file).**
Any weight system `idx` supported on the GL₂ Schur–Weyl image (vanishing off the ≤2-row
blocks — the SU(2)-side WRT modular data) **differs** from any `W` that is nonzero on the
electron block `(3,1,1)`.

Applied to the q-Plancherel weight `W = W_λ`, whose value on the electron block is
`d_q(3,1,1)²/[5]_q! > 0` at the substrate (`hW`), this says the geometric `W_λ` index
**cannot** be the naive SU(2)/WRT(S³/2I) modular data — it must live on the full-Hecke
side. Abstract over the codomain `R`; positivity of `W_λ(3,1,1)` enters only via `hW`. -/
theorem su2_index_ne_wlambda {R : Type*} [Zero R] (idx W : PartitionOf5 → R)
    (hsupp : ∀ p, ¬ p.inGL2SchurWeylImage → idx p = 0)
    (hW : W .threeOneOne ≠ 0) : idx ≠ W := by
  intro hEq
  apply hW
  have h0 : idx .threeOneOne = 0 := hsupp .threeOneOne electron_not_in_gl2_image
  rw [← hEq, h0]

end QOU.BraidsAndKnots.Su2Foreclosure
