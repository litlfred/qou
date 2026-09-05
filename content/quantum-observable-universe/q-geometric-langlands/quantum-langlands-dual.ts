import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:quantum-langlands-dual",
  title:
    "Quantum Langlands duality — $H_n(q)$ ↔ $H_n(q^{-1})$ via Cartan folding (Type $A_{n-1}$ ↔ ${}^L\\!A_{n-1}$)",
  lean: {
    ref: "qou:QOU.Conjectures.QuantumLanglandsDual",
    validation: "not_checked",
  },
  uses: [
    "conj:type-b-folding-cpt",
    "conj:reverse-limit-q-to-infinity",
  ],
  cites: [
    "macdonald1971",
    "lusztig1989",
    "frenkel-reshetikhin1998",
  ],
  tags: [
    "langlands-dual",
    "duality-d19",
    "quantum-langlands",
    "cartan-folding",
    "research-grade",
    "axiom-class",
    "open-problem",
  ],
});
