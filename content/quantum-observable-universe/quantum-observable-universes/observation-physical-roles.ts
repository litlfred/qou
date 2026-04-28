import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-physical-roles",
  title: "Physical roles of the observation components",
  tags: ["observation", "interpretation", "jet", "adjoint"],
  uses: ["def:observation"],
});
