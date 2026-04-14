import { remark } from "../../schema/builders";

/**
 * H₂ bond length interpretation from the braid framework.
 */
export default remark({
  label: "rem:h2-bond-length-interpretation",
  title: "$H_2$ bond length from covalent channel eigenvalue ratio",
  interprets: "def:h2-molecular-braid",
  uses: ["prop:h2-lp-dual-binding"],
  tags: ["H2", "bond-length", "eigenvalue-ratio", "interpretation"],
});
