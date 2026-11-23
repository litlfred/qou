import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.Structures
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.InstantonConnection

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/InstantonConnection.lean (monolithic).
That file no longer exists — the library was split, and `InstantonConnection` now lives at
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/CRRealisation.lean
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Propositions.lean

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **CR manifold data** for the ℂ realisation (ℝ ground ring).

    Re-declared from the library module
    `QOU.QuantumObservableUniverse.CRRealisation` so this sibling is a
    self-contained compilation unit — importing `CRRealisation` would
    collide with this block's own `InstantonConnection` declaration.
    Keep field-for-field in sync with the library. -/
structure CRManifoldData where
  /-- The underlying smooth manifold carrier. -/
  M : Type*
  [topM : TopologicalSpace M]
  /-- CR dimension `n ≥ 1`; real dimension of `M` is `2n + 1`. -/
  n : ℕ
  n_pos : 0 < n
  /-- Levi form signature `(r, s)` with `r + s = n`. -/
  r : ℕ
  s : ℕ
  rs_sum : r + s = n
  /-- The contact form `θ` represented abstractly as a continuous 1-form. -/
  contactForm : M → ℝ
  /-- **Non-degeneracy**: `θ` does not vanish identically. -/
  contact_nondeg : ∃ p : M, contactForm p ≠ 0
  /-- The Reeb vector field `ξ`, characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`. -/
  reebField : C(M, M)
  /-- The Reeb field preserves the contact form: `θ(ξ(p)) = θ(p)`. -/
  reeb_preserves_contact : ∀ p : M, contactForm (reebField p) = contactForm p

attribute [instance] CRManifoldData.topM

/-- **Instanton connection** on a principal bundle `P` over a CR manifold.

    When `dim_ℝ H = 4`, the curvature restricted to `H = ker θ` is self-dual:
    `F_A|_H = *_H F_A|_H`.  More generally, it minimises the Yang–Mills
    functional `∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ`.

    LaTeX: `\label{def:instanton}`

    **Vacuity status (bean `qou-dx7g`, 2026-11-20) — this structure does NOT
    yet encode `def:instanton`.**  `curvature_H` is a real-valued proxy for
    `‖F_A|_H‖`, `hodgeStar` is an arbitrary involution supplied with the
    connection, and `yang_mills_minimises` asserts only `YM(A) ≥ 0`.  So
    `curvature_H := 0`, `hodgeStar := id`, `yangMillsEnergy := 0` is an
    inhabitant, and neither self-duality nor minimisation is constrained.
    Repairing it needs (i) curvature as an `Ad(P)`-valued 2-form on `H`,
    (ii) the Hodge star of the Webster metric `g_θ` on `Λ²H` (fixed by `θ`
    and `J`, not by the instance), and (iii) `YM` as the integral
    `∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ` minimised over the gauge orbit — none of which
    the corpus or Mathlib defines on a CR manifold.  The fields are kept
    unchanged rather than constrained by stand-ins, because a constraint on a
    real-valued proxy would not be a constraint on the curvature. -/
structure InstantonConnection (cr : CRManifoldData) where
  /-- Abstract connection data (gauge potential).
      Full type: a 𝔤-valued 1-form on `P`. Modelled as `C(M, ℝ)` —
      the real-valued proxy captures the norm ‖A‖ at each point. -/
  connectionData : C(cr.M, ℝ)
  /-- Curvature `F_A` restricted to `H = ker θ`.
      Full type: an Ad(P)-valued 2-form on `H`. Modelled as `C(M, ℝ)` —
      the real-valued proxy captures the norm ‖F_A|_H‖ at each point. -/
  curvature_H : C(cr.M, ℝ)
  /-- The type of covariant-constant sections of `Ad(P)` w.r.t. this
      connection: `{ s ∈ Γ(Ad(P)) | D_A s = 0 }`. -/
  parallelAdjointSections : Type*
  /-- When `n = 2` (`dim_ℝ H = 4`), the Hodge star on `Ad(P)`-valued
      2-forms restricted to `H`, determined by the Webster metric `g_θ`
      and the complex structure `J`. -/
  hodgeStar : cr.n = 2 → HodgeInvolution C(cr.M, ℝ)
  -- Yang–Mills minimisation: the connection is a critical point of
  -- `YM(A) = ∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ`.
  /-- The Yang–Mills energy functional `YM(A) = ∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ`.
      Returns the energy evaluated on `curvature_H`. -/
  yangMillsEnergy : ℝ
  /-- Non-negativity of the Yang–Mills energy.  Named `minimises`, but it
      does NOT state `YM(A) ≤ YM(A')` for any competitor `A'` (GAP, bean
      `qou-dx7g`; see the structure docstring). -/
  yang_mills_minimises : yangMillsEnergy ≥ 0
  /-- **Self-duality**: when `dim_ℝ H = 4` (CR dimension `n = 2`), the
      curvature restricted to `H` is self-dual with respect to the Hodge star.
      This is the Bogomolny bound: YM minimisation forces `F⁻ = 0`. -/
  self_dual : ∀ (hn : cr.n = 2), (hodgeStar hn).IsSelfDual curvature_H

/-- A connection is **irreducible** if the space of its covariant-constant
    adjoint sections is trivial (at most one element, necessarily zero). -/
def InstantonConnection.IsIrreducible {cr : CRManifoldData}
    (inst : InstantonConnection cr) : Prop :=
  Subsingleton inst.parallelAdjointSections

end QOU
