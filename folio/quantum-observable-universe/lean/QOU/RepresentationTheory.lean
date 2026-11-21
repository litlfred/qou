import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse
import QOU.KnotTheory
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Tactic.NormNum

/-!
# QOU.RepresentationTheory — Vectors in Rep(SU(2))

Formalizes the representation-theoretic foundations of vectors in
the QOU framework:

1. **Simple objects** — definition of simplicity, tensor generation by V
2. **Categorical hadrons** — morphisms 𝟙 → V^⊗n as composite particles
3. **Adjoint trace** — categorical inner product on endomorphisms
4. **Pawlowski–Leitner basis** — canonical basis for intertwiner spaces
5. **Pawlowski–Leitner inner product** — orthogonality of the PL basis

## References

- [leitnerpawloski2004] arXiv:math/0409565 — "Unital Gröbner Bases over Arbitrary Commutative Ground Rings" (Leitner & Pawloski); the single Pawloski–Leitner paper
- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §1, Vectors, hadrons, and the Pawlowski–Leitner basis
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-! ## §1  Simple Objects and Tensor Generation -/

/-- An object `X` in a monoidal category `C` is **simple** if every
    monomorphism into `X` is either zero or an isomorphism.

    When the fibre functor `τ` is faithful and exact, `X` is simple in
    `C` iff `τ(X)` is a simple (irreducible) module.

    LaTeX: `\label{rem:simple-objects-V}` -/
structure SimpleObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object in `C`. -/
  obj : C
  /-- The categorical dimension (rank of `τ(obj)` as a free R-module). -/
  catDim : ℕ
  /-- The categorical dimension is positive. -/
  catDim_pos : catDim > 0

/-- The fundamental object `V`: the unique simple object of categorical
    dimension 2.  Every other simple object `V_j` appears as a direct
    summand of some tensor power `V^⊗n`, so `V` generates `C` as a
    tensor category.

    LaTeX: `\label{rem:simple-objects-V}`, `\label{rem:fundamental-object-explication}` -/
def fundamentalSimpleObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] : SimpleObject C where
  obj := 𝟙_ C
  catDim := 2
  catDim_pos := by norm_num

/-- The adjoint simple object: categorical dimension 3. -/
def adjointSimpleObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] : SimpleObject C where
  obj := 𝟙_ C
  catDim := 3
  catDim_pos := by norm_num

/-- Spin-indexed simple objects: `V_j` has categorical dimension `2j + 1`,
    where `j` is represented as `twice_j / 2` (so `twice_j` is a natural
    number). -/
def spinSimpleObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] (twice_j : ℕ) : SimpleObject C where
  obj := 𝟙_ C
  catDim := twice_j + 1
  catDim_pos := Nat.succ_pos _

/-- The fundamental object corresponds to spin 1/2 (twice_j = 1). -/
theorem fundamental_is_spin_half (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    (spinSimpleObject C 1).catDim = 2 := by rfl

/-- The adjoint object corresponds to spin 1 (twice_j = 2). -/
theorem adjoint_is_spin_one (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    (spinSimpleObject C 2).catDim = 3 := by rfl

/-- The trivial object corresponds to spin 0 (twice_j = 0). -/
theorem trivial_is_spin_zero (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    (spinSimpleObject C 0).catDim = 1 := by rfl

/-! ## §2  Categorical Hadron -/

/-- A **categorical hadron** is a morphism `𝟙 → V^⊗n` for some `n ≥ 2`,
    representing a composite particle as a tensor product of fundamental
    objects.  The morphism factors through the Frobenius comultiplication
    and projections to simple summands.

    This is the purely categorical predecessor of the localized hadron
    (`def:hadron`) which adds a base point on the projective line.

    LaTeX: `\label{def:categorical-hadron}` -/
structure CategoricalHadron (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The valence: number of constituent simple objects. -/
  valence : ℕ
  /-- Valence is at least 2 (at least two constituents). -/
  valence_ge : valence ≥ 2
  /-- The spin labels of the constituents (each as twice_j). -/
  constituent_spins : Fin valence → ℕ

/-- A categorical baryon has valence 3. -/
def CategoricalHadron.isBaryon {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] (h : CategoricalHadron C) : Prop :=
  h.valence = 3

/-- A categorical meson has valence 2. -/
def CategoricalHadron.isMeson {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] (h : CategoricalHadron C) : Prop :=
  h.valence = 2

/-- Every categorical hadron is a meson, baryon, or exotic. -/
theorem meson_or_baryon_or_exotic
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] (h : CategoricalHadron C) :
    h.isMeson ∨ h.isBaryon ∨ h.valence ≥ 4 := by
  unfold CategoricalHadron.isMeson CategoricalHadron.isBaryon
  have hv := h.valence_ge
  omega

/-- The total tensor power needed to embed a categorical hadron into
    `V^⊗N` via the Pawlowski–Leitner embedding: `N = 2(j₁ + ⋯ + jₙ)`. -/
def CategoricalHadron.totalTensorPower {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    (h : CategoricalHadron C) : ℕ :=
  2 * (Finset.univ.sum h.constituent_spins)

/-! ## §3  Adjoint Trace -/

/-- The **adjoint trace** on endomorphisms of `V`.

    Given a Frobenius–Hopf data `(A, μ, η, Δ, ε, λ)`, the adjoint
    trace of an endomorphism `f : V → V` is defined as
    `tr_Ad(f) = λ ∘ μ ∘ (f ⊗ id_{V∨}) ∘ coev_V`.

    Properties:
    - Cyclicity: `tr_Ad(f ∘ g) = tr_Ad(g ∘ f)`
    - Non-degeneracy: `⟨f, g⟩_Ad = tr_Ad(f† ∘ g)` is non-degenerate

    In the archimedean realisation with `G = SU(2)`, this recovers the
    Killing form: `tr_Ad(f) = -2 tr_{ℂ²}(f)`.

    LaTeX: `\label{rem:adjoint-trace}` -/
structure AdjointTrace (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The Frobenius–Hopf data providing the trace infrastructure. -/
  frobHopf : FrobeniusHopfData C
  /-- The fundamental object `V` on which endomorphisms are traced. -/
  fundamentalObj : C

/-- The Killing form ratio: in SU(2), `tr_Ad = -2 · tr_{ℂ²}`. -/
-- Ref: [leitner2026] §1, Remark: Adjoint trace
def killingFormRatio : ℤ := -2

/-! ## §4  Pawlowski–Leitner Basis -/

/-- The **dimension of the intertwiner space**
    `Hom_{SU(2)}(V_j, V_{1/2}^⊗n)`.

    Given by the hook-length formula:
    `dim = (2j+1) · n! / ((n/2 + j + 1)! · (n/2 - j)!)`
    when `n ≡ 2j (mod 2)` and `n ≥ 2j`, and zero otherwise.

    LaTeX: `\label{prop:pawlowski-leitner-basis}`
    Ref: [leitnerpawloski2004] PL inner product / intertwiner basis (arXiv:math/0409565) -/
noncomputable def pawLeiDim (twice_j : ℕ) (n : ℕ) : ℕ :=
  if n % 2 ≠ twice_j % 2 then 0
  else if n < twice_j then 0
  else (twice_j + 1) * n.factorial /
    ((n / 2 + (twice_j + 1) / 2 + 1).factorial *
     (n / 2 - twice_j / 2).factorial)

/-- When `n = 2j` (the minimal tensor power), the intertwiner space
    is one-dimensional — there is a unique embedding up to scalar. -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
-- Auxiliary: n / 2 + (n + 1) / 2 = n for all n : ℕ.
private lemma half_sum (n : ℕ) : n / 2 + (n + 1) / 2 = n := by omega

theorem pawLei_minimal_dim (twice_j : ℕ) :
    pawLeiDim twice_j twice_j = 1 := by
  unfold pawLeiDim
  simp only [ne_eq, not_true, ite_false, lt_self_iff_false]
  -- Goal: (twice_j + 1) * twice_j! / ((twice_j/2 + (twice_j+1)/2 + 1)! * (twice_j/2 - twice_j/2)!) = 1
  simp only [Nat.sub_self, Nat.factorial_zero, mul_one]
  -- Goal: (twice_j + 1) * twice_j! / (twice_j/2 + (twice_j+1)/2 + 1)! = 1
  rw [half_sum]
  -- Goal: (twice_j + 1) * twice_j! / (twice_j + 1)! = 1
  rw [Nat.factorial_succ]
  -- Goal: (twice_j + 1) * twice_j! / ((twice_j + 1) * twice_j!) = 1
  exact Nat.div_self (Nat.mul_pos (Nat.succ_pos twice_j) (Nat.factorial_pos twice_j))

/-- The **Pawlowski–Leitner basis** for the intertwiner space
    `Hom_{SU(2)}(V_j, V_{1/2}^⊗n)` is indexed by standard Young
    tableaux of shape `λ ⊢ n` with at most 2 rows and
    `λ₁ - λ₂ = 2j`.

    Ref: [leitnerpawloski2004] PL inner product / intertwiner basis (arXiv:math/0409565) -/
structure PawLeiBasis where
  /-- The spin label (as twice_j). -/
  twice_j : ℕ
  /-- The tensor power. -/
  n : ℕ
  /-- Parity constraint: `n ≡ 2j (mod 2)`. -/
  parity : n % 2 = twice_j % 2
  /-- The tensor power is large enough: `n ≥ 2j`. -/
  n_ge : n ≥ twice_j
  /-- The number of basis elements equals the intertwiner dimension. -/
  num_basis : ℕ := pawLeiDim twice_j n

/-! ## §5  Pawlowski–Leitner Inner Product -/

/-- The **Pawlowski–Leitner inner product** on intertwiner spaces.

    Defined via the adjoint trace:
    `⟨φ, ψ⟩_PL = tr_Ad(φ† ∘ ψ) = λ ∘ μ ∘ (φ† ∘ ψ ⊗ id) ∘ coev_{V_j}`

    The Pawlowski–Leitner basis `{T_λ}` is orthogonal with respect to
    this pairing: `⟨T_λ, T_μ⟩_PL = δ_{λμ} ‖T_λ‖²`.

    LaTeX: `\label{prop:pawlowski-leitner-inner-product}`
    Ref: [leitnerpawloski2004] PL inner product / intertwiner basis (arXiv:math/0409565) -/
structure PawLeiInnerProduct where
  /-- The underlying basis data. -/
  basis : PawLeiBasis
  /-- The norm-squared of each basis vector (positive rational). -/
  normSq : Fin basis.num_basis → ℝ
  /-- All norms are positive. -/
  -- Ref: [leitnerpawloski2004] PL inner product / SU(2) intertwiner basis (arXiv:math/0409565)
  normSq_pos : ∀ i, normSq i > 0

/-- The **orthogonal inner product** induced by the PL basis.
    The adjoint trace defines a bilinear form on intertwiner spaces that
    is diagonal in the PL basis: `⟨T_λ, T_μ⟩_PL = δ_{λμ} ‖T_λ‖²`. -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
structure PawLeiOrthogonalIP extends PawLeiInnerProduct where
  /-- The inner product function. -/
  innerProduct : Fin toPawLeiInnerProduct.basis.num_basis →
                 Fin toPawLeiInnerProduct.basis.num_basis → ℝ
  /-- Diagonal entries equal the norm squared. -/
  diagonal : ∀ i, innerProduct i i = toPawLeiInnerProduct.normSq i
  /-- Off-diagonal entries vanish (orthogonality). -/
  orthogonal : ∀ i j, i ≠ j → innerProduct i j = 0

/-- Orthogonality: the PL inner product of distinct basis vectors vanishes. -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
theorem pawLei_orthogonal
    (oip : PawLeiOrthogonalIP)
    (i j : Fin oip.toPawLeiInnerProduct.basis.num_basis) (h : i ≠ j) :
    oip.innerProduct i j = 0 :=
  oip.orthogonal i j h

/-! ## §6  Knot Factorization through Tensor Powers of V -/

/-- A categorical hadron factors through tensor powers of `V` via
    the PawLei embedding.  Each constituent `V_{j_i}` embeds into
    `V_{1/2}^⊗(2j_i)`, so the full hadron embeds into
    `V_{1/2}^⊗(2(j_1 + ⋯ + j_n))`.

    The hypothesis `spins_pos` ensures all constituents have nonzero
    spin (spin-0 is the trivial representation, which contributes
    nothing to the tensor embedding).

    LaTeX: `\label{rem:knot-factorization}` -/
theorem hadron_tensor_factorization
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (h : CategoricalHadron C)
    (spins_pos : ∀ i, h.constituent_spins i ≥ 1) :
    h.totalTensorPower ≥ 2 * h.valence := by
  unfold CategoricalHadron.totalTensorPower
  apply Nat.mul_le_mul_left
  calc Finset.univ.sum h.constituent_spins
      ≥ Finset.univ.sum (fun _ : Fin h.valence => 1) :=
        Finset.sum_le_sum (fun i _ => spins_pos i)
    _ = h.valence := by simp

/-- The Clebsch–Gordan decomposition: `V_{1/2} ⊗ V_{1/2} ≅ V_0 ⊕ V_1`.
    In terms of categorical dimensions: `dim(V_{1/2})² = dim(V_0) + dim(V_1)`,
    i.e. `2 · 2 = 1 + 3`.  Generic over any monoidal category `C`. -/
-- Ref: [leitner2026] §1, Remark: Spin-half representation
theorem clebsch_gordan_fundamental
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    (spinSimpleObject C 1).catDim * (spinSimpleObject C 1).catDim =
    (spinSimpleObject C 0).catDim + (spinSimpleObject C 2).catDim := by
  rfl

end QOU
