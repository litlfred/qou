import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-energy-categorical-origin",
  title: "Crossing weights are Hecke eigenvalues, not postulates",
  interprets: "def:crossing-energy",
  uses: [
    "def:crossing-energy",
    "def:quantum-observable-universe",
    "prop:braiding-eigenvalue-extraction",
    "prop:nuclear-groebner-reduction",
    "rem:r-matrix-braiding",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([nuclear normal form](#prop:nuclear-groebner-reduction))" },
  ],
  tags: ["crossing", "energy", "hecke", "eigenvalue", "r-matrix"],
});
