import { definition } from "../../schema/builders";

export default definition({
  label: "def:two-q-adic-valuation",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoQAdicValuation",
    validation: "not_checked",
  },
  title:
    "The $[2]_q$-adic valuation on the Skein module",
  uses: [
    // conj:q-collatz removed (qou-tm3c): the definition is the (q+1)-adic valuation of a polynomial; it does not use the Collatz map.
  ],
  tags: [
    "collatz",
    "contact-order",
    "adic-valuation",
    "skein-module",
    "divisor",
  ],
});
