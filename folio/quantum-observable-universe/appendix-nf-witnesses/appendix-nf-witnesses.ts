import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Normal Form Witnesses.
 *
 * Exact Pauli witnesses for light and medium nuclei,
 * computed via inductive Gröbner reduction in the Hecke algebra.
 */
export default chapter({
  title: "Normal Form Witnesses",
  label: "app:nf-witnesses",
  sections: [
    section({
      title: "Light nuclei ($A \\leq 12$)",
      label: "sec:nf-witnesses-light",
      blocks: [
        "witness-4he",
        "witness-4he-remark",
        "witness-8be",
        "witness-8be-remark",
        "witness-12c",
        "witness-12c-remark",
      ],
    }),
    section({
      title: "Medium nuclei ($A = 13$–$60$)",
      label: "sec:nf-witnesses-medium",
      blocks: [
        "witness-computation-method",
      ],
    }),
  ],
});
