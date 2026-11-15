import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:crossed-module-euler-characteristic",
  label: "rem:geom-bridge-status",
  title: "Logical status of the algebraic → geometric → boundary chain",
  tags: ["geom", "non-abelian-stokes", "open-problem", "bring-surface"],
  uses: [
    "prop:crossed-module-euler-characteristic",
    "conj:geom-universality",
  ],
});
