import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-characteristic-classes-unique",
  title: "Uniqueness of quantum characteristic classes",
  lean: { ref: "qou:QOU.QuantumCharClasses.unique",
    validation: "not_checked",
  },
  uses: ["prop:quantum-characteristic-classes-exists"],
  proofs: ["prf:quantum-characteristic-classes-unique"],
  tags: ["uniqueness", "characteristic-classes", "cohomology"],
});
