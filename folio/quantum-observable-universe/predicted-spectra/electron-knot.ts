import { definition } from "../../schema/builders";

export default definition({
  label: "def:electron-knot",
  title: "Electron",
  tags: ["electron", "lepton", "hopf-link", "braid-word", "fermion"],
  lean: { ref: "qou:QOU.Archimedean.Electron",
    validation: "not_checked",
  },
  uses: ["def:up-quark", "rem:knot-particle-dictionary"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body: "Owner ruling 2026-11-21 (verbatim): *\"I think it is hopf link so take. That as ruling for now, but keep trefoil as backup in case need to recisit\"*. The electron is the word $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$, whose closure is the Hopf link; this block previously identified it with the trefoil $T_{2,3}$. The trefoil braid $\\sigma_0^3 \\in B_2$ is kept as the documented backup. Side-by-side consequences and revisit conditions: `docs/audits/2026-11-21-electron-word-options-downstream.md`.",
    },
  ],
});
