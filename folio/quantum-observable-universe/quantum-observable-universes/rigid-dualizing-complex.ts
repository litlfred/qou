import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-dualizing-complex",
  title: "Rigid dualizing complex",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.RigidDualizingComplex",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  cites: ["yekutieli-zhang1999-auslander-dualizing",
    "yekutieli2010",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-23",
      body:
        "Item 2 previously gave the rigidifying isomorphism as $\\omega_A \\simeq R\\mathrm{Hom}_{A^e}(A, A^e)$. " +
        "That complex is the inverse dualizing complex; rigidity is " +
        "$\\omega_A \\simeq R\\mathrm{Hom}_{A^e}(A, \\omega_A \\otimes \\omega_A)$ (Van den Bergh 1997; " +
        "Yekutieli–Zhang 1999). Corrected (issue #9179). Item 3 is unchanged.",
    },
  ],
  tags: ["dualizing-complex", "derived-category", "yekutieli", "self-duality"],
});
