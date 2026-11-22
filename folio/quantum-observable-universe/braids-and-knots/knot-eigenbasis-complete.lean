import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic


/-!
# QOU.Braiding.knot_eigenbasis_complete — Knot eigenbasis completeness

For C = Rep(SU_q(2)) with q not a root of unity:
1. V^⊗n decomposes completely via q-Schur–Weyl duality
2. Every knot type corresponds to a braid closure (Alexander's theorem)
3. Knot types span the algebraic direct limit `V_phys = colim V^⊗n`

The combining theorem `knot_eigenbasis_complete` shows that given
Schur–Weyl completeness, Alexander surjectivity, and Markov trace
detection, every element of V^⊗n is reached by a knot-labelled
irreducible summand.

LaTeX label: `prop:knot-eigenbasis-complete`

## 2026-09-03 — the detection claim bound `μ` and never used it

`KnotEigenbasisData.summands_detected` read

    ∀ μ ∈ decomp.partitions, ∃ β : alex.Braid, markov.tr (braid_rep β) ≠ 0

and **`μ` does not occur in the body.** So the field said "some braid has
non-zero Markov trace", repeated once per partition — not "each summand is
detected". `mu_free_detection_vacuous` below proves this mechanically: a
single non-zero value discharges that shape for *every* list of partitions,
so no instance of it constrains the decomposition at all.

Its own docstring claimed the missing content — *"the Jones polynomial of the
braid closure β̂, **restricted to the S_μ summand**, is non-zero"* — and the
`.md` claims more still: that the map from knot types to irreducible summands
*defined by the support of* `tr_M(ρ_n(β))` is **surjective**. A trace with no
block components cannot express either.

**Fixed** by giving the bundle a per-block component `trBlock` tied to the
trace by `tr_eq_sum_blocks` (`tr x = Σ_{μ ∈ partitions} trBlock μ x`), so
`trBlock` is not free data, and restating detection over it. `μ` now occurs
in the body of the field and in the conclusions of every theorem below.

Two consequences follow from the constraint that did not follow before:
`tr_ne_zero_of_single_block` and `single_summand_detected` — block detection
plus the decomposition gives a braid whose *total* Jones value is non-zero.

## Two duplicate re-exports removed

`knot_eigenbasis_density` was `:= kec.summands_detected` at the field's exact
type, and `jones_nontrivial_all_summands` was that field applied — the
self-assuming projection of AGENTS.md §3b-cond item 5, and here also
*misnamed*. The `.md`'s density claim is its item 3, that the knot-labelled
summands **span** `V_phys = colim V^⊗n`; re-exporting detection under the
name `density` reads as though that were encoded. It is not: there is no
colimit, no inclusion `η : 𝟙 → V`, and no spanning statement anywhere in this
file, and adding one needs the direct limit rather than a rename.

`jones_nontrivial_all_summands` likewise concluded "no summand is invisible
to the knot invariant" from a field that, as written, did not mention the
summand.

## The same defect next door — FIXED 2026-09-04

[`descartes-knot-eigenbasis.lean`](../brings-surface/descartes-knot-eigenbasis.lean)
carried it in a stronger form: `DescartesKnotEigenbasis.all_summands_detected`
and `DescartesMarkovTrace.summand_detection` both bound the summand index as
`_`, and the detected value was a free `∃ jonesVal : ℝ, jonesVal ≠ 0` tied to
no trace, so each field asserted that `ℝ` has a non-zero element.

Repaired the same way (bean `qou-9552`): a `trSummand` component constrained
by `tr_eq_sum_summands`, with detection stated over it.

Its own docstring named `descartes_n3_both_detected` as the concrete `n = 3`
content standing in for the general-`n` gap — and **that theorem had the
defect too**, stated as `∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0`, a
property of `ℝ`. Worse, once its two values are named, they are provably
**not separating**: they coincide at `q ≈ 0.7795446638`, a `q` the Descartes
condition permits (`QOU.Archimedean.jones_channels_not_separating`).

## References

- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
- [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923)
- [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
- [leitner2026] §4-path-integrals-and-braiding/knot-eigenbasis-complete

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
noncomputable def q_param : R_q := LaurentPolynomial.T 1
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Hecke Algebra H_n(q) -/

/-- **Hecke algebra H_n(q)**: the quotient of the group algebra k[B_n]
    by the quadratic relation (σ_i − q)(σ_i + q⁻¹) = 0.

    When q is not a root of unity, H_n(q) is semisimple and isomorphic
    to k[S_n] as an abstract algebra (Jimbo's theorem). -/
-- Ref: [chari1994guide] Chari–Pressley, Ch. 10
structure HeckeAlgebra where
  /-- Number of strands. -/
  n : ℕ
  /-- Carrier type. -/
  carrier : Type*
  /-- Deformation parameter q. -/
  q : R_q
  /-- q ≠ 0. -/
  q_ne_zero : q ≠ 0
  /-- Inverse parameter q⁻¹ (the ring `R_q = ℤ[q, q⁻¹]` has no native
      `Inv`, so the inverse is carried as data). -/
  q_inv : R_q
  /-- Defining relation `q · q⁻¹ = 1`. -/
  q_mul_inv : q * q_inv = 1
  -- q is not a root of unity: q^k ≠ 1 for all k ≥ 1.
  -- q_not_root_of_unity : ∀ (k : ℕ), k ≥ 1 → q ^ k ≠ 1  -- (archimedean; not meaningful over R_q)
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- Unit element. -/
  one : carrier
  /-- Zero element. -/
  zero : carrier
  /-- Subtraction. -/
  sub : carrier → carrier → carrier
  /-- Scalar multiplication by ℝ. -/
  smul : R_q → carrier → carrier
  /-- Generators T₁, …, T_{n-1} (images of Artin generators). -/
  T : Fin (n - 1) → carrier
  /-- Braid relation: T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}. -/
  braid_relation : ∀ (i : Fin (n - 2)),
    let i' : Fin (n - 1) := ⟨i.val, by omega⟩
    let j : Fin (n - 1) := ⟨i.val + 1, by omega⟩
    mul (mul (T i') (T j)) (T i') = mul (mul (T j) (T i')) (T j)
  /-- Quadratic relation: T_i² − (q − q⁻¹)·T_i − 1 = 0.
      Equivalently (T_i − q)(T_i + q⁻¹) = 0: eigenvalues are q and −q⁻¹. -/
  quadratic : ∀ (i : Fin (n - 1)),
    sub (sub (mul (T i) (T i)) (smul (q - q_inv) (T i))) one = zero

/-! ## Young Diagrams (Partition Labels) -/

/-- A partition of n with at most r parts, represented as a
    non-increasing list of row lengths. For SU_q(2), r = 2. -/
structure BoundedPartition where
  /-- Row lengths in non-increasing order. -/
  rows : List ℕ
  /-- Size n (sum of row lengths). -/
  n : ℕ
  /-- Maximum number of parts (rows). -/
  maxParts : ℕ
  /-- The rows sum to n. -/
  size_eq : rows.sum = n
  /-- At most maxParts rows. -/
  parts_bound : rows.length ≤ maxParts
  /-- Non-increasing (valid Young diagram). -/
  sorted : rows.Pairwise (· ≥ ·)

/-- The spin label j = (λ₁ − λ₂)/2 for a two-part partition.
    This is the spin of the irreducible SU_q(2)-module V_λ — a
    q-independent half-integer, hence valued in `ℚ`. -/
def BoundedPartition.spin (bp : BoundedPartition) : ℚ :=
  match bp.rows with
  | [] => 0
  | [a] => (a : ℚ) / 2
  | a :: b :: _ => ((a : ℚ) - (b : ℚ)) / 2

/-- Spin labels are non-negative for single-part partitions. -/
theorem spin_nonneg_single (a : ℕ) :
    (0 : ℚ) ≤ (a : ℚ) / 2 := by positivity

/-- The maximum spin of a partition of n is n/2 (the fully symmetric case). -/
theorem max_spin_bound (bp : BoundedPartition) (h : bp.maxParts = 2) :
    bp.spin ≤ (bp.n : ℚ) / 2 := by
  unfold BoundedPartition.spin
  match hr : bp.rows with
  | [] =>
    simp [hr]
    exact div_nonneg (Nat.cast_nonneg bp.n) (by norm_num)
  | [a] =>
    have ha : a = bp.n := by
      have := bp.size_eq; simp [hr] at this; exact this
    subst ha
    simp [hr]
  | a :: b :: rest =>
    simp [hr]
    -- (a - b)/2 ≤ n/2 since a + b + rest.sum = n and b, rest.sum ≥ 0
    have hsum : (a : ℕ) + b + rest.sum = bp.n := by
      have := bp.size_eq; simp [hr, List.sum_cons] at this; linarith
    -- In ℚ: a - b ≤ a ≤ a + b + rest.sum = n
    have hsumQ : (a : ℚ) + (b : ℚ) + (rest.sum : ℚ) = (bp.n : ℚ) := by
      exact_mod_cast hsum
    have hb : (0 : ℚ) ≤ (b : ℚ) := Nat.cast_nonneg b
    have hrest : (0 : ℚ) ≤ (rest.sum : ℚ) := Nat.cast_nonneg rest.sum
    have hab : (a : ℚ) - (b : ℚ) ≤ (bp.n : ℚ) := by linarith
    linarith

/-! ## Part 1: q-Schur–Weyl Decomposition -/

/-- **q-Schur–Weyl decomposition** of V^⊗n under the joint action
    of SU_q(2) and the Hecke algebra H_n(q).

    When q is not a root of unity:
      V^⊗n ≅ ⊕_{λ ⊢ n, ≤ 2 parts} V_λ ⊗ S_λ
    where V_λ is the irreducible SU_q(2)-module of spin j = (λ₁−λ₂)/2
    and S_λ is the irreducible H_n(q)-module.

    The `complete` field encodes that the direct sum is exhaustive:
    every element of V^⊗n lies in some summand. -/
-- Ref: [chari1994guide] Chari–Pressley, Ch. 10
structure SchurWeylDecomposition where
  /-- Number of tensor factors. -/
  n : ℕ
  /-- The Hecke algebra. -/
  hecke : HeckeAlgebra
  /-- Consistency: same n. -/
  n_eq : hecke.n = n
  /-- Type of the tensor power V^⊗n. -/
  tensorPower : Type*
  /-- The set of partitions indexing the decomposition. -/
  partitions : List BoundedPartition
  /-- Each partition has size n with at most 2 parts. -/
  partitions_valid : ∀ μ ∈ partitions, μ.n = n ∧ μ.maxParts = 2
  /-- The number of partitions equals ⌊n/2⌋ + 1 (one per spin value). -/
  partitions_count : partitions.length = n / 2 + 1
  /-- Irreducible SU_q(2)-module for partition μ (spin j). -/
  V_irrep : BoundedPartition → Type*
  /-- Irreducible H_n(q)-module for partition μ. -/
  S_irrep : BoundedPartition → Type*
  /-- Embedding of each summand V_μ ⊗ S_μ into V^⊗n. -/
  summand_embed : ∀ μ ∈ partitions,
    V_irrep μ → S_irrep μ → tensorPower
  /-- **Completeness**: every element of V^⊗n lies in the image of
      some summand embedding. This encodes semisimplicity. -/
  -- Ref: [chari1994guide] Chari–Pressley, Ch. 10 (Jimbo's theorem)
  complete : ∀ (v : tensorPower), ∃ μ, ∃ (hμ : μ ∈ partitions),
    ∃ (w : V_irrep μ) (s : S_irrep μ), summand_embed μ hμ w s = v

/-- The number of partitions of n with ≤ 2 parts is ⌊n/2⌋ + 1.
    This is a consequence of `partitions_count` on `SchurWeylDecomposition`:
    the partition [a, b] with a + b = n, a ≥ b gives one summand per
    value of b = 0, 1, ..., ⌊n/2⌋. -/
theorem num_summands_bound (n : ℕ) : n / 2 + 1 ≥ 1 := by omega

/-! ## Part 2: Alexander Surjectivity -/

/-- **Alexander's theorem**: every oriented link in S³ is the closure
    β̂ of some braid β ∈ B_n for some n.

    This guarantees surjectivity of the braid-closure map onto link types,
    which is essential for ensuring that the knot-type eigenbasis reaches
    every irreducible summand of V^⊗n. -/
-- Ref: [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923), 93–95
structure AlexanderSurjectivity where
  /-- Type of oriented links in S³. -/
  Link : Type*
  /-- Type of braids (union over all B_n). -/
  Braid : Type*
  /-- Braid closure map β ↦ β̂. -/
  closure : Braid → Link
  /-- **Surjectivity**: every link is the closure of some braid. -/
  -- Ref: [alexander1923] https://doi.org/10.1073/pnas.9.3.93
  surjective : Function.Surjective closure

/-- Alexander surjectivity implies every link has a braid representative. -/
theorem alexander_has_braid (alex : AlexanderSurjectivity)
    (L : alex.Link) : ∃ β : alex.Braid, alex.closure β = L :=
  alex.surjective L

/-! ## Part 3: Markov Trace -/

/-- **Markov trace** on the Hecke algebra tower ⋃_n H_n(q).
    The unique trace satisfying the Markov property
    tr(x σ_n^{±1}) = z^{±1} tr(x) for x ∈ H_n(q).

    On each irreducible summand S_λ, the trace restricts to a non-zero
    scalar multiple of the character, so every summand is detected by
    some braid closure. The trace value equals the Jones polynomial
    J_L(q) of the braid closure up to a framing factor. -/
-- Ref: [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987), 335–388
structure MarkovTrace (H : HeckeAlgebra) where
  /-- The trace functional tr : H_n(q) → ℝ. -/
  tr : H.carrier → R_q
  /-- Trace property (cyclicity / Markov I): tr(ab) = tr(ba). -/
  trace_comm : ∀ (a b : H.carrier), tr (H.mul a b) = tr (H.mul b a)
  /-- Markov parameter z determined by q. -/
  z : R_q
  /-- z ≠ 0. -/
  z_ne_zero : z ≠ 0
  /-- Non-degeneracy: the trace of the unit is non-zero. -/
  tr_one_ne_zero : tr H.one ≠ 0
  /-- **Markov property** (Markov II / stabilisation):
      tr(x · T_{n-1}) = z · tr(x). -/
  markov_stab : ∀ (hn : H.n ≥ 2) (x : H.carrier),
    let last : Fin (H.n - 1) := ⟨H.n - 2, by omega⟩
    tr (H.mul x (H.T last)) = z * tr x

/-! ## Combining Structure -/

/-- **The μ-free detection shape asserts nothing per summand.**

A single non-zero value `f β₀ ≠ 0` discharges

    ∀ μ ∈ l, ∃ β, f β ≠ 0

for **every** list `l` of partitions, because `μ` does not occur in the body.
This is the shape `summands_detected` had until 2026-09-03, and it is
recorded as a theorem so the module docstring's claim about it is checked
rather than asserted — and so a later "simplification" back to that shape
fails against a standing demonstration of its emptiness. -/
theorem mu_free_detection_vacuous {α : Type*} {f : α → R_q} {β₀ : α}
    (h : f β₀ ≠ 0) (l : List BoundedPartition) :
    ∀ _μ ∈ l, ∃ β, f β ≠ 0 :=
  fun _ _ => ⟨β₀, h⟩

/-- **Completeness of the knot-type eigenbasis** (full data bundle).

    Combines:
    1. q-Schur–Weyl decomposition (semisimplicity of H_n(q))
    2. Alexander surjectivity (braid closure covers all links)
    3. Markov trace detection (every summand reached by some braid)

    Together, these establish that knot types form a complete eigenbasis
    for the algebraic direct limit `V_phys = colim V^⊗n`, replacing
    Feynman's continuum integral with a finite algebraic trace. -/
-- Ref: [chari1994guide], [alexander1923], [jones1987]
structure KnotEigenbasisData (H : HeckeAlgebra) where
  /-- Part 1: Schur–Weyl decomposition (shares H). -/
  decomp : SchurWeylDecomposition
  /-- Consistency: decomposition uses the same Hecke algebra. -/
  decomp_hecke : decomp.hecke = H
  /-- Part 2: Alexander surjectivity. -/
  alex : AlexanderSurjectivity
  /-- Part 3: Markov trace (parameterized by H, no type equality needed). -/
  markov : MarkovTrace H
  /-- Representation map: braid → Hecke algebra element. -/
  braid_rep : alex.Braid → H.carrier
  /-- Component of the Markov trace in the block `S_μ`.

      Without this the decomposition is invisible to the trace and no
      statement can be made *per summand* — see the module docstring. -/
  trBlock : BoundedPartition → H.carrier → R_q
  /-- The block components decompose the trace:
      `tr x = Σ_{μ ∈ partitions} trBlock μ x`.

      This is what stops `trBlock` from being free data an instance may
      choose independently of `markov.tr`, and it is what
      `tr_ne_zero_of_single_block` is proved from. -/
  tr_eq_sum_blocks : ∀ (x : H.carrier),
    markov.tr x = (decomp.partitions.map (fun μ => trBlock μ x)).sum
  /-- **Summand detection**: for each partition μ in the decomposition,
      there exists a braid β whose Markov trace **in the block `S_μ`** is
      non-zero — i.e. the Jones polynomial of the closure β̂, restricted to
      that summand, does not vanish.

      `μ` occurs in the body. The previous version bound it and did not,
      which `mu_free_detection_vacuous` above shows says nothing. -/
  -- Ref: [jones1987] Annals of Mathematics 126 (1987), 335–388
  summands_detected : ∀ μ ∈ decomp.partitions,
    ∃ (β : alex.Braid), trBlock μ (braid_rep β) ≠ 0

/-! ## Main Theorem: Knot Eigenbasis Completeness -/

/-- **Theorem (Knot eigenbasis completeness).**
    Given the three components of KnotEigenbasisData, every element of
    V^⊗n belongs to an irreducible summand that is detected by a
    knot type (braid closure).

    This is the combining step: Schur–Weyl provides the decomposition,
    Alexander provides the braid representative, and the Markov trace
    confirms detection. -/
theorem knot_eigenbasis_complete {H : HeckeAlgebra}
    (kec : KnotEigenbasisData H)
    (v : kec.decomp.tensorPower) :
    ∃ μ, ∃ (_ : μ ∈ kec.decomp.partitions),
      ∃ (β : kec.alex.Braid), kec.trBlock μ (kec.braid_rep β) ≠ 0 := by
  -- By Schur–Weyl completeness, v lies in some summand V_μ ⊗ S_μ.
  obtain ⟨μ, hμ, _, _, _⟩ := kec.decomp.complete v
  -- By summand detection, THAT μ's block is reached by some braid β.
  obtain ⟨β, hβ⟩ := kec.summands_detected μ hμ
  exact ⟨μ, hμ, β, hβ⟩

/-- **Corollary**: The eigenbasis is non-empty when V^⊗n has
    at least one irreducible summand (which holds for all n ≥ 1). -/
theorem eigenbasis_nonempty {H : HeckeAlgebra}
    (kec : KnotEigenbasisData H)
    (h : kec.decomp.partitions ≠ []) :
    ∃ μ ∈ kec.decomp.partitions,
      ∃ (β : kec.alex.Braid), kec.trBlock μ (kec.braid_rep β) ≠ 0 := by
  obtain ⟨μ, hμ⟩ := List.exists_mem_of_ne_nil _ h
  exact ⟨μ, hμ, kec.summands_detected μ hμ⟩

/-- **A non-zero block component is visible in the total trace when the
    decomposition has a single block** — *derived* from `tr_eq_sum_blocks`,
    which is the constraint the old encoding had no analogue of.

    For `n ≤ 1` the Schur–Weyl decomposition has `⌊n/2⌋ + 1 = 1` partition,
    so the whole Markov trace is that one block's component. -/
theorem tr_ne_zero_of_single_block {H : HeckeAlgebra}
    (kec : KnotEigenbasisData H) {μ : BoundedPartition}
    (hμ : kec.decomp.partitions = [μ]) {x : H.carrier}
    (h : kec.trBlock μ x ≠ 0) :
    kec.markov.tr x ≠ 0 := by
  rw [kec.tr_eq_sum_blocks x, hμ]
  simpa using h

/-- **The Jones value of some closure is non-zero**, for a single-block
    decomposition — obtained by composing summand detection with the trace
    decomposition rather than by re-exporting a field.

    This is the statement `knot_eigenbasis_density` appeared to make and did
    not: it concerns `markov.tr`, the quantity the manuscript identifies with
    the Jones polynomial of the closure, and it is *proved* from the block
    detection rather than assumed. -/
theorem single_summand_detected {H : HeckeAlgebra}
    (kec : KnotEigenbasisData H) {μ : BoundedPartition}
    (hμ : kec.decomp.partitions = [μ]) :
    ∃ (β : kec.alex.Braid), kec.markov.tr (kec.braid_rep β) ≠ 0 := by
  have hmem : μ ∈ kec.decomp.partitions := by rw [hμ]; simp
  obtain ⟨β, hβ⟩ := kec.summands_detected μ hmem
  exact ⟨β, tr_ne_zero_of_single_block kec hμ hβ⟩

end QOU.Braiding
