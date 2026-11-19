import { proof } from "../../schema/builders";

export default proof({
  label: "prf:explicit-alpha-k-h3",
  title: "Proof of explicit alpha k h3",
  uses: ["prop:explicit-alpha-k-h3"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/alpha/alpha-k-jones-markov-h3.witness.json.",
    },
  ],
});
