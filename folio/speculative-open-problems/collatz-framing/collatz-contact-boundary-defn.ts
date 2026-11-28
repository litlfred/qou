import { definition } from "../../schema/builders";

export default definition({
  label: "def:collatz-contact-boundary",
  title: "Orbit $[2]_q$-contact average and heuristic contact locus",
  lean: {
    ref: "qou:QOU.BringsSurface.collatz_contact_boundary",
    validation: "not_checked",
  },
  uses: [
    "conj:q-collatz",
    "quantum-observable-universe:def:two-q-adic-valuation",
  ],
  tags: ["collatz", "contact-boundary", "valuation", "orbit-average"],
});
