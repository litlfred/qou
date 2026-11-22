import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hydrogen-shell-writhe",
  label: "rem:hydrogen-orbitals",
  title:
    "Hydrogen orbitals: the electron word around the Borromean anchor",
  tags: [
    "hydrogen",
    "orbital",
    "shell",
    "subshell",
    "braid-word",
    "writhe",
    "borromean",
    "electron-cloud",
  ],
  uses: [
    "ex:hydrogen-knot-structure",
    "conj:hydrogen-shell-writhe",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner choice 2026-11-21, 'rebuild the rest on sigma_0 sigma_1 sigma_0'; issue #8822): rebuilt on the electron word sigma_0 sigma_1 sigma_0 in B_3, whose closure is the Hopf link. Photon absorption is the strand-adding curl (Markov stabilisation), so the level is n = w - 2 (QOU.BraidKnot.ElectronLevelWord). Where a statement was built on the trefoil's own geometry it is now stated as not re-derived; the trefoil is kept as the backup reading." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , and it is proved as `mode_cutoff_iff` in the Lean sibling of that conjecture, with no symmetry group entering the argument." },
  ],
});
