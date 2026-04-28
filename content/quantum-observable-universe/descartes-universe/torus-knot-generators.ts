import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-generators",
  title: "Finiteness of the $T_{m,n}$ generator set",
  tags: [
    "torus-knot",
    "generator",
    "euler-characteristic",
    "genus",
    "finiteness",
  ],
  lean: { ref: "qou:QOU.Torsion.torus_knot_generators_finite",
    validation: "not_checked",
  },
  uses: [
    "def:knot-particle-generation",
    "prop:euler-char-stability",
    "prop:s5-equivariant-torus-knots",
  ],
  proofs: ["prf:torus-knot-generators"],
});
