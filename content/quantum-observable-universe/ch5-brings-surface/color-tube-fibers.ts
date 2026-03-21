import { definition } from "../../schema/builders";

export default definition({
  label: "def:color-tube-fibers",
  title: "Color tube fibers",
  tags: ["brings-surface", "color-tube"],
  uses: ["rem:color-tube-cubic", "rem:lagrange-resolvents", "prop:chiral-elliptic"],
});
