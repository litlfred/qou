import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-gram-star-positive",
  title:
    "The Markov--Gram star form is positive semidefinite; positivity reduces to $y_\\lambda \\ge 0$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.markov_star_nonneg",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-gram-matrix",
    "prop:h3-markov-wenzl-weights",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The contrast is drawn in\n[two pairings, two signatures](#rem:markov-gram-bilinear-vs-star), and n" },
  ],
  tags: [
    "markov-trace",
    "gram-matrix",
    "star-pairing",
    "hecke-algebra",
    "convention-d",
    "trace-convention",
  ],
});
