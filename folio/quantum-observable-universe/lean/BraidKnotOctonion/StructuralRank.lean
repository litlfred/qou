import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.DivisionRing
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.DFinsupp
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.Order.SupIndep
import Mathlib.Algebra.DirectSum.Module

/-!
# QOU.BraidKnot.StructuralRank — Hecke panel structural rank decomposition (conditional on Mackey-filtration nesting)

Backs the audit
[`docs/audits/2026-05-09-A-operator-rank-structure.md`](../../../../../docs/audits/2026-05-09-A-operator-rank-structure.md).

Encodes — at the level of ℕ-valued ranks — the structural rank
identity for the operator-valued least-squares supply matrix `M_λ`
arising from the Hecke branching `H_{n_1+n_2}(q) ⊃ H_{n_1}(q) ⊗
H_{n_2}(q)`:

  rank(M_λ) = Σ_{μ ∈ supp_λ} max_{ν : c^λ_{μν} > 0} rank(X_μ) · rank(Y_ν)

where `X_μ`, `Y_ν` are the test-panel image matrices for the
Hoefsmit reps `V_μ`, `V_ν`, and `c^λ_{μν}` are LR coefficients.

Two structural ingredients enter as **class hypotheses** (per
§3b-cond conditional-class pattern):

1. **Within-μ nesting (max over ν).** For fixed μ, the column spaces
   of the (μ, ν)-blocks vary with ν as a *nested chain*, not a
   direct sum.  Joint column-span rank = `max_ν rank(block μ ν)`.
   Closest published precedent: the Mackey filtration on induced
   modules for cyclotomic Hecke algebras
   ([Mathas 2004](https://doi.org/10.1016/S0021-8693(02)00075-3))
   and its graded refinement
   ([Hu–Mathas 2012](https://arxiv.org/abs/1008.1462)).  Neither
   states the column-span / fitting-matrix rank consequence
   explicitly, but both establish the underlying nested-filtration
   structure.

2. **Across-μ independence (sum over μ).** Different μ-blocks
   contribute orthogonal column spaces, so total rank = `Σ_μ` of
   per-μ joint ranks.  This is Wedderburn block-diagonality for
   `H_n(q)` semisimple — folklore, freely used in
   [Geck–Pfeiffer (2000), §8–9](https://global.oup.com/academic/product/9780198502500).

Given both hypotheses, the rank formula is an unconditional ℕ
arithmetic consequence (proved here without `sorry`).  Numerical
sanity at λ = [7, 2] matches the empirical extract
(`A_operator_rank_probe.witness.json` v1.1, A=3): 22 + 64 = 86.

LaTeX: not yet — audit-only.

References:
- `docs/audits/2026-05-09-A-operator-rank-structure.md`
- Mathas, A. (2004). Filtrations on the Mackey decomposition for
  cyclotomic Hecke algebras. J. Algebra 271(2), 522–560.
- Hu, J. & Mathas, A. (2012). Graded induction for Specht modules.
  IMRN 2012(6), 1230–1263.
- Geck, M. & Pfeiffer, G. (2000). Characters of Finite Coxeter
  Groups and Iwahori–Hecke Algebras.  LMS Monograph 21, OUP.
- Mathas, A. (1999). Iwahori–Hecke and Schur algebras of the
  symmetric group.  AMS Univ. Lect. Series 15.
-/

namespace QOU.BraidKnot

open scoped DirectSum

/-- **Structural rank decomposition class** for a Hecke panel
    matrix indexed by `(μ, ν)`-blocks.

    Class hypotheses encode the two structural facts from the audit:
    (a) within-μ nesting (joint = max), and
    (b) across-μ independence (total = sum of joints).

    Conjectural status: §3b-cond.  The within-μ nesting field is
    the Mackey-filtration / Specht-filtration nesting (Mathas 2004;
    Hu–Mathas 2012), specialized to test-panel column spaces.  Not
    explicitly stated in the published literature for the
    fitting-matrix / column-rank shape used here, but mechanically
    a corollary of those filtration results once the column spaces
    are identified with Specht-filtration layers. -/
-- Ref: [mathas2004mackey] Filtrations on the Mackey decomposition for cyclotomic Hecke algebras
-- Ref: [hu-mathas2012graded] Graded induction for Specht modules
-- Ref: [geckpfeiffer2000] Characters of Finite Coxeter Groups and Iwahori-Hecke Algebras §8-9
class PanelRankDecomposition
    (μIdx : Type) [Fintype μIdx]
    (νIdx : μIdx → Type) [∀ μ, Fintype (νIdx μ)]
    (blockRank : (μ : μIdx) → νIdx μ → ℕ)
    (jointRankMu : μIdx → ℕ)
    (totalRank : ℕ) : Prop where
  /-- **Within-μ nesting** (Mackey/Specht filtration; cf. Mathas
      2004, Hu–Mathas 2012).  The joint column-span rank across
      all ν-blocks for a fixed μ equals the maximum of the
      individual ν-block ranks — column spaces vary as a nested
      chain in ν, not as a direct sum. -/
  joint_eq_max :
    ∀ μ : μIdx,
      jointRankMu μ = (Finset.univ : Finset (νIdx μ)).sup (blockRank μ)
  /-- **Across-μ independence** (Wedderburn block-diagonality for
      `H_n(q)` semisimple; standard).  Total rank decomposes
      additively across μ-blocks. -/
  total_eq_sum :
    totalRank = ∑ μ : μIdx, jointRankMu μ

namespace PanelRankDecomposition

/-- **Structural rank formula** (derived).

    Given the within-μ nesting and across-μ independence
    hypotheses, the total rank of the panel matrix is the sum
    over μ of the maximum over ν of the per-block rank.  Pure ℕ
    arithmetic — proved unconditionally from the class fields. -/
theorem rank_formula
    {μIdx : Type} [Fintype μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {blockRank : (μ : μIdx) → νIdx μ → ℕ}
    {jointRankMu : μIdx → ℕ}
    {totalRank : ℕ}
    [D : PanelRankDecomposition μIdx νIdx blockRank jointRankMu totalRank] :
    totalRank =
      ∑ μ : μIdx, (Finset.univ : Finset (νIdx μ)).sup (blockRank μ) := by
  rw [D.total_eq_sum]
  exact Finset.sum_congr rfl (fun μ _ => D.joint_eq_max μ)

end PanelRankDecomposition

/-! ## Numerical sanity at λ = [7, 2], A = 3

Matches the empirical SVD rank probe
(`A_operator_rank_probe.witness.json`, A=3): with two μ-blocks
(`μ = [3]` and `μ = [2,1]`), per-(μ,ν) ranks measured at the
H_3 ⊗ H_6 panel are:

| μ      | ν-blocks (with c^λ_{μν} > 0) | per-block ranks    | max_ν |
|--------|------------------------------|--------------------|-------|
| [3]    | [6], [5,1], [4,2]            | 1, 16, 22          | 22    |
| [2,1]  | [6], [5,1]                   | 4, 64              | 64    |

Total rank = 22 + 64 = **86**, matching `A_operator_rank_probe`
exactly (drop ratio 10^13 → exact zero in the SVD spectrum).
-/

/-- **λ = [7, 2] empirical rank decomposition** —
    encoded as a `PanelRankDecomposition` instance over the two
    LR-support μ-partitions and their respective ν-blocks. -/
def panel_7_2_blockRank : Bool → Fin 3 → ℕ
  | false, ⟨0, _⟩ => 1     -- μ = [3], ν = [6]
  | false, ⟨1, _⟩ => 16    -- μ = [3], ν = [5,1]
  | false, ⟨2, _⟩ => 22    -- μ = [3], ν = [4,2]
  | true,  ⟨0, _⟩ => 4     -- μ = [2,1], ν = [6]
  | true,  ⟨1, _⟩ => 64    -- μ = [2,1], ν = [5,1]
  | true,  ⟨2, _⟩ => 0     -- placeholder: c^λ = 0 for μ=[2,1], ν=[4,2]

/-- The per-μ joint rank: `max_ν` of `panel_7_2_blockRank`. -/
def panel_7_2_jointRankMu : Bool → ℕ
  | false => 22
  | true  => 64

instance : PanelRankDecomposition Bool (fun _ => Fin 3)
    panel_7_2_blockRank panel_7_2_jointRankMu 86 where
  joint_eq_max := by
    intro μ
    cases μ <;> decide
  total_eq_sum := by decide

/-- **Empirical match** — the rank formula yields 86 at λ = [7, 2]. -/
theorem panel_7_2_total_rank :
    (86 : ℕ) =
      ∑ μ : Bool, (Finset.univ : Finset (Fin 3)).sup (panel_7_2_blockRank μ) :=
  -- Pin `jointRankMu` explicitly: it appears only in `rank_formula`'s
  -- instance binder (not its conclusion), so it cannot be inferred from
  -- the goal — left implicit it stalls instance search on a metavariable.
  PanelRankDecomposition.rank_formula (jointRankMu := panel_7_2_jointRankMu)

/-! ## Submodule-level reformulation

Lifts the ℕ-arithmetic `PanelRankDecomposition` to actual
sub-spaces: the panel-image of each `(μ, ν)`-block is a
`Submodule K V` for a finite-dimensional ambient `V`, the
within-μ nesting becomes a *chain* (totally ordered by ≤) of
sub-spaces, and across-μ independence becomes `iSupIndep` of the
per-μ joint sub-spaces.

**Both parts fully proved** (no `sorry`):

| Lemma | Statement |
|---|---|
| `iSup_eq_νStar` | `⨆ ν, W μ ν = W μ (νStar μ)` |
| `finrank_iSup_eq_νStar` | finrank of joint span = finrank of νStar block |
| `finrank_blockRank_le` | each block's finrank ≤ νStar block's finrank |
| `finrank_iSup_eq_finset_sup` | finrank of joint span = max-over-ν of block finranks |
| `finrank_iSup_eq_sum_of_iSupIndep` | (general) `iSupIndep p → finrank (⨆ i, p i) = ∑ i, finrank (p i)` |
| `toRankDecomposition` | `PanelImageStructure → PanelRankDecomposition` (instance) |

The general lemma `finrank_iSup_eq_sum_of_iSupIndep` factors
through `DirectSum.coeLinearMap`: its range is `⨆ i, p i`
(`DirectSum.range_coeLinearMap`), and `iSupIndep` makes it
injective (`iSupIndep.dfinsupp_lsum_injective`), so we get
`(⨁ i, p i) ≃ₗ[K] (⨆ i, p i)` and then close with
`Module.finrank_directSum`.
-/

universe u v

/-- **Panel-image Submodule structure.**

    A finite-dimensional ambient space `V` over a field `K`,
    together with a `(μ, ν)`-indexed family of sub-spaces
    `W : (μ : μIdx) → νIdx μ → Submodule K V` carrying the two
    structural hypotheses of the audit:

    1. For each μ, there is a maximizing `νStar μ` such that
       `W μ ν ≤ W μ (νStar μ)` for all ν (within-μ chain).
    2. The per-μ joint sub-spaces `W μ (νStar μ)` are
       complete-lattice-independent (across-μ orthogonality). -/
-- Ref: [mathas2004mackey] Mackey filtration on cyclotomic Hecke induction
-- Ref: [hu-mathas2012graded] Graded induction for Specht modules
class PanelImageStructure
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    (μIdx : Type) [Fintype μIdx] [DecidableEq μIdx]
    (νIdx : μIdx → Type) [∀ μ, Fintype (νIdx μ)]
    (W : (μ : μIdx) → νIdx μ → Submodule K V) where
  -- Type-valued (not `Prop`): the `νStar` field below is *data* (a
  -- chosen maximiser per μ), which a `Prop`-valued class cannot carry.
  /-- A maximizing ν for each μ (witness of the chain's top element). -/
  νStar : (μ : μIdx) → νIdx μ
  /-- Within-μ nesting: `νStar μ` dominates every ν in the inclusion order. -/
  νStar_max : ∀ μ ν, W μ ν ≤ W μ (νStar μ)
  /-- Across-μ independence of the per-μ joint sub-spaces. -/
  independent :
    iSupIndep (fun μ : μIdx => W μ (νStar μ))

namespace PanelImageStructure

/-- **Within-μ joint span equals the maximum chain element.**

    From the chain hypothesis (`νStar_max`), every ν-block is
    contained in the `νStar`-block, so `⨆ ν, W μ ν = W μ (νStar μ)`. -/
theorem iSup_eq_νStar
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {μIdx : Type} [Fintype μIdx] [DecidableEq μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {W : (μ : μIdx) → νIdx μ → Submodule K V}
    [P : PanelImageStructure μIdx νIdx W] (μ : μIdx) :
    (⨆ ν : νIdx μ, W μ ν) = W μ (P.νStar μ) :=
  le_antisymm (iSup_le (P.νStar_max μ)) (le_iSup (W μ) (P.νStar μ))

/-- **Within-μ finrank equals the chain-maximum's finrank.**

    Combines `iSup_eq_νStar` with `finrank` (no monotonicity
    needed since the supremum is literally the maximum element). -/
theorem finrank_iSup_eq_νStar
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {μIdx : Type} [Fintype μIdx] [DecidableEq μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {W : (μ : μIdx) → νIdx μ → Submodule K V}
    [P : PanelImageStructure μIdx νIdx W] (μ : μIdx) :
    Module.finrank K (⨆ ν : νIdx μ, W μ ν : Submodule K V) =
      Module.finrank K (W μ (P.νStar μ)) := by
  rw [iSup_eq_νStar (P := P) μ]

/-- **finrank-monotonicity over the within-μ chain.**

    Since `W μ ν ≤ W μ (νStar μ)`, finrank is monotone on
    sub-spaces of a finite-dimensional space, so every block's
    finrank is at most the `νStar`-block's. -/
theorem finrank_blockRank_le
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {μIdx : Type} [Fintype μIdx] [DecidableEq μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {W : (μ : μIdx) → νIdx μ → Submodule K V}
    [P : PanelImageStructure μIdx νIdx W] (μ : μIdx) (ν : νIdx μ) :
    Module.finrank K (W μ ν) ≤ Module.finrank K (W μ (P.νStar μ)) :=
  Submodule.finrank_mono (P.νStar_max μ ν)

/-- **Within-μ finrank equals the sup-over-ν of block finranks.**

    Combines the chain hypothesis (every block ≤ νStar-block) with
    finrank monotonicity: the supremum's finrank equals the
    νStar-block's finrank, which is also the maximum of the
    individual ν-block finranks. -/
theorem finrank_iSup_eq_finset_sup
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {μIdx : Type} [Fintype μIdx] [DecidableEq μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {W : (μ : μIdx) → νIdx μ → Submodule K V}
    [P : PanelImageStructure μIdx νIdx W] (μ : μIdx) :
    Module.finrank K (⨆ ν : νIdx μ, W μ ν : Submodule K V) =
      (Finset.univ : Finset (νIdx μ)).sup
        (fun ν => Module.finrank K (W μ ν)) := by
  rw [finrank_iSup_eq_νStar (P := P) μ]
  apply le_antisymm
  · exact Finset.le_sup (f := fun ν => Module.finrank K (W μ ν))
      (Finset.mem_univ (P.νStar μ))
  · exact Finset.sup_le fun ν _ => finrank_blockRank_le μ ν

end PanelImageStructure

/-! ### Across-μ summation: finrank of an iSupIndep family -/

/-- **Finrank of an independent supremum decomposes as a sum.**

    For an `iSupIndep` family of submodules in a finite-dimensional
    space, the finrank of the joint supremum is the sum of the
    individual finranks.

    Proof: `DirectSum.coeLinearMap p : (⨁ i, p i) →ₗ[K] V` has
    range `⨆ i, p i` (`DirectSum.range_coeLinearMap`), and is
    injective by `iSupIndep.dfinsupp_lsum_injective`.  So
    `(⨁ i, p i) ≃ₗ[K] (⨆ i, p i)`, and the conclusion follows
    from `Module.finrank_directSum`. -/
theorem finrank_iSup_eq_sum_of_iSupIndep
    {K : Type u} [DivisionRing K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    {p : ι → Submodule K V} (hp : iSupIndep p) :
    Module.finrank K (⨆ i, p i : Submodule K V) =
      ∑ i, Module.finrank K (p i) := by
  classical
  -- Step 1: the canonical linear map ⨁ i, p i →ₗ V has range ⨆ i, p i
  -- and is injective (by iSupIndep).
  have hinj : Function.Injective (DirectSum.coeLinearMap p) :=
    hp.dfinsupp_lsum_injective
  have hrange : LinearMap.range (DirectSum.coeLinearMap p) = ⨆ i, p i :=
    DirectSum.range_coeLinearMap
  -- Step 2: factor as a LinearEquiv via ofInjective + ofEq.
  have L : (⨁ i, p i) ≃ₗ[K] (⨆ i, p i : Submodule K V) :=
    (LinearEquiv.ofInjective _ hinj).trans (LinearEquiv.ofEq _ _ hrange)
  -- Step 3: transport finrank along L, then close with finrank_directSum.
  rw [← L.finrank_eq, Module.finrank_directSum]

namespace PanelImageStructure

/-- **Translation to ℕ-rank class.**

    Given a `PanelImageStructure` over a finite-dimensional ambient
    space, build a `PanelRankDecomposition` instance with
    `blockRank μ ν := finrank K (W μ ν)`,
    `jointRankMu μ := finrank K (W μ (νStar μ))`, and
    `totalRank := finrank K (⨆ μ ν, W μ ν)`.

    The within-μ field follows from `finrank_iSup_eq_finset_sup`.
    The across-μ field uses `finrank_iSup_eq_sum_of_iSupIndep` after
    rewriting the inner `⨆ ν` to its νStar value via
    `iSup_eq_νStar`. -/
def toRankDecomposition
    {K : Type u} [Field K]
    {V : Type v} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    {μIdx : Type} [Fintype μIdx] [DecidableEq μIdx]
    {νIdx : μIdx → Type} [∀ μ, Fintype (νIdx μ)]
    {W : (μ : μIdx) → νIdx μ → Submodule K V}
    [P : PanelImageStructure μIdx νIdx W] :
    PanelRankDecomposition μIdx νIdx
      (fun μ ν => Module.finrank K (W μ ν))
      (fun μ => Module.finrank K (W μ (P.νStar μ)))
      (Module.finrank K (⨆ μ : μIdx, ⨆ ν : νIdx μ, W μ ν : Submodule K V)) where
  joint_eq_max := fun μ => by
    have h := finrank_iSup_eq_finset_sup (P := P) μ
    -- h : finrank (⨆ ν, W μ ν) = sup_ν finrank (W μ ν)
    -- want : finrank (W μ (νStar μ)) = sup_ν finrank (W μ ν)
    rw [← finrank_iSup_eq_νStar (P := P) μ]; exact h
  total_eq_sum := by
    -- Rewrite ⨆ μ ⨆ ν, W μ ν as ⨆ μ, W μ (νStar μ) using iSup_eq_νStar
    have hcongr : (⨆ μ : μIdx, ⨆ ν : νIdx μ, W μ ν : Submodule K V) =
        ⨆ μ : μIdx, W μ (P.νStar μ) :=
      iSup_congr (fun μ => iSup_eq_νStar (P := P) μ)
    rw [hcongr]
    exact finrank_iSup_eq_sum_of_iSupIndep P.independent

end PanelImageStructure

end QOU.BraidKnot
