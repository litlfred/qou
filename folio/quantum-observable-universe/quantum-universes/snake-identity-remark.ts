import { remark } from "../../schema/builders";

export default remark({
  label: "rem:snake-identity-remark",
  title: "The snake identities in the graphical calculus",
  interprets: "def:snake-identity",
  uses: ["def:snake-identity"],
  tags: ["category-theory", "monoidal", "duality"],
});
