import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. The trefoil resonance-mode and Fourier-mode wording is replaced by the derived level word e_n (hydrogen-shell-writhe, QOU.BraidKnot.ElectronLevelWord). Nothing derived Fourier modes for the ruled electron." },
  ],
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table",
  title:
    "Knot-centric periodic table: reorganization by nuclear and electronic knot structure",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "nuclear-shell",
    "borromean",
    "magic-receptive",
    "transfer-matrix",
    "skein-polynomial",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "thm:generation-completeness",
    "rem:knot-exhaustiveness",
  ],
});
