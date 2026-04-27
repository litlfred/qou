import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-contact-boundary",
  title:
    "The $[2]_q$-contact boundary on the Reeb bundle",
  uses: [
    "conj:q-collatz",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "collatz",
    "contact-order",
    "adic-valuation",
    "reeb-bundle",
    "kummer",
    "boundary",
    "divisor",
    "hopf-fibration",
  ],
});
