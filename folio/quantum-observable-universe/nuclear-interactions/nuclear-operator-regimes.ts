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
  lean: { ref: "qou:QOU.Interactions.nuclearOperatorRegimes",
    validation: "not_checked",
  },
  uses: [
    "prop:demand-stability",
  ],
});
