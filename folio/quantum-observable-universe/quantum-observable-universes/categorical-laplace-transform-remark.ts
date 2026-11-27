import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-laplace-remark",
  title: "The Laplace transform as a mate of the comultiplication",
  interprets: "def:categorical-laplace",
  uses: ["def:categorical-laplace"],
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "laplace"],
});
