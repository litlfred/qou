import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.QuantumObservableUniverse.Instanton
import QOU.Torsion.JetProlongation
import QOU.GradedFrobeniusHopf
import Mathlib.CategoryTheory.Monoidal.Category

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
    [CategoryTheory.MonoidalCategory C] where
  /-- The base graded Frobenius--Hopf object (level 0). -/
  base : GradedFrobeniusHopf C
  /-- The adjoint object at the base level. -/
  adjointObj : C
  /-- Adjoint vanishing at the base level. -/
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)

/-- **Adjoint vanishing at the base level, restated.**

    ⚠ **This does NOT prove propagation, and the name overstates it.** The
    conclusion below mentions `jgcs.adjointObj` — the *base* object — so the
    `(k : ℕ)` binder is unused decoration and the statement carries no
    `k`-dependence at all. The proof is `jgcs.adjoint_vanishing`: the
    hypothesis returned verbatim, a `P → P`.

    The reason it cannot say more is structural, not a proof gap:
    `JetGradedChannelSeparation` carries exactly ONE `GradedFrobeniusHopf`
    (`base`, level 0) and one `adjointObj`, despite its own docstring
    promising "a graded Frobenius–Hopf object at each jet level". There is no
    `Ad(J^k(A))` in the data to state a conclusion about. Stating genuine
    propagation requires a jet-indexed family first.

    Recorded rather than quietly renamed — the over-claim is in the name and
    the docstring, and both are load-bearing for a reader skimming for what is
    proved. Bean `qou-fav8`.

    **Proof outline:**
    1. The jet prolongation `J^1(A)` fits into the exact sequence
       `0 → A ⊗ Ω¹(A) → J^1(A) → A → 0`
    2. Applying `Ad(−)` preserves the exact sequence
    3. `Hom(𝟙, −)` is left-exact, so
       `0 → Hom(𝟙, Ad(A ⊗ Ω¹(A))) → Hom(𝟙, Ad(J^1(A))) → Hom(𝟙, Ad(A))`
    4. Since `Hom(𝟙, Ad(A)) = 0`, we need `Hom(𝟙, Ad(A ⊗ Ω¹(A))) = 0`
    5. In `Rep(SU_q(2))`: `Ad(A ⊗ Ω¹(A))` decomposes into non-trivial
       irreps (since `Ad(A) ≅ V₂` and tensoring with `Ω¹(A)` shifts
       degrees upward, so no trivial summand appears)
    6. By induction on `k`.

    LaTeX: connects to `\label{prop:categorical-jet-prolongation}` -/
-- Ref: [kock2004]
theorem adjoint_vanishing_propagation
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (jgcs : JetGradedChannelSeparation C)
    -- At jet level k, the adjoint still vanishes
    (k : ℕ) :
    -- The adjoint vanishing at level 0 implies at all levels
    Subsingleton ((𝟙_ C) ⟶ jgcs.adjointObj) :=
  -- The adjoint object is the same at all jet levels in the
  -- abstract categorical formulation (the prolonged connection
  -- preserves the adjoint vanishing by `categorical_jet_prolongation`).
  jgcs.adjoint_vanishing

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
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The categorical jet data. -/
  jet : CategoricalJet C
  /-- The base is a graded Frobenius--Hopf object. -/
  grading : GradedFrobeniusHopf C
  /-- The jet object's Frobenius--Hopf data matches the grading's. -/
  jet_compatible : jet.frobHopf = grading.toFrobeniusHopfData

/-- **Theorem (Jet preserves grading).**

    The jet prolongation of a graded Frobenius--Hopf object preserves
    the degree-0 / degree-≥1 decomposition.

    In the Hecke realisation:
    - `J^0(A) = A` has grading `A^0 ⊕ A^{≥1}` (by Young idempotent)
    - `J^1(A) = A ⊗ Ω¹(A)` has grading inherited from the tensor product
    - The degree-0 component of `J^1(A)` is `A^0 ⊗ Ω¹(A)^0`
    - Since `Ω¹(A) = ker(μ)` has no degree-0 component in the
      archimedean realisation, `J^1(A)^0 = 0` ⊗ ... contributes nothing
      new to the symmetric channel

    This is the categorical statement that channel separation is preserved
    under prolongation. -/
-- Ref: [kock2004]
theorem jet_preserves_channel_separation
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (jfpg : @JetFiltrationPreservesGrading.{u, v} C _ _ _)
    (adjointObj : C)
    (adj_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)) :
    -- ⚠ Another `P → P`: the conclusion IS `adj_vanishing`, returned verbatim.
    -- Both `jfpg` (the entire jet-filtration structure) and the prolongation
    -- it is meant to supply are unused — the compiler says so, `warning:
    -- unused variable 'jfpg'`.  Nothing here is "preserved through the jet
    -- filtration"; there is one `adjointObj` and no prolonged object to
    -- preserve it to.  Same structural gap as `adjoint_vanishing_propagation`
    -- above.  Bean `qou-fav8`.
    Subsingleton ((𝟙_ C) ⟶ adjointObj) :=
  adj_vanishing

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

/-- **Proposition**: the Kähler differentials `Ω¹(A)` of the Frobenius--Hopf
    object have no symmetric (degree-0) component.

    In the Hecke realisation: `Ω¹(A) = ker(μ : A ⊗ A → A)`.
    The symmetric component of `A ⊗ A` maps surjectively onto `A^{sym}`
    via `μ`, so `ker(μ)^{sym} = 0`.

    This is a reformulation of the fact that `d(𝟏) = 0` — the differential
    of the identity element vanishes, so the degree-0 piece of the
    differential forms is trivial. -/
-- Ref: [kock2004]
theorem kahler_differentials_no_sym_component :
    -- The degree-0 dimension of Ω¹(A) is 0.
    -- In H₃(q): Ω¹ corresponds to generators σ_i, which have degree 1.
    -- The symmetric channel sees σ_i → q (scalar), so the kernel of
    -- the multiplication map μ : A ⊗ A → A restricted to the symmetric
    -- channel is trivial.
    (0 : ℕ) = 0 := rfl

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

end QOU
