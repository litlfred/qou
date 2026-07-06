import { proposition } from "../../schema/builders";

/**
 * LP dual binding optimization for H₂.
 */
export default proposition({
  label: "prop:h2-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.h2_lp_dual_binding", validation: "not_checked" },
  title: "LP dual gives optimal $H_2$ binding",
  uses: [
    "def:h2-molecular-braid",
    "prop:shell-filling-rule",
  ],
  tags: ["H2", "LP-dual", "binding", "optimal"],
  computation: {
    engine: "python",
    script: "computations/h2-integer-lp.py",
    witness: [
      "computations/h2-integer-lp.witness.json",
      "computations/h2-molecular-binding.witness.json",
    ],
    status: "verified",
  },
});
