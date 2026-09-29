import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-pivotal-category",
  title: "Pivotal category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-rigid-category"],
  defines: ["pivotal-category"],
});
