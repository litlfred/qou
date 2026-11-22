import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. Electron relabelled in the legend and the Z <= 4 table; the figures in simulators/knot_atom_diagrams.html still draw the backup trefoil, and the legend says so. Not changed: the proton drawn as a left trefoil (flagged on #8822)." },
  ],
  interprets: "def:stable-nucleus",
  label: "rem:knot-atom-diagrams",
  title:
    "Knot diagrams of light atoms ($Z \\leq 4$)",
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "sub-link",
    "atom",
    "transfer-matrix",
    "antineutrino",
    "borromean",
  ],
  uses: ["prop:shell-structure-eigenvalues"],
});
