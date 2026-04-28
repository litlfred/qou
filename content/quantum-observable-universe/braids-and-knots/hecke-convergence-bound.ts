import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-convergence-bound",
  title: "Hecke convergence bound: $\\mathrm{MAE}(H_k) \\leq C \\cdot r^{-(k-3)}$",
  lean: { ref: "qou:QOU.BraidKnot.hecke_convergence_bound", validation: "not_checked" },
  uses: ["rem:body-asymptotics-catalog"],
  tags: ["convergence", "hecke-level", "plancherel", "mass-formula"],
});
