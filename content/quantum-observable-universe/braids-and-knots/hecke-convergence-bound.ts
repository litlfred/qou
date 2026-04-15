import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-convergence-bound",
  title: "Hecke convergence bound: $\\mathrm{MAE}(H_k) \\leq C \\cdot r^{-(k-3)}$",
  lean: { decl: "QOU.BraidKnot.hecke_convergence_bound", validation: "not_checked" },
  uses: [
    "thm:wedderburn-mass-formula",
    "prop:wedderburn-trace-identity",
    "prop:q-integer-mass-formula",
  ],
  tags: ["convergence", "hecke-level", "plancherel", "mass-formula"],
});
