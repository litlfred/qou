import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:jones-markov-trace-formalization-note",
  title:
    "Formalization strategy for the Markov trace: axiomatic encoding of the three Jones properties",
  tags: [
    "markov-trace",
    "jones-polynomial",
    "formalization-note",
    "external-proof",
  ],
  uses: ["thm:jones-markov-trace"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Our formalization takes the result as axiomatic, encoding its core properties as a Lean structure over the $R_q = \\mathbb{Z}[q, q^{-1}]$ ground ring. Downstream theorems, such as completeness on irreducibles, are formally verified against these structure fields." },
  ],
});
