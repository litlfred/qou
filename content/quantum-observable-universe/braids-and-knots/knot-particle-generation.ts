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
  lean: { ref: "qou:QOU.Torsion.KnotParticleGeneration",
    validation: "not_checked",
  },
  uses: [
    "prop:skein-generation",
    "rem:knot-particle-dictionary",
    "rem:color-tube-interpretation",
  ],
});
