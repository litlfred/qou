import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:collatz-contact-boundary",
  title: "Withdrawn contact-threshold reformulation of $q$-Collatz",
  lean: {
    ref: "qou:QOU.BringsSurface.collatz_contact_boundary",
    validation: "stub",
  },
  uses: [
    "conj:q-collatz",
    "def:collatz-contact-boundary",
    "quantum-observable-universe:def:two-q-adic-valuation",
    "quantum-observable-universe:def:reeb-bundle",
  ],
  tags: ["collatz", "contact-boundary", "withdrawn"],
});
