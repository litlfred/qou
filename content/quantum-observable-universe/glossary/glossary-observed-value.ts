import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-observed-value",
  lean: { decl: "QOU.ObservedValue", validation: "not_checked" },
  title: "Observed spacetime value",
  tags: ["glossary", "brings-surface", "color-tube"],
  uses: ["def:color-tube-fibers", "rem:brings-smoothness"],});
