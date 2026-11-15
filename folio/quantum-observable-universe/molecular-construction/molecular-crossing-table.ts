import { remark } from "../../schema/builders";

/**
 * Inter-atomic crossing coefficients: how strands from different
 * atoms interact in the molecular Hecke algebra.
 */
export default remark({
  label: "rem:molecular-crossing-table",
  title: "Inter-atomic crossing coefficients",
  interprets: "def:molecular-braid",
  uses: ["def:atomic-braid"],
  tags: ["molecular", "crossing-coefficients", "electromagnetic"],
});
