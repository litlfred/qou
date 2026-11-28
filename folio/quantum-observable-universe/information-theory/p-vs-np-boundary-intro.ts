import { prose } from "../../schema/builders";

export default prose({
  label: "sec:p-vs-np-boundary-intro",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-28",
      body:
        "Rewritten on owner instruction (Carl, 2026-11-28: re-evaluate the P vs NP statements in view of intent, cellular automata and inner vs outer automorphisms; make it clear in the section intro, no separate write-up). Owner ruling the same day: a Lean result counts only if it has a human-readable equivalent stated against Mathlib and QOU definitions. " +
        "Lean carriers of the 'proved' list: `QOU.Information.commutatorSubmodule_le_ker_of_trace`, `QOU.Information.trace_comp_innerDerivation_eq_zero`, `QOU.Information.not_inner_of_hh1Class_ne_zero`; `QOU.GoldmanIwahori.theta`, `theta_theta`, `theta_not_inner`, `trace_theta_invariant_iff`, `convD_theta_forces`; `QOU.IntentHolonomy.hol_gauge_closed`, `classFun_gauge_invariant`, `hol_flux`, `flux_coboundary_is_gauge`; `HeckeTemperleyLieb.HeckeH3Semisimple`, `HeckeH4Semisimple`, `QOU.MathlibExt.WenzlSchurElement.schurElement_ne_zero`, `wenzlGeneric_of_one_lt`; `QOU.Information.superPoly_two_pow`, `two_pow_le_resolutionTreeSize`, `qou_physical_intractability_unconditional`. " +
        "Formal-content-vs-intent flags: `QOU.Information.chiResidual := -6` with `chiResidual_ne_zero`; `PNeqNPInQOU decisionCost := ¬ FamilyPolyBounded decisionCost` for an arbitrary `decisionCost`; `CountingDecisionWorld` treats P = NP and FP = #P as opaque `Prop`s (and its `toda` field is the elementary inclusion NP ⊆ P^#P, not Toda's theorem PH ⊆ P^#P); `QOU.PvsNPBoundary.boundary_dichotomy` is the classical dichotomy only; `OuterDerivationResidue` places any residue at roots of unity, which contradicts the non-torsion localisation in the earlier intro.",
    },
  ],
  cites: [
    "cook1971",
    "jaeger1990",
    "geckpfeiffer2000",
    "bakergillsolovay1975",
    "razborovrudich1997",
    "aaronsonwigderson2009",
  ],
});
