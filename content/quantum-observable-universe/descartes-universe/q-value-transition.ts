import { definition } from "../../schema/builders";

export default definition({
  label: "def:Q-value-transition",
  title:
    "$\\mathcal{Q}_q$-Value as Categorical Action Difference",
  tags: [
    "q-value",
    "transition-energy",
    "beta-decay",
    "crossing-change",
    "recoil",
    "kinetic-energy",
    "skein",
  ],
  lean: { ref: "qou:QOU.Descartes.QValueTransition",
    validation: "not_checked",
  },
  uses: [
    "def:q-energy",
    "thm:parity-regime-selection",
  ],
});
