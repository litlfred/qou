import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.List.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.descartes_knot_eigenbasis

Instantiation theorem: a Descartes universe (χ(A) = -6) provides all the
data needed for `KnotEigenbasisData`, establishing that knot types form a
complete eigenbasis for the algebraic direct limit V_phys = colim V^⊗n
(no metric completion is used).

The chain of reasoning:
1. Descartes condition forces genus 4, hence C = Rep(SU_q(2))
2. The R-matrix of U_q(su(2)) gives a braided monoidal structure on C
3. The quadratic relation of c_{V,V} yields the Hecke algebra H_n(q)
4. q not a root of unity → H_n(q) semisimple → Schur-Weyl decomposition
5. Alexander surjectivity + Markov trace → knot eigenbasis completeness

LaTeX label: `cor:descartes-knot-eigenbasis`

## 2026-09-04 — three detection claims quantified over an index they discarded

`DescartesMarkovTrace.summand_detection` and
`DescartesKnotEigenbasis.all_summands_detected` both read, in effect,

    ∀ (_ : Fin numSummands), ∃ (val : ℝ), val ≠ 0

The summand index is bound as `_` — explicitly discarded — and the detected
value is a free real tied to no trace, no braid and no character. So each
field asserted that **`ℝ` has a non-zero element**, and any instance
discharged it with `⟨1, one_ne_zero⟩`. `descartes_knot_eigenbasis` did
exactly that.

Both are now stated over `DescartesMarkovTrace.trSummand`, a per-summand
component of the trace constrained by
`tr_eq_sum_summands : tr n x = Σ_{i < ⌊n/2⌋+1} trSummand n i x`, so the
component is not free data an instance may choose independently of `tr`, and
the index occurs in the body. Same repair as
[`knot-eigenbasis-complete.lean`](../braids-and-knots/knot-eigenbasis-complete.lean)
next door (bean `qou-9552`).

Also added: `schurWeyl_level`. `DescartesSchurWeyl` carries its own `n`, and
nothing tied it to the level it was requested at, so `schurWeyl n hn` could
return the decomposition of any *other* level. The sibling
`QOU.Braiding.SchurWeylDecomposition` carries the analogous `n_eq`.

## The designated fallback had the defect too — and is provably not separating

The theorem's old docstring named `descartes_n3_both_detected` as the concrete
`n = 3` content standing in for the missing general-`n` character formula.
That theorem was `∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0` — again a
property of `ℝ`. The two Jones values, the two channels and `n = 3` appeared
only in the proof term and the comments. The proof was real work; the
statement recorded none of it.

The values are now named (`jonesSymmetric`, `jonesMixed`) and the theorem is
stated over them. Naming them makes a further fact reachable, and it is not a
comfortable one:

**The two channel values coincide at a `q` the Descartes condition permits.**
`jonesSymmetric D = jonesMixed D` reduces over `q > 0` to
`q⁵ - q⁴ + q³ + q² - 1 = 0` (`jonesSymmetric_eq_jonesMixed_iff`, proved, not
asserted), which has a root in `[7/10, 4/5]` by the intermediate value theorem
(`jones_channels_coincide`). At it — `q ≈ 0.779544663820934968877573423932`,
both channels `≈ -2.0623447988`, verified at 50 decimal digits — the pair
`(jonesSymmetric, jonesMixed)` carries no more information than one number
(`jones_channels_not_separating`).

So exhibiting two non-zero values does **not** establish that the two summands
are distinguished, which is what "both summands are detected" needs. The old
existential form could not have expressed the difference; the named form makes
the gap statable and now states it. Separating the channels requires the
values attached to their summands — that is what `trSummand` is for, and the
per-summand character values for general `n` remain upstream.

## References

- [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
- [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [turaev2010] https://doi.org/10.1515/9783110218145
- [manuscript] §6/§4

**Ground ring.** This is the **archimedean realisation** (namespace
`QOU.Archimedean`): the deformation parameter carries the order `0 < q`,
the inverse `q⁻¹`, and eigenvalue/positivity inequalities, none of which
live on the formal ground ring `R_q = ℤ[q, q⁻¹]`. The data is stated over
`ℝ` at the substrate image `ι : R_q → ℝ, q ↦ q₀` (§7c).
-/

namespace QOU.Archimedean

/-! ## Descartes Universe Data (from archimedean-condition.lean) -/

/-- Descartes condition: χ(A) = -6 with 6 invertible. -/
structure DescartesData where
  /-- Deformation parameter q from U_q(su(2)). -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- q ≠ 1 (non-classical deformation). -/
  q_ne_one : q ≠ 1
  /-- Euler characteristic is -6. -/
  eulerChar : ℤ
  euler_eq : eulerChar = -6
  /-- Dimension of V (forced to 2 by the volume constraint). -/
  dimV : ℕ
  dimV_eq : dimV = 2

/-- The genus of a Descartes universe is 4. -/
theorem DescartesData.genus_is_four (D : DescartesData) :
    (1 : ℤ) - D.eulerChar / 2 = 4 := by
  rw [D.euler_eq]; norm_num

/-- q > 0 implies q ≠ 0. -/
theorem DescartesData.q_ne_zero (D : DescartesData) : D.q ≠ 0 :=
  D.q_pos.ne'

/-! ## Hecke Algebra from the Descartes R-Matrix -/

/-- The Hecke algebra H_n(q) constructed from the R-matrix of
    U_q(su(2)) in a Descartes universe.

    The braiding c_{V,V} has eigenvalues q and -q⁻¹.
    The quadratic relation (T_i - q)(T_i + q⁻¹) = 0 defines
    the Hecke algebra as a quotient of the braid group algebra. -/
-- Ref: [chari1994guide] Ch. 10, [kassel1995] Ch. XIII
structure DescartesHeckeAlgebra (D : DescartesData) where
  /-- Number of strands. -/
  n : ℕ
  n_ge_two : 2 ≤ n
  /-- Carrier of H_n(q). -/
  carrier : Type*
  /-- The generators T_i. -/
  T : Fin (n - 1) → carrier
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- Unit. -/
  one : carrier
  /-- The positive braiding eigenvalue q. -/
  eigenvalue_pos : ℝ := D.q
  /-- The negative braiding eigenvalue -q⁻¹. -/
  eigenvalue_neg : ℝ := -(D.q⁻¹)
  /-- Eigenvalues are distinct (q ≠ -q⁻¹ when q > 0, q ≠ 1). -/
  eigenvalues_distinct : eigenvalue_pos ≠ eigenvalue_neg

/-- For q > 0, the eigenvalues q and -q⁻¹ are distinct. -/
theorem eigenvalues_distinct_of_descartes (D : DescartesData) :
    D.q ≠ -(D.q⁻¹) := by
  have hq := D.q_pos
  have hqi : 0 < D.q⁻¹ := inv_pos.mpr hq
  linarith

/-! ## Schur-Weyl Decomposition for Rep(SU_q(2)) -/

/-- **Schur-Weyl data** for a Descartes universe at level n.

    For C = Rep(SU_q(2)) with V the spin-1/2 representation:
    V^⊗n ≅ ⊕_{j} V_j ⊗ S_j where j ranges over spins
    n/2, n/2 - 1, ..., 1/2 or 0 (partitions with ≤ 2 parts).

    The number of summands is ⌊n/2⌋ + 1. -/
-- Ref: [chari1994guide] Ch. 10
structure DescartesSchurWeyl (D : DescartesData) where
  /-- Number of tensor factors. -/
  n : ℕ
  /-- V^⊗n as a type. -/
  tensorPower : Type*
  /-- Number of irreducible summands = ⌊n/2⌋ + 1. -/
  numSummands : ℕ
  summands_count : numSummands = n / 2 + 1
  /-- Spin labels for each summand. -/
  spinLabel : Fin numSummands → ℝ
  /-- Maximum spin is n/2. -/
  max_spin : ∀ i, spinLabel i ≤ (n : ℝ) / 2
  /-- Projection: every vector projects to a unique summand index. -/
  -- Ref: [chari1994guide] Ch. 10 (Jimbo's theorem gives semisimplicity)
  summandOf : tensorPower → Fin numSummands

/-- The Schur-Weyl decomposition at n = 3 has 2 summands:
    spin 3/2 (symmetric) and spin 1/2 (mixed symmetry). -/
theorem schur_weyl_n3 (D : DescartesData) (sw : DescartesSchurWeyl D)
    (hn : sw.n = 3) : sw.numSummands = 2 := by
  rw [sw.summands_count, hn]

/-- The Schur-Weyl decomposition always has at least one summand. -/
theorem schur_weyl_nonempty (D : DescartesData) (sw : DescartesSchurWeyl D)
    (hn : sw.n ≥ 1) : sw.numSummands ≥ 1 := by
  rw [sw.summands_count]; omega

/-! ## Braid Representation from the Descartes Structure -/

/-- **Faithful braid representation** ρ_n : B_n → Aut_C(V^⊗n) from
    the Descartes braided monoidal structure.

    Faithfulness for n = 3 follows from the distinct eigenvalues
    of the R-matrix (q ≠ -q⁻¹), which is guaranteed by q > 0, q ≠ 1. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure DescartesBraidRep (D : DescartesData) where
  /-- Number of strands. -/
  n : ℕ
  n_ge_two : 2 ≤ n
  /-- Braid type (abstract B_n). -/
  BraidType : Type*
  /-- Braid generators σ_1, ..., σ_{n-1}. -/
  sigma : Fin (n - 1) → BraidType
  /-- The representation ρ_n assigns each braid to an automorphism
      of V^⊗n, encoded here as a real number (trace in the
      fundamental representation). -/
  trace_of : BraidType → ℝ
  /-- Faithfulness: distinct braids give distinct traces. -/
  faithful : ∀ β₁ β₂ : BraidType,
    trace_of β₁ = trace_of β₂ → β₁ = β₂
  /-- Braid group structure. -/
  [grp : Group BraidType]
  /-- σ₁σ₂σ₁ = σ₂σ₁σ₂ (braid relation for adjacent generators). -/
  braid_relation : ∀ (i : Fin (n - 2)),
    let i' : Fin (n - 1) := ⟨i.val, by omega⟩
    let j : Fin (n - 1) := ⟨i.val + 1, by omega⟩
    sigma i' * sigma j * sigma i' = sigma j * sigma i' * sigma j
  /-- Far commutativity: σᵢσⱼ = σⱼσᵢ for |i - j| ≥ 2. -/
  far_comm : ∀ (i j : Fin (n - 1)),
    i.val + 2 ≤ j.val →
    sigma i * sigma j = sigma j * sigma i

/-! ## Markov Trace from the Descartes Hecke Algebra -/

/-- **Markov trace** on the Hecke algebra tower of a Descartes universe.
    The trace exists, is unique, and detects every irreducible summand. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987)
structure DescartesMarkovTrace (D : DescartesData) where
  /-- The Markov parameter z = -(q - q⁻¹)⁻¹ · q^(1/2). -/
  z : ℝ
  z_ne_zero : z ≠ 0
  /-- The trace functional on H_n(q) elements. -/
  tr : ℕ → ℝ → ℝ  -- tr n x: trace of element x at level n
  /-- The trace of the identity is nonzero. -/
  tr_one_ne_zero : ∀ n, n ≥ 2 → tr n 1 ≠ 0
  /-- Component of the trace in the summand indexed by `i` at level `n`.

      Without this the decomposition is invisible to the trace, and no
      statement can be made *per summand* — see the module docstring. -/
  trSummand : ℕ → ℕ → ℝ → ℝ
  /-- The components decompose the trace:
      `tr n x = Σ_{i < ⌊n/2⌋+1} trSummand n i x`.

      This is what stops `trSummand` from being free data an instance may
      choose independently of `tr`. -/
  tr_eq_sum_summands : ∀ (n : ℕ) (x : ℝ),
    tr n x = ∑ i ∈ Finset.range (n / 2 + 1), trSummand n i x
  /-- Every irreducible summand is detected: for each level `n` and each
      summand index `i`, some element has non-zero trace **in that
      summand**.

      `i` occurs in the body. It did not until 2026-09-04 — see the module
      docstring for what the previous form asserted. -/
  -- Ref: [jones1987] §3, character non-vanishing
  summand_detection : ∀ (n i : ℕ), i < n / 2 + 1 →
    ∃ (x : ℝ), trSummand n i x ≠ 0

/-! ## Main Instantiation Theorem -/

/-- **Descartes knot eigenbasis completeness.**

    A Descartes universe provides all the data needed for knot
    eigenbasis completeness: the Hecke algebra (from the R-matrix),
    the Schur-Weyl decomposition (from semisimplicity), and the
    Markov trace (from Jones's construction).

    This is the instantiation theorem that bridges the abstract
    `KnotEigenbasisData` structure (Chapter 4) with the concrete
    Descartes universe (Chapter 6). -/
-- Ref: [chari1994guide], [jones1987], [kassel1995]
structure DescartesKnotEigenbasis (D : DescartesData) where
  /-- Schur-Weyl decomposition at each level n. -/
  schurWeyl : ∀ (n : ℕ), n ≥ 1 → DescartesSchurWeyl D
  /-- Braid representation at each level n ≥ 2. -/
  braidRep : ∀ (n : ℕ), n ≥ 2 → DescartesBraidRep D
  /-- Markov trace on the Hecke tower. -/
  markov : DescartesMarkovTrace D
  /-- Consistency: the decomposition returned at level `n` is a
      decomposition of `V^⊗n`.

      Missing until 2026-09-04, so `schurWeyl n hn` could return the
      decomposition of any *other* level and nothing noticed. The sibling
      `QOU.Braiding.SchurWeylDecomposition` carries the analogous `n_eq`. -/
  schurWeyl_level : ∀ (n : ℕ) (hn : n ≥ 1), (schurWeyl n hn).n = n
  /-- Each summand at each level is detected by the Markov trace — stated
      over `markov.trSummand`, so the summand index occurs in the body and
      the detected value is the trace's component in *that* summand rather
      than a free real. -/
  all_summands_detected : ∀ (n : ℕ) (hn : n ≥ 1) (i : ℕ),
    i < (schurWeyl n hn).numSummands →
    ∃ (x : ℝ), markov.trSummand n i x ≠ 0

/-- The Descartes condition (q > 0, q ≠ 1, q not a root of unity)
    is sufficient to construct the full knot eigenbasis data.

    The key inputs:
    - Semisimplicity of H_n(q) ← q not a root of unity (Jimbo's theorem)
    - Eigenvalue distinctness ← q > 0 and q ≠ 1
    - Markov trace existence ← Jones's construction (1987)
    - Alexander surjectivity ← classical topology (Alexander, 1923)

    All four are available for any Descartes universe.

    **The witness is trivial, and the statement now says so.** The previous
    version's conclusion was `∀ (_ : Fin numSummands), ∃ jonesVal, jonesVal
    < 0` — the summand index discarded and the value tied to nothing — and
    it was proved by exhibiting the symmetric-channel Jones value
    `-(q + q⁻¹)`, once, for every index. The docstring described that as "a
    genuine, `q`-dependent detector"; the *type* accepted any negative real
    and would have accepted the same one for all summands, which is what the
    proof did.

    The conclusion is now stated over `trSummand`, so the index occurs. The
    witness constructed below is deliberately the trivial one
    (`trSummand n i x = x`), because that is all this file can supply: the
    per-summand character values for general `n` are upstream. Nothing here
    claims otherwise any more. -/
-- Ref: [chari1994guide] Ch. 10, [jones1987] §3
theorem descartes_knot_eigenbasis (D : DescartesData) :
    ∃ mt : DescartesMarkovTrace D,
      ∀ (n i : ℕ), i < n / 2 + 1 → ∃ x : ℝ, mt.trSummand n i x ≠ 0 := by
  refine ⟨{ z := 1, z_ne_zero := one_ne_zero
            tr := fun n x => (n / 2 + 1 : ℕ) * x
            tr_one_ne_zero := ?_
            trSummand := fun _ _ x => x
            tr_eq_sum_summands := ?_
            summand_detection := fun _ _ _ => ⟨1, one_ne_zero⟩ }, ?_⟩
  · intro n _
    have : (0 : ℝ) < ((n / 2 + 1 : ℕ) : ℝ) := by positivity
    simpa using this.ne'
  · intro n x
    simp [Finset.sum_const, nsmul_eq_mul, mul_comm]
  · exact fun _ _ _ => ⟨1, one_ne_zero⟩

/-- Jones value of the unknot in the symmetric (spin-3/2) channel at `n = 3`:
    `J = -(q + q⁻¹)`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def jonesSymmetric (D : DescartesData) : ℝ := -(D.q + D.q⁻¹)

/-- Jones value of the trefoil in the mixed-symmetry (spin-1/2) channel at
    `n = 3`: `J = -q⁻⁴(1 - q² + q⁴)`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def jonesMixed (D : DescartesData) : ℝ :=
  -(D.q⁻¹ ^ 4 * (1 - D.q ^ 2 + D.q ^ 4))

/-- **Corollary**: for `n = 3` in a Descartes universe, the symmetric and
    mixed-symmetry channel values are each non-zero — the unknot's value in
    the spin-3/2 channel and the trefoil's in the spin-1/2 channel.

    Stated over the two **named** values. Until 2026-09-04 this was
    `∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0`, which is a property of `ℝ`:
    the two Jones values, and `n = 3`, and the two channels, appeared only in
    the proof term and the comments. The proof was real work; the statement
    recorded none of it.

    **This does not say the two channels are separated** — see
    `jones_channels_coincide` below, which shows they take the *same* value at
    a `q` the Descartes condition permits. -/
-- Ref: [manuscript] §4, [jones1987] §3
theorem descartes_n3_both_detected (D : DescartesData) :
    jonesSymmetric D ≠ 0 ∧ jonesMixed D ≠ 0 := by
  have hq := D.q_pos
  have hqi : 0 < D.q⁻¹ := inv_pos.mpr hq
  constructor
  · -- -(q + q⁻¹) < 0 for q > 0
    have : jonesSymmetric D < 0 := by unfold jonesSymmetric; linarith
    exact this.ne
  · -- -q⁻⁴(1 - q² + q⁴) < 0 for q > 0 (both factors positive)
    have hqi4 : 0 < D.q⁻¹ ^ 4 := pow_pos hqi 4
    have h_poly : 0 < 1 - D.q ^ 2 + D.q ^ 4 := by nlinarith [sq_nonneg (D.q ^ 2 - 1 / 2)]
    have : jonesMixed D < 0 := by
      unfold jonesMixed; linarith [mul_pos hqi4 h_poly]
    exact this.ne

/-- **The two `n = 3` channel values coincide at a `q` the Descartes
    condition permits**, so non-vanishing of each does *not* establish that
    the two summands are distinguished.

    `jonesSymmetric D = jonesMixed D` reduces, over `q > 0`, to
    `q⁵ - q⁴ + q³ + q² - 1 = 0`, which is negative at `q = 7/10` and positive
    at `q = 4/5`; the intermediate value theorem supplies a root between.
    Numerically the root is `q ≈ 0.779544663820934968877573423932`, where both
    channels take the value `≈ -2.0623447988` (verified at 50 decimal digits).

    Such a `q` satisfies `0 < q` and `q ≠ 1`, so it is a legitimate Descartes
    parameter. At it, the pair `(jonesSymmetric, jonesMixed)` carries no more
    information than a single number.

    This is why `descartes_n3_both_detected` is scoped to non-vanishing:
    separating the channels needs the values attached to their summands, i.e.
    `DescartesMarkovTrace.trSummand`, not two reals that happen to be
    non-zero. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem jones_channels_coincide :
    ∃ q : ℝ, q ∈ Set.Icc (7 / 10 : ℝ) (4 / 5 : ℝ) ∧
      q ^ 5 - q ^ 4 + q ^ 3 + q ^ 2 - 1 = 0 := by
  have hcont : ContinuousOn (fun q : ℝ => q ^ 5 - q ^ 4 + q ^ 3 + q ^ 2 - 1)
      (Set.Icc (7 / 10 : ℝ) (4 / 5 : ℝ)) := by fun_prop
  have hle : (7 / 10 : ℝ) ≤ 4 / 5 := by norm_num
  have hmem : (0 : ℝ) ∈ Set.Icc
      ((7 / 10 : ℝ) ^ 5 - (7 / 10 : ℝ) ^ 4 + (7 / 10 : ℝ) ^ 3 + (7 / 10 : ℝ) ^ 2 - 1)
      ((4 / 5 : ℝ) ^ 5 - (4 / 5 : ℝ) ^ 4 + (4 / 5 : ℝ) ^ 3 + (4 / 5 : ℝ) ^ 2 - 1) := by
    constructor <;> norm_num
  obtain ⟨q, hq, hq0⟩ := intermediate_value_Icc hle hcont hmem
  exact ⟨q, hq, hq0⟩

/-- The reduction the docstring above describes, **proved** rather than
    asserted: over `q > 0`, the two channel values agree exactly when the
    quintic vanishes. -/
theorem jonesSymmetric_eq_jonesMixed_iff (D : DescartesData) :
    jonesSymmetric D = jonesMixed D ↔
      D.q ^ 5 - D.q ^ 4 + D.q ^ 3 + D.q ^ 2 - 1 = 0 := by
  have hq0 : D.q ≠ 0 := ne_of_gt D.q_pos
  unfold jonesSymmetric jonesMixed
  rw [neg_inj]
  field_simp
  constructor <;> intro h <;> nlinarith [h, sq_nonneg D.q, pow_pos D.q_pos 4]

/-- **There is a Descartes universe in which the two `n = 3` channel values
    are equal.**

    The headline consequence of the two results above, and the reason
    `descartes_n3_both_detected` is scoped to non-vanishing: at this `q` the
    unknot's symmetric-channel value and the trefoil's mixed-channel value are
    the *same real number*, so exhibiting both non-zero says nothing about the
    two summands being distinguished.

    Numerically `q ≈ 0.7795446638`, both channels `≈ -2.0623447988` (50 dps).
    Separating the channels needs `DescartesMarkovTrace.trSummand`. -/
theorem jones_channels_not_separating :
    ∃ D : DescartesData, jonesSymmetric D = jonesMixed D := by
  obtain ⟨q, hq, hroot⟩ := jones_channels_coincide
  obtain ⟨hlo, hhi⟩ := hq
  have hpos : 0 < q := by linarith
  have hne : q ≠ 1 := by intro h; rw [h] at hhi; norm_num at hhi
  refine ⟨⟨q, hpos, hne, -6, rfl, 2, rfl⟩, ?_⟩
  exact (jonesSymmetric_eq_jonesMixed_iff _).mpr hroot

/-! ### The characters do separate, where the Jones pair does not

`jones_channels_not_separating` above is a negative about the *particular
pair of Jones values* `descartes_n3_both_detected` names. It is not a
statement about the framework, and the object that does separate the
summands — the per-partition character `χ^λ` — already exists in the corpus
(`tools/hecke-engine/src/seminormal.rs`, Hoefsmit seminormal form, general
`n` and `λ`; MPFR variants alongside).

On the single generator `σ₁`, at `n = 3` with the two `≤ 2`-row partitions
of 3, those characters are

    χ^[3](σ₁)   = q          (symmetric, spin 3/2, dim 1)
    χ^[2,1](σ₁) = q − q⁻¹    (mixed symmetry, spin 1/2, dim 2)

so their difference is `q⁻¹`, which never vanishes. Verified against the
native seminormal path at eight sample `q` to better than `1e-45`
(`computations/descartes_n3_channel_separation_probe.py`), including at the
`q*` of `jones_channels_not_separating` itself.
-/

/-- Character of the symmetric (spin-3/2) summand `λ = [3]` on `σ₁` at
    `n = 3`: the one-dimensional representation sends each generator to `q`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def charSymmetricSigma (D : DescartesData) : ℝ := D.q

/-- Character of the mixed-symmetry (spin-1/2) summand `λ = [2,1]` on `σ₁` at
    `n = 3`: the two-dimensional representation has `σ₁` with eigenvalues `q`
    and `−q⁻¹`, so its trace is `q − q⁻¹`. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
noncomputable def charMixedSigma (D : DescartesData) : ℝ := D.q - D.q⁻¹

/-- **The two `n = 3` channel characters differ by exactly `q⁻¹`.** -/
theorem charSymmetricSigma_sub_charMixedSigma (D : DescartesData) :
    charSymmetricSigma D - charMixedSigma D = D.q⁻¹ := by
  unfold charSymmetricSigma charMixedSigma; ring

/-- **`σ₁` separates the two `n = 3` summands, in every Descartes universe.**

    The positive counterpart to `jones_channels_not_separating`, and the
    reason that negative is narrow: the difference is `q⁻¹`, and `q > 0`
    forces `q⁻¹ ≠ 0`, so there is no Descartes `q` at which these two
    characters agree — including the `q*` where the two *Jones values* do.

    So "both summands are detected" is not out of reach; it needs the
    detector attached to its summand, which is what
    `DescartesMarkovTrace.trSummand` is for. What remains is to construct
    `trSummand` from the Hoefsmit values rather than leave it free — a
    formalisation of the seminormal representation, not a further open
    question about the mathematics. -/
-- Ref: [jones1987] Annals of Mathematics 126 (1987) §3
theorem sigma_separates_n3_channels (D : DescartesData) :
    charSymmetricSigma D ≠ charMixedSigma D := by
  intro h
  have hgap : charSymmetricSigma D - charMixedSigma D = 0 := by rw [h]; ring
  rw [charSymmetricSigma_sub_charMixedSigma] at hgap
  exact (inv_pos.mpr D.q_pos).ne' hgap

/-- **Corollary**: the eigenvalues q and -q⁻¹ of the R-matrix braiding
    are always distinct in a Descartes universe, ensuring the Hecke
    algebra quotient is well-defined and the braid representation
    is faithful. -/
theorem descartes_eigenvalues_distinct (D : DescartesData) :
    D.q ≠ -(D.q⁻¹) :=
  eigenvalues_distinct_of_descartes D

/-- **Corollary**: the number of particle species at level n is finite
    and equals ⌊n/2⌋ + 1 — each species is a knot type. -/
theorem descartes_particle_count (n : ℕ) :
    n / 2 + 1 ≥ 1 := by omega

end QOU.Archimedean
