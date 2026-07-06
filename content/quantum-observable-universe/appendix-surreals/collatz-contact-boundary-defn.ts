import { definition } from "../../schema/builders";

export default definition({
  label: "def:collatz-contact-boundary",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.CollatzContactBoundary",
    validation: "not_checked",
  },
  title:
    "Collatz contact boundary and orbit contact average",
  uses: [
    "def:two-q-adic-valuation",
    "conj:q-collatz",
  ],
  tags: [
    "collatz",
    "contact-order",
    "boundary",
    "skein-module",
    "orbit-average",
  ],
});
