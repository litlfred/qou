import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "caveat", date: "2026-11-16", body: "**Demoted to conjecture (owner, 2026-11-16).** The predicted $193\\text{--}386$ kJ/mol uses a molecular energy quantum $|q+q^{-1}|_{\\mathrm{mol}} \\sim 1\\text{--}2$ eV that is chosen, not derived from $q_0$. The agreement with the observed $200\\text{--}400$ kJ/mol is therefore a calibrated comparison, not a parameter-free prediction. The cited Lean lemma `benzene_weights` checks only the integer arithmetic $6-1=5$, $6/2=3$, $5-3=2$." },
  ],
  label: "conj:chain-ring-comparison",
  title:
    "Predicted vs. observed $\\mathrm{C}_6$ ring-closure barrier",
  tags: [
    "comparison",
    "experimental",
    "theoretical",
    "activation-energy",
    "benzene",
    "carbyne",
    "ring-closure",
    "substrate-parameter",
  ],
  lean: { ref: "qou:QOU.Organic.benzene_weights",
    validation: "not_checked",
  },
  uses: ["rem:chain-ring-energy"],
});
