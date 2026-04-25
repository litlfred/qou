import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vacuum-state",
  title: "Existence and Uniqueness of the Vacuum State",
  tags: ["vacuum-state", "invariant", "frobenius-trace"],
  lean: { ref: "qou:QOU.Torsion.invariant_functional_unique",
    validation: "not_checked",
  },
  uses: [
    "def:direct-limit-algebra",
    "def:quantum-gauge-group",
    "lem:descent",
  ],
  proofs: ["prf:vacuum-state"],
});
