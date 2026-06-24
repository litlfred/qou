import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-tower-convergence",
  proofs: ["prf:jet-tower-convergence"],
  title:
    "Geometric-series tail bound for the $\\hbar_q^2$ brane-tower sum",
  lean: { ref: "qou:QOU.MassEndomorphism.jet_tower_tail_bound",
    validation: "not_checked",
  },
  uses: ["prop:confinement-sdp"],
  cites: ["leitner2026"],
});
