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
  lean: {
    decl: "QOU.Torsion.torus_knot_generators_finite",
    validation: "not_checked",
  },
  uses: [
    "def:knot-particle-generation",
    "def:hadron",
    "prop:skein-generation",
    "prop:euler-char-stability",
    "rem:knot-particle-dictionary",
    "def:recursive-brane-tower",
  ],
  proofs: ["prf:torus-knot-generators"],
});
