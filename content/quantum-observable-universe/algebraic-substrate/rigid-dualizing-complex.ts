import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-dualizing-complex",
  title: "Rigid dualizing complex",
  lean: {
    decl: "QOU.AlgebraicSubstrate.RigidDualizingComplex",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  cites: ["yekutieli2015"],
  tags: ["dualizing-complex", "derived-category", "yekutieli", "self-duality"],
});
