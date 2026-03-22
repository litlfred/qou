import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bundle-category",
  title: "The category of finite bundles over $\\mathbb{P}(V)$",
  tags: ["bundle", "category", "knot", "categorical"],
  uses: [
    "def:bundle-initial-conditions",
    "def:torsion-knot-flow",
    "def:projective-line-object",
  ],
});
