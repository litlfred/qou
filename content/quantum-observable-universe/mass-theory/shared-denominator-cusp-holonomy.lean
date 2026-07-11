import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic


/-!
# Shared-denominator cusp holonomy (conjecture class)

The conjecture: zeros of the q-Pochhammer denominator `(x; q)_n`
enforce the Thurston cusp-completeness conditions
`Hol_μ(z) = Hol_λ(z) = 1` on the corresponding ideal tetrahedron.

Dependency note: this block sits downstream of
`conj:algebraic-geometric-dilog-equivalence` §1 at the **manifest**
level (`uses[]`); the sibling `.lean` files are built self-contained
(no cross-sibling imports), so the dependency is NOT a type-level
`[AlgebraicGeometricEquivalence]` binder here. Conversely, the
alg-geom class's `pole_cusp_matched` hypothesis is exactly what an
instance of THIS class would supply — this conjecture is the
geometric input, not a consequence.

-- Ref: [manuscript] conj:shared-denominator-cusp-holonomy
-- Ref: [thurston1978] manuscript: The geometry and topology of 3-manifolds
-- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds — see content/schema/references.ts
-/

namespace QOU.QPochhammer

/-- The geometric-shape predicate over `ℂ` at the shape parameter `z` —
    the *necessary* conditions for cusp completeness (the name says what
    it asserts; the full holonomy content remains open, see below):
    the shape is a **geometric** ideal-tetrahedron shape — non-degenerate
    (`z ≠ 0`, `z ≠ 1`) and of positive imaginary part (upper half-plane,
    positively oriented). A genuine formalisation would additionally carry
    the ideal triangulation and the Neumann-Zagier potential with
    `Hol_μ(z) = Hol_λ(z) = 1`; those gluing equations remain open here,
    but `im_pos` already excludes every real (flattened) shape, so the
    predicate is not dischargeable by a constant real witness. -/
-- Ref: [thurston1978] §4.5 (gluing equations)
structure GeometricShape (z : ℂ) : Prop where
  /-- Shape nondegeneracy: `z ≠ 0` (the degenerate collapsed vertex; the
      meridian holonomy equation `Hol_μ(z) = 1` itself remains open). -/
  shape_ne_zero : z ≠ 0
  /-- Shape nondegeneracy: `z ≠ 1` (the degenerate flat vertex; the
      longitude holonomy equation `Hol_λ(z) = 1` itself remains open). -/
  shape_ne_one : z ≠ 1
  /-- Geometric (positively oriented) shape: `Im z > 0`. -/
  im_pos : 0 < z.im

/-- The shared-denominator conjecture, packaged as a typeclass over a
    state variable `x`, substrate parameter `q`, and depth `n`.
    An instance asserts that whenever the algebraic denominator
    `(x; q)_n` vanishes at a root of the form `x = q^{-k}`, the
    matched cusp shape parameter `z_k` satisfies the Thurston cusp-
    completeness predicate. -/
-- Ref: [manuscript] conj:shared-denominator-cusp-holonomy
class SharedDenominatorCuspHolonomy
    (q x : ℝ) (n : ℕ) : Prop where
  /-- For each algebraic denominator zero `x = q^{-k}` (i.e. each
      `k < n` with `1 - x q^k = 0`), the matched complex cusp shape
      parameter is `GeometricShape`. -/
  -- Ref: [manuscript] conj:shared-denominator-cusp-holonomy §proof sketch
  cusp_complete_of_root :
    ∀ (k : Fin n), 1 - x * q ^ (k : ℕ) = 0 →
      ∃ z : ℂ, GeometricShape z

/-- Stated conjecture form: the algebraic denominator zeros are the
    Thurston cusp-completeness solutions. Inhabited only by an
    instance of `SharedDenominatorCuspHolonomy`. -/
-- Ref: [manuscript] conj:shared-denominator-cusp-holonomy
theorem shared_denominator_cusp_holonomy
    (q x : ℝ) (n : ℕ) [h : SharedDenominatorCuspHolonomy q x n] :
    ∀ (k : Fin n), 1 - x * q ^ (k : ℕ) = 0 →
      ∃ z : ℂ, GeometricShape z :=
  h.cusp_complete_of_root

/-- **Solver-pipeline corollary.** The algebraic denominator zeros
    `{q^{-k} : k < n}` are valid Newton–Raphson seed values for the
    Thurston gluing equations on the matched JSJ piece. This is a
    direct re-packaging of `shared_denominator_cusp_holonomy` for
    consumption by the WASM compute layer. -/
-- Ref: [manuscript] conj:shared-denominator-cusp-holonomy §implication
theorem newton_seed_completeness
    (q x : ℝ) (n : ℕ) [h : SharedDenominatorCuspHolonomy q x n] :
    ∀ (k : Fin n), 1 - x * q ^ (k : ℕ) = 0 →
      ∃ z : ℂ, GeometricShape z :=
  shared_denominator_cusp_holonomy q x n

/-! ## No instance — this is an open primary conjecture

A previous revision carried a "skeleton" `instance canonical` witnessing
cusp-completeness with the constant real shape `z = 2`. That instance
encoded none of the Thurston gluing-equation content yet *discharged* the
§3b-cond hypothesis for every downstream consumer — precisely the
"fabricated trivial instance" pattern forbidden by AGENTS.md §3b-tax
("an unproved primary is honestly represented by a content-bearing class
with no instance"). It is removed: the open state of the conjecture is now
visible in the type system, and the strengthened `im_pos` field makes any
real-constant witness impossible. The actual `z_k` for the `k`-th cusp
must come from the Newton–Raphson gluing pipeline
(`computations/q-pochhammer-seed.witness.json` records the trefoil case). -/

end QOU.QPochhammer
