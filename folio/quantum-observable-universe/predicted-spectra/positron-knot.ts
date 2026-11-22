import { definition } from "../../schema/builders";

export default definition({
  label: "def:positron-knot",
  title: "Positron",
  tags: ["positron", "antiparticle", "hopf-link", "braid-word", "lepton"],
  lean: { ref: "qou:QOU.Archimedean.Positron",
    validation: "not_checked",
  },
  uses: ["rem:chirality-trefoil-electron-positron"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body: "Follows the owner ruling of 2026-11-21 on the electron (`def:electron-knot`): the positron is the conjugate word $\\sigma_0^{-1}\\sigma_1^{-1}\\sigma_0^{-1}$ (closure: the negative Hopf link). This block previously identified it with the mirror trefoil $T_{2,3}^{\\sigma}$. The interpreting remark `rem:chirality-trefoil-electron-positron` still argues from trefoil chirality and is listed for the owner.",
    },
  ],
});
