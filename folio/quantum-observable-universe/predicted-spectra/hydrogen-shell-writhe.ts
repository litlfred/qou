import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hydrogen-shell-writhe",
  title:
    "Electron shell number equals writhe level of the trefoil embedding",
  tags: ["hydrogen", "shell", "writhe", "trefoil", "reidemeister", "orbital"],
  lean: { ref: "qou:QOU.BringsSurface.hydrogen_shell_writhe",
    validation: "not_checked",
  },
  uses: ["def:electron-knot"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "Conflicts with the owner ruling of 2026-11-21 on [the electron](#def:electron-knot), which makes the electron the word $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ with closure the Hopf link. This conjecture is built on the electron being the trefoil $T_{2,3}$: the ground state $w = 3$ is the writhe of a minimal trefoil diagram, while a minimal Hopf-link diagram has writhe $\\pm 2$, which gives $n = (w-1)/2 = 1/2$. Left unchanged for an owner decision rather than relabelled (audit: `docs/audits/2026-11-21-electron-word-options-downstream.md`).",
    },
  ],
});
