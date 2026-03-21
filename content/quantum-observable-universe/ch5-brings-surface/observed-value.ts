import { definition } from "../../schema/builders";

export default definition({
  label: "def:observed-value",
  title: "Observed spacetime value",
  tags: ["brings-surface", "color-tube"],
  uses: [
    "def:color-tube-fibers",
    "rem:brings-smoothness",
  ],
});
