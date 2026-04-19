import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-contact-boundary",
  lean: {
    decl: "QOU.AlgebraicSubstrate.collatz_contact_boundary",
    validation: "not_checked",
  },
  title:
    "The $[2]_q$-contact boundary on the Reeb bundle",
  uses: [
    "conj:q-collatz",
    "def:reeb-bundle",
    "rem:substrate-gm-torsion",
    "prop:root-of-unity-truncation",
    "prop:skein-generation",
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
