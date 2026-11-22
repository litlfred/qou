import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hadron-level-knot-table",
  title:
    "Hadron-level knot decomposition table for nucleons and atoms",
  tags: [
    "hecke",
    "normal-form",
    "hadron",
    "knot-table",
    "appendix",
    "witness",
  ],
  uses: ["rem:particle-nf-table"],
  interprets: "rem:particle-nf-table",
  computation: {
    engine: "python",
    script: "computations/hadron_knot_table.py",
    witness: "computations/hadron-knot-table.witness.json",
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (LP_stable(c14)). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The NF coefficients for each atom (6 values) are in the computation witness `hadron-knot-table.witness.json`." },
  ],
});
