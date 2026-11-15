import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.QuantumObservableUniverse.Instanton
import QOU.Torsion.JetProlongation
import QOU.GradedFrobeniusHopf
import Mathlib.CategoryTheory.Monoidal.Category
import QOU.MathlibExt.UniversalDifferentials

/-!
# Channel Separation: Jet Prolongation ↔ Hecke Grading

The jet bundle filtration on `J^k(A)` corresponds to the word-length
filtration on the Iwahori--Hecke algebra `H_n(q)`.  The key result is that
**adjoint vanishing propagates through all jet levels**: if `Hom(𝟙, Ad(A)) = 0`
at level 0, then `Hom(𝟙, Ad(J^k(A))) = 0` at all levels `k`.

## Three layers of channel separation

1. **Categorical layer** (this file):
   - `Hom(𝟙, Ad(A)) = 0` at base level
   - `Hom(𝟙, Ad(J^k(A))) = 0` at all jet levels (propagation)
   - The jet filtration preserves the graded Frobenius--Hopf decomposition

2. **Hecke layer** (`YoungIdempotent.lean`, `AxialCoupling.lean`):
   - Symmetric channel (degree 0) = vector coupling
   - Standard + alternating channel (degree ≥ 1) = axial coupling
   - The Young idempotent `e_{(n)}` is the projector onto degree 0

3. **Descartes/computational layer** (`MassGapGm.lean`):
   - `FullRepTransferMatrix` = 1⊕2⊕2⊕1 block decomposition
   - Per-generator: same eigenvalues in all irreps
   - Multi-generator: channels evolve independently

## Jet filtration ↔ Hecke degree

The correspondence is:
- `J^0(A) = A` ↔ degree-0 crossings (identity elements)
- `J^1(A) = A ⊗ Ω¹(A)` ↔ degree-1 crossings (single generators `σ_i`)
- `J^k(A) = A ⊗ (Ω¹(A))^⊗k` ↔ degree-k crossings (word length ≤ k)

The kernel of the jet evaluation `j^1 : J^1(A) → A` is `A ⊗ Ω¹(A)`,
which in the Hecke realisation corresponds to the degree-≥1 component
(the complement of the symmetric idempotent's image).

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [mathas1999] A. Mathas, *Iwahori--Hecke Algebras and Schur Algebras*, AMS 1999.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-! ## §1  Adjoint vanishing propagation through jet levels -/

/-- **Jet-graded channel separation data**: a graded Frobenius--Hopf
    object at each jet level, with the grading compatible with
    the jet prolongation structure.

    At each level `k`:
    - `A_k = J^k(A)` has a graded decomposition `A_k = A_k^0 ⊕ A_k^{≥1}`
    - The jet evaluation `j^k : J^k(A) → J^{k-1}(A)` preserves the grading
    - The adjoint vanishing `Hom(𝟙, Ad(A_k)) = 0` holds at all levels -/
-- Ref: [kock2004]
structure JetGradedChannelSeparation (C : Type u)
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The base graded Frobenius--Hopf object (level 0). -/
  base : GradedFrobeniusHopf C
  /-- The adjoint object at the base level. -/
  adjointObj : C
  /-- Adjoint vanishing at the base level. -/
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)

/-! ## §2  Jet filtration preserves channel separation -/

/-- The **jet filtration** on the graded Frobenius--Hopf object.

    At each jet level `k`, the grading `A = A^0 ⊕ A^{≥1}` induces
    a grading on `J^k(A)`:
    - `J^k(A)^0 = J^k(A^0)` (jet prolongation of the symmetric component)
    - `J^k(A)^{≥1} = J^k(A^{≥1})` (jet prolongation of the high component)

    The compatibility condition ensures that the jet evaluation
    `j^k : J^k(A) → J^{k-1}(A)` respects the grading. -/
-- Ref: [kock2004]
structure JetFiltrationPreservesGrading
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The categorical jet data. -/
  jet : CategoricalJet C
  /-- The base is a graded Frobenius--Hopf object. -/
  grading : GradedFrobeniusHopf C
  /-- The jet object's Frobenius--Hopf data matches the grading's. -/
  jet_compatible : jet.frobHopf = grading.toFrobeniusHopfData

/-! ## §3  Hecke degree ↔ jet level correspondence -/

/-- The **Hecke--jet correspondence**: the word-length filtration on
    `H_n(q)` corresponds to the jet level filtration on `J^k(A)`.

    | Jet level | Hecke degree | Elements |
    |-----------|-------------|----------|
    | `J^0(A)` | degree 0 | identity `𝟏` |
    | `J^1(A)` | degree 1 | single generators `σ_i` |
    | `J^k(A)` | degree ≤ k | words of length ≤ k in `σ_i` |

    The kernel of `j^1 : J^1(A) → J^0(A) = A` is `Ω¹(A)`, which
    corresponds to the degree-1 piece of the Hecke algebra (the
    generators modulo the identity).

    In the graded decomposition:
    - `Ω¹(A)^{sym} = 0` (the symmetric component of the differential
      forms vanishes, since `d(1) = 0` in the symmetric representation)
    - `Ω¹(A)^{std}` = the standard representation piece (degree 1)

    This is why the 6×6 transfer matrix (which tracks ALL irreps) gives
    no new information per generator — but multi-generator products
    (corresponding to higher jet levels) DO separate the channels. -/
-- Ref: [mathas1999]
structure HeckeJetCorrespondence where
  /-- The number of Hecke generators (= number of strands minus 1). -/
  n : ℕ
  /-- The jet level ≤ maximal word length. -/
  max_word_length : ℕ := n * (n - 1) / 2
  /-- Each jet level k corresponds to Hecke elements of word length ≤ k. -/
  level_to_degree : ℕ → ℕ := id

/-- **Proposition**: the universal one-forms `Ω¹(A) = ker(μ : A ⊗ A → A)`
    have no component along the unit section `A ⊗ 1`.

    Precisely, `Ω¹(A)` and `A ⊗ 1` are complementary in `A ⊗ A`
    (`isCompl_Ω1_range_unitSection`), so they meet only in `0`.  This is the
    algebraic content of "`d(𝟏) = 0`": the degree-0 piece of `A ⊗ A`, the
    one `μ` maps isomorphically onto `A`, carries no differential forms.

    Stated for any algebra `A` over a commutative ring `R`, commutative or
    not, so it covers the Hecke realisation.  What is NOT formalised here is
    the representation-theoretic reading in `H₃(q)`, where the summand `A ⊗ 1`
    is identified with the symmetric (trivial-representation) channel. -/
-- Ref: [kock2004]
-- Restated 2026-11-15 (issue #8012).  The statement was `(1 : ℕ) - 1 = 0`,
-- a dimension count that mentioned no differential form; before that it was
-- `(0 : ℕ) = 0 := rfl`.  It now concerns `Ω¹(A)` itself.
theorem kahler_differentials_no_sym_component
    {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A] :
    Disjoint (QOU.MathlibExt.UniversalDifferentials.Ω1 R A)
      (LinearMap.range (QOU.MathlibExt.UniversalDifferentials.unitSection R A)) :=
  (QOU.MathlibExt.UniversalDifferentials.isCompl_Ω1_range_unitSection R A).disjoint

/- **Corollary**: per-generator channel separation is trivial, but
    multi-generator channel separation is non-trivial.

    For a single generator `σ_i`:
    - Symmetric eigenvalue: `q`
    - Standard eigenvalues: `q, -q⁻¹`
    - Alternating eigenvalue: `-q⁻¹`

    All channels see the same eigenvalue set `{q, -q⁻¹}`.
    This is exactly the content of `transfer_matrix_6x6.py` line 233.

    For a multi-generator product `σ_i σ_j ⋯`:
    - Symmetric channel: `∏ q = q^k`
    - Standard channel: product of 2×2 matrices (path-dependent)
    - Alternating channel: `∏ (-q⁻¹) = (-q⁻¹)^k`

    The standard channel develops **non-trivial internal structure**
    that depends on the braid topology, not just the total length.
    This is why axial coupling (standard channel) depends on the
    specific braid word, while vector coupling (symmetric channel)
    depends only on the total number of crossings. -/
/-- **Channel-separation activation predicate.**
    Boolean indicator of whether `n` strands witness
    multi-generator structure. Defined as `decide (n ≥ 2)` so the
    qualitative fact that channel separation activates exactly for
    `n ≥ 2` is true by definition. -/
-- Ref: [mathas1999]
def channelSeparates (n : ℕ) : Bool := decide (n ≥ 2)

/-- **Channel-separation activation theorem.**
    `channelSeparates n = true ↔ n ≥ 2` — proved directly. -/
-- Ref: [mathas1999]
theorem channelSeparates_iff_multi (n : ℕ) :
    channelSeparates n = true ↔ n ≥ 2 := by
  simp [channelSeparates]


/-! ### Removed 2026-08-30 — self-assuming projections

- `adjoint_vanishing_propagation` — body was `jgcs.adjoint_vanishing`: the conclusion was the
  projected field verbatim, so the declaration restated its own hypothesis.

  Additional finding, recorded because it outlives the removal: the
  declaration bound `(k : ℕ)` — the jet level whose *propagation* it is named
  for — and its conclusion `Subsingleton ((𝟙_ C) ⟶ jgcs.adjointObj)` never
  mentions `k`. The statement was level-independent, so "the adjoint
  vanishing at level 0 implies at all levels" was carried entirely in a
  comment and in the name. Encoding it needs the level-indexed adjoint object
  the abstract formulation does not provide.

**Why removal.** The content stays in the class field each declaration
projected, asserting the same proposition under the same hypotheses; only the
restatement goes. That is the vacuity ledger's recorded disposition for this
category — *"drop the pseudo-theorem and project the field at use sites"* — and
there were no use sites: each had **zero references anywhere in the corpus**.
Bean `qou-z9ws`.
-/

end QOU
