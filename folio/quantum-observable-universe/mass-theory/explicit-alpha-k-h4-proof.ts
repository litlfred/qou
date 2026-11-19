import { proof } from "../../schema/builders";

export default proof({
  label: "prf:explicit-alpha-k-h4",
  title: "Proof of explicit alpha k h4",
  uses: ["prop:explicit-alpha-k-h4"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/wedderburn-orthogonal-r-3-h4.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/explicit_central_idempotent_probe.py",
    witness: [
      "computations/probes/explicit-central-idempotent-probe.witness.json",
      "computations/alpha/alpha-k-jones-markov-h4.witness.json",
    ],
    status: "verified",
  },
});
