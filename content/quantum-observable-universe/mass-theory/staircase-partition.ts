import { definition } from "../../schema/builders";

export default definition({
  label: "def:staircase-partition",
  title: "Staircase partition $\\rho_k = (k, k-1, \\ldots, 1)$",
  lean: {
    ref: "qou:QOU.Hecke.staircasePartition",
    validation: "not_checked",
  },
  uses: [],
  tags: [
    "staircase-partition",
    "young-diagram",
    "self-conjugate",
    "hecke-algebra",
    "specht-module",
    "ew-residual",
  ],
});
