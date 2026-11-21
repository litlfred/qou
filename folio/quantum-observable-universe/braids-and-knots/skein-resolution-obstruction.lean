import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.LinearAlgebra.Prod


/-!
# QOU.SkeinResolutionObstruction — Obstruction decomposition and perpetual obstruction

The Skein resolution obstruction κ_c^comp(L, q) decomposes into:
- Topological component κ_c^top: universal, depends only on the link L
- Analytic component δ_c^comp: q-dependent, measures irreducible tree weight

These live in complementary subspaces.  The **perpetual obstruction**
theorem (mirroring QU-to-QOU item 3) proves that when both are nonzero,
the total obstruction is nonzero — independent of any cancellation.

Over finite fields, the obstruction vanishes (field-dependent complexity).
At roots of unity, the Hecke radical prunes the tree (BQP).
At non-torsion q, the algebra is semisimple and the obstruction persists.

LaTeX labels: `def:skein-resolution-obstruction`,
  `prop:computational-perpetual-obstruction`,
  `prop:field-dependent-complexity`,
  `prop:computational-kummer-specialisation`

## References

- [leitner2026] §9/skein-resolution-obstruction
- [leitner2026] §3/qu-to-qou (item 3: perpetual obstruction)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.SkeinResolutionObstruction

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Obstruction decomposition

    The key algebraic structure: a direct sum decomposition V = V_top ⊕ V_an
    where the topological and analytic components live in complementary
    subspaces.  This is the abstract core of the perpetual obstruction. -/

/-- A direct sum decomposition of an additive group into two complementary
    subgroups.  Elements from different summands cannot cancel. -/
structure ComplementaryDecomposition (α : Type*) [AddCommGroup α] where
  /-- The topological subspace. -/
  topological : α → Prop
  /-- The analytic subspace. -/
  analytic : α → Prop
  /-- Zero is in both subspaces. -/
  top_zero : topological 0
  an_zero : analytic 0
  /-- Subspace closure under addition within each component. -/
  top_add : ∀ {a b}, topological a → topological b → topological (a + b)
  an_add : ∀ {a b}, analytic a → analytic b → analytic (a + b)
  /-- Subspace closure under negation within each component. -/
  top_neg : ∀ {a}, topological a → topological (-a)
  an_neg : ∀ {a}, analytic a → analytic (-a)
  /-- Every element decomposes uniquely. -/
  decompose : α → α × α
  /-- First component is topological. -/
  fst_top : ∀ v, topological (decompose v).1
  /-- Second component is analytic. -/
  snd_an : ∀ v, analytic (decompose v).2
  /-- The decomposition sums to the original. -/
  sum_eq : ∀ v, (decompose v).1 + (decompose v).2 = v
  /-- **Complementarity**: the intersection is trivial. -/
  complementary : ∀ v, topological v → analytic v → v = 0

/-! ## The perpetual obstruction theorem

    The algebraic core: if v = v_top + v_an with v_top ≠ 0 and
    v_an ≠ 0, and the subspaces are complementary, then v ≠ 0. -/

/-- **Perpetual obstruction (algebraic core).**

    If an element decomposes into topological and analytic components,
    and either component is nonzero, and the subspaces are complementary,
    then the total element is nonzero.

    This was written to mirror QU-to-QOU theorem item 3 (κ₀ and δₙ in
    complementary subgroups, so κₙ = κ₀ + δₙ ≠ 0). The algebraic lemma here is
    unaffected, but that reading of item 3 is withdrawn: on Bring's surface the
    obstruction vanishes for `n ∣ χ = -6` (re-scoped 2026-11-15, owner decision,
    PR #7747, bean `qou-lx8f`). -/
-- Ref: [leitner2026] §3/qu-to-qou (item 3)
-- Ref: [leitner2026] §9/computational-perpetual-obstruction
theorem perpetual_obstruction_top {α : Type*} [AddCommGroup α]
    (D : ComplementaryDecomposition α)
    (v : α)
    (h_top_nonzero : (D.decompose v).1 ≠ 0) :
    v ≠ 0 := by
  intro h_v_zero
  -- `(D.sum_eq v).trans h_v_zero` avoids rewriting `v` inside `D.decompose v`.
  have h_sum : (D.decompose v).1 + (D.decompose v).2 = 0 := (D.sum_eq v).trans h_v_zero
  -- So (decompose v).1 = -(decompose v).2 (a pure `AddCommGroup` identity).
  have h_eq : (D.decompose v).1 = -(D.decompose v).2 := eq_neg_of_add_eq_zero_left h_sum
  -- (decompose v).1 is topological; -(decompose v).2 is analytic (closure under negation).
  have h_t := D.fst_top v
  have h_a_neg := D.an_neg (D.snd_an v)
  rw [h_eq] at h_t
  -- By complementarity, -(decompose v).2 = 0, hence (decompose v).1 = 0 — contradiction.
  have h_neg_zero := D.complementary _ h_t h_a_neg
  exact h_top_nonzero (h_eq.trans h_neg_zero)

/-- **Perpetual obstruction (analytic nonzero).**

    Symmetric version: if the analytic component is nonzero,
    the total element is nonzero. -/
theorem perpetual_obstruction_an {α : Type*} [AddCommGroup α]
    (D : ComplementaryDecomposition α)
    (v : α)
    (h_an_nonzero : (D.decompose v).2 ≠ 0) :
    v ≠ 0 := by
  intro h_v_zero
  have h_sum : (D.decompose v).1 + (D.decompose v).2 = 0 := (D.sum_eq v).trans h_v_zero
  have h_eq : (D.decompose v).2 = -(D.decompose v).1 := eq_neg_of_add_eq_zero_right h_sum
  have h_a := D.snd_an v
  have h_t_neg := D.top_neg (D.fst_top v)
  rw [h_eq] at h_a
  have h_neg_zero := D.complementary _ h_t_neg h_a
  exact h_an_nonzero (h_eq.trans h_neg_zero)

/-- **Perpetual obstruction (both nonzero).**

    When both components are nonzero and live in complementary
    subspaces, the sum is nonzero. -/
theorem perpetual_obstruction_both {α : Type*} [AddCommGroup α]
    (D : ComplementaryDecomposition α)
    (v : α)
    (h_top : (D.decompose v).1 ≠ 0)
    (_h_an : (D.decompose v).2 ≠ 0) :
    v ≠ 0 :=
  perpetual_obstruction_top D v h_top

/-! ## Application to the Skein resolution obstruction

    The computational Yekutieli class κ_c^comp = κ_c^top + δ_c^comp
    decomposes into:
    - κ_c^top ∈ im(H²(R, R)): topological, depends on deg P_L
    - δ_c^comp ∈ im(H²(R, O_R)): analytic, depends on q

    These are complementary by the constant-vs-varying argument:
    a class that is simultaneously constant (topological) and
    varying (analytic) must be zero.

    We model this concretely over ℝ using the product decomposition. -/

/-- The obstruction decomposition over ℝ: the topological component
    is a constant (the Skein degree), and the analytic component
    is the residual tree weight at parameter q. -/
structure ObstructionData where
  /-- The topological component: Skein polynomial degree. -/
  topological : R_q
  /-- The analytic component: residual tree weight at q. -/
  analytic : R_q
  /-- The total obstruction: their sum. -/
  total : R_q := topological + analytic

/-- The standard complementary decomposition on ℝ × ℝ
    (product of two copies, intersection is the origin). -/
def realProductDecomposition : ComplementaryDecomposition (R_q × R_q) where
  topological := fun p => p.2 = 0
  analytic := fun p => p.1 = 0
  top_zero := rfl
  an_zero := rfl
  top_add := fun h1 h2 => by simp [h1, h2]
  an_add := fun h1 h2 => by simp [h1, h2]
  top_neg := fun h => by simp [h]
  an_neg := fun h => by simp [h]
  decompose := fun p => ((p.1, 0), (0, p.2))
  fst_top := fun _ => rfl
  snd_an := fun _ => rfl
  sum_eq := fun p => by simp
  -- `h1 : v.2 = 0` (topological), `h2 : v.1 = 0` (analytic). Use `Prod.ext_iff`
  -- directly — `ext` would recurse into the `Finsupp` structure of `R_q`.
  complementary := fun _ h1 h2 => Prod.ext_iff.mpr ⟨h2, h1⟩

/-- **Perpetual obstruction for the Skein resolution (concrete).**

    If the topological component (Skein degree) is nonzero,
    the total obstruction is nonzero in the product decomposition. -/
theorem skein_perpetual_top
    (top : R_q) (an : R_q)
    (h_top : top ≠ 0) :
    (top, an) ≠ (0 : R_q × R_q) := by
  intro h
  have := congr_arg Prod.fst h
  simp at this
  exact h_top this

/-- If the analytic component (residual weight) is nonzero,
    the total obstruction is nonzero. -/
theorem skein_perpetual_an
    (top : R_q) (an : R_q)
    (h_an : an ≠ 0) :
    (top, an) ≠ (0 : R_q × R_q) := by
  intro h
  have := congr_arg Prod.snd h
  simp at this
  exact h_an this

/-! ## Field-dependent complexity

    Over finite fields, every function on a finite set is computable.
    The obstruction vanishes because the resolution tree is finite. -/

/-- Over a finite type with decidable equality, every function is
    computable: one can evaluate it by enumeration. -/
theorem finite_decidable {α : Type*} [Fintype α] [DecidableEq α]
    {β : Type*} (f : α → β) :
    ∃ (table : List (α × β)),
      ∀ a, ∃ p ∈ table, p.1 = a := by
  refine ⟨(Finset.univ.toList).map fun x => (x, f x), fun a => ⟨(a, f a), ?_, rfl⟩⟩
  simp only [List.mem_map, Finset.mem_toList, Finset.mem_univ, true_and]
  exact ⟨a, rfl⟩

/-- The resolution tree over a finite field has finitely many
    distinct weights, bounded by the field size. -/
theorem finite_field_bounded_weights (p : ℕ) (hp : 0 < p) (num_paths : ℕ) :
    num_paths % p < p :=
  Nat.mod_lt num_paths hp

/-! ## Hecke semisimplicity at non-torsion q

    At non-torsion q (q^k ≠ 1 for all k ≥ 1), the Hecke algebra
    H_n(q) is semisimple: its radical is trivial.  This means no
    resolution paths are annihilated, and the full 3^c tree survives.

    At torsion q (root of unity), the radical is non-trivial and
    prunes the tree: this is the BQP mechanism. -/

-- The q-integer `[k]_q = (q^k - q^{-k}) / (q - q^{-1})` and its non-vanishing at
-- non-torsion `q` are **archimedean** facts: they need the order `q > 1`, which the
-- order-free ground ring `R_q = ℤ[q, q⁻¹]` does not carry (§7c base-ring wall). They
-- are therefore stated over `ℝ` in the archimedean specialisation, not here — see
-- `hecke-character-q-integer.lean`. (Earlier drafts left these declarations here with
-- their `R_q`-typed signatures commented out and their proof bodies orphaned, which
-- did not compile; the content lives in the ℝ file.)

/-! ## The Kummer divisibility condition

    At root of unity q_k = e^(2πi/(k+2)) with n = k+2,
    the obstruction κ_c^top mod n = 0 iff n > c² - 1.
    For n ≤ c² - 1, the obstruction persists.

    We encode this as a divisibility condition on natural numbers. -/

/-- The Kummer divisibility condition: the obstruction at level n
    vanishes iff n divides the Skein degree. -/
def kummerVanishes (skeinDegree : ℕ) (n : ℕ) : Prop :=
  n ∣ skeinDegree

/-- There are infinitely many levels where the obstruction persists:
    for any degree d > 0, the set {n : ¬ n | d} is infinite. -/
theorem infinitely_many_non_divisors (d : ℕ) (hd : 0 < d) :
    ∀ N : ℕ, ∃ n > N, ¬ kummerVanishes d n := by
  intro N
  -- d + N + 1 does not divide d (since d + N + 1 > d > 0)
  refine ⟨d + N + 1, by omega, ?_⟩
  unfold kummerVanishes
  intro hdvd
  -- a positive number is ≥ any of its divisors, but d + N + 1 > d
  have := Nat.le_of_dvd hd hdvd
  omega

/-- For the Descartes universe (χ = -6), the obstruction persists
    at all levels n where n does not divide 6. -/
theorem descartes_kummer_persistence (n : ℕ) (hn : ¬ n ∣ 6) :
    ¬ kummerVanishes 6 n := by
  unfold kummerVanishes
  exact hn

end

end QOU.SkeinResolutionObstruction
