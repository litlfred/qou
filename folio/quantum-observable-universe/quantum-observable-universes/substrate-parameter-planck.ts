import { definition } from "../../schema/builders";

export default definition({
  label: "def:aether-parameter-planck",
  renamedFrom: ["def:substrate-parameter-planck"],
  title: "Aether parameter and quantum Planck constant",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.SubstrateParameterPlanck",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-aether"],
  tags: ["substrate-parameter", "planck-constant", "q-deformation"],
});
