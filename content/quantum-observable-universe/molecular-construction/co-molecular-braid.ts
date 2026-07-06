import { definition } from "../../schema/builders";

/**
 * CO molecular braid: heteronuclear triple bond.
 * C(6,6) + O(8,8) with 3 shared electron pairs.
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:co-molecular-braid",
  title: "Carbon monoxide $CO$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.COBraid",
    validation: "not_checked",
  },
  uses: ["def:covalent-bond-shared-trefoil"],
  tags: [
    "carbon-monoxide",
    "CO",
    "triple-bond",
    "heteronuclear",
    "molecular-braid",
  ],
});
