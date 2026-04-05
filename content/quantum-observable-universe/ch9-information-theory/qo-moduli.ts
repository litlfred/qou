import { definition } from "../../schema/builders";

export default definition({
  label: "def:qo-moduli",
  lean: { decl: "QOU.MotivicIntegration.QuantumObservable", validation: "not_checked" },
  title: "Moduli of quantum observables",
  uses: [
    "def:q-categorical-language",
    "def:quantum-universe",
  ],
  tags: ["motivic-integration", "moduli", "quantum-observable"],
});
