import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-parity-to-divisor",
  title:
    "From integer parity to the $[2]_q$-divisor",
  interprets: "conj:collatz-contact-boundary",
  uses: [
    "def:two-q-adic-valuation",
    "conj:q-collatz",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "collatz",
    "parity",
    "divisor",
    "kummer",
    "contact-order",
  ],
});
