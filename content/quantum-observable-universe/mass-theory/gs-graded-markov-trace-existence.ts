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
    "prop:graded-markov-trace-from-gs-filtration",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script: "computations/markov/markov_pipeline_cross_validator.py",
    witness:
      "computations/markov/markov-pipeline-cross-validation.witness.json",
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (tr_M_at_q0_archimedean[n (neutron). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
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
