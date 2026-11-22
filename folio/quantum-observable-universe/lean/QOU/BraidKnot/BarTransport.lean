/-
  General bar-transport of q-holonomic annihilators.

  Generalizes the figure-eight-specific `annihilates_bar_transport` from
  `QOU.BraidKnot.AJFigureEight` to abstract settings. Two results:

  **1. Bar-symmetric tower transport (sorry-free).** If a tower satisfies
  `J(q, n) = J(q⁻¹, n)` for all `n` (amphichirality), then any operator
  annihilating `J(q⁻¹, ·)` at parameter `q⁻¹` also annihilates `J(q, ·)`
  at `q⁻¹`. This is the abstract version of the figure-eight's
  `annihilates_bar_transport`.

  **2. m-free operator transport (sorry-free).** For q-difference operators
  whose coefficients depend only on `q` (not on the lattice variable `m`),
  the bar involution `q ↦ q⁻¹` in the operator yields an annihilation
  relation at `q⁻¹` from one at `q`. This covers the most common case:
  recurrence relations with q-rational coefficients.

  Pre-archimedean: generic `Field K`. No analysis, no ordering.

  -- Ref: [leitner2026] braids-and-knots, bar-involution transport
-/

import QOU.BraidKnot.AJFigureEight

namespace QOU.BraidKnot.BarTransport

open Finset
open QOU.BraidKnot.AJFigureEight

variable {K : Type*} [Field K]

/-! ### §1  Bar-symmetric tower transport (the amphichiral case) -/

/-- A tower `J` (indexed by a parameter `q : K` and a color `n : ℕ`) is
    bar-symmetric at `q` if its values at `q` and `q⁻¹` coincide pointwise.
    This holds for amphichiral knots (like `4₁`) where the colored Jones
    polynomial is invariant under `q ↦ q⁻¹`. -/
def IsBarSymmetric (J : K → ℕ → K) (q : K) : Prop :=
  ∀ n, J q n = J q⁻¹ n

/-- Bar symmetry gives function-level equality. -/
theorem IsBarSymmetric.eq_fun {J : K → ℕ → K} {q : K}
    (hsym : IsBarSymmetric J q) : J q = J q⁻¹ :=
  _root_.funext hsym

/-- **Annihilation transports for symmetric towers.** If `op` annihilates
    `J(q⁻¹, ·)` at parameter `q⁻¹` and `J` is bar-symmetric at `q`, then
    `op` also annihilates `J(q, ·)` at `q⁻¹`. Sorry-free; the proof
    substitutes `J q = J q⁻¹` as functions. -/
theorem annihilates_bar_of_symmetric
    (op : QDifferenceOperator K)
    (J : K → ℕ → K) (q : K)
    (hsym : IsBarSymmetric J q)
    (h : Annihilates op q⁻¹ (J q⁻¹)) :
    Annihilates op q⁻¹ (J q) := by
  rw [IsBarSymmetric.eq_fun hsym]
  exact h


/-- **q-Holonomicity transports for symmetric towers.** If `J(q⁻¹, ·)` is
    q-holonomic at `q⁻¹` and `J` is bar-symmetric at `q`, then `J(q, ·)` is
    also q-holonomic at `q⁻¹`. Generalizes `coloredJones41_qholonomic_bar`. -/
theorem of_bar_symmetric
    {J : K → ℕ → K} {q : K}
    (hsym : IsBarSymmetric J q)
    (hJ : IsQHolonomic q⁻¹ (J q⁻¹)) :
    IsQHolonomic q⁻¹ (J q) := by
  obtain ⟨op, hnt, hann⟩ := hJ
  exact ⟨op, hnt, annihilates_bar_of_symmetric op J q hsym hann⟩

/-! ### §2  m-free q-difference operators and bar duality

    Many q-difference recurrences in knot theory have coefficients that
    depend on `q` but NOT on the lattice variable `m`. For such operators
    the bar involution `q ↦ q⁻¹` is a clean algebraic operation. -/

/-- An **m-free** q-difference operator: one whose coefficients depend on
    `q` alone, not on the lattice variable `m`. The `Annihilates` relation
    for such an operator uses `q^N` in the m-slot, but since the coefficients
    ignore m, the annihilation condition simplifies. -/
structure MFreeQDiffOp (K : Type*) [Field K] where
  /-- The order (shift-degree) of the operator. -/
  order : ℕ
  /-- Coefficient of the `j`-th shift, depending only on `q`. -/
  coeff : ℕ → K → K
  /-- Inhomogeneous RHS, depending only on `q`. -/
  rhs : K → K

/-- Convert an m-free operator to the general `QDifferenceOperator`. -/
def MFreeQDiffOp.toOp (op : MFreeQDiffOp K) : QDifferenceOperator K where
  order := op.order
  coeff j q _m := op.coeff j q
  rhs q _m := op.rhs q

/-- Annihilation for an m-free operator: `∑_j c_j(q) · J(N+j) = r(q)`. -/
def MFreeAnnihilates (op : MFreeQDiffOp K) (q : K) (J : ℕ → K) : Prop :=
  ∀ N : ℕ,
    ∑ j ∈ range (op.order + 1), op.coeff j q * J (N + j) = op.rhs q

/-- m-free annihilation IS annihilation of the general operator. -/
theorem MFreeQDiffOp.annihilates_iff (op : MFreeQDiffOp K) (q : K) (J : ℕ → K) :
    MFreeAnnihilates op q J ↔ Annihilates op.toOp q J := by
  simp only [MFreeAnnihilates, Annihilates, MFreeQDiffOp.toOp]

/-- The bar involution of an m-free operator: replace `q` by `q⁻¹`. -/
def MFreeQDiffOp.bar (op : MFreeQDiffOp K) : MFreeQDiffOp K where
  order := op.order
  coeff j q := op.coeff j q⁻¹
  rhs q := op.rhs q⁻¹

/-- **m-free bar duality.** If an m-free operator annihilates `J` at `q`, then
    its bar annihilates `J` at `q⁻¹`. This is the clean algebraic bar
    transport: the m-independence means the annihilation condition `∑ c_j(q)
    · J(N+j) = r(q)` transforms to `∑ c_j(q⁻¹) · J(N+j) = r(q⁻¹)` by
    simply replacing `q` with `q⁻¹` in the coefficients — and since the
    Tower values `J(N+j)` don't change, this is the barred operator acting
    on the SAME tower. Sorry-free. -/
theorem MFreeQDiffOp.bar_annihilates_of_annihilates
    (op : MFreeQDiffOp K) (q : K) (J : ℕ → K)
    (h : MFreeAnnihilates op q J) :
    MFreeAnnihilates op.bar q⁻¹ J := by
  intro N
  -- op.bar.coeff j q⁻¹ = op.coeff j (q⁻¹)⁻¹ = op.coeff j q
  -- op.bar.rhs q⁻¹ = op.rhs (q⁻¹)⁻¹ = op.rhs q
  simp only [MFreeQDiffOp.bar, inv_inv]
  exact h N

/-- **m-free q-holonomicity transports across bar.** If `J` is q-holonomic at
    `q` (via an m-free operator), then `J` is q-holonomic at `q⁻¹`. Sorry-free.
    This is the general bar-transport lemma for the common case. -/
theorem IsQHolonomic_bar_of_mfree
    {q : K}
    {J : ℕ → K}
    (op : MFreeQDiffOp K)
    (hnt : ∃ m : K, op.toOp.coeff op.order q m ≠ 0)
    (hann : MFreeAnnihilates op q J) :
    IsQHolonomic q⁻¹ J := by
  refine ⟨op.bar.toOp, ?_, (op.bar.annihilates_iff q⁻¹ J).mp
    (op.bar_annihilates_of_annihilates q J hann)⟩
  -- Nontriviality: op.bar.toOp at q⁻¹ evaluates coeff at (q⁻¹)⁻¹ = q
  obtain ⟨m, hm⟩ := hnt
  refine ⟨m, ?_⟩
  simp only [MFreeQDiffOp.bar, MFreeQDiffOp.toOp, inv_inv]
  exact hm

/-! ### §3  The specialization tower: q ↦ 1 and IsQHolonomic ↦ IsHolonomic

    If `J` is q-holonomic and the operator coefficients have well-defined
    q → 1 limits, the limiting sequence satisfies a classical recurrence
    (D-finite / holonomic in the sense of Zeilberger). This is structural
    — the q-holonomic category is a deformation of the holonomic one. -/

/-- If `J` satisfies the m-free annihilation at `q` for every `q`, it satisfies
    the `q = 1` specialization. A trivial instantiation, but it anchors the
    conceptual bridge: the q → 1 limit of a q-holonomic sequence is holonomic. -/
theorem MFreeAnnihilates_at_one
    (op : MFreeQDiffOp K) (J : ℕ → K)
    (h : MFreeAnnihilates op 1 J) :
    ∀ N : ℕ, ∑ j ∈ range (op.order + 1), op.coeff j 1 * J (N + j) = op.rhs 1 :=
  h

end QOU.BraidKnot.BarTransport
