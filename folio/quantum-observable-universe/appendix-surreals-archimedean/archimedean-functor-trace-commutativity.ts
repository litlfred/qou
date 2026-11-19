import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-functor-trace-commutativity",
  title: "Archimedean realisation and binding-trace commutativity",
  tags: [
    "surreal-numbers",
    "standard-part",
    "archimedean",
    "binding-energy",
    "markov-trace",
    "q-clt",
  ],
  interprets: "def:standard-part-functor",
  uses: ["def:standard-part-functor"],
  authorNotes: [
    {
      kind: "note",
      body: "Side-by-side numerical comparison spanning $^2\\mathrm{H}$ through $^7\\mathrm{Li}$ is recorded in `computations/binding-single-pipeline-comparison.witness.json`.",
    },
  ],
});
