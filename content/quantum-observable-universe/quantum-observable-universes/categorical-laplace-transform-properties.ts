import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-laplace-transform-properties",
  interprets: "def:categorical-laplace",
  title: "Realisations of the categorical Laplace transform: base ring, three contexts, and the $q$-heat resolvent",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "laplace"],
  uses: [
    "def:categorical-laplace",
    "rem:q-exp-finite-field-obstruction",
    "rem:q-exp-p-adic",
    "def:q-heat-equation",
    "def:q-resolvent",
  ],
});
