import { remark } from "../../schema/builders";

/**
 * Moved out of prop:q-beta-c-k-leading-bias-correction-identity on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:q-beta-c-k-leading-bias-correction-identity-extraction-check",
  title: "Bias correction applied to the extracted $\\hat c_2$ and $\\hat c_3$",
  interprets: "prop:q-beta-c-k-leading-bias-correction-identity",
  uses: ["prop:q-beta-c-k-leading-bias-correction-identity"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The proposition mechanically inverts the bias in Lean." },
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:q-beta-c-k-leading-bias-correction-identity` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["q-beta", "c-k-ladder", "extraction", "comparison-with-measurement"],
});
