import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:alpha-cosh-h-z-step-correction",
  title:
    "Per-Z step factor in the Δ_λ closure equals [3]_q² · cosh(h) at q_0",
  lean: {
    ref: "qou:QOU.BraidKnot.AlphaCoshHZStepCorrection",
    validation: "not_checked",
  },
  uses: [
    "prop:interface-knot-markov-z",
    "thm:jones-markov-trace",
    "prop:mass-tower-operator-valued",
  ],
  cites: ["wenzl1988", "jones1987"],
  computation: {
    engine: "python",
    script:
      "computations/delta_lambda_z4N_phase4.py",
    witness:
      "computations/delta-lambda-z4N-phase4.witness.json",
    status: "verified",
  },
  tags: [
    "delta-lambda",
    "categorical-closure",
    "bar-symmetric",
    "hecke-skein",
    "z-step",
    "cosh-h",
    "research-conjectural",
  ],
});
