import { remark } from "../../schema/builders";

/**
 * Moved out of prop:mass-endomorphism-tower on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:mass-endomorphism-tower-phi-q-history",
  title: "Why $\\mathrm{Li}_2^q$ replaced the Faddeev $\\Phi_q$ form in the mass tower",
  interprets: "prop:mass-endomorphism-tower",
  uses: ["prop:mass-endomorphism-tower"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:mass-endomorphism-tower` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["mass-tower", "dilogarithm", "comparison-with-measurement"],
});
