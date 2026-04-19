import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-tower-convergence",
  title:
    "Geometric-series tail bound for the $\\hbar_q^2$ brane-tower sum",
  lean: {
    decl: "QOU.MassEndomorphism.jet_tower_tail_bound",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-endomorphism-tower",
    "rem:mass-endomorphism-jet-tower",
    "def:recursive-brane-tower",
  ],
  cites: ["leitner2026"],
});
