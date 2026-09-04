/-
  Categorical transfer matrix.

  A categorical transfer matrix for a hadron H is the equivalence
  class of braiding operations that produce the same vertex volume.
  The key theorem (level independence) states that operating on
  constituent insertion points or on the composite insertion point
  yields the same Skein polynomial.

  ## References
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  - [frenkel2004] https://doi.org/10.1090/surv/088

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Topology.FiberBundle.Basic

namespace QOU

set_option autoImplicit false

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The ordered configuration space Conf_n(𝒮_p): n-tuples of distinct
    insertion points on the exceptional divisor.  The index i labels
    the constituent slot (not the knot type), so multiple slots may
    carry the same simple object. -/
structure InsertionConfig where
  /-- Number of constituent slots. -/
  n : ℕ
  /-- The insertion points z_1, …, z_n as affine coordinates on 𝒮_p. -/
  points : Fin n → R_q  -- In full formalization: Fin n → 𝒮_p
  /-- Distinct insertion points: z_i ≠ z_j for i ≠ j.
      This is the configuration space constraint; collisions
      produce OPE singularities (z_i − z_j)^{−k}. -/
  distinct : ∀ (i j : Fin n), i ≠ j → points i ≠ points j

/-- The interaction bi-filtration on the configuration space algebra.

    Two filtrations act simultaneously:

    1. **Ascending (jet prolongation).**  The brane tower
       A_0 ↪ A_1 ↪ A_2 ↪ ⋯ grows with each Planck step.

    2. **Descending (Hecke relations).**  Within a given jet level,
       each crossing adds a relation to the interaction ideal. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [frenkel2004] Frenkel, "Lectures on the Langlands program and conformal field theory," arXiv:hep-th/0512172 (related: 0007054)
structure InteractionBiFiltration where
  /-- The underlying insertion configuration. -/
  config : InsertionConfig
  /-- Current jet level (Planck step count). -/
  jetLevel : ℕ
  /-- Total number of crossings resolved so far. -/
  numCrossings : ℕ
  /-- Crossing number cannot exceed jet level:
      a knot with c crossings requires at least c Planck steps. -/
  crossings_le_jet : numCrossings ≤ jetLevel
  /-- The ordered sequence of crossing pairs (slot i, slot j). -/
  crossingPairs : Fin numCrossings → Fin config.n × Fin config.n
  /-- Each crossing is between distinct slots. -/
  crossing_distinct : ∀ k, (crossingPairs k).1 ≠ (crossingPairs k).2

/-- The categorical transfer matrix: equivalence class of braiding
    operations on a hadron that produce the same vertex volume. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
structure CategoricalTransferMatrix (B : Type*) (q : R_q) where
  /-- The exceptional divisor where braiding takes place, carried as a
      **type parameter** `B` rather than by naming `ExceptionalDivisor`.

      Two reasons, and the second is the load-bearing one. `ExceptionalDivisor`
      is declared in a *sibling* (`quantum-observable-universes/exceptional-divisor.lean`)
      which this file cannot import — siblings sit outside the Lake globs — and
      in the library as `structure ExceptionalDivisor (M : Type*)` in
      `QOU/ArchimedeanUniverse.lean`, i.e. on the **archimedean** side of the
      §7c wall, while this file is over the categorical `R_q = ℤ[q, q⁻¹]`.
      Naming either here would straddle the wall.

      With `autoImplicit` on, the bare name became an auto-bound variable and
      the errors surfaced three levels downstream, as
      `don't know how to synthesize implicit argument α` on `T₁.base = T₂.base`.
      `set_option autoImplicit false` above makes that a name error instead. -/
  base : B
  /-- The bi-filtration: jet level (ascending) and accumulated
      Hecke relations (descending) at the current Planck step. -/
  filtration : InteractionBiFiltration
  /-- The vertex volume polynomial (the invariant). -/
  vertex_volume : R_q  -- In full formalization: polynomial in q

/-- Adding a crossing while advancing the jet level preserves the
    bi-filtration invariant. -/
theorem InteractionBiFiltration.step_preserves_bound
    (F : InteractionBiFiltration) :
    F.numCrossings ≤ F.jetLevel →
    F.numCrossings + 1 ≤ F.jetLevel + 1 := by omega

/-! ### Level independence — constituent-composite agreement

The narrative claim: the vertex volume of a hadron does not depend on whether
it is computed from constituent insertion points or from the composite
insertion point.

**The axiom that stood here is FALSE as stated.**

`transfer_matrix_level_independence` was a bare `axiom` asserting

    T₁.base = T₂.base → T₁.vertex_volume = T₂.vertex_volume

for the structure above. That does not hold, and cannot: `vertex_volume` is a
**free field**, so two transfer matrices may share a base and carry any two
values whatsoever. The refutation below constructs exactly that.

This is not a quibble about formalisation. It is the `.md`'s own reasoning
being dropped in the encoding: the block says the equivalence is well-defined
*"because the vertex volume depends only on the Markov trace of the
Hecke-reduced element"*. Dependence on the reduction is what makes the claim
true, and carrying the volume as free data discards it — leaving a statement
that is false, asserted as an axiom, and therefore available to prove anything
downstream. -/

/-- The empty insertion configuration, used only to witness the refutation. -/
def trivialConfig : InsertionConfig where
  n := 0
  points := Fin.elim0
  distinct := by intro i; exact i.elim0

/-- The empty bi-filtration, used only to witness the refutation. -/
def trivialFiltration : InteractionBiFiltration where
  config := trivialConfig
  jetLevel := 0
  numCrossings := 0
  crossings_le_jet := le_refl 0
  crossingPairs := Fin.elim0
  crossing_distinct := by intro k; exact k.elim0

/-- **The former axiom is false.**  Same base, different volume: nothing in
    `CategoricalTransferMatrix` ties the two together. -/
theorem level_independence_false_as_stated :
    ¬ ∀ (B : Type) (q : R_q) (T₁ T₂ : CategoricalTransferMatrix B q),
        T₁.base = T₂.base → T₁.vertex_volume = T₂.vertex_volume := by
  intro h
  exact zero_ne_one (h Unit 0
    ⟨(), trivialFiltration, 0⟩ ⟨(), trivialFiltration, 1⟩ rfl)

/-- **Vertex volume DERIVED from the Hecke reduction**, which is what the
    `.md` actually describes.

    `reduce` is the Markov trace of the Hecke-reduced element (abstracted
    here as a function of the bi-filtration); `volume_eq` says a transfer
    matrix's volume *is* that reduction rather than independent data. -/
structure DerivedVertexVolume (B : Type*) (q : R_q) where
  /-- The Hecke-reduced invariant of a bi-filtration. -/
  reduce : InteractionBiFiltration → R_q
  /-- The vertex volume of a transfer matrix. -/
  volume : CategoricalTransferMatrix B q → R_q
  /-- The volume is determined by the reduction — the `.md`'s
      "depends only on the Markov trace of the Hecke-reduced element". -/
  volume_eq : ∀ T, volume T = reduce T.filtration

/-- **Level independence, in the form that is true.**

    Two transfer matrices with the same bi-filtration have the same derived
    volume.  Note the hypothesis is on the **filtration**, not on `base`: the
    braiding data is what the volume depends on, and equal bases say nothing.
    That substitution is the whole content of the correction. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
theorem transfer_matrix_level_independence {B : Type*} {q : R_q}
    (D : DerivedVertexVolume B q) (T₁ T₂ : CategoricalTransferMatrix B q)
    (h_same_braiding : T₁.filtration = T₂.filtration) :
    D.volume T₁ = D.volume T₂ := by
  rw [D.volume_eq, D.volume_eq, h_same_braiding]


end

end QOU
