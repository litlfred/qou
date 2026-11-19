import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-left-dual",
  title: "Left dual",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-exact-pairing"],
  defines: ["left-dual"],
});
