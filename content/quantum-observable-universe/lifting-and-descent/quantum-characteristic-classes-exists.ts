import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-characteristic-classes-exists",
  title: "Well-definedness of quantum characteristic classes",
  lean: { ref: "qou:QOU.QuantumCharClasses.exists",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-characteristic-classes",
    "def:recursive-brane-tower",
    "prop:jet-prolongation",
  ],
  proofs: ["prf:quantum-characteristic-classes-exists"],
  tags: ["existence", "characteristic-classes", "cohomology"],
});
