import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-axiomatic-closed-form",
  label: "rem:markov-trace-axiomatic-closed-form-interpretation",
  title:
    "Methodology generalisation and the categorical-mass anchor interpretation",
  tags: [
    "markov-trace",
    "axiomatic-reduction",
    "categorical-mass-anchor",
    "proton",
  ],
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
    "prop:categorical-mass-markov",
    "prop:atomic-mass-gb-nf",
    "prop:markov-trace-antipode-polynomial-symmetry",
    "prop:mass-coefficient-shadow-price",
    "def:markov-axiom-recursive-ascent",
  ],
  cites: ["jones1987", "kassel1995", "wenzl1988"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , [Mass-formula coefficients as shadow prices of the Frobenius positivity constraints](#prop:mass-coefficient-shadow-price)" },
  ],
});
