import { simulator } from "../../schema/builders";

export default simulator({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. Electron relabelled; the HTML still draws the backup trefoil, and the prose says so." },
  ],
  label: "sim:knot-atom-diagrams",
  title: "Knot Diagrams of Light Atoms ($Z \\leq 4$)",
  html: "simulators/knot_atom_diagrams.html",
  uses: ["rem:knot-atom-diagrams"],
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "sub-link",
    "atom",
    "interactive",
    "borromean",
  ],
  defaultView: {
    name: "default",
    title: "Light atom knot diagrams (H, He, Li, Be)",
    params: {
      display: "all",
    },
  },
});
