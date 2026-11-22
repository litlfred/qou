import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-dualizing-complex",
  title: "Rigid dualizing complex",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.RigidDualizingComplex",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  cites: ["yekutieli-zhang1999-auslander-dualizing",
    "yekutieli2010",
  ],
  tags: ["dualizing-complex", "derived-category", "yekutieli", "self-duality"],
});
