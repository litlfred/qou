import { remark } from "../../schema/builders";

/**
 * Moved out of prop:q-beta-over-e0-classical-vanishing on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:q-beta-over-e0-classical-vanishing-ladder-reading",
  title: "What the vanishing $S(1) = 0$ means for the $c_k$ ladder",
  interprets: "prop:q-beta-over-e0-classical-vanishing",
  uses: ["prop:q-beta-over-e0-classical-vanishing"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:q-beta-over-e0-classical-vanishing` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["q-beta", "c-k-ladder", "comparison-with-measurement"],
});
