import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quark-level-knot-table",
  title:
    "Quark-level knot decomposition table for nucleons and light atoms",
  tags: [
    "hecke",
    "normal-form",
    "quark",
    "knot-table",
    "appendix",
    "witness",
  ],
  uses: [
    "rem:particle-nf-table",
    "def:hecke-normal-form",
    "rem:knot-particle-dictionary",
  ],
  interprets: "rem:particle-nf-table",
  computation: {
    engine: "python",
    script: "computations/quark-level-knot-table.py",
    witness: "computations/quark-level-knot-table.witness.json",
    status: "verified",
  },
});
