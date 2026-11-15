import QOU.Shared.MarkovTraceClaim

/-!
# QOU.Torsion.antiparticle_crossing_reversal

**Canonical declaration** for content block referenced by
`qou:QOU.Torsion.antiparticle_crossing_reversal`.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.Torsion


/-- Abstract context for the `antiparticle_crossing_reversal` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class AntiparticleCrossingReversalContext extends QOU.Shared.MarkovTraceContext where
  /-- Crossing energy of a hadron, valued in the inherited coefficient ring
      `R` of the parent Markov-trace context: the crossing energy is read off
      the Hecke crossing coefficients, so it is a Laurent expression in `q`
      and the bar-involution `q ↔ q⁻¹` acts on it inside `R`. -/
  E_cross : R
  /-- Crossing energy of the corresponding antihadron. -/
  E_cross_anti : R
  /-- Crossing energy evaluated under `q ↔ q⁻¹` swap. -/
  E_cross_bar : R
  /-- Braid type (for the mirror operation). -/
  Braid : Type
  /-- Braid representative of a hadron and its mirror image. -/
  β_hadron : Braid
  β_anti : Braid
  /-- Mirror involution `σ ↦ σ⁻¹` on braids. -/
  mirror : Braid → Braid
  /-- Coulomb charge of a hadron and its antihadron. -/
  Q_charge : R
  Q_charge_anti : R
  /-- Topological (relational) mass of a hadron and its antihadron.  This is
      the *relational* mass — a knot-type invariant, not an archimedean MeV
      value — so it too lives in `R`. -/
  m_topological : R
  m_topological_anti : R
  /-- Proposition: antiparticle crossing reversal holds. -/
  crossing_reversal_holds : Prop
  /-- Hypothesis that crossing reversal is active. -/
  reversal_active : crossing_reversal_holds
  /-- Manuscript sub-claim (i) — Crossing reversal defines the
      antihadron via the braid-mirror involution: `β_anti = mirror β`. -/
  impl_crossing_reversal_defines :
    crossing_reversal_holds →
    β_anti = mirror β_hadron ∧ ∀ b : Braid, mirror (mirror b) = b
  /-- Manuscript sub-claim (ii) — Crossing energy sign reversal under
      `q ↔ q⁻¹`: `E_cross(𝔋^σ) = −E_cross(𝔋)|_{q ↔ q⁻¹}`. -/
  impl_crossing_energy_sign :
    haveI := ringR; crossing_reversal_holds → E_cross_anti = - E_cross_bar
  /-- Manuscript sub-claim (iii) — Coulomb charge reversal:
      `Q(𝔋^σ) = −Q(𝔋)`. -/
  impl_coulomb_charge_reversal :
    haveI := ringR; crossing_reversal_holds → Q_charge_anti = - Q_charge
  /-- Manuscript sub-claim (iv) — Topological mass invariance: the mirror
      preserves the knot type so `m_topological(𝔋^σ) = m_topological(𝔋)`. -/
  impl_topological_mass_invariance : crossing_reversal_holds → m_topological_anti = m_topological

/-- **Content statement** (from manuscript):

Let $T_{2,3}$ be the left trefoil (the electron generator) and
$T_{2,3}^{\sigma}$ its mirror image (all crossings reversed).

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/antiparticle-crossing-reversal.ts
theorem antiparticle_crossing_reversal [ctx : AntiparticleCrossingReversalContext] :
    (ctx.β_anti = ctx.mirror ctx.β_hadron ∧
     ∀ b : ctx.Braid, ctx.mirror (ctx.mirror b) = b) ∧
    (haveI := ctx.ringR; ctx.E_cross_anti = - ctx.E_cross_bar) ∧
    (haveI := ctx.ringR; ctx.Q_charge_anti = - ctx.Q_charge) ∧
    ctx.m_topological_anti = ctx.m_topological :=
  ⟨ctx.impl_crossing_reversal_defines ctx.reversal_active,
   ctx.impl_crossing_energy_sign ctx.reversal_active,
   ctx.impl_coulomb_charge_reversal ctx.reversal_active,
   ctx.impl_topological_mass_invariance ctx.reversal_active⟩

end QOU.Torsion
