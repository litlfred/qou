import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-01",
      body:
        "Promoted from claim 3 of [`prop:crossing-energy-decomposition`](#prop:crossing-energy-decomposition) to a standalone proposition, since the Lean sibling `pair_cancellation` proves it directly and it is the statement downstream blocks actually cite. Lean sibling is the archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c); the underlying combinatorial content is generic to any commutative ring carrying the same $q$-data.",
      see: "docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md",
    },
  ],
  label: "prop:crossing-energy-pair-cancellation",
  lean: { ref: "qou:QOU.Braiding.pair_cancellation" },
  title: "Mirror pairing cancels the symmetric channel",
  uses: [
    "prop:crossing-energy-decomposition",
    "def:crossing-energy",
  ],
  examples: ["rem:pair-creation-energy"],
  tags: [
    "crossing-energy",
    "pair-creation",
    "mirror",
    "coulomb",
    "antisymmetric",
  ],
});
