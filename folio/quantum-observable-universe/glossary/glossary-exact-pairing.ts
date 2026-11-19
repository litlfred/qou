import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-exact-pairing",
  title: "Exact pairing",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-monoidal-category", "def:snake-identity"],
});
