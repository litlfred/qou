import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brane-boundary",
  lean: { ref: "qou:QOU.Torsion.brane_boundary_structure",
    validation: "not_checked",
  },
  title: "Structure of the defining boundary",
  tags: ["brane-boundary", "codimension", "blow-up", "chirality"],
  uses: [
    "def:brane-boundary",
    "def:descent-involution",
    "def:quantum-characteristic-classes",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Descartes chirality](#rem:archimedean-chirality))" },
  ],
  proofs: ["prf:brane-boundary"],
});
