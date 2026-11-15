import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-product",
  title: "Proof of markov trace product",
  uses: ["thm:markov-trace-product"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-10-10",
      body: "The figures 0.1245 and 0.5514 were quoted here as the main values until 2026-10-10; they are the excised convention-C values. Earlier versions also had the two values swapped.",
    },
  ],
});
