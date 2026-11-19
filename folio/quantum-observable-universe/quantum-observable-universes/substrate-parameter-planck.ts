import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter-planck",
  title: "Aether parameter and quantum Planck constant",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.SubstrateParameterPlanck",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  tags: ["substrate-parameter", "planck-constant", "q-deformation"],
});
