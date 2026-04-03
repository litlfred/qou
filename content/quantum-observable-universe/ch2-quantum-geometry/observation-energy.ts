import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:observation-energy",
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
