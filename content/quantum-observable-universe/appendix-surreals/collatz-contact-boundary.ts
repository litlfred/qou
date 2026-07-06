import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-contact-boundary",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.collatz_contact_boundary", validation: "not_checked" },
  title:
    "The $[2]_q$-contact boundary on the Reeb bundle",
  uses: [
    "def:two-q-adic-valuation",
    "def:collatz-contact-boundary",
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
