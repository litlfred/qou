import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-lp",
  lean: {
    decl: "QOU.ParticleInteractions.confinement_lp",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  title:
    "Confinement as linear program over the Hecke normal form basis",
  tags: [
    "linear-programming",
    "optimization",
    "confinement",
    "frobenius-dual",
    "gram-matrix",
    "minimum-action",
    "lp-duality",
  ],
  uses: [
    "prop:confinement-operator-selection",
    "prop:frobenius-gram-matrix",
    "prop:knot-operator-selection",
  ],
});
