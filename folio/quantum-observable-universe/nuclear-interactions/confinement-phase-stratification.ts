import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-phase-stratification",
  title:
    "The confinement locus is open, and the active support is constant on a strictly complementary phase",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementPhaseStratification",
    validation: "not_checked",
  },
  uses: ["def:confined-particle", "prop:confinement-sdp"],
  tags: [
    "phase",
    "phase-boundary",
    "stratification",
    "open-set",
    "regime-switch",
    "deconfinement",
    "sdp-feasibility",
    "local-constancy",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Until this date the Lean carried openness and the constancy of the binding multiplicity as fields of a class over opaque `confined` and `mu`, and the theorems returned those fields. The statement now writes strict feasibility as finitely many continuous strict inequalities, and Lean derives openness and constancy (the latter under continuity and strict complementarity of the dual pair, stated as hypotheses). The boundary stratification, analyticity of the stability index, scope and phase transitions moved to `conj:confinement-phase-boundaries`.",
    },
  ],
});
