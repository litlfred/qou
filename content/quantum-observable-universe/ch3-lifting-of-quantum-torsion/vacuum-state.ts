import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vacuum-state",
  title: "Existence and Uniqueness of the Vacuum State",
  tags: ["vacuum-state", "invariant", "frobenius-trace"],
  lean: {
    decl: "QOU.Torsion.invariant_functional_unique",
    validation: "not_checked",
  },
  status: "has_sorry",
  uses: [
    "def:quantum-observable-universe",
    "def:direct-limit-algebra",
    "def:quantum-gauge-group",
    "lem:descent",
  ],
  proofs: ["prf:vacuum-state"],
});
