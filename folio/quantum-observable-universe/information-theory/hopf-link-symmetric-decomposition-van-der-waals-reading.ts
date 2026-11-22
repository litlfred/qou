import { remark } from "../../schema/builders";

/**
 * Moved out of prop:hopf-link-symmetric-decomposition on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:hopf-link-symmetric-decomposition-van-der-waals-reading",
  title: "Hopf-element split at $q_0$ and the van der Waals reading",
  interprets: "prop:hopf-link-symmetric-decomposition",
  uses: ["prop:hopf-link-symmetric-decomposition"],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/hbond_vdw_sdp.py",
    witness: ["computations/hbond-vdw-sdp.witness.json"],
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:hopf-link-symmetric-decomposition` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["hopf-link", "van-der-waals", "comparison-with-measurement"],
});
