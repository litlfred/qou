import { remark } from "../../schema/builders";

/**
 * H₂ binding energy: comparison with observed value.
 */
export default remark({
  label: "rem:h2-binding-energy",
  title: "$H_2$ binding energy from the LP dual",
  interprets: "prop:h2-lp-dual-binding",
  uses: ["def:h2-molecular-braid"],
  tags: ["H2", "binding-energy", "prediction", "comparison"],
});
