import { proof } from "../../schema/builders";

export default proof({
  label: "prf:borromean-markov-trace-closed-form",
  title: "Proof of borromean markov trace closed form",
  uses: ["prop:borromean-markov-trace-closed-form"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: y-lambda-wenzl-bridge-symbolic-witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/borromean_trace_cross_validator.py",
    witness: "computations/probes/borromean-trace-cross-validation.witness.json",
    status: "verified",
  },
});
