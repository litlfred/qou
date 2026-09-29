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
});
