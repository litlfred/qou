import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:rigid-monoidal-category",
  label: "rem:monoidal-justification",
  title: "Rationale for monoidal categories",
  uses: ["def:snake-identity"],
  tags: ["category-theory", "monoidal", "motivation"],
  cites: ["coecke2017", "haag1996"],
});
