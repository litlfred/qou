import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-dual-h3",
  title: "Frobenius dual $K^\\vee$ in $H_3(q)$",
  lean: {
    ref: "qou:QOU.Archimedean.frobeniusDual",
    validation: "not_checked",
  },
  uses: ["prop:frobenius-gram-matrix"],
  cites: ["kassel1995"],
  tags: [
    "frobenius-dual",
    "gram-matrix",
    "hecke-algebra",
    "markov-trace",
    "non-degenerate",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): — [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean))" },
  ],
});
