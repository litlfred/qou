import Mathlib.Data.Real.Basic
import QOU.Shared.MarkovTraceClaim

/-!
# QOU.HadronicMass.deuteron_binding_energy

**Canonical declaration** for content block
[`lem:deuteron-binding-energy`](../../../quantum-observable-universe/observations/deuteron-binding-energy.md): *Deuteron binding energy from Skein-polynomial smoothing*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

## Base ring (§7c) — `ℝ` here is correct

`DeuteronBindingEnergyContext` extends `QOU.Shared.MarkovTraceContext`, which
supplies a generic coefficient ring `R`, but this block's fields stay at `ℝ`
and that is the right call: `ΔE_exp = 2.2246` is a CODATA value in MeV and the
precision sub-claim is `|ΔE_bind − ΔE_exp| < 0.001`, an absolute value and an
order comparison.  Both are archimedean, so the block sits after the
substrate→archimedean wall.  Reviewed under bean `qou-mtcx`; do not "port" it
to `R` to reduce an `ℝ` count.
-/

namespace QOU.HadronicMass


/-- Abstract context for the `deuteron_binding_energy` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class DeuteronBindingEnergyContext extends QOU.Shared.MarkovTraceContext where
  /-- Predicted deuteron binding energy `ΔE_bind` (MeV). -/
  ΔE_bind : ℝ
  /-- CODATA experimental value 2.2246 MeV. -/
  ΔE_exp : ℝ
  /-- CODATA experimental value matches the theoretical 2.2246 MeV. -/
  h_ΔE_exp : ΔE_exp = 2.2246
  /-- Predicted value matches CODATA to sub-keV precision. -/
  h_ΔE_bind_precision : |ΔE_bind - ΔE_exp| < 0.001

/-- **Lemma statement** (from manuscript):

The deuteron is the six-component link $L_6$ formed by joining the
proton and neutron Borromean braids.  Its binding energy equals the
change in the Skein polynomial when the proton--neutron crossing is
smoothed,*

$$
  \Delta \mathfrak{E}_{\mathrm{bind}} \approx 2.224\,\text{MeV},
$$

*matching the CODATA value $2.2246\,\text{MeV}$ to sub-keV precision.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/deuteron-binding-energy.ts
theorem deuteron_binding_energy [ctx : DeuteronBindingEnergyContext] :
    ctx.ΔE_exp = 2.2246 ∧ |ctx.ΔE_bind - ctx.ΔE_exp| < 0.001 :=
  ⟨ctx.h_ΔE_exp, ctx.h_ΔE_bind_precision⟩

end QOU.HadronicMass
