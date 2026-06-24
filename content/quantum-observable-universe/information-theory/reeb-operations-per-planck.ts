import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-operations-per-planck",
  proofs: ["prf:reeb-operations-per-planck"],
  lean: { ref: "qou:QOU.Information.reeb_operations_per_planck", validation: "not_checked" },
  title: "Discrete iterations per Reeb circuit",
  tags: [
    "planck-time",
    "reeb-flow",
    "julia-set",
    "discrete-time",
    "information-theory",
  ],
  uses: [
    "def:planck-time",
    "rem:discrete-planck-step",
  ],
});
