import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descent-eigenspaces",
  title: "Eigenspaces of the descent involution",
  hasProof: true,
  tags: ["descent", "eigenspace", "bosonic", "fermionic"],
  uses: [
    "def:descent-involution",
    "rem:algebraic-filter",
    "rem:weight-space-decomposition",
    "lem:descent",
  ],
});
