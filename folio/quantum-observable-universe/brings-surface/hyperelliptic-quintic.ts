import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): of [Bring's surface](#def:brings-surface)" },
  ],
  label: "def:hyperelliptic-quintic",
  // Was `qou:QOU.HyperellipticQuintic` — that names the *directory*
  // `QOU/HyperellipticQuintic/`, not a declaration, so it matched two files and
  // resolved to neither reliably. Pointed at the substantive module: both it and
  // the 94-line `ScratchZeta5.lean` declare `HyperellipticQuintic`/`zeta5`/
  // `Zeta5MonodromyContext` in the SAME namespace, but nothing imports Scratch
  // and this file is the fuller one (124 lines, incl. the monodromy content).
  lean: {
    ref: "qou:QOU.HyperellipticQuintic.zeta5_residue_monodromy.HyperellipticQuintic",
    validation: "not_checked",
  },
  title: "The hyperelliptic quintic $\\mathcal{X}_5 \\colon y^2 = x^5 - 1$",
  tags: ["hyperelliptic", "genus-2", "bolza", "roots-of-unity"],
  uses: ["prop:lagrange-resolvent-transform"],
  cites: [
    "bolza1887",
  ],
});
