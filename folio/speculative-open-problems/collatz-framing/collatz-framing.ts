import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "Collatz Problem Framing",
  label: "chap:collatz-framing",
  sections: [
    section({
      title: "Domain-stable Laurent lifts, withdrawn contact thresholds, and open problems",
      label: "sec:collatz-framing",
      blocks: [
        "collatz-section-intro",
        "q-collatz-conjecture",
        "collatz-contact-boundary-defn",
        "collatz-contact-boundary",
        "collatz-parity-to-divisor",
        "collatz-three-forms",
        "q-collatz-interpretation",
        "collatz-surreal-bound",
        "collatz-hausdorff-comparison",
        "collatz-hausdorff-comparison-table-data",
        "collatz-open-problems",
      ],
    }),
  ],
});
