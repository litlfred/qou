import Mathlib.Tactic

/-!
# QOU.Archimedean.SingleVolumeIrrationality — conjecture carrier (content-bearing, no instance)

**§3b-cond class axiomatisation** for content block
[`conj:single-volume-irrationality`](../../../quantum-observable-universe/archimedean-universe/single-volume-irrationality.md): *Irrationality of a single hyperbolic knot volume*.

This is a **conjecture**, and the honest open state is a **content-bearing class
with no instance** (AGENTS.md §3b-tax). `SingleVolumeIrrationality` carries three real volume fields (`vol41`, `vol52`, `volBorromean`) and one
`Irrational` field for each — the conjecture's content, not a placeholder.

**No instance is provided anywhere in this file.** An instance *is* the
conjecture; fabricating one would be the audit-dodge §1a forbids. A downstream
result takes `[SingleVolumeIrrationality]` as an explicit `[Instance]` hypothesis and
is thereby **conditional on it** — rigorous modulo this single named input, per
§3b-cond. It is not unconditional, and calling it so would be the
"conditional-proved ≠ premise-established" confusion AGENTS.md warns about.
-/

namespace QOU.Archimedean

/-- Irrationality of a single hyperbolic knot volume

    Conjectural class — see [`conj:single-volume-irrationality`](../../../quantum-observable-universe/archimedean-universe/single-volume-irrationality.md). -/
class SingleVolumeIrrationality where
  -- Witness: computations/none
  /-- **Content statement** (from manuscript):

      $$
  \mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \notin \mathbb{Q},
  \qquad
  \mathrm{Vol}(5_2) \notin \mathbb{Q},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3) \notin \mathbb{Q}.
$$

      The fields assert the conjecture's shape: irrationality of
      each volume.  The three volume fields are data pinned by the
      manuscript's definitions ($2\,\mathrm{Cl}_2(\pi/3)$ etc.);
      tying them to formalised Clausen/Lobachevsky values is the
      remaining refinement. -/
  vol41 : ℝ
  vol52 : ℝ
  volBorromean : ℝ
  /-- $\mathrm{Vol}(4_1) \notin \mathbb{Q}$. -/
  vol41_irrational : Irrational vol41
  /-- $\mathrm{Vol}(5_2) \notin \mathbb{Q}$. -/
  vol52_irrational : Irrational vol52
  /-- $\mathrm{Vol}(\mathcal{B}_3) \notin \mathbb{Q}$. -/
  volBorromean_irrational : Irrational volBorromean

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/single-volume-irrationality.ts
-- **No instance is provided — that is the honest open state** (AGENTS.md §3b-tax).
-- History: this file previously carried
--     axiom singleVolumeIrrationality_conjecture : SingleVolumeIrrationality
--     noncomputable instance : SingleVolumeIrrationality := singleVolumeIrrationality_conjecture
-- i.e. the conjecture was asserted by `axiom` and installed as a global instance, so
-- every downstream `[SingleVolumeIrrationality]` resolved for free.  Removed, not completed — downstream
-- results must take `[SingleVolumeIrrationality]` as an explicit hypothesis.

end QOU.Archimedean
