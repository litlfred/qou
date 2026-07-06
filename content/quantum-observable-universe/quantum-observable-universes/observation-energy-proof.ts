import { proof } from "../../schema/builders";

export default proof({
  label: "prf:observation-energy",
  title: "Proof of Observation increases quantum energy and deforms the action",
  of: "prop:observation-energy",
  uses: [
    "def:observation",
    "def:quantum-planck-constant",
    "def:categorical-action",
  ],
});
