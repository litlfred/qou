import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-graded-markov-trace-existence",
  title:
    "Existence of the graded Markov trace on the GS filtration (categorical existence)",
  lean: {
    ref: "qou:QOU.IwahoriHecke.MarkovTrace.GradedMarkovTraceExistence",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:graded-markov-trace-from-gs-filtration",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script: "computations/markov/markov_pipeline_cross_validator.py",
    witness:
      "computations/markov/markov-pipeline-cross-validation.witness.json",
    status: "verified",
  },
  tags: [
    "tier:keystone",
    "gs-filtration",
    "spectral-sequence",
    "graded-trace",
    "markov-trace",
    "noncomputable-opaque",
    "closure-tier-b",
    "phase-2-sprint-4-discharge",
  ],
});
