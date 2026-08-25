import { remark } from "../../schema/builders";

/**
 * Step-by-step LP stability verification for each atom.
 */
export default remark({
  label: "rem:step-lp-verification",
  title: "Step-by-step LP stability verification",
  interprets: "prop:atomic-lp-stability",
});
