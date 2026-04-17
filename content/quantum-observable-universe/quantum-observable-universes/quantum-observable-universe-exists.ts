import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-observable-universe-exists",
  title: "Existence of quantum observable universes",
  lean: {
    decl: "QOU.QuantumObservableUniverse.exists_instance",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:quantum-universe",
    "ex:qou-su2",
  ],
  proofs: ["prf:quantum-observable-universe-exists"],
  tags: ["existence", "quantum-observable-universe"],
});
