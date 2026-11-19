import { proof } from "../../schema/builders";

export default proof({
  label: "prf:wedderburn-bratteli-recursion",
  title: "Proof of wedderburn bratteli recursion",
  uses: ["prop:wedderburn-bratteli-recursion"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/y-lambda-jones-markov-witness.json, y-lambda-symbolic-witness.json.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/plancherel_weight_boundedness_probe.py",
    witness: "computations/probes/plancherel-weight-boundedness-probe.witness.json",
    status: "verified",
  },
});
