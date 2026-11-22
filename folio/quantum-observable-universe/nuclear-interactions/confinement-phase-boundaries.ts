import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:confinement-phase-boundaries",
  title: "Phase boundaries of the confinement locus",
  uses: [
    "prop:confinement-phase-stratification",
    "prop:level-sufficiency",
    "prop:shell-closure-stability",
    "thm:parity-regime-selection",
    "rem:deconfinement-golden-threshold",
  ],
  tags: [
    "phase",
    "phase-boundary",
    "stratification",
    "regime-switch",
    "deconfinement",
    "strict-complementarity",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Claims 2, 4 and 5 and the analyticity of the Frobenius stability index were part of `prop:confinement-phase-stratification` until this date, with a proof that cited perturbation lemmas but did not establish them. Lean proved openness and the constancy of the active support (under continuity and strict complementarity of the dual pair); the rest moved here as a conjecture after an attempt to prove it (owner: \"Can we prove conjecures/reformulate?\", thread \"N2 Lean foundations\").",
    },
  ],
});
