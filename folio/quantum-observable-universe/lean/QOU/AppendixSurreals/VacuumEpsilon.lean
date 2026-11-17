import Mathlib.Data.Real.Basic

/-!
# QOU.AppendixSurreals.VacuumEpsilon — conjectural link-energy vacuum carrier (`qou-ffwk`)

**§3b-cond class axiomatisation** for content block
[`conj:vacuum-epsilon`](../../../quantum-observable-universe/appendix-surreals/vacuum-epsilon.md): *Infinitesimal vacuum: $\mathrm{Geom}(\bigcirc) = \varepsilon$*.

This is a **conjecture**: the class `VacuumEpsilon` is a primary conjecture
carrier with **no instance** — the honest open state per AGENTS.md §3b-tax.
Per bean `qou-ffwk`, the trivially-inhabited `residual = 0` placeholder has been
replaced by the actual link-energy vacuum structure: a link carrier `Link` with
chosen `unknot`, disjoint-union operation `disjointUnion`, geometric energy
functional `geom : Link → ℝ` satisfying `geom unknot = 0` and additivity under
disjoint union, and vacuum residual `residual = geom unknot`.

Downstream theorems take `[VacuumEpsilon]` as an explicit `[Instance]` hypothesis
to derive conditional Lean theorems against this named input (per §3b-cond).
-/

namespace QOU.AppendixSurreals

/-- Infinitesimal vacuum carrier (`conj:vacuum-epsilon`, bean `qou-ffwk`).

Carries the link type `Link`, the unknot `unknot`, disjoint union `disjointUnion`,
and the real-valued geometric energy functional `geom : Link → ℝ` normalized on
the unknot and additive under disjoint union. -/
class VacuumEpsilon where
  /-- Carrier of topological links in the scattering pipeline. -/
  Link : Type
  /-- The unknot (empty vacuum link). -/
  unknot : Link
  /-- Disjoint union of two links. -/
  disjointUnion : Link → Link → Link
  /-- Geometric energy functional `Geom(L) ∈ ℝ`. -/
  geom : Link → ℝ
  /-- Vacuum normalisation on the unknot: `Geom(◯) = 0`. -/
  geom_unknot : geom unknot = 0
  /-- Additivity of geometric energy under disjoint union of links. -/
  geom_disjointUnion : ∀ L₁ L₂ : Link, geom (disjointUnion L₁ L₂) = geom L₁ + geom L₂
  /-- Vacuum energy residual, identified with the unknot geometric energy. -/
  residual : ℝ
  /-- Identification of the vacuum residual with `geom unknot`. -/
  residual_eq_geom_unknot : residual = geom unknot

/-- Under `[VacuumEpsilon]`, the vacuum residual vanishes as a consequence of
`residual = geom unknot` and the unknot normalization `geom unknot = 0`. -/
theorem VacuumEpsilon.residual_eq_zero [v : VacuumEpsilon] :
    v.residual = 0 :=
  v.residual_eq_geom_unknot.trans v.geom_unknot

/-- Adjoining a vacuum unknot component on the right leaves the geometric link energy invariant. -/
theorem VacuumEpsilon.geom_disjointUnion_unknot_right [v : VacuumEpsilon] (L : v.Link) :
    v.geom (v.disjointUnion L v.unknot) = v.geom L := by
  rw [v.geom_disjointUnion L v.unknot, v.geom_unknot, add_zero]

/-- Adjoining a vacuum unknot component on the left leaves the geometric link energy invariant. -/
theorem VacuumEpsilon.geom_disjointUnion_unknot_left [v : VacuumEpsilon] (L : v.Link) :
    v.geom (v.disjointUnion v.unknot L) = v.geom L := by
  rw [v.geom_disjointUnion v.unknot L, v.geom_unknot, zero_add]

-- **No instance is provided — the honest open state** (AGENTS.md §3b-tax).

end QOU.AppendixSurreals
