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
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization provenance moved from prose: the arithmetic cutoff $\\lambda_\\ell \\le \\lambda_{n-1}$ ($\\ell \\le n - 1$) is proved as `mode_cutoff_iff` in the Lean sibling of `conj:orbital-space-normal-bundle`.",
    },
  ],
});
