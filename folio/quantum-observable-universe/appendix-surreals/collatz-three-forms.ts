import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-three-forms",
  title: "Three faces of the $q$-Collatz conjecture",
  interprets: "conj:collatz-contact-boundary",
  uses: ["conj:collatz-contact-boundary"],
  tags: [
    "collatz",
    "hecke-algebra",
    "markov-trace",
    "gaussian-integers",
    "contact-order",
    "saturation",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-28", body: "Labelled heuristic. Corrected 'classical Collatz has no margin / gap collapses at q=1': the gap is q=1 at q=1 and the classical heuristic factor is 3/4. The braid form is a conjecture in words." },
  ],
});
