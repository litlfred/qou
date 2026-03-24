import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brane-boundary",
  lean: {
    decl: "QOU.Torsion.brane_boundary_structure",
    validation: "not_checked",
  },
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
