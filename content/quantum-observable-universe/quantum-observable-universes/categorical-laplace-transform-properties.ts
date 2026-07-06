import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-laplace-transform-properties",
  interprets: "def:categorical-laplace",
  title: "Base-ring independence of the categorical Laplace transform",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "laplace"],
  uses: [
    "def:categorical-laplace",
  ],
});
