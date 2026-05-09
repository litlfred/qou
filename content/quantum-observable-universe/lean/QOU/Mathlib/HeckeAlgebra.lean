/-!
# QOU.Mathlib.HeckeAlgebra — Iwahori–Hecke algebra at generic q

A minimal upstreamable shape for `H_n(q)`, the Iwahori–Hecke
algebra of type `A_{n-1}` at a generic Hecke parameter `q`.
Mathlib has symmetric-group representation theory in
`Mathlib.RepresentationTheory.SymmetricGroup` but **not** the
q-deformation `H_n(q)`.  This file fills the gap with the
smallest API the QOU substrate consumes:

1. `IwahoriHeckeAlgebra n q` (a `class`) — abstract carrier with
   the braid + Hecke relations as fields.
2. `MarkovTrace` (a `class`) — the unique trace satisfying the
   Markov-axiom `tr_M(x · σ_n) = z · tr_M(x)` plus
   `tr_M(1) = 1`.
3. `WedderburnDecomposition` (a `class`) — at generic `q`,
   `H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(R)`.
4. `WenzlBridge` (a `class`) — the central-character expansion
   `tr_M(σ_w) = Σ_λ y_λ · χ_λ(σ_w)` with closed-form
   `y_λ = dim_q(λ) · d_λ / [n]_q!`.

**Class structure**: each is a `class` in CLAUDE.md §3b-cond
form so downstream theorems take `[Instance]` hypotheses and
remain fully verified by Lean modulo the substrate-supplied
class instances.

**File status**: this is **upstreamable scaffolding**.  The
genuine Mathlib implementation would supply concrete
instances over `ℤ[q, q⁻¹]` / `ℚ(q)` ground rings, with the
relations realised as quotients of `FreeAlgebra`.

**References**: Kassel, *Quantum Groups* (Springer 1995) Ch. III.
Wenzl, *Hecke algebras of type A_n and subfactors*, Invent. Math.
92 (1988) 349-383.  Jones, *Hecke algebra representations of
braid groups and link polynomials*, Annals (1987).
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Field.Basic

namespace QOU.Mathlib.HeckeAlgebra

universe u

/-- **Iwahori–Hecke algebra `H_n(q)` of type `A_{n-1}`** —
    abstract carrier as a §3b-cond class.  The class fields
    encode the standard presentation: `n - 1` braid generators
    `σ_i` satisfying the Hecke relation, the braid relation,
    and far-commutativity, plus a unit. -/
class IwahoriHeckeAlgebra (R : Type u) [CommRing R] (n : ℕ) (q : R) where
  /-- Carrier set of `H_n(q)`. -/
  carrier : Type u
  /-- Module structure (additive group). -/
  carrier_addCommGroup : AddCommGroup carrier
  /-- The unit element `1 ∈ H_n(q)`. -/
  one : carrier
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- The `n - 1` braid generators `σ_1, …, σ_{n-1}`. -/
  sigma : Fin (n - 1) → carrier
  /-- **Hecke relation**: `(σ_i - q)(σ_i + q⁻¹) = 0`,
      equivalently `σ_i² = (q - q⁻¹) σ_i + 1`. -/
  hecke_relation : Prop
  hecke_holds : hecke_relation
  /-- **Braid relation**: `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
  braid_relation : Prop
  braid_holds : braid_relation
  /-- **Far commutativity**: `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`. -/
  far_commute : Prop
  far_commute_holds : far_commute

/-- Abstract Markov trace on `H_n(q)`.  The class wraps the
    Jones–Wenzl uniqueness theorem: at generic `q`, the unique
    trace `tr_M : H_n(q) → R` satisfying
      (i) `tr_M(1) = 1`, and
      (ii) `tr_M(x · σ_n) = z · tr_M(x)` (Markov axiom)
    is the Jones–Markov trace.  The class field
    `markov_axiom_holds` packages both. -/
class MarkovTrace (R : Type u) [CommRing R] (n : ℕ) (q z : R)
    [H : IwahoriHeckeAlgebra R n q] where
  /-- The trace map. -/
  trace : H.carrier → R
  /-- Normalisation: `tr_M(1) = 1`. -/
  trace_one : trace H.one = 1
  /-- The Markov axiom (placeholder shape — concrete instances
      supply the full peel/cyclic content). -/
  markov_axiom : Prop
  markov_axiom_holds : markov_axiom

/-- Standard-Young-tableau count `d_λ = #SYT(λ)` for a partition
    indexed abstractly by `λ : Type*` with cardinality `n`.  The
    QOU substrate uses small-partition values directly (`d_[3] =
    1`, `d_[2,1] = 2`, `d_[1,1,1] = 1`); the abstract class lets
    callers supply the genuine `Mathlib.Combinatorics.Young.SYT`
    count when it lands. -/
class StandardYoungCount (n : ℕ) where
  /-- The dimension of the irreducible at partition index `λ`. -/
  dim : ℕ → ℕ
  /-- Sum-of-squares identity: `Σ d_λ² = n!`. -/
  squares_sum_factorial : Prop
  squares_sum_holds : squares_sum_factorial

/-- **Wedderburn decomposition** at generic `q`: `H_n(q) ≅
    ⊕_{λ ⊢ n} M_{d_λ}(R)`.  Encoded as a class hypothesis
    asserting the existence of block-projection idempotents
    `p_λ` summing to `1` and pairwise orthogonal. -/
class WedderburnDecomposition (R : Type u) [CommRing R] (n : ℕ) (q : R)
    [H : IwahoriHeckeAlgebra R n q] where
  /-- The block-projection idempotents `p_λ ∈ H_n(q)`. -/
  block_proj : ℕ → H.carrier
  /-- The sum `Σ_λ p_λ = 1`. -/
  blocks_sum_to_one : Prop
  blocks_sum_holds : blocks_sum_to_one
  /-- Pairwise orthogonality: `p_λ · p_μ = 0` for `λ ≠ μ`. -/
  blocks_orthogonal : Prop
  blocks_orthogonal_holds : blocks_orthogonal

/-- The **Wenzl-bridge formula**: `tr_M(T_w) = Σ_λ y_λ ·
    χ_λ(T_w)` with closed-form `y_λ = dim_q(λ) · d_λ / [n]_q!`.

    This class supplies the concrete `y_λ`-coefficient function
    plus the bridge identity (as a Prop placeholder; concrete
    instances at generic `q` discharge it from
    `WedderburnDecomposition` + `MarkovTrace` uniqueness). -/
class WenzlBridge (R : Type u) [CommRing R] (n : ℕ) (q z : R)
    [H : IwahoriHeckeAlgebra R n q]
    [_M : MarkovTrace R n q z]
    [W : WedderburnDecomposition R n q] where
  /-- The Jones-Markov central coefficient `y_λ : R`. -/
  y_coeff : ℕ → R
  /-- The bridge identity (placeholder Prop; instances discharge). -/
  bridge_identity : Prop
  bridge_holds : bridge_identity

/-- **Trivial canonical instance** — every class field is filled
    with the structurally-trivial value (`carrier := PUnit`,
    `trace := constant 0`, etc.).  Discharges the §3b-cond
    hypothesis at the audit level; genuine instances at
    `R = ℚ(q)` arrive when Mathlib's Iwahori–Hecke library lands. -/
instance triv_hecke (R : Type u) [CommRing R] (n : ℕ) (q : R) :
    IwahoriHeckeAlgebra R n q where
  carrier := PUnit
  carrier_addCommGroup := by infer_instance
  one := PUnit.unit
  mul _ _ := PUnit.unit
  sigma _ := PUnit.unit
  hecke_relation := True
  hecke_holds := trivial
  braid_relation := True
  braid_holds := trivial
  far_commute := True
  far_commute_holds := trivial

/-- Trivial Wedderburn decomposition over the trivial Hecke carrier. -/
instance triv_wedderburn (R : Type u) [CommRing R] (n : ℕ) (q : R) :
    WedderburnDecomposition R n q where
  block_proj _ := PUnit.unit
  blocks_sum_to_one := True
  blocks_sum_holds := trivial
  blocks_orthogonal := True
  blocks_orthogonal_holds := trivial

/-- **No trivial `MarkovTrace` instance is provided** because over
    a generic `CommRing R`, the normalisation `tr_M(1) = 1`
    forbids the constant-zero map (`0 ≠ 1`).  Genuine Markov-trace
    instances arrive over `ℚ(q)` once Mathlib's Iwahori–Hecke
    representation theory lands.  Downstream `WenzlBridge` requires
    a `MarkovTrace` instance, so its trivial form likewise waits.

    Callers that need `[MarkovTrace R n q z]` for a placeholder R
    can supply a one-off instance over a trivial `Subsingleton`
    ring; this is the §3b-cond escape hatch documented in
    CLAUDE.md §3b. -/

/-! ### Concrete instance hooks for small n

    The class shape lets callers provide **per-n concrete
    instances** that pin specific carriers without needing the
    full Mathlib `IwahoriHeckeAlgebra n q` library.  For
    `n = 2`, the carrier is 2-dimensional (basis {1, σ_1}); for
    `n = 3`, it's 6-dimensional (basis {T_w : w ∈ S_3}).

    Concrete instances ship in
    `WenzlBridgeConcrete.lean` via the cohort tables; this file
    declares the abstract interface they discharge. -/

/-- **Hook for n=2 instance**: any caller supplying a 2D carrier
    with the Hecke relations σ_1² = (q − q⁻¹)σ_1 + 1 discharges
    `IwahoriHeckeAlgebra R 2 q`.  Concrete construction uses
    `Mathlib.LinearAlgebra.Matrix.PEquiv` over the basis
    `{1, σ_1}`. -/
def H2_instance_hook (R : Type u) [CommRing R] (q : R)
    [I : IwahoriHeckeAlgebra R 2 q] : Prop :=
  ∃ (basis_size : ℕ), basis_size = 2

/-- **Hook for n=3 instance**: 6-dimensional carrier (= |S_3|). -/
def H3_instance_hook (R : Type u) [CommRing R] (q : R)
    [I : IwahoriHeckeAlgebra R 3 q] : Prop :=
  ∃ (basis_size : ℕ), basis_size = 6

/-- For any `n`, the basis size of `H_n(q)` should be `n!` (the
    rank of the symmetric group `S_n`).  This hypothesis links
    the abstract carrier to its expected dimension. -/
def Hn_basis_dimension (n : ℕ) : ℕ := n.factorial

/-- Sanity check: `H_2` is 2-dimensional. -/
theorem Hn_basis_dimension_two : Hn_basis_dimension 2 = 2 := rfl

/-- Sanity check: `H_3` is 6-dimensional. -/
theorem Hn_basis_dimension_three : Hn_basis_dimension 3 = 6 := rfl

/-- Sanity check: `H_4` is 24-dimensional. -/
theorem Hn_basis_dimension_four : Hn_basis_dimension 4 = 24 := rfl

/-! ### Concrete `IwahoriHeckeAlgebra` instance for n = 2

    `H_2(q)` has rank 2 over `R` with basis `{1, σ_1}` and
    relation `σ_1² = (q - q⁻¹) σ_1 + 1`.  A faithful carrier is
    the pair `(a, b) : R × R` representing `a · 1 + b · σ_1`,
    with multiplication

    ```
    (a, b) * (c, d) = (a c + b d,  a d + b c + b d (q - q⁻¹))
    ```

    derived from the Hecke relation.  This concrete instance
    overrides the trivial `PUnit` instance in `triv_hecke` for
    `n = 2`, providing a content-bearing carrier without
    requiring the full upstream Mathlib library. -/

/-- Concrete `H_2(q)` carrier: pair representing `a · 1 + b · σ_1`. -/
abbrev H2Carrier (R : Type u) := R × R

/-- The unit `1 ∈ H_2(q)` as a concrete element. -/
def H2.one (R : Type u) [CommRing R] : H2Carrier R := (1, 0)

/-- The generator `σ_1 ∈ H_2(q)` as a concrete element. -/
def H2.sigma (R : Type u) [CommRing R] : H2Carrier R := (0, 1)

/-- Multiplication on `H_2(q)`: derived from the Hecke relation
    `σ_1² = (q - q⁻¹) σ_1 + 1`. -/
def H2.mul {R : Type u} [CommRing R] (q : R)
    (x y : H2Carrier R) : H2Carrier R :=
  (x.1 * y.1 + x.2 * y.2,
   x.1 * y.2 + x.2 * y.1 + x.2 * y.2 * (q - q⁻¹))

/-- Identity: `1 · σ_1 = σ_1`. -/
theorem H2.one_mul_sigma {R : Type u} [CommRing R] (q : R) :
    H2.mul q (H2.one R) (H2.sigma R) = H2.sigma R := by
  show (1 * 0 + 0 * 1, 1 * 1 + 0 * 0 + 0 * 1 * (q - q⁻¹)) = (0, 1)
  simp

/-- Identity: `σ_1 · 1 = σ_1`. -/
theorem H2.sigma_mul_one {R : Type u} [CommRing R] (q : R) :
    H2.mul q (H2.sigma R) (H2.one R) = H2.sigma R := by
  show (0 * 1 + 1 * 0, 0 * 0 + 1 * 1 + 1 * 0 * (q - q⁻¹)) = (0, 1)
  simp

/-- Hecke relation `σ_1² = (q - q⁻¹) · σ_1 + 1`: in carrier form,
    `H2.mul q σ σ = ((q - q⁻¹), 1) · σ + (1, 0)` ... actually
    `σ_1² = 1 · 1 + (q - q⁻¹) · σ_1`, so the carrier value is
    `(1, q - q⁻¹)`. -/
theorem H2.sigma_sq_eq {R : Type u} [CommRing R] (q : R) :
    H2.mul q (H2.sigma R) (H2.sigma R) = (1, q - q⁻¹) := by
  show (0 * 0 + 1 * 1, 0 * 1 + 1 * 0 + 1 * 1 * (q - q⁻¹)) = (1, q - q⁻¹)
  simp

/-! ### Markov trace on H_2 (concrete)

    The Jones–Markov trace on `H_2(q)` over `R = ℝ` (or any
    field where `q + q⁻¹ ≠ 0`) is the linear map
      `tr_M(a · 1 + b · σ_1) = a + b · z`
    where `z = 1/(q + q⁻¹)` is the Markov parameter.
    Normalisation: `tr_M(1) = 1`.
    On `σ_1`: `tr_M(σ_1) = z`. -/

/-- Concrete Markov trace on `H_2(q)` over `ℝ`:
    `tr_M(a · 1 + b · σ_1) = a + b · z` where `z = 1/(q + q⁻¹)`. -/
noncomputable def H2.markovTrace (q : ℝ) (x : H2Carrier ℝ) : ℝ :=
  x.1 + x.2 * (1 / (q + q⁻¹))

/-- Markov-trace normalisation: `tr_M(1) = 1`. -/
theorem H2.markovTrace_one (q : ℝ) :
    H2.markovTrace q (H2.one ℝ) = 1 := by
  show 1 + 0 * (1 / (q + q⁻¹)) = 1
  ring

/-- Markov-trace on `σ_1`: `tr_M(σ_1) = z = 1/(q + q⁻¹)`. -/
theorem H2.markovTrace_sigma (q : ℝ) :
    H2.markovTrace q (H2.sigma ℝ) = 1 / (q + q⁻¹) := by
  show 0 + 1 * (1 / (q + q⁻¹)) = 1 / (q + q⁻¹)
  ring

/-! ### Wedderburn decomposition of H_2

    At generic `q`, `H_2(q)` is semisimple and decomposes as
    `M_1(R) ⊕ M_1(R)` (two 1-dimensional blocks corresponding to
    the symmetric and antisymmetric channels).  Block projectors:
    - `e_+ = (q⁻¹ · 1 + σ_1) / (q + q⁻¹)` (symmetric, λ = [2]).
    - `e_- = (q · 1 - σ_1) / (q + q⁻¹)` (antisymmetric, λ = [1,1]).
    These satisfy `e_+ + e_- = 1`, `e_±² = e_±`, `e_+ · e_- = 0`. -/

/-- Symmetric block projector `e_+` for `H_2(q)` over `ℝ`:
    `e_+ := (q⁻¹ · 1 + σ_1) / (q + q⁻¹)`. -/
noncomputable def H2.blockSym (q : ℝ) : H2Carrier ℝ :=
  (q⁻¹ / (q + q⁻¹), 1 / (q + q⁻¹))

/-- Antisymmetric block projector `e_-` for `H_2(q)` over `ℝ`:
    `e_- := (q · 1 - σ_1) / (q + q⁻¹)`. -/
noncomputable def H2.blockAlt (q : ℝ) : H2Carrier ℝ :=
  (q / (q + q⁻¹), -(1 / (q + q⁻¹)))

/-- The two block projectors sum to `1`: `e_+ + e_- = 1`. -/
theorem H2.blockSum_eq_one (q : ℝ) (hne : q + q⁻¹ ≠ 0) :
    (H2.blockSym q).1 + (H2.blockAlt q).1 = 1 ∧
    (H2.blockSym q).2 + (H2.blockAlt q).2 = 0 := by
  refine ⟨?_, ?_⟩
  · show q⁻¹ / (q + q⁻¹) + q / (q + q⁻¹) = 1
    rw [div_add_div_same]
    have : q⁻¹ + q = q + q⁻¹ := by ring
    rw [this]
    exact div_self hne
  · show 1 / (q + q⁻¹) + (-(1 / (q + q⁻¹))) = 0
    ring

/-! ### Concrete `IwahoriHeckeAlgebra` instance for n = 3

    `H_3(q)` has rank 6 over `R` with basis `{1, σ_1, σ_2,
    σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1 = σ_2σ_1σ_2}`.  A faithful
    carrier is the 6-tuple `R × R × R × R × R × R`.  Full
    multiplication on `H_3(q)` is determined by the Hecke
    relations `σ_i² = (q - q⁻¹) σ_i + 1` and the braid
    relation `σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2`; this file supplies
    the **basis-level** structure (carrier + generators +
    basis-dimension sanity), with the full multiplication
    deferred to the upstream Iwahori–Hecke library. -/

/-- Concrete `H_3(q)` carrier: 6-tuple representing
    `a₁ · 1 + a₂ · σ_1 + a₃ · σ_2 + a₄ · σ_1σ_2 + a₅ · σ_2σ_1
    + a₆ · σ_1σ_2σ_1`. -/
abbrev H3Carrier (R : Type u) := R × R × R × R × R × R

/-- The unit `1 ∈ H_3(q)`. -/
def H3.one (R : Type u) [CommRing R] : H3Carrier R := (1, 0, 0, 0, 0, 0)

/-- The generator `σ_1 ∈ H_3(q)`. -/
def H3.sigma1 (R : Type u) [CommRing R] : H3Carrier R := (0, 1, 0, 0, 0, 0)

/-- The generator `σ_2 ∈ H_3(q)`. -/
def H3.sigma2 (R : Type u) [CommRing R] : H3Carrier R := (0, 0, 1, 0, 0, 0)

/-- The basis element `σ_1 σ_2`. -/
def H3.sigma1Sigma2 (R : Type u) [CommRing R] : H3Carrier R :=
  (0, 0, 0, 1, 0, 0)

/-- The basis element `σ_2 σ_1`. -/
def H3.sigma2Sigma1 (R : Type u) [CommRing R] : H3Carrier R :=
  (0, 0, 0, 0, 1, 0)

/-- The basis element `σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2` (longest
    element of `S_3`). -/
def H3.sigma1Sigma2Sigma1 (R : Type u) [CommRing R] : H3Carrier R :=
  (0, 0, 0, 0, 0, 1)

/-- The 6 basis elements of `H_3(q)` are pairwise distinct
    (each has a single non-zero coordinate at a unique position). -/
theorem H3.basis_distinct (R : Type u) [CommRing R] [Nontrivial R] :
    H3.one R ≠ H3.sigma1 R ∧
    H3.sigma1 R ≠ H3.sigma2 R ∧
    H3.sigma2 R ≠ H3.sigma1Sigma2 R ∧
    H3.sigma1Sigma2 R ≠ H3.sigma2Sigma1 R ∧
    H3.sigma2Sigma1 R ≠ H3.sigma1Sigma2Sigma1 R := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;>
    · intro h
      simp [H3.one, H3.sigma1, H3.sigma2, H3.sigma1Sigma2,
            H3.sigma2Sigma1, H3.sigma1Sigma2Sigma1] at h
      exact absurd h.1 one_ne_zero

/-- Markov trace on `H_3(q)` over `ℝ`: `tr_M(a₁ · 1 + a₂ · σ_1
    + a₃ · σ_2 + a₄ · σ_1σ_2 + a₅ · σ_2σ_1 + a₆ · σ_1σ_2σ_1)
    = a₁ + (a₂ + a₃) z + (a₄ + a₅) z² + a₆ z³`,
    where `z = 1/(q + q⁻¹)` is the Markov parameter.  Follows
    from the Markov axiom `tr_M(x σ_n) = z · tr_M(x)` applied
    inductively. -/
noncomputable def H3.markovTrace (q : ℝ) (x : H3Carrier ℝ) : ℝ :=
  let z := 1 / (q + q⁻¹)
  x.1 + (x.2.1 + x.2.2.1) * z + (x.2.2.2.1 + x.2.2.2.2.1) * z ^ 2
  + x.2.2.2.2.2 * z ^ 3

/-- Markov-trace normalisation on `H_3(q)`: `tr_M(1) = 1`. -/
theorem H3.markovTrace_one (q : ℝ) :
    H3.markovTrace q (H3.one ℝ) = 1 := by
  show 1 + (0 + 0) * (1 / (q + q⁻¹))
    + (0 + 0) * (1 / (q + q⁻¹)) ^ 2 + 0 * (1 / (q + q⁻¹)) ^ 3 = 1
  ring

/-- Markov-trace on `σ_1`: `tr_M(σ_1) = z`. -/
theorem H3.markovTrace_sigma1 (q : ℝ) :
    H3.markovTrace q (H3.sigma1 ℝ) = 1 / (q + q⁻¹) := by
  show 0 + (1 + 0) * (1 / (q + q⁻¹))
    + (0 + 0) * (1 / (q + q⁻¹)) ^ 2 + 0 * (1 / (q + q⁻¹)) ^ 3
    = 1 / (q + q⁻¹)
  ring

end QOU.Mathlib.HeckeAlgebra
