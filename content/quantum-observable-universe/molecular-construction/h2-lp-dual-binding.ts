import { proposition } from "../../schema/builders";

/**
 * LP dual binding optimization for H₂.
 */
export default proposition({
  label: "prop:h2-lp-dual-binding",
  lean: {
    decl: "QOU.MolecularConstruction.h2_lp_dual_binding",
    validation: "not_checked",
  },
  title: "LP dual gives optimal $H_2$ binding",
  uses: [
    "def:h2-molecular-braid",
    "def:covalent-bond-shared-trefoil",
    "prop:shell-filling-rule",
  ],
  tags: ["H2", "LP-dual", "binding", "optimal"],
});
