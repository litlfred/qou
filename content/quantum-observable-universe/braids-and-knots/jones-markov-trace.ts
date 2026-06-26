import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:jones-markov-trace",
  lean: { ref: "qou:QOU.Braiding.JonesMarkovTrace",
    validation: "not_checked",
  },
  title: "Existence and non-degeneracy of the Markov trace (Jones, 1987)",
  tags: ["hecke-algebra", "markov-trace", "jones-polynomial", "external-proof"],
  uses: ["prop:braid-action-tensor", "prop:braiding-eigenvalue-extraction"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-26",
      body: "Standard result (Jones, 1987); no new mathematical argument is claimed. The contribution is the formalization: the three trace properties and the $R_q = \\mathbb{Z}[q, q^{-1}]$ ground-ring framing are encoded as Lean structure fields to support downstream machine-checked proofs.",
    },
  ],
});
