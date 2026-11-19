import { remark } from "../../schema/builders";

export default remark({
  label: "rem:periodic-table-demand",
  interprets: "prop:demand-stability",
  title:
    "The valley of stability is the demand-minimizing locus in $(Z, N)$-space",
  lean: {
    ref: "qou:QOU.Nuclear.PeriodicTableDemand",
    validation: "leanok",
  },
  tags: [
    "periodic-table",
    "valley-of-stability",
    "demand",
    "magic-numbers",
    "conjecture",
    "nuclear-physics",
  ],
  uses: ["prop:demand-stability"],
});
