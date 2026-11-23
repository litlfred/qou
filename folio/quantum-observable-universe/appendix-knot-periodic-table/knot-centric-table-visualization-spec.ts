import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. The electron panel now specifies the derived level word e_n and its closure instead of standing waves on a trefoil; the notation list no longer ties fermions to trefoil glyphs." },
  ],
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table-visualization-spec",
  title:
    "Interactive visualization specification for the knot-centric periodic table",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "simulator",
    "appendix",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "rem:knot-atom-diagrams",
  ],
});
