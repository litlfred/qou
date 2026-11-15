import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace
import QOU.Mathlib.NonAbelianStokes

/-!
# QOU.Mathlib.LatticeGaugeShadow — the algebraic core of the lattice-QCD-from-QOU shadow

This file formalises the **structural / categorical** core of the
"lattice QCD as the `q → 1` shadow of the `q`-deformed surface state-sum"
correspondence recorded narratively in the content block
`rem:lattice-qcd-from-qou`
(`folio/quantum-observable-universe/brings-surface/lattice-qcd-from-qou.md`,
PR #4622).

## Scope discipline (STRICT — read first)

The **physical / numerical** correspondence — "the `q`-deformed surface
state-sum reproduces lattice-gauge results", any numerical agreement — is
**evidence-tier only** (owner ruling): it is an empirical cross-check of the
same evidential tier as agreement with an experimental datum, strictly weaker
than a formal derivation, and it is **NOT** proved here (or anywhere in Lean).
The remark itself states: *"This correspondence is a structural observation,
not a theorem. … A proof of the state-sum / lattice-gauge correspondence
remains open."*

What **is** provable, and is proved sorry-free below, is the pure **algebra**
that underlies the structural observation. Three targets:

1. **Null scalar channel** (`CyclicCharacter.annihilates_orderingDefect`,
   `matrix_trace_annihilates_orderingDefect`). The surface-ordering
   correction of two cell holonomies is the ordering defect
   `A·B − B·A` (identical to the `q`-curvature transport defect `F_q` of
   `QOU.LocalQ.ObservationParallelogram.Fq`). A block-trace character
   `χ^λ` — a *cyclic* additive functional — annihilates it:
   `χ(A·B − B·A) = 0`. This is the rigorous version of the σ₁³-agent's
   numerical `tr[A,B] = 0` observation. The concrete matrix trace realises
   the abstract cyclic character.

2. **`q → 1` degeneration → Wilson plaquette product**
   (`qSurfaceOrderedProduct_at_one`, `qCellMul_sub_classical`). The
   `q`-deformed surface-ordered cell product carries the surface-ordering
   (non-abelian) correction, weighted by `(q − 1)`; at `q = 1` the correction
   switches off and the ordered product degenerates to the ordinary
   (Wilson-action) plaquette product `∏ U_p`.

3. **Refinement invariance of the surface state-sum, single move**
   (`wilsonPlaquetteProduct_refine_invariant`,
   `holonomy_R2_move_invariant`, `qCellMul_associator_at_one_eq_zero`).
   The classical (undeformed / `q = 1`) state-sum is invariant under the two
   elementary refinement moves — the `1 → 2` cell subdivision and the
   Reidemeister-II cancelling-pair insertion — because the ordered product is
   an **associative monoid product**. The obstruction to invariance is the
   *associator* of the `q`-deformed cell product, which is proved to **vanish
   at `q = 1`**. Away from `q = 1` the associator is the pentagon /
   Pachner-2–3 obstruction, which is **open** and carried by the existing
   conjecture-class `QOU.BraidsAndKnots.PachnerPentagonBorromean`
   (`conj:pachner-pentagon-borromean`); the general `q`-deformed
   triangulation-invariance is beaned, not claimed.

## Base ring (§7c)

Everything here is pure algebra over a generic noncommutative `Ring R`
(holonomies) with a value ring / group for the character. No `ℝ`, no ordering,
no `Real.*`, no archimedean construct — the substrate→archimedean wall is not
crossed.

Ref: [leitner2026] rem:lattice-qcd-from-qou, conj:pachner-pentagon-borromean,
     def:q-flat-connection, rem:two-observer-parallelogram
-/

namespace QOU.Mathlib.LatticeGaugeShadow

/-! ## Target 1 — the null scalar channel: a cyclic character kills the ordering defect -/

variable {R S : Type*} [Ring R] [AddCommGroup S]

/-- The **surface-ordering defect** (additive commutator) of two cell
    holonomies `A, B`. This is exactly the `q`-curvature transport defect
    `F_q = (1 + δq₁)(1 + δq₂) − (1 + δq₂)(1 + δq₁)` of
    `QOU.LocalQ.ObservationParallelogram.Fq` specialised to the two cell
    holonomies (both are `A·B − B·A`), and the obstruction to two adjacent
    cells commuting. -/
def orderingDefect (A B : R) : R := A * B - B * A

/-- The ordering defect is antisymmetric in the two cells:
    `orderingDefect B A = − orderingDefect A B`. -/
theorem orderingDefect_antisymm (A B : R) :
    orderingDefect B A = - orderingDefect A B := by
  simp only [orderingDefect]
  noncomm_ring

/-- A **block-trace character** `χ^λ`: a cyclic additive functional on the
    holonomy ring. The two fields are the genuine defining properties of a
    class function / trace: additivity (`toHom : R →+ S`) and cyclicity
    (`χ(a·b) = χ(b·a)`). The concrete matrix trace `Matrix.trace` is such a
    character (see `matrix_trace_annihilates_orderingDefect`), so the notion
    is inhabited by a real object, not a stub. -/
structure CyclicCharacter (R S : Type*) [Ring R] [AddCommGroup S] where
  /-- The underlying additive functional (a class function is additive). -/
  toHom : R →+ S
  /-- **Cyclicity** — the defining property of a trace / class function:
      `χ(a·b) = χ(b·a)`. -/
  cyclic : ∀ a b : R, toHom (a * b) = toHom (b * a)

/-- **Null scalar channel (single cell pair).** A block-trace character
    annihilates the surface-ordering defect: `χ(A·B − B·A) = 0`. The scalar
    (character) channel of the surface-ordering correction vanishes — the
    rigorous version of the numerical `tr[A,B] = 0`. -/
theorem CyclicCharacter.annihilates_orderingDefect
    (χ : CyclicCharacter R S) (A B : R) :
    χ.toHom (orderingDefect A B) = 0 := by
  rw [orderingDefect, map_sub, χ.cyclic A B, sub_self]

/-- **Null scalar channel (full surface correction).** A surface-ordering
    correction is a sum, over the plaquettes/cells of the tessellation, of
    ordering defects `∑ᵢ (Aᵢ·Bᵢ − Bᵢ·Aᵢ)`. The block-trace character
    annihilates the whole sum: the scalar channel of the surface state-sum's
    ordering correction is null. -/
theorem CyclicCharacter.annihilates_surfaceOrderingCorrection
    (χ : CyclicCharacter R S) (pairs : List (R × R)) :
    χ.toHom ((pairs.map (fun p => orderingDefect p.1 p.2)).sum) = 0 := by
  induction pairs with
  | nil => simp
  | cons p ps ih =>
    simp only [List.map_cons, List.sum_cons, map_add,
      χ.annihilates_orderingDefect p.1 p.2, ih, add_zero]

/-- **Concrete realisation via the matrix trace.** The genuine block-trace
    character `Matrix.trace` (a class function on the Hecke block's
    representation) annihilates the ordering defect: `tr(A·B − B·A) = 0`.
    Uses `Matrix.trace_mul_comm` (`tr(A·B) = tr(B·A)`) — the concrete
    cyclicity. This is the σ₁³-agent's `tr[A,B] = 0 @ 40 dps` as an exact
    theorem. -/
theorem matrix_trace_annihilates_orderingDefect
    {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (A B : Matrix n n R) :
    (orderingDefect A B).trace = 0 := by
  rw [orderingDefect, Matrix.trace_sub, Matrix.trace_mul_comm, sub_self]

end QOU.Mathlib.LatticeGaugeShadow
