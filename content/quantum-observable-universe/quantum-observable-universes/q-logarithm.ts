import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-logarithm",
  title: "$q$-Logarithm (categorical adjoint)",
  tags: ["hopf-algebra", "primitive", "q-logarithm", "adjoint"],
  lean: { ref: "qou:QOU.QLogarithm",
    validation: "not_checked",
  },
  uses: ["def:q-exponential"],
});
