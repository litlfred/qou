import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-shells-hopf",
  interprets: "prop:torus-hopf-stability",
  title:
    "Electron shells as closed sub-Hopf links of the electron chain",
  lean: {
    ref: "qou:QOU.ElectronShellsHopf.ElectronShellsHopf",
    validation: "not_checked",
  },
  tags: [
    "electron",
    "shell",
    "hopf-link",
    "sub-link",
    "photon",
    "orbital",
    "braid-word",
    "absorption",
  ],
  uses: [
    "prop:torus-hopf-stability",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner choice 2026-11-21, 'rebuild the rest on sigma_0 sigma_1 sigma_0'; issue #8822): rebuilt on the electron word sigma_0 sigma_1 sigma_0 in B_3, whose closure is the Hopf link. Photon absorption is the strand-adding curl (Markov stabilisation), so the level is n = w - 2 (QOU.BraidKnot.ElectronLevelWord). Where a statement was built on the trefoil's own geometry it is now stated as not re-derived; the trefoil is kept as the backup reading." },
  ],
});
