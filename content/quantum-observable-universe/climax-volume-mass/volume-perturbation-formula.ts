import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:volume-perturbation-formula",
  title: "Volume perturbation: $\\delta\\Phi_k = z^2 \\cdot \\mathrm{Vol}(4_1) \\cdot [k{-}3]_q$",
  lean: { ref: "qou:QOU.BraidKnot.volume_perturbation", validation: "not_checked" },
  uses: ["thm:topological-mass", "prop:topological-mass-formula", "prop:hecke-convergence-bound"],
  tags: ["volume-perturbation", "figure-eight", "markov-parameter", "jet-level"],
});
