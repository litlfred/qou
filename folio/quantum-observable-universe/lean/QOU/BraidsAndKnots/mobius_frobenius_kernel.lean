import Mathlib.Tactic
import Mathlib.Analysis.Normed.Group.Basic

/-!
# QOU.BraidsKnots.mobius_frobenius_kernel

Content block
[`lem:mobius-energy-frobenius-kernel`](../../../quantum-observable-universe/climax-volume-mass/mobius-energy-frobenius-kernel.md):
*Classical limit of the Frobenius--Hopf kernel is the repulsive $1/r^2$*.

**Manuscript statement.**
*At $q = 1$ the $q$-Hodge star reduces to the classical Hodge star,
and the Frobenius pairing $\int_A \circ \mu$ on $A \otimes A$ reduces
to the standard $\mathrm{SU}(2)$ Killing form.  The Frobenius--Hopf
kernel collapses to the repulsive $1/r^2$:*

$$
  \mathrm{tr}\bigl(
    \Delta(\gamma(s)) \otimes \Delta(\gamma(t))
  \bigr)
  \xrightarrow{q \to 1}
  \frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}.
$$

## Disposition (integrity)

The previous encoding was a self-assuming projection (AGENTS.md
§3b-cond item 5): the class carried a
`claim_mobius_frobenius_kernel` field that *was* the conclusion
(`K_classical = 1/r² ∧ (q = 1 → K_FH = K_classical)`), and a `def`
merely projected it back out.  Here `MobiusFrobeniusKernelContext`
separates the two independent structural reductions
(`kernel_tendsto_killing` and `killing_eq_inverse_square`),
`mobius_frobenius_kernel` derives the deformation limit
`K_FH(q; s, t) → 1/‖γ(s) − γ(t)‖²` as `q → 1` at distinct filament
points without `sorry`, and `qDeformedMobiusFrobeniusContext` provides
a genuinely `q`-dependent inhabiting model (`K_FH(q; s, t) = q / ‖s − t‖²`).
-/

namespace QOU.BraidsKnots

open Filter Topology

/-- Data of the Möbius-energy / Frobenius–Hopf-kernel claim
    ([`lem:mobius-energy-frobenius-kernel`]).

    **RESTRUCTURED 2026-09-13 — the previous version carried the CONCLUSION
    as a field.** It had a single field `classical_limit` whose statement was,
    verbatim and with the same binders, the theorem below; the theorem's body
    was `ctx.classical_limit s t hst`. That is the self-assuming projection
    AGENTS.md §3b-cond item 5 names, and the class docstring asserted the
    opposite of what the code did — *"All fields are inputs; none is the
    conclusion"* — while the conclusion was field three of three.

    The two fields that replace it are **exactly the two reductions the
    theorem's own docstring says the proof requires**, and neither is the
    conclusion:

    * `kernel_tendsto_killing` — the `q`-Hodge star reduces to the classical
      Hodge star, so the `q → 1` limit **exists** and is the Frobenius
      pairing's classical kernel. Its limit point is the abstract
      `killingKernel`, not the target value.
    * `killing_eq_inverse_square` — the Frobenius pairing `∫_A ∘ μ` reduces to
      the `SU(2)` Killing form, and that form evaluates to the inverse square.
      A pointwise algebraic identity; no limit appears in it.

    **What this does and does not buy, stated plainly.** The *conjunction* of
    the two is equivalent to the old single field — splitting an assumption
    does not discharge it, and this file still proves no analysis. What
    changes is that the obligation is **localised**: an instantiator now faces
    the two named unformalised reductions separately rather than one field
    spelling out the answer, and the theorem below **derives** its conclusion
    instead of projecting it.

    The second field is no longer an arbitrary target. `QOU.MobiusMutualChannel`
    §7–§8 prove the inverse square is the **unique** Möbius-invariant separation
    kernel — on unconstrained triples (`mobiusInvariant_forces_inverse_square`)
    and on geometrically realisable ones (`realisable_forces_inverse_square`),
    both sorry-free. So `killing_eq_inverse_square` asserts that the Killing
    form lands on the kernel that symmetry independently forces, rather than on
    a value chosen to match. -/
class MobiusFrobeniusKernelContext (E : Type*) [NormedAddCommGroup E] where
  /-- Knot filament curve `γ : ℝ → E` (arc-length parametrised). -/
  γ : ℝ → E
  /-- `q`-parametrised Frobenius–Hopf kernel: `K_FH q s t` is the trace
      `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` of the Frobenius pairing at deformation
      parameter `q`. -/
  K_FH : ℝ → ℝ → ℝ → ℝ
  /-- The Frobenius pairing's **classical** (`q = 1`) kernel, carried
      abstractly. Kept separate from `1/r²` on purpose: the two fields below
      are then independent claims rather than one claim and its restatement. -/
  killingKernel : ℝ → ℝ → ℝ
  /-- **Reduction 1 — the `q`-Hodge star reduces to the classical Hodge star.**
      The deformation limit exists and is the classical kernel. Not the
      conclusion: the limit point is `killingKernel`, an opaque field. -/
  kernel_tendsto_killing : ∀ (s t : ℝ), γ s ≠ γ t →
    Filter.Tendsto (fun q => K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (killingKernel s t))
  /-- **Reduction 2 — the Frobenius pairing reduces to the `SU(2)` Killing
      form, which evaluates to the inverse square.** Not the conclusion: a
      pointwise identity between two kernels, containing no limit. -/
  killing_eq_inverse_square : ∀ (s t : ℝ), γ s ≠ γ t →
    killingKernel s t = 1 / ‖γ s - γ t‖ ^ 2

/-- **Classical limit of the Frobenius–Hopf kernel is the repulsive
    `1/r²`** ([`lem:mobius-energy-frobenius-kernel`]) — the resolving
    declaration for `lean.ref`
    `qou:QOU.BraidsKnots.mobius_frobenius_kernel`.

    At distinct filament points `γ(s) ≠ γ(t)`, the Frobenius–Hopf
    kernel `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` collapses, in the deformation
    limit `q → 1`, to the Möbius-energy kernel `1/‖γ(s) − γ(t)‖²`.

    **The statement is unchanged; the proof is now a derivation.** The body
    rewrites the target through reduction 2 and discharges it with reduction 1.
    Previously it was `ctx.classical_limit s t hst` — a projection of a field
    that *was* this conclusion. Both the old and the new version are sorry-free
    and report the same axioms, which is the point: `#print axioms` cannot tell
    a derivation from a restatement, and did not. -/
-- Ref: [leitner2026] lem:mobius-energy-frobenius-kernel, quantum-observable-universe/climax-volume-mass/mobius-energy-frobenius-kernel.md
theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ)
    (hst : ctx.γ s ≠ ctx.γ t) :
    Filter.Tendsto (fun q => ctx.K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) := by
  rw [← ctx.killing_eq_inverse_square s t hst]
  exact ctx.kernel_tendsto_killing s t hst

/-! ## Non-vacuity — the class is inhabited, so the theorem is about something

`qou-z9ws` sized the self-assuming-projection population at ~102 independent
defects and fixed the discriminator that separates a genuine defect from the
legitimate Mathlib accessor idiom: **a projection is legitimate only when
something builds the bundle.** Every one of the twelve it sampled was
uninhabited. Restructuring the fields above without exhibiting an instance
would leave this file in that same bucket — a conditional true of nothing.
-/

/-- **A context exists.** The degenerate one: a `q`-independent kernel already
    equal to the inverse square, on `E = ℝ` with `γ = id`.

    Deliberately trivial. It witnesses that the three fields are **mutually
    consistent** — which is all inhabitation can show — and it is emphatically
    not the Frobenius–Hopf kernel, whose `q`-dependence is the entire content
    of reduction 1. -/
noncomputable def inverseSquareContext : MobiusFrobeniusKernelContext ℝ where
  γ := id
  K_FH := fun _ s t => 1 / ‖s - t‖ ^ 2
  killingKernel := fun s t => 1 / ‖s - t‖ ^ 2
  kernel_tendsto_killing := fun _ _ _ => tendsto_const_nhds
  killing_eq_inverse_square := fun _ _ _ => rfl

/-- **A genuinely `q`-dependent context exists.** On `E = ℝ` with `γ = id`,
    the linearly `q`-scaled kernel `K_FH q s t = q * (1 / ‖s - t‖ ^ 2)` varies
    non-trivially with `q` and converges to `killingKernel s t = 1 / ‖s - t‖ ^ 2`
    as `q → 1`. -/
noncomputable def qDeformedMobiusFrobeniusContext : MobiusFrobeniusKernelContext ℝ where
  γ := id
  K_FH := fun q s t => q * (1 / ‖s - t‖ ^ 2)
  killingKernel := fun s t => 1 / ‖s - t‖ ^ 2
  kernel_tendsto_killing := fun s t _ => by
    have hcont : Continuous (fun q : ℝ => q * (1 / ‖s - t‖ ^ 2)) :=
      continuous_id.mul continuous_const
    have hlim : Filter.Tendsto (fun q : ℝ => q * (1 / ‖s - t‖ ^ 2))
        (nhds 1) (nhds (1 / ‖s - t‖ ^ 2)) := by
      simpa [one_mul] using hcont.tendsto 1
    exact tendsto_nhdsWithin_of_tendsto_nhds hlim
  killing_eq_inverse_square := fun _ _ _ => rfl

/-- The `q`-deformed model kernel depends genuinely on `q` (`K_FH 2 0 1 ≠ K_FH 1 0 1`). -/
theorem qDeformedMobiusFrobeniusContext_q_dependent :
    qDeformedMobiusFrobeniusContext.K_FH 2 0 1 ≠
      qDeformedMobiusFrobeniusContext.K_FH 1 0 1 := by
  simp [qDeformedMobiusFrobeniusContext]

/-- **So `MobiusFrobeniusKernelContext` is inhabitable**, witnessed by the
    genuinely `q`-dependent context `qDeformedMobiusFrobeniusContext`. -/
theorem nonempty_mobiusFrobeniusKernelContext :
    Nonempty (MobiusFrobeniusKernelContext ℝ) :=
  ⟨qDeformedMobiusFrobeniusContext⟩

end QOU.BraidsKnots
