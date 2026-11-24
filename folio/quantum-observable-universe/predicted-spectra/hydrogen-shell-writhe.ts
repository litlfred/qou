import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hydrogen-shell-writhe",
  title:
    "Electron shell number from the writhe of the level word",
  tags: ["hydrogen", "shell", "writhe", "braid-word", "markov-stabilisation", "orbital"],
  lean: { ref: "qou:QOU.BringsSurface.BringsSurfaceRoot.hydrogen_shell_writhe_ruled",
    validation: "not_checked",
  },
  uses: ["def:electron-knot", "conj:orbital-space-normal-bundle"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-borromean-quark-carriers-trivial.lean` (`T9`) inhabits the local `BorromeanQuark` carrier with `bareMass := 1`.",
      see: "docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean",
    },
    {
      kind: "note",
      date: "2026-11-21",
      body: "Rebuilt on the ruled electron $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ (owner choice 2026-11-21, 'rebuild the rest on sigma_0 sigma_1 sigma_0'; issue #8822). Excitation is the strand-adding curl of docs/audits/2026-11-21-photon-excitation-gs-reduction.md section 4a, giving $n = w - 2$, proved in `QOU.BraidKnot.ElectronLevelWord`. The orbital count and the $1/n^2$ scaling are stated as not re-derived. The trefoil reading $n = (w-1)/2$ is kept as backup.",
    },
  ],
});
