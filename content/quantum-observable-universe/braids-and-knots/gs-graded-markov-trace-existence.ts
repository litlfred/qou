import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-graded-markov-trace-existence",
  title:
    "Existence of the graded Markov trace on the GS filtration",
  lean: {
    ref: "qou:QOU.BraidKnot.GBResidueSpectralSum.gradedTrace",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:graded-markov-trace-from-gs-filtration",
    "def:confinement-level",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/markov_pipeline_cross_validator.py",
    witness:
      "folio-assistant/computations/markov-pipeline-cross-validation.witness.json",
    status: "verified",
  },
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "graded-trace",
    "markov-trace",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
