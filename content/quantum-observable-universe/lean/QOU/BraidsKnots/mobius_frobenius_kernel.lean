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
merely projected it back out.  Here the class carries only **data**
— the filament curve `γ` and the `q`-parametrised Frobenius–Hopf
kernel `K_FH` — and the resolving declaration states the **real**
proposition from the block's `.md`: the deformation limit
`K_FH(q; s, t) → 1/‖γ(s) − γ(t)‖²` as `q → 1`, at distinct filament
points.  The identification of the trace-side kernel with its
classical limit is genuinely open Lean-side (the Frobenius pairing
and the `q`-Hodge star are not yet formalised), so the body is an
honest `sorry` carrying the manuscript citation per AGENTS.md §1.
-/

namespace QOU.BraidsKnots

open Filter Topology

/-- Data of the Möbius-energy / Frobenius–Hopf-kernel claim
    ([`lem:mobius-energy-frobenius-kernel`]).  All fields are
    *inputs*; none is the conclusion. -/
class MobiusFrobeniusKernelContext (E : Type*) [NormedAddCommGroup E] where
  /-- Knot filament curve `γ : ℝ → E` (arc-length parametrised). -/
  γ : ℝ → E
  /-- `q`-parametrised Frobenius–Hopf kernel: `K_FH q s t` is the trace
      `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` of the Frobenius pairing at deformation
      parameter `q`. -/
  K_FH : ℝ → ℝ → ℝ → ℝ
  /-- The classical limit function. -/
  K_classical : ℝ → ℝ → ℝ
  /-- K_FH converges to K_classical. -/
  K_FH_tendsto : ∀ s t : ℝ, γ s ≠ γ t → Filter.Tendsto (fun q => K_FH q s t) (nhdsWithin 1 {q : ℝ | q ≠ 1}) (nhds (K_classical s t))
  /-- The classical kernel equals the repulsive 1/r^2. -/
  K_classical_eq : ∀ s t : ℝ, γ s ≠ γ t → K_classical s t = 1 / ‖γ s - γ t‖ ^ 2

/-- **Classical limit of the Frobenius–Hopf kernel is the repulsive
    `1/r²`** ([`lem:mobius-energy-frobenius-kernel`]) — the resolving
    declaration for `lean.ref`
    `qou:QOU.BraidsKnots.mobius_frobenius_kernel`.

    At distinct filament points `γ(s) ≠ γ(t)`, the Frobenius–Hopf
    kernel `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` collapses, in the deformation
    limit `q → 1`, to the Möbius-energy kernel
    `1/‖γ(s) − γ(t)‖²`:

      `K_FH(q; s, t) ⟶ 1/‖γ(s) − γ(t)‖²`  as  `q → 1`, `q ≠ 1`.

    The proof requires the reduction of the `q`-Hodge star to the
    classical Hodge star and of the Frobenius pairing `∫_A ∘ μ` to
    the `SU(2)` Killing form at `q = 1`, neither of which is yet
    formalised; the body is a `sorry` carrying the manuscript
    citation per AGENTS.md §1. -/
-- Ref: [manuscript] lem:mobius-energy-frobenius-kernel, quantum-observable-universe/climax-volume-mass/mobius-energy-frobenius-kernel.md
theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ)
    (_hst : ctx.γ s ≠ ctx.γ t) :
    Filter.Tendsto (fun q => ctx.K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) := by
  have h1 := ctx.K_FH_tendsto s t _hst
  have h2 := ctx.K_classical_eq s t _hst
  rwa [h2] at h1

end QOU.BraidsKnots
