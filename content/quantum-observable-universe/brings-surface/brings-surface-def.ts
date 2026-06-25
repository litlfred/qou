import { definition } from "../../schema/builders";

export default definition({
  label: "def:brings-surface",
  lean: { ref: "qou:QOU.BringsSurface", validation: "not_checked" },
  title: "Bring's surface",
  tags: ["algebraic-geometry", "brings-surface"],
  uses: [],
  examples: ["rem:braid-group-action", "rem:color-tube-interpretation", "rem:color-tube-cubic", "rem:color-bundles", "rem:brings-smoothness"],
});
