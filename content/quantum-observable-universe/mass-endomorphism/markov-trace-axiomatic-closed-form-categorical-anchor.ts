import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-axiomatic-closed-form",
  label: "rem:markov-trace-axiomatic-closed-form-categorical-anchor",
  title: "The proton categorical-mass anchor and the Plancherel-trace contrast",
  tags: [
    "categorical-mass-anchor",
    "proton",
    "markov-trace",
    "plancherel-contrast",
  ],
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
    "prop:categorical-mass-markov",
    "prop:atomic-mass-gb-nf",
    "prop:markov-trace-antipode-polynomial-symmetry",
    "prop:mass-coefficient-shadow-price",
  ],
  cites: ["jones1987", "kassel1995", "wenzl1988"],
});
