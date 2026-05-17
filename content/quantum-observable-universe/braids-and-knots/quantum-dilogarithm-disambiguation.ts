import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-dilogarithm-disambiguation",
  title:
    "Quantum dilogarithm disambiguation: $\\Phi_q$ (product form) vs $-\\mathrm{Li}_2^q(-z)$ (Kashaev integration limit)",
  lean: {
    ref: "qou:QOU.BraidKnot.QuantumDilogarithm",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-endomorphism-tower",
  ],
  cites: [],
  tags: [
    "quantum-dilogarithm",
    "kashaev-limit",
    "anti-regression",
    "li2q",
    "phi_q",
    "disambiguation",
    "structural-discipline",
  ],
});
