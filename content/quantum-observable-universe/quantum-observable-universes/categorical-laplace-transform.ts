import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-laplace",
  title: "Categorical Laplace transform",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "laplace"],
  lean: {
    decl: "QOU.CategoricalLaplace",
    validation: "not_checked",
  },
  uses: [
    "def:adjoint-trace",
    "def:q-harmonic-form",
    "rem:base-field-independence",
  ],
});
