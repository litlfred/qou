import { definition } from "../../schema/builders";

export default definition({
  label: "def:knot-particle-generation",
  title: "Knot-particle generation from $T_{m,n}$ torus knot generators",
  tags: [
    "knot",
    "particle",
    "generation",
    "torus-knot",
    "hopf-link",
    "color-tube",
    "skein",
    "exceptional-divisor",
  ],
  lean: {
    decl: "QOU.Torsion.KnotParticleGeneration",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "rem:hadron-operations",
    "prop:skein-generation",
    "rem:knot-particle-dictionary",
    "def:localized-knot",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "def:color-tube-coordinates",
    "rem:color-tube-interpretation",
  ],
});
