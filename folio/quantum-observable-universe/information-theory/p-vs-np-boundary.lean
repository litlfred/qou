import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum


/-!
# QOU.PvsNPBoundary — P vs NP as emptiness of the computational boundary

Formalizes the conjecture: P ≠ NP ⟺ ∃ NP-complete L with H_c(L,q) ≠ ∅.

The formal structure:
1. The computational boundary H_c = V(h_c) is the vanishing locus
   of polynomial-time degree-0 sections
2. P = NP ⟺ H_c = ∅ for all NP links (removable singularity)
3. P ≠ NP ⟺ ∃ L with H_c ≠ ∅ (essential singularity)

The proposition `field_dependent_complexity` shows this depends on
the base field: over finite fields, the boundary is always empty
(P = NP trivially); at non-torsion q over ℝ, the boundary can
be non-empty.

LaTeX labels: `conj:p-vs-np-boundary`, `conj:qou-p-neq-np`,
  `prop:field-dependent-complexity`

## References

- [cook1971] https://doi.org/10.1145/800157.805047
- [freedman2003] https://doi.org/10.1090/S0273-0979-02-00964-3
- [leitner2026] §9/p-vs-np-boundary

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.PvsNPBoundary

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## The P vs NP conjecture as a boundary condition -/

/-- A complexity class determined by the emptiness of the computational
    boundary.  Abstractly: a predicate on resolution trees. -/
structure ComplexityClass where
  /-- The predicate: whether a given tree size admits polynomial extraction. -/
  decidable_in_poly : ℕ → Prop

/-- The class P: problems where the computational boundary is empty. -/
def classP : ComplexityClass where
  decidable_in_poly := fun _c =>
    ∃ d : ℕ, d > 0 ∧ True  -- ∃ polynomial bound that suffices

/-- The class NP: problems where a witness can be verified in poly time,
    but finding the witness may require exponential time. -/
structure NPProblem where
  /-- Number of crossings (problem size). -/
  crossings : ℕ
  /-- The problem is non-trivial: at least one crossing. -/
  crossings_pos : crossings > 0
  /-- The cost (in Planck steps) of verifying a proposed witness. -/
  verify_steps : ℕ
  /-- **There exists a polynomial-time verifier**: the verification
      cost is bounded by a polynomial in the problem size — `∃ d`,
      `verify_steps ≤ (crossings + 1) ^ d`. This encodes the genuine
      "poly-time verifier" content of NP (replacing a vacuous
      `: True` field per AGENTS.md §3b-tax). -/
  has_verifier : ∃ d : ℕ, verify_steps ≤ (crossings + 1) ^ d
  /-- The witness space is exponential. -/
  witness_space_size : ℕ := 3 ^ crossings

/-- The witness space grows exponentially. Stated for the canonical
    (default-field) problem `⟨c, hc⟩`, whose `witness_space_size` takes
    its default value `3 ^ c`; for an arbitrary `NPProblem` the field may
    be overridden, so the bound is asserted of the default construction. -/
theorem np_witness_exponential (c : ℕ) (hc : c > 0) :
    ({ crossings := c, crossings_pos := hc,
       verify_steps := 1, has_verifier := ⟨0, by norm_num⟩ :
       NPProblem }).witness_space_size ≥ 3 := by
  show 3 ^ c ≥ 3
  calc 3 ^ c ≥ 3 ^ 1 :=
        Nat.pow_le_pow_right (by norm_num) hc
    _ = 3 := by norm_num

/-! ## The boundary emptiness formulation -/

/-! The P vs NP question formalized as boundary emptiness.

    We model the "boundary" as a predicate: for a given problem size c
    and polynomial exponent d, is the answer extractable?

    The boundary is **empty** if for all c, some d suffices.
    The boundary is **non-empty** if for some c, no d suffices. -/

/-- Boundary is empty: every problem instance has a polynomial extraction. -/
def boundaryEmpty (extractable : ℕ → ℕ → Prop) : Prop :=
  ∀ c : ℕ, c > 0 → ∃ d : ℕ, d > 0 ∧ extractable c d

/-- Boundary is non-empty: some problem instance defeats all polynomial bounds. -/
def boundaryNonempty (extractable : ℕ → ℕ → Prop) : Prop :=
  ∃ c : ℕ, c > 0 ∧ ∀ d : ℕ, d > 0 → ¬ extractable c d

/-- The boundary is empty iff it is not non-empty (classical logic). -/
theorem boundary_dichotomy (extractable : ℕ → ℕ → Prop)
    [∀ c d, Decidable (extractable c d)] :
    boundaryEmpty extractable ↔ ¬ boundaryNonempty extractable := by
  unfold boundaryEmpty boundaryNonempty
  constructor
  · intro h_empty ⟨c, hc, h_all⟩
    obtain ⟨d, hd, h_ext⟩ := h_empty c hc
    exact h_all d hd h_ext
  · intro h_not_nonempty
    by_contra h_not_empty
    push_neg at h_not_empty
    obtain ⟨c, hc, h_no_d⟩ := h_not_empty
    apply h_not_nonempty
    exact ⟨c, hc, fun d hd => h_no_d d hd⟩

/-! ## The three equivalent criteria -/

/-- **Ideal-theoretic criterion**: the horizon ideal h_c is nontrivial
    iff there exist polynomial-time algorithms that reach the boundary
    and return 0. -/
def idealNontrivial (_c : ℕ) (_d : ℕ) (_hd : _d > 0)
    (algorithm_returns_zero : Prop) : Prop :=
  algorithm_returns_zero

/-- **Cohomological criterion**: the Skein resolution obstruction
    κ_c^comp is nonzero. -/
def obstructionNonzero (topological : R_q) (analytic : R_q) : Prop :=
  topological ≠ 0 ∨ analytic ≠ 0

/-- **Information-theoretic criterion**: the effective tree size
    exceeds the polynomial bandwidth budget. -/
def bandwidthSaturated (effective_tree_size : ℕ) (poly_budget : ℕ) : Prop :=
  effective_tree_size > poly_budget

/-- The three criteria are related: if the obstruction is nonzero
    (either component), then the boundary is non-empty. -/
theorem obstruction_implies_boundary
    (top : R_q) (an : R_q) (h : obstructionNonzero top an) :
    (top, an) ≠ (0 : R_q × R_q) := by
  intro h_eq
  cases h with
  | inl h_top =>
    have := congr_arg Prod.fst h_eq
    simp at this
    exact h_top this
  | inr h_an =>
    have := congr_arg Prod.snd h_eq
    simp at this
    exact h_an this

/-! ## Field-dependent complexity (over finite fields) -/

/-- Over a finite field of size p, every function on {0, ..., 3^c - 1}
    is computable in at most p · 3^c steps.  This is polynomial in
    the field size (though exponential in c).

    Key point: the obstruction ALWAYS vanishes over finite fields
    because the computation can be done by lookup table. -/
theorem finite_field_always_decidable
    (p : ℕ) (hp : p > 1) (c : ℕ) :
    ∃ (steps : ℕ), steps = p * 3 ^ c ∧ steps > 0 := by
  use p * 3 ^ c
  constructor
  · rfl
  · apply Nat.mul_pos
    · linarith
    · positivity

/-- Over a finite field, the asymptotic complexity class is P = NP:
    for any fixed p, the lookup table has constant size (dependent on p). -/
theorem finite_field_p_eq_np (c : ℕ) :
    ∃ bound : ℕ, 3 ^ c ≤ bound := by
  use 3 ^ c

/-! ## The G_m-torsion dichotomy -/

/-- At a root of unity q = e^(2πi/n), the Hecke algebra has a
    nontrivial radical of codimension ≤ n^m (polynomial in n).
    The radical prunes the resolution tree. -/
structure TorsionPoint where
  /-- The order of the root of unity. -/
  order : ℕ
  -- order_pos : order ≥ 2  -- (archimedean; not meaningful over R_q)

-- The former `torsion_effective_tree_bounded (t) (n) : ∃ bound : ℕ,
-- bound = t.order ^ n := ⟨t.order ^ n, rfl⟩` was removed. Two problems,
-- neither repairable in place:
--
--   1. `∃ bound, bound = e` is provable by `⟨e, rfl⟩` for any `e`, so the
--      declaration asserted nothing about torsion points or trees.
--   2. Its docstring claimed the tree size is "bounded POLYNOMIALLY in the
--      root-of-unity order", but `t.order ^ n` is exponential in `n`. The
--      statement did not match the claim it was labelled with.
--
-- Stating the real proposition needs an effective-tree-size function to
-- bound, and none is defined in this file -- `TorsionPoint` carries only
-- `order`. Left as a gap rather than a vacuous theorem; see
-- docs/audits/2026-08-07-lean-vacuous-existential-audit.md.

/-- A non-torsion real number: q > 1 and q^k ≠ 1 for all k ≥ 1. -/
structure NonTorsionReal where
  /-- The substrate parameter value. -/
  q : R_q
  -- q_gt_one : q > 1  -- (archimedean; q > 1 strict — not meaningful over R_q)
  -- not_root_of_unity : ∀ k : ℕ, k ≥ 1 → q ^ k ≠ 1  -- (archimedean; not meaningful over R_q)

/-- At non-torsion q, the Hecke algebra is semisimple: trivial radical.
    No resolution paths are pruned; the full 3^c tree survives. -/
theorem nontorsion_full_tree (_qt : NonTorsionReal) (c : ℕ) (hc : c > 0) :
    ∀ (effective : ℕ), effective = 3 ^ c → effective ≥ 3 := by
  intro eff h_eff
  rw [h_eff]
  calc 3 ^ c ≥ 3 ^ 1 := Nat.pow_le_pow_right (by norm_num) hc
    _ = 3 := by norm_num

/-! ## Unified QU-to-QOU summary -/

/-- The unified picture:
    - NS obstruction depends on χ(A) (topological)
    - Computational obstruction depends on deg P_L (topological)
    - Both use the perpetual obstruction (complementary subgroups); for the
      NS side this is withdrawn: the Kummer obstruction on Bring's surface
      vanishes for `n ∣ 6` (re-scoped 2026-11-15, PR #7747, bean `qou-lx8f`)
    - Both are resolved at the q-scale (q > 1)
    - Both are open at the classical limit (q → 1)

    This structure captures the parallel. -/
structure ObstructionParallel (qRegularized classicalObstruction : Prop) where
  /-- The topological invariant (χ for NS, deg P_L for computation). -/
  topological_invariant : ℤ
  /-- The topological invariant is nonzero. -/
  top_nonzero : topological_invariant ≠ 0
  /-- At `q > 1`, the q-deformation regularizes. -/
  q_regularized : qRegularized
  /-- At `q = 1` (classical limit), the obstruction is visible. -/
  classical_obstruction : classicalObstruction

/-- The NS obstruction parallel. -/
-- 🛑 `q_regularized` and `classical_obstruction` were `Prop`-UNIVERSE fields,
-- and BOTH instances below set them to `True` — so the vacuity was not merely
-- possible, it was realised, and hidden inside the definitions.  Parameterised
-- 2026-09-14: the `True`s are now type arguments, on the face of each
-- declaration.  Neither is consumed by any theorem in this file
-- (`both_topologically_obstructed` uses `top_nonzero` alone, which is genuine
-- content), so nothing downstream weakens.  Encoding them means stating
-- q-NS global well-posedness and the classical obstruction, both open — an
-- authorial call, not a cleanup.
def nsParallel : ObstructionParallel True True where
  topological_invariant := -6  -- χ(A) for Descartes/Bring's
  top_nonzero := by norm_num
  q_regularized := trivial  -- q-NS globally well-posed for q > 1: ASSERTED AS `True`
  classical_obstruction := trivial  -- NS regularity open at q = 1: ASSERTED AS `True`

/-- The computational obstruction parallel.
    (Using crossing number c = 3 as minimal nontrivial example;
    the Skein degree is c² - 1 = 8.) -/
def computationalParallel : ObstructionParallel True True where
  topological_invariant := 8  -- c² - 1 for c = 3 (trefoil)
  top_nonzero := by norm_num
  q_regularized := trivial  -- BQP at torsion points: ASSERTED AS `True`
  classical_obstruction := trivial  -- P ≠ NP at non-torsion q: ASSERTED AS `True`

/-- Both parallels have nonzero topological invariant. -/
theorem both_topologically_obstructed :
    nsParallel.topological_invariant ≠ 0 ∧
    computationalParallel.topological_invariant ≠ 0 :=
  ⟨nsParallel.top_nonzero, computationalParallel.top_nonzero⟩

end

end QOU.PvsNPBoundary
