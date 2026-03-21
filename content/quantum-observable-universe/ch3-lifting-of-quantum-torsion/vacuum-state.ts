import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vacuum-state",
  title: "Existence and Uniqueness of the Vacuum State",
  hasProof: true,
  tags: ["vacuum-state", "invariant", "haar-measure"],
  uses: [
    "def:quantum-observable-universe",
    "def:direct-limit-algebra",
    "def:quantum-gauge-group",
    "lem:descent",
  ],
});
