import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:parity-regime-selection",
  title:
    "Parity regime selection for Q-values",
  tags: [
    "parity",
    "regime-selection",
    "sign",
    "odd-even",
    "q-value",
    "mass-number",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.parity_regime_selection",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  uses: [
    "prop:branching-qvalue-factorization",
    "prop:confinement-lp",
  ],
});
