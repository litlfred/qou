import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:wenzl-qmn-synergy",
  title:
    "Wenzl-bridge + q-Murnaghan-Nakayama synergy: $\\mathrm{tr}_M$ on canonical braids in $O(p(n)(\\max\\text{hooks} + n^2))$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.wenzl_qmn_synergy",
    validation: "not_checked",
  },
  uses: ["prop:y-lambda-recipe-from-partition"],
  cites: ["wenzl1988", "halverson_ram_1998", "ram1991"],
  tags: [
    "wenzl-bridge",
    "q-murnaghan-nakayama",
    "markov-trace",
    "compute-speedup",
    "atom-knot-id",
    "synergy",
  ],
});
