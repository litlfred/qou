import { proposition } from "../../schema/builders";

/**
 * LP dual binding optimization for H₂.
 */
export default proposition({
  label: "prop:h2-lp-dual-binding",
  title: "LP dual gives optimal $H_2$ binding",
  uses: [
    "def:h2-molecular-braid",
    "prop:shell-filling-rule",
  ],
  tags: ["H2", "LP-dual", "binding", "optimal"],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/h2-integer-lp.py",
    witness: [
      "folio-assistant/computations/h2-integer-lp.witness.json",
      "folio-assistant/computations/h2-molecular-binding.witness.json",
    ],
    status: "verified",
  },
});
