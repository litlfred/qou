import { definition } from "../../schema/builders";

export default definition({
  label: "def:color-tube-fibers",
  title: "Color tube fibers",
  tags: ["brings-surface", "color-tube"],
  uses: [
    "rem:color-tube-cubic",
    "prop:chiral-elliptic",
    "rem:lagrange-resolvents",
  ],
});
