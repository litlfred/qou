import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.LeviDegeneracy — `conj:levi-degeneracy` axiomatised

Conjectural content: **the Levi form of the $q$-NS singularity locus
degenerates exactly at the parameter values $q_\kappa = e^{i\pi/\kappa}$
($\kappa \geq 2$)**, and the degeneracy set is therefore countable.

This Lean axiomatisation works in the **real-parameter projection**:
the manuscript's complex principal-root family
$q_\kappa = e^{i\pi/\kappa}$ is parametrised by the angular fraction
$\theta_\kappa = \pi/\kappa$, and the Lean `degeneracySet` records
the angular reciprocal $1/\kappa \in \mathbb{R}$.  Each $1/\kappa$
is the unique real datum identifying the principal root $q_\kappa$
on the unit circle — formalising directly in $\mathbb{C}$ awaits
the complex-`q` substrate API (Mathlib root-of-unity machinery
indexed over an arbitrary `R`-valued parameter).

LaTeX label: `conj:levi-degeneracy`

## Conjectural content

Conjectural Levi-degeneracy: the contact form at a vortex-collision
locus is non-degenerate iff the q-NS flow remains regular through
the collision; equivalently, the Levi form on the q-NS singularity
locus is positive-definite away from $\{q_\kappa\}_{\kappa \geq 2}$.

## Status

Class-axiomatised per AGENTS.md §3b-cond. The conjecture sits in
the residual §3b-violator cone identified in
[`AUDIT-DEEP-2026-05.md`](../../../../AUDIT-DEEP-2026-05.md) §1A
(P1.b sweep). Class declaration here lets downstream
provable-kind blocks (in the same `uses[]` cone) become
`conditional-on-class` rather than violators.

`sorry` in any concrete instance is understood as **conjecture**,
not missing proof. Downstream blocks may take `[LeviDegeneracy]` as an
explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status under §3b-cond.

## References

- [leitner2026] §Levi degeneracy conjecture: contact non-degeneracy at
  vortex collision determines NS regularity, `conj:levi-degeneracy`
-/

namespace QOU.FluidDynamics

/-- **`conj:levi-degeneracy` (axiomatised).**

    The Levi form on the singularity locus of the $q$-NS evolution
    is positive-definite away from the discrete set
    $\{q_\kappa = e^{i\pi/\kappa} : \kappa \geq 2\}$ and degenerates
    exactly on it.  This Lean axiomatisation uses the
    real-parameter projection: each principal root $q_\kappa$ on the
    unit circle is identified by its angular reciprocal
    $1/\kappa \in \mathbb{R}$ (see file docstring).  A direct
    $\mathbb{C}$-valued formalisation awaits a complex-`q`
    substrate API. -/
class LeviDegeneracy where
  /-- The Levi-form pairing on the singularity locus. -/
  leviForm : ℝ → ℝ → ℝ
  /-- The degeneracy set: the locus on which the Levi form is not
      positive-definite, recorded as the real angular-reciprocal
      projection of the complex root family. -/
  degeneracySet : Set ℝ
  /-- The Levi form is symmetric. -/
  leviForm_symm : ∀ x y, leviForm x y = leviForm y x
  /-- **`degeneracySet` is the degeneracy locus OF `leviForm`.**

      Without this field the two are unrelated: `degeneracySet` could
      be any set at all and the Levi form would be inert decoration,
      so `levi_degeneracy_holds` below would assert nothing about the
      Levi form despite being the file's stated subject.  This is what
      makes the conjecture a statement about contact geometry rather
      than a bare set equality. -/
  degeneracy_iff :
    ∀ x : ℝ, x ∈ degeneracySet ↔ ¬ (0 < leviForm x x)
  /-- **The conjecture itself.**  The (real-parameter projection of
      the) degeneracy set is precisely the countable family
      $\{1/\kappa : \kappa \geq 2\}$, where each $1/\kappa$ is the
      angular reciprocal of the manuscript's principal-root parameter
      $q_\kappa = e^{i\pi/\kappa}$ on the unit circle. -/
  -- Ref: [leitner2026] fluid-dynamics/levi-degeneracy-conjecture
  levi_degeneracy_holds :
    degeneracySet = { x : ℝ | ∃ κ : ℕ, 2 ≤ κ ∧ x = 1 / (κ : ℝ) }

/-- **Levi positive-definiteness off the principal-root family**
    ([`conj:levi-degeneracy`]).

    The manuscript's actual claim — *"the Levi form is positive-definite
    away from $\{q_\kappa\}_{\kappa \geq 2}$"* — now follows, rather
    than being assumed: it composes `degeneracy_iff` (which locates the
    degeneracy set as the locus of `leviForm`) with
    `levi_degeneracy_holds` (which identifies that locus with the
    angular-reciprocal family).  Neither field states this on its own. -/
theorem levi_positive_definite_off_family [ctx : LeviDegeneracy]
    (x : ℝ) (hx : ¬ ∃ κ : ℕ, 2 ≤ κ ∧ x = 1 / (κ : ℝ)) :
    0 < ctx.leviForm x x := by
  by_contra hpos
  have hmem : x ∈ ctx.degeneracySet := (ctx.degeneracy_iff x).mpr hpos
  rw [ctx.levi_degeneracy_holds] at hmem
  exact hx hmem

/-- Converse direction: every member of the principal-root family is a
    genuine degeneracy of the Levi form.  Together with
    `levi_positive_definite_off_family` this is the "degenerates
    **exactly** on it" of the file docstring. -/
theorem levi_degenerate_on_family [ctx : LeviDegeneracy]
    (κ : ℕ) (hκ : 2 ≤ κ) :
    ¬ (0 < ctx.leviForm (1 / (κ : ℝ)) (1 / (κ : ℝ))) := by
  refine (ctx.degeneracy_iff _).mp ?_
  rw [ctx.levi_degeneracy_holds]
  exact ⟨κ, hκ, rfl⟩

end QOU.FluidDynamics
