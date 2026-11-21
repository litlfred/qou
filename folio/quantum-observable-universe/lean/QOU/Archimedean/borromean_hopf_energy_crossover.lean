import Mathlib.Data.Real.Basic

/-!
# QOU.Archimedean.borromean_hopf_energy_crossover

Canonical Lean declaration for content block at
[`quantum-observable-universe/observations/borromean-hopf-energy-crossover.ts`](quantum-observable-universe/observations/borromean-hopf-energy-crossover.ts).

The three manuscript sub-claims (the two phase-mass formulae and the
crossover condition) are stated over the **opaque physical input** `V_B`
(the Borromean volume); no faithful Mathlib structure realises the
phase-mass map, so per the vacuity-fix playbook pattern C the proposition
is **named** as a `def … : Prop` over the context — honestly recording the
conditional conjecture rather than projecting context fields.  The context
class carries the genuine *inputs*; a Lean instance would be the conjecture.

The crossover conjunct was a `diquark_favoured : Prop` field until
2026-09-07, read back as `ctx.diquark_favoured ↔ |E_D| > |E_B|`.  A field
typed with the *universe* `Prop` holds a proposition as DATA, so the
instance chose it: `diquark_favoured := |E_D| > |E_B|` made that conjunct
`Iff.rfl` and it constrained nothing.  The manuscript states the condition
outright — *"The crossover occurs when |𝔈_D| > |𝔈_B|"* — so it is now
stated outright, over `E_B` and `E_D`, which the context already carries.
-/

namespace QOU.Archimedean


/-- Abstract context (inputs) for the `borromean_hopf_energy_crossover`
    claim — the substrate parameter, the Borromean volume, and the two
    phase masses and binding energies.  No field asserts a conclusion. -/
class BorromeanHopfEnergyCrossoverContext where
  /-- Substrate parameter `q : ℝ` (`q > 1`). -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Borromean hyperbolic volume `V_B ≈ 7.32772`. -/
  V_B : ℝ
  /-- Mass of the Borromean phase (two `B_3` baryons + inter-baryon Hopf
      binding). -/
  M_B : ℝ
  /-- Mass of the Hopf-diquark phase. -/
  M_D : ℝ
  /-- Binding energy per baryon-number in the Borromean phase. -/
  E_B : ℝ
  /-- Binding energy per baryon-number in the diquark phase. -/
  E_D : ℝ

/-- **Manuscript statement** (full body):

**Proposition.**
Let $q > 1$ be the substrate parameter and $\hbar_q = (q-1)/q$.
Consider $6$ quarks (two baryon-number units) with flavor content
$(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})^{\otimes 2}$.  These
$6$ quarks can be assembled in two topologically distinct
configurations:

- **Borromean phase** ($\mathcal{P}_B$): two Borromean baryons
  $\mathcal{B}_3 \cdot \mathcal{B}_3$, each with Borromean
  volume $V_B = 7.32772$ and inter-baryon Hopf binding.

- **Diquark phase** ($\mathcal{P}_D$): three Hopf diquark
  pairs ([Hopf diquark](#def:hopf-diquark))
  $D_{[\mathfrak{u}\mathfrak{d}]} \cdot D_{[\mathfrak{d}\mathfrak{s}]} \cdot D_{[\mathfrak{s}\mathfrak{u}]}$, each bound by $\mathcal{L}_H$.

Then:

1. **Mass comparison.**  The Borromean phase has mass

$$
  M_B
  = 
  2 \cdot \frac{V_B}{\hbar_q^2}
  = 
  \frac{2 \times 7.32772}{((q-1)/q)^2}
  = 
  \frac{14.6554 q^2}{(q-1)^2}.
$$

   The diquark phase has mass from crossing energy only
   (Hopf link volume is zero):

$$
  M_D
  = 
  3 \cdot \tfrac{1}{3}(q + q^{-1})
  = 
  q + q^{-1}
   \approx  2.011  \text{Skein units}.
$$

   Since $\mathrm{Vol}(\mathcal{L}_H) = 0$, the diquark
   mass is **purely from crossing energy**, not from
   hyperbolic volume.  At any $q > 1$: $M_D \ll M_B$.

2. **Binding energy comparison.**  The binding energy
   per baryon number is:

   - Borromean: $\mathfrak{E}_B = -V_B / \hbar_q^2$ (from
     Borromean volume)
   - Diquark: $\mathfrak{E}_D = -\tfrac{3}{2}(q + q^{-1})$
     (from three Hopf links shared between two baryon-number
     units, strong channel only since the CFL condensate is
     color-neutral)

   The crossover occurs when $|\mathfrak{E}_D| > |\mathfrak{E}_B|$,
   i.e., when the Hopf-link binding per baryon number exceeds
   the Borromean binding:

$$
  \frac{3}{2}(q + q^{-1})
   > 
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772 q^2}{(q-1)^2}.
$$

3. **At $q = q_0$.**

$$
  \frac{3}{2}(q + q^{-1})
  = 
  \frac{3}{2}(q_0 + q_0^{-1})
  = 
  \frac{3}{2} \times 2.0108
  =  3.

[…truncated; see manuscript for remainder…]

    The proposition is **named** below as a `def … : Prop` (pattern C):
    `V_B` and the energy-comparison predicate are opaque inputs, so the
    three-part claim is recorded as the conditional conjecture over the
    context rather than discharged by a fake projection. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/borromean-hopf-energy-crossover.ts
def borromean_hopf_energy_crossover (ctx : BorromeanHopfEnergyCrossoverContext) :
    Prop :=
  ctx.M_B = 2 * ctx.V_B / ((ctx.q - 1) / ctx.q) ^ 2 ∧
  ctx.M_D = ctx.q + ctx.q⁻¹ ∧
  |ctx.E_D| > |ctx.E_B|

end QOU.Archimedean
