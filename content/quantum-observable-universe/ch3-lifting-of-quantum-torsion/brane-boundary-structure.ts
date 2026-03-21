import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brane-boundary",
  title: "Structure of the defining boundary",
  tags: ["brane-boundary", "codimension", "blow-up", "chirality"],
  uses: [
    "def:brane-boundary",
    "def:descent-involution",
    "def:quantum-characteristic-classes",
    "lem:descent",
  ],
  proofs: ["prf:brane-boundary"],
});
