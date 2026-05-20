import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-dualizing-complex",
  title: "Rigid dualizing complex",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.RigidDualizingComplex",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  cites: ["yekutieli2015",
    "yekutieli2010",
  ],
  tags: ["dualizing-complex", "derived-category", "yekutieli", "self-duality"],
});
