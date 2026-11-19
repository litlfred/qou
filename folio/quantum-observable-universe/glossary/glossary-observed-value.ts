import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-observed-value",
  title: "Observed spacetime value",
  tags: ["glossary", "brings-surface", "color-tube"],
  uses: ["def:color-tube-fibers", "rem:brings-smoothness"],
  defines: ["observed-value"],
});
