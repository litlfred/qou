import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hydrogen-shell-writhe",
  label: "rem:hydrogen-orbitals",
  title:
    "Hydrogen orbitals: the spinning trefoil around the Borromean anchor",
  tags: [
    "hydrogen",
    "orbital",
    "shell",
    "subshell",
    "trefoil",
    "writhe",
    "borromean",
    "electron-cloud",
  ],
  uses: [
    "ex:hydrogen-knot-structure",
    "conj:hydrogen-shell-writhe",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , and it is proved as `mode_cutoff_iff` in the Lean sibling of that conjecture, with no symmetry group entering the argument." },
  ],
});
