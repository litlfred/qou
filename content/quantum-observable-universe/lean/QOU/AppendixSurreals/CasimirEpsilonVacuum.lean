/-!
# QOU.AppendixSurreals.CasimirEpsilonVacuum — conditional class (§3b-cond)

**§3b-cond class axiomatisation** for content block
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md):
*Casimir force as $\mathrm{st}$-image of $\varepsilon$-vacuum density gradient*.

This is a **conjecture**. Per CLAUDE.md §3b-cond, the conjecture is
axiomatised as a Lean `class` whose single field carries the open
content (the surreal coefficient of the plate-constrained unknot
density). A downstream consumer that takes both `VacuumEpsilon` and
this class as `[Instance]` hypotheses derives the textbook Casimir
energy gradient as a *conditional* theorem — fully verified by Lean
modulo the two named conjectural inputs.

The `class` is a parameter, not an asserted fact: it represents the
conjectural existence and scaling of a plate-constrained unknot-
density function. Closing the conjecture means *constructing* such
an instance from QOU primitives, not proving a Lean theorem.

The conditional theorem `energyPerArea_deriv` below is elementary
calculus on a polynomial in `1/d`; the `sorry` is the conjecture
itself in §3b-cond form (the class axiom is the conjectural input,
the calculus then proceeds as in the narrative
`casimir-epsilon-vacuum.md`).
-/

import QOU.AppendixSurreals.VacuumEpsilon
import QOU.AppendixSurreals.StandardPart
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic

namespace QOU.AppendixSurreals

/-- **Plate-mode-count class** — §3b-cond axiomatisation of the
    surreal-coefficient appearing in the parallel-plate Casimir
    conjecture.  See
    [`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md).

    The class carries the *archimedean image* of the surreal
    quantity `(N⊙^in − N⊙^out) · ε`.  The surreal `ε⁻¹` and `ε`
    cancel in the energy density `u(d) = ε·(N⊙^in − N⊙^out)/A`,
    leaving a real-valued function.  This class encodes that
    real-valued energy-density function directly. -/
class PlateModeCount where
  /-- Archimedean energy per unit area between two parallel
      conducting plates separated by `d`, in units where
      `ℏc = 1`.  The conjecture is that this equals
      `-π²/(720 d³)` — the standard-physics Casimir result. -/
  energyPerArea : ℝ → ℝ
  /-- Scaling axiom — the standard-physics result that the QOU
      derivation must reproduce.  Sign: negative (lower energy
      between plates than outside means the force is attractive). -/
  energyPerArea_eq :
    ∀ d : ℝ, 0 < d →
      energyPerArea d = -(Real.pi ^ 2) / (720 * d ^ 3)

/-- **Conditional Casimir-energy gradient** — §3b-cond conditional
    theorem.  Given the plate-mode-count class, the derivative of
    the energy per area is `π²/(240 d⁴)`; the force per area is
    minus this, i.e. `-π² ℏ c / (240 d⁴)` in dimensional units
    (textbook Casimir 1948).

    **Proof sketch (elementary calculus, to be filled in with
    explicit Mathlib API):**

    1. `energyPerArea_eq` lets us locally rewrite
       `energyPerArea x = -π²/720 · x⁻³` on `(0, ∞)` (open
       neighbourhood of `d`).
    2. `HasDerivAt (fun x => x⁻³) (-3 · d⁻⁴) d` from
       `hasDerivAt_zpow (-3) d (Or.inl (ne_of_gt hd))`.
    3. Multiplying by the constant `-π²/720` gives
       `HasDerivAt (energyPerArea) ((-π²/720) · (-3 · d⁻⁴)) d`
       via `HasDerivAt.const_mul`.
    4. `Filter.EventuallyEq.deriv_eq` transfers the derivative
       across the local rewrite.
    5. `(-π²/720) · (-3) = 3π²/720 = π²/240` by `ring` /
       `field_simp` / `norm_num`.

    The `VacuumEpsilon` instance is not used by this proof but is
    listed in the hypothesis to advertise the full §3b-cond
    conditional structure: both classes together are required to
    *interpret* this real-valued statement as the standard-part of
    the surreal mechanism in
    [`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md). -/
theorem energyPerArea_deriv
    [VacuumEpsilon] [PlateModeCount]
    (d : ℝ) (hd : 0 < d) :
    deriv PlateModeCount.energyPerArea d = Real.pi ^ 2 / (240 * d ^ 4) := by
  -- Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
  -- Ref: [manuscript] appendix-surreals/casimir-epsilon-vacuum.md
  sorry

end QOU.AppendixSurreals
