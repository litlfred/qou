import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ch4-lp-dual-binding",
  lean: {
    decl: "QOU.MolecularConstruction.ch4_lp_dual_binding",
    validation: "not_checked",
  },
  title: "$S_4$-symmetric strand ordering minimises $\\Phi_1$ for $CH_4$",
  uses: [
    "def:ch4-molecular-braid",
    "prop:h2-lp-dual-binding",
  ],
  tags: ["CH4", "LP-dual", "tetrahedral", "S4-symmetry"],
});
