import { prose } from "../../schema/builders";

export default prose({
  label: "prose:knot-periodic-table",
  title: "Knot-periodic table of the elements",
  uses: [
    // The classification the whole table is organised by.
    // def:borromean-baryon, the trefoil-link identification the summary
    // asserts for p and n, is NOT listed: it is reached through this cone.
    "prop:fermion-boson-knot-link",
    "prop:shell-structure-eigenvalues",
    "thm:generation-completeness",
    "rem:knot-exhaustiveness",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. Electron relabelled in the atom formula and the knot-particle identification. Not changed: the proton/neutron quarks as Borromean-linked trefoils, which clashes with the unknot-strand up quark (owner ruling 2026-11-20); flagged on #8822." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Per-element table.** The full $Z = 1$ to $92$ grid lives as the *Per-element stability summary* section of the [recursive atom-knot atlas](#prop:recursive-atom-knot-atlas), which also carries the per-isotope coverage table for all 3558 nuclides in AME 2020 (Z = 0 to 118)." },
  ],
  tags: [
    "knot",
    "periodic-table",
    "mass",
    "generation",
    "torus-knot",
    "proton",
    "neutron",
    "transfer-matrix",
    "skein-polynomial",
    "appendix",
    "fermion",
    "boson",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
