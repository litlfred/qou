import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:observation-energy",
  lean: {
    decl: "QOU.QuantumObservableUniverses.observation_energy",
    file: "QOU/QuantumObservableUniverses.lean",
    validation: "not_checked",
  },
  title:
    "Observation increases quantum energy and deforms the action",
  tags: [
    "observation",
    "energy",
    "substrate-perturbation",
    "action",
    "intent",
  ],
  uses: [
    "def:observation",
    "def:quantum-planck-constant",
    "def:categorical-action",
  ],
});
