import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-laplace",
  title: "Categorical Laplace transform",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "laplace"],
  lean: { ref: "qou:QOU.CategoricalLaplace",
    validation: "not_checked",
  },
  uses: [
    "rem:adjoint-trace",
    "def:q-heat-equation",
  ],
});
