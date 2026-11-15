import { definition } from "../../schema/builders";

/**
 * Covalent bond as a shared electron trefoil Hopf-linked
 * across two nuclei.
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:covalent-bond-shared-trefoil",
  title: "Covalent bond as shared electron trefoil",
  lean: { ref: "qou:QOU.Molecular.CovalentBond",
    validation: "not_checked",
  },
  uses: ["def:molecular-braid"],
  tags: [
    "covalent-bond",
    "trefoil",
    "hopf-link",
    "electron-sharing",
  ],
});
