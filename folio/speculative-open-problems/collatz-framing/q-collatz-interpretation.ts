import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-collatz-interpretation",
  title: "Cyclotomic polynomial ratios $[2]_q^k / [p]_q$ versus orbit dynamics",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "conj:collatz-contact-boundary",
    "quantum-observable-universe:prop:q-syracuse-lift",
  ],
  cites: ["collatz1937", "lagarias2010"],
  tags: ["collatz", "q-integer", "polynomials"],
});
