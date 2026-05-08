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
    script: "folio-assistant/computations/hadron_knot_table.py",
    witness: "folio-assistant/computations/hadron-knot-table.witness.json",
    status: "verified",
  },
});
