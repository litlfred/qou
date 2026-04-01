import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:bundle-initial-conditions",
  label: "rem:bundle-category",
  title: "The category of finite bundles over $\\mathbb{P}(V)$",
  tags: ["bundle", "category", "knot", "categorical"],
  uses: ["def:torsion-knot-flow"],
});
