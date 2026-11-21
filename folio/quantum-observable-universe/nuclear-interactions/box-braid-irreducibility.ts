import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:box-braid-irreducibility",
  title:
    "The $\\gamma\\gamma \\to \\nu\\nu^{\\sigma}$ box braid is irreducible",
  tags: [
    "neutrino",
    "stability",
    "box-diagram",
    "groebner-basis",
    "irreducibility",
    "skein-relation",
    "weak-force",
    "photon",
    "virtual-particles",
  ],
  lean: { ref: "qou:QOU.Archimedean.BoxBraidIrreducibility",
    validation: "not_checked",
  },
  // rem:electron-immortality dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [
    "rem:virtual-particles-exceptional-divisor",
    "ex:photon-wavefront"
  ],
});
