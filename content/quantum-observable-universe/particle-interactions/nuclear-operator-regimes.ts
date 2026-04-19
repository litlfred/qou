import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-operator-regimes",
  title:
    "Three operator regimes for nuclear binding",
  tags: [
    "nuclear-binding",
    "operator-selection",
    "magic-numbers",
    "torus-knot",
    "hopf-link",
    "shell-closure",
    "regime-transition",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.nuclearOperatorRegimes",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-operator-selection",
    "prop:demand-stability",
    "def:derived-atom",
    "prop:torus-knot-shell-binding",
  ],
});
