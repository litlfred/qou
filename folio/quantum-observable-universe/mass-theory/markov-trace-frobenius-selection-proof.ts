import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-frobenius-selection",
  title: "Proof of markov trace frobenius selection",
  uses: ["prop:markov-trace-frobenius-selection"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/markov-trace-weights-wenzl.witness.json.",
    },
  ],
});
