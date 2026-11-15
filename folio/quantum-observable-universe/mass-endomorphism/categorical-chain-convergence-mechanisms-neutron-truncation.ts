import { remark } from "../../schema/builders";

/**
 * Moved out of prop:categorical-chain-convergence-mechanisms on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:categorical-chain-convergence-mechanisms-neutron-truncation",
  title: "Truncation depth needed for free-neutron $\\beta$-decay at 1 ppb",
  interprets: "prop:categorical-chain-convergence-mechanisms",
  uses: ["prop:categorical-chain-convergence-mechanisms"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:categorical-chain-convergence-mechanisms` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["q-beta", "truncation", "comparison-with-measurement"],
});
