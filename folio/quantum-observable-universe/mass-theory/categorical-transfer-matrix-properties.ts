import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-transfer-matrix-properties",
  interprets: "def:categorical-transfer-matrix",
  title:
    "Configuration space, bi-filtration, and categorification of $\\mathcal{T}(\\mathfrak{H})$",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding", "configuration-space",
    "interaction-filtration",
  ],
  uses: [
    "def:categorical-transfer-matrix",
    "def:hadron",
    "def:localized-hadron",
    "def:exceptional-divisor",
    "rem:knot-factorization",
    "def:vertex-operator",
    "rem:observation-braid",
    "prop:jet-prolongation",
    "rem:jet-planck-steps",
    "def:bundle-initial-conditions",
    "def:operational-entropy",
    "thm:markov-trace-product",
    "conj:crystal-graph-realization",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The information-theoretic\ncontent of a hadron is the balance between these two: $\\eta_q$\n$q$-bits of information per step\n([operational entropy](#def:operational-entropy)) measures the net\nrate at which the ascending tower outruns the descending constraints." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([bundle initial conditions](#def:bundle-initial-conditions))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([jet-Planck steps](#rem:jet-planck-steps))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([observation braid](#rem:observation-braid))" },
  ],
  cites: [
    "brundankleshchev2009",
  ],
});
