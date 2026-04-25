import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-universe-exists",
  title: "Existence of quantum universes",
  lean: { ref: "qou:QOU.QuantumUniverse.exists_instance",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-universe",
    "ex:rigid-monoidal-vect",
  ],
  proofs: ["prf:quantum-universe-exists"],
  tags: ["existence", "quantum-universe"],
});
