import { definition } from "../../schema/builders";

/**
 * Electron shell structure as braid bonding capacity.
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:electron-shell-braid-capacity",
  title: "Electron shell as braid bonding capacity",
  lean: { ref: "qou:QOU.Molecular.ElectronShell",
    validation: "not_checked",
  },
  uses: ["def:atomic-braid"],
  tags: [
    "bonding-capacity",
    "valence",
    "hopf-link",
  ],
});
