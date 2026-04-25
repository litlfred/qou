/-!
# QOU.AppendixSurreals.BirthdayGrading — Birthday-graded hom-spaces

A birthday grading on a `K`-linear hom-space `H` is an ordinal-indexed
filtration `filter α : Submodule K H` with `filter` monotone in `α`
and exhaustive.

This module provides:

- the `BirthdayGrading` structure (filter family + monotonicity +
  exhaustiveness fields);
- helper definitions `archimedeanPart` (= `filter ω`) and
  `firstOrderPart` (= `filter (ω + 1)`);
- a few lattice lemmas (`archimedeanPart ≤ firstOrderPart`,
  `filter α ≤ ⊤`, `⊥ ≤ filter α`, exhaustiveness extraction).

Closure of `filter` under sum / scalar action is **not** proved
here — these would require the additional arithmetic-on-birthdays
lemmas from the surrounding `SurrealField` axioms and are deferred
to a future expansion of this module.

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press.

LaTeX label: `def:birthday-grading`
-/

import Mathlib.LinearAlgebra.Span
import Mathlib.SetTheory.Ordinal.Arithmetic
import QOU.AppendixSurreals.Basic

namespace QOU.AppendixSurreals

universe u

variable {K : Type u} [SurrealField K]
variable {H : Type u} [AddCommGroup H] [Module K H]

/-- A **birthday grading** on a `K`-linear hom-space `H` is an
    ordinal-indexed filtration of `H` by `K`-submodules. -/
-- Ref: [conway1976] §0, [gonshor1986] §2
structure BirthdayGrading (K : Type u) [SurrealField K]
    (H : Type u) [AddCommGroup H] [Module K H] where
  /-- The birthday-`≤ α` submodule. -/
  filter : Ordinal → Submodule K H
  /-- Filtration is monotone in α. -/
  mono : ∀ {α β : Ordinal}, α ≤ β → filter α ≤ filter β
  /-- Filtration exhausts `H`. -/
  exhaustive : ⨆ α, filter α = ⊤

namespace BirthdayGrading

variable (G : BirthdayGrading K H)

/-- The **archimedean part** of the grading: hom elements of birthday `≤ ω`. -/
def archimedeanPart : Submodule K H := G.filter Ordinal.omega0

/-- The **first-order infinitesimal layer**: filter at birthday ω+1. -/
def firstOrderPart : Submodule K H := G.filter (Ordinal.omega0 + 1)

/-- Archimedean is contained in first-order. -/
theorem archimedeanPart_le_firstOrderPart :
    G.archimedeanPart ≤ G.firstOrderPart := by
  unfold archimedeanPart firstOrderPart
  exact G.mono (Ordinal.le_add_right Ordinal.omega0 1)

/-- Filter at any ordinal is contained in `⊤`. -/
theorem filter_le_top (α : Ordinal) : G.filter α ≤ ⊤ := le_top

/-- The zero submodule is contained in every filter stage. -/
theorem bot_le_filter (α : Ordinal) : ⊥ ≤ G.filter α := bot_le

/-- Every element of `H` lies in some filter stage. -/
theorem exists_filter_mem (x : H) :
    ∃ α : Ordinal, x ∈ G.filter α := by
  have hx : x ∈ (⊤ : Submodule K H) := Submodule.mem_top
  rw [← G.exhaustive] at hx
  exact (Submodule.mem_iSup_of_directed _ (fun α β =>
    ⟨α ⊔ β, G.mono (le_sup_left), G.mono (le_sup_right)⟩)).mp hx

end BirthdayGrading

end QOU.AppendixSurreals
