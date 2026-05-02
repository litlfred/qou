import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-from-iterative-brane-tower",
  title:
    "Proposition 6. Magic ladder emerges iteratively from the brane tower at $q_0$",
  lean: {
    ref: "qou:QOU.LiftingDescent.IterativeBraneTower.MagicEmergesIteratively",
    validation: "not_checked",
  },
  uses: [
    "def:recursive-brane-tower",
    "prop:jet-prolongation",
    "prop:categorical-jet-prolongation",
    "conj:homological-shell-condensation",
    "conj:sdp-rank-collapse-magic-shell",
    "prop:hoefsmit-seminormal-form",
    "prop:magic-numbers-from-q",
    "def:q-pochhammer-partial-product",
  ],
  cites: [
    "yekutieli2010",
    "yekutieli2008",
    "mathas1999",
    "hoefsmit1974",
  ],
  tags: [
    "brane-tower",
    "iterative",
    "yekutieli-jet",
    "magic-numbers",
    "shell-condensation",
    "compute-tricks",
    "open-problem",
    "axiom-class",
  ],
});
